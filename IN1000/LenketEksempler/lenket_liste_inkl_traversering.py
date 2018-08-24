class Stasjon:
    def __init__(self, navn):
        self._navn = navn.strip()
        self._nabo = None

    def legg_til_nabo(self, nabo):
        self._nabo = nabo

    def hent_navn(self):
        return self._navn

    def hent_nabo(self):
        return self._nabo

def hovedprogram():
    trikkestall = Stasjon("Trikkestall")
    forrige = trikkestall
    for stasjonsnavn in open("trase.txt"):
        denne = Stasjon(stasjonsnavn)
        forrige.legg_til_nabo(denne)
        forrige = denne

    maal = input("Hvor skal du ende opp?: ")
    lokasjon = trikkestall
    while lokasjon.hent_navn() != maal:
        lokasjon = lokasjon.hent_nabo()
        print(lokasjon.hent_navn())

hovedprogram()
