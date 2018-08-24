#Celleklassen

class Celle:

    #Konstruktør
    def __init__(self):
        self._alive = False

    #Metoder for å endre status
    def settDoed(self):
        self._alive = False

    def settLevende(self):
        self._alive = True

    #Henter status på celleobjektet
    def erLevende(self):
        return self._alive
    #Henter tegnet som repreresenterer statusen til cellen
    def hentStatusTegn(self):
        if self._alive:
            return(" O")
        else:
            return(" .")
