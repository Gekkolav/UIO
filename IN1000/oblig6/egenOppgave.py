#Lag en enkel Tamaguchi-klone
from random import randint
from tamaguchi import Tamaguchi




#Definerer hovedprosedyren
def main():
#Variabler som navn  og liv og slikt som blir brukt til å lage objektet
    name=input("Hva vil du tamaguchi'n din skal hete?\n")
    age = 0

    hp = randint(3, 5)
    hunger = randint(4, 6)
    fat = randint(0,5)

    ikkeRiktig = False
#Lager objektet
    tama = Tamaguchi(hp, hunger, fat)
#Lager en ordbok som kalller på prosedyrer som kjører de forskjellige metodene til klassen
    actions = {1:eat,2:eatMuch,3:workOut, 4:workOutMore, 5:wait}
#kjører så lenge man er i live
    while tama.alive():
        age += 1
        print("\n")
        tama.hp()
        tama.sjekkTilstand(name)


#Ber bruker si hva de vil gjøre
        ikkeRiktig = True
        while ikkeRiktig:
            action = int(input("Hva vil du gjøre [1-5]?\n1.Spise\n2.Spise masse\n3.Trene\n4.Trene masse\n5.Ikke no\n"))
            if action in actions:
                actions[action](tama)
                ikkeRiktig = False
            else:
                print("Tast bare tallet til den handlingen du vil utføre")

    print("%s ble %s dager gammel" % (name, age))
#de forskjellige metodene som blir referert til i ordboka.
def eat(tama):
    tama.eat(1)

def eatMuch(tama):
    tama.eat(3)

def workOut(tama):
    tama.workOut(1)

def workOutMore(tama):
    tama.workOut(3)

def wait(tama):
    tama.wait()


#Kaller hovedprosedyren
main()
