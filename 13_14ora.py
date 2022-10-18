"""
szam1 = int( input("kérek egy számot"))
szam2 = int( input("kétrek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
if szam2 > szam1:
    print("szam2 nagyobb mint szam1")
if szam1 == szam2:
    print("szam1 megegyezik szam2-vel")   """

"""
szam1 = int( input("kérek egy számot"))
szam2 = int( input("kétrek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
elif szam1 == szam2:
    print("szam1 megegyezik szam2-vel") """

"""
szam1 = int( input("kérek egy számot"))
szam2 = int( input("kétrek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
else :
    print("szam1 megegyezik szam2-vel") """

"""
X = None
print(X)
print(type(X))


if X:
    print("Do you think None is True?")
elif X is False:
    print("Do you think None is False")
else:
    print("None is not true,or false,None is just true")"""  

"""
jegy = int(input("kérek egy jegyet 1 és 5 között"))
if jegy == 1:
    print("elégtelen")
elif jegy == 2:
    print("elégséges")
elif jegy == 3:
    print("közepes")
elif jegy == 4:
    print("jó")
elif jegy == 5:
    print("jeles")
"""

"""
#--------------------------------------
#bekérek egy pozitív egész számot és ieassuk ki hogy páros vagy páratlan

szam = int(input("Kérek egy számot"))
if szam % 2 == 0:
    print("a szám páros")
else:
    print("a szám páratlan")   """ 

"""
#---------------------------------------
#véletlen szám előállítása

import random

gondolt_szám = random.randint(1,6)
print("Súgók" ,gondolt_szám)
tipp = int(input("gondoltam egy számra.Tippeld meg"))
if tipp == gondolt_szám:
    print("egyezik")
else:
    print("Nem egyezik")    """



#---------------------------------------------
#generáljunk egy számot 1-1000 között,irassuk ki a számot ha páros és kisbb mint 500,ha nem igaz akkor irja ki hogy a szám nem felelt meg a feltételeknek
 
import random

szam = random.randint(1,1000)
print(szam)
if not(szam % 2 == 0) and szam <= 500:
    print("jó")
else:
    print("Nem felel meg a feltételeknek")  




