#Lag et program som tar inn 3 forskjellige tall etterhverandre.
#Lag så if statements som sjekker og printer ut tallene i stigende rekkefølge.


#Denne blir løst mye mer ellegant med løkker og matriser/vektorer, men gjorde et poeng av å bare bruke ting vi har lært.
#Tar inn 3 variabler
a, b, c = input("Skriv 3 forskjellige tall her skilt med mellomrom: ").split()
#Gjør om variablene til integers
a=int(a)
b=int(b)
c=int(c)
#Kan løses på mange måter, men først sjekker om noen av tallene er like
if a==b or b==c or a==c:
    print("venligst oppgi 3 forskjellige tall")
else:
#Dersom ingen av tallene er like så sjekker den hvilke tall som er størst metodisk.
    if a>b and a>c:
        if b>c:
            print(a , ">" , b , ">" , c)
        else:
            print(a , ">" , c + ">" , b)
    if b>c and b>a:
        if c>a:
            print(b , ">" , c , ">" , a)
        else:
            print(b , ">" , a , ">" , c)
    if c>a and c>b:
        if b>a:
            print(c , ">" , b , ">" , a)
        else:
            print(c , ">" , a , ">" , b)
