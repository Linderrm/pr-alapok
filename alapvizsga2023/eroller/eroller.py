import rollers
objektum_nevek = rollers.Eroller("Akai F10",25,250)
print(f"{objektum_nevek.ToString()}")


roller_nev = input("Kérem a roller nevét: ")
rollers_max_sb = int(input("Kérem a roller max sebességét"))
roller_telj = int(input("kérem a roller teljesítményét"))

eroller1 = rollers.Eroller(roller_nev , rollers_max_sb,roller_telj )
print(eroller1.ToString())


eroller1.szoveg_be_ki()





rollerek = []
ujNev = " "
while ujNev != "":
    ujNev = input("Kérem, adja meg a következő roller márkáját: ")
    if ujNev != "":
        ujSeb = input("Kérem, adja meg a roller maximális sebességét: ")
        ujTelj = input("Kérem, adja meg a roller teljesítményét: ")
        rollerek.append(rollers.Eroller(ujNev,ujSeb,ujTelj))
        print('Sikeres rögzítés')
with open('tobbmint500.txt', 'w', encoding='utf-8') as kimenet:
    for roller in rollerek:
        if roller.teljesitmeny > 500:
            kimenet.write(f"{roller.marka}\n")