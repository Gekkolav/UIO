#funksjoner


#Del 1
#Definerer funksjonen adder, som tar inn 2 variabler
def adder(tall1, tall2):
    summen=tall1+tall2
    #Returnerer summen
    return summen

#Kaller funksjonen 2 ganger med en løkke
for i in range (0,2):
    #Definerer inputen til funksjonen, dette kan også gjøres når den blir kalt,
    #men synes dette er ryddigere.
    tall1 = i+2
    tall2 = i +10
    print("summen av tallene er", adder(tall1, tall2))

#Del 2
#tar inn 2 strenger
tekst = input("Skriv en tekststreng her: ")
bokstav = input("Skriv en bokstav her: ")

#Gjør om strengen til en liste med bokstaver
bokstaverliste = list(tekst)


# Del 3
#Definerer funksjonen som tar inn to strenger og sjekker hvor mange ganger
#den ene strengen forekommer i den andre
def tellForekomst(minTekst, minBokstav):
    tellBokstav=0
    #Sjekker hver bokstav i strengen mot den valgte.
    for i in range(0,len(minTekst)):
        if minBokstav == minTekst[i]:
            tellBokstav += 1
    #Returnerer hvor mange ganger vi fant bokstaven
    return tellBokstav

#Her kaller jeg på funksjonen
antall = tellForekomst(bokstaverliste,bokstav)
#Her printer resultatet,
print("Bokstaven " + bokstav + " forekommer ", antall, "ganger i strengen: " + tekst)
