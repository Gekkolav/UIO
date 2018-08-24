#
# Variabelen a tar inn et tall i form av en streng.
#Variabelen b gjør om strengen a om til in integer.
#if statementen sier at dersom b mindre enn 10
#MEN her vil den i print funksjonen plusse sammen en int og en streng "Hei!"
#Den siste operasjonen er ikke lovelig. Enten gjør b om til en streng, eller sett inn et komma i printfunskjonen.
a = input ( "Tast inn et heltall! " )
b = int ( a )
if b < 10 :
print ( b + "Hei!" )

#Prøvde å kjøre koden, og det viste seg å være riktig.
