#1.szélsőérték meghatározása(min,max)

lista = [12,5,4,8,9,11,10,12,6]


def  szelsoertek_10c(munka_lista):
    min = munka_lista[0]
    max = munka_lista[0]
    
    for szam in lista:
        if szam < min:
            min = szam
        if szam > max:
            max = szam   

    print(f"A legkisebb szám a lista {min}")
    print(f"A legnagyobb szám a lista {max}")          

szelsoertek_10c(lista)