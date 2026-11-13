/* ---------- pittogrammi animati ---------- */
const L = {torso:26, thigh:20, shin:20, ua:14, fa:13};
const dir = a => { const r = a*Math.PI/180; return [Math.sin(r), -Math.cos(r)]; };
const add = (p, a, l) => { const d = dir(a); return [p[0]+d[0]*l, p[1]+d[1]*l]; };
function fk(q){
  let P=[0,0]; const S=add(P,q.t,L.torso), H=add(S,q.t,9.5), K=add(P,q.th,L.thigh), A=add(K,q.sh,L.shin);
  const E=add(S,q.ua,L.ua*(q.uaL===undefined?1:q.uaL)), W=add(E,q.fa,L.fa*(q.faL===undefined?1:q.faL));
  const J={P,S,H,K,A,E,W};
  if (q.th2!==undefined){ J.K2=add(P,q.th2,L.thigh); J.A2=add(J.K2,q.sh2,L.shin); }
  const an=q.an, ref=J[an[0]], dx=an[1]-ref[0], dy=an[2]-ref[1];
  for (const k in J) J[k]=[J[k][0]+dx, J[k][1]+dy];
  J.F=add(J.A, q.ft===undefined ? q.sh-90 : q.ft, 6); if (J.A2) J.F2=add(J.A2, q.sh2-90, 6);
  J.t=q.t;
  return J;
}
const PAT = {
  squat:{a:{t:4,th:180,sh:180,ua:215,fa:20,an:['A',56,93]}, b:{t:38,th:96,sh:205,ua:225,fa:40,an:['A',56,93]}, eq:[{k:'plate',at:'S',dx:-3,dy:1,r:9}]},
  goblet:{a:{t:2,th:180,sh:180,ua:165,fa:15,an:['A',56,93]}, b:{t:22,th:98,sh:208,ua:150,fa:20,an:['A',56,93]}, eq:[{k:'db',at:'W'}]},
  pendulum:{a:{t:-4,th:182,sh:178,ua:168,fa:18,ft:76,an:['A',64,88]}, b:{t:10,th:76,sh:214,ua:150,fa:20,ft:76,an:['A',64,88]},
    eq:[{k:'line',p:[16,37,16,94],w:4},{k:'line',p:[54,91,86,83],w:4},{k:'line',p:[60,90,60,94],w:3},{k:'line',p:[82,84,82,94],w:3},{k:'pendarm',pivot:[16,37]},{k:'backpad'},{k:'shpad'}]},
  hack:{a:{t:-22,th:155,sh:150,ua:158,fa:-12,ft:62,an:['A',80,87]}, b:{t:-22,th:65,sh:215,ua:150,fa:-8,ft:62,an:['A',80,87]},
    eq:[{k:'line',p:[68,93,98,77],w:4},{k:'line',p:[76,89,76,94],w:3},{k:'line',p:[94,80,94,94],w:3},{k:'rail'},{k:'backpad'},{k:'shpad'}]},
  legpress:{a:{t:300,th:55,sh:55,ua:170,fa:150,an:['P',44,74]}, b:{t:300,th:22,sh:122,ua:170,fa:150,an:['P',44,74]}, eq:[{k:'line',p:[14,62,48,82],w:5},{k:'line',p:[66,94,112,42],w:2},{k:'sled'}]},
  deadlift:{a:{t:62,th:118,sh:188,ua:180,fa:180,an:['A',58,93]}, b:{t:0,th:180,sh:180,ua:180,fa:180,an:['A',58,93]}, eq:[{k:'plate',at:'W',dy:3,r:10}]},
  rdl:{a:{t:0,th:180,sh:180,ua:180,fa:180,an:['A',58,93]}, b:{t:76,th:164,sh:186,ua:180,fa:180,an:['A',58,93]}, eq:[{k:'plate',at:'W',dy:3,r:9}]},
  hipthrust:{a:{t:321,th:73,sh:169,ua:140,fa:110,an:['A',90,93]}, b:{t:280,th:100,sh:166,ua:130,fa:100,an:['A',90,93]}, eq:[{k:'rect',p:[10,64,30,30]},{k:'plate',at:'P',dy:-7,r:8}]},
  split:{a:{t:2,th:170,sh:182,th2:205,sh2:290,ua:180,fa:180,an:['A',74,93]}, b:{t:10,th:105,sh:200,th2:185,sh2:290,ua:180,fa:180,an:['A',74,93]}, eq:[{k:'rect',p:[12,68,32,26]},{k:'db',at:'W'}]},
  legext:{a:{t:350,th:90,sh:180,ua:170,fa:120,an:['P',42,64]}, b:{t:350,th:90,sh:95,ua:170,fa:120,an:['P',42,64]}, eq:[{k:'line',p:[26,68,56,68],w:5},{k:'line',p:[28,68,22,36],w:5},{k:'pad',at:'A'}]},
  legcurl:{a:{t:270,th:90,sh:90,ua:200,fa:160,an:['P',58,64]}, b:{t:270,th:90,sh:15,ua:200,fa:160,an:['P',58,64]}, eq:[{k:'line',p:[14,70,82,70],w:5},{k:'pad',at:'A'}]},
  legcurl_seated:{a:{t:350,th:90,sh:100,ua:170,fa:120,an:['P',42,64]}, b:{t:350,th:90,sh:200,ua:170,fa:120,an:['P',42,64]}, eq:[{k:'line',p:[26,68,56,68],w:5},{k:'line',p:[28,68,22,36],w:5},{k:'pad',at:'A'}]},
  nordic:{a:{t:0,th:180,sh:270,ua:160,fa:130,an:['K',62,90]}, b:{t:58,th:238,sh:270,ua:120,fa:95,an:['K',62,90]}, eq:[{k:'pad',at:'A',dy:-5}]},
  calf:{a:{t:0,th:180,sh:180,ua:180,fa:180,an:['A',58,89]}, b:{t:0,th:180,sh:180,ua:180,fa:180,an:['A',58,84]}, eq:[{k:'rect',p:[48,89,26,5]},{k:'db',at:'W'}]},
  calf_seated:{a:{t:355,th:90,sh:180,ua:150,fa:120,an:['A',64,92]}, b:{t:355,th:90,sh:180,ua:150,fa:120,an:['A',64,87]}, eq:[{k:'plate',at:'K',dy:-5,r:5}]},
  bench:{a:{t:270,th:115,sh:178,ua:0,fa:0,an:['P',74,63]}, b:{t:270,th:115,sh:178,ua:158,fa:-6,an:['P',74,63]}, eq:[{k:'line',p:[18,69,84,69],w:6},{k:'line',p:[30,72,30,94],w:3},{k:'line',p:[76,72,76,94],w:3},{k:'plate',at:'W',r:8}]},
  incline:{a:{t:300,th:100,sh:180,ua:5,fa:5,an:['P',76,70]}, b:{t:300,th:100,sh:180,ua:165,fa:10,an:['P',76,70]}, eq:[{k:'line',p:[80,75,42,53],w:6},{k:'line',p:[70,77,70,94],w:3},{k:'plate',at:'W',r:7}]},
  chestpress:{a:{t:355,th:90,sh:180,ua:200,fa:90,an:['P',40,66]}, b:{t:355,th:90,sh:180,ua:90,fa:90,an:['P',40,66]}, eq:[{k:'line',p:[26,70,52,70],w:5},{k:'line',p:[30,70,26,36],w:5},{k:'handle',at:'W'}]},
  fly:{a:{t:270,th:115,sh:178,ua:0,fa:0,uaL:1,faL:1,an:['P',74,63]}, b:{t:270,th:115,sh:178,ua:12,fa:20,uaL:.3,faL:.3,an:['P',74,63]}, eq:[{k:'line',p:[18,69,84,69],w:6},{k:'line',p:[30,72,30,94],w:3},{k:'line',p:[76,72,76,94],w:3},{k:'db',at:'W'}]},
  dip:{a:{t:0,th:175,sh:200,ua:180,fa:180,an:['W',66,50]}, b:{t:15,th:170,sh:215,ua:285,fa:160,an:['W',66,50]}, eq:[{k:'line',p:[56,50,88,50],w:4},{k:'line',p:[84,50,84,94],w:3}]},
  ohp:{a:{t:0,th:180,sh:180,ua:150,fa:5,an:['A',56,93]}, b:{t:0,th:180,sh:180,ua:5,fa:3,an:['A',56,93]}, eq:[{k:'plate',at:'W',r:8}]},
  ohp_seated:{a:{t:0,th:90,sh:180,ua:150,fa:5,an:['P',46,66]}, b:{t:0,th:90,sh:180,ua:5,fa:3,an:['P',46,66]}, eq:[{k:'line',p:[30,70,56,70],w:5},{k:'line',p:[38,70,36,34],w:5},{k:'db',at:'W'}]},
  row_bent:{a:{t:72,th:165,sh:185,ua:180,fa:180,an:['A',60,93]}, b:{t:72,th:165,sh:185,ua:300,fa:190,an:['A',60,93]}, eq:[{k:'plate',at:'W',r:8}]},
  row_db:{a:{t:85,th:175,sh:182,ua:180,fa:180,an:['A',30,93]}, b:{t:85,th:175,sh:182,ua:305,fa:185,an:['A',30,93]}, eq:[{k:'line',p:[44,66,90,66],w:6},{k:'line',p:[84,68,84,94],w:3},{k:'db',at:'W'}]},
  row_seated:{a:{t:355,th:85,sh:100,ua:95,fa:92,an:['P',38,70]}, b:{t:355,th:85,sh:100,ua:215,fa:85,an:['P',38,70]}, eq:[{k:'line',p:[24,74,50,74],w:5},{k:'cable',from:[112,66]},{k:'handle',at:'W'}]},
  pulldown:{a:{t:350,th:90,sh:180,ua:15,fa:12,uaL:1,an:['P',50,68]}, m:{ua:95,fa:6,uaL:.3}, b:{t:345,th:90,sh:180,ua:196,fa:20,uaL:1,an:['P',50,68]}, eq:[{k:'line',p:[36,72,62,72],w:5},{k:'cable',from:[62,4]},{k:'hbar',at:'W'}]},
  pullup:{a:{t:0,th:180,sh:200,ua:0,fa:0,uaL:1,an:['W',62,14]}, m:{ua:85,fa:4,uaL:.3}, b:{t:6,th:176,sh:206,ua:168,fa:8,uaL:1,an:['W',62,14]}, eq:[{k:'line',p:[36,14,90,14],w:4}]},
  facepull:{a:{t:0,th:180,sh:180,ua:82,fa:84,uaL:1,an:['A',50,93]}, b:{t:-4,th:180,sh:180,ua:100,fa:12,uaL:.3,an:['A',50,93]}, eq:[{k:'cable',from:[112,24]},{k:'handle',at:'W'}]},
  curl:{a:{t:0,th:180,sh:180,ua:182,fa:178,an:['A',56,93]}, b:{t:-4,th:180,sh:180,ua:196,fa:22,an:['A',56,93]}, eq:[{k:'db',at:'W'}]},
  pushdown:{a:{t:8,th:180,sh:180,ua:172,fa:35,an:['A',50,93]}, b:{t:8,th:180,sh:180,ua:172,fa:178,an:['A',50,93]}, eq:[{k:'cable',from:[74,6]},{k:'handle',at:'W'}]},
  skull:{a:{t:270,th:115,sh:178,ua:350,fa:350,an:['P',74,63]}, b:{t:270,th:115,sh:178,ua:350,fa:235,an:['P',74,63]}, eq:[{k:'line',p:[18,69,84,69],w:6},{k:'line',p:[30,72,30,94],w:3},{k:'line',p:[76,72,76,94],w:3},{k:'plate',at:'W',r:5}]},
  ohext:{a:{t:14,th:180,sh:180,ua:25,fa:215,an:['A',64,93]}, b:{t:14,th:180,sh:180,ua:22,fa:388,an:['A',64,93]}, eq:[{k:'cable',from:[12,26]},{k:'handle',at:'W'}]},
  crunch:{a:{t:12,th:180,sh:270,ua:52,fa:232,an:['K',64,91]}, b:{t:95,th:180,sh:270,ua:135,fa:315,an:['K',64,91]}, eq:[{k:'cable',from:[74,4]},{k:'handle',at:'W'}]},
  abwheel:{a:{t:45,th:180,sh:270,ua:170,fa:170,an:['K',40,91]}, b:{t:95,th:230,sh:270,ua:105,fa:105,an:['K',40,91]}, eq:[{k:'wheel'}]}
};
/* ---------- tempo e sequenza dei movimenti ---------- */
// Ogni ripetizione: fase eccentrica lenta (~2 s), concentrica più rapida (~1 s), brevi pause ai punti di inversione.
const ECC_FIRST = new Set(['squat','goblet','pendulum','hack','rdl','split','nordic','bench','incline','fly','dip','skull','abwheel']);
const TEMPO = {con:1.05, ecc:2.0, top:.45, bot:.35};
const SPEC = {nordic:{ecc:3.2, con:1.5, bot:.5}, calf:{top:.7, con:.8, ecc:1.4}, calf_seated:{top:.7, con:.8, ecc:1.4}, legext:{top:.6}, legcurl:{top:.55},
  legcurl_seated:{top:.55}, hipthrust:{top:.75}, lateral:{top:.4, con:1.1, ecc:1.7}, rearfly:{top:.5}, facepull:{top:.6}, crunch:{top:.5},
  deadlift:{con:1.4, ecc:1.6, bot:.6, top:.3}, pullup:{con:1.3, ecc:2.0, top:.4, bot:.5}, abwheel:{ecc:2.2, con:1.6}};
// Ritardo (+) o anticipo (−) di ogni articolazione nella fase a→b; al ritorno l'ordine si inverte, come nel gesto reale.
const LAG = {deadlift:{t:.32, an:.32}, squat:{th:.06, sh:.06}, goblet:{th:.06, sh:.06}, rdl:{th:.2, sh:.2}, hipthrust:{t:.06},
  split:{th2:.08, sh2:.08}, row_bent:{fa:.14}, row_db:{fa:.14}, row_seated:{fa:.12, t:-.15}, pulldown:{fa:.12, t:-.2},
  pullup:{fa:.12, th:.25, sh:.25}, facepull:{fa:.2}, dip:{t:.18, th:.1}, crunch:{ua:.2, fa:.2}, abwheel:{t:.12, th:.12},
  nordic:{ua:.55, fa:.55}, ohp:{fa:.12}, ohp_seated:{fa:.12}, bench:{fa:.06}, incline:{fa:.06}, skull:{ua:.25}, legpress:{sh:.06}, pendulum:{th:.06, sh:.06}, hack:{th:.06, sh:.06}};
function poseVal(A, M, B, uOf){
  const q = {};
  for (const k in A){
    const u = uOf(k);
    if (k === 'an'){ q.an = [A.an[0], A.an[1] + (B.an[1] - A.an[1]) * u, A.an[2] + (B.an[2] - A.an[2]) * u]; continue; }
    if (M && M[k] !== undefined) q[k] = u < .5 ? A[k] + (M[k] - A[k]) * u * 2 : M[k] + (B[k] - M[k]) * (u - .5) * 2;
    else q[k] = A[k] + (B[k] - A[k]) * u;
  }
  return q;
}
// profilo a minimo jerk (come i movimenti umani): velocità e accelerazione nulle all'inizio e alla fine
const mj = x => x * x * x * (10 + x * (-15 + 6 * x));
const ease = mj;
// concentrica: spinta più decisa all'inizio, poi rallenta verso il blocco
const easeOut = x => mj(Math.pow(x, .8));
function cycleOf(name){
  const t = Object.assign({}, TEMPO, SPEC[name] || {}), ef = ECC_FIRST.has(name);
  const seq = ef ? [['hold', t.top, 0], ['move', t.ecc, 0, 1, 'ecc'], ['hold', t.bot, 1], ['move', t.con, 1, 0, 'con']]
                 : [['hold', t.bot, 0], ['move', t.con, 0, 1, 'con'], ['hold', t.top, 1], ['move', t.ecc, 1, 0, 'ecc']];
  return {seq, total: seq.reduce((a, x) => a + x[1], 0)};
}
const CYC = {};
function phaseAt(name, sec){
  const c = CYC[name] || (CYC[name] = cycleOf(name));
  let t = sec % c.total;
  for (const p of c.seq){ if (t <= p[1]) return p[0] === 'hold' ? {hold:true, at:p[2]} : {from:p[2], to:p[3], r:t/p[1], kind:p[4]}; t -= p[1]; }
  return {hold:true, at:0};
}
function jointU(r, lag, kind){
  const x = lag >= 0 ? (r - lag) / (1 - lag) : r / (1 + lag);
  const c = Math.min(1, Math.max(0, x));
  return kind === 'con' ? easeOut(c) : ease(c);
}
/* ---------- vincoli per traiettorie realistiche ---------- */
const deg = (dx, dy) => Math.atan2(dx, -dy) * 180 / Math.PI;
const lerp2 = (a, b, u) => [a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u];
// IK a due segmenti: gomito/ginocchio dalla spalla/anca e dal polso/caviglia, piegato dalla stessa parte della posa di partenza
function ik2(R, T, l1, l2, side){
  let dx = T[0] - R[0], dy = T[1] - R[1], d = Math.hypot(dx, dy) || 1e-6;
  const dm = Math.min(l1 + l2 - .01, Math.max(Math.abs(l1 - l2) + .01, d)); if (dm !== d){ dx *= dm / d; dy *= dm / d; d = dm; }
  const a = Math.acos(Math.min(1, Math.max(-1, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d)))), b = Math.atan2(dy, dx) + side * a;
  const E = [R[0] + Math.cos(b) * l1, R[1] + Math.sin(b) * l1];
  return {E, T: [R[0] + dx, R[1] + dy]};
}
const cross = (R, M, T) => (M[0] - R[0]) * (T[1] - R[1]) - (M[1] - R[1]) * (T[0] - R[0]);
// verso di piegatura preso dalla posa più piegata delle due (quella distesa non lo dice)
const bendSide = (a, b, r, m, t) => { const ca = cross(a[r], a[m], a[t]), cb = cross(b[r], b[m], b[t]); return -(Math.sign(Math.abs(ca) > Math.abs(cb) ? ca : cb) || 1); };
// bilanciere sulla verticale del mezzo piede: il busto si inclina quanto serve (squat, stacchi, affondi)
const BAR = {squat:'S', goblet:'S', split:'S', deadlift:'S', rdl:'S'};
// spinte e tirate multiarticolari: mani su una traiettoria quasi rettilinea, il gomito segue
const HAND = {bench:.06, incline:.04, chestpress:0, ohp:-.05, ohp_seated:-.05, row_bent:0, row_db:0, row_seated:0};
const FOOT = {legpress:1};
const FK0 = {};
function ends(name){ const p = PAT[name]; return FK0[name] || (FK0[name] = {a: fk(p.a), b: fk(p.b)}); }
function constrain(name, q, u){
  const p = PAT[name], E0 = ends(name);
  if (BAR[name]){
    const J = fk(Object.assign({}, q, {t: 0})), tx = E0.a.S[0] + (E0.b.S[0] - E0.a.S[0]) * u;
    const sx = Math.max(-.98, Math.min(.98, (tx - J.P[0]) / L.torso));
    q.t = Math.asin(sx) * 180 / Math.PI;
    if (q.t < -10) q.t = -10;
  }
  if (HAND[name] !== undefined){
    const J = fk(q), Wa = E0.a.W, Wb = E0.b.W, bow = HAND[name], W = lerp2(Wa, Wb, u);
    // leggera curva (a J nella panca, verso il viso nella lento)
    const nx = -(Wb[1] - Wa[1]), ny = Wb[0] - Wa[0], k = Math.sin(Math.PI * u) * bow; W[0] += nx * k; W[1] += ny * k;
    const l1 = L.ua * (q.uaL === undefined ? 1 : q.uaL), l2 = L.fa * (q.faL === undefined ? 1 : q.faL), side = bendSide(E0.a, E0.b, 'S', 'E', 'W');
    const r = ik2(J.S, W, l1, l2, side); q.ua = deg(r.E[0] - J.S[0], r.E[1] - J.S[1]); q.fa = deg(r.T[0] - r.E[0], r.T[1] - r.E[1]);
  }
  if (FOOT[name]){
    const J = fk(q), A = lerp2(E0.a.A, E0.b.A, u), side = bendSide(E0.a, E0.b, 'P', 'K', 'A');
    const r = ik2(J.P, A, L.thigh, L.shin, side); q.th = deg(r.E[0] - J.P[0], r.E[1] - J.P[1]); q.sh = deg(r.T[0] - r.E[0], r.T[1] - r.E[1]);
  }
  return q;
}
// respiro e piccole variazioni di ritmo: il gesto non si ripete identico come una macchina
const warp = sec => sec + .22 * Math.sin(sec * .5) + .06 * Math.sin(sec * 1.3);
function breathe(name, q, sec){ const b = Math.sin(sec * 1.25); q.t += .7 * b; if (q.an) q.an = [q.an[0], q.an[1], q.an[2] - .15 * (1 + b) * (q.an[0] === 'A' ? 1 : 0)]; return q; }
function poseAt(name, sec0){
  const sec = warp(sec0), pat = PAT[name], ph = phaseAt(name, sec);
  if (!pat){ const u = ph.hold ? ph.at : (ph.from + (ph.to - ph.from) * jointU(ph.r, 0, ph.kind)); return {u}; }
  const lag = LAG[name] || {};
  const prog = k => { if (ph.hold) return ph.at; const L = lag[k] || 0; return ph.from === 0 ? jointU(ph.r, L, ph.kind) : 1 - jointU(ph.r, -L, ph.kind); };
  const q = poseVal(pat.a, pat.m, pat.b, prog), uMain = prog(HAND[name] !== undefined ? 'ua' : FOOT[name] ? 'th' : 'th');
  if (!BAR[name]) breathe(name, q, sec0);
  constrain(name, q, uMain);
  if (BAR[name]) q.t += .6 * Math.sin(sec0 * 1.25);
  return {q, u: prog('_')};
}
function lerpPose(a, b, u, m){ if (m) return poseVal(a, m, b, () => u); const q = {}; for (const k in a){ if (k === 'an') q.an = [a.an[0], a.an[1]+(b.an[1]-a.an[1])*u, a.an[2]+(b.an[2]-a.an[2])*u]; else q[k] = a[k]+(b[k]-a[k])*u; } return q; }
const ln = (p, q, w, c, o) => `<line x1="${p[0].toFixed(1)}" y1="${p[1].toFixed(1)}" x2="${q[0].toFixed(1)}" y2="${q[1].toFixed(1)}" stroke="${c}" stroke-width="${w}" stroke-linecap="round"${o?` opacity="${o}"`:''}/>`;
function frontFig(u, rear){
  const phi = 12 + 70*u, c = 'var(--fig)', out = [];
  out.push(`<line x1="20" y1="94" x2="100" y2="94" stroke="var(--equip)" stroke-width="2"/>`);
  out.push(ln([54,58],[53,93],5,c), ln([66,58],[67,93],5,c));
  out.push(`<path d="M50 32 L70 32 L66 58 L54 58 Z" fill="var(--fig)"/>`);
  out.push(`<circle cx="60" cy="21" r="7.5" fill="var(--fig)"/>`);
  for (const s of [-1, 1]){
    const S = [60+s*10, 33]; const r = phi*Math.PI/180;
    const E = [S[0]+s*Math.sin(r)*14, S[1]+Math.cos(r)*14];
    const r2 = (phi+12)*Math.PI/180; const W = [E[0]+s*Math.sin(r2)*13, E[1]+Math.cos(r2)*13];
    out.push(ln(S,E,4.5,c), ln(E,W,4,c));
    out.push(`<rect x="${(W[0]-4).toFixed(1)}" y="${(W[1]-2.5).toFixed(1)}" width="8" height="5" rx="2" fill="var(--plate)"/>`);
  }
  if (rear) out.push(`<text x="60" y="12" text-anchor="middle" font-size="7" fill="var(--equip)">vista posteriore</text>`);
  return out.join('');
}
function drawFig(name, st, tool){
  const u = typeof st === 'number' ? st : st.u;
  if (name === 'lateral' || name === 'rearfly') return frontFig(u, name === 'rearfly');
  const pat = PAT[name] || PAT.curl;
  const J = fk(typeof st === 'number' || !st.q ? lerpPose(pat.a, pat.b, u, pat.m) : st.q);
  const c = 'var(--fig)', e = 'var(--equip)', out = [];
  out.push(`<line x1="4" y1="94" x2="116" y2="94" stroke="${e}" stroke-width="2"/>`);
  const eqs = pat.eq.slice();
  if (name === 'curl' && tool === 'Cavo') eqs.push({k:'cable', from:[86,90]});
  // riferimento solidale al busto: d = verso la schiena, s = lungo il busto (per schienale e imbottiture)
  const tf = JJ => { const b = dir(JJ.t - 90), u2 = dir(JJ.t); return (p, d, s) => [p[0] + b[0]*d + u2[0]*s, p[1] + b[1]*d + u2[1]*s]; }, tb = tf(J);
  for (const q of eqs){
    if (q.k === 'pendarm'){ const X = tb(J.S, 5.5, -4), pv = q.pivot, m = [pv[0] + (X[0]-pv[0])*.42, pv[1] + (X[1]-pv[1])*.42];
      out.push(ln(pv, X, 3.5, e) + `<circle cx="${pv[0]}" cy="${pv[1]}" r="3.2" fill="${e}"/><circle cx="${m[0].toFixed(1)}" cy="${m[1].toFixed(1)}" r="7" fill="var(--plate)"/><circle cx="${m[0].toFixed(1)}" cy="${m[1].toFixed(1)}" r="1.8" fill="var(--surface)"/>`); }
    if (q.k === 'rail'){ const Ja = fk(pat.a), Jb = fk(pat.b), A1 = tf(Ja)(Ja.S, 9, 4), B1 = tf(Jb)(Jb.P, 9, -6); out.push(ln(A1, B1, 3, e) + ln(B1, [B1[0], 94], 3, e)); }
    if (q.k === 'backpad') out.push(ln(tb(J.P, 5.5, 2), tb(J.S, 5.5, -1), 5, e));
    if (q.k === 'line') out.push(`<line x1="${q.p[0]}" y1="${q.p[1]}" x2="${q.p[2]}" y2="${q.p[3]}" stroke="${e}" stroke-width="${q.w}" stroke-linecap="round"/>`);
    if (q.k === 'rect') out.push(`<rect x="${q.p[0]}" y="${q.p[1]}" width="${q.p[2]}" height="${q.p[3]}" rx="2" fill="${e}"/>`);
    if (q.k === 'cable'){ const W = J.W; out.push(`<circle cx="${q.from[0]}" cy="${q.from[1]}" r="3" fill="none" stroke="${e}" stroke-width="2"/>` + ln(q.from, W, 1.4, e)); }
  }
  if (J.K2){ out.push(ln(J.P,J.K2,5,c,.45), ln(J.K2,J.A2,4.5,c,.45), ln(J.A2,J.F2,3.5,c,.45)); }
  out.push(ln(J.P,J.K,5.5,c), ln(J.K,J.A,5,c), ln(J.A,J.F,4,c));
  out.push(ln(J.P,J.S,8,c));
  out.push(`<circle cx="${J.H[0].toFixed(1)}" cy="${J.H[1].toFixed(1)}" r="7" fill="${c}"/>`);
  out.push(ln(J.S,J.E,4.5,c), ln(J.E,J.W,4,c));
  for (const q of eqs){
    const at = q.at ? J[q.at] : null;
    if (q.k === 'plate'){ const x = at[0]+(q.dx||0), y = at[1]+(q.dy||0); out.push(`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${q.r}" fill="var(--plate)"/><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="1.8" fill="var(--surface)"/>`); }
    if (q.k === 'db') out.push(`<rect x="${(at[0]-5).toFixed(1)}" y="${(at[1]-3).toFixed(1)}" width="10" height="6" rx="2.5" fill="var(--plate)"/>`);
    if (q.k === 'pad') out.push(`<circle cx="${at[0].toFixed(1)}" cy="${(at[1]+(q.dy||0)).toFixed(1)}" r="3.6" fill="var(--equip)"/>`);
    if (q.k === 'shpad') out.push(ln(tb(J.S, 4, 3.2), tb(J.S, -4.5, 3.2), 4.5, e));
    if (q.k === 'handle') out.push(`<circle cx="${at[0].toFixed(1)}" cy="${at[1].toFixed(1)}" r="2.6" fill="var(--plate)"/>`);
    if (q.k === 'hbar') out.push(ln([at[0]-9,at[1]],[at[0]+9,at[1]],3,'var(--plate)'));
    if (q.k === 'wheel') out.push(ln(J.W,[J.W[0],89],2,e) + `<circle cx="${J.W[0].toFixed(1)}" cy="89" r="5" fill="none" stroke="var(--plate)" stroke-width="2.5"/>`);
    if (q.k === 'sled'){ const d = dir(55+90), A = J.A; out.push(ln([A[0]+d[0]*9,A[1]+d[1]*9],[A[0]-d[0]*9,A[1]-d[1]*9],4,'var(--plate)')); }
  }
  return out.join('');
}
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const anim = new Set();
const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(en => en.isIntersecting ? anim.add(en.target) : anim.delete(en.target))) : null;
function mountFig(svg){ svg.innerHTML = drawFig(svg.dataset.p, reduce ? 1 : 0, svg.dataset.t); if (!reduce){ io ? io.observe(svg) : anim.add(svg); } }
function loop(ts){ const sec = ts/1000; anim.forEach(s => { if (s.isConnected) s.innerHTML = drawFig(s.dataset.p, poseAt(s.dataset.p, sec + (+s.dataset.o || 0)), s.dataset.t); else anim.delete(s); }); requestAnimationFrame(loop); }
if (!reduce) requestAnimationFrame(loop);

