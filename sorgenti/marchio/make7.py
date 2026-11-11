import math, make3
# quarto di insalata: cespo girato di 90° (taglio in basso) e poi tagliato a metà.
# Due tagli dritti (sinistra e in basso), bordo tondo da in alto a sinistra fino in basso a destra; torsolo nell'angolo.
X0, Y0, RX, RY = 28, -8, 613, 699
def outline_pts(N=56):
    # bordo esterno: in alto tondo come il cespo, in basso a destra si arrotonda verso il torsolo
    pts = []
    for i in range(N // 2 + 1):            # quarto superiore: centro (28,230)
        a = math.pi / 2 - (math.pi / 2) * i / (N // 2)
        pts.append((28 + 613 * math.cos(a), 230 + 461 * math.sin(a)))
    for i in range(1, N // 2 + 1):         # parte bassa: centro (330,230), si chiude sul taglio
        a = -(math.pi / 2) * i / (N // 2)
        pts.append((330 + 311 * math.cos(a), 230 + 238 * math.sin(a)))
    return pts
def quarter(f, amp=0.0, k=0, n=7):
    P = outline_pts(); N = len(P) - 1; pts = []
    for i, (x, y) in enumerate(P):
        w = 1 + amp * (0.5 + 0.5 * math.sin(n * math.pi * i / N * 2 + k)) if 0 < i < N else 1
        pts.append((X0 + (x - X0) * f * w, Y0 + (y - Y0) * f * w))
    d = f'M{X0} {Y0} L{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(1, len(pts) - 1):
        p, q = pts[i], pts[i + 1]
        d += f' Q{p[0]:.1f} {p[1]:.1f} {(p[0]+q[0])/2:.1f} {(p[1]+q[1])/2:.1f}'
    return d + f' L{pts[-1][0]:.1f} {pts[-1][1]:.1f}Z'
def lettuce():
    rings = [(1.0, '#2E7D2A', .03), (.93, '#4FA83D', .028), (.84, '#93D158', .024), (.74, '#5DB646', .02), (.66, '#BFE47F', .018), (.52, '#7CC44A', .015), (.44, '#DDF0A8', .012)]
    s = ''.join(f'<path d="{quarter(f, amp=a, k=i * 1.7)}" fill="{c}"/>' for i, (f, c, a) in enumerate(rings))
    # venature che partono dal torsolo
    for ang in (14, 34, 54, 74):
        a = math.radians(ang); r = .62 if ang < 25 else .74
        x2, y2 = X0 + RX * r * math.cos(a), Y0 + RY * r * math.sin(a)
        cx, cy = X0 + RX * .42 * math.cos(a + .12), Y0 + RY * .42 * math.sin(a + .12)
        s += f'<path d="M{X0+40} {Y0+40} Q{cx:.0f} {cy:.0f} {x2:.0f} {y2:.0f}" fill="none" stroke="#F6FBE4" stroke-width="12" stroke-linecap="round" opacity=".7"/>'
    # torsolo nell'angolo
    s += f'<path d="M{X0} {Y0} L{X0} {Y0+190} Q{X0+120} {Y0+150} {X0+170} {Y0} Z" fill="#F3EDBE" stroke="#D3CB8C" stroke-width="10" stroke-linejoin="round"/>'
    return s
make3.DEXTRA = 0
svg = make3.wordmark('Q', True)
dpath = make3.g['D']['d']
i = svg.index(f'd="{dpath}"'); a = svg.rindex('<path', 0, i); b = svg.index('/>', i) + 2
svg = svg[:a] + f'<g transform="translate(60 0)">{lettuce()}</g>' + svg[b:]
open('wm_Q.svg', 'w').write(svg); print('ok')
