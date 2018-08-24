from random import randint

class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._naboer = []

    def legg_til_nabo(self, nabo):
        if not nabo in self._naboer:
            self._naboer.append(nabo)

    def hent_navn(self):
        return self._navn

    def hent_tilfeldig_nabo(self):
        valgt = randint(0,len(self._naboer)-1)
        return self._naboer[valgt]

def fordrukken_traversering(start_stasjon, maal_stasjon):
    stasjon = start_stasjon
    antall_strekninger = 0
    while not stasjon == maal_stasjon:
        stasjon = stasjon.hent_tilfeldig_nabo()
        antall_strekninger += 1
        print( stasjon.hent_navn() )
    print("Antall strekninger: " + str(antall_strekninger) )

def hovedprogram():
    stasjonsbok = {}
    for linje in open("ruter_full.txt"):
        biter = linje.strip().split()
        fra = biter[0]
        til = biter[1]
        if not fra in stasjonsbok:
            stasjonsbok[fra] = Stasjon(fra)
        if not til in stasjonsbok:
            stasjonsbok[til] = Stasjon(til)
        fra_stasjon = stasjonsbok[fra]
        til_stasjon = stasjonsbok[til]
        fra_stasjon.legg_til_nabo(til_stasjon)
        til_stasjon.legg_til_nabo(fra_stasjon)

    start = input("Hvor starter du?: ")
    start_stasjon = stasjonsbok[start]
    maal = input("Hvor skal du ende opp?: ")
    maal_stasjon = stasjonsbok[maal]
    fordrukken_traversering(start_stasjon, maal_stasjon)

hovedprogram()
