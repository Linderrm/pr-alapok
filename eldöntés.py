# van egy n elemü lista a sorozatban van egy T tulajdonság és az algoritmusom megadja 
# nekem hogy van e a listába ilyen T tulajdonságu elem(igen,nem)


lista = [2, 5, 4, 8, 19, 11, 10, 13]

talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index +1 


if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')       
print(talalat)



#2

'''    
Az KERESÉS esetében azt vizsgáljuk, 
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában),
és ha igen, hányadik helyen.

A program azt vizsgálja, hogy szerepel-e a piros szín a listában, és ha igen, hányadik helyen.
'''
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
  