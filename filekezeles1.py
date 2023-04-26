#fajl megnyitása
forrasfajl = open("szoveg.txt")
#fajlobjektum tartalmanak bejárása
"""
for sor in forrasfajl:
    print(sor)
forrasfajl.close()
"""
print('----------------------------')

with open('szoveg.txt' , 'r' , encoding = 'UTF-8') as forrasfajl:
    for sor in forrasfajl:
        sor = sor.strip() #Megtisztítom a sor végét
        print(sor,end=' ')
forrasfajl.close() 
print()
print('---------------------------------')

