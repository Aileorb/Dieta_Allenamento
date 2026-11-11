import math, make3
CX, CY, RX, RY, L = 28, 341, 600, 350, 28
def arcpt(a, f=1.0, x0=40, y0=341, w=1.0):
    x, y = CX + RX * math.cos(a) * w, CY + RY * math.sin(a) * w
    return x0 + (x - x0) * f, y0 + (y - y0) * f
def dshape(f, amp=0.0, k=0, n=12):
    # quarto di insalata: lato del taglio dritto a sinistra, bordo destro tutto tondo
    pts = []
    N = 48
    for i in range(N + 1):
        a = math.pi / 2 - math.pi * i / N
        w = 1 + amp * (0.5 + 0.5 * math.sin(n * math.pi * i / N * 2 + k))
        pts.append(arcpt(a, f, w=w))
    d = f'M{40 + (L - 40) * f:.1f} {CY + RY * f:.1f} L{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(1, len(pts) - 1):
        p, q = pts[i], pts[i + 1]
        d += f' Q{p[0]:.1f} {p[1]:.1f} {(p[0]+q[0])/2:.1f} {(p[1]+q[1])/2:.1f}'
    d += f' L{pts[-1][0]:.1f} {pts[-1][1]:.1f} L{40 + (L - 40) * f:.1f} {CY - RY * f:.1f}Z'
    return d
def ruffle(p0, p1, c, n, amp):
    # bordo increspato lungo una curva quadratica p0 -> c -> p1
    d = ''
    for i in range(1, n + 1):
        t0, t1 = (i - .5) / n, i / n
        q = lambda t: ((1-t)**2*p0[0] + 2*(1-t)*t*c[0] + t*t*p1[0], (1-t)**2*p0[1] + 2*(1-t)*t*c[1] + t*t*p1[1])
        m, e = q(t0), q(t1)
        # spingi il punto di controllo verso l'esterno (perpendicolare)
        a, b = q(t0 - .02), q(t0 + .02); nx, ny = -(b[1] - a[1]), b[0] - a[0]; ln = math.hypot(nx, ny) or 1
        d += f' Q{m[0] + nx/ln*amp:.1f} {m[1] + ny/ln*amp:.1f} {e[0]:.1f} {e[1]:.1f}'
    return d
def leaf(a1, a2, uid, gap=.12, spread=.24, n=26, rf=9):
    # foglia che si stacca dal cespo e si apre verso l'esterno: attaccata in a1, sempre più aperta verso a2
    A1, A2 = math.radians(a1), math.radians(a2)
    inner, outer, under = [], [], []
    for i in range(n + 1):
        t = i / n; a = A1 + (A2 - A1) * t
        inner.append(arcpt(a, w=1 + gap * t ** 1.4))
        base = 1 + gap * t ** 1.4
        rw = base + .01 + spread * math.sin(math.pi * t) ** .8 + ((0.02 if i % 2 else -0.002) if 0 < i < n else 0) * (rf / 9)
        outer.append(arcpt(a, w=rw)); under.append(arcpt(a, w=rw - (rw - base) * .28))
    poly = lambda P: 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in P)
    face = poly(inner + outer[::-1]) + 'Z'
    rim = poly(under + outer[::-1]) + 'Z'
    s = f'<path d="{face}" fill="url(#lf{uid})" stroke="#2E7D2A" stroke-width="9" stroke-linejoin="round"/>'
    s += f'<path d="{rim}" fill="#3F9A35" opacity=".9"/>'
    # nervatura centrale lungo la foglia e nervature laterali
    mid = [((inner[i][0] + under[i][0]) / 2, (inner[i][1] + under[i][1]) / 2) for i in range(n + 1)]
    s += f'<path d="{poly(mid[1:-1])}" fill="none" stroke="#F1F9D6" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    for t in (.22, .4, .58, .76):
        k = int(t * n); mx, my = mid[k]; x2, y2 = under[min(n, k + 2)]
        s += f'<path d="M{mx:.0f} {my:.0f} L{mx + (x2-mx)*.8:.0f} {my + (y2-my)*.8:.0f}" stroke="#F1F9D6" stroke-width="6" stroke-linecap="round" opacity=".85"/>'
    return s
def lettuce(uid):
    rings = [(1.0, '#2E7D2A', .016), (.93, '#4FA83D', .016), (.84, '#93D158', .014), (.74, '#5DB646', .012), (.67, '#BFE47F', .011), (.53, '#7CC44A', .01), (.46, '#DDF0A8', .008)]
    s = f'<defs><linearGradient id="lf{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E4F4BD"/><stop offset=".6" stop-color="#B5E07A"/><stop offset="1" stop-color="#7CC44A"/></linearGradient></defs>'
    s += ''.join(f'<path d="{dshape(f, amp=a, k=i*1.3)}" fill="{c}"/>' for i, (f, c, a) in enumerate(rings))
    s += '<path d="M28 270 Q120 300 150 341 Q120 382 28 412 Z" fill="#F3EDBE" stroke="#D3CB8C" stroke-width="10"/>'
    for ang in (-55, -25, 5, 35, 62):
        a = math.radians(ang); x2, y2 = 150 + 330 * math.cos(a), 341 + 290 * math.sin(a)
        s += f'<path d="M150 341 Q{150+190*math.cos(a)+30:.0f} {341+170*math.sin(a):.0f} {x2:.0f} {y2:.0f}" fill="none" stroke="#F6FBE4" stroke-width="12" stroke-linecap="round" opacity=".7"/>'
    # foglie che si aprono: una grande in alto a destra, una piccola in basso
    s += leaf(86, 26, uid, gap=.26, spread=.3, n=30)
    s += leaf(-34, -80, uid, gap=.16, spread=.2, n=24)
    return s
def wordmark(uid, tag=True):
    make3.DEXTRA = 90
    svg = make3.wordmark(uid, tag)
    dpath = make3.g['D']['d']
    i = svg.index(f'd="{dpath}"'); a = svg.rindex('<path', 0, i); b = svg.index('/>', i) + 2
    return svg[:a] + f'<g transform="translate(60 0)">{lettuce(uid)}</g>' + svg[b:]
open('wm_L2.svg', 'w').write(wordmark('L2'))
open('wm_L2_notag.svg', 'w').write(wordmark('L2n', False))
print('ok')
