import sqlite3

conn = sqlite3.connect('aanwezigheidssysteem.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS leerlingen
             (leerling_id INTEGER PRIMARY KEY AUTOINCREMENT,
              naam TEXT NOT NULL,
              gebruikersnaam TEXT NOT NULL,
              wachtwoord TEXT NOT NULL,
              rooster TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS docenten
             (docent_id INTEGER PRIMARY KEY AUTOINCREMENT,
              naam TEXT NOT NULL,
              gebruikersnaam TEXT NOT NULL,
              wachtwoord TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS lessen
             (les_id INTEGER PRIMARY KEY AUTOINCREMENT,
              vak TEXT NOT NULL,
              datum TEXT NOT NULL,
              starttijd TEXT NOT NULL,
              eindtijd TEXT NOT NULL,
              docent_id INTEGER NOT NULL,
              code INTEGER,
              FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS aanwezigheid
             (aanwezigheid_id INTEGER PRIMARY KEY AUTOINCREMENT,
              leerling_id INTEGER NOT NULL,
              les_id INTEGER NOT NULL,
              aanwezig INTEGER NOT NULL,
              reden TEXT,
              FOREIGN KEY (leerling_id) REFERENCES leerlingen(leerling_id),
              FOREIGN KEY (les_id) REFERENCES lessen(les_id))''')

conn.commit()

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


import sqlite3

conn = sqlite3.connect('aanwezigheidssysteem.db')
c = conn.cursor()

# Voeg de leerlingen toe
# c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES ('David', 'david', 'david', 'Klas 1A')")
# c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES ('Max', 'max', 'max', 'Klas 2B')")

# # Voeg de docenten toe
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Docent 1', 'admin', 'admin')")
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Docent 2', 'admin', 'admin')")

# # Voeg de admin-account toe
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES ('Admin', 'admin', 'admin')")

# conn.commit()
# conn.close()

query = """
SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden
FROM aanwezigheid
INNER JOIN leerlingen ON aanwezigheid.leerling_id = leerlingen.leerling_id
"""

c.execute(query)
result = c.fetchall()
print(result)


# import sqlite3

# # Maak een verbinding met de database
# conn = sqlite3.connect('aanwezigheidssysteem.db')

# # Definieer een cursor-object
# cursor = conn.cursor()

# # Voer de SQL-query uit om een nieuwe kolom "code" toe te voegen aan de tabel "lessen"
# cursor.execute("ALTER TABLE lessen ADD COLUMN code INTEGER;") 

# Bevestig de wijzigingen in de database
conn.commit()

# Sluit de verbinding met de database
conn.close()
