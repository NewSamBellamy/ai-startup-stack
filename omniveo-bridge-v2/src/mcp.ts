import { McpServer } from '@modelcontextprotocol/server';
import * as z from 'zod/v4';
import type { BridgeConfig } from './config.js';
import type { TokenStore } from './store.js';
import { assertCan, type AgentIdentity } from './policy.js';
import { calendar, drive, gmail, makeRawEmail, summarizeMessage, threadToPlainText } from './google.js';

function text(value: unknown) {
  return { content: [{ type: 'text' as const, text: JSON.stringify(value, null, 2) }] };
}

export function buildMcpServer(config: BridgeConfig, store: TokenStore, agent: AgentIdentity) {
  const server = new McpServer({
    name: 'omniveo-bridge-v2',
    version: '0.1.0'
  });

  server.registerTool('accounts_list', {
    description: 'List Google accounts connected to OmniVeo Bridge. Tokens are never exposed.',
    inputSchema: z.object({})
  }, async () => {
    assertCan(agent, 'accounts.read');
    await store.audit({ agent: agent.id, tool: 'accounts_list' });
    return text(await store.list());
  });

  server.registerTool('gmail_search', {
    description: 'Search Gmail in one connected account using Gmail search syntax.',
    inputSchema: z.object({
      account: z.string(),
      query: z.string(),
      maxResults: z.number().int().min(1).max(100).default(20)
    })
  }, async ({ account, query, maxResults }) => {
    assertCan(agent, 'gmail.read');
    const api = await gmail(config, store, account);
    const list = await api.users.messages.list({ userId: 'me', q: query, maxResults });
    const ids = list.data.messages || [];
    const messages = await Promise.all(ids.map(async m => {
      const got = await api.users.messages.get({
        userId: 'me',
        id: m.id!,
        format: 'metadata',
        metadataHeaders: ['From', 'To', 'Subject', 'Date']
      });
      return summarizeMessage(got.data);
    }));
    await store.audit({ agent: agent.id, tool: 'gmail_search', account, query, count: messages.length });
    return text(messages);
  });

  server.registerTool('gmail_get_thread', {
    description: 'Read a Gmail thread as plain text.',
    inputSchema: z.object({ account: z.string(), threadId: z.string() })
  }, async ({ account, threadId }) => {
    assertCan(agent, 'gmail.read');
    const api = await gmail(config, store, account);
    const got = await api.users.threads.get({ userId: 'me', id: threadId, format: 'full' });
    await store.audit({ agent: agent.id, tool: 'gmail_get_thread', account, threadId });
    return text(threadToPlainText(got.data));
  });

  server.registerTool('gmail_send', {
    description: 'Send a plain-text email. This requires the gmail.write grant.',
    inputSchema: z.object({
      account: z.string(),
      to: z.string().email(),
      subject: z.string(),
      body: z.string(),
      threadId: z.string().optional(),
      inReplyTo: z.string().optional()
    })
  }, async ({ account, to, subject, body, threadId, inReplyTo }) => {
    assertCan(agent, 'gmail.write');
    const api = await gmail(config, store, account);
    const sent = await api.users.messages.send({
      userId: 'me',
      requestBody: { raw: makeRawEmail({ to, subject, body, inReplyTo }), threadId }
    });
    await store.audit({ agent: agent.id, tool: 'gmail_send', account, to, subject, messageId: sent.data.id });
    return text({ id: sent.data.id, threadId: sent.data.threadId });
  });

  server.registerTool('calendar_list_events', {
    description: 'List upcoming Google Calendar events.',
    inputSchema: z.object({
      account: z.string(),
      calendarId: z.string().default('primary'),
      timeMin: z.string().datetime().optional(),
      timeMax: z.string().datetime().optional(),
      maxResults: z.number().int().min(1).max(100).default(20)
    })
  }, async ({ account, calendarId, timeMin, timeMax, maxResults }) => {
    assertCan(agent, 'calendar.read');
    const api = await calendar(config, store, account);
    const result = await api.events.list({
      calendarId,
      timeMin: timeMin || new Date().toISOString(),
      timeMax,
      maxResults,
      singleEvents: true,
      orderBy: 'startTime'
    });
    const events = (result.data.items || []).map(e => ({
      id: e.id,
      summary: e.summary,
      description: e.description,
      start: e.start,
      end: e.end,
      attendees: e.attendees?.map(a => ({ email: a.email, responseStatus: a.responseStatus })),
      htmlLink: e.htmlLink
    }));
    await store.audit({ agent: agent.id, tool: 'calendar_list_events', account, count: events.length });
    return text(events);
  });

  server.registerTool('calendar_create_event', {
    description: 'Create a Google Calendar event. Requires calendar.write.',
    inputSchema: z.object({
      account: z.string(),
      calendarId: z.string().default('primary'),
      summary: z.string(),
      description: z.string().optional(),
      start: z.string().datetime(),
      end: z.string().datetime(),
      attendeeEmails: z.array(z.string().email()).optional()
    })
  }, async ({ account, calendarId, summary, description, start, end, attendeeEmails }) => {
    assertCan(agent, 'calendar.write');
    const api = await calendar(config, store, account);
    const result = await api.events.insert({
      calendarId,
      sendUpdates: attendeeEmails?.length ? 'all' : 'none',
      requestBody: {
        summary,
        description,
        start: { dateTime: start },
        end: { dateTime: end },
        attendees: attendeeEmails?.map(email => ({ email }))
      }
    });
    await store.audit({ agent: agent.id, tool: 'calendar_create_event', account, eventId: result.data.id });
    return text({ id: result.data.id, htmlLink: result.data.htmlLink });
  });

  server.registerTool('drive_search', {
    description: 'Search Google Drive files by Drive API query.',
    inputSchema: z.object({
      account: z.string(),
      query: z.string().default('trashed = false'),
      pageSize: z.number().int().min(1).max(100).default(20)
    })
  }, async ({ account, query, pageSize }) => {
    assertCan(agent, 'drive.read');
    const api = await drive(config, store, account);
    const result = await api.files.list({
      q: query,
      pageSize,
      fields: 'files(id,name,mimeType,modifiedTime,webViewLink,owners(displayName,emailAddress))',
      orderBy: 'modifiedTime desc'
    });
    await store.audit({ agent: agent.id, tool: 'drive_search', account, query, count: result.data.files?.length || 0 });
    return text(result.data.files || []);
  });

  server.registerTool('drive_get_text', {
    description: 'Read a Google Doc or text-like Drive file as text.',
    inputSchema: z.object({ account: z.string(), fileId: z.string(), mimeType: z.string() })
  }, async ({ account, fileId, mimeType }) => {
    assertCan(agent, 'drive.read');
    const api = await drive(config, store, account);
    let output = '';
    if (mimeType === 'application/vnd.google-apps.document') {
      const result = await api.files.export({ fileId, mimeType: 'text/plain' }, { responseType: 'text' });
      output = String(result.data);
    } else {
      const result = await api.files.get({ fileId, alt: 'media' }, { responseType: 'text' });
      output = String(result.data);
    }
    await store.audit({ agent: agent.id, tool: 'drive_get_text', account, fileId });
    return { content: [{ type: 'text' as const, text: output.slice(0, 200000) }] };
  });

  return server;
}
