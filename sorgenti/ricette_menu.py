# Passaggi per i pasti del menu (proposte e alternative vegane) che non hanno una ricetta numerata.
# MEAL: titolo -> passaggi, oppure (passaggi, n. della ricetta collegata) quando una parte è una ricetta del piano.
# LINK: titolo -> n. della ricetta del piano che descrive il piatto per intero (si usano i suoi passaggi).

LINK = {
 'f1': {"Salmone in crosta di noci, patate e broccoli": 7, "Overnight oats «tiramisù»": 1, "Pollo al curry e yogurt con riso e zucchine": 8,
        "Straccetti di seitan al limone e rosmarino, patate e rucola": 4, "Riso integrale con tofu croccante e verdure": 5,
        "Burger di lenticchie e soia con spinaci": 6, "Pancake di avena e albumi con yogurt e frutti di bosco": 2,
        "Nice cream ai frutti di bosco con yogurt greco": 9, "Tagliatelle di semola al ragù di soia + verdure": 3},
 'f2': {"Porridge «apple pie» con yogurt e noci": 2, "Burrito bowl con pollo, fagioli, mais e avocado": 5,
        "Salmone teriyaki con riso basmati e broccoli": 8, "Pizza integrale fatta in casa con verdure e mozzarella light": 9,
        "Paella di pollo, piselli e peperoni": 10, "Polpette di tacchino e avena al sugo, purè leggero e spinaci": 6,
        "Curry di ceci e spinaci con riso basmati e raita allo yogurt": 11, "French toast integrale con frutti di bosco e yogurt": 4,
        "Fajitas di manzo con peperoni e piadine integrali fatte in casa": 7},
}

MEAL = {
 # ---------- colazioni ----------
 "Porridge d'avena ai frutti di bosco": [
  "In un pentolino scalda il latte con un pizzico di sale e versa l'avena.",
  "Cuoci a fuoco medio 3-4 minuti mescolando, finché diventa cremoso.",
  "Togli dal fuoco e lascia intiepidire 2 minuti, poi incorpora lo yogurt.",
  "Completa con i frutti di bosco (anche surgelati: si scongelano nel caldo) e le noci tritate."],
 "Porridge con latte e yogurt di soia": [
  "In un pentolino scalda il latte di soia con un pizzico di sale e versa l'avena.",
  "Cuoci a fuoco medio 3-4 minuti mescolando, finché diventa cremoso.",
  "Togli dal fuoco, lascia intiepidire 2 minuti e incorpora lo yogurt di soia.",
  "Completa con i frutti di bosco e le noci tritate."],
 "Toast integrale con tofu strapazzato e spinaci": [
  "Asciuga il tofu e sbriciolalo con le mani.",
  "Scalda l'olio in padella, aggiungi il tofu con curcuma, pepe e un pizzico di sale e cuoci 4-5 minuti mescolando.",
  "Unisci gli spinaci e i pomodorini a metà e cuoci altri 2 minuti, finché gli spinaci appassiscono.",
  "Tosta il pane e servi il tofu sopra o accanto."],
 "Yogurt bowl con avena, mela e mandorle": [
  "Versa lo yogurt in una ciotola.",
  "Taglia la mela a cubetti e trita grossolanamente le mandorle.",
  "Completa con avena, mela, mandorle e cannella a piacere."],
 "Bowl di yogurt di soia, avena e semi di lino": [
  "Versa lo yogurt di soia in una ciotola e mescola i semi di lino.",
  "Taglia la mela a cubetti e trita grossolanamente le mandorle.",
  "Completa con avena, mela, mandorle e cannella a piacere."],
 "Porridge al cacao con pera": [
  "In un pentolino mescola latte, avena, cacao e un pizzico di sale.",
  "Cuoci a fuoco medio 4-5 minuti mescolando, finché diventa cremoso.",
  "Togli dal fuoco, lascia intiepidire 2 minuti e incorpora lo yogurt.",
  "Completa con la pera a cubetti e le noci tritate."],
 "Porridge al cacao con latte e yogurt di soia": [
  "In un pentolino mescola latte di soia, avena, cacao e un pizzico di sale.",
  "Cuoci a fuoco medio 4-5 minuti mescolando, finché diventa cremoso.",
  "Togli dal fuoco, lascia intiepidire 2 minuti e incorpora lo yogurt di soia.",
  "Completa con la pera a cubetti e le noci tritate."],
 "Overnight oats alla mela e cannella": [
  "La sera prima: grattugia metà mela e mescolala in un barattolo con avena, yogurt, latte e cannella.",
  "Chiudi e lascia in frigo tutta la notte.",
  "Al mattino aggiungi il resto della mela a cubetti e le mandorle tritate."],
 "Overnight oats con yogurt e latte di soia": [
  "La sera prima: grattugia metà mela e mescolala in un barattolo con avena, yogurt di soia, latte di soia e cannella.",
  "Chiudi e lascia in frigo tutta la notte.",
  "Al mattino aggiungi il resto della mela a cubetti e le mandorle tritate."],
 "Pancake di farina di ceci e avena": [
  "Frulla l'avena fino a ridurla in farina e mescolala con farina di ceci, mezzo cucchiaino di lievito, cannella e un pizzico di sale.",
  "Aggiungi il latte di soia a filo, sbattendo con la frusta, fino a una pastella liscia; lasciala riposare 5 minuti.",
  "Scalda una padella antiaderente a fuoco medio e ungila appena con carta da cucina.",
  "Versa un piccolo mestolo per volta: gira quando compaiono le bollicine (circa 2 minuti), poi 1 minuto dall'altro lato.",
  "Servi con yogurt di soia, frutti di bosco e la crema di arachidi scaldata 10 secondi."],
 "Toast integrale con uovo, albumi, avocado e pomodoro": [
  "Tosta il pane.",
  "Sbatti uovo e albumi con sale e pepe.",
  "Cuocili in una padella antiaderente a fuoco basso mescolando con una spatola, finché sono cremosi (2-3 minuti).",
  "Schiaccia l'avocado con un pizzico di sale e limone e spalmalo sul pane.",
  "Completa con le uova strapazzate e il pomodoro a fette."],
 "Toast integrale con tofu strapazzato e avocado": [
  "Tosta il pane.",
  "Sbriciola il tofu e cuocilo in padella antiaderente con curcuma, pepe e un pizzico di sale per 4-5 minuti.",
  "Schiaccia l'avocado con un pizzico di sale e limone e spalmalo sul pane.",
  "Completa con il tofu strapazzato e il pomodoro a fette."],
 "Skyr con granola croccante e fragole": ([
  "Versa lo skyr in una ciotola.",
  "Taglia le fragole a pezzi.",
  "Completa con 50 g di granola (ricetta n. 1, preparata in anticipo) e le fragole."], 1),
 "Yogurt di soia con granola vegana e fragole": ([
  "Granola vegana: prepara la ricetta n. 1 sostituendo miele e albume con lo sciroppo d'acero e aggiungendo i semi di lino; si conserva 2 settimane.",
  "Versa lo yogurt di soia in una ciotola.",
  "Completa con la granola e le fragole a pezzi."], 1),
 "Smoothie bowl ai frutti di bosco": [
  "La sera prima metti in freezer la banana a rondelle.",
  "Frulla lo yogurt con la banana congelata e metà dei frutti di bosco, a scatti, fino a una crema densa.",
  "Versa in una ciotola.",
  "Completa con avena, semi di lino, mandorle a lamelle e il resto dei frutti di bosco."],
 "Smoothie bowl con yogurt e latte di soia": [
  "La sera prima metti in freezer la banana a rondelle.",
  "Frulla yogurt e latte di soia con la banana congelata e metà dei frutti di bosco fino a una crema densa.",
  "Versa in una ciotola.",
  "Completa con avena, semi di lino, mandorle a lamelle e il resto dei frutti di bosco."],
 "Muffin di avena e mirtilli, skyr e arancia": ([
  "Prendi 2 muffin di avena e mirtilli (ricetta n. 3, preparati in anticipo); se sono in frigo, scaldali 10 secondi al microonde.",
  "Servi con lo skyr in una ciotola, le mandorle e l'arancia a spicchi."], 3),
 "Chia pudding al cacao con avena e banana": [
  "La sera prima: in un barattolo mescola latte di soia, chia, avena, cacao e sciroppo d'acero.",
  "Dopo 10 minuti mescola di nuovo perché la chia non faccia grumi, chiudi e lascia in frigo tutta la notte.",
  "Al mattino completa con la banana a rondelle.",
  "I lupini, sciacquati, sono a parte."],
 "Overnight oats al cacao e chia": [
  "La sera prima: in un barattolo mescola avena, latte, skyr, chia e cacao.",
  "Chiudi e lascia in frigo tutta la notte.",
  "Al mattino mescola e completa con la banana a rondelle."],
 "Overnight oats al cacao con latte e yogurt di soia": [
  "La sera prima: in un barattolo mescola avena, latte di soia, yogurt di soia, chia e cacao.",
  "Chiudi e lascia in frigo tutta la notte.",
  "Al mattino mescola e completa con la banana a rondelle."],
 "Porridge «apple pie» con latte e yogurt di soia": [
  "Taglia la mela a cubetti e cuocila in un pentolino con 2 cucchiai d'acqua e metà della cannella per 3-4 minuti.",
  "Aggiungi avena, latte di soia, un pizzico di sale e il resto della cannella; cuoci a fuoco medio 4-5 minuti mescolando.",
  "Togli dal fuoco, lascia intiepidire un minuto e incorpora metà dello yogurt di soia.",
  "Servi con il resto dello yogurt e le noci tostate 2 minuti in padella."],
 "French toast vegano con frutti di bosco": [
  "Sbatti latte di soia, farina di ceci, cannella e vaniglia fino a una pastella liscia.",
  "Immergi le fette di pane 20 secondi per lato.",
  "Cuocile in una padella antiaderente appena unta, 2-3 minuti per lato, finché sono dorate.",
  "Intanto scalda i frutti di bosco in un pentolino per 2 minuti: diventano una salsa.",
  "Servi con la salsa, lo yogurt di soia, lo sciroppo d'acero e le noci tritate."],
 "Toast con avocado e uovo in camicia + yogurt e fragole": [
  "Porta a leggero bollore un pentolino d'acqua con un goccio d'aceto.",
  "Rompi l'uovo in una tazzina, crea un vortice nell'acqua con un cucchiaio e fai scivolare l'uovo al centro: cuoci 3 minuti e scolalo con una schiumarola.",
  "Tosta il pane e spalmaci l'avocado schiacciato con sale, pepe e limone.",
  "Adagia l'uovo sul toast.",
  "Servi con lo yogurt e le fragole a pezzi a parte."],
 "Toast con avocado e tofu strapazzato + yogurt di soia e fragole": [
  "Sbriciola il tofu e cuocilo in padella antiaderente con curcuma, pepe e un pizzico di sale per 4-5 minuti.",
  "Tosta il pane e spalmaci l'avocado schiacciato con sale, pepe e limone.",
  "Completa con il tofu strapazzato.",
  "Servi con lo yogurt di soia e le fragole a pezzi a parte."],
 # ---------- spuntini ----------
 "Skyr e mela": ["Versa lo skyr in una ciotola.", "Aggiungi la mela a cubetti e la cannella a piacere."],
 "Lupini e mela": ["Sciacqua bene i lupini sotto l'acqua per togliere il sale.", "Mangiali con la mela."],
 "Fiocchi di latte, pera e noci": ["Versa i fiocchi di latte in una ciotola.", "Aggiungi la pera a cubetti e le noci spezzettate."],
 "Edamame e pera": ["Scongela gli edamame (4 minuti in acqua bollente oppure in frigo dalla sera prima) e scolali.", "Condiscili con un pizzico di sale e succo di limone.", "Mangiali con la pera."],
 "Skyr e arancia": ["Versa lo skyr in una ciotola.", "Mangialo con l'arancia a spicchi."],
 "Lupini e arancia": ["Sciacqua bene i lupini per togliere il sale.", "Mangiali con l'arancia a spicchi."],
 "Yogurt greco, frutti di bosco e noci": ["Versa lo yogurt in una ciotola.", "Aggiungi i frutti di bosco (se surgelati, scongelali 1 minuto al microonde) e le noci spezzettate."],
 "Yogurt di soia, frutti di bosco e noci": ["Versa lo yogurt di soia in una ciotola.", "Aggiungi i frutti di bosco (se surgelati, scongelali 1 minuto al microonde) e le noci spezzettate."],
 "Gallette con fiocchi di latte e pomodorini": ["Condisci i fiocchi di latte con sale, pepe e origano.", "Spalmali sulle gallette e completa con i pomodorini a fettine."],
 "Gallette con tofu affumicato e pomodorini": ["Taglia il tofu affumicato a fettine sottili.", "Disponilo sulle gallette con i pomodorini a fettine, un pizzico di sale e origano."],
 "Skyr e frutti di bosco": ["Versa lo skyr in una ciotola.", "Aggiungi i frutti di bosco (se surgelati, scongelali 1 minuto al microonde)."],
 "Lupini e kiwi": ["Sciacqua bene i lupini per togliere il sale.", "Mangiali con i kiwi sbucciati a fette."],
 "Bresaola, gallette e pomodorini": ["Condisci la bresaola con qualche goccia di limone e pepe.", "Servila con le gallette e i pomodorini."],
 "Edamame e pomodorini": ["Scongela gli edamame (4 minuti in acqua bollente oppure in frigo dalla sera prima) e scolali.", "Mescolali con i pomodorini a metà, un pizzico di sale e limone."],
 "Skyr, kiwi e mandorle": ["Versa lo skyr in una ciotola.", "Aggiungi i kiwi a cubetti e le mandorle tritate."],
 "Lupini, kiwi e mandorle": ["Sciacqua bene i lupini per togliere il sale.", "Mangiali con i kiwi a cubetti e le mandorle."],
 "Yogurt di soia, frutti di bosco e semi di lino": ["Versa lo yogurt di soia in una ciotola.", "Aggiungi i frutti di bosco e i semi di lino macinati."],
 "Yogurt greco, mela e noci": ["Versa lo yogurt in una ciotola.", "Aggiungi la mela a cubetti, le noci spezzettate e un pizzico di cannella."],
 "Yogurt di soia, mela e noci + lupini": ["Versa lo yogurt di soia in una ciotola con la mela a cubetti e le noci.", "Sciacqua i lupini e mangiali a parte."],
 "Mela e mandorle": ["Lava la mela e tagliala a spicchi.", "Mangiala con le mandorle."],
 "Hummus con carote e gallette": [
  "Sciacqua i ceci e frullali con tahina, succo di mezzo limone, mezzo spicchio d'aglio, cumino e un pizzico di sale.",
  "Aggiungi acqua fredda un cucchiaio alla volta fino a una crema liscia (se ne fai una dose per più giorni, dura 4-5 giorni in frigo).",
  "Servi con le carote a bastoncini e le gallette."],
 "Gallette con hummus e pomodorini": [
  "Sciacqua i ceci e frullali con tahina, succo di limone, aglio, cumino, sale e un cucchiaio d'acqua fredda alla volta fino a una crema liscia.",
  "Spalma l'hummus sulle gallette e completa con i pomodorini a fettine."],
 "Pera e cioccolato fondente": ["Lava la pera e tagliala a spicchi.", "Mangiala con un quadratino di cioccolato fondente."],
 "Edamame al limone": ["Cuoci gli edamame surgelati in acqua bollente per 4 minuti e scolali.", "Condiscili con succo di limone e un pizzico di sale; sono buoni caldi o freddi."],
 "Fiocchi di latte con pomodorini e gallette": ["Condisci i fiocchi di latte con i pomodorini a pezzetti, sale, pepe e origano.", "Servi con le gallette."],
 "Yogurt greco, kiwi e noci": ["Versa lo yogurt in una ciotola.", "Aggiungi i kiwi a cubetti e le noci spezzettate."],
 "Lupini, kiwi e noci": ["Sciacqua bene i lupini per togliere il sale.", "Mangiali con i kiwi a cubetti e le noci."],
 "Pera, mandorle e cioccolato fondente": ["Taglia la pera a spicchi.", "Mangiala con le mandorle e un quadratino di cioccolato fondente."],
 "Skyr e fragole": ["Versa lo skyr in una ciotola.", "Aggiungi le fragole a pezzi e le mandorle tritate."],
 "Edamame e fragole": ["Scongela gli edamame (4 minuti in acqua bollente oppure in frigo dalla sera prima) e condiscili con sale e limone.", "Mangiali con le fragole e le mandorle."],
 "Mandorle e arancia": ["Sbuccia l'arancia e dividila a spicchi.", "Mangiala con le mandorle."],
 "Yogurt greco, miele e noci": ["Versa lo yogurt in una ciotola.", "Completa con il miele a filo e le noci spezzettate."],
 "Yogurt di soia, noci e lupini": ["Versa lo yogurt di soia in una ciotola con lo sciroppo d'acero e le noci.", "Sciacqua i lupini e mangiali a parte."],
 # ---------- pre-allenamento e moduli ----------
 "Pane integrale, bresaola e banana": ["Farcisci il pane con la bresaola (qualche goccia di limone e pepe a piacere).", "Mangialo 60-90 minuti prima dell'allenamento, con la banana."],
 "Panino integrale con tofu e senape + banana": ["Taglia il tofu a fette di 1 cm e scaldale 2 minuti per lato in padella antiaderente con un pizzico di sale.", "Spalma il pane con un velo di senape e farciscilo con il tofu.", "Mangialo 60-90 minuti prima dell'allenamento, con la banana."],
 "Yogurt greco, banana e gallette": ["Versa lo yogurt in una ciotola con la banana a rondelle.", "Mangialo con le gallette 60-90 minuti prima dell'allenamento."],
 "Latte di soia, banana e gallette": ["Bevi il latte di soia con la banana e le gallette.", "Meglio 60-90 minuti prima dell'allenamento."],
 "Skyr, banana e datteri": ["Versa lo skyr in una ciotola con la banana a rondelle.", "Aggiungi i datteri snocciolati e tagliati a pezzi; mangialo 60-90 minuti prima dell'allenamento."],
 "Yogurt di soia, banana e datteri": ["Versa lo yogurt di soia in una ciotola con la banana a rondelle.", "Aggiungi i datteri snocciolati e tagliati a pezzi; mangialo 60-90 minuti prima dell'allenamento."],
 "Banana e gallette di riso": ["Solo se fai la sessione facoltativa del mercoledì.", "Mangia banana e gallette 45-60 minuti prima dell'allenamento."],
 "Banana, datteri e gallette": ["Solo se fai la sessione del mercoledì.", "Mangia banana, datteri e gallette 45-60 minuti prima dell'allenamento."],
 "Pane integrale, miele e banana": ["Tosta il pane e spalmaci il miele (sciroppo d'acero nella versione vegana).", "Mangialo con la banana circa 60 minuti prima della corsa."],
 "Aggiunta alla colazione: pane, miele e banana": ["Aggiungi alla colazione il pane tostato con il miele e la banana.", "Lascia almeno un'ora tra la colazione e la corsa delle 10."],
 "Aggiunta a cena: riso e skyr al miele": ["Cuoci il riso basmati in acqua salata per 10-12 minuti e servilo come contorno della cena.", "Come dessert: skyr con il miele (yogurt di soia nella versione vegana)."],
 "Aggiunta a cena: riso e yogurt greco al miele": ["Cuoci il riso basmati in acqua salata per 10-12 minuti e servilo come contorno della cena.", "Come dessert: yogurt greco con il miele (yogurt di soia e sciroppo d'acero nella versione vegana)."],
 "Recupero post-corsa": ["Entro un'ora dalla corsa mangia lo skyr con i datteri snocciolati a pezzi.", "Accompagna con le gallette (versione vegana: 100 g di lupini al posto dello skyr)."],
 "Frullato di recupero al cacao": ["Frulla latte, banana, avena, cacao e miele per 1 minuto (latte di soia e sciroppo d'acero nella versione vegana).", "Bevilo entro un'ora dalla fine della corsa."],
 "Yogurt greco ed energy balls al cacao": (["Prendi 2 energy balls (ricetta n. 12, preparate in anticipo).", "Mangiale con lo yogurt 60-90 minuti prima dell'allenamento."], 12),
 "Yogurt di soia ed energy balls al cacao": (["Prendi 2 energy balls (ricetta n. 12, preparate in anticipo).", "Mangiale con lo yogurt di soia e la banana 60-90 minuti prima dell'allenamento.", "I lupini, sciacquati, sono a parte."], 12),
 "Toast integrale con crema di arachidi e banana + latte": ["Tosta il pane e spalmaci la crema di arachidi.", "Completa con la banana a rondelle e bevi il latte; meglio 60-90 minuti prima dell'allenamento."],
 "Toast con crema di arachidi e banana + latte di soia": ["Tosta il pane e spalmaci la crema di arachidi.", "Completa con la banana a rondelle e bevi il latte di soia; meglio 60-90 minuti prima dell'allenamento."],
 "Skyr al miele con gallette e fragole": ["Mescola lo skyr con il miele.", "Mangialo con le gallette, le fragole e la banana 60-90 minuti prima dell'allenamento."],
 "Yogurt di soia, gallette, fragole e datteri": ["Versa lo yogurt di soia in una ciotola con le fragole a pezzi e i datteri.", "Mangialo con le gallette e la banana 60-90 minuti prima dell'allenamento."],
 # ---------- pranzi ----------
 "Insalata di farro, pollo e verdure grigliate": [
  "Cuoci il farro in acqua salata per circa 25 minuti (controlla i tempi sulla confezione), scolalo e passalo sotto l'acqua fredda.",
  "Taglia le verdure (zucchine, melanzane, peperoni) a fette e grigliale su una piastra rovente, 2-3 minuti per lato.",
  "Cuoci il petto di pollo alla piastra 4-5 minuti per lato e taglialo a striscioline.",
  "Taglia i pomodorini a metà e mescola tutto con il farro.",
  "Condisci con l'olio, sale, pepe e limone; si conserva in frigo fino al giorno dopo."],
 "Farro con seitan alla piastra e verdure": [
  "Cuoci il farro in acqua salata per circa 25 minuti, scolalo e passalo sotto l'acqua fredda.",
  "Griglia le verdure a fette su una piastra rovente, 2-3 minuti per lato.",
  "Taglia il seitan a fette e scottalo sulla piastra 2 minuti per lato, poi a striscioline.",
  "Mescola farro, verdure, seitan e pomodorini a metà e condisci con olio, sale, pepe e limone."],
 "Seitan al curry con riso e zucchine": [
  "Taglia il seitan a bocconcini e mescolalo con lo yogurt di soia, curry, curcuma, zenzero, aglio e succo di limone; lascialo insaporire almeno 15 minuti.",
  "Cuoci il riso basmati in acqua salata (10-12 minuti).",
  "In una padella scalda l'olio e cuoci le zucchine a rondelle per 5 minuti.",
  "Aggiungi il seitan con la sua salsa e cuoci 5 minuti a fuoco medio, con un goccio d'acqua se serve.",
  "Completa con prezzemolo o coriandolo e servi con il riso."],
 "Orzo tiepido con fagioli, pollo e verdure": [
  "Cuoci l'orzo in acqua salata per circa 20 minuti e scolalo.",
  "Cuoci il pollo alla piastra 4-5 minuti per lato e taglialo a cubetti.",
  "Salta le verdure a pezzi in padella con metà dell'olio per 5-6 minuti.",
  "Sciacqua i fagioli e unisci tutto all'orzo ancora tiepido.",
  "Condisci con il resto dell'olio, sale, pepe ed erbe a piacere."],
 "Orzo con fagioli, tempeh e verdure": [
  "Cuoci l'orzo in acqua salata per circa 20 minuti e scolalo.",
  "Sbollenta il tempeh 10 minuti, taglialo a cubetti e rosolalo in padella con metà dell'olio e un goccio di salsa di soia.",
  "Salta le verdure a pezzi nella stessa padella per 5-6 minuti.",
  "Sciacqua i fagioli e unisci tutto all'orzo, condendo con il resto dell'olio, sale e pepe."],
 "Pasta integrale al tonno e pomodorini + insalata": [
  "Porta a bollore l'acqua salata e cuoci la pasta integrale.",
  "Intanto taglia i pomodorini a metà e mettili in una ciotola con il tonno sgocciolato, 10 g d'olio, basilico o origano.",
  "Scola la pasta e condiscila con il tonno e i pomodorini (se la porti al lavoro, falla raffreddare: è ottima fredda).",
  "Servi con l'insalata condita con il resto dell'olio al momento."],
 "Pasta di lenticchie rosse con pomodorini ed edamame": [
  "Porta a bollore l'acqua salata, aggiungi gli edamame e dopo 1 minuto la pasta di lenticchie (cuoce in 6-8 minuti).",
  "Taglia i pomodorini a metà e condiscili con 5 g d'olio, sale e basilico.",
  "Scola pasta ed edamame e mescolali con i pomodorini; è buona anche fredda.",
  "Servi con l'insalata condita con il resto dell'olio."],
 "Insalatona di quinoa, ceci e tonno": [
  "Sciacqua la quinoa in un colino e cuocila in acqua salata per 15 minuti; scolala e falla raffreddare.",
  "Sciacqua i ceci e taglia i pomodorini a metà.",
  "Mescola quinoa, ceci, pomodorini, tonno sgocciolato e insalata.",
  "Condisci con olio, limone, sale e pepe."],
 "Insalatona di quinoa, ceci e tofu affumicato": [
  "Sciacqua la quinoa e cuocila in acqua salata per 15 minuti; scolala e falla raffreddare.",
  "Taglia il tofu affumicato a cubetti e, se ti piace croccante, rosolalo 3-4 minuti in padella antiaderente.",
  "Mescola quinoa, ceci sciacquati, pomodorini a metà, tofu e insalata.",
  "Condisci con olio, limone, sale e pepe."],
 "Tagliatelle al ragù magro + verdure": [
  "Trita finemente carota, sedano e cipolla (sono parte delle verdure) e falli appassire con l'olio a fuoco dolce per 5 minuti.",
  "Aggiungi il macinato e rosolalo a fuoco vivace, sgranandolo con il cucchiaio, finché perde il colore rosa.",
  "Unisci passata, sale e un bicchiere d'acqua e cuoci coperto a fuoco basso per almeno 45 minuti, mescolando ogni tanto (più cuoce, più è buono).",
  "Cuoci le tagliatelle in acqua salata e scolale al dente.",
  "Condiscile con il ragù e il Parmigiano; le altre verdure, al vapore o in padella, a parte."],
 "Cous cous integrale con pollo, ceci, verdure e menta": [
  "Metti il cous cous in una ciotola, coprilo con il doppio del suo volume di acqua bollente salata, copri e lascia 5 minuti; poi sgranalo con la forchetta.",
  "Taglia peperoni e zucchine a dadini e saltali in padella con metà dell'olio per 5-6 minuti.",
  "Cuoci il pollo a cubetti nella stessa padella per 6-7 minuti con un pizzico di cumino.",
  "Unisci al cous cous verdure, pollo, ceci sciacquati e pomodorini a pezzi.",
  "Condisci con il resto dell'olio, menta, limone e sale."],
 "Cous cous con ceci, tofu speziato e verdure": [
  "Idrata il cous cous con il doppio del suo volume di acqua bollente salata per 5 minuti, poi sgranalo.",
  "Taglia il tofu a cubetti e rosolalo in padella con l'olio, paprika e cumino finché è dorato.",
  "Salta peperoni e zucchine a dadini nella stessa padella per 5-6 minuti.",
  "Unisci tutto al cous cous con ceci sciacquati e pomodorini; condisci con menta, limone e sale."],
 "Farro alla nizzarda con tonno, fagiolini, pomodorini e uovo sodo": [
  "Cuoci il farro in acqua salata per circa 25 minuti, scolalo e raffreddalo sotto l'acqua.",
  "Rassoda l'uovo: 9 minuti dal bollore, poi in acqua fredda; sgusciato e a spicchi.",
  "Sbollenta i fagiolini spuntati per 7-8 minuti e passali in acqua fredda.",
  "Mescola farro, fagiolini a pezzi, pomodorini a metà e tonno sgocciolato.",
  "Condisci con olio, sale, pepe e qualche oliva o cappero, e completa con l'uovo."],
 "Farro con tofu affumicato, fagiolini e pomodorini": [
  "Cuoci il farro in acqua salata per circa 25 minuti, scolalo e raffreddalo.",
  "Sbollenta i fagiolini per 7-8 minuti e passali in acqua fredda.",
  "Taglia il tofu affumicato a cubetti.",
  "Mescola farro, fagiolini a pezzi, pomodorini a metà e tofu; condisci con olio, sale e pepe."],
 "Burrito bowl con tofu speziato": [
  "Cuoci il riso integrale (o usa quello precotto).",
  "Taglia il tofu a cubetti, condiscilo con paprika affumicata, cumino e origano e rosolalo in padella antiaderente finché è dorato.",
  "Prepara il pico de gallo con pomodori e cipolla rossa a dadini, coriandolo, lime e sale.",
  "Scalda i fagioli con un pizzico di cumino e salta i peperoni a listarelle per 3-4 minuti.",
  "Componi la bowl con riso, tofu, fagioli, mais, peperoni, pico de gallo, avocado e lo yogurt di soia con lime."],
 "Pasta integrale al pesto leggero con pollo, fagiolini e pomodorini": [
  "Porta a bollore l'acqua salata: cuoci i fagiolini a pezzi per 5 minuti, poi aggiungi la pasta nella stessa acqua.",
  "Intanto cuoci il pollo alla piastra e taglialo a striscioline.",
  "Pesto: frulla un mazzetto di basilico con pinoli, olio, Parmigiano, un pizzico di sale e un cucchiaio d'acqua di cottura.",
  "Scola pasta e fagiolini e condiscili con il pesto, il pollo e i pomodorini a metà."],
 "Pasta di lenticchie al pesto con fagiolini e pomodorini": [
  "Porta a bollore l'acqua salata: cuoci i fagiolini a pezzi per 5 minuti, poi aggiungi la pasta di lenticchie (6-8 minuti).",
  "Pesto: frulla un mazzetto di basilico con pinoli, olio, un pizzico di sale e un cucchiaio d'acqua di cottura (lievito alimentare a piacere).",
  "Scola pasta e fagiolini e condiscili con il pesto e i pomodorini a metà."],
 "Insalata di riso venere con pollo, edamame e verdure croccanti": [
  "Cuoci il riso venere in acqua salata (circa 18 minuti, vedi confezione), scolalo e raffreddalo.",
  "Cuoci il pollo alla piastra e taglialo a cubetti; cuoci gli edamame 4 minuti in acqua bollente.",
  "Taglia carote e peperoni a julienne o a dadini piccoli.",
  "Condimento: olio, succo di limone, un cucchiaino di salsa di soia e zenzero grattugiato.",
  "Mescola tutto e condisci al momento di mangiare."],
 "Insalata di riso venere con tofu, edamame e verdure": [
  "Cuoci il riso venere in acqua salata (circa 18 minuti), scolalo e raffreddalo.",
  "Rosola il tofu a cubetti in padella antiaderente; cuoci gli edamame 4 minuti in acqua bollente.",
  "Taglia carote e peperoni a julienne o a dadini piccoli.",
  "Mescola tutto e condisci al momento con olio, limone, un cucchiaino di salsa di soia e zenzero."],
 "Burger di manzo fatto in casa con panino integrale e patate al forno": [
  "Scalda il forno a 200°C: taglia le patate a spicchi, condiscile con 10 g d'olio, rosmarino e sale e cuocile 35 minuti, girandole a metà.",
  "Impasta il macinato con sale, pepe e un cucchiaino di senape e forma un burger alto circa 1,5 cm.",
  "Cuocilo su una piastra rovente, 3-4 minuti per lato, senza schiacciarlo.",
  "Tosta il pane e farciscilo con il burger, l'insalata e il pomodoro a fette.",
  "Servi con le patate e il resto dell'olio sull'insalata."],
 "Burger di tempeh con panino integrale e patate al forno": [
  "Scalda il forno a 200°C e cuoci le patate a spicchi con metà dell'olio, rosmarino e sale per 35 minuti.",
  "Taglia il tempeh a fette di 1 cm e sbollentalo 5 minuti.",
  "Marinalo 15 minuti (o dalla sera prima) con salsa di soia e paprika affumicata.",
  "Cuocilo sulla piastra con il resto dell'olio, 3 minuti per lato.",
  "Farcisci il pane tostato con tempeh, insalata e pomodoro e servi con le patate."],
 "Paella di verdure con ceci e tofu affumicato": [
  "In una padella larga soffriggi cipolla, aglio e peperoni a listarelle con l'olio per 5 minuti.",
  "Aggiungi il riso e tostalo 1 minuto, poi paprika dolce e passata.",
  "Versa 300 ml di brodo vegetale caldo con lo zafferano sciolto, aggiungi ceci e piselli e cuoci 16-18 minuti senza mescolare.",
  "Negli ultimi 5 minuti adagia sopra il tofu affumicato a cubetti.",
  "Lascia riposare 5 minuti coperta e servi con limone e prezzemolo."],
 # ---------- cene ----------
 "Tempeh al forno con patate e broccoli": [
  "Scalda il forno a 200°C: taglia le patate a spicchi, condiscile con l'olio e cuocile 35 minuti.",
  "Taglia il tempeh a fette e marinalo 10 minuti con succo di limone, salsa di soia e paprika.",
  "Negli ultimi 15 minuti aggiungi il tempeh nella teglia con le patate, girandolo a metà.",
  "Cuoci i broccoli al vapore per 6-7 minuti e condiscili con limone."],
 "Merluzzo in guazzetto con ceci, pane e insalata": [
  "In una padella larga scalda 5 g d'olio con uno spicchio d'aglio, aggiungi la passata e i ceci sciacquati e cuoci 5 minuti.",
  "Adagia il merluzzo scongelato a pezzi nel sugo, copri e cuoci 8-10 minuti a fuoco dolce senza girarlo.",
  "Completa con prezzemolo tritato e 5 g d'olio a crudo.",
  "Servi con il pane tostato e l'insalata condita con il resto dell'olio."],
 "Guazzetto di ceci e tofu": [
  "In una padella larga scalda l'olio con uno spicchio d'aglio, aggiungi la passata e i ceci sciacquati e cuoci 5 minuti.",
  "Unisci il tofu a cubetti, copri e cuoci 8 minuti a fuoco dolce perché si insaporisca.",
  "Completa con prezzemolo e pepe.",
  "Servi con il pane tostato e l'insalata condita al momento."],
 "Tacchino alla piastra, patate dolci e verdure": [
  "Scalda il forno a 200°C: taglia le patate dolci a spicchi, condiscile con 5 g d'olio e paprika e cuocile 30 minuti.",
  "Taglia le verdure a pezzi e saltale in padella (o grigliale) per 6-8 minuti.",
  "Cuoci la fesa di tacchino su una piastra rovente, 2-3 minuti per lato, con sale, pepe e rosmarino.",
  "Servi con le patate e le verdure condite con il resto dell'olio e limone."],
 "Frittata al forno di albumi e verdure, patate dolci": [
  "Scalda il forno a 180°C e cuoci le patate dolci a spicchi (le puoi infornare insieme alla frittata, 30 minuti in tutto).",
  "Taglia le verdure a pezzi piccoli e saltale in padella con l'olio per 5 minuti.",
  "Sbatti uovo e albumi con sale, pepe ed erbe e mescolali con le verdure.",
  "Versa in una teglia piccola con carta forno e cuoci 20-25 minuti, finché è soda al centro."],
 "Tagliata di manzo, patate e rucola con scaglie di Parmigiano": [
  "Scalda il forno a 200°C: taglia le patate a spicchi, condiscile con 5 g d'olio e rosmarino e cuocile 35 minuti.",
  "Tira fuori la carne dal frigo 20 minuti prima, perché cuocia in modo uniforme.",
  "Cuoci la fesa su una piastra rovente 2-3 minuti per lato (dipende dallo spessore e da come la preferisci).",
  "Lasciala riposare 3 minuti su un tagliere, poi tagliala a fette oblique.",
  "Servila sulla rucola con le scaglie di Parmigiano, il resto dell'olio, sale e pepe, e le patate accanto."],
 "Orata/branzino al cartoccio, patate e spinaci": [
  "Scalda il forno a 200°C e cuoci le patate a fette sottili con metà dell'olio per 15 minuti.",
  "Prepara il cartoccio con carta forno: filetti, pomodorini o limone a fette, prezzemolo, sale e qualche goccia d'olio; chiudilo bene.",
  "Infornalo insieme alle patate per 15 minuti.",
  "Intanto salta gli spinaci in padella con l'aglio e il resto dell'olio per 2-3 minuti.",
  "Apri il cartoccio a tavola e servi con patate e spinaci."],
 "Sgombro al forno con pomodorini, verdure e pane": [
  "Scalda il forno a 200°C.",
  "Metti lo sgombro in una teglia con i pomodorini a metà, le verdure a pezzi, olio, sale, origano e limone.",
  "Cuoci 15-20 minuti, finché la carne si stacca facilmente dalla lisca.",
  "Servi con il pane integrale tostato."],
 "Seitan alla pizzaiola con verdure e pane": [
  "In una padella scalda metà dell'olio con uno spicchio d'aglio, aggiungi la passata, origano e capperi e cuoci 5 minuti.",
  "Adagia il seitan a fette nel sugo e cuoci 10 minuti, girandolo a metà.",
  "Intanto salta o griglia le verdure con il resto dell'olio.",
  "Servi con il pane integrale per raccogliere il sugo."],
 "Merluzzo al forno con minestrone di verdure e fagioli": [
  "Minestrone: in una pentola fai appassire cipolla, carota e sedano (parte delle verdure) con metà dell'olio per 5 minuti.",
  "Aggiungi le altre verdure a cubetti e i fagioli, copri d'acqua o brodo e cuoci 25 minuti.",
  "Scalda il forno a 200°C e cuoci il merluzzo scongelato su carta forno con limone, prezzemolo e sale per 12-15 minuti.",
  "Servi il minestrone con il resto dell'olio a crudo, il pesce e il pane tostato."],
 "Minestrone di verdure e fagioli con tofu croccante": ([
  "Minestrone: fai appassire cipolla, carota e sedano con metà dell'olio, aggiungi le altre verdure a cubetti e i fagioli, copri d'acqua o brodo e cuoci 25 minuti.",
  "Tofu croccante: pressalo 10 minuti tra carta da cucina, taglialo a cubetti, passalo in un cucchiaino di amido e cuocilo in forno a 200°C per 25 minuti, girandolo a metà (come nella ricetta n. 5).",
  "Servi il minestrone con il tofu sopra, il resto dell'olio a crudo e il pane tostato."], 5),
 "Trota salmonata al forno, patate dolci e cavolfiore arrosto": [
  "Scalda il forno a 200°C.",
  "Taglia le patate dolci a spicchi e il cavolfiore a cimette, condiscili con 10 g d'olio, sale e spezie e cuocili 30 minuti.",
  "Negli ultimi 12 minuti aggiungi la trota nella teglia con limone, timo e il resto dell'olio.",
  "Servi appena pronta."],
 "Tempeh glassato con patate dolci e cavolfiore arrosto": [
  "Scalda il forno a 200°C e cuoci patate dolci a spicchi e cavolfiore a cimette con metà dell'olio per 30 minuti.",
  "Taglia il tempeh a fette e sbollentalo 10 minuti.",
  "Rosolalo in padella con il resto dell'olio finché è dorato.",
  "Aggiungi salsa di soia e sciroppo d'acero con 2 cucchiai d'acqua e glassa 2 minuti, finché è lucido.",
  "Servi con le verdure arrosto."],
 "Polpette di lenticchie e soia al sugo, purè e spinaci": [
  "Idrata la soia in brodo caldo 10 minuti e strizzala; frulla grossolanamente le lenticchie con cipolla, spezie e prezzemolo.",
  "Unisci soia e avena, impasta e forma 8-10 polpette; lasciale 15 minuti in frigo.",
  "Prepara il sugo con 5 g d'olio, aglio, passata e basilico (10 minuti), poi cuoci le polpette nel sugo coperte per 15 minuti.",
  "Lessa le patate, schiacciale e montale con il latte di soia caldo, 5 g d'olio, noce moscata e sale.",
  "Salta gli spinaci con il resto dell'olio e servi tutto insieme."],
 "Curry di ceci, tofu e spinaci con riso e raita di soia": [
  "Soffriggi cipolla, aglio e zenzero tritati nell'olio per 4 minuti; aggiungi garam masala, curcuma e cumino e tostali 1 minuto.",
  "Unisci passata, ceci, il tofu a cubetti e mezzo bicchiere d'acqua; cuoci 12-15 minuti.",
  "Aggiungi gli spinaci e lasciali appassire 2-3 minuti. Intanto cuoci il riso basmati.",
  "Raita: cetriolo grattugiato e strizzato, yogurt di soia, menta, limone e sale.",
  "Servi il curry con il riso e la raita a parte."],
 "Fajitas di seitan con peperoni e piadine integrali": [
  "Piadine: impasta farina, un pizzico di bicarbonato e di sale, 5 g d'olio e 40 ml d'acqua tiepida; riposo 15 minuti.",
  "Taglia il seitan a striscioline e condiscilo con paprika, cumino, aglio in polvere e lime.",
  "Stendi l'impasto in 2 piadine sottili e cuocile in padella rovente, 1-2 minuti per lato.",
  "Nella stessa padella salta peperoni e cipolla con il resto dell'olio per 5-6 minuti, poi il seitan per 3 minuti.",
  "Componi le fajitas con seitan, verdure, avocado e lo yogurt di soia con lime ed erba cipollina."],
 "Tofu teriyaki con riso basmati e broccoli": [
  "Asciuga il tofu e taglialo a cubi o a fette.",
  "Glassa: salsa di soia, sciroppo d'acero, zenzero grattugiato, aglio, 3 cucchiai d'acqua e un cucchiaino di amido.",
  "Cuoci il riso basmati (10-12 minuti) e i broccoli al vapore (6-7 minuti).",
  "Rosola il tofu in padella con l'olio finché è dorato, poi versa la glassa e lasciala addensare 1 minuto.",
  "Servi con riso, broccoli e qualche goccia di lime."],
 "Pizza integrale con verdure e tofu affumicato": ([
  "Impasto: come nella ricetta n. 9 (lievitazione 3-4 ore, o 24 ore in frigo).",
  "Griglia zucchine e melanzane a fette sottili e taglia il tofu affumicato a cubetti.",
  "Stendi l'impasto su una teglia con carta forno, condisci con passata e origano e cuoci a 250°C per 8 minuti.",
  "Aggiungi verdure e tofu e prosegui per 5-7 minuti; completa con l'olio a crudo e il basilico."], 9),
 "Nasello gratinato alle erbe con finocchi al forno e pane": [
  "Scalda il forno a 200°C: taglia finocchi e patate a fette, condiscili con metà dell'olio e cuocili 25 minuti.",
  "Frulla 10 g di pane con prezzemolo, scorza di limone e Parmigiano.",
  "Disponi il nasello scongelato su carta forno, spennellalo con il resto dell'olio e coprilo con la panatura.",
  "Infornalo con le verdure per gli ultimi 15 minuti, finché la crosta è dorata.",
  "Servi con il pane rimasto."],
 "Vellutata di lenticchie rosse e carote con tofu croccante e crostini": [
  "Soffriggi mezza cipolla e le carote a rondelle con metà dell'olio per 5 minuti.",
  "Aggiungi le lenticchie e brodo o acqua fino a coprire; cuoci 15 minuti e frulla fino a una crema.",
  "Rosola il tofu a cubetti in padella con il resto dell'olio finché è croccante.",
  "Tosta il pane a crostini.",
  "Servi la vellutata con tofu, crostini e un pizzico di pepe o curcuma."],
}

def apply(d):
    used, miss = set(), []
    for ph in ('f1', 'f2'):
        recs = {r['n']: r for r in d[ph]['recipes']}
        for day in d[ph]['days']:
            for m in day['meals']:
                for o in (m, m.get('alt')):
                    if not o: continue
                    t = o['title']
                    if t in LINK[ph]:
                        n = LINK[ph][t]; o['ref'] = n; o['steps'] = recs[n]['steps']; used.add(t)
                    elif t in MEAL:
                        v = MEAL[t]
                        if isinstance(v, tuple): o['steps'], o['ref'] = v
                        else: o['steps'] = v
                        used.add(t)
                    else: miss.append((ph, t))
    extra = set(MEAL) - used
    if miss or extra: raise SystemExit(f'Pasti senza passaggi: {miss}\nPassaggi non usati: {extra}')
