import crypto from 'node:crypto';
import { createMcpExpressApp, requireBearerAuth, type OAuthTokenVerifier } from '@modelcontextprotocol/express';
import { toNodeHandler } from '@modelcontextprotocol/node';
import { createMcpHandler, OAuthError, OAuthErrorCode, type AuthInfo } from '@modelcontextprotocol/server';
import type { Request, Response, NextFunction } from 'express';
import { loadConfig } from './config.js';
import { timingSafeEqualText, randomToken } from './crypto.js';
import { authorizationUrl, exchangeCode } from './google.js';
import { buildMcpServer } from './mcp.js';
import { TokenStore } from './store.js';

const config = loadConfig();
const store = new TokenStore(config.dataDir, config.encryptionKey);
await store.init();

type OAuthState = { alias: string; nonce: string; createdAt: number };
const oauthStates = new Map<string, OAuthState>();

function ownerOnly(req: Request, res: Response, next: NextFunction) {
  const token = req.headers.authorization?.replace(/^Bearer\s+/i, '') || '';
  if (!timingSafeEqualText(token, config.ownerToken)) {
    res.status(401).json({ error: 'owner_unauthorized' });
    return;
  }
  next();
}

function resolveAgent(token: string) {
  for (const [id, entry] of Object.entries(config.agents)) {
    if (timingSafeEqualText(token, entry.token)) return { id, scopes: entry.scopes };
  }
  return null;
}

const verifier: OAuthTokenVerifier = {
  async verifyAccessToken(token: string): Promise<AuthInfo> {
    const agent = resolveAgent(token);
    if (!agent) throw new OAuthError(OAuthErrorCode.InvalidToken, 'Unknown Bridge agent token.');
    return {
      token,
      clientId: agent.id,
      scopes: agent.scopes,
      expiresAt: Math.floor(Date.now() / 1000) + 3600
    };
  }
};

const app = createMcpExpressApp({
  host: config.host,
  allowedHosts: config.host === '127.0.0.1' ? undefined : [config.host]
});

app.get('/health', (_req, res) => {
  res.json({ ok: true, service: 'omniveo-bridge-v2', version: '0.1.0' });
});

app.get('/admin/accounts', ownerOnly, async (_req, res) => {
  res.json(await store.list());
});

app.delete('/admin/accounts/:alias', ownerOnly, async (req, res) => {
  res.json({ removed: await store.remove(req.params.alias) });
});

app.get('/oauth/google/start', (req, res) => {
  const alias = String(req.query.alias || '').trim();
  if (!/^[a-zA-Z0-9._-]{1,64}$/.test(alias)) {
    res.status(400).send('Provide a safe alias, e.g. /oauth/google/start?alias=personal');
    return;
  }
  const state = randomToken(24);
  oauthStates.set(state, { alias, nonce: randomToken(16), createdAt: Date.now() });
  const loginHint = typeof req.query.login_hint === 'string' ? req.query.login_hint : undefined;
  res.redirect(authorizationUrl(config, state, loginHint));
});

app.get('/oauth/google/callback', async (req, res) => {
  try {
    const code = String(req.query.code || '');
    const state = String(req.query.state || '');
    const saved = oauthStates.get(state);
    oauthStates.delete(state);
    if (!saved || Date.now() - saved.createdAt > 10 * 60 * 1000) {
      res.status(400).send('Invalid or expired OAuth state. Start again.');
      return;
    }
    const { tokens, email, scopes } = await exchangeCode(config, code);
    const previous = await store.list();
    if (!tokens.refresh_token) {
      res.status(400).send('Google did not issue a refresh token. Revoke the app in Google Account permissions and connect again.');
      return;
    }
    await store.upsert({
      alias: saved.alias,
      email,
      tokens,
      scopes,
      connectedAt: new Date().toISOString()
    });
    await store.audit({ actor: 'owner', action: 'google_account_connected', alias: saved.alias, email });
    res.type('html').send(`<!doctype html><meta charset="utf-8"><title>OmniVeo Bridge</title><style>body{font:16px system-ui;max-width:640px;margin:80px auto;padding:24px;line-height:1.5}</style><h1>Connected</h1><p><strong>${email}</strong> is now stored under alias <strong>${saved.alias}</strong>.</p><p>You can close this tab and connect another account with a different alias.</p><p>Total accounts: ${previous.length + (previous.some(a => a.alias === saved.alias) ? 0 : 1)}</p>`);
  } catch (error: any) {
    res.status(500).send(`OAuth failed: ${String(error?.message || error)}`);
  }
});

const mcpHandler = createMcpHandler(({ authInfo }) => {
  const id = authInfo?.clientId || 'unknown';
  const entry = config.agents[id];
  if (!entry) throw new Error('Unknown agent.');
  return buildMcpServer(config, store, { id, scopes: entry.scopes });
}, { responseMode: 'json' });

const nodeHandler = toNodeHandler(mcpHandler);
const auth = requireBearerAuth({ verifier });
app.all('/mcp', auth, (req, res) => void nodeHandler(req, res, req.body));

const server = app.listen(config.port, config.host, () => {
  console.error(`OmniVeo Bridge 2.0 listening at http://${config.host}:${config.port}`);
  console.error(`Connect account: http://${config.host}:${config.port}/oauth/google/start?alias=personal`);
});

for (const signal of ['SIGINT', 'SIGTERM'] as const) {
  process.on(signal, async () => {
    await mcpHandler.close();
    server.close(() => process.exit(0));
  });
}
