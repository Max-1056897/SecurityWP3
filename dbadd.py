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
#               code INTEGER,
#               FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# c.execute('''CREATE TABLE IF NOT EXISTS aanwezigheid
#              (aanwezigheid_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               leerling_id INTEGER NOT NULL,
#               les_id INTEGER NOT NULL,
#               aanwezig INTEGER NOT NULL,
#               reden TEXT,
#               FOREIGN KEY (leerling_id) REFERENCES leerlingen(leerling_id),
#               FOREIGN KEY (les_id) REFERENCES lessen(les_id))''')

# c.execute('''CREATE TABLE IF NOT EXISTS klassen
#              (klas_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               les_id INTEGER NOT NULL,
#               leerling_id INTEGER NOT NULL,
#               docent_id INTEGER NOT NULL,
#               lesnaam TEXT NOT NULL,
#               FOREIGN KEY (les_id) REFERENCES lessen(les_id),
#               FOREIGN KEY (leerling_id) REFERENCES leerlingen(leerling_id),
#               FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# conn.commit()



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
#               code INTEGER,
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

# # Toevoegen van leerling naam en id aan aanwezigheid tabel
# c.execute('''ALTER TABLE aanwezigheid
#              ADD COLUMN leerling_naam TEXT''')

# c.execute('''ALTER TABLE aanwezigheid
#              ADD COLUMN leerling_id INTEGER''')

# c.execute('''UPDATE aanwezigheid
#              SET leerling_naam = (SELECT naam FROM leerlingen WHERE leerlingen.leerling_id = aanwezigheid.leerling_id),
#                  leerling_id = aanwezigheid.leerling_id''')

# conn.commit()

# conn.close()


# import sqlite3



# conn = sqlite3.connect('aanwezigheidssysteem.db')
# c = conn.cursor()

# # Voeg de leerlingen toe
# c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES ('David', 'david', 'david', 'Klas 1A')")
# c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES ('Max', 'max', 'max', 'Klas 2B')")

# # Voeg de docenten toe
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Docent 1', 'admin', 'admin')")
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Docent 2', 'admin', 'admin')")

# # Voeg de admin-account toe
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Admin', 'admin', 'admin')")

# conn.commit()
# conn.close()

# query = """
# SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden
# FROM aanwezigheid
# INNER JOIN leerlingen ON aanwezigheid.leerling_id = leerlingen.leerling_id
# """

# c.execute(query)
# result = c.fetchall()

# print(result)


# import sqlite3

# # Maak een verbinding met de database
# conn = sqlite3.connect('aanwezigheidssysteem.db')

# # Definieer een cursor-object
# cursor = conn.cursor()

# # Voer de SQL-query uit om een nieuwe kolom "code" toe te voegen aan de tabel "lessen"
# cursor.execute("ALTER TABLE lessen ADD COLUMN code INTEGER;") 

# Bevestig de wijzigingen in de database
# conn.commit()

# # Sluit de verbinding met de database
# conn.close()
# import sqlite3

# conn = sqlite3.connect('aanwezigheidssysteem.db')
# c = conn.cursor()

# # Klas 1
# klad_id = 1
# les_id = 1
# leerling_id = 1
# docent_id = 1
# lesnaam = 'Klas 1'
# c.execute("INSERT INTO klassen (klas_id, les_id, leerling_id, docent_id, lesnaam) VALUES (?, ?, ?, ?, ?, ?)",
#           (klas_id, les_id, leerling_id, docent_id, lesnaam))

# # Klas 2
# les_id = 2
# leerling_id = 2
# docent_id = 2
# lesnaam = 'Klas 2'
# c.execute("INSERT INTO klassen (les_id, leerling_id, docent_id, lesnaam) VALUES (?, ?, ?, ?)",
#           (les_id, leerling_id, docent_id, lesnaam))

# # Klas 3
# les_id = 3
# leerling_id = 3
# docent_id = 3
# lesnaam = 'Klas 3'
# c.execute("INSERT INTO klassen (les_id, leerling_id, docent_id, lesnaam) VALUES (?, ?, ?, ?)",
#           (les_id, leerling_id, docent_id, lesnaam))

# conn.commit()
# conn.close()

# import sqlite3

# conn = sqlite3.connect('aanwezigheidssysteem.db')
# c = conn.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS admin
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               gebruikersnaam TEXT NOT NULL,
#               wachtwoord TEXT NOT NULL)''')

# conn.commit()
# conn.close()


# import sqlite3

# conn = sqlite3.connect('aanwezigheidssysteem.db')
# c = conn.cursor()

# # Voeg admin account toe
# c.execute("INSERT INTO admin (gebruikersnaam, wachtwoord) VALUES (?, ?)", ('admin', 'admin'))

# # Commit de veranderingen
# conn.commit()

# # Sluit de verbinding
# conn.close()



import sqlite3

conn = sqlite3.connect('aanwezigheidssysteem.db')
c = conn.cursor()

# Gegevens om in te voegen in de tabel klassen
les_id = 1
leerling_id = 1
docent_id = 1
lesnaam = '1A1'

# Een SQL-query om gegevens in de tabel klassen in te voegen
c.execute('''INSERT INTO klassen (les_id, leerling_id, docent_id, lesnaam)
             VALUES (?, ?, ?, ?)''', (les_id, leerling_id, docent_id, lesnaam))

# Gegevens om in te voegen in de tabel klassen
les_id = 2
leerling_id = 2
docent_id = 2
lesnaam = '1A2'

# Een SQL-query om gegevens in de tabel klassen in te voegen
c.execute('''INSERT INTO klassen (les_id, leerling_id, docent_id, lesnaam)
             VALUES (?, ?, ?, ?)''', (les_id, leerling_id, docent_id, lesnaam))

# Gegevens om in te voegen in de tabel klassen
les_id = 3
leerling_id = 3
docent_id = 2
lesnaam = '1A3'

# Een SQL-query om gegevens in de tabel klassen in te voegen
c.execute('''INSERT INTO klassen (les_id, leerling_id, docent_id, lesnaam)
             VALUES (?, ?, ?, ?)''', (les_id, leerling_id, docent_id, lesnaam))

# Gegevens om in te voegen in de tabel klassen
les_id = 4
leerling_id = 4
docent_id = 3
lesnaam = '2A1'

# Een SQL-query om gegevens in de tabel klassen in te voegen
c.execute('''INSERT INTO klassen (les_id, leerling_id, docent_id, lesnaam)
             VALUES (?, ?, ?, ?)''', (les_id, leerling_id, docent_id, lesnaam))

# Commit de wijzigingen in de database
conn.commit()

# Sluit de database connectie
conn.close()
