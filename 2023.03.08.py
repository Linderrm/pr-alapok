#Linder Martin , A csoport, 2 csoport 2023.03.08
szam_sorozat = [15,4,5,19,2]
def eljaras():

    darab = 0
    x = 0
    for szam in szam_sorozat:
        if x < szam:
            darab = darab + 1

    print(f'A listában {darab} szám van')  


eljaras()