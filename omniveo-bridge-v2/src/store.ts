import fs from 'node:fs/promises';
import path from 'node:path';
import type { Credentials } from 'google-auth-library';
import { decryptJson, encryptJson, type EncryptedPayload } from './crypto.js';

export type StoredGoogleAccount = {
  alias: string;
  email: string;
  tokens: Credentials;
  connectedAt: string;
  scopes: string[];
};

type StoreShape = {
  accounts: StoredGoogleAccount[];
};

export class TokenStore {
  private file: string;
  private auditFile: string;

  constructor(private dataDir: string, private key: Buffer) {
    this.file = path.join(dataDir, 'google-accounts.enc.json');
    this.auditFile = path.join(dataDir, 'audit.jsonl');
  }

  async init() {
    await fs.mkdir(this.dataDir, { recursive: true, mode: 0o700 });
  }

  private async readAll(): Promise<StoreShape> {
    await this.init();
    try {
      const raw = await fs.readFile(this.file, 'utf8');
      return decryptJson<StoreShape>(JSON.parse(raw) as EncryptedPayload, this.key);
    } catch (error: any) {
      if (error?.code === 'ENOENT') return { accounts: [] };
      throw error;
    }
  }

  private async writeAll(data: StoreShape): Promise<void> {
    await this.init();
    const payload = encryptJson(data, this.key);
    const tmp = this.file + '.tmp';
    await fs.writeFile(tmp, JSON.stringify(payload, null, 2), { mode: 0o600 });
    await fs.rename(tmp, this.file);
  }

  async list(): Promise<Array<Omit<StoredGoogleAccount, 'tokens'>>> {
    const data = await this.readAll();
    return data.accounts.map(({ tokens: _tokens, ...safe }) => safe);
  }

  async get(alias: string): Promise<StoredGoogleAccount> {
    const data = await this.readAll();
    const found = data.accounts.find(a => a.alias === alias);
    if (!found) throw new Error(`Unknown Google account alias: ${alias}`);
    return found;
  }

  async upsert(account: StoredGoogleAccount): Promise<void> {
    const data = await this.readAll();
    const i = data.accounts.findIndex(a => a.alias === account.alias);
    if (i >= 0) data.accounts[i] = account;
    else data.accounts.push(account);
    await this.writeAll(data);
  }

  async remove(alias: string): Promise<boolean> {
    const data = await this.readAll();
    const before = data.accounts.length;
    data.accounts = data.accounts.filter(a => a.alias !== alias);
    await this.writeAll(data);
    return data.accounts.length !== before;
  }

  async audit(event: Record<string, unknown>) {
    await this.init();
    const row = JSON.stringify({ at: new Date().toISOString(), ...event }) + '\n';
    await fs.appendFile(this.auditFile, row, { mode: 0o600 });
  }
}
