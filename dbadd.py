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
#               code INTEGER DEFAULT 0,
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


# # import sqlite3

# # conn = sqlite3.connect('aanwezigheidssysteem.db')

# # c = conn.cursor()

# # c.execute('''CREATE TABLE IF NOT EXISTS leerlingen
# #              (leerling_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #               naam TEXT NOT NULL,
# #               gebruikersnaam TEXT NOT NULL,
# #               wachtwoord TEXT NOT NULL,
# #               rooster TEXT NOT NULL)''')

# # c.execute('''CREATE TABLE IF NOT EXISTS docenten
# #              (docent_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #               naam TEXT NOT NULL,
# #               gebruikersnaam TEXT NOT NULL,
# #               wachtwoord TEXT NOT NULL)''')

# # c.execute('''CREATE TABLE IF NOT EXISTS lessen
# #              (les_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #               vak TEXT NOT NULL,
# #               datum TEXT NOT NULL,
# #               starttijd TEXT NOT NULL,
# #               eindtijd TEXT NOT NULL,
# #               code INTEGER DEFAULT 0,
# #               docent_id INTEGER NOT NULL,
# #               FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# # c.execute('''CREATE TABLE IF NOT EXISTS aanwezigheid
# #              (aanwezigheid_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #               leerling_id INTEGER NOT NULL,
# #               les_id INTEGER NOT NULL,
# #               aanwezig INTEGER NOT NULL,
# #               reden TEXT,
# #               FOREIGN KEY (leerling_id) REFERENCES leerlingen(leerling_id),
# #               FOREIGN KEY (les_id) REFERENCES lessen(les_id),
# #               FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# # conn.commit()
# # conn.close()
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
#               code INTEGER DEFAULT 0,
#               docent_id INTEGER NOT NULL,
#               FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# c.execute('''CREATE TABLE IF NOT EXISTS aanwezigheid
#              (aanwezigheid_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               leerling_id INTEGER NOT NULL,
#               les_id INTEGER NOT NULL,
#               aanwezig INTEGER NOT NULL,
#               reden TEXT,
#               FOREIGN KEY (leerling_id) REFERENCES leerlingen(leerling_id),
#               FOREIGN KEY (les_id) REFERENCES lessen(les_id),
#               FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# conn.commit()
# conn.close()
import sqlite3

conn = sqlite3.connect('aanwezigheidssysteem.db')
c = conn.cursor()

# # Voeg de leerlingen toe
c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES ('David', 'david', 'david', 'Klas 1A')")
c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES ('Max', 'max', 'max', 'Klas 2B')")

# # Voeg de docenten toe
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Docent 1', 'admin', 'admin')")
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Docent 2', 'admin', 'admin')")

# # Voeg de admin-account toe
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Admin', 'admin', 'admin')")

conn.commit()
conn.close()

# import sqlite3

# # Maak een verbinding met de database
# conn = sqlite3.connect('aanwezigheidssysteem.db')

# # Definieer een cursor-object
# cursor = conn.cursor()

# # Voer de SQL-query uit om een nieuwe kolom "code" toe te voegen aan de tabel "lessen"
# cursor.execute("ALTER TABLE lessen ADD COLUMN code INTEGER;")

# # Bevestig de wijzigingen in de database
# conn.commit()

# # Sluit de verbinding met de database
# conn.close()
