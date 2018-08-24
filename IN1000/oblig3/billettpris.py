#Lager en prosedyre som tar inn en alder og lagrer prisen så printer den ut.
def minPros():
    #Setter variabelen billettpris = 0.
    billettpris=0
    #Tar inn en alder som en integer
    alder=int(input("Skriv inn alderen din: "))
    #Sjekker om alder er under 18, eller over 62 og setter pris tilsvarende alder
    if alder <= 17:
        billettpris=30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 50
    #Printer så betalingen
    print("Betal: ", billettpris, ",-")
#Kjører prosedyren 4 ganger med en løkke
for i in range(0,4):
    minPros()

#Det er et problem at hver gang prosedyren blir kalt så settes billettpris=0
#Hvis den absolutt må defineres utenfor if setningen, noe som ikke er nødvendig,
#Burde den vært definert globalt slik at den ikke ble definert til = 0 hver gang.
