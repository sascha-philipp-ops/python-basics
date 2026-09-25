# =========================
# Klasse (Bauplan)
# =========================
class Grafikkarte:
    def __init__(self, id, name, hersteller, preis, speicher_gb, anschluss, leistungsklasse):
        self.id = id
        self.name = name
        self.hersteller = hersteller
        self.preis = preis
        self.speicher_gb = speicher_gb
        self.anschluss = anschluss
        self.leistungsklasse = leistungsklasse

    def anzeigen(self):
        print(
            f"{self.name} | {self.hersteller} | "
            f"{self.speicher_gb} GB | {self.anschluss} | "
            f"{self.leistungsklasse} | {self.preis:.2f} €"
        )


# =========================
# Objekte (erste 5 Karten)
# =========================
grafikkarte1 = Grafikkarte(1, "RTX 3060", "NVIDIA", 329.99, 12, "PCIe 4.0", "Mittelklasse")
grafikkarte2 = Grafikkarte(2, "RTX 3070", "NVIDIA", 499.99, 8, "PCIe 4.0", "Oberklasse")
grafikkarte3 = Grafikkarte(3, "RX 6700 XT", "AMD", 379.99, 12, "PCIe 4.0", "Mittelklasse")
grafikkarte4 = Grafikkarte(4, "RX 6800", "AMD", 549.99, 16, "PCIe 4.0", "Oberklasse")
grafikkarte5 = Grafikkarte(5, "RTX 3080", "NVIDIA", 699.99, 10, "PCIe 4.0", "High-End")

# =========================
# Warenkorb (Liste)
# =========================
warenkorb = []

warenkorb.append(grafikkarte1)
warenkorb.append(grafikkarte2)
warenkorb.append(grafikkarte3)
warenkorb.append(grafikkarte4)
warenkorb.append(grafikkarte5)

# Beispiel: eine Grafikkarte entfernen
warenkorb.remove(grafikkarte3)

# =========================
# Rabatt & Berechnung
# =========================
lieferkosten = 6.95
gesamtpreis = 0

print("Warenkorb:")
print("--------------------------------------------------")

for index, artikel in enumerate(warenkorb):
    if index == 0:
        preis_mit_rabatt = artikel.preis * 0.9  # 10 % Rabatt
        print(f"{artikel.name}: {preis_mit_rabatt:.2f} € (10% Rabatt)")
        gesamtpreis += preis_mit_rabatt
    else:
        print(f"{artikel.name}: {artikel.preis:.2f} € (kein Rabatt)")
        gesamtpreis += artikel.preis

# =========================
# Gesamtpreis
# =========================
gesamtpreis += lieferkosten

print("--------------------------------------------------")
print(f"Lieferkosten: {lieferkosten:.2f} €")
print(f"Zu zahlender Gesamtpreis: {gesamtpreis:.2f} €")