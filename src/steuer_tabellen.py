import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Verbindung zur SQLite-Datenbank
conn = sqlite3.connect('steuer.db')
c = conn.cursor()

# Funktion zum Laden und Anzeigen der Datensätze aus der jeweiligen Tabelle
def lade_tabelle(tabelle):
    c.execute(f"SELECT * FROM {tabelle}")
    rows = c.fetchall()

    # Löschen des bisherigen Inhalts im Textfeld
    textfeld.delete(1.0, tk.END)

    # Anzeige der Tabelleninhalte im Textfeld
    for row in rows:
        textfeld.insert(tk.END, f"ID: {row[0]}, Datum: {row[1]}, Betrag: {row[2]}, Bemerkung: {row[3]}\n")

# Funktion zum Hinzufügen eines neuen Datensatzes
def datensatz_hinzufuegen():
    tabelle = tabelle_var.get()
    datum = simpledialog.askstring("Datum", "Geben Sie das Datum ein (YYYY-MM-DD):")
    betrag = simpledialog.askfloat("Betrag", "Geben Sie den Betrag ein:")
    bemerkung = simpledialog.askstring("Bemerkung", "Geben Sie eine Bemerkung ein:")

    if datum and betrag is not None:
        try:
            c.execute(f"INSERT INTO {tabelle} (datum, betrag, bemerkung) VALUES (?, ?, ?)", (datum, betrag, bemerkung))
            conn.commit()
            messagebox.showinfo("Erfolg", "Datensatz wurde hinzugefügt.")
            lade_tabelle(tabelle)
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Hinzufügen des Datensatzes: {e}")
    else:
        messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen.")

# Funktion zum Löschen eines Datensatzes
def datensatz_loeschen():
    tabelle = tabelle_var.get()
    try:
        datensatz_id = simpledialog.askinteger("ID zum Löschen", "Geben Sie die ID des Datensatzes ein, den Sie löschen möchten:")
        if datensatz_id is not None:
            c.execute(f"DELETE FROM {tabelle} WHERE id = ?", (datensatz_id,))
            conn.commit()
            messagebox.showinfo("Erfolg", f"Datensatz mit ID {datensatz_id} wurde gelöscht.")
            lade_tabelle(tabelle)
        else:
            messagebox.showerror("Fehler", "Ungültige ID.")
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Löschen des Datensatzes: {e}")


# GUI-Setup
# GUI-Setup
root = tk.Tk()
root.title("Steuerverwaltung")

# Haupt-Layout: Zwei Spalten
# Linker Frame für Auswahl und Textfeld
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Rechter Frame für die Buttons
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Auswahl der Tabelle
tk.Label(left_frame, text="Tabelle auswählen:").pack(anchor="w", pady=5)
tabelle_var = tk.StringVar(value="tbl_ek_ke")
tabelle_auswahl = tk.OptionMenu(left_frame, tabelle_var, "tbl_ek_ke", "tbl_ek_selbstst", "tbl_ag_abgeltst", "tbl_ag_vers", "tbl_ag_buero", "tbl_ag_porto")
tabelle_auswahl.pack(anchor="w", pady=5)

# Textfeld für die Anzeige der Datensätze
textfeld = tk.Text(left_frame, height=20, width=80)
textfeld.pack(pady=5)

# Buttons im rechten Frame zentriert und gleich breit
button_width = 25
tk.Button(right_frame, text="Datensatz anzeigen", width=button_width, command=lambda: lade_tabelle(tabelle_var.get())).pack(pady=5)
tk.Button(right_frame, text="Datensatz hinzufügen", width=button_width, command=datensatz_hinzufuegen).pack(pady=5)
tk.Button(right_frame, text="Datensatz löschen", width=button_width, command=datensatz_loeschen).pack(pady=5)






# Start des Programms
root.mainloop()

conn.close()
