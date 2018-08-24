#Importer GraphicsWindow fra ezgraphics
from ezgraphics import GraphicsWindow
#Lager et vindu med navn win
win = GraphicsWindow()
#Definerer et lerret til å tegne på
canvas = win.canvas()
#Setter en rød farge på neste figur
canvas.setOutline("red")
#Tegner en oval med like radiuser altså en sirkel.
canvas.drawOval(10,10, 50, 50,)
#Hindrer vinduet i å lukke seg ved å vente på en input.
input("Tast enter når du er ferdig med å beundre kunstverket")
