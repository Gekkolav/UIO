#Sirkler
#Importer GraphicsWindow fra ezgraphics
from ezgraphics import GraphicsWindow
#For å gjøre ting litt mer spennende så importerer vi en RNG
from random import randint
#Lager et vindu med navn win
win = GraphicsWindow()
#Definerer et lerret til å tegne på
canvas = win.canvas()

#Definerer litt variabler
teller = 0
x_pos = 10
stoerrelse = 50
farge=["red","blue", "black", "pink", "green", "purple"]

#så lenge teller mindre enn 9 så tegner den en ny figur.
while teller < 9:
    #Tilordner figuren en tilfeldig farge fra min liste
    ran=randint(0,5)
    canvas.setOutline(farge[ran])
    #Tegner en sirkel
    canvas.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    #Forandrer enkelta av variablene til sirkelen
    x_pos += (teller+1)*8
    stoerrelse += 5
    teller += 1




#Hindrer vinduet i å lukke seg ved å vente på en input.
input("Tast enter når du er ferdig med å beundre kunstverket")
