#rack
#Importerer Node
from node import Node

class Rack:
    #Setter maxNodes max antall noder i en rack
    def __init__(self, maxNodes):
        self._maxNodes = maxNodes
        self._listOfNodes = []

        #Denne funksjonen returnerer true/false avhengig av om det er plass til en til Node
    def isRoom(self):
        if len(self._listOfNodes) >= self._maxNodes:
            return False
        else:
            return True
        #Denne metoden legger til en Node i Rack Objektet sin liste med Noder
    def addNode(self, memo, proc):
        self._listOfNodes.append(Node(memo, proc))
        #Denne funksjonen returnerer listen med Noder
    def getListOfNodes(self):
        return self._listOfNodes
