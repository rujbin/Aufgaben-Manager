# Kontaktverwaltungssystem in Python

# Initialisierung der Kontaktliste
kontakte = []

def kontakt_hinzufuegen(name, telefon, email):
    """Fügt einen neuen Kontakt zur Liste hinzu."""
    kontakt = {'Name': name, 'Telefon': telefon, 'Email': email}
    kontakte.append(kontakt)
    print(f"Kontakt {name} hinzugefügt.")

def kontakte_anzeigen():
    """Zeigt alle Kontakte in der Liste an."""
    if not kontakte:
        print("Keine Kontakte vorhanden.")
        return
    for kontakt in kontakte:
        print(f"Name: {kontakt['Name']}, Telefon: {kontakt['Telefon']}, Email: {kontakt['Email']}")

def kontakte_suchen(name):
    """Sucht nach einem Kontakt anhand des Namens."""
    ergebnisse = set()
    for kontakt in kontakte:
        if name.lower() in kontakt['Name'].lower():
            ergebnisse.add(f"Name: {kontakt['Name']}, Telefon: {kontakt['Telefon']}, Email: {kontakt['Email']}")
    if ergebnisse:
        for ergebnis in ergebnisse:
            print(ergebnis)
    else:
        print(f"Kein Kontakt mit dem Namen '{name}' gefunden.")

def kontakt_loeschen(name):
    """Löscht einen Kontakt anhand des Namens."""
    global kontakte
    kontakte = [kontakt for kontakt in kontakte if kontakt['Name'].lower() != name.lower()]
    print(f"Kontakt {name} gelöscht.")

def kontakt_aktualisieren(name, neue_telefon=None, neue_email=None):
    """Aktualisiert Telefonnummer oder E-Mail-Adresse eines bestehenden Kontakts."""
    kontakt_geupdated = False
    for kontakt in kontakte:
        if kontakt['Name'].lower() == name.lower():
            if neue_telefon:
                kontakt['Telefon'] = neue_telefon
            if neue_email:
                kontakt['Email'] = neue_email
            kontakt_geupdated = True
            print(f"Kontakt {name} aktualisiert.")
            break
    if not kontakt_geupdated:
        print(f"Kein Kontakt mit dem Namen '{name}' gefunden.")

def kontakte_sortieren(nach='Name'):
    """Sortiert Kontakte nach Name oder Telefonnummer."""
    if nach not in ['Name', 'Telefon']:
        print("Ungültiges Sortierkriterium. Wählen Sie 'Name' oder 'Telefon'.")
        return

    sortierte_kontakte = sorted(kontakte, key=lambda k: k[nach])
    kontakte_anzeigen(sortierte_kontakte)

def kontakte_anzeigen(kontakte_liste):
    """Zeigt eine Liste von Kontakten an."""
    if not kontakte_liste:
        print("Keine Kontakte vorhanden.")
        return
    for kontakt in kontakte_liste:
        print(f"Name: {kontakt['Name']}, Telefon: {kontakt['Telefon']}, Email: {kontakt['Email']}")

# Beispiel für die Nutzung des Programms
if __name__ == "__main__":
    kontakt_hinzufuegen("Max Mustermann", "123-456-7890", "max@example.com")
    kontakt_hinzufuegen("Erika Mustermann", "987-654-3210", "erika@example.com")
    kontakt_anzeigen()
    kontakte_suchen("Max")
    kontakt_aktualisieren("Max Mustermann", neue_telefon="111-222-3333")
    kontakt_loeschen("Erika Mustermann")
    kontakte_sortieren(nach='Telefon')
