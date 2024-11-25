#dú0
# Napiš funkci, která pro argumentem zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n a jako hodnoty k nim jejich druhé mocniny. Například:

# >>> mocniny(4)
# {1: 1, 2: 4, 3: 9, 4: 16}
# >>> mocniny(2)
# {1: 1, 2: 4}

def mocniny(n):
    slovnik = {}
    for i in range(1, n + 1):
        slovnik[i] = i ** 2
    return slovnik

print(mocniny(4))

# dú1
# Napiš funkci, která sečte a vrátí sumu všech klíčů a sumu všech hodnot ve slovníku, který dostane jako argument. 
# K vyzkoušení můžeš použít slovník z minulé úlohy. Například:

# >>> soucet_klicu_a_hodnot(mocniny(4))
# (10, 30)
# >>> muj_slovnik = {0: 0, 1: 5, 2: 10}
# >>> soucet_klicu_a_hodnot(muj_slovnik)
# (3, 15)

def soucet_klicu_a_hodnot(slovnik):
    suma_hodnot = sum(slovnik.keys())
    suma_klicu = sum(slovnik.values())
    return (suma_klicu, suma_hodnot)
print(soucet_klicu_a_hodnot(mocniny(4)))

# dú2
# Napiš funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci. Například:

# >>> pocet_znaku("hello world")
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# Co vrátí funkce, když jejím argmentem bude "Máme rádi PyLadies!"?

    
def pocet_znaku(string):
    znaky = string.strip().lower()
    slovnik = {}
    for znak in znaky:
        slovnik[znak] = slovnik.get(znak, 0) + 1
    return slovnik

vysledek = pocet_znaku("Máme rádi PyLadies!.")
print(vysledek)

#nebo:

def pocet_znaku(string):
    znaky = string.lower().strip()
    vypis = {}
    for znak in znaky:
        if znak in vypis:
            vypis[znak] += 1
        else:
            vypis[znak] = 1
    return vypis

print(pocet_znaku("Máme rádi Pyladies!"))


#dú3

# Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) a vypíše je jako mapu: mřížku 10×10, 
# kde na políčka, která jsou v seznamu, napíše X, jinde tečku. Například:

# nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])
# X X . . . . . . . .
# . . . . . . . . . .
# . . X . . . . . . .
# . . . . X . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . X .
# Jak na to?

# Udělej tabulku (seznam seznamů) se samými tečkami, něco jako:
# [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']].
# Na příslušných místech nahraď tečky X-ky.
# Tabulku vypiš pomocí dvou cyklů for zanořených do sebe.
def vytvor_mapa():
    mapa = {}
    for radek in range(10):  # Počet řádků
        for sloupec in range(10):  # Počet sloupců
            mapa[(radek, sloupec)] = '.'  
    return mapa

def uprav_mapa(mapa, souradnice):
    for x, y in souradnice:
        if 0 <= x < 10 and 0 <= y < 10:  
            mapa[(x, y)] = 'X'  

# Funkce pro tisk mapy
def vytiskni_mapa(mapa):
    for radek in range(10):
        for sloupec in range(10):
            print(mapa[(radek, sloupec)], end=' ')  
        print()  

# Volání funkcí 
mapa = vytvor_mapa()  #vytvoření základní mapy

uprav_mapa(mapa, [(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])# Aktualizace mapy podle zadaných souřadnic - odpovídá zadání v textu, ale ne obrázku v zadání - je tam rozpor 

vytiskni_mapa(mapa)# Zobrazení aktualizované mapy

#dú4
# Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:

# souradnice = [(0, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]

# ja['jazyk'] = 'Python'
# ja
# {'jméno': 'Anna', 'město': 'Brno', 'čísla': [3, 7, 42], 'jazyk': 'Python'}

def pohyb(souradnice, smer):
    posledni_bod = souradnice[-1]
    x, y = posledni_bod 

    if smer == 's':  
        souradnice.append((x - 1, y))
    elif smer == 'j':  
        souradnice.append((x + 1, y))
    elif smer == 'v':  
        souradnice.append((x, y + 1))
    elif smer == 'z':  
        souradnice.append((x, y - 1))
    else:
        print("Neplatný směr! Zadej 's', 'j', 'v' nebo 'z'.")
        
        

#dú5

def vytvor_mapa():
    # Statická mapa 10×10 s tečkami
    mapa = {}
    for radek in range(10):
        for sloupec in range(10):
            mapa[(radek, sloupec)] = '.'  # Každá tečka má souřadnici
    return mapa

def vytiskni_mapa(mapa, souradnice):
    # Aktualizace mapy s tečkami a X
    for radek in range(10):
        for sloupec in range(10):
            if (radek, sloupec) in souradnice:
                print('X', end=' ')  # Body v seznamu souřadnic jsou X
            else:
                print('.', end=' ')  # Ostatní jsou tečky
        print()

def pohyb(souradnice, smer):
    posledni_bod = souradnice[-1]
    x, y = posledni_bod
    if smer == 's':  # Sever
        novy_bod = (x - 1, y)
    elif smer == 'j':  # Jih
        novy_bod = (x + 1, y)
    elif smer == 'v':  # Východ
        novy_bod = (x, y + 1)
    elif smer == 'z':  # Západ
        novy_bod = (x, y - 1)
    else:
        print("Neplatný směr! Zadej 's', 'j', 'v' nebo 'z'.")
        return
    # Ověření, že nový bod je v mapě
    if 0 <= novy_bod[0] < 10 and 0 <= novy_bod[1] < 10:
        souradnice.append(novy_bod)
    else:
        print("Pohyb mimo hranice mapy!")

# Hlavní cyklus
souradnice = [(0, 0), (1, 0), (2, 0)]  # Startovní body
mapa = vytvor_mapa()

while True:
    vytiskni_mapa(mapa, souradnice)  # Zobrazení mapy
    smer = input("Zadej světovou stranu (s, j, v, z): ").lower()
    pohyb(souradnice, smer)



