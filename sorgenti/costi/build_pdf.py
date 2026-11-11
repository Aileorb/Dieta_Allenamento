import json, math
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, CondPageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from packs import P
from sim import simulate, consume_cost, weekly

FD = '/usr/share/fonts/truetype/dejavu/'
for n, f in [('DV', 'DejaVuSans.ttf'), ('DVB', 'DejaVuSans-Bold.ttf'), ('DVC', 'DejaVuSansCondensed.ttf'), ('DVCB', 'DejaVuSansCondensed-Bold.ttf'), ('DVCI', 'DejaVuSansCondensed-Oblique.ttf')]:
    pdfmetrics.registerFont(TTFont(n, FD + f))
from reportlab.lib.fonts import addMapping
addMapping('DVC', 0, 0, 'DVC'); addMapping('DVC', 1, 0, 'DVCB'); addMapping('DVC', 0, 1, 'DVCI'); addMapping('DVC', 1, 1, 'DVCB')
addMapping('DV', 0, 0, 'DV'); addMapping('DV', 1, 0, 'DVB'); addMapping('DV', 0, 1, 'DV'); addMapping('DV', 1, 1, 'DVB')

NAVY = colors.HexColor('#1F4A5C'); TEAL = colors.HexColor('#2F7D8C'); LIGHT = colors.HexColor('#EEF3F5'); GRID = colors.HexColor('#C9D6DC'); MUTE = colors.HexColor('#5F6F77'); WARM = colors.HexColor('#FFF4E0')
st = {
 'h0': ParagraphStyle('h0', fontName='DVB', fontSize=24, leading=29, textColor=NAVY, spaceAfter=4),
 'sub': ParagraphStyle('sub', fontName='DV', fontSize=11.5, leading=15, textColor=MUTE, spaceAfter=10),
 'h1': ParagraphStyle('h1', fontName='DVB', fontSize=15, leading=19, textColor=NAVY, spaceBefore=12, spaceAfter=6),
 'h2': ParagraphStyle('h2', fontName='DVB', fontSize=11.5, leading=15, textColor=NAVY, spaceBefore=8, spaceAfter=4),
 'p': ParagraphStyle('p', fontName='DV', fontSize=9.3, leading=13, spaceAfter=5),
 'b': ParagraphStyle('b', fontName='DV', fontSize=9.3, leading=13, leftIndent=11, bulletIndent=2, spaceAfter=3),
 'note': ParagraphStyle('note', fontName='DVC', fontSize=8, leading=10.5, textColor=MUTE, spaceAfter=4),
 'c': ParagraphStyle('c', fontName='DVC', fontSize=8.2, leading=10.3),
 'cb': ParagraphStyle('cb', fontName='DVCB', fontSize=8.2, leading=10.3),
 'cr': ParagraphStyle('cr', fontName='DVC', fontSize=8.2, leading=10.3, alignment=2),
 'ch': ParagraphStyle('ch', fontName='DVCB', fontSize=8.2, leading=10.3, textColor=colors.white),
 'chr': ParagraphStyle('chr', fontName='DVCB', fontSize=8.2, leading=10.3, textColor=colors.white, alignment=2),
}
def eur(x): return f"{x:,.2f} €".replace(',', 'X').replace('.', ',').replace('X', '.')
def eur0(x): return f"≈{round(x):,} €".replace(',', '.')
def qty(k, g):
    if k == 'uovo': n = round(g / 60); return f"{n} uova"
    u = 'ml' if FOOD[k][1] == 'ml' else 'g'
    if g >= 1000: return f"{g/1000:.2f}".rstrip('0').rstrip('.').replace('.', ',') + (' l' if u == 'ml' else ' kg')
    return f"{round(g/10)*10 if g >= 100 else round(g)} {u}"
FOOD = json.load(open('/home/claude/ios/diet2.json'))['food']; CATS = json.load(open('/home/claude/ios/diet2.json'))['cats']
def P_(t, s='c'): return Paragraph(t, st[s])
def table(rows, widths, head=1, sub_rows=(), total_rows=(), zebra=True):
    t = Table(rows, colWidths=widths, repeatRows=head)
    ts = [('BACKGROUND', (0, 0), (-1, head - 1), NAVY), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
          ('TOPPADDING', (0, 0), (-1, -1), 3.2), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.2), ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
          ('LINEBELOW', (0, head), (-1, -1), 0.4, GRID)]
    for r in sub_rows: ts += [('BACKGROUND', (0, r), (-1, r), LIGHT)]
    for r in total_rows: ts += [('BACKGROUND', (0, r), (-1, r), NAVY)]
    t.setStyle(TableStyle(ts)); return t

def kpis(items, w):
    cells = [[Paragraph(f"<font name='DVB' size=17 color='#1F4A5C'>{a}</font>", ParagraphStyle('k', alignment=1, leading=21)) for a, _ in items],
             [Paragraph(b, ParagraphStyle('kl', fontName='DVC', fontSize=7.8, leading=9.6, textColor=MUTE, alignment=1)) for _, b in items]]
    t = Table(cells, colWidths=[w / len(items)] * len(items))
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), LIGHT), ('LINEAFTER', (0, 0), (-2, -1), 3, colors.white),
        ('TOPPADDING', (0, 0), (-1, 0), 8), ('BOTTOMPADDING', (0, -1), (-1, -1), 8), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
    return t

def first_week(ph):
    need, out = simulate(ph, 8); return need, out
def initial_table(ph, W):
    need, out = first_week(ph); wk = {l['k']: l for l in out[0]}
    rows = [[P_('Prodotto', 'ch'), P_('Confezione Esselunga', 'ch'), P_('Serve in sett.', 'chr'), P_('Compri', 'chr'), P_('Costo', 'chr')]]
    sub, tot_rows, total = [], [], 0
    for cn, ks in CATS:
        ks = [k for k in ks if k in wk and wk[k]['cost'] > 0]
        if not ks: continue
        ct = sum(wk[k]['cost'] for k in ks); total += ct
        sub.append(len(rows)); rows.append([P_(cn, 'cb'), '', '', '', P_(f"<b>{eur(ct)}</b>", 'cr')])
        for k in ks:
            l = wk[k]; p = P[k]
            buy = f"{l['packs']} conf." if p['size'] else qty(k, l['got'])
            rows.append([P_(FOOD[k][0]), P_(p['label'] + (f" · {eur(p['price'])}" if p['size'] else f" · {eur(p['price'])}/kg")), P_(qty(k, l['need']), 'cr'), P_(buy, 'cr'), P_(eur(l['cost']), 'cr')])
    tot_rows.append(len(rows)); rows.append([P_('<b>Totale prima spesa</b>', 'ch'), '', '', '', P_(f"<b>{eur(total)}</b>", 'chr')])
    t = table(rows, [W*.21, W*.47, W*.11, W*.10, W*.11], sub_rows=sub, total_rows=tot_rows)
    t.setStyle(TableStyle([('SPAN', (0, r), (3, r)) for r in sub + tot_rows]))
    return t, total

def rebuy_table(ph, W):
    need = weekly(ph)
    rows = [[P_('Prodotto', 'ch'), P_('Confezione', 'ch'), P_('Consumo a sett.', 'chr'), P_('Una conf. dura', 'chr'), P_('Costo a sett.', 'chr')]]
    items = []
    for k, n in need.items():
        p = P[k]
        if not p['size']: continue
        wks = p['size'] / n
        if wks < 1.5: continue
        life_w = p['life'] / 7
        dur = min(wks, life_w)
        items.append((dur, k, n, wks, life_w))
    items.sort(key=lambda x: (x[0], x[1]))
    for dur, k, n, wks, life_w in items:
        p = P[k]
        if life_w < wks:
            d = f"{life_w:.0f} sett.*"; cost = p['price'] / life_w
        else:
            d = (f"{wks:.1f}".replace('.', ',') if wks < 10 else f"{wks:.0f}") + " sett."; cost = consume_cost(k, n)
        lab = p['label'] + (" · <i>porziona e congela</i>" if p.get('frz') else '')
        rows.append([P_(FOOD[k][0]), P_(lab), P_(qty(k, n), 'cr'), P_(d, 'cr'), P_(eur(cost), 'cr')])
    return KeepTogether([table(rows, [W*.22, W*.42, W*.12, W*.13, W*.11]), Spacer(1, 3), Paragraph('* La confezione basterebbe più a lungo, ma una volta aperta (o comprata, se fresca) si conserva solo fin lì: il costo a settimana tiene conto di quello che avanza.', st['note'])]) if False else [table(rows, [W*.22, W*.42, W*.12, W*.13, W*.11]), Spacer(1, 3), Paragraph('* La confezione basterebbe più a lungo, ma si conserva solo fin lì: il costo a settimana tiene conto di quello che avanza e va buttato.', st['note'])]

def weekly_list(ph):
    need = weekly(ph)
    wk = [k for k, n in need.items() if not P[k]['size'] or P[k]['size'] / n < 1.5]
    by = {}
    for cn, ks in CATS:
        l = [FOOD[k][0] for k in ks if k in wk]
        if l: by[cn] = l
    return by

class Doc(BaseDocTemplate):
    def __init__(self, fn):
        super().__init__(fn, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=17*mm, bottomMargin=15*mm,
                         title='Spesa Esselunga: costi e scorte', author='Il mio piano')
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='f')
        self.addPageTemplates([PageTemplate('p', [fr], onPage=self.deco)])
    def deco(self, c, d):
        if d.page == 1: return
        c.setFont('DVC', 7.5); c.setFillColor(MUTE)
        c.drawString(16*mm, A4[1] - 10*mm, 'Spesa Esselunga · costi iniziali, costi settimanali e quando ricomprare')
        c.drawRightString(A4[0] - 16*mm, A4[1] - 10*mm, f'pag. {d.page}')

def build(out):
    doc = Doc(out); W = doc.width; s = []
    n1, o1 = simulate('f1', 8); n2, o2 = simulate('f2', 8)
    sp1 = [sum(l['cost'] for l in w) for w in o1]; sp2 = [sum(l['cost'] for l in w) for w in o2]
    c1 = sum(consume_cost(k, n) for k, n in n1.items()); c2 = sum(consume_cost(k, n) for k, n in n2.items())
    s += [Paragraph('Spesa Esselunga: costi e scorte', st['h0']),
          Paragraph('Quanto costa partire con il piano, quanto si spende poi ogni settimana e ogni quanto ricomprare i prodotti a lunga conservazione, con le confezioni che si trovano all’Esselunga.', st['sub'])]
    s.append(kpis([(eur0(sp1[0]), 'prima spesa<br/>Ricomposizione'), (eur0(c1), 'a settimana, a regime<br/>Ricomposizione'), (eur0(c1/7*30.4), 'al mese<br/>Ricomposizione'),
                   (eur0(sp2[0]), 'prima spesa<br/>Mantenimento'), (eur0(c2), 'a settimana, a regime<br/>Mantenimento')], W))
    s.append(Spacer(1, 8))
    s.append(Paragraph('Come sono calcolate le stime', st['h2']))
    for t in [
        'Quantità: menu di default di ogni fase, con gli extra dei giorni di palestra e di corsa, versione onnivora. Cambiando i pasti con le alternative cambiano anche i costi: l’app li ricalcola.',
        'Prezzi: <b>prezzo pieno indicativo Esselunga, novembre 2026</b>, soprattutto marca Esselunga. Sono stime ancorate ai prezzi pubblicati (vedi le fonti in fondo); a scaffale possono variare di un 10-15% da negozio a negozio. Con le offerte Fìdaty si spende in genere meno.',
        'Confezioni: si comprano confezioni intere. Quello che avanza resta in dispensa e copre le settimane successive, finché non scade. Carne e pesce freschi avanzati si porzionano e si congelano il giorno della spesa, così non si butta niente.',
        '<b>Prima spesa</b> = la spesa della prima settimana, quando la dispensa è vuota e olio, riso, frutta secca, miele e simili si comprano interi. <b>A regime</b> = il costo di quello che consumi davvero in una settimana; la spesa reale oscilla intorno a questo valore (sezione 1, qui sotto).',
        'Non inclusi: sale, pepe, spezie, aceto, aglio, limoni e simili, che il piano dà per scontati. Se parti da zero calcola circa 10-15 € una tantum.']:
        s.append(Paragraph(t, st['b'], bulletText='•'))
    s.append(Paragraph('1. Quanto si spende settimana per settimana', st['h1']))
    s.append(Paragraph('Simulazione delle prime 8 settimane con le scorte che avanzano da una settimana all’altra. La spesa scende subito dopo la prima settimana e poi oscilla: le settimane più care sono quelle in cui finiscono insieme più prodotti da dispensa (olio, riso, frutta secca, uova).', st['p']))
    hdr = [P_('€', 'ch')] + [P_(f'Sett. {i+1}', 'chr') for i in range(8)] + [P_('Media 2-8', 'chr')]
    r1 = [P_('<b>Ricomposizione</b>')] + [P_(eur(x)[:-2], 'cr') for x in sp1] + [P_(f'<b>{eur(sum(sp1[1:])/7)[:-2]}</b>', 'cr')]
    r2 = [P_('<b>Mantenimento</b>')] + [P_(eur(x)[:-2], 'cr') for x in sp2] + [P_(f'<b>{eur(sum(sp2[1:])/7)[:-2]}</b>', 'cr')]
    s.append(table([hdr, r1, r2], [W*.17] + [W*.0825]*8 + [W*.17]))
    s.append(Spacer(1, 6))
    s.append(Paragraph(f'In 4 settimane di Ricomposizione si spendono circa <b>{eur(sum(sp1[:4]))}</b> (prima spesa compresa), poi in media <b>{eur(c1)}</b> a settimana, cioè circa <b>{eur(c1/7)}</b> al giorno. Il Mantenimento costa un po’ meno a regime (<b>{eur(c2)}</b> a settimana) perché usa più legumi e uova e niente bresaola e branzino, ma la prima spesa è più alta perché il menu usa più prodotti diversi.', st['p']))

    s.append(PageBreak())
    s.append(Paragraph('2. La prima spesa · Ricomposizione', st['h1']))
    s.append(Paragraph('Tutto quello che serve per la prima settimana. Nella colonna «Serve» c’è la quantità del piano, in «Compri» quante confezioni prendere: la differenza resta per le settimane dopo.', st['p']))
    t, tot1 = initial_table('f1', W); s.append(t)
    s.append(Spacer(1, 4)); s.append(Paragraph('Frutta, verdura sfusa e sgombro al banco si pagano a peso: la quantità in «Compri» è arrotondata ai 50 g.', st['note']))

    s.append(CondPageBreak(70*mm))
    s.append(Paragraph('3. Ogni quanto ricomprare · Ricomposizione', st['h1']))
    s.append(Paragraph('I prodotti di cui una confezione dura più di una settimana e mezza. Quando li spunti nella lista della spesa, l’app li mette tra le «Scorte in casa», scala ogni giorno il consumo del menu e te li rimette in lista la settimana in cui stanno per finire. Il costo a settimana è la quota di confezione che consumi.', st['p']))
    s += rebuy_table('f1', W)
    by = weekly_list('f1')
    s.append(Spacer(1, 6)); s.append(Paragraph('Da comprare ogni settimana', st['h2']))
    for cn, l in by.items(): s.append(Paragraph(f'<b>{cn}:</b> ' + ', '.join(l).lower().capitalize() + '.', st['b'], bulletText='•'))

    s.append(PageBreak())
    s.append(Paragraph('4. La prima spesa · Mantenimento', st['h1']))
    s.append(Paragraph('Stesso calcolo per la fase di mantenimento. Se arrivi dalla Ricomposizione, buona parte della dispensa (olio, riso, avena, frutta secca, miele, cacao) ce l’hai già: la prima spesa reale sarà più bassa.', st['p']))
    t, tot2 = initial_table('f2', W); s.append(t)
    s.append(CondPageBreak(70*mm))
    s.append(Paragraph('5. Ogni quanto ricomprare · Mantenimento', st['h1']))
    s += rebuy_table('f2', W)

    s.append(CondPageBreak(80*mm))
    s.append(Paragraph('6. Come spendere meno all’Esselunga', st['h1']))
    for t in [
        '<b>Offerte Fìdaty sui prodotti da dispensa.</b> Olio, riso, pasta, tonno, frutta secca e legumi in scatola si conservano a lungo: quando l’app ti dice che stanno per finire nelle prossime 2 settimane, prendili se sono in volantino.',
        '<b>Carne e pesce in confezione grande, poi in freezer.</b> Il petto di pollo in confezione famiglia o in offerta (a novembre 2026 in volantino a 7,80 €/kg) costa un quarto in meno del prezzo pieno. Porziona e congela.',
        '<b>Pesce surgelato al posto del fresco.</b> Merluzzo e nasello surgelati hanno le stesse proteine del pesce fresco e costano circa la metà di branzino e orata freschi.',
        '<b>Linea Smart e marca Esselunga</b> per yogurt greco, skyr, latte, passata, legumi e cereali: valori nutrizionali praticamente identici ai marchi, prezzo più basso.',
        '<b>Frutta e verdura di stagione.</b> A novembre: mele, pere, arance, clementine, kiwi, cavolfiore, broccoli, verza, finocchi e zucca. Fragole e frutti di bosco freschi fuori stagione costano il doppio: usa i frutti di bosco surgelati.',
        '<b>Il salmone è la voce più cara del pesce.</b> Alternarlo con sgombro e trota mantiene gli omega-3 spendendo meno.']:
        s.append(Paragraph(t, st['b'], bulletText='•'))
    s.append(Paragraph('Fonti dei prezzi', st['h2']))
    for t in [
        'Il Fatto Alimentare, «Yogurt greco: prezzi e proteine», 4 agosto 2026: yogurt greco Esselunga 5,30 €/kg (rilevazione di luglio 2026). ilfattoalimentare.it/yogurt-greco-prezzi-proteine.html',
        'Il Fatto Alimentare, «Pollo Esselunga Smart, Naturama e Top», 22 luglio 2024: petto di pollo Smart 7,98 €/kg, Naturama 14,99 €/kg. ilfattoalimentare.it/esselunga-prezzi-pollo-smart-naturama-top.html',
        'Volantino Esselunga 5-18 novembre 2026 (anteprima su confrontavolantini.com): petto di pollo 7,80 €/kg, branzino 9,80 €/kg, arista e lonza di suino 6,59 €/kg, mandorle tostate 500 g 4,55 €, pasta Barilla 1 kg 0,92 €.',
        'Volantino Esselunga 8-21 ottobre 2026 (tuttoesselunga.com): olio extravergine 1 l da 4,49 a 6,99 €, skyr 150 g 0,74 € con sconto 50%, mele Gala 0,98 €/kg.',
        'Spesalyze, prezzi mediani Esselunga da scontrini degli ultimi 12 mesi (aggiornato all’8 novembre 2026): carne macinata di manzo 5,99 €, bresaola 5,99 €, branzino 6,02 €, albume 1,93 €, burro di arachidi 2,44 €. spesalyze.com/prezzi-supermercati/esselunga',
        'Gli altri prezzi sono stime per confezioni equivalenti a marca Esselunga, coerenti con queste fonti. Per i prezzi esatti e aggiornati fa fede lo scaffale o la spesa online Esselunga.']:
        s.append(Paragraph(t, st['note'], bulletText='–'))
    doc.build(s)
    return sp1, sp2, c1, c2
if __name__ == '__main__':
    print(build('/home/claude/costi/Spesa_Esselunga_costi_e_scorte.pdf'))
