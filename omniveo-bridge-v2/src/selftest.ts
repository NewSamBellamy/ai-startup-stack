import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import { decryptJson, encryptJson, timingSafeEqualText } from './crypto.js';
import { assertCan, can } from './policy.js';

const key = crypto.randomBytes(32);
const payload = encryptJson({ hello: 'bridge', n: 2 }, key);
assert.deepEqual(decryptJson(payload, key), { hello: 'bridge', n: 2 });
assert.equal(timingSafeEqualText('abc', 'abc'), true);
assert.equal(timingSafeEqualText('abc', 'abd'), false);
assert.equal(can({ id: 'reader', scopes: ['gmail.read'] }, 'gmail.read'), true);
assert.equal(can({ id: 'reader', scopes: ['gmail.read'] }, 'gmail.write'), false);
assert.throws(() => assertCan({ id: 'reader', scopes: ['gmail.read'] }, 'gmail.write'));
console.log('OmniVeo Bridge self-test passed.');
