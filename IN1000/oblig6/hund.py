#Definerer klassen Hund
class Hund:
#Initierer
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10
#Skriv ut alder og vekt
    def skrivUt(self):
        print("Hunden er %s år gammel og veier %s kg" % (self._alder, self._vekt))
#Lar hunden løpe
    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1
#Lar hunden spise
    def spis(self, mengdeMat):
        self._metthet += mengdeMat
        if self._metthet > 7:
            self._vekt += 1
