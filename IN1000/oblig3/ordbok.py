#Lager en ordbok med varer linket til priser.
#Del 1
varer={"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
#Printer ordboka
print(varer)
#Del 2
#Leser inn to nye varer "nøkler" og priser som blir linket i ordboka.
for i in range(0,2):
    #Spørr etter vare
    vare=input("Skriv inn en vare her: ").lower()
    #Spør etter pris på 'vare'
    pris=float(input("Skriv inn prisen på " + vare + " her: "))
    #setter inn i ordboka
    varer[vare]=pris
#Printer varene
print(varer)
