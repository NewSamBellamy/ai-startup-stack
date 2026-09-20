import { google, type gmail_v1, type calendar_v3, type drive_v3 } from 'googleapis';
import type { BridgeConfig } from './config.js';
import type { StoredGoogleAccount, TokenStore } from './store.js';

export const GOOGLE_SCOPES = [
  'openid',
  'email',
  'profile',
  'https://www.googleapis.com/auth/gmail.modify',
  'https://www.googleapis.com/auth/gmail.send',
  'https://www.googleapis.com/auth/calendar.events',
  'https://www.googleapis.com/auth/calendar.calendarlist.readonly',
  'https://www.googleapis.com/auth/drive.readonly'
];

export function makeOAuthClient(config: BridgeConfig) {
  return new google.auth.OAuth2(
    config.googleClientId,
    config.googleClientSecret,
    config.googleRedirectUri
  );
}

export function authorizationUrl(config: BridgeConfig, state: string, loginHint?: string) {
  return makeOAuthClient(config).generateAuthUrl({
    access_type: 'offline',
    include_granted_scopes: true,
    prompt: 'consent',
    scope: GOOGLE_SCOPES,
    state,
    login_hint: loginHint
  });
}

export async function exchangeCode(config: BridgeConfig, code: string) {
  const client = makeOAuthClient(config);
  const { tokens } = await client.getToken(code);
  client.setCredentials(tokens);
  const oauth2 = google.oauth2({ version: 'v2', auth: client });
  const { data } = await oauth2.userinfo.get();
  if (!data.email) throw new Error('Google did not return an email address.');
  return { tokens, email: data.email, scopes: (tokens.scope || '').split(' ').filter(Boolean) };
}

async function authorized(config: BridgeConfig, store: TokenStore, alias: string) {
  const account = await store.get(alias);
  const client = makeOAuthClient(config);
  client.setCredentials(account.tokens);

  client.on('tokens', async tokens => {
    if (!tokens.refresh_token && !tokens.access_token) return;
    const merged: StoredGoogleAccount = {
      ...account,
      tokens: { ...account.tokens, ...tokens }
    };
    await store.upsert(merged);
  });

  return client;
}

export async function gmail(config: BridgeConfig, store: TokenStore, alias: string): Promise<gmail_v1.Gmail> {
  return google.gmail({ version: 'v1', auth: await authorized(config, store, alias) });
}

export async function calendar(config: BridgeConfig, store: TokenStore, alias: string): Promise<calendar_v3.Calendar> {
  return google.calendar({ version: 'v3', auth: await authorized(config, store, alias) });
}

export async function drive(config: BridgeConfig, store: TokenStore, alias: string): Promise<drive_v3.Drive> {
  return google.drive({ version: 'v3', auth: await authorized(config, store, alias) });
}

function header(headers: gmail_v1.Schema$MessagePartHeader[] | undefined, name: string) {
  return headers?.find(h => h.name?.toLowerCase() === name.toLowerCase())?.value || '';
}

export function summarizeMessage(message: gmail_v1.Schema$Message) {
  return {
    id: message.id,
    threadId: message.threadId,
    snippet: message.snippet,
    labelIds: message.labelIds,
    from: header(message.payload?.headers, 'From'),
    to: header(message.payload?.headers, 'To'),
    subject: header(message.payload?.headers, 'Subject'),
    date: header(message.payload?.headers, 'Date')
  };
}

function decodeBody(data?: string | null): string {
  if (!data) return '';
  return Buffer.from(data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8');
}

function collectText(part?: gmail_v1.Schema$MessagePart): string {
  if (!part) return '';
  if (part.mimeType === 'text/plain') return decodeBody(part.body?.data);
  const children = (part.parts || []).map(collectText).filter(Boolean);
  if (children.length) return children.join('\n\n');
  if (part.mimeType === 'text/html') return decodeBody(part.body?.data).replace(/<[^>]+>/g, ' ');
  return '';
}

export function threadToPlainText(thread: gmail_v1.Schema$Thread) {
  return (thread.messages || []).map(message => ({
    ...summarizeMessage(message),
    body: collectText(message.payload)
  }));
}

export function makeRawEmail(input: { to: string; subject: string; body: string; inReplyTo?: string }) {
  const lines = [
    `To: ${input.to}`,
    `Subject: ${input.subject}`,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset="UTF-8"'
  ];
  if (input.inReplyTo) lines.push(`In-Reply-To: ${input.inReplyTo}`, `References: ${input.inReplyTo}`);
  lines.push('', input.body);
  return Buffer.from(lines.join('\r\n'), 'utf8').toString('base64url');
}
