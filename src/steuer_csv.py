import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import sqlite3
import openpyxl
from openpyxl.styles import Font

# 🔑 Stichworte zur Kategorisierung
kategorie_mapping = {
    "post": "Porto",
    "dhl": "Porto",
    "signal iduna": "Versicherung",
    "allianz": "Versicherung",
    "versicherung": "Versicherung",
    "telekom": "Buero",
    "aral": "Buero",
    "kapitalertrag": "Kapitalertraege",
    "dividende": "Kapitalertraege",
    "zins": "Kapitalertraege",
    "freelance": "Selbststaendigkeit",
    "kunde": "Selbststaendigkeit",
    "freiberuflich": "Selbststaendigkeit",
    "finanzamt": "Abgeltungssteuer"
}

# 🔍 Kategorie ermitteln anhand Buchungstext
def finde_kategorie(text):
    text = str(text).lower()
    for schlagwort, kategorie in kategorie_mapping.items():
        if schlagwort in text:
            return kategorie
    return "Sonstiges"

# 📥 CSV einlesen & kategorisieren
def lese_kontoauszuege(csv_datei):
    try:
        df = pd.read_csv(csv_datei)

        if not {'Datum', 'Buchungstext', 'Betrag'}.issubset(df.columns):
            raise ValueError("CSV muss die Spalten: Datum, Buchungstext, Betrag enthalten.")

        df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y', errors='raise')
        df['Datum'] = df['Datum'].dt.strftime('%Y-%m-%d')

        df['Kategorie'] = df['Buchungstext'].apply(finde_kategorie)

        # Datensätze nach Kategorien trennen
        kapitalertraege = df[df['Kategorie'] == 'Kapitalertraege']
        selbststaendigkeit = df[df['Kategorie'] == 'Selbststaendigkeit']
        versicherung = df[df['Kategorie'] == 'Versicherung']
        buero = df[df['Kategorie'] == 'Buero']
        porto = df[df['Kategorie'] == 'Porto']
        abgeltung = df[df['Kategorie'] == 'Abgeltungssteuer']

        return kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung

    except Exception as e:
        messagebox.showerror("Fehler beim Einlesen", str(e))
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

# 💾 Daten in die Datenbank schreiben
def speichere_in_db(kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung):
    try:
        conn = sqlite3.connect('steuer.db')
        c = conn.cursor()

        for _, row in kapitalertraege.iterrows():
            c.execute("INSERT INTO tbl_ek_ke (datum, betrag, bemerkung) VALUES (?, ?, ?)",
                      (row['Datum'], row['Betrag'], row['Buchungstext']))

        for _, row in selbststaendigkeit.iterrows():
            c.execute("INSERT INTO tbl_ek_selbstst (datum, betrag, bemerkung) VALUES (?, ?, ?)",
                      (row['Datum'], row['Betrag'], row['Buchungstext']))

        for _, row in versicherung.iterrows():
            c.execute("INSERT INTO tbl_ag_vers (datum, betrag) VALUES (?, ?)",
                      (row['Datum'], row['Betrag']))

        for _, row in buero.iterrows():
            c.execute("INSERT INTO tbl_ag_buero (datum, betrag) VALUES (?, ?)",
                      (row['Datum'], row['Betrag']))

        for _, row in porto.iterrows():
            c.execute("INSERT INTO tbl_ag_porto (datum, betrag) VALUES (?, ?)",
                      (row['Datum'], row['Betrag']))

        for _, row in abgeltung.iterrows():
            c.execute("INSERT INTO tbl_ag_abgeltst (datum, betrag) VALUES (?, ?)",
                      (row['Datum'], row['Betrag']))

        conn.commit()
        conn.close()
        messagebox.showinfo("Erfolg", "Daten wurden erfolgreich gespeichert.")
    except Exception as e:
        messagebox.showerror("Fehler bei Speicherung", str(e))

# 📤 Excel-Export
def exportiere_nach_excel(kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung):
    try:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Kontoauszüge"

        ws.append(["Kategorie", "Datum", "Betrag (€)", "Buchungstext"])
        for cell in ws[1]:
            cell.font = Font(bold=True)

        def schreibe_daten(df):
            for _, row in df.iterrows():
                ws.append([
                    row.get('Kategorie', ''),
                    row.get('Datum', ''),
                    row.get('Betrag', ''),
                    row.get('Buchungstext', '')
                ])

        for df in [kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung]:
            schreibe_daten(df)

        wb.save("kontoauszuege_einzelbuchungen.xlsx")
        messagebox.showinfo("Excel gespeichert", "Datei wurde erfolgreich erstellt.")
    except Exception as e:
        messagebox.showerror("Fehler beim Excel-Export", str(e))

# 🔘 Hauptfunktion
def lade_csv_und_verarbeite():
    datei_pfad = filedialog.askopenfilename(
        title="CSV-Datei auswählen",
        filetypes=[("CSV-Dateien", "*.csv"), ("Alle Dateien", "*.*")]
    )

    if not datei_pfad:
        return

    kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung = lese_kontoauszuege(datei_pfad)

    if all(df.empty for df in [kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung]):
        messagebox.showinfo("Keine Daten", "Keine passenden Buchungen gefunden.")
        return

    speichere_in_db(kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung)
    exportiere_nach_excel(kapitalertraege, selbststaendigkeit, versicherung, buero, porto, abgeltung)

# 🖼️ GUI
root = tk.Tk()
root.title("Steuer-Import aus Kontoauszug")
root.geometry("400x200")

label = tk.Label(root, text="Kontoauszug (CSV) einlesen & speichern", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="CSV laden & verarbeiten", command=lade_csv_und_verarbeite, height=2)
btn.pack(pady=30)

root.mainloop()
