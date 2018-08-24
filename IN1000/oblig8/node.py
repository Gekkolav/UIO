#node-Klasse

class Node:
    #Tar inn minne og antall prosessorer
    def __init__(self, memo, numProcessors):
        self._processors = numProcessors
        self._memory = memo
    #returnerer Minne
    def getMemory(self):
        return self._memory
    #returnerer Prosessorer
    def getProcessors(self):
        return self._processors
