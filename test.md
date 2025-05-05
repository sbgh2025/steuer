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
