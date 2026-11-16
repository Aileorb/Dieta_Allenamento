# Il mio piano

App per iPhone (web app installabile) con piano alimentare, ricette, lista della spesa e schede di allenamento con timer.

**Installazione:** apri il sito con Safari su iPhone → pulsante Condividi → «Aggiungi alla schermata Home».

I dati (spunte, carichi, preferenze) restano salvati sul dispositivo.

## Cloudflare e notifiche del recupero

L'app gira anche come Worker Cloudflare (`wrangler.jsonc`): la cartella è servita come sito statico e `worker/index.js`
risponde su `/api/` per le notifiche di fine recupero (Web Push, iOS 16.4+ con l'app sulla schermata Home).
Ogni iPhone ha un Durable Object che genera da sé le proprie chiavi VAPID: nel repository non ci sono segreti.
Deploy: Cloudflare → Workers & Pages → Create → Import a repository → questo repo, comando di deploy `npx wrangler deploy`.
