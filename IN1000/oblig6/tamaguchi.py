#Definerer tamaguchi-klassen
class Tamaguchi:
    #Initierer objektet
    def __init__ (self, hp, hunger, fat):
        self._hp = hp
        self._hunger = hunger
        self._fat = fat
#Under er de forskjelllige instansmetodene som forandrer instansvariablene til objektet.
    def eat(self, mass):
        self._hunger += mass
        self._fat += mass

    def workOut(self, much):
        self._fat -= much
        self._hunger -= much

    def sjekkTilstand(self, name):
        if self._hunger < 2:
            print(name + " er livstruende sulten")
            self._hp -=1
        elif self._hunger < 4:
            print(name+ " begynner å bli sulten")
        elif self._hunger > 10:
            self._hunger = 10
            print(name + " er mett og kan ikke spise mer")

        if self._fat < -2:
            print(name + " er livsfarlig tynn")
            self._hp -=1
        elif self._fat < 0:
            print(name + " begynner å bli farlig tynn")
        elif self._fat > 8:
            print(name + " er farlig overvektig!")
            self._hp -=1
        elif self._fat > 6:
            print(name + " begynner å bli overvektig")

    def wait(self):
        self._hunger -= 1

    def alive(self):
        if self._hp > 0:
            return True
        else:
            return False

    def hp(self):
        print("hp: ", self._hp )
