import json, re, sys
sys.path.insert(0, '/home/claude/ric')
from db import DB, calc
from nuove import R as NEW
from estere import R as EST
ESCLUSE = {'Zuppa di miso con soba, tofu e pak choi'}
d = json.load(open('diet.json'))
def disp(k):
    n = DB[k][0]; return n if n.startswith(('Parmigiano','Skyr')) else n[0].lower()+n[1:]
rev = {disp(k): k for k in DB}
def items(foods): return [[rev[f['n']], float(f['q'].split()[0].replace(',', '.'))] for f in foods]
for ph in ('f1','f2'):
    for day in d[ph]['days']:
        for m in day['meals']:
            m['items'] = items(m['foods'])
            if m.get('alt'): m['alt']['items'] = items(m['alt']['foods'])
HOUSE = {('olio',5):'1 cucchiaino',('olio',10):'1 cucchiaio',('olio',15):'1 cucchiaio e ½',('uovo',60):'1 uovo medio',('banana',80):'½ banana grande',('banana',100):'1 piccola, sbucciata',
 ('mela',150):'1 media',('pera',150):'1 media',('kiwi',150):'2 kiwi',('arancia',150):'1 piccola, sbucciata',('albume',100):'≈3 albumi',('albume',120):'≈4 albumi',('albume',150):'≈4-5 albumi',
 ('albume',200):'≈6 albumi',('mandorle',10):'≈8 mandorle',('mandorle',15):'≈12 mandorle',('noci',15):'≈3 noci',('miele',5):'1 cucchiaino raso',('cacao',5):'1 cucchiaino',('cacao',10):'2 cucchiaini',
 ('lino',10):'1 cucchiaio',('chia',15):'1 cucchiaio e ½',('tahina',5):'1 cucchiaino',('arachidi_crema',10):'1 cucchiaino abbondante',('avocado',40):'¼ scarso di avocado',
 ('parmigiano',5):'1 cucchiaino grattugiato',('parmigiano',10):'1 cucchiaio grattugiato',('gallette',10):'1 galletta',('gallette',20):'≈2 gallette',('pane_int',15):'mezza fetta',
 ('pane_int',30):'1 fetta',('pane_int',40):'1 fetta grande',('pane_int',50):'2 fette sottili',('pane_int',60):'2 fette',('pane_int',70):'2 fette grandi',('salsa_soia',5):'1 cucchiaino',('yogurt',30):'1 cucchiaio abbondante'}
def food(k, g):
    unit = 'ml' if k in ('latte','latte_soia','salsa_soia') else 'g'
    return {'q': f"{g} {unit}", 'n': disp(k), 'h': HOUSE.get((k, g), '')}
def mac(it):
    m = calc(it); return {'k': round(m['k']), 'p': round(m['p']), 'c': round(m['c']), 'g': round(m['g'])}
extra = []
for r in d['extra']:
    r = dict(r); r['items'] = items(r['foods']); r['new'] = False; extra.append(r)
for tit, tag, slot, tempo, dose, its, ext, steps, tip, _ in NEW:
    r = {'title': tit, 'tag': tag, 'slot': slot, 'when': slot, 'portions': '1 porzione' if not dose else 'dose per più giorni', 'time': tempo,
         'foods': [food(k, g) for k, g in its], 'dose': dose, 'extra': ext, 'steps': steps, 'tip': tip, 'items': [[k, g] for k, g in its], 'new': True}
    r.update(mac(its)); extra.append(r)
HOUSE.update({('sesamo',5):'1 cucchiaino',('miso',15):'1 cucchiaio',('miso',20):'1 cucchiaio abbondante',('tortilla',80):'3 tortillas piccole',('tortilla',100):'4 tortillas piccole',
  ('kimchi',30):'1 cucchiaio abbondante',('kimchi',50):'2 cucchiai',('kimchi',60):'2 cucchiai abbondanti',('arachidi',10):'1 cucchiaio raso',('arachidi_crema',15):'1 cucchiaio'})
for tit, paese, tag, slot, tempo, its, ext, steps, tip in EST:
    if tit in ESCLUSE: continue
    r = {'title': tit, 'paese': paese, 'tag': 'Carne' if tag in ('Manzo','Maiale','Carne') else tag, 'slot': slot, 'when': slot, 'portions': '1 porzione', 'time': tempo,
         'foods': [food(k, g) for k, g in its], 'dose': '', 'extra': ext, 'steps': steps, 'tip': tip, 'items': [[k, g] for k, g in its], 'new': True}
    r.update(mac(its)); extra.append(r)
for i, r in enumerate(extra, 1): r['n'] = f"E{i}"; r['num'] = i
d['extra'] = extra
CATS = [
 ('Cereali, pane e tuberi', ['avena','pasta','pasta_int','pasta_uovo','pasta_lent','soba','vermicelli','riso','riso_int','riso_venere','riso_car','cous_int','farro','orzo','quinoa','farina_int','farina_ceci','bulgur','tortilla','pane_int','gallette','patate','patate_dolci']),
 ('Legumi e proteine vegetali', ['lenticchie','ceci','fagioli','piselli','edamame','lupini','tofu','tempeh','seitan','soia_text']),
 ('Carne, pesce e uova', ['pollo','tacchino','manzo','macinato','bresaola','trota','salmone','sgombro','merluzzo','branzino','tonno','gamberi','lonza','uovo','albume']),
 ('Latticini e alternative', ['yogurt','skyr','fiocchi','latte','mozz_light','parmigiano','yogurt_soia','latte_soia']),
 ('Frutta', ['banana','mela','pera','arancia','kiwi','fragole','bosco','datteri','avocado']),
 ('Verdura', ['verdure','insalata','broccoli','spinaci','zucchine','peperoni','cavolfiore','carote','finocchi','fagiolini','melanzane','zucca','verza','pakchoi','germogli','kimchi','cetriolo','funghi','pomodori','passata','mais']),
 ('Dispensa', ['olio','noci','mandorle','pinoli','arachidi','arachidi_crema','tahina','sesamo','miso','lino','chia','cacao','cioccolato','miele','acero','salsa_soia'])]
used = set()
for ph in ('f1','f2'):
    for day in d[ph]['days']:
        for m in day['meals']:
            used |= {k for k, _ in m['items']} | ({k for k, _ in m['alt']['items']} if m.get('alt') else set())
for r in extra: used |= {k for k, _ in r['items']}
allcat = {k for _, ks in CATS for k in ks}
print('senza categoria', used - allcat)
GROUP = {**{k:'pollo' for k in ('pollo','tacchino')}, **{k:'manzo' for k in ('manzo','macinato','bresaola')},
         **{k:'pesce' for k in ('trota','salmone','sgombro','merluzzo','branzino','tonno','gamberi')}, 'lonza':'maiale'}
for ph in ('f1','f2'):
    for r in d[ph]['recipes']:
        r['items'] = items(r['foods']); used |= {k for k, _ in r['items']}
d['food'] = {k: [DB[k][0], 'ml' if k in ('latte','latte_soia','salsa_soia') else 'g', DB[k][1], GROUP.get(k, '')] for k in used}
d['cats'] = [[n, [k for k in ks if k in used]] for n, ks in CATS]
for ph in ('f1','f2'): d[ph].pop('shopping', None)
import preparazioni; preparazioni.apply(d)
json.dump(d, open('diet2.json','w'), ensure_ascii=False)
print(len(extra), sum(r['new'] for r in extra))
# copertura alternative
def slot(n): return 'Colazione' if n=='Colazione' else ('Spuntino' if n in ('Spuntino','Spuntino serale','Pre-allenamento') else ('Pranzo o cena' if n in ('Pranzo','Cena') else None))
for ph in ('f1','f2'):
    cnt = []
    for day in d[ph]['days']:
        for m in day['meals']:
            if m['mod']: continue
            for veg in (False, True):
                b = m['alt'] if veg and m.get('alt') else m
                c = [r for r in extra if r['slot'] == slot(m['name']) and abs(r['k']-b['k'])/b['k'] <= .25 and (not veg or r['tag'] == 'Vegana')
                     and r['p'] * min(1.25, max(.8, b['k']/r['k'])) >= b['p'] - 10]
                cnt.append((veg, len(c), day['short'], m['name'], b['k']))
    print(ph, 'min onnivoro', min(x[1] for x in cnt if not x[0]), 'min vegano', min(x[1] for x in cnt if x[0]))
    print([x for x in cnt if x[1] < 3])
