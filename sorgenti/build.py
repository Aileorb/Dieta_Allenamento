# Costruisce site/index.html: inserisce dati e animazioni nel template, compatta i JSON e minimizza HTML, CSS e JS.
import json, subprocess, sys
def compact(f): return json.dumps(json.load(open(f, encoding='utf-8')), ensure_ascii=False, separators=(',', ':'))
t = open('template.html', encoding='utf-8').read()
t = (t.replace('/*__DIET__*/null', compact('diet2.json')).replace('/*__TRAIN__*/null', compact('train.json'))
      .replace('/*__FIG__*/', open('fig.js', encoding='utf-8').read()).replace('/*__PACKS__*/{}', compact('packs.json')))
open('build/index.full.html', 'w', encoding='utf-8').write(t)
if '--no-min' in sys.argv:
    open('site/index.html', 'w', encoding='utf-8').write(t)
else:
    subprocess.run(['node', '/tmp/claude-0/minify/min.js', 'build/index.full.html', 'site/index.html'], check=True)
