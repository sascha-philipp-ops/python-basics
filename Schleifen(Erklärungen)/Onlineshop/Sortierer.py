import os
import shutil
from pathlib import Path

# Definiere den Ordner, der aufgeräumt werden soll
ZIEL_ORDNER = Path.home() / "Downloads"

# Zuordnungen von Ordnernamen zu Dateiendungen
ORDNER_STRUKTUR = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Dokumente": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".csv"],
    "Archive": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Programme": [".exe", ".msi", ".dmg", ".sh"],
    "Audio_Video": [".mp3", ".wav", ".mp4", ".mkv", ".mov"]
}

def ordner_aufräumen():
    if not ZIEL_ORDNER.exists():
        print(f"Ordner {ZIEL_ORDNER} existiert nicht.")
        return

    print(f"Starte Sortierung in: {ZIEL_ORDNER}")
    dateien_verschoben = 0

    # Scanne alle Dateien im Zielordner
    for eintrag in ZIEL_ORDNER.iterdir():
        # Ignoriere Unterordner, betrachte nur Dateien
        if eintrag.is_file():
            endung = eintrag.suffix.lower()
            
            # Suche den passenden Ziel-Unterordner
            for ordner_name, endungen in ORDNER_STRUKTUR.items():
                if endung in endungen:
                    neuer_ordner = ZIEL_ORDNER / ordner_name
                    
                    # Erstelle den Unterordner, falls er noch nicht existiert
                    neuer_ordner.mkdir(exist_ok=True)
                    
                    # Verschiebe die Datei
                    ziel_pfad = neuer_ordner / eintrag.name
                    
                    # Verhindert Überschreiben, falls Datei schon existiert
                    if not ziel_pfad.exists():
                        shutil.move(str(eintrag), str(ziel_pfad))
                        print(f"Verschoben: {eintrag.name} -> {ordner_name}/")
                        dateien_verschoben += 1
                    break
                    
    print(f"Fertig! {dateien_verschoben} Dateien erfolgreich sortiert.")

if __name__ == "__main__":
    ordner_aufräumen()