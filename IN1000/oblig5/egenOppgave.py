# Linux har en liste med innebygde ord.
# Lag et enkelt hangman spill med et tilfeldig ord fra den lista


#Importerer random
from random import randint


#Hovedprogrammet mitt
def main():
    #Definerer en del variabler
    ordbok = open("ord.txt")
    alive = True
    ordliste = []
    vunnet = False
    lettersGuessed= []

    life = 8
    #Kaller funksjonen som finner et tilfeldig ord
    riktigBokstaver = finnOrd(ordbok)
    #Kaller funksjonen som oppdaterer hvordan ordet ser ut
    tomtOrd = lagTomtOrd(riktigBokstaver)
    #while løkke som kjører dersom man ikke har vunnet og fortsatt lever
    while sjekkAlive(life) and not vunnet:
        print("Dette er ordet ditt: ", tomtOrd, "\n")
        print("Bokstaver gjettet som var feil %s \nDu har %s forsøk igjen \n" % (lettersGuessed, life))
        #Ber bruker om en bokstav
        bokstav = input("Skriv inn en bokstav: ")
        #Kaller funksjonen sjekkBokstav
        #Den sjekker om bokstaven  er i ordet.
        #Den kunne vært splitta i flere funksjoner for åbli mer oversiklig
        #Litt mange parametre inn og ut, ettersom den gjør mer enn bare å sjekke.
        tomtOrd, life, lettersGuessed = sjekkBokstav(bokstav, riktigBokstaver, tomtOrd, life,lettersGuessed)
        #Sjekker om spiller har vunnet.
        vunnet =spillSlutt(life, riktigBokstaver, tomtOrd)
    spillIgjen=input("Vil du spille på nytt? [y/n]: ").lower()
    if spillIgjen == "y":
        main()





#----------Definerer de brukte parametrene under-------------


def finnOrd(ordbok):
    teller = 0
    funnetOrd = False
    rand = randint(0, 99170)
    riktigOrd = ""

    while not funnetOrd:
        for word in ordbok:
            if teller == rand:
                riktigOrd = word.lower()
                listOrd = list(riktigOrd)
                del listOrd[-1]
                funnetOrd = True
                if "'" in listOrd:
                    rand += 1
                else:
                    return listOrd
            else:
                teller += 1


def lagTomtOrd(riktigBokstaver):
    tomtOrd=[]
    for i in range(len(riktigBokstaver)):
        tomtOrd.append(" __ ")
    return tomtOrd


def sjekkBokstav(bokstav, riktigBokstaver, tomtOrd, life, lettersGuessed):
    teller=0
    if bokstav in riktigBokstaver:
        for letter in riktigBokstaver:
            if bokstav == letter:
                tomtOrd [teller] = bokstav
            teller += 1
    else:
        lettersGuessed.append(bokstav)
        life -= 1
        print ("Feil! prøv igjen \n")

    return (tomtOrd, life, lettersGuessed)



def sjekkAlive(life):
    if life <= 0:
        return False
    else:
        return True
#print(riktigBokstaver)

def spillSlutt(life, riktigBokstaver, tomtOrd):
    if life <= 0:
        print("Du tapte!!!")
        print("     =========#")
        print("     ||       ¦")
        print("     ||       ¦")
        print("     ||       O")
        print("     ||      /|\\")
        print("     ||       |")
        print("     ||       /\\")
        print("     ||       ")
        print("  |------|       ¦")
        print("Ordet ditt var", riktigBokstaver)
        return False
    elif " __ " not in tomtOrd:
        print("Gratulerer du vant!!")
        print("  **      * '  *")
        print("  ***")
        print("   **           *")
        print("  *    \\O/   *")
        print(" *      |   '  ' ")
        print("  '     /\\   *   ")
        print("Ordet ditt var", riktigBokstaver)
        return True


main()
