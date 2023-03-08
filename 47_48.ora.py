#eljaras paraméter nélkül
def koszont():

    print('üdv 10. évfolyam')


koszont()


#eljaras 1 paraméterrel
def koszont_nevvel(nev):
        print('Szia '+ nev +', üdv a fedélzeten!') #
        print(f'Szia {nev}, üdv a fedélzeten!')

koszont_nevvel('Ádám')


#eljaras 2 paraméterrel
def koszont_ket_nevvel(nev1, nev2):
        print('Szia '+ nev1 + ', ' + nev2 +'!\nÜdv a fedélzeten!')

koszont_ket_nevvel('Nóra', 'Ádám')
    
#eljeres paraméterrel exta
def osszead(x, y):
    eredmeny = x + y
    print('A két szám összege: ', eredmeny)


osszead(10, 9)
osszead(5+5, 5+4)

a = 10
b = 9
osszead(a, b) 



    
#Változók hatóköre: globális és lokális változók
    
def kepernyore_ir():
    lokalis_valtozo = 'alma'
    print(lokalis_valtozo)
    print(globalis_valtozo)


globalis_valtozo = 'gyümölcs'
kepernyore_ir()

print(globalis_valtozo)
# a lokalis_valtozo az eljáráson KÍVŰL nem elérhető !!!
print(lokalis_valtozo) # hibát eredményez !!!
    
    




  