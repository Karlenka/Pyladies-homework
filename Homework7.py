#dú0
import random
pole = '-' * 20

def tah(pole, cislo_policka, symbol):
    pole_nove = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return pole_nove

def tah_pocitace(pole, symbol):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        cislo_policka = random.randint(0, 19)
        if 0 <= cislo_policka < 20 and pole[cislo_policka] == '-':
                return tah(pole, cislo_policka, symbol)
# Testování funkce s volitelným symbolem
symbol = 'o' 
pole = tah_pocitace(pole, symbol)
print(pole)



#DÚ1:
import random

# Inicializace herního pole
pole = '-' * 20

# Základní funkce pro tah
def tah(pole, cislo_policka, symbol):
    pole_nove = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return pole_nove

# Funkce pro tah hráče
def tah_hrace(pole, symbol):
    while True:
        cislo_policka = int(input('Zadej číslo políčka v rozmezí 1 - 20, na které chceš umístit symbol: ')) - 1
        if 0 <= cislo_policka < 20 and pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, symbol)  # Vrací aktualizované pole
        else:
            print("Číslo musí být v rozmezí 1 až 20 a políčko nesmí být obsazené. Zkus to znovu.")

# Funkce pro tah počítače
def tah_pocitace(pole, symbol):
    while True:
        cislo_policka = random.randint(0, 19)
        if pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, symbol)

# Funkce pro vyhodnocení stavu hry
def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return '-'

# Celková funkce pro hru
def piskvorky1d():
    pole = '-' * 20
    while True:
        # Tah hráče
        pole = tah_hrace(pole, 'x')
        print(pole)
        vysledek = vyhodnot(pole)
        if vysledek != '-':
            break
        
        # Tah počítače
        pole = tah_pocitace(pole, 'o')
        print(pole)
        vysledek = vyhodnot(pole)
        if vysledek != '-':
            break

    # Vyhodnocení výsledku hry
    if vysledek == 'x':
        print("Vyhrál hráč s křížky!")
    elif vysledek == 'o':
        print("Vyhrál hráč s kolečky!")
    elif vysledek == '!':
        print("Hra skončila remízou.")

# Spuštění hry
piskvorky1d()

# úkol 2
# přikládám upravenou def pro tah počítače
def tah_pocitace(pole, symbol):
    protivnik_symbol = 'x' 
    
    for i in range(len(pole) - 1):
        if pole[i:i + 2] == f"{protivnik_symbol}-":
            return tah(pole, i + 1, symbol)
        elif pole[i:i + 2] == f"-{protivnik_symbol}":
            return tah(pole, i, symbol)
    
    while True:
        cislo_policka = random.randint(0, 19)
        if pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, symbol)