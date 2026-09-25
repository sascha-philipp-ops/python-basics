batterie = 30 # Startwert

# Solange die Bedingung (batterie > 0) wahr ist, läuft die Schleife


while batterie > 0:
    print(f"Status: {batterie}% - System läuft...")
    batterie -= 10 # Wir ziehen pro Schritt 10% ab (wichtig, sonst Endlosschleife!)

print("System fährt herunter: Batterie leer.")

# ZUSAMMENFASSUNG:
# Warum: Wenn ein Zustand erreicht werden muss (Wahr/Falsch).
# Wie oft: In diesem Fall 3 Mal (bei 30, 20 und 10). Bei 0 ist die Bedingung falsch.