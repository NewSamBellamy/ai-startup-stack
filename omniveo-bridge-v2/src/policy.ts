export const CAPABILITIES = [
  'accounts.read',
  'gmail.read',
  'gmail.write',
  'calendar.read',
  'calendar.write',
  'drive.read'
] as const;

export type Capability = (typeof CAPABILITIES)[number];

export type AgentIdentity = {
  id: string;
  scopes: string[];
};

export function can(agent: AgentIdentity, capability: Capability): boolean {
  return agent.scopes.includes('*') || agent.scopes.includes(capability);
}

export function assertCan(agent: AgentIdentity, capability: Capability): void {
  if (!can(agent, capability)) {
    throw new Error(`Agent "${agent.id}" is not granted "${capability}".`);
  }
}
