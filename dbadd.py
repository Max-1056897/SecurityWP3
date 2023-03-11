# import sqlite3

# conn = sqlite3.connect('aanwezigheidssysteem.db')

# c = conn.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS leerlingen
#              (leerling_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               naam TEXT NOT NULL,
#               gebruikersnaam TEXT NOT NULL,
#               wachtwoord TEXT NOT NULL,
#               rooster TEXT NOT NULL)''')

# c.execute('''CREATE TABLE IF NOT EXISTS docenten
#              (docent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               naam TEXT NOT NULL,
#               gebruikersnaam TEXT NOT NULL,
#               wachtwoord TEXT NOT NULL)''')

# c.execute('''CREATE TABLE IF NOT EXISTS lessen
#              (les_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               vak TEXT NOT NULL,
#               datum TEXT NOT NULL,
#               starttijd TEXT NOT NULL,
#               eindtijd TEXT NOT NULL,
#               docent_id INTEGER NOT NULL,
#               FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# c.execute('''CREATE TABLE IF NOT EXISTS aanwezigheid
#              (aanwezigheid_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               leerling_id INTEGER NOT NULL,
#               les_id INTEGER NOT NULL,
#               aanwezig INTEGER NOT NULL,
#               reden TEXT,
#               FOREIGN KEY (leerling_id) REFERENCES leerlingen(leerling_id),
#               FOREIGN KEY (les_id) REFERENCES lessen(les_id))''')

# conn.commit()
# conn.close()
# import sqlite3

# conn = sqlite3.connect('aanwezigheidssysteem.db')
# c = conn.cursor()

# c.execute("DELETE FROM lessen")

# conn.commit()
# conn.close()
