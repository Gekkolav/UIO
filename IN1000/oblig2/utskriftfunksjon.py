#Lager en kodeblokk som jeg kaller 3 ganger i slutten av koden.
#Den spør om Nanv og Bosted og printer ut en setning som bruker begge disse variblene
def mitt_skript():
    Navn, Bosted = input("Hei! skriv hva du heter og hvor du kommer fra skilt med et mellomrom: ").split()
    print("Hei, " + Navn +"! Du er fra " + Bosted)


#Dette kunne blitt løst mye mer elegant med en løkke og en counter.
#Her kaller jeg på mitt_skript 3 ganger.
mitt_skript()
mitt_skript()
mitt_skript()
