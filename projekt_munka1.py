def osszegzes_tetele():
    print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
        darab = darab + 1
        osszeg = osszeg + erdemjegy
        erdemjegy = int(input('Add meg az következő érdemjegyet: '))

if darab != 0:
        print('A jegyeid átlaga: ', osszeg / darab)
else:
        print('Nem adtál meg egy jegyet sem!')


#-------------------------------------------------------------------

def eldontes_tetele():
    lista = [2, 5, 4, 8, 9, 11, 10, 12]
    
    talalat = False
    index = 0
    while index < len(lista) and not talalat:
        if lista[index] % 3 == 0:
            talalat = True
        index = index + 1
    
    if talalat:
        print('Van a listában hárommal osztható szám.')
    else:
        print('Nincs a listában hárommal osztható szám.')

#---------------------------------------------------------------------

def kereses_tetele():
    lista = ['kék', 'zöld', 'piros', 'fehér']

    talalat = False
    index = 0
    while index < len(lista) and not talalat:
            if lista[index] == 'piros':
                talalat = True
            index = index + 1

    if talalat:
        print('Van a listában piros szín, az indexe: ', index-1)
    else:
        print('Nincs a listában piros szín.')

#-------------------------------------------------------------------

def kivalasztas_tetele():

    lista = [2, 5, 4, 8, 9, 11, 10, 12]

    talalat = False
    index = 0
    while not talalat:
        if lista[index] % 3 == 0:
            talalat = True
        index = index + 1

        print('A hárommal osztható szám indexe a listában: ', index-1)





print()