#telefonsalg
#Leser inn fra fil.
def innlesning(filnavn):
    dictionary = {}
    for line in filnavn:
        nameNum = line.split()
        dictionary[nameNum[0]] = int(nameNum[1])

    return dictionary

#Finner person med mest salg
def maanedensSalgsperson(ordbok):
    salgstall = 0
    for key in ordbok:
        if ordbok[key] > salgstall:
            salgspers = key
            salgstall = ordbok[key]

    return salgspers

#Finner totalt antall salg
def totaltAntallSalg(ordbok):
    total = 0
    for key in ordbok:
        total += ordbok[key]

    return total
#Finner gjennomsnittSalg
def gjennomsnittSalg(ordbok):
    return totaltAntallSalg(ordbok)/len(ordbok)

#definerer hovedprogrammet
def hovedprogram():
    #Variabler for hovedprogrammet
    salgsFila = open("salgstall.txt")
    #Kaller de forskjellige funksjonene
    salgsbok = innlesning(salgsFila)
    maanedensPerson = maanedensSalgsperson(salgsbok)
    totalesalg = totaltAntallSalg(salgsbok)
    snittSalg = gjennomsnittSalg(salgsbok)
#Printer resultatene.
    print("maanedens salgsperson er %s med %s salg" % (maanedensPerson, salgsbok[maanedensPerson]))

    print("Aktive selgere: ", len(salgsbok))
    print("Totalt antall salg: ", totalesalg)
    print("gjennomsnitt antal salg: ", snittSalg)

hovedprogram()
