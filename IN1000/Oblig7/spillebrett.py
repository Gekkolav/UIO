#spillebrettklassen

#Importerer celle og randint for å få tilgang på nødvendige metoder.
from celle import Celle
from random import randint

#Lager klassen
class Spillebrett:
    def __init__(self, row, column):
        #Definerer objektvariablene
        self._row = row
        self._column = column
        self._cellsGrid =[]
        self._cellsList = []

        #Her tegnes brettet, den bruker metoden hentStatusTegn fra Celle.py
    def drawBoard(self):
        for i in range(self._row):
            for j in range(self._column):
                print(self._cellsGrid[i][j].hentStatusTegn(), end="")
            print("\n")
        for i in range(5):
            print("\n")

    #Her oppdateres spillet.
    def update(self):
        #Lager lister for celler som skal leve og dø.
        #Listene er der for at det blir enklere å gå igjennom hele matrisen før noe blir oppdatert.

        deadCells = []
        aliveCells = []
        aliveNabors = 0

        #går igjennom alle celleobjektene og sjekker ut ifra spillets regler om de skal dø eller leve
        for i in range(self._row):
            for j in range(self._column):
                aliveNabors = 0
                listOfNabors = self.findNabor(i,j)
                for naborCell in listOfNabors:
                    if naborCell.erLevende():
                        aliveNabors += 1
                if self._cellsGrid[i][j].erLevende():
                    if aliveNabors > 3 or aliveNabors < 2:
                        deadCells.append(self._cellsGrid[i][j])
                    else:
                        aliveCells.append(self._cellsGrid[i][j])
                else:
                    if aliveNabors == 3:
                        aliveCells.append(self._cellsGrid[i][j])
                    else:
                        deadCells.append(self._cellsGrid[i][j])
        #alle celler som skal leve blir satt levende
        for cell in aliveCells:
            cell.settLevende()
        #alle celler som skal dø blir satt død
        for cell in deadCells:
            cell.settDoed()
        #Tegner brettet
        self.drawBoard()



    #returnerer hvor mange levende celler i spill
    def findAlive(self):
        numbersAlive = 0
        for i in range(self._row):
            for j in range(self._column):
                if self._cellsGrid[i][j].erLevende():
                    numbersAlive += 1
        return numbersAlive

    #Lager utgangspunktet (seed)
    def makeBoard(self):
        for i in range(self._row):
            for j in range(self._column):
                self._cellsList.append(Celle())
                rand = randint(0,4)
                if rand == 2:
                    self._cellsList[j].settLevende()
            self._cellsGrid.append(self._cellsList)
            self._cellsList = []

    #Returnerer en liste med alle celleObjektene som ligger intill cellen som blir tatt inn
    def findNabor(self, posX, posY):
        listOfNabors = []
        for i in range(-1,2):
            for j in range(-1,2):
                naborX = posX+i
                naborY = posY+j
                #Sjekker at vi ikke tar med den oppgitte cellen
                if (naborX == posX and naborY == posY) == False:
                    #Sjekker at vi ikke er utenfor brettet
                    if (naborX < 0 or naborY < 0 or naborX > self._row-1 or naborY > self._column-1) == False:
                        listOfNabors.append(self._cellsGrid[naborX][naborY])
        return listOfNabors
