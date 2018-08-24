#lagrer variablen temperatur som et fil.txt element
temperaturer = open("temperatur.txt")
#Tom liste
listeTemp=[]
#Legger hver linje i fila som int i en liste
for temp in temperaturer:
    listeTemp.append(int(temp))


Funksjon som tar inn en liste og gir ut gjennomsnittet av lista
def average(liste):
    snitt = 0
    for i in liste:
        snitt += i
#Printer resultatet
    print("gjennomsnittet er ", snitt/len(liste))
#Kaller funksjonen finn gjennomsnittet
average(listeTemp)
