#Reiseplan

#Del 1 og 2
#Lager 3 tomme lister.
steder = []
klesplagg = []
avreisedatoer = []

#3 for løkker som ber deg først sette in reisemål, klesplagg så dato
for i in range(0,5):
    steder.append(input("skriv inn et reisemål: "))

for i in range(0,5):
    klesplagg.append(input("skriv inn et klesplagg: "))

for i in range(0,5):
    avreisedatoer.append(input("skriv inn en avreisedato: "))
#Del 3
#Legger alt dette i en felles liste
reiseplan = [steder, klesplagg, avreisedatoer]

#Del 4
#Printer for each
for i in reiseplan:
    print(i)

#Del 5
#to inputs for å hente ut en verdi fra reiseplan[i][j]
i=-1+int(input("\ntast 1 for steder \nTast 2 for klesplagg \ntast 3 for avreisedato\n ditt tall: "))

j=-1+int(input("\ntast 1,2,3,4 eller 5 for å velge posisjon i din valgte liste: \n"))

if i <0 or i > 2 or j < 0 or j > 4:
    print("ugyldig verdi")
else:
    print(reiseplan[i][j])
