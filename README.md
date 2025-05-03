SteuerTool – Einnahmen-Überschuss-Auswertung aus CSV-Kontoauszügen

Ein Python-Tool zur automatisierten Auswertung von Kontoauszügen (CSV) mit Einnahmen-Überschuss-Rechnung und Steuerberechnung auf Dividenden und Kapitalerträge. Besonders geeignet für Selbstständige und Privatanleger.

Funktionen

    Automatisches Einlesen und Verarbeiten von Kontoauszügen im CSV-Format

    Übersichtliche Einnahmen-Überschuss-Auswertung

    Steuerberechnung auf Kapitalerträge (z. B. Dividenden, Zinsen)

    Speicherung der Daten in einer lokalen SQLite-Datenbank

    Export als formatierte Excel-Datei (XLSX)

    Benutzerfreundliche grafische Oberfläche mit Tkinter

Voraussetzungen

    Python 3.9 oder höher
    

    Die folgenden Python-Pakete (siehe requirements.txt):

pip install -r requirements.txt

Inhalt von requirements.txt:

openpyxl>=3.1.2
pandas>=2.2.0
matplotlib>=3.8.0
tkintertable>=1.3.5


Hinweise:

    openpyxl wird für den Excel-Export benötigt.

    pandas ist hilfreich für das Einlesen und Auswerten der CSV-Dateien.

    matplotlib kannst du verwenden, falls du Diagramme für die Auswertung erstellen willst (optional).

    tkintertable ist ein Add-on für tkinter, das Tabellenansichten ermöglicht (optional, je nach GUI-Umfang).

Nicht nötig in requirements.txt:

    tkinter und sqlite3 sind Teil der Python-Standardbibliothek und müssen nicht aufgeführt werden.


    
Starten der Anwendung

python steuer_index.py


Mitwirken

Pull Requests und Vorschläge sind herzlich willkommen.
Für größere Änderungen bitte vorher ein Issue erstellen.


