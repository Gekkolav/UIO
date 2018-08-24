#Lag et program som spørr etter en liste med X antall tall i Fibonacci tallsekvens

#Spørr først hvor mange tall man vil ha
x=int(input("Hvor lang skal Fibonacci være? "))
#lagrer de 2 første tallene for å gjøre det enkelt
fib=[1, 1]
#Sjekker om bruker spørr om bare 1 tall da lista vår starter med 2 tall.
if x<2:
    print("Her er det første tallet, velg et større tall neste gang kanskje?\n", fib[0])
else:
    #kjører en løkke som legger til et tall i lista som er summen av de to forige tallene.
    for i in range(0,x-2):
            fib.append(fib[i]+fib[i+1])
    #printer lista
    print("Her er de ", x, "første tallen: \n", fib)

#Var dette for svakt? Vet ikke helt hvor vanskelig du vil vi skal gjøre de egne oppgavene.
#Og det er jo mye morsommere å lage egne oppgaver enn å følge eksemplet, selv om jeg løste det også.
