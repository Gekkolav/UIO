
#definerer funksjonen minFunksjon, tar ikke inn noen parametre.

#Så definerer hovedprogram, ingen paramtre inn

#så kalles hovedprogram prosedyren

# I hovedprogramprosedyren settes a = 42
# b = 0
# printer b som er 0
# b settes lik 42
# a settes lik verdien som returnes fra minFunksjon

#i minFunksjon skjer:
#kjører en løkke 2 ganger hvor x = 0 og x = 1.
#I starten av løkka settes c = 2 for så å bli printet
# c +=1 gir c = 3
# b settes lik 10
#b plusses med a OBS, a er ikke deklarert og vil gi error
#For at dette skal kjøre er man avhengig av å enten deklarere a i funksjonen
#Eller gi den som input i funksjonen
#printer b
#så kjører løkka en gang til
# så returneres b

# printer b og a hver sin linje

#Fiksa versjon!
def minFunksjon (a):
    for x in range ( 2 ):
        c = 2
        print ( c)
        c += 1
        b = 10
        b += a
        print ( b )
    return ( b )
def hovedprogram():
    a = 42
    b = 0
    print ( b )
    b = a
    a = minFunksjon (a)
    print ( b )
    print ( a )

hovedprogram()
