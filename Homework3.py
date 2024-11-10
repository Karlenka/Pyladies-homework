# for c in range(5):
#     print(c)

# l = -1
# for k in range (6):
#     l = l + 2
#     print (l)

# for i in range(1, 12, 2):
#     print(i)

# for l in range(1, 5):
#     print(f'{l} na druhou = {l*l}')

# l = 1 # proměnnou je zde l, které je definované funkcí range - tedy číselnou řadou v rozmezí od jedné do pěti
# for l in range (1,5):
#     l = (f'{l} na druhou = {l*l}')
#     print(l)

 

# for radek in range (5): # proměnou je zde počet řádků
#     for pocet_znaku in range(5): # v tomto cyklu je proměnou počet znaků na jednotlivém řádku
#         print('X', end=' ')
#     print()


# for a in range (1, 5):
#     for b in range (1, 5):
#         print (a * b, end= ' ')
#     print()

# for k in range (1, 5):
#     for l in range (1):
#         print (k * 'X ', end = ' ')
#     print()

from turtle import forward, left, exitonclick, right
from math import sqrt
strana = 50

for i in range (4):
    uhlopricka = sqrt(2) * strana
    for i in range(4):
        forward(strana)
        left(90)
    left(45)
    forward(uhlopricka)
    for i in range(2):
        left(90)
        forward(uhlopricka/2)
    left(90)
    forward(uhlopricka)
    left(45)
    forward(strana)
    strana+= 20

exitonclick()

import turtle
turtle.shape('turtle')
from turtle import left, right, forward, exitonclick, clear 

n = int(input('Napiš číslem, kolika úhelník má program namalovat: '))
strana = 400 / n
for _ in range (n):
    forward(strana)
    left(180 -(180 * (1-2/n)))
exitonclick()