# Preparazioni del giorno prima e passaggi estesi delle ricette.
# PREP: cosa fare la sera prima (oltre allo scongelamento, che è calcolato dagli ingredienti).
# BOX: consiglio per il pranzo portato al lavoro. PL: riga completa per il pranzo al lavoro (sostituisce quella generica).
# NOTHAW: ricette in cui lo scongelamento è già compreso in PREP. ALT: preparazioni delle alternative vegane del menu.
# STEPS: passaggi riscritti dove quelli originali erano troppo compressi.

PREP = {
 # ricette del piano
 "Overnight oats «tiramisù»": "prepara gli overnight oats (passaggi 1-4) e lasciali in frigo tutta la notte: al mattino aggiungi solo cacao e noci.",
 "Tagliatelle al ragù di soia": "prepara il ragù di soia (passaggi 1-4): il giorno dopo è più saporito e ti resta da cuocere solo la pasta.",
 "Tofu croccante al forno con riso integrale e verdure saltate": "pressa il tofu e mettilo a marinare in frigo con soia, zenzero e aglio (passaggi 1-2): più marina, più è saporito.",
 "Pollo al curry e yogurt con riso basmati e zucchine": "metti il pollo a bocconcini a marinare in frigo con yogurt, spezie, aglio, zenzero e limone (passaggio 1).",
 "Hummus leggero con gallette e verdure croccanti": "se lo mangi fuori casa, frulla l'hummus stasera e tienilo in frigo (dura 4-5 giorni); verdure e gallette a parte.",
 "Granola croccante senza olio": "se la granola è finita, preparane una dose intera: deve raffreddarsi nella teglia per diventare croccante e dura 2 settimane.",
 "Muffin di avena e mirtilli": "controlla che siano rimasti 2 muffin; se sono finiti, preparane una dose (durano 4 giorni in frigo).",
 "Fajitas di manzo con piadine integrali fatte in casa": "taglia il manzo a striscioline e mettilo a marinare in frigo con paprika, cumino e aglio; il lime aggiungilo poco prima di cuocere, così la carne resta tenera.",
 "Pizza integrale fatta in casa con verdure e mozzarella light": "prepara l'impasto (passaggio 1) e lascialo lievitare in frigo per 24 ore, coperto.",
 "Energy balls al cacao e datteri": "se le energy balls sono finite, preparane una dose (12 palline): devono stare almeno 30 minuti in frigo e durano una settimana.",
 # colazioni
 "Chia pudding alla vaniglia con frutti di bosco": "prepara il chia pudding (passaggi 1-2) e lascialo in frigo tutta la notte.",
 "Bircher müesli con mela grattugiata": "prepara il bircher (passaggi 1-2) e lascialo in frigo tutta la notte: al mattino aggiungi solo le noci.",
 "Overnight oats alla pera e zenzero": "prepara gli overnight oats (passaggi 1-3) e lasciali in frigo tutta la notte.",
 "Congee di riso con tofu e zenzero": "cuoci il congee stasera (passaggi 1-2): al mattino scaldalo con un goccio d'acqua e aggiungi tofu, pak choi ed edamame.",
 "Colazione giapponese: tamagoyaki, riso e zuppa di miso": "cuoci il riso stasera (o tieni da parte quello avanzato): al mattino basta scaldarlo.",
 "Smoothie bowl al tè matcha con skyr": "taglia la banana a rondelle e mettila in freezer: va frullata congelata.",
 # spuntini
 "Barrette di avena, arachidi e datteri": "se le barrette sono finite, preparane una dose (6 barrette): devono rassodare almeno 1 ora in frigo e durano 5 giorni.",
 "Hummus di lenticchie con carote e gallette": "se lo mangi fuori casa, frulla l'hummus stasera e tienilo in frigo; carote e gallette a parte.",
 "Ceci croccanti al forno e una mela": "tosta i ceci stasera (passaggi 1-4): restano croccanti 2-3 giorni in un barattolo chiuso.",
 "Edamame alla soia e zenzero": "se lo mangi fuori casa, cuoci e condisci gli edamame stasera e tienili in frigo: sono buoni anche freddi.",
 "Crostini integrali con mousse di tonno e limone": "se lo mangi fuori casa, prepara la mousse di tonno stasera e tienila in frigo; il pane a parte, così non si inzuppa.",
 "Uovo sodo, fiocchi di latte e crudité": "se lo mangi fuori casa, rassoda l'uovo e taglia le verdure stasera: in frigo si conservano fino a domani.",
 "Involtini di zucchine grigliate con tacchino e fiocchi di latte": "se lo mangi fuori casa, prepara gli involtini stasera e tienili in frigo coperti.",
 "Budino di chia al cacao con skyr e fragole": "prepara il budino di chia (passaggi 1-2): deve stare in frigo almeno 2 ore, meglio tutta la notte.",
 "Mix croccante di edamame, ceci tostati e mandorle": "prepara il mix stasera: scongela gli edamame in acqua calda per 5 minuti, asciugali bene e tosta tutto (passaggi 1-3). Resta croccante 2 giorni in un barattolo chiuso.",
 "Tzatziki con crudité e crostini integrali": "se lo mangi fuori casa, prepara lo tzatziki stasera: in frigo diventa anche più saporito.",
 "Muffin salati di albumi e verdure": "se i muffin salati sono finiti, preparane una dose (6 muffin): durano 3 giorni in frigo.",
 "Crema di cannellini al limone su gallette": "se la mangi fuori casa, frulla la crema stasera e tienila in frigo; gallette e pomodorini a parte.",
 "Tofu marinato alla soia con kiwi": "taglia il tofu a cubetti e mettilo a marinare in frigo con soia, zenzero e lime: più riposa, più è saporito.",
 "Onigiri al tonno": "se li mangi fuori casa, prepara gli onigiri stasera e tienili in frigo avvolti nella pellicola; l'alga mettila al momento, così resta croccante.",
 "Involtini vietnamiti con tofu (gỏi cuốn)": "se li mangi fuori casa, preparali stasera e avvolgili uno per uno nella pellicola; la salsa in un contenitorino a parte.",
 "Chana chaat, insalata di ceci speziata": "metti gli edamame a scongelare in frigo.",
 "Tempeh croccante al sesamo con carote": "se lo mangi fuori casa, cuoci il tempeh stasera: è buono anche freddo.",
 # pranzi e cene
 "Merluzzo al miso con riso e pak choi": "metti il merluzzo ancora surgelato a scongelare in frigo, già spalmato di miso, mirin e zenzero: marina mentre si scongela.",
}

PL = {
 "Merluzzo al miso con riso e pak choi": "scongela il merluzzo (in un sacchetto chiuso in acqua fredda bastano 30-40 minuti), spalmalo con miso, mirin e zenzero e lascialo marinare almeno 1 ora; poi cuocilo con il riso e il pak choi e porta tutto al lavoro.",
}
NOTHAW = {"Merluzzo al miso con riso e pak choi", "Involtini di zucchine grigliate con tacchino e fiocchi di latte"}  # negli involtini la fesa è già cotta (arrosto)

BOX = {
 "Insalata di orzo, salmone, zucchine e limone": "condiscila con olio e limone al momento",
 "Poke bowl di tonno, riso ed edamame": "avocado e condimento in un contenitorino a parte",
 "Wrap integrali di tacchino, peperoni e salsa allo yogurt": "piadine, ripieno e salsa separati, farcisci al momento",
 "Piadina integrale con bresaola, rucola e fiocchi di latte": "piadina e ripieno separati, farcisci al momento così non si inzuppa",
 "Piadina di ceci con tacchino e verdure grigliate": "piadina e ripieno separati, farcisci al momento",
 "Tacos di fagioli neri e tofu": "tortillas e ripieno separati, farcisci al momento",
 "Tacos di pesce con cavolo e salsa allo yogurt": "tortillas, pesce, cavolo e salsa separati, farcisci al momento",
 "Souvlaki di pollo con pita e tzatziki": "pane, pollo e tzatziki separati",
 "Zuppa di lenticchie e zucca con crostini": "la zuppa in un thermos o in un contenitore da scaldare, i crostini a parte",
 "Zuppa di lenticchie rosse, curcuma e zenzero": "la zuppa in un thermos o in un contenitore da scaldare",
 "Zuppa di borlotti, cavolo nero e farro": "la zuppa in un thermos o in un contenitore da scaldare",
 "Zuppa di pollo, verdure e quinoa": "la zuppa in un thermos o in un contenitore da scaldare",
 "Minestra di orzo, piselli e merluzzo": "la minestra in un thermos o in un contenitore da scaldare",
 "Soba fredde con edamame, tofu e sesamo": "condimento a parte, da versare al momento",
 "Gado-gado, insalata indonesiana con salsa di arachidi": "salsa di arachidi in un contenitorino a parte",
 "Insalata tiepida di pollo e lenticchie": "condimento a parte, da versare al momento",
 "Sgombro alla griglia con insalata di farro, finocchi e arancia": "condisci l'insalata al momento",
 "Tortilla al forno di albumi, zucchine e patate": "è ottima anche fredda",
 "Bibimbap con tofu e uovo": "salsa piccante a parte",
 "Bún thịt nướng, maiale alla citronella con vermicelli": "condimento a parte, da versare al momento",
 "Tofu alla citronella con vermicelli (bún)": "condimento a parte, da versare al momento",
}

# alternative vegane del menu: (fase, giorno, titolo dell'alternativa) -> preparazione
ALT = {
 ('f1', 0, "Farro con seitan alla piastra e verdure"): "cuoci il farro, griglia il seitan e le verdure e porta tutto al lavoro in un contenitore.",
 ('f1', 1, "Edamame e pera"): "metti gli edamame a scongelare in frigo.",
 ('f1', 1, "Seitan al curry con riso e zucchine"): "cuoci il seitan al curry con lo yogurt di soia, il riso basmati e le zucchine e porta tutto al lavoro.",
 ('f1', 2, "Orzo con fagioli, tempeh e verdure"): "cuoci l'orzo e il tempeh; prepara l'insalata tiepida con fagioli e verdure e porta tutto al lavoro.",
 ('f1', 3, "Pasta di lenticchie rosse con pomodorini ed edamame"): "cuoci la pasta di lenticchie e condiscila con pomodorini ed edamame: domani la mangi fredda (l'insalata a parte, condita al momento).",
 ('f1', 4, "Overnight oats con yogurt e latte di soia"): "prepara gli overnight oats con yogurt e latte di soia e mela e mettili in frigo.",
 ('f1', 4, "Edamame e pomodorini"): "metti gli edamame a scongelare in frigo.",
 ('f1', 5, "Insalatona di quinoa, ceci e tofu affumicato"): "cuoci la quinoa e mettila in frigo: per l'insalatona deve essere ben fredda.",
 ('f1', 6, "Tagliatelle di semola al ragù di soia + verdure"): "prepara il ragù di soia (ricetta n. 3, passaggi 1-4): il giorno dopo è più saporito e ti resta da cuocere solo la pasta.",
 ('f2', 0, "Cous cous con ceci, tofu speziato e verdure"): "prepara il cous cous con ceci, tofu speziato e verdure e mettilo in frigo.",
 ('f2', 1, "Farro con tofu affumicato, fagiolini e pomodorini"): "cuoci il farro e sbollenta i fagiolini; unisci tofu affumicato e pomodorini e porta tutto al lavoro.",
 ('f2', 2, "Smoothie bowl con yogurt e latte di soia"): "taglia una banana a rondelle e mettila in freezer per lo smoothie bowl.",
 ('f2', 2, "Burrito bowl con tofu speziato"): "cuoci il riso integrale e il tofu speziato, prepara il pico de gallo per la burrito bowl (avocado e yogurt a parte).",
 ('f2', 3, "Chia pudding al cacao con avena e banana"): "prepara il chia pudding al cacao con avena e latte di soia e lascialo in frigo tutta la notte.",
 ('f2', 3, "Gallette con hummus e pomodorini"): "se lo mangi fuori casa, frulla l'hummus stasera e tienilo in frigo.",
 ('f2', 3, "Pasta di lenticchie al pesto con fagiolini e pomodorini"): "cuoci la pasta di lenticchie e i fagiolini, condisci con il pesto e i pomodorini e porta tutto al lavoro.",
 ('f2', 4, "Overnight oats al cacao con latte e yogurt di soia"): "prepara gli overnight oats al cacao con latte e yogurt di soia e mettili in frigo.",
 ('f2', 4, "Insalata di riso venere con tofu, edamame e verdure"): "cuoci il riso venere e il tofu, scongela gli edamame e taglia le verdure; condisci al momento.",
 ('f2', 5, "Edamame e fragole"): "metti gli edamame a scongelare in frigo.",
 ('f2', 5, "Burger di tempeh con panino integrale e patate al forno"): "metti il tempeh a fette a marinare in frigo con salsa di soia e paprika affumicata.",
 ('f2', 5, "Pizza integrale con verdure e tofu affumicato"): "prepara l'impasto della pizza integrale e lascialo lievitare in frigo per 24 ore (ricetta n. 9).",
}

STEPS = {
 "Pasta integrale con broccoli, tonno e pinoli": [
  "Porta a bollore abbondante acqua salata e dividi i broccoli in cimette piccole (pela e taglia a rondelle anche il gambo).",
  "Butta i broccoli nell'acqua e dopo 5 minuti aggiungi la pasta integrale: cuociono insieme.",
  "Intanto in una padella larga scalda l'olio con l'aglio schiacciato e il peperoncino per 1 minuto, togli l'aglio e tosta i pinoli finché sono dorati.",
  "Aggiungi il tonno sgocciolato e sgranalo con la forchetta per 1 minuto.",
  "Scola pasta e broccoli tenendo da parte un mestolo d'acqua di cottura; saltali in padella con l'acqua, schiacciando qualche cimetta per fare una crema, e completa con la scorza di limone."],
 "Pollo alla cacciatora leggero con patate": [
  "Scalda il forno a 200°C: taglia le patate a spicchi, condiscile con 5 g d'olio e rosmarino e infornale per 35 minuti, girandole a metà.",
  "Taglia il pollo a pezzi grandi, la cipolla a fette e i peperoni a listarelle.",
  "In una casseruola rosola il pollo con il resto dell'olio, l'aglio e il rosmarino per 5 minuti, finché è dorato su tutti i lati.",
  "Sfuma con il vino (facoltativo) e lascialo evaporare; aggiungi cipolla e peperoni e cuoci 3 minuti.",
  "Unisci passata, alloro e olive, copri e cuoci 25 minuti a fuoco dolce, con un goccio d'acqua se il sugo si asciuga troppo.",
  "Togli l'alloro, regola di sale e pepe e servi con le patate."],
 "Polpette di merluzzo e patate con insalata": [
  "Lessa le patate con la buccia per 25 minuti (o 6-7 minuti al microonde, bucherellate), poi pelale e schiacciale.",
  "Asciuga bene il merluzzo scongelato con carta da cucina e frullalo crudo a scatti.",
  "Unisci patate, albume, prezzemolo, scorza di limone, aglio in polvere, sale e pepe: l'impasto deve essere morbido ma modellabile (se è troppo molle, aggiungi un cucchiaio di pane frullato).",
  "Frulla il pane integrale a briciole, forma 8 polpette e passale nel pane.",
  "Disponile su una teglia con carta forno, spennellale con 5 g d'olio e cuoci a 200°C per 20 minuti, girandole a metà.",
  "Servi con l'insalata condita con il resto dell'olio e un po' di limone."],
 "Wrap integrali di tacchino, peperoni e salsa allo yogurt": [
  "Impasta la farina con 5 g d'olio, un pizzico di sale e di bicarbonato e circa 40 ml di acqua tiepida fino a un panetto liscio; lascialo riposare 10 minuti coperto.",
  "Dividilo in 2 e stendi due piadine sottili con il mattarello.",
  "Cuoci ogni piadina in una padella rovente senza grassi, 1-2 minuti per lato, e tienile coperte con un canovaccio perché restino morbide.",
  "Taglia il tacchino a striscioline e i peperoni a listarelle e condiscili con paprika, origano e aglio in polvere.",
  "Nella stessa padella salta i peperoni con il resto dell'olio per 5 minuti, poi aggiungi il tacchino e cuoci 4-5 minuti a fuoco vivace.",
  "Mescola lo yogurt con limone ed erba cipollina, farcisci le piadine con tacchino, peperoni, insalata e salsa e arrotolale."],
 "Chili sin carne con riso": [
  "Idrata la soia nel brodo caldo per 10 minuti e strizzala bene.",
  "Soffriggi cipolla, aglio e peperoni a dadini nell'olio per 5 minuti.",
  "Aggiungi la soia con cumino, paprika affumicata, origano e peperoncino e rosolala 3 minuti a fuoco vivace.",
  "Unisci passata, fagioli scolati e mais e cuoci 20 minuti a fuoco dolce, con un goccio di brodo se si asciuga. Intanto cuoci il riso basmati (10-12 minuti).",
  "Servi il chili con il riso."],
 "Curry di tofu e zucca con riso basmati": [
  "Asciuga il tofu, taglialo a cubetti e rosolalo con metà dell'olio finché è dorato su tutti i lati; tienilo da parte.",
  "Nella stessa padella soffriggi cipolla, aglio e zenzero tritati con il resto dell'olio per 3 minuti, poi aggiungi curry e curcuma e tostali 1 minuto.",
  "Unisci la zucca a cubetti e mezzo bicchiere d'acqua e cuoci coperto 15 minuti, finché è morbida.",
  "Intanto cuoci il riso basmati (10-12 minuti).",
  "A fuoco spento unisci il tofu e lo yogurt di soia, mescola e servi con il riso e il coriandolo."],
 "Burger di tacchino e zucchine con patate dolci al forno": [
  "Taglia le patate dolci a spicchi, condiscile con metà dell'olio e la paprika e cuocile in forno a 200°C per 30 minuti, girandole a metà.",
  "Trita finemente la fesa di tacchino al mixer (o comprala già macinata).",
  "Grattugia le zucchine, salale leggermente e strizzale bene con le mani: se restano bagnate i burger si sfaldano.",
  "Impasta tacchino, zucchine, avena, prezzemolo, aglio in polvere, sale e pepe e forma 2 burger alti circa 1,5 cm; se hai tempo, lasciali 15 minuti in frigo.",
  "Cuocili su una piastra ben calda e appena unta, 4-5 minuti per lato, senza schiacciarli.",
  "Servi con le patate dolci e l'insalata condita con il resto dell'olio."],
 "Manzo saltato con broccoli e riso": [
  "Metti a cuocere il riso basmati (10-12 minuti).",
  "Taglia il manzo a listarelle sottili e mescolalo con amido, salsa di soia e zenzero grattugiato.",
  "Sbollenta le cimette di broccoli per 3 minuti e scolale.",
  "Salta il manzo in padella rovente con l'olio per 2 minuti, poi aggiungi broccoli, aglio e un goccio d'acqua per altri 2 minuti: la salsa diventa lucida.",
  "Servi sul riso con lime e peperoncino."],
 "Spiedini di pollo e verdure con cous cous integrale": [
  "Taglia il pollo a cubetti e marinalo 15 minuti con metà dell'olio, paprika, origano e limone.",
  "Infilzalo sugli spiedini alternandolo con peperoni e zucchine a pezzi.",
  "Cuoci gli spiedini sulla piastra o in forno a 220°C per 12-15 minuti, girandoli a metà.",
  "Intanto idrata il cous cous con il doppio del suo volume di acqua bollente salata per 5 minuti, sgranalo e condiscilo con menta e il resto dell'olio.",
  "Servi gli spiedini sul cous cous con lo yogurt mescolato a limone e menta come salsa."],
 "Carbonara leggera di zucchine": [
  "Porta a bollore l'acqua salata e cuoci la pasta integrale.",
  "Intanto taglia le zucchine a bastoncini e rosolale in padella con olio e aglio a fuoco vivace finché sono dorate; togli l'aglio.",
  "Sbatti uovo, albumi, Parmigiano e molto pepe in una ciotola.",
  "Scola la pasta tenendo da parte un mestolo d'acqua, saltala 30 secondi con le zucchine e togli la padella dal fuoco.",
  "Versa le uova con un mestolino d'acqua di cottura e mescola velocemente finché diventa cremosa, senza rimettere sul fuoco (altrimenti diventa una frittata)."],
 "Polpette di seitan al sugo con patate": [
  "Lessa le patate a spicchi per 15-20 minuti, finché la forchetta entra facilmente.",
  "Frulla il seitan con avena, prezzemolo, aglio e noce moscata e forma 8 polpette con le mani umide.",
  "In una padella soffriggi la cipolla tritata con metà dell'olio per 3 minuti, aggiungi passata e basilico e cuoci 10 minuti.",
  "Adagia le polpette nel sugo, copri e cuoci 10 minuti a fuoco dolce, girandole a metà.",
  "Servi con le patate condite con il resto dell'olio, sale e prezzemolo."],
 "Medaglioni di tofu e spinaci con patate dolci": [
  "Taglia le patate dolci a spicchi, condiscile con metà dell'olio e la paprika e cuocile in forno a 200°C per 30 minuti.",
  "Appassisci gli spinaci in padella con un goccio d'acqua per 2 minuti e strizzali bene.",
  "Asciuga il tofu e frullalo con spinaci, avena, aglio in polvere, noce moscata e sale fino a un impasto compatto.",
  "Forma 4 medaglioni con le mani umide e cuocili in padella con il resto dell'olio, 4 minuti per lato, finché sono dorati.",
  "Servi con le patate dolci."],
 "Merluzzo in crosta di mandorle con patate e fagiolini": [
  "Lessa le patate a cubetti per 15 minuti e i fagiolini per 8 minuti (oppure cuocili al vapore).",
  "Scalda il forno a 200°C. Frulla mandorle, pane, prezzemolo e scorza di limone fino a una granella.",
  "Asciuga bene il merluzzo, spennellalo con un velo di senape e premi sopra la crosta.",
  "Cuocilo su carta forno per 12-15 minuti, finché la crosta è dorata.",
  "Condisci patate e fagiolini con l'olio, sale e limone e servi con il pesce."],
 "Pasta integrale al ragù bianco di tacchino e funghi": [
  "Trita finemente il tacchino al mixer (o compralo macinato) e metti a bollire l'acqua per la pasta.",
  "Rosola cipolla e aglio tritati nell'olio, aggiungi il tacchino e sgranalo bene per 5 minuti; sfuma con il vino.",
  "Unisci i funghi a fette, rosmarino e salvia e cuoci 10 minuti con un goccio d'acqua.",
  "Cuoci la pasta integrale e scolala al dente tenendo da parte un po' d'acqua di cottura.",
  "Saltala nel ragù con un cucchiaio d'acqua di cottura e completa con il Parmigiano."],
 "Congee di riso con tofu e zenzero": [
  "Sciacqua il riso e mettilo in una pentola con 600 ml d'acqua o brodo e lo zenzero a fiammiferi.",
  "Porta a bollore, poi cuoci a fuoco basso 25 minuti con il coperchio socchiuso, mescolando spesso, finché i chicchi si sfaldano in una crema (aggiungi acqua se si addensa troppo).",
  "Taglia il tofu a cubetti e il pak choi a pezzi.",
  "Negli ultimi 5 minuti aggiungi pak choi, edamame e tofu.",
  "Condisci con salsa di soia, pepe bianco, cipollotto, sesamo e due gocce di olio di sesamo."],
 "Bibimbap con tofu e uovo": [
  "Cuoci il riso basmati (10-12 minuti).",
  "Salta separatamente in padella con poche gocce d'olio gli spinaci con l'aglio, le carote a julienne e i germogli, 2 minuti ciascuno; sala appena.",
  "Rosola il tofu a cubetti con il resto dell'olio e un goccio di salsa di soia finché è dorato.",
  "Cuoci l'uovo all'occhio di bue, con il tuorlo morbido.",
  "Componi la ciotola: riso sul fondo, verdure e tofu a spicchi, kimchi e uovo al centro.",
  "Completa con sesamo e un cucchiaino di salsa piccante e mescola tutto prima di mangiare."],
 "Gado-gado, insalata indonesiana con salsa di arachidi": [
  "Lessa le patate a cubetti per 12 minuti e i fagiolini per 8 minuti.",
  "Rassoda l'uovo: 9 minuti dal bollore, poi in acqua fredda.",
  "Sbollenta germogli e cavolo a listarelle per 1 minuto e scolali.",
  "Rosola il tofu a cubetti in padella antiaderente finché è dorato.",
  "Prepara la salsa sciogliendo la crema di arachidi con lime, aglio grattugiato, soia, peperoncino e 2-3 cucchiai d'acqua calda.",
  "Componi il piatto con verdure, tofu e uovo a spicchi e condisci con la salsa."],
 "Rajma, fagioli rossi al curry": [
  "Idrata la soia in acqua calda per 10 minuti e strizzala.",
  "Soffriggi cipolla, aglio e zenzero tritati nell'olio per 4 minuti, poi tosta garam masala, cumino e curcuma per 1 minuto.",
  "Aggiungi passata, fagioli scolati, soia e un bicchiere d'acqua.",
  "Cuoci 20 minuti a fuoco dolce schiacciando qualche fagiolo per addensare. Intanto cuoci il riso basmati.",
  "Servi con il riso e il coriandolo."],
 "Falafel al forno con bulgur e tahina": [
  "Asciuga bene i ceci e frullali a scatti con prezzemolo, coriandolo, cipolla, aglio, cumino e la farina di ceci: l'impasto deve restare granuloso, non una crema.",
  "Lascialo 15 minuti in frigo, poi forma 10 palline e schiacciale leggermente.",
  "Spennellale d'olio e cuocile in forno a 200°C per 25 minuti, girandole a metà.",
  "Cuoci il bulgur in acqua salata per 10 minuti, scolalo e condiscilo con pomodori, cetriolo e limone.",
  "Mescola tahina, yogurt di soia, limone e un goccio d'acqua per la salsa e servi tutto insieme."],
 "Tacos di fagioli neri e tofu": [
  "Prepara il pico de gallo: pomodori e cipolla rossa a dadini, coriandolo, lime e un pizzico di sale.",
  "Sbriciola il tofu e rosolalo in padella antiaderente con cumino e paprika affumicata per 5 minuti, finché è dorato.",
  "Scalda i fagioli con un cucchiaio d'acqua schiacciandoli in parte con la forchetta.",
  "Taglia il cavolo a julienne sottile e condiscilo con lime; scalda le tortillas in padella 30 secondi per lato.",
  "Farcisci con fagioli, tofu, cavolo, pico de gallo, avocado a fette e salsa piccante a piacere."],
 "Mujaddara, lenticchie e riso con cipolle": [
  "Affetta sottili le cipolle e cuocile con l'olio a fuoco basso per 20 minuti, mescolando ogni tanto, finché sono scure e dolci.",
  "Intanto cuoci il riso basmati con un pizzico di cumino e cannella (10-12 minuti).",
  "Scalda le lenticchie e mescolale con il riso e metà delle cipolle.",
  "Mescola lo yogurt con la menta tritata e un pizzico di sale; condisci l'insalata con il limone.",
  "Completa la mujaddara con le cipolle rimaste e servi con lo yogurt e l'insalata."],
}

# scongelamento calcolato dagli ingredienti
TH = {'pollo': ('il pollo', 'o'), 'tacchino': ('il tacchino', 'o'), 'manzo': ('il manzo', 'o'), 'macinato': ('il macinato', 'o'),
      'trota': ('la trota', 'a'), 'salmone': ('il salmone', 'o'), 'branzino': ('il pesce', 'o'), 'lonza': ('la lonza', 'a')}
ALWAYS = {'merluzzo': 'il merluzzo', 'gamberi': 'i gamberi'}

def thaw(items):
    keys = [k for k, _ in items]
    for k in keys:
        if k in ALWAYS:
            n = ALWAYS[k]
            return f"scongela {n} in frigo.", f"scongela prima {n}: in un sacchetto chiuso in acqua fredda bastano 30-40 minuti"
    for k in keys:
        if k in TH:
            n, g = TH[k]; pr = 'lo' if g == 'o' else 'la'
            return f"se {n} è surgelat{g}, sposta{pr} dal freezer al frigo.", f"se {n} è surgelat{g}, scongela{pr} prima"
    return '', ''

def apply(d):
    used = set()
    recs = [r for ph in ('f1', 'f2') for r in d[ph]['recipes']] + d['extra']
    for r in recs:
        t = r['title']
        if t in STEPS: r['steps'] = STEPS[t]; used.add(('s', t))
        if t in PREP: r['prep'] = PREP[t]; used.add(('p', t))
        if t in BOX: r['box'] = BOX[t]; used.add(('b', t))
        if t in PL: r['pl'] = PL[t]; used.add(('l', t))
        if t not in NOTHAW:
            a, b = thaw(r['items'])
            if a: r['thaw'], r['thawL'] = a, b
    for ph in ('f1', 'f2'):
        for di, day in enumerate(d[ph]['days']):
            for m in day['meals']:
                a = m.get('alt')
                if a and (ph, di, a['title']) in ALT: a['prep'] = ALT[(ph, di, a['title'])]; used.add(('a', ph, di, a['title']))
    miss = [('s', t) for t in STEPS] + [('p', t) for t in PREP] + [('b', t) for t in BOX] + [('l', t) for t in PL] + [('a',) + k for k in ALT]
    miss = [x for x in miss if x not in used]
    if miss: raise SystemExit('Titoli non trovati: ' + repr(miss))
