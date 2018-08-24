#regnefunksjoner

#------Definerer prosedyrene og funksjonene ---------

#Tar inn 2 parametre, og adderer dem
def addisjon(tall1, tall2):
    added = tall1 + tall2
    return added
#Tar inn 2 parametre, og subraherer dem
def subtraksjon(tall1, tall2):
    subbed = tall1 - tall2
    return subbed

#Tar inn 2 parametre, og dividerer dem
def divisjon(tall1, tall2):
    divided = tall1 / tall2
    return divided

#tar inn en parameter og gjør den om til cm
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    antallCm = antallTommer * 2.54
    return antallCm

#selve prosedyren har ingen parametre som teas inn, men i prosedyren
#tar den in 2 variabler fra input.
def skrivBeregninger():
    tall1 = float(input("Skriv inn tall 1: "))
    tall2 = float(input("Skriv inn tall 2: "))
    #Kaller de 3 regnefunksjonene og printer resultatet.
    print("\nResultat av summering: ", addisjon(tall1, tall2))
    print("Resultat av subtraksjon: ", subtraksjon(tall1, tall2))
    print("Resultat av divisjon: ", divisjon(tall1, tall2))
    #Kaller konverteringsfunksjonen og printer resultatet.
    tall = float(input("\n Konvertering fra tommer til Cm \n Skriv inn et tall: "))

    print("Resultat: ", tommerTilCm(tall))

#--------Kaller prosedyren skrivBeregninger----------
skrivBeregninger()
