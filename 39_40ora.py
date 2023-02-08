"""
szamok = [3,21,7,63,9,27,]
print(min(szamok))
print(max(szamok))
def szelso_ertek():
    min = szamok[0]
    max = szamok[0]

    for szam in szamok:
        if szam < min:
            min = szam
        if szam > max:
            max = szam       

    print(f'szamok listában a legkisebb {min}')
    print(f'szamok listában a legknagyobb {max}')       

szelso_ertek()    
"""


#2
# a llista elemeinek összegzése

szamok = [3,21,7,63,9,27,]
osszeg = 0
for rész in szamok:
    osszeg = osszeg + rész
print(f'Ennyi az összeg {osszeg}') 


# a llista elemeinek átlagának számítása
atlag = None
atlag = osszeg / len(szamok)
print(f'a lista elemeinek átlaga: {atlag:.2f}')
