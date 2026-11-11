# Sorgenti dell'app

L'app pubblicata (`index.html` nella cartella principale) è generata da questi file ed è compattata.

- `template.html`: interfaccia, stili e logica dell'app.
- `fig.js`: animazioni degli esercizi.
- `dati/`: menu e ricette (`diet2.json`, generato da `build_data.py` con `diet.json`, `nuove.py`, `estere.py`, `db.py`), schede di allenamento (`train.json`), confezioni e prezzi Esselunga (`packs.json`).
- `build.py`: inserisce i dati nel template e genera `index.html`; `min.js` lo compatta con html-minifier-terser.
- `costi/`: calcolo dei costi e generazione del PDF della spesa.

Per rigenerare: copiare i JSON accanto a `build.py`, poi `python3 build.py` (con `--no-min` per la versione leggibile).
