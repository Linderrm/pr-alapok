#python lista
lista = ["alma", "banán", "cseresznye"]
print(lista)
#------------------------------------------------

lista = ["alma", "banán", "cseresznye", "alma", "banán",]
print(lista)
#----------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
print(len(lista))
#---------------------------------------------------

lista1 = ["alma", "banán", "cseresznye"] #string
lista2 = [1, 5, 7, 9, 3] 
lista3 = [True , False , False]
#-------------------------------------------------

lista5 = ["alma", "banán", "cseresznye"]
print(type(lista5))
# <class 'list'>
#--------------------------------------------------------

lista5 = list (("alma", "banán", "cseresznye")) # vegye figyelembe a dupla kerek zárójelet
print(lista)
# ['alma', 'banán', 'cseresznye']
#------------------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
print(1)
#banán
#------------------------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
print([-1])
#cseresznye
#---------------------------------------------------------------------

lista = ["alma-0" , "bamán-1", "cseresznye-2", "naramcs-3", "kivi-4", "szőlő-5", "mangó-6"]
print (lista[2:5])
#-------------------------------------------------------------------------- 

lista = ["alma-0" , "bamán-1", "cseresznye-2", "naramcs-3", "kivi-4", "szőlő-5", "mangó-6"]
if "banán-1" not in lista:
    print(" banán-1 nem szerepel")
#--------------------------------------------------------------------------------------

lista = ["alma-0" , "bamán-1", "cseresznye-2", "naramcs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista[1:3] = ["körte","szilva"]
print(lista)
#----------------------------------------------------------------------------------------------

lista = ["alma-0" , "bamán-1", "cseresznye-2", "naramcs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista[1:3] = ["körte"]
print(lista)
#-------------------------------------------------------------------------------------------------

lista = ["alma-0" , "bamán-1", "cseresznye-2", "naramcs-3", "kivi-4", "szőlő-5", "mangó-6"]
lista.insert(2, "körte")
print(lista)
#--------------------------------------------------------------------------------------------------

lista = ["alma", "banán", "cseresznye"]
lista.append ("körte")
print(lista)
#------------------------------------------------------------------------------------------------------