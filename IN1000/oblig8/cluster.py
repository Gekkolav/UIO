#Cluster
#Importerer Node og rack da den skal ha kontakt med alt under seg.
#Vil at Cluster skal kunne bruke metodene til Node og Rack
from node import Node
from rack import Rack

#Initierer cluster klassen
class Cluster:
    def __init__(self, clusterfile):
        #Tar inn txt fila med spisfikasjonene
        self._allNodes = clusterfile
        #Lager en liste som skal inneholde alle racks, den starter med å lage et rack Objekt
        self._listOfRacks = []
        self._counter = 0
        #Går igjennom alle linjene i tekstfila
        for line in self._allNodes:
            #Sjekker om det er første linje, da den setter max noder i en rack
            if self._counter == 0:
                self._maxNodes = int(line)
                #Lager en liste som skal inneholde alle racks, den starter med å lage et rack Objekt
                self._listOfRacks.append(Rack(self._maxNodes))
                #Setter counter = 1 så den kjører else: for resten av fila
                self._counter = 1
            else:
                #Setter nodeMemoProc som en liste med [node, minne, prosessorer]
                nodeMemoProc = line.split()
                for i in range(int(nodeMemoProc[0])):
                    self.addNode(int(nodeMemoProc[1]), int(nodeMemoProc[2]))

    #Legger til en Node
    def addNode(self, memory, processors):
        #Sjekker om det er plass i racken, dersom det ikke er plass legger den til en ny rack
        if not self._listOfRacks[-1].isRoom():
            self.newRack()
        #Bruker metoden addNode til rack Objektet for å legge inn noden
        self._listOfRacks[-1].addNode(memory, processors)

    #Sjekker antall prosessorer
    def numberOfProcessors(self):
        nodeProcCounter = 0
        for rack in self._listOfRacks:
            for node in rack.getListOfNodes():
                nodeProcCounter += node.getProcessors()
        print("Number of processors: ", nodeProcCounter)
    #Sjekker antall Racks
    def numberOfRacks(self):
        print("Number of racks: ", len(self._listOfRacks))

    #Sjekker hvor mange Noder som har mer enn eller lik parameter i minne
    def memoryCheck(self, memo):
        nodeMemoCounter = 0
        for rack in self._listOfRacks:
            for node in rack.getListOfNodes():
                if node.getMemory() >= memo:
                    nodeMemoCounter += 1
        print("Noder med minst %s GB: %s" %(memo, nodeMemoCounter))


    def newRack(self):
        self._listOfRacks.append(Rack(self._maxNodes))
