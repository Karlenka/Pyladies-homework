
#dú0
def pocet_vterin(minuty, vteriny):
    return 60 * minuty + vteriny

print(f'Počet vteřin je {pocet_vterin(5, 24)}.')

#dú1
prvni = float(input('Zadej první číslo: '))
druhe = float(input('Zadej druhé číslo: '))
treti = float(input('Zadej třetí číslo: '))

def max_ze_tri(a ,b ,c ): 
    if  a >= b and a >= c:
        return(a)
    elif b > a and b >= c:
        return(b)
    else:
        return(c)

print(f'Největší číslo je: {max_ze_tri(prvni, druhe, treti)}')

# dú2
obvod_hrudniku = float(input('Vlož obvod hrudníku v centimetrech:'))
delka_nohy = float(input('Vlož délku nohy od kolena ke kotníku v centimetrech:'))

def body_index (a, b ):
    return ((a/0.7062 - b)/0.9156) - b

print(f'Body mass index vaší kočky je:{body_index(obvod_hrudniku, delka_nohy):.2f}.')

#dú3
from turtle import left, right, forward, exitonclick, clear, shape, penup, pendown
def nakresli_n_uhelnik(n):
    shape('turtle')
    strana = 200/n
    uhel = 180 -(180 * (1-2/n))

    for c in range (n):
        forward(strana)
        left(uhel)
    penup()
    forward (80)
    pendown()

for n in range(5, 9):
    nakresli_n_uhelnik(n)    
exitonclick()

#dú4
def obdelnik_x(n):
    for radek in range(1, n + 1):  # Cyklus zahrnuje i poslední řádek
        if radek == 1 or radek == n:  # První a poslední řádek
            print('X ' * 7)
        else:
            print('X' + ' ' * 11 +'X') 


obdelnik_x(7)

def obdelnik_x(n):
    for radek in range(1, n + 1):
        if radek == 1 or radek == n: 
            radek_text = ""
            for i in range(7): 
                radek_text += "X "
            print(radek_text)
        else:
            radek_text = "X"  
            for i in range(11): 
                radek_text += " "
            radek_text += "X"  
            print(radek_text)

obdelnik_x(8)

#dú5s
from random import randrange

#def hod():
    #return random.randint(1,6)
    s

def hod_kostkou(hrac):
    pocet_hodu = 0
    while True:
        hod = randrange(1, 7)  
        pocet_hodu += 1
        if hod != 6:
            print(f'Hráč {hrac} hodil: {hod}')
        else:S
            print(f'Hráč {hrac} hodil: {hod}. K hození 6 potřeboval {pocet_hodu} hodů.')
            return pocet_hodu  

vitez = 0
nejvic_hodu = 0

for hrac in range(1, 5):  
    pocet_hodu = hod_kostkou(hrac)  
    if pocet_hodu > nejvic_hodu:
        nejvic_hodu = pocet_hodu
        vitez = hrac

print(f"Vítězem je hráč {vitez}, který potřeboval {nejvic_hodu} hodů.")

#dú6
#toto je špatná vareze...vypisuje, místo aby vracela a ještě navíc sudé-liché místo bum bác
def sude_liche(n):
    if n % 2 == 0:
        print(f'Číslo {n} je sudé.')
    else:
        print(f'Číslo {n} je liché.')

cislo = sude_liche(9)

#špatná varianta - výstupem mělo být bum bác

def cislo_sl(n):
    if n % 2 == 0:
        return ('sudé')
    else:
        return('liché')

n = int(input('Zadej celé číslo:'))
print(f'Toto číslo je {cislo_sl(n)}.')

#správně
def bum_nebo_bac(n):
    if n % 2 == 0:
        return ('Bác')
    else:
        return('Bum')

n = int(input('Zadej celé číslo:'))
print(bum_nebo_bac(n))

#dú7

#špatná varianta - měla jsem použít funkci z předch. úkolu
def bum_bac(n):
    for radek in range(1, n + 1):
        if radek % 2 == 0:
            print('Bác')
        else:
            print('Bum')

bum_bac(5)

 # varianta, kdy používám funkci z min úkolu
def bum_nebo_bac(n):
    if n % 2 == 0:
        return ('Bác')
    else:
        return('Bum')

def bum_bac(k):
    for radek in range(1, k + 1):
        n = radek
        print(bum_nebo_bac(n))

bum_bac(9)