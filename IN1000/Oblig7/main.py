#Main

#Importerer de to klassene
from celle import Celle
from spillebrett import Spillebrett

#Definerer Main
def main():
    generation = 0
    #Ber om antalll kolonner og rader
    boardHight = int(input("Skriv inn hvor mange kolonner du vil ha: "))
    boardWidth = int(input("Skriv inn hvor mange rader du vil ha: "))

    #Konstruerer brett-objektet
    board = Spillebrett(boardWidth, boardHight)
    #Kaller metoden til brettobjektet som lager et nytt brett
    board.makeBoard()
    #Printer altall levende celler og generasjon
    print("Antall levende celler: ", board.findAlive())
    print("Dette er %s generasjon" % (generation))
    #Kaller metoen som tegner brettet
    board.drawBoard()
    #Har en løkke som kjører så lenge input ikke er q
    while input("tast q for å avslutte, eller bare tast enter for å fortsette: ") != "q":
        #Denne løkka er kun får å tømme sida.
        for i in range(20):
            print("\n")
        #Oppdaterer generasjonen
        generation += 1
        #Oppdaterer alt
        board.update()
        print("Antall levende celler: ", board.findAlive())
        print("Dette er %s generasjon" % (generation))





#Kaller på main.
main()
