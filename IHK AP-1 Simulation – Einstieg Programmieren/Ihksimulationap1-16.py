# Endlosschleife 
# Die Schleife hört nie auf, weil die Abbruchbedingung nie aufhört
# Beispiel:

i =1
while i <= 5:
    print(i)

# Off-by-one Fehler -> Die Schleife läuft zu oft odr zu selten, weil start oder Endwert
#faslsch gewählt wurden 

for in range (1, 5):
    print (i) läuft nur von 1-4 evt fehlt 5 