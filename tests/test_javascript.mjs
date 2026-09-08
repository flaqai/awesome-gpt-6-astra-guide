import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';

const script = new URL('../examples/quickstart.mjs', import.meta.url);
function run(code, args = [], key = '') {
  return spawnSync(process.execPath, ['--input-type=module', '-e', code, '--', ...args], {
    encoding: 'utf8', env: { ...process.env, OPENAI_API_KEY: key },
  });
}
const load = `await import(${JSON.stringify(script.href)});`;

test('dry run requires no key and no network', () => {
  const r = run(`globalThis.fetch=()=>{throw new Error('unexpected network')}; ${load}`, ['--dry-run']);
  assert.equal(r.status, 0);
  assert.equal(JSON.parse(r.stdout).model, 'gpt-6-astra');
});
test('missing key fails without network', () => {
  const r = run(`globalThis.fetch=()=>{throw new Error('unexpected network')}; ${load}`);
  assert.equal(r.status, 1);
  assert.match(r.stderr, /OPENAI_API_KEY/);
});
test('mock success prints only message text', () => {
  const body = {status:'completed', output:[{type:'reasoning'}, {type:'message',content:[{type:'output_text',text:'中文结果'}]}]};
  const r = run(`globalThis.fetch=async()=>({ok:true,json:async()=>(${JSON.stringify(body)})}); ${load}`, [], 'test-placeholder');
  assert.equal(r.status, 0);
  assert.match(r.stdout, /中文结果/);
});
test('incomplete response exits with error', () => {
  const r = run(`globalThis.fetch=async()=>({ok:true,json:async()=>({status:'incomplete',incomplete_details:{reason:'max_output_tokens'}})}); ${load}`, [], 'test-placeholder');
  assert.equal(r.status, 1);
  assert.match(r.stderr, /max_output_tokens/);
});
test('HTTP failure exits with error', () => {
  const r = run(`globalThis.fetch=async()=>({ok:false,status:429}); ${load}`, [], 'test-placeholder');
  assert.equal(r.status, 1);
  assert.match(r.stderr, /429/);
});

test('original release evidence identifies both failures in the request', () => {
  const r = run(`globalThis.fetch=()=>{throw new Error('unexpected network')}; ${load}`, ['--dry-run']);
  assert.equal(r.status, 0);
  const input = JSON.parse(r.stdout).input;
  const evidence = JSON.parse(input.slice(input.indexOf('\n') + 1));
  assert.equal(evidence.mode, 'offline_fixture');
  assert.equal(evidence.project, 'Paper Circuit Studio');
  assert.deepEqual(evidence.checks.filter(x => !x.passed).map(x => x.id), ['R02', 'R03']);
});
