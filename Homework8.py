#dú0
# Udělej si seznam domácích zvířat. Budeš ho potřebovat v dalších úlohách. Domácí zvířata známe tato: "pes", "kočka", "králík", "had".

# Napiš funkci, která dostane jako argumenty seznam zvířat a slovo a zjistí, jestli je toto slovo v seznamu. „Zjistí“ znamená, že funkce vrátí True nebo False.

domaci_zvirata = ["pes", "kocka", "kralik", "had"]
def zvire_ano_ne(seznam, slovo):
    return slovo in seznam
    
print(zvire_ano_ne(domaci_zvirata, "kun"))


#dú1
# Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která jsou kratší než 5 písmen.

domaci_zvirata = ["pes", "kocka", "kralik", "had"]
def zvirata_pod_pet(seznam):
    vysledek = []
    for zvire in seznam:
        if len(zvire) < 5:
            vysledek.append(zvire)
    return vysledek

#volání funkce    
print(zvirata_pod_pet(domaci_zvirata))


#dú2
# Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která začínají na k.

domaci_zvirata = ["pes", "kocka", "kralik", "had"]
def zvirata_na_k(seznam):
    vysledek = []
    for zvire in seznam:
        if zvire[0] == "k" or zvire [0] == "K":
            vysledek.append(zvire)
    return vysledek
    
#volání funkce
print(zvirata_na_k(domaci_zvirata))

#dú3
# Napiš program, který seřadí seznam domácích zvířat podle abecedy. Víš, jaký je rozdíl mezi metodou sort a funkcí sorted?

domaci_zvirata = ["pes", "kocka", "kralik", "had"]
def zvirata_abeceda1(seznam):
    seznam.sort ()
    return seznam
    
#volání funkce - metoda sort změní původní seznam
print(zvirata_abeceda1(domaci_zvirata))


domaci_zvirata = ["pes", "kocka", "kralik", "had"]
def zvirata_abeceda2(seznam):
    return sorted(seznam)
        
#volání funkce - funkce sorted vrátí nově vytvořený seznam
print(zvirata_abeceda2(domaci_zvirata))

#dú4
# Napiš funkci, která dostane dva seznamy jmen zvířat a vrátí tři seznamy:

# zvířata, která jsou v obou seznamech současně (průnik množin: první ∩ druhá),
# zvířata, která jsou jen v prvním seznamu (rozdíl množin: první - druhá),
# zvířata, která jsou jen ve druhém seznamu (rozdíl množin: druhá - první).

domaci_zvirata = ["pes", "kocka", "kralik", "had"]
divoka_zvirata = ["had", "kralik", "slon", "zirafa"]
def zvirata(seznam1, seznam2):
    zvirata_v_obou = [] 
    for zvire in seznam1:
        if zvire in seznam2:
            zvirata_v_obou.append(zvire) 
    zvirata_pouze_domaci = [] 
    for zvire in seznam1:
        if zvire not in seznam2:
            zvirata_pouze_domaci.append(zvire) 
    zvirata_pouze_divoka = [] 
    for zvire in seznam2:
        if zvire not in seznam1:
            zvirata_pouze_divoka.append(zvire) 
    return zvirata_v_obou, zvirata_pouze_domaci,zvirata_pouze_divoka
    
#volání funkce
print(zvirata(domaci_zvirata,divoka_zvirata))

#dú5
# Napiš funkci, která dostane dvojici (tzv. tuple) a vrátí její součet. 
# Pokud funkce dostane více jak dvě čísla, tj. např. trojici, tak vypíše: "Bohužel, umím sečíst jen dvě čísla.":


def soucet_dvou(cisla):
    if len(cisla) == 2:
        return cisla[0] + cisla[1]
    else:
        print("Bohužel, umím sečíst jen dvě čísla.")

#volání funkce
print(soucet_dvou((12,38)))
print(soucet_dvou((1,3,45)))