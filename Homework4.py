#úkol č.1
heslo = ['python','Python', 'PYTHON']
hadanka = input('Zadej tajné heslo: ')
while hadanka not in heslo:
    hadanka = input('Špatně, zkus to znovu:')
print('Skvěle, uhodls.')
    
# úkol 2

print('Pojď, zahrajeme si hru "Kámen, nůžky, papír".')

člověk = input('Pokud chceš skončit, zadej konec. Jinak zvol kámen, nůžky nebo papír:  ') 
while člověk != 'konec':
    počítač = 'kámen'
    if člověk == počítač:
        print('Počítač zadal taky', počítač, 'Plichta.')
    elif člověk == 'nůžky' and počítač == 'kámen':
        print('Počítač zadal', počítač, 'Vyhrál počítač.')
    elif člověk == 'papír' and počítač == 'nůžky':
        print('Počítač zadal', počítač, 'Vyhrál počítač.')
    elif člověk == 'kámen' and počítač == 'papír':
        print('Počítač zadal', počítač, 'Vyhrál počítač.')
    elif člověk == 'papír' and počítač == 'kámen':
        print('Počítač zadal', počítač, 'Jsi vítěz.')
    elif člověk == 'kámen' and počítač == 'nůžky':
        print('Počítač zadal', počítač, 'Jsi vítěz.')
    elif člověk == 'nůžky' and počítač == 'papír':
        print('Počítač zadal', počítač, 'Jsi vítěz.')
    else:
        print('Špatné zadání.')
    člověk = input('Zadej konec nebo hraj znovu.: ')

#úkol č.3
import random
from random import choice

print('Pojď, zahrajeme si hru "Kámen, nůžky, papír".')

člověk = input('Pokud chceš skončit, zadej konec. Jinak zvol kámen, nůžky nebo papír:  ') 
while člověk != 'konec':
    počítač = choice(['kámen', 'nůžky', 'papír'])
    if člověk == počítač:
        print('Počítač zadal taky', počítač, 'Plichta.')
    elif člověk == 'nůžky' and počítač == 'kámen':
        print('Počítač zadal', počítač, 'Vyhrál počítač.')
    elif člověk == 'papír' and počítač == 'nůžky':
        print('Počítač zadal', počítač, 'Vyhrál počítač.')
    elif člověk == 'kámen' and počítač == 'papír':
        print('Počítač zadal', počítač, 'Vyhrál počítač.')
    elif člověk == 'papír' and počítač == 'kámen':
        print('Počítač zadal', počítač, 'Jsi vítěz.')
    elif člověk == 'kámen' and počítač == 'nůžky':
        print('Počítač zadal', počítač, 'Jsi vítěz.')
    elif člověk == 'nůžky' and počítač == 'papír':
        print('Počítač zadal', počítač, 'Jsi vítěz.')
    else:
        print('Špatné zadání.')
    člověk = input('Zadej konec nebo hraj znovu.: ')
print('Konec.')


#č4
nejmensi = float('inf')  # Inicializace proměnné, která bude ukládat nejmenší číslo

while True:
    cislo = int(input('Zadej číslo (nebo 0 pro ukončení): '))

    if cislo == 0:  # Ukončí smyčku, pokud uživatel zadá 0
        break

    if nejmensi is None or cislo < nejmensi:
        nejmensi = cislo  # Uloží nové nejmenší číslo

if nejmensi is not None:
    print('Nejmenší zadané číslo je:', nejmensi)
else:
    print('Nebyla zadána žádná čísla kromě nuly.')

#č5
import random
from random import randrange, choice
hody_hracu = [0, 0, 0, 0]
for hrac in range(1, 5):
    
    pocet_hodu = 0
    while True:
        hod = randrange(1, 7)  
        pocet_hodu +=1
        if hod != 6:
            print(f'Hrac {hrac} hodil:{hod}')
        else:
            print(f'Hrac {hrac} hodil:{hod}.K hození 6 potřeboval {pocet_hodu} hodů.')
            hody_hracu[hrac - 1] = pocet_hodu
            break
vitez = 1
nejvic = hody_hracu[0]

for i in range(1, 4):
    if hody_hracu[i] > nejvic:
        vitez = i + 1
        nejvic= hody_hracu[i]

print(f"Vítězem je hráč {vitez}, který hodil šestku po {nejvic} hodech.")

#úkol 6

print('Zadej dvě čísla a matematickou operaci +, -, \ nebo *.')
prvni_cislo = int(input('První čílo:'))
druhe_cislo = int(input('Druhé čílo:'))
operace = input("Operace (+, -, *, /): ")

if operace == '+':
    print(f'výsledek je {prvni_cislo + druhe_cislo}.')
elif operace == '-':
    print(f'výsledek je {prvni_cislo - druhe_cislo}.') 
elif operace == '*':
    print(f'výsledek je {prvni_cislo * druhe_cislo}.')
elif operace ==':':
    print(f'výsledek je {prvni_cislo / druhe_cislo}.')
else:
    print('Špatně jsi zadal číslo nebo proměnou.')

#úkol č. 

for i in range(4):
    if i == 1:
        print("první řádek")
    else:
        print("není první")



    