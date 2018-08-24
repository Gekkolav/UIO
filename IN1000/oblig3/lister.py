#Oppgave 1
#Lager først en liste med 3 tall, så legger til et tall med .append

#Del 1
liste= [2, 4, 6]
liste.append(19)
#Printer første og tredje tall i lista
print("Foerste tall i liste: ", liste[0], ", andre tall i liste:", liste[2])
#Del 2
navnListe=[]
#Tar inn 4 navn som blir lagt til i den tomme lista definert rett over
for i in range(0,4):
    navnListe.append(input("Skriv inn ett navn: ").lower())
#Del 3
#Gjorde om alle bokstaver til små bokstaver med .lower() i input
#Sjekker om navnet Olav er skrevet med en IF.
if "olav" in navnListe:
    print("Du husket meg! \n" )
else:
    print("Glemte du meg? \n")
#Del 4
#Lager en ny liste ved å slå sammen de to forrige listene
nyListe=liste+navnListe
#Printer den nye lista
print(nyListe)
#fjerner de 2 siste elemntene i lista.
del nyListe[-2:]
#Printer den nye lista
print(nyListe)
