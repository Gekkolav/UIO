#løkker

#Her definerer jeg et par variabler
#Synes det er ryddig med mye brukte variabler helt øverst
tall=1
listeTall = []
minSum=0

#del 1 og 2
#While tall ikke lik 0, så kjører løkka
while tall != 0:
    tall = int(input("(enter 0 to exit) Skriv inn et tall her: "))
    if tall != 0:
        #Legger til tallet i lista så lenge det ikke er 0
        listeTall.append(tall)
    else:
        #Printer en ny linje dersom tallet er 0
        print("\n")

#del 3
#Alle disse for løkkene kunne vært gjort i samma forløkke.
#Men oppgaven spesifiserer at den vil ha dem i forskjellige løkker

#Printer tallene
for i in range(0, len(listeTall)):
    print("tall nr. ", i, " er ", listeTall[i])


#del 4

#Summerer alle tallene i lista
for i in range(0, len(listeTall)):
    minSum += listeTall[i]
#Printer Summen
print("\nSummen av lista er ", minSum, "\n")

#del 5

#Sjekker det miste tallet, ved å først sette tallet lik første i lista
#Så bytter varibelen hver gang den finner et mindre tall
for i in range(0, len(listeTall)):
    if i == 0:
        minsteTall = listeTall[i]
    elif minsteTall > listeTall[i]:
        minsteTall = listeTall[i]
#Samme fremgangsmåte som for å finne minste tall
#Finner største tall.
for i in range(0, len(listeTall)):
    if i == 0:
        storsteTall = listeTall[i]
    elif storsteTall < listeTall[i]:
        storsteTall = listeTall[i]

#Printer
print("minste tall er: ", minsteTall, " \n" "stoerste tall er: ", storsteTall)
