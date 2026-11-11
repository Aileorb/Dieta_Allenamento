import json, math
from packs import P
W = json.load(open('/tmp/claude-0/weekly.json'))
FOOD = json.load(open('/home/claude/ios/diet2.json'))['food']
def weekly(ph):
    b, m = W[ph]['base'], W[ph]['mod']; t = dict(b)
    for k, v in m.items(): t[k] = t.get(k, 0) + v
    return {k: v for k, v in t.items() if v > 0}
def loose_buy(g): return math.ceil(g / 50 - 1e-9) * 50
def simulate(ph, weeks=8):
    need = weekly(ph); st = {}; out = []
    for w in range(weeks):
        t = 7 * w; lines = []
        for k, n in need.items():
            p = P[k]; rate = n / 7
            have = 0
            if k in st:
                q, d = st[k]
                if t - d < p['life']: have = max(0.0, q - rate * (t - d))
            buy = max(0.0, n - have)
            if p['size']:
                packs = math.ceil(buy / p['size'] - 1e-9) if buy > 1e-6 else 0
                cost = packs * p['price']; got = packs * p['size']
            else:
                got = loose_buy(buy) if buy > 1e-6 else 0; packs = None; cost = got / 1000 * p['price']
            if got: st[k] = (have + got, t)
            lines.append(dict(k=k, need=n, have=have, packs=packs, got=got, cost=cost))
        out.append(lines)
    return need, out
def consume_cost(k, n):  # costo del consumo effettivo (ammortizzato)
    p = P[k]; return n / (p['size'] or 1000) * p['price']
if __name__ == '__main__':
    for ph in ('f1', 'f2'):
        need, out = simulate(ph)
        tot = [sum(l['cost'] for l in wk) for wk in out]
        print(ph, 'weekly spend', [round(x, 2) for x in tot], 'avg 2-8', round(sum(tot[1:]) / 7, 2), 'consumo', round(sum(consume_cost(k, n) for k, n in need.items()), 2))
        dur = sorted(((P[k]['size'] or 0) / n, k) for k, n in need.items() if P[k]['size'])
        print('  pack weeks:', [(k, round(x, 1)) for x, k in dur if x >= 1.5])
