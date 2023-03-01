def osszegzes_tetele():


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
    lista1 = [2, 5, 4, 8, 9, 11, 10, 12]
    
    talalat = False
    index = 0
    while index < len(lista1) and not talalat:
        if lista1[index] % 3 == 0:
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


#-----------------------------------------------------------------------


def szamlalas_tetele():

    lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

    darab = 0
    for szam in lista:
            if szam % 3 == 0:
                darab = darab + 1

    print('A listában lévő hárommal osztható számok száma: ', darab)  


#----------------------------------------------------------------------

def szelsoertek_tetele():

    lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

    min = lista[0]
    max = lista[0]
    for szam in lista:
            if szam < min:
                min = szam
            if szam > max:
                max = szam

    print('A legkisebb szám a listában: ', min)
    print('A legnagyobb szám a listában: ', max)

#--------------------------------------------------------------------
#-------------------------------------------------------------------

while True:
    print("1 = összegzés")
    print("2 = eldöntés")
    print("3 = keresés")
    print("4 = kiválasztás")
    print("5 = Megszámlálás")
    print("6 = Szélsőérték")
    fuggveny = int(input("kérem a függvény számát: "))
    if fuggveny == 1:
        osszegzes_tetele()
    elif fuggveny == 2:
        eldontes_tetele()
    elif fuggveny == 3:
        kereses_tetele()   
    elif fuggveny == 4:
        kivalasztas_tetele()
    elif fuggveny == 5:
        szamlalas_tetele()
    elif fuggveny == 6:
        szelsoertek_tetele()   
    elif fuggveny == 0:
        print("Program vége!")
        break             
       



  