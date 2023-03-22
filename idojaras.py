#napi hőmérséklet max,min marc 22-től apr 20-ig EMŐD
#a prgram globális véltozói
from statistics import harmonic_mean


napi_max = [14,17,21,15,16,13,8,11,12,14,16,16,14,15,13,14,16,16,14,12,12,10,11,13,15,17,19,17,19,20]
napi_min = [8,8,9,6,7,1,0,2,3,5,4,4,3,5,4,6,8,6,4,2,1,-1,-1,1,3,5,7,5,7,9]
napi_minimum_darab = None
napi_miaximum_darab = None

harmonic_napi_atlag = []
#1.feladat Hány darab eleme van a napi max es a napi min listanak 
def napimax(napi_max):
    darab = 0
    for szam in napi_max:
        darab = darab + 1
    return darab

print(f"napi max elem : {napimax(napi_max)} db")

def napimin(napi_min):
    darab = 0
    for szam in napi_min:
        darab = darab + 1
    return darab

print(f"napi min elem : {napimax(napi_min)} db")

#2.feladat

def atlag_max(napi_max):
    lista_elemeinek_osszege = 0
    for szam in napi_max:
        lista_elemeinek_osszege = lista_elemeinek_osszege + szam
    atlag = lista_elemeinek_osszege / len(napi_max)    
    return atlag

print(f"napi max elem átlaga : {atlag_max(napi_max)} ")

def atlag_min(napi_min):
    lista_elemeinek_osszege = 0
    for szam in napi_min:
        lista_elemeinek_osszege = lista_elemeinek_osszege + szam
    atlag = lista_elemeinek_osszege / len(napi_min)    
    return atlag

print(f"napi min elem átlaga : {atlag_min(napi_min)} ")

#3.feladat 30 napos atlag hőmérséklet
#3.a

print(f"A 30 napos atlag homerseklet : {(atlag_max(napi_max) + atlag_min(napi_min)) /2}")

#3.b Szamítsuk ki a napi átlag hőmérséletét és tároljuk el egy étlag listában






