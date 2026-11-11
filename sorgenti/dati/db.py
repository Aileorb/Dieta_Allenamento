# per 100 g: nome, P, C, G, saturi, fibra  (stessi valori del piano)
DB = {
 "avena":("Fiocchi d'avena",13.0,60.0,7.0,1.2,9.5),"latte":("Latte scremato",3.5,5.0,0.2,0.1,0.0),"yogurt":("Yogurt greco 0%",10.0,3.5,0.2,0.1,0.0),
 "skyr":("Skyr naturale",11.0,4.0,0.2,0.1,0.0),"fiocchi":("Fiocchi di latte light",12.5,3.0,2.0,1.3,0.0),"albume":("Albume d'uovo",11.0,0.7,0.2,0.0,0.0),
 "uovo":("Uovo intero",12.5,0.7,9.5,3.1,0.0),"pollo":("Petto di pollo",23.0,0.0,1.5,0.4,0.0),"tacchino":("Fesa di tacchino",24.0,0.0,1.2,0.4,0.0),
 "merluzzo":("Merluzzo/nasello",18.0,0.0,0.7,0.1,0.0),"salmone":("Salmone fresco",20.4,0.0,13.4,3.1,0.0),"branzino":("Orata/branzino (filetto)",19.5,0.0,4.0,1.0,0.0),
 "tonno":("Tonno al naturale sgocciolato",24.0,0.0,1.0,0.3,0.0),"sgombro":("Sgombro fresco",18.5,0.0,12.0,2.8,0.0),"bresaola":("Bresaola",32.0,0.0,2.6,1.0,0.0),
 "manzo":("Manzo magro (fesa/magatello)",21.5,0.0,3.0,1.2,0.0),"tofu":("Tofu naturale",14.0,1.5,7.5,1.1,1.0),"lenticchie":("Lenticchie lessate",8.0,13.0,0.5,0.1,6.5),
 "ceci":("Ceci lessati",7.5,16.0,2.4,0.3,6.5),"fagioli":("Fagioli lessati",7.5,14.0,0.5,0.1,6.5),"pasta":("Pasta di semola",12.5,71.0,1.5,0.3,3.0),
 "pasta_int":("Pasta integrale",13.5,64.0,2.5,0.4,8.0),"riso":("Riso basmati",7.5,78.0,0.6,0.2,1.0),"riso_int":("Riso integrale",7.5,74.0,2.5,0.5,3.5),
 "farro":("Farro perlato",14.0,67.0,2.5,0.4,7.0),"orzo":("Orzo perlato",10.0,66.0,1.2,0.3,10.0),"quinoa":("Quinoa",14.0,57.0,6.0,0.7,7.0),
 "patate":("Patate",2.0,16.5,0.1,0.0,1.8),"patate_dolci":("Patate dolci",1.6,17.0,0.1,0.0,3.0),"pane_int":("Pane integrale",9.0,42.0,2.5,0.4,7.0),
 "gallette":("Gallette di riso integrale",8.0,78.0,3.0,0.6,4.0),"banana":("Banana",1.1,20.0,0.3,0.1,2.5),"mela":("Mela",0.3,12.0,0.2,0.0,2.4),
 "bosco":("Frutti di bosco",1.0,8.0,0.4,0.0,5.0),"kiwi":("Kiwi",1.1,10.5,0.5,0.0,3.0),"arancia":("Arancia",0.9,9.5,0.1,0.0,2.0),"pera":("Pera",0.4,12.0,0.1,0.0,3.1),
 "datteri":("Datteri secchi",2.5,66.0,0.4,0.0,7.5),"miele":("Miele",0.4,81.0,0.0,0.0,0.0),"verdure":("Verdure miste",1.3,4.0,0.2,0.0,2.0),
 "insalata":("Insalata mista",1.3,2.5,0.2,0.0,1.8),"broccoli":("Broccoli",2.8,4.0,0.4,0.1,2.6),"spinaci":("Spinaci",2.9,1.5,0.4,0.1,2.2),
 "pomodori":("Pomodori/pomodorini",0.9,3.0,0.2,0.0,1.2),"passata":("Passata di pomodoro",1.3,5.0,0.2,0.0,1.3),"zucchine":("Zucchine",1.3,2.0,0.1,0.0,1.2),
 "piselli":("Piselli (surgelati)",5.4,9.0,0.4,0.1,5.1),"funghi":("Funghi champignon",3.1,1.0,0.3,0.0,2.0),"olio":("Olio extravergine d'oliva",0.0,0.0,100.0,15.0,0.0),
 "noci":("Noci",15.0,7.0,65.0,6.0,6.5),"mandorle":("Mandorle",21.0,9.5,50.0,3.8,12.5),"arachidi_crema":("Crema 100% arachidi",25.0,12.0,50.0,9.0,6.0),
 "lino":("Semi di lino macinati",18.0,1.5,42.0,3.7,27.0),"avocado":("Avocado",2.0,1.9,14.7,2.1,6.7),"parmigiano":("Parmigiano Reggiano",33.0,0.0,28.0,18.0,0.0),
 "cioccolato":("Cioccolato fondente 85%",11.0,19.0,46.0,28.0,12.0),"cacao":("Cacao amaro in polvere",20.0,11.0,11.0,6.5,30.0),
 "pasta_uovo":("Pasta all'uovo secca",14.0,66.0,4.3,1.3,3.0),"macinato":("Macinato magro di manzo (5%)",21.0,0.0,5.0,2.2,0.0),
 "seitan":("Seitan",23.0,5.0,2.0,0.3,0.5),"tempeh":("Tempeh",19.5,6.0,11.0,2.2,4.0),"soia_text":("Soia texturizzata (granulare, secca)",50.0,18.0,1.5,0.2,16.0),
 "edamame":("Edamame sgusciati (surgelati)",11.5,4.0,5.0,0.6,5.0),"yogurt_soia":("Yogurt di soia bianco senza zuccheri",4.2,1.0,2.3,0.4,1.0),
 "latte_soia":("Latte di soia senza zuccheri",3.3,0.3,1.8,0.3,0.5),"lupini":("Lupini pronti (sciacquati)",15.5,7.0,2.9,0.35,3.0),
 "pasta_lent":("Pasta di lenticchie rosse",25.0,48.0,2.0,0.3,11.0),"farina_ceci":("Farina di ceci",22.0,47.0,6.5,0.7,11.0),
 "tahina":("Tahina (crema di sesamo)",17.0,10.0,54.0,7.5,9.0),"salsa_soia":("Salsa di soia",8.0,5.0,0.0,0.0,0.0),
 "cous_int":("Cous cous integrale",12.5,64.0,1.8,0.3,7.0),"riso_venere":("Riso venere",8.0,72.0,2.5,0.5,4.0),"farina_int":("Farina integrale",12.0,62.0,2.0,0.3,9.0),
 "mozz_light":("Mozzarella light",19.5,1.0,9.0,6.0,0.0),"trota":("Trota salmonata (filetto)",20.5,0.0,6.2,1.8,0.0),"chia":("Semi di chia",17.0,7.7,31.0,3.3,34.0),
 "pinoli":("Pinoli",13.7,4.0,68.0,4.9,3.7),"zucca":("Zucca",1.1,4.5,0.1,0.0,1.8),"peperoni":("Peperoni",0.9,4.2,0.3,0.05,1.9),"cavolfiore":("Cavolfiore",2.0,2.7,0.2,0.05,2.4),
 "carote":("Carote",1.0,7.6,0.2,0.03,3.0),"finocchi":("Finocchi",1.2,4.0,0.2,0.0,3.1),"fagiolini":("Fagiolini",1.8,4.3,0.2,0.05,2.7),"melanzane":("Melanzane",1.1,2.6,0.1,0.0,2.6),
 "fragole":("Fragole",0.7,5.7,0.3,0.0,2.0),"mais":("Mais dolce (sgocciolato)",2.9,15.0,1.2,0.2,2.5),"acero":("Sciroppo d'acero",0.0,67.0,0.1,0.0,0.0),
 "riso_car":("Riso Carnaroli",7.0,79.0,0.6,0.2,1.0),"arachidi":("Arachidi tostate non salate",25.0,8.0,49.0,7.0,8.5),"verza":("Verza o cavolo nero",1.5,4.0,0.1,0.0,2.5),
 "cetriolo":("Cetriolo",0.7,3.6,0.1,0.0,0.5),"gamberi":("Gamberi sgusciati (surgelati)",18.0,0.0,1.0,0.2,0.0),
 "soba":("Soba (spaghetti di grano saraceno)",14.0,68.0,1.0,0.2,4.5),"vermicelli":("Vermicelli di riso",6.0,80.0,0.6,0.2,1.6),
 "miso":("Miso",12.0,20.0,6.0,1.0,5.0),"pakchoi":("Pak choi",1.5,1.2,0.2,0.0,1.0),"germogli":("Germogli di soia",3.0,4.0,0.2,0.0,1.8),
 "kimchi":("Kimchi",1.1,2.4,0.5,0.1,1.6),"sesamo":("Semi di sesamo",18.0,12.0,50.0,7.0,12.0),"tortilla":("Tortillas di mais",5.7,44.0,2.9,0.4,6.3),
 "bulgur":("Bulgur",12.0,64.0,1.3,0.2,12.0),"lonza":("Lonza di maiale magra",22.0,0.0,3.5,1.2,0.0),
}
def calc(items):
    t = dict(k=0,p=0,c=0,g=0,s=0,f=0)
    for key, g in items:
        _, p, c, f, s, fi = DB[key]; x = g/100
        t['p'] += p*x; t['c'] += c*x; t['g'] += f*x; t['s'] += s*x; t['f'] += fi*x
    t['k'] = 4*t['p'] + 4*t['c'] + 9*t['g']
    return t
