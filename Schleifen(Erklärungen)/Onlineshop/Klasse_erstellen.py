class Produkt:
    def _init_(self, name, preis, lager):
        self.name = name
        self.preis = preis
        self.lager = lager

    def anzeigen(self):
        # Hier ist der f-String: Alles in einer Zeile, sauber formatiert
        print(f"Modell: {self.name} | Preis: {self.preis}€ | Auf Lager: {self.lager}")

# Instanzen erstellen (ganz links eingerückt)
produkt1 = Produkt("Razor Gaming PC", 1900, True)
produkt2 = Produkt("Alienware Gaming PC", 1499, False)
produkt3 = Produkt("Asus Desktop PC", 599, True)

# Die Methode aufrufen
produkt1.anzeigen()
produkt2.anzeigen()
produkt3.anzeigen()