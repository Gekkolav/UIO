#Main
#importerer kun clusterklassen, da det er den eneste jeg vil main skal ha kontakt med
from cluster import Cluster

def main():
    #Tar inn en fil
    clusterfile = open("regneklynge.txt")
    #konstruerer en Cluster objekt.
    abel = Cluster(clusterfile)
    #Printer antal prosessorer

    abel.memoryCheck(32)
    abel.memoryCheck(64)
    abel.memoryCheck(128)
    print("\n")
    abel.numberOfProcessors()
    abel.numberOfRacks()


main()
