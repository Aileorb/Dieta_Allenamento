// Di&T – Worker Cloudflare: serve l'app (cartella statica) e manda le notifiche di fine recupero.
// Ogni iPhone ha un id casuale (u) e un proprio Durable Object «Timer», che:
//  - genera e conserva la sua coppia di chiavi VAPID (nessun segreto nel repository pubblico);
//  - salva l'abbonamento push del telefono;
//  - tiene un solo timer alla volta (setAlarm) e allo scadere manda la notifica cifrata (RFC 8291, aes128gcm).
import { DurableObject } from 'cloudflare:workers';

const PUSH_HOSTS = /(^|\.)(push\.apple\.com|fcm\.googleapis\.com|push\.services\.mozilla\.com|notify\.windows\.com|push\.api\.chromium\.org)$/;
const enc = new TextEncoder();
const json = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });

const b64u = buf => { let s = ''; new Uint8Array(buf).forEach(b => { s += String.fromCharCode(b); }); return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); };
const unb64u = str => { const s = atob(str.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((str.length + 3) % 4)); return Uint8Array.from(s, c => c.charCodeAt(0)); };
const cat = (...a) => { const out = new Uint8Array(a.reduce((n, x) => n + x.length, 0)); let o = 0; a.forEach(x => { out.set(x, o); o += x.length; }); return out; };

async function hkdf(salt, ikm, info, len) {
  const k = await crypto.subtle.importKey('raw', ikm, 'HKDF', false, ['deriveBits']);
  return new Uint8Array(await crypto.subtle.deriveBits({ name: 'HKDF', hash: 'SHA-256', salt, info }, k, len * 8));
}

// Cifra il contenuto per un abbonamento (p256dh + auth) – Web Push Message Encryption, un solo record.
export async function encryptPayload(sub, payload) {
  const uaPub = unb64u(sub.keys.p256dh), auth = unb64u(sub.keys.auth);
  const eph = await crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveBits']);
  const asPub = new Uint8Array(await crypto.subtle.exportKey('raw', eph.publicKey));
  const uaKey = await crypto.subtle.importKey('raw', uaPub, { name: 'ECDH', namedCurve: 'P-256' }, false, []);
  const ecdh = new Uint8Array(await crypto.subtle.deriveBits({ name: 'ECDH', public: uaKey }, eph.privateKey, 256));
  const ikm = await hkdf(auth, ecdh, cat(enc.encode('WebPush: info\0'), uaPub, asPub), 32);
  const salt = crypto.getRandomValues(new Uint8Array(16));
  const cek = await hkdf(salt, ikm, enc.encode('Content-Encoding: aes128gcm\0'), 16);
  const nonce = await hkdf(salt, ikm, enc.encode('Content-Encoding: nonce\0'), 12);
  const key = await crypto.subtle.importKey('raw', cek, 'AES-GCM', false, ['encrypt']);
  const ct = new Uint8Array(await crypto.subtle.encrypt({ name: 'AES-GCM', iv: nonce }, key, cat(enc.encode(payload), new Uint8Array([2]))));
  const head = new Uint8Array(21); head.set(salt); new DataView(head.buffer).setUint32(16, 4096); head[20] = 65;
  return cat(head, asPub, ct);
}

async function vapidAuth(endpoint, keys, sub) {
  const aud = new URL(endpoint).origin;
  const h = b64u(enc.encode(JSON.stringify({ typ: 'JWT', alg: 'ES256' })));
  const c = b64u(enc.encode(JSON.stringify({ aud, exp: Math.floor(Date.now() / 1000) + 12 * 3600, sub })));
  const priv = await crypto.subtle.importKey('jwk', keys.priv, { name: 'ECDSA', namedCurve: 'P-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, priv, enc.encode(h + '.' + c));
  return `vapid t=${h}.${c}.${b64u(sig)}, k=${keys.pub}`;
}

export class Timer extends DurableObject {
  async keys() {
    let k = await this.ctx.storage.get('vapid');
    if (!k) {
      const p = await crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify']);
      k = { pub: b64u(await crypto.subtle.exportKey('raw', p.publicKey)), priv: await crypto.subtle.exportKey('jwk', p.privateKey) };
      await this.ctx.storage.put('vapid', k);
    }
    return k;
  }
  async vapid() { return (await this.keys()).pub; }
  async subscribe(sub, site) {
    if (!sub || typeof sub.endpoint !== 'string' || !sub.keys || !sub.keys.p256dh || !sub.keys.auth) return { ok: false, err: 'abbonamento non valido' };
    const u = new URL(sub.endpoint);
    if (u.protocol !== 'https:' || !PUSH_HOSTS.test(u.hostname)) return { ok: false, err: 'servizio push sconosciuto' };
    await this.ctx.storage.put('sub', { endpoint: sub.endpoint, keys: { p256dh: sub.keys.p256dh, auth: sub.keys.auth } });
    await this.ctx.storage.put('site', site);
    return { ok: true };
  }
  async status() { const [s, t] = await Promise.all([this.ctx.storage.get('sub'), this.ctx.storage.get('job')]); return { sub: !!s, job: t || null }; }
  // un solo timer per telefono: un nuovo recupero sostituisce quello vecchio
  async schedule(job) {
    const at = Math.min(Math.max(+job.at || 0, Date.now()), Date.now() + 6 * 3600e3);
    const j = { id: String(job.id || '').slice(0, 64), at, title: String(job.title || 'Di&T').slice(0, 120), body: String(job.body || '').slice(0, 300), tag: String(job.tag || 'recupero').slice(0, 40) };
    await this.ctx.storage.put('job', j);
    await this.ctx.storage.setAlarm(at);
    return { ok: true, at };
  }
  async cancel(id) {
    const j = await this.ctx.storage.get('job');
    if (j && (!id || j.id === id)) { await this.ctx.storage.delete('job'); await this.ctx.storage.deleteAlarm(); return { ok: true, cancelled: true }; }
    return { ok: true, cancelled: false };
  }
  async test() { return this.send({ id: 'test', title: 'Notifiche attive', body: 'Ti avviso così quando finisce il recupero.', tag: 'test' }); }
  async alarm() {
    const j = await this.ctx.storage.get('job'); if (!j) return;
    if (j.at > Date.now() + 500) { await this.ctx.storage.setAlarm(j.at); return; }
    await this.ctx.storage.delete('job');
    await this.send(j);
  }
  async send(j) {
    const sub = await this.ctx.storage.get('sub'); if (!sub) return { ok: false, err: 'nessun abbonamento' };
    const keys = await this.keys(), site = (await this.ctx.storage.get('site')) || 'https://aileorb.github.io/Dieta_Allenamento/';
    const body = await encryptPayload(sub, JSON.stringify({ title: j.title, body: j.body, tag: j.tag, id: j.id, at: j.at || Date.now() }));
    let r;
    try {
      r = await fetch(sub.endpoint, { method: 'POST', body, headers: {
        'content-encoding': 'aes128gcm', 'content-type': 'application/octet-stream', ttl: '120', urgency: 'high', topic: 'recupero',
        authorization: await vapidAuth(sub.endpoint, keys, site) } });
    } catch (e) { return { ok: false, err: String(e) }; }
    if (r.status === 404 || r.status === 410) await this.ctx.storage.delete('sub');   // abbonamento scaduto: va riattivato dall'app
    return { ok: r.ok, status: r.status, err: r.ok ? undefined : (await r.text()).slice(0, 200) };
  }
}

async function readBody(req) { try { const t = await req.text(); return t ? JSON.parse(t) : {}; } catch (e) { return null; } }

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (!url.pathname.startsWith('/api/')) return env.ASSETS.fetch(req);
    if (url.pathname === '/api/ping') return json({ ok: true, push: true });
    const u = url.searchParams.get('u') || '';
    if (!/^[A-Za-z0-9_-]{16,64}$/.test(u)) return json({ ok: false, err: 'id non valido' }, 400);
    const t = env.TIMER.get(env.TIMER.idFromName(u));
    const route = url.pathname.slice(5);
    if (req.method === 'GET' && route === 'vapid') return json({ ok: true, key: await t.vapid() });
    if (req.method === 'GET' && route === 'status') return json(Object.assign({ ok: true }, await t.status()));
    if (req.method !== 'POST') return json({ ok: false, err: 'metodo' }, 405);
    const b = await readBody(req); if (!b) return json({ ok: false, err: 'json' }, 400);
    if (route === 'subscribe') return json(await t.subscribe(b.sub, url.origin + '/'));
    if (route === 'timer') return json(await t.schedule(b));
    if (route === 'cancel') return json(await t.cancel(b.id));
    if (route === 'test') return json(await t.test());
    return json({ ok: false, err: 'sconosciuto' }, 404);
  }
};
