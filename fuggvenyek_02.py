#7
#A lower()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter kisbetű.
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#8
#A upper()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter nagybetűs.
txt = "Hello my friends"

x = txt.upper()

print(x)

#9
#A capitalize()metódus egy karakterláncot ad vissza, ahol az első karakter nagybetű, a többi pedig kisbetű.
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#10
#A endswith()metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel végződik, ellenkező esetben False-t.
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

#11
#A find()metódus megkeresi a megadott érték első előfordulását.
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#12
#A isalnum()metódus igaz értéket ad vissza, ha az összes karakter alfanumerikus, azaz ábécé betűi (az) és számok (0-9).
txt = "Company12"

x = txt.isalnum()

print(x)

#13
#A isalpha()metódus igaz értéket ad vissza, ha az összes karakter ábécé betűje (az).
txt = "CompanyX"

x = txt.isalpha()

print(x)

#14
#A islower()metódus igaz értéket ad vissza, ha minden karakter kisbetűvel van írva, ellenkező esetben False-t.
txt = "hello world!"

x = txt.islower()

print(x)

#15
#A join()metódus az összes elemet iterálhatóvá teszi, és egyetlen karakterláncba egyesíti.
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#16
#A replace()metódus lecserél egy megadott kifejezést egy másik megadott kifejezésre.
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#17
#A rfind()metódus megkeresi a megadott érték utolsó előfordulását.
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

#18
#A rstrip()metódus eltávolítja a záró karaktereket (a karakterlánc végén lévő karaktereket), a szóköz az alapértelmezett eltávolítandó karakter.
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

#19
#A startswith()metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel kezdődik, ellenkező esetben False-t.
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

#20
#A strip()metódus eltávolítja a kezdő (szóköz az elején) és a záró (szóköz a végén) karaktereket (a szóköz az eltávolítandó alapértelmezett kezdő karakter).
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

#21
#A swapcase()metódus egy karakterláncot ad vissza, ahol az összes nagybetű kisbetű, és fordítva.
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#22
#A title()metódus egy karakterláncot ad vissza, ahol minden szó első karaktere nagybetű. Mint egy fejléc vagy egy cím
txt = "Welcome to my world"

x = txt.title()

print(x)

#23
#A center()metódus középre igazítja a karakterláncot, és egy megadott karaktert használ (a szóköz az alapértelmezett) kitöltési karakterként.
txt = "banana"

x = txt.center(20)

print(x)