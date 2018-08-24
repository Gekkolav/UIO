#Egen Oppgave

#Lag en liste med 15 dyr og ting, be brukeren om å plassere disse dyrene i hver sin liste
#dette er for at brukeren skal sortere denne lista for deg.
#Hver liste skal i en dyre liste eller i en ikkeDyr liste, og disse skal i en liste om alt.

#Lager en usortert liste
usortert = ["katt", "komodovaran","molybden", "kornsnok", "pils", "grevling","bronsje", "superduplex steel", "hest", "maurpinnsvin", "gull", "menneske", "kufiolilla", "nepe", "melk"]
#lager lister som hører til dyr
reptiler=[]
pattedyr=[]
pattedyrEgg=[]
dyr=[reptiler, pattedyr, pattedyrEgg]
#Lager lister som hører til ting
metaller=[]
legeringer=[]
matDrikke=[]
ingen=[]
ting=[metaller, legeringer, matDrikke, ingen]

#Lager en liste hvor alt er sortert
sortert=[dyr, ting]
#sorterer alt ved bruk av en løkke og If etninger
for i in range(0,15):
    svar_Dyr=input("Er " + usortert[i] + " et dyr? [y/n]: " ).lower()
    if svar_Dyr=="y":
         listenr=int(input("tast Nr tilsvarende den kategorien du mener " + usortert[i]+ " hører til i: \n 1. Retil \n 2. Pattedyr \n 3. Pattedyr som legger egg\n svar: "))
         if listenr==1:
             reptiler.append(usortert[i])
         elif listenr==2:
             pattedyr.append(usortert[i])
         else:
             pattedyrEgg.append(usortert[i])
    else:
        listenr=int(input("tast Nr tilsvarende den kategorien du mener " + usortert[i]+ " hører til i: \n 1. Metall \n 2. Legering \n 3. Mat og drikke\n 4. ingen av dem \n svar: "))
        if listenr==1:
            metaller.append(usortert[i])
        elif listenr==2:
            legeringer.append(usortert[i])
        elif listenr==3:
            matDrikke.append(usortert[i])
        else:
            ingen.append(usortert[i])

#Printer resultatet med en dobbel forløkke 
print("din liste er")
for i in range (0,2):
    for j in sortert[i]:
        print(j)
