class KontaktVerwaltung:
    def __init__(self):
        self.kontakte = []

    def kontakt_hinzufuegen(self, name, telefon, email):
        """Fügt einen neuen Kontakt zur Liste hinzu, falls er noch nicht existiert."""
        if any(kontakt['Name'].lower() == name.lower() for kontakt in self.kontakte):
            print(f"Ein Kontakt mit dem Namen '{name}' existiert bereits.")
            return
        kontakt = {'Name': name, 'Telefon': telefon, 'Email': email}
        self.kontakte.append(kontakt)
        print(f"Kontakt {name} hinzugefügt.")

    def kontakte_anzeigen(self):
        """Zeigt alle Kontakte in der Liste an."""
        if not self.kontakte:
            print("Keine Kontakte vorhanden.")
            return
        for kontakt in self.kontakte:
            print(f"Name: {kontakt['Name']}, Telefon: {kontakt['Telefon']}, Email: {kontakt['Email']}")

    def kontakte_suchen(self, name):
        """Sucht nach einem Kontakt anhand des Namens."""
        ergebnisse = [kontakt for kontakt in self.kontakte if name.lower() in kontakt['Name'].lower()]
        if ergebnisse:
            for kontakt in ergebnisse:
                print(f"Name: {kontakt['Name']}, Telefon: {kontakt['Telefon']}, Email: {kontakt['Email']}")
        else:
            print(f"Kein Kontakt mit dem Namen '{name}' gefunden.")

    def kontakt_loeschen(self, name):
        """Löscht einen Kontakt anhand des Namens."""
        initiale_anzahl = len(self.kontakte)
        self.kontakte = [kontakt for kontakt in self.kontakte if kontakt['Name'].lower() != name.lower()]
        if len(self.kontakte) < initiale_anzahl:
            print(f"Kontakt {name} gelöscht.")
        else:
            print(f"Kein Kontakt mit dem Namen '{name}' gefunden.")

    def kontakt_aktualisieren(self, name, neue_telefon=None, neue_email=None):
        """Aktualisiert Telefonnummer oder E-Mail-Adresse eines bestehenden Kontakts."""
        for kontakt in self.kontakte:
            if kontakt['Name'].lower() == name.lower():
                if neue_telefon:
                    kontakt['Telefon'] = neue_telefon
                if neue_email:
                    kontakt['Email'] = neue_email
                print(f"Kontakt {name} aktualisiert.")
                return
        print(f"Kein Kontakt mit dem Namen '{name}' gefunden.")

    def kontakte_sortieren(self, nach='Name'):
        """Sortiert Kontakte nach Name oder Telefonnummer."""
        if nach not in ['Name', 'Telefon']:
            print("Ungültiges Sortierkriterium. Wählen Sie 'Name' oder 'Telefon'.")
            return
        self.kontakte.sort(key=lambda k: k[nach])
        self.kontakte_anzeigen()

# Beispiel für die Nutzung des Programms
if __name__ == "__main__":
    verwaltung = KontaktVerwaltung()
    verwaltung.kontakt_hinzufuegen("Max Mustermann", "123-456-7890", "max@example.com")
    verwaltung.kontakt_hinzufuegen("Erika Mustermann", "987-654-3210", "erika@example.com")
    verwaltung.kontakte_anzeigen()
    verwaltung.kontakte_suchen("Max")
    verwaltung.kontakt_aktualisieren("Max Mustermann", neue_telefon="111-222-3333")
    verwaltung.kontakt_loeschen("Erika Mustermann")
    verwaltung.kontakte_sortieren(nach='Telefon')
