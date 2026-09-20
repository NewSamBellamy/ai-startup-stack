import path from 'node:path';

function required(name: string): string {
  const value = process.env[name]?.trim();
  if (!value) throw new Error(`Missing required environment variable: ${name}`);
  return value;
}

export type AgentConfig = {
  token: string;
  scopes: string[];
};

export function loadConfig() {
  const key = Buffer.from(required('BRIDGE_ENCRYPTION_KEY'), 'base64');
  if (key.length !== 32) throw new Error('BRIDGE_ENCRYPTION_KEY must decode to exactly 32 bytes.');

  let agents: Record<string, AgentConfig> = {};
  const rawAgents = process.env.BRIDGE_AGENTS_JSON?.trim();
  if (rawAgents) {
    agents = JSON.parse(rawAgents) as Record<string, AgentConfig>;
  }

  return {
    googleClientId: required('GOOGLE_CLIENT_ID'),
    googleClientSecret: required('GOOGLE_CLIENT_SECRET'),
    googleRedirectUri: process.env.GOOGLE_REDIRECT_URI?.trim() || 'http://127.0.0.1:8787/oauth/google/callback',
    encryptionKey: key,
    ownerToken: required('BRIDGE_OWNER_TOKEN'),
    agents,
    port: Number(process.env.PORT || '8787'),
    host: process.env.HOST || '127.0.0.1',
    dataDir: path.resolve(process.env.DATA_DIR || './data')
  };
}

export type BridgeConfig = ReturnType<typeof loadConfig>;
