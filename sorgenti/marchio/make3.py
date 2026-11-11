import json, math
DEXTRA=0
TGAP=120
G=json.load(open('glyphs.json')); g=G['g']; T=json.load(open('tag.json'))
def meatball(cx, cy, r, uid, k, sauce=False, sx=1.0, sy=1.0):
    # contorno irregolare (bozzoli) come una polpetta vera
    n=16; pts=[]
    for i in range(n):
        a=2*math.pi*i/n; rr=r*(1+(0.06 if i%2 else -0.03)+0.025*math.sin(i*2.7+k))
        pts.append((cx+rr*sx*math.cos(a), cy+rr*sy*math.sin(a)))
    d=f'M{(pts[0][0]+pts[-1][0])/2:.1f} {(pts[0][1]+pts[-1][1])/2:.1f}'
    for i in range(n):
        p=pts[i]; q=pts[(i+1)%n]; d+=f' Q{p[0]:.1f} {p[1]:.1f} {(p[0]+q[0])/2:.1f} {(p[1]+q[1])/2:.1f}'
    d+='Z'
    s=f'<path d="{d}" fill="url(#mb{uid})"/>'
    # riflesso (in alto a sinistra: in coordinate del font y cresce verso l'alto)
    s+=f'<ellipse cx="{cx-r*.36*sx:.0f}" cy="{cy+r*.38*sy:.0f}" rx="{r*.3*sx:.0f}" ry="{r*.19*sy:.0f}" fill="#D99368" opacity=".85" transform="rotate({30*sy:.0f} {cx-r*.36*sx:.0f} {cy+r*.38*sy:.0f})"/>'
    # granelli di carne e prezzemolo
    for (dx,dy,rr,c) in [(.35,.1,.09,'#5A2510'),(-.1,-.35,.08,'#5A2510'),(.15,-.05,.06,'#5A2510'),(-.42,-.1,.07,'#5A2510'),(.42,-.38,.07,'#5A2510'),(.05,.42,.06,'#4C9A2A'),(-.25,.05,.05,'#4C9A2A'),(.3,.35,.05,'#4C9A2A')]:
        s+=f'<circle cx="{cx+dx*r*sx:.0f}" cy="{cy+dy*r*sy:.0f}" r="{rr*r:.0f}" fill="{c}"/>'
    if sauce:
        s+=(f'<path d="M{cx-r*.85:.0f} {cy+r*.35:.0f} C{cx-r*.6:.0f} {cy+r*1.05:.0f} {cx+r*.6:.0f} {cy+r*1.1:.0f} {cx+r*.9:.0f} {cy+r*.35:.0f} '
            f'C{cx+r*.7:.0f} {cy+r*.1:.0f} {cx+r*.55:.0f} {cy+r*.45:.0f} {cx+r*.35:.0f} {cy+r*.2:.0f} C{cx+r*.2:.0f} {cy-r*.05:.0f} {cx:.0f} {cy+r*.4:.0f} {cx-r*.2:.0f} {cy+r*.3:.0f} '
            f'C{cx-r*.45:.0f} {cy+r*.15:.0f} {cx-r*.6:.0f} {cy+r*.05:.0f} {cx-r*.85:.0f} {cy+r*.35:.0f}Z" fill="#E63A26"/>'
            f'<ellipse cx="{cx-r*.25:.0f}" cy="{cy+r*.68:.0f}" rx="{r*.22:.0f}" ry="{r*.09:.0f}" fill="#FF8A73" opacity=".8"/>')
    return s
def wordmark(uid, tag=True):
    top=840; parts=[]; track=-18; x=60; lab='var(--label,#000)'
    parts.append(f'<path transform="translate({x} 0)" d="{g["D"]["d"]}" fill="{lab}"/>'); x+=g['D']['adv']+track+20+DEXTRA
    # i: gambo di polpette impilate + puntino-polpetta con il sugo
    cx=x+118; balls=''
    stack=[(104,1.12,.78,-3),(98,1.07,.88,4),(93,1.03,.96,-2)]  # (raggio, larghezza, altezza, spostamento)
    yb=-6
    for i,(r,sxx,syy,jx) in enumerate(stack):
        ry=r*syy; cyy=yb+ry; balls+=meatball(cx+jx, cyy, r, uid, i, sx=sxx, sy=syy); yb=cyy+ry-14
    balls+=meatball(cx, 640, 98, uid, 7, sauce=True)
    x+=236+track+90
    ax=x; d="M 640 40 C 520 150, 420 260, 330 380 C 250 480, 200 560, 250 650 C 300 735, 430 720, 440 630 C 450 540, 330 480, 230 420 C 120 350, 70 260, 110 150 C 160 20, 330 0, 450 90 C 540 160, 590 240, 620 320"
    pasta=(f'<g transform="translate({ax} 0)" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="{d}" stroke="#C7840F" stroke-width="150"/>'
           f'<path d="{d}" stroke="#F6C445" stroke-width="112"/><path d="{d}" stroke="#FFE59A" stroke-width="30" transform="translate(-14 14)" opacity=".9"/></g>')
    x+=700+track+190-TGAP
    tx=x; stem_w=168; scx=tx+330
    stem=f'<rect x="{scx-stem_w/2:.0f}" y="-9" width="{stem_w}" height="640" rx="78" fill="{lab}"/>'
    barL=tx+20; barR=tx+640; by=566; bh=120; cyb=by+bh/2
    bb=(f'<rect x="{barL}" y="{by}" width="{barR-barL}" height="{bh}" rx="{bh/2:.0f}" fill="url(#bar{uid})"/>'
        f'<rect x="{barL-70}" y="{cyb-165:.0f}" width="86" height="330" rx="36" fill="#E5484D"/><rect x="{barL+22}" y="{cyb-115:.0f}" width="56" height="230" rx="24" fill="#F0302B"/>'
        f'<rect x="{barR-16}" y="{cyb-165:.0f}" width="86" height="330" rx="36" fill="#E5484D"/><rect x="{barR-78}" y="{cyb-115:.0f}" width="56" height="230" rx="24" fill="#F0302B"/>')
    W=barR+110
    tagsvg=''
    if tag:
        sc=.62; tx2=W+80; s_=''; cur=0
        for ch in "– diet & training":
            gl=T[ch]; s_+=f'<path transform="translate({cur} 0)" d="{gl["d"]}"/>'; cur+=gl['adv']-10
        tagsvg=f'<g transform="translate({tx2} 0) scale({sc})" fill="var(--label2,#8E8E93)">{s_}</g>'
        W=tx2+cur*sc+30
    bot=-150; H=top-bot
    defs=(f'<linearGradient id="bar{uid}" x1="{barL}" y1="0" x2="{barR}" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FF8A1F"/><stop offset="1" stop-color="#FFB21A"/></linearGradient>'
          f'<radialGradient id="mb{uid}" cx=".38" cy=".3" r=".75"><stop offset="0" stop-color="#B0653A"/><stop offset=".7" stop-color="#7E3C1D"/><stop offset="1" stop-color="#5E2A12"/></radialGradient>')
    body=''.join(parts)+pasta+stem+bb+balls+tagsvg
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H}"><defs>{defs}</defs><g transform="translate(0 {top}) scale(1 -1)">{body}</g></svg>'
if __name__=='__main__':
    open('wm_C3.svg','w').write(wordmark('C3')); open('wm_C3_notag.svg','w').write(wordmark('C3n', False)); print('ok')
