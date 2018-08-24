#Tom liste
mineOrd = []
#En variabel som sørger for første gjennomkjøring av whileløkken
bokstav = "a"

#Funksjon som konktenerer to streng-parametre
def slaaSammen(streng1, streng2):
    return streng1 + streng2

#Funksjon som skriver ut hvert element i en liste.
def skrivUt(liste):
     for element in liste:
         print(element)

#Hovedprogram som kjører helt til brukeren taster s
while bokstav != "s":
    bokstav = input("Skriv i eller u: (s for å avslutte) ").lower()
#Kjører konkatenerer funksjonen
    if bokstav == "i":
        streng1 = input("skriv inn en streng: ")
        streng2 = input("skriv inn en streng til: ")
        mineOrd.append(slaaSammen(streng1, streng2))
#Kjører skriv ut funksjonen
    elif bokstav == "u":
        skrivUt(mineOrd)
