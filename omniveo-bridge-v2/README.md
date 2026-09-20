# OmniVeo Bridge 2.0

A private, multi-account Google Workspace MCP gateway for your agents.

Bridge is **not an email client**. It is a permissioned access layer between your agents and your Google accounts:

```
Google accounts -> OmniVeo Bridge -> agent policy -> MCP tools
```

## What this MVP does

- Connect any number of personal Gmail / Google accounts, one at a time.
- Authenticate each Google account once using OAuth offline access.
- Store Google refresh/access tokens encrypted at rest with AES-256-GCM.
- Expose Gmail, Calendar, and Drive through MCP.
- Give each agent its own bearer token and capability list.
- Separate read grants from write grants.
- Keep an append-only local audit log of agent actions.
- Never expose Google refresh tokens to an MCP client.

### MCP tools

| Tool | Capability |
|---|---|
| `accounts_list` | `accounts.read` |
| `gmail_search` | `gmail.read` |
| `gmail_get_thread` | `gmail.read` |
| `gmail_send` | `gmail.write` |
| `calendar_list_events` | `calendar.read` |
| `calendar_create_event` | `calendar.write` |
| `drive_search` | `drive.read` |
| `drive_get_text` | `drive.read` |

## Security model

1. Google credentials live only inside Bridge.
2. OAuth tokens are encrypted before writing to disk.
3. Each agent has a different Bridge bearer token.
4. Every MCP tool checks a capability before touching Google.
5. Writes are denied unless that agent is explicitly granted a write capability.
6. Audit entries are written to `data/audit.jsonl`.

For an automation such as an inbox monitor, give it only:

```json
["accounts.read", "gmail.read"]
```

That automation can inspect mail but cannot send, archive, delete, change calendars, or read Drive.

## Google Cloud setup

Create one Google Cloud project and enable:

- Gmail API
- Google Calendar API
- Google Drive API

Create an **OAuth 2.0 Web application** client and add this redirect URI:

```
http://127.0.0.1:8787/oauth/google/callback
```

For personal Gmail accounts, set the OAuth audience to External and add the accounts you want to connect while developing.

**Important:** Google's Testing publishing state issues time-limited refresh tokens (commonly 7 days). If you want the "authenticate once" behavior, move the OAuth app to **In production** after configuration. You are still in control of which accounts you authorize.

Bridge requests these Google scopes:

- `openid email profile`
- `gmail.modify`
- `gmail.send`
- `calendar.events`
- `calendar.calendarlist.readonly`
- `drive.readonly`

Bridge's own policy layer can still give an agent read-only access even though the owner has authorized the Google connection for broader capabilities.

## Install

Requires Node.js 20+.

```bash
cd omniveo-bridge-v2
cp .env.example .env
npm install
```

Generate secrets:

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('base64'))"
node -e "console.log(require('crypto').randomBytes(32).toString('base64url'))"
```

Put the first output in `BRIDGE_ENCRYPTION_KEY` and use fresh random outputs for `BRIDGE_OWNER_TOKEN` and each agent token.

Example agent policy:

```env
BRIDGE_AGENTS_JSON={"chatgpt":{"token":"LONG_RANDOM_TOKEN_1","scopes":["accounts.read","gmail.read","calendar.read","drive.read"]},"email-monitor":{"token":"LONG_RANDOM_TOKEN_2","scopes":["accounts.read","gmail.read"]}}
```

## Run

```bash
npm run selftest
npm run typecheck
npm start
```

By default Bridge binds to `127.0.0.1:8787` so it is not exposed to your network.

## Connect Google accounts

With Bridge running, open:

```
http://127.0.0.1:8787/oauth/google/start?alias=personal
```

Complete Google's consent flow.

Connect another account:

```
http://127.0.0.1:8787/oauth/google/start?alias=omniveo
```

And another:

```
http://127.0.0.1:8787/oauth/google/start?alias=other
```

You only repeat OAuth when connecting a new Google account, changing requested Google scopes, revoking Bridge from the Google account, or if Google invalidates the refresh token.

## MCP endpoint

```
http://127.0.0.1:8787/mcp
```

Clients send their Bridge token as:

```
Authorization: Bearer <AGENT_TOKEN>
```

The server uses the current MCP TypeScript SDK Streamable HTTP handler.

## Inspect connected accounts

Owner-only:

```bash
curl -H "Authorization: Bearer $BRIDGE_OWNER_TOKEN" \
  http://127.0.0.1:8787/admin/accounts
```

Tokens are intentionally omitted from this response.

## Remote deployment

Do **not** expose the development HTTP server directly to the public internet.

For remote agents:

1. Put Bridge behind HTTPS.
2. Set `HOST` to the real hostname / deployment binding.
3. Store `.env` secrets in the hosting platform's secret manager.
4. Persist `DATA_DIR` on encrypted durable storage.
5. Keep a unique bearer token per agent/automation.
6. Rotate an agent token immediately if it leaks.

For a production deployment with multiple instances, replace the encrypted file store with Postgres/KMS or an equivalent managed secret store.

## Current boundary

This first version deliberately does not let an agent grant itself new permissions. Permission expansion is an owner/admin action by design.

A future version can add an approval queue so an agent can request a one-time write permission and you can approve it from a small owner UI.
