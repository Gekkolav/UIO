#test motorsykkelklassen

from motorsykkel import Motorsykkel

def hovedprogram():
#Lager tre motorsykkelobjekter
    motorsykkel1 = Motorsykkel("Yamaha", "C6H12O6", 31415)
    motorsykkel2 = Motorsykkel("BMW", "DNTH8M8", 1337)
    motorsykkel3 = Motorsykkel("Suzuki", "Gr81mL8", 6959)
#Skriver dem ut.
    motorsykkel1.skrivUt()
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt()
#Kjører 10 km
    motorsykkel3.kjor(10)
#Viser at vi har kjørt 10 km
    motorsykkel3.hentKilometerstand()

hovedprogram()
