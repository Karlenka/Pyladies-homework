#dú0
def zena_muz(p):
    if p[-1] == 'á':     
        return('žena')
    else:
        return('muž')

prijmeni = input('Zadej příjmení:')
print(f'Zadaná osoba je pravděpodobně {zena_muz(prijmeni)}.')

#dú1
def icislo(n):
    # Nahrazuje všechny znaky kromě posledních čtyř symbolem 'X'
    return 'X' * (len(n) - 4) + n[-4:]

cislo = input('Zadej identifikační číslo: ')
print(icislo(cislo))

#dú2

def pocet_k(retezec):
    retezec_maly = retezec.lower()
    return(retezec_maly.count('k'))

def pocet_t(retezec):
    retezec_maly = retezec.lower()
    return(retezec_maly.count('t'))

retezec = '''Are you going to Scarborough Fair?
Parsley, sage, rosemary, and thyme
Remember me to one who lives there
She once was a true love of mine
Tell her to make me a cambric shirt
(On the side of a hill, in the deep forest green)
Parsley, sage, rosemary, and thyme
(Tracing of sparrow on snow-crested ground)
Without no seams nor needle work
(Blankets and bedclothes the child of the mountain)
Then she'll be a true love of mine
(Sleeps unaware of the clarion call)
Tell her to find me an acre of land
(On the side of a hill, a sprinkling of leaves)
Parsley, sage, rosemary and thyme
(Washes the grave with silvery tears)
Between the salt water and the sea strands
(A soldier cleans and polishes a gun)
Then she'll be a true love of mine
Tell her to reap it with a sickle of leather
(War bellows blazing in scarlet battalions)
Parsley, sage, rosemary, and thyme
(Generals order their soldiers to kill)
And gather it all in a bunch of heather
(And to fight for a cause they've long ago forgotten)
Then she'll be a true love of mine
Are you going to Scarborough Fair?
Parsley, sage, rosemary, and thyme
Remember me to one who lives there
She once was a true love of mine'''
print(f'Písmeno k se v uvedeném textu objevuje {pocet_k(retezec)} x.')
print(f'Písmeno t se v uvedeném textu objevuje {pocet_t(retezec)} x.')

#dú3

def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka).lower().strip()
        if odpoved == 'ano'or odpoved == 'a':
            return True
        elif odpoved == 'ne' or odpoved == 'n':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne" nebo "a" nebo "n".')

if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')

#dú4
def sude(n):
    return n % 2 == 0:
        
print(sude(48))


#dú 5
def soucet_nad_deset(a,b,c):
    soucet = a + b + c
    return soucet > 10:
       
print(soucet_nad_deset(6,2,3))

#dú 6
def vyhodnot(text):
    if 'xxx' in text:
        return 'x'
    elif 'ooo' in text:
        return 'o'
    elif '-' not in text:
        return '!'
    else:
        return '-'

#dú7

pole = ' ' * 20
def tah(pole, cislo_policka, symbol):
    pole_nove = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return pole_nove
    
# pole = (tah(pole,5,'o'))
# print(pole)
# pole = (tah(pole,6,'x'))

# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

# Použij jednoduchou náhodnou „strategii”:

# Vyber číslo od 0 do 19.
# Pokud je dané políčko volné, hrej na něj.
# Pokud ne, opakuj od bodu 1.
# Můžeš předpokládat, že řetězec s herním polem vždy obsahuje alespoň jednu volnou pozici.

# Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
print(pole)
pole = (tah(pole,4,'o'))
print(pole)

#dú8

pole = '-' * 20
symbol = 'x'

def tah(pole, cislo_policka, symbol):
    pole_nove = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return pole_nove

def tah_hrace(pole):
    while True:
        cislo_policka = int(input('Zadej číslo políčka v rozmezí 1 - 20, na které chceš umístit symbol: ')) -1 
        if 0 <= cislo_policka < 20 and pole[cislo_policka] == '-':
            break
        else:
            print("Číslo musí být v rozmezí 1 až 20 a políčko nesmí být obsazené. Zkus to znovu.")
   
    return tah(pole, cislo_policka, symbol)

# Testování funkce

pole = tah_hrace(pole)
print(pole)


# Testování funkce
# Testování funkce čau MAtěji
# pokus c 2