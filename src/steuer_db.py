import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect("steuer.db")
c = conn.cursor()

# Tabellen Einnahmen
#
#
# Tabellen mit Python und SQL anlegen
#Tabelle Kapitalerträge
c.execute('''
    CREATE TABLE IF NOT EXISTS tbl_ek_ke (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datum Date NOT NULL,
        betrag REAL NOT NULL,
        bemerkung Text
    )
''')


#Tabelle einkuenfte aus Selbststaendigkeit
c.execute('''
    CREATE TABLE IF NOT EXISTS tbl_ek_selbstst (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datum Date NOT NULL,
        betrag REAL NOT NULL,
        bemerkung Text
    )
''')


#Tabellen zu Ausgaben Tabellen mit Python und SQL anlegen
# Tabelle zur Abgeltungssteuer
c.execute('''
    CREATE TABLE IF NOT EXISTS tbl_ag_abgeltst(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datum Date NOT NULL,
        betrag REAL NOT NULL,
        bemerkung Text
        
        
    )
''')


# Tabelle zur Versicherung
c.execute('''
    CREATE TABLE IF NOT EXISTS tbl_ag_vers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datum Date NOT NULL,
        betrag REAL NOT NULL,
        bemerkung Text
    )
''')



# Tabelle zur Buero
c.execute('''
    CREATE TABLE IF NOT EXISTS tbl_ag_buero(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datum Date NOT NULL,
        betrag REAL NOT NULL,
        bemerkung Text
    )
''')


# Tabelle zur Porto
c.execute('''
    CREATE TABLE IF NOT EXISTS tbl_ag_porto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datum Date NOT NULL,
        betrag REAL NOT NULL,
        bemerkung Text
    )
''')





conn.commit()
conn.close()

