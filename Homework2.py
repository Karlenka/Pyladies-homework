strana = 2852  # v centimetrech
povrch = 6 * strana**2
objem = strana**3
print(f'Povrch krychle o straně {strana} cm je {povrch} cm2.')  
print(f'Objem krychle o straně {strana} cm je {objem} cm3')

strana = float(input('Zadej délku strany krychle v centimetrech: '))
povrch = 6 * strana**2
objem = strana**3
print(f'Povrch krychle o straně {strana} cm je {povrch} cm2.')  
print(f'Objem krychle o straně {strana} cm je {objem} cm3')


heslo = 'error'
hádanka = input('Pokud chceš slyšet programátorský vtip, zadej heslo: ')
if hádanka == 'error':
    print('Co dělá programátor, když má zlomené srdce? Napíše do kódu if (feelings == "broken"): delete(feelings) a pokračuje dál!')
else: 
    hádanka_znovu = input('Error. Zkus to znovu: ')
    if hádanka_znovu == 'error': 
        print('Co dělá programátor, když má zlomené srdce? Napíše do kódu if (feelings == "broken"): delete(feelings) a pokračuje dál!')
    else:
        print('Neuhodls heslo, vtip nebude.')


zpoždění = int(input('Čekáš na vlak, ale vlak je zpožděný. Kolik minut později má vlak přijet? '))
if zpoždění <= 15:
    print('Posaď se (pokud je na nástupišti nějaká lavička) a doufej, že nelžou.')
elif zpoždění <= 30:
    print('Běž do nádražky a dej si jedno pivo!')
elif zpoždění <= 60:
    print('Běž do nádražky a dej si dvě piva!')
elif zpoždění <= 90:
    print('Běž do nádražky a dej si tři piva!')
else:
    print('Běž domů.')

# program nastavený tak, že počítač může hrát pouze tah "kámen" ale zároveň je řešení připravené i na variantu se všemi třema volbami
print('Pojď, zahrajeme si hru "Kámen, nůžky, papír".')
člověk = input('Zadej kámen, nůžky nebo papír:  ') 
počítač = 'kámen' 
if člověk == počítač:
    print('Počítač zadal taky', počítač, 'Plichta.')
elif člověk == 'nůžky' and počítač == 'kámen':
    print('Počítač zadal', počítač, '.Vyhrál počítač.')
elif člověk == 'papír' and počítač != 'kámen':
    print('Počítač zadal', počítač, 'Vyhrál počítač.')
elif člověk == 'kámen' and počítač != 'kámen':
    print('Počítač zadal', počítač, 'Vyhrál počítač.')
elif člověk == 'papír' and počítač == 'kámen':
    print('Počítač zadal', počítač, 'Jsi vítěz.')
elif člověk == 'kámen' and počítač != 'kámen':
    print('Počítač zadal', počítač, 'Jsi vítěz.')
elif člověk == 'nůžky' and počítač != 'kámen':
    print('Počítač zadal', počítač, 'Jsi vítěz.')
else:
    print('Špatné zadání.')