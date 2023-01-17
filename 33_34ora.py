"""
#1.1 Feladat
#A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

megszamolas = 0
szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
  """
"""
  #1.2 Feladat
  paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']
if szin in paletta:
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat == szin]), '-szor szerepel a listában:', ', '.join(paletta))
else:
    print('A megadott szín nem szerepel a listában')
"""
"""
#1.3 feladat
paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

megszamolas = 0
szin = input('Adj meg egy színt!\t')
if szin in paletta:
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat == szin]), '-szor szerepel a listában:', end = ' ')
else:
    print('A megadott szín nem szerepel a listában:', end = ' ')

paletta.append(szin)

print(', '.join(paletta))

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
 """   
"""
# 2.feladat

import random

lista = [random.randint(1, 3) for _ in range(10)]

print('A lista:', lista)

torlendo = int(input('Törlendő: '))

lista = [szam for szam in lista if szam != torlendo]

print('A lista', torlendo, '-es nélkül:', lista)
"""
"""
# 3 feladat
betu_leves = []

while True:
    betu = input('Betű: ')
    if not betu:
        break

    if betu.lower() in betu_leves or betu.upper() in betu_leves:
        print('Ezt a betűt már rögzítettem')
    else:
        betu_leves.append(betu)
        betu_leves.sort()

    print('Rögzített betűk:', betu_leves)

""" 


"""
#1.1

print('Nagybetűsen:', input('Szó: ').upper())

#1.2

lista = ['mit', 'sütsz', 'kis', 'szűcs', 'sós', 'húst', 'sütsz', 'kis', 'szűcs']

mas_lista = [szo.upper() for szo in lista]

print('Eredeti:', lista)
print('Nagybetűs:', mas_lista)

#1.3

lista = ['mit', 'sütsz', 'kis', 'szűcs', 'sós', 'húst', 'sütsz', 'kis', 'szűcs']

mas_lista = [szo.upper() for szo in lista if len(szo) > 3]

print('Eredeti:', lista)
print('Nagybetűs:', mas_lista)

#1.4 (Feltételezem, hogy a str metódusok a listájához küldött a feladat.)

lista = ['Python', 'eHázi', 'HU']

mas_lista = [szo.swapcase() for szo in lista]

print('Eredeti:', lista)
print('Ellentétesbetűs:', mas_lista)

2.1 (Gőzöm sincs mit akarhat. Talán ezt. Talán nem. A matek nem az erősségem.)

ertelmezesi_tartomany = list(range(-3, 5))

ertek_keszlet = [2 * x - 3 for x in ertelmezesi_tartomany]

print('Értelemzési tartomány:', ertelmezesi_tartomany)
print('Érték készlet:', ertek_keszlet)

#2.2

ertelmezesi_tartomany = list(range(-3, 5))

ertek_keszlet = [2 * x - 3 for x in ertelmezesi_tartomany if x >= 0]

print('Értelemzési tartomány:', ertelmezesi_tartomany)
print('Érték készlet:', ertek_keszlet)
"""