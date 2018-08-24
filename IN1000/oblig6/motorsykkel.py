#Definerer klassen Motorsykkel
class Motorsykkel :
#Initierer
    def __init__(self, merke, regnummer, kilometerstand):
        self._merke = merke
        self._regnummer = regnummer
        self._kilometerstand = kilometerstand
#Legger til kilometer kjørt
    def kjor(self, km):
        self._kilometerstand += km

#Printer kilometer kjørt
    def hentKilometerstand(self):
        print("\nDu har no kjort: ", self._kilometerstand)
#Printer alt
    def skrivUt(self):
        print("\nMotorsykkelinfo:\nMerke: %s\nRegNummer: %s\nKilometerstand: %s" % (self._merke, self._regnummer, self._kilometerstand))
