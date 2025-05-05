  
# SteuerTool – Einnahmen-Überschuss-Auswertung aus CSV-Kontoauszügen

Ein Python-Tool zur automatisierten Auswertung von Kontoauszügen (CSV) mit Einnahmen-Überschuss-Rechnung und Steuerberechnung auf Dividenden und Kapitalerträge. Besonders geeignet für Selbstständige und Privatanleger.

## Funktionen

- Automatisches Einlesen und Verarbeiten von Kontoauszügen im **CSV-Format**
- Übersichtliche **Einnahmen-Überschuss-Auswertung**
- **Steuerberechnung** auf Kapitalerträge (z. B. Dividenden, Zinsen)
- Speicherung der Daten in einer lokalen **SQLite-Datenbank**
- **Export** als formatierte Excel-Datei (**XLSX**)
- Benutzerfreundliche grafische Oberfläche mit **Tkinter**

## Voraussetzungen

- Python **3.9** oder höher

- Die folgenden Python-Pakete (siehe `requirements.txt`):

```bash
pip install -r requirements.txt
````

Inhalt von `requirements.txt`:

* `openpyxl>=3.1.2`
* `pandas>=2.2.0`
* `matplotlib>=3.8.0`
* `tkintertable>=1.3.5`

### Hinweise:

* **openpyxl** wird für den **Excel-Export** benötigt.
* **pandas** ist hilfreich für das Einlesen und Auswerten der CSV-Dateien.
* **matplotlib** kannst du verwenden, falls du Diagramme für die Auswertung erstellen willst (**optional**).
* **tkintertable** ist ein Add-on für tkinter, das Tabellenansichten ermöglicht (**optional**, je nach GUI-Umfang).

### Nicht nötig in `requirements.txt`:

* **tkinter** und **sqlite3** sind Teil der **Python-Standardbibliothek** und müssen nicht aufgeführt werden.

## Starten der Anwendung

Um das Tool zu starten, führe folgenden Befehl aus:

```bash
python steuer_index.py
```

---

## Kategorie Zuordnung (`kategorie_mapping`)

Das Programm verwendet ein `kategorie_mapping`in der Datei steuer_csv.py, um verschiedene Buchungen aus einer CSV-Datei in die entsprechenden Kategorien zuzuordnen. Das Mapping besteht aus einer Sammlung von **Schlagwörtern** und den dazugehörigen **Kategorien**. Wenn eines der Schlagwörter im Buchungstext gefunden wird, wird die zugehörige Kategorie zugewiesen.

### Beispiel für das `kategorie_mapping`:

```python
kategorie_mapping = {
    "Porto": ["post", "dhl"],
    "Versicherung": ["signal iduna", "allianz", "versicherung"],
    "Buero": ["telekom", "aral"],
    "Kapitalertraege": ["kapitalertrag", "dividende", "zins"],
    "Selbststaendigkeit": ["freelance", "kunde", "freiberuflich"],
    "Abgeltungssteuer": ["finanzamt"]
}
```

### Anpassung des `kategorie_mapping`

Die Liste der Schlagwörter in den Kategorien kann leicht an die eigenen Bedürfnisse angepasst werden. Zum Beispiel, wenn du weitere Versicherungsunternehmen oder Porto-Dienstleister hinzufügen möchtest, kannst du dies tun:

```python
kategorie_mapping["Versicherung"].append("axa")  # Fügt 'axa' zur Kategorie 'Versicherung' hinzu
kategorie_mapping["Porto"].append("briefporto")  # Fügt 'briefporto' zur Kategorie 'Porto' hinzu
```

### Hinweise

* Achte darauf, dass die Schlagwörter präzise genug sind, um keine falschen Zuordnungen zu verursachen. Ein allgemeiner Begriff wie „versicherung“ könnte auch in anderen Kontexten gefunden werden.
* Das Mapping ist **case-insensitive**, das heißt, es spielt keine Rolle, ob ein Schlagwort in Groß- oder Kleinschreibung vorkommt.

Passe das Mapping an deine eigenen Bedürfnisse an, um sicherzustellen, dass die Kategorisierung der Buchungen korrekt erfolgt.

---

## Mitwirken

Pull Requests und Vorschläge sind herzlich willkommen.
Für größere Änderungen bitte vorher ein **Issue** erstellen.

