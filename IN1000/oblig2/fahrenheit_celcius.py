#Programmet tar inn en temperatur i fahrenheit, så gjør den om til en integer og regner den om til celcius.
tempF=int(input("Skriv en temperatur i fahrenheit her: "))
#Printer temperaturen i fahrenheit
print("Temp Fahrenheit = ", + tempF)
#Regner ut temperaturen til celcius
tempC=(tempF-32)*(5/9)
#Printer temperaturen i celcius
print("Temp celcius = ", + tempC)
