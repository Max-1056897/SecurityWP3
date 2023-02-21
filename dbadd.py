import sqlite3

# maak een nieuwe database met de naam aanwezigheidssysteem.db
conn = sqlite3.connect('aanwezigheidssysteem.db')

# maak een cursor-object waarmee we SQL-queries kunnen uitvoeren
c = conn.cursor()

# maak een tabel voor de leerlingen
c.execute('''CREATE TABLE IF NOT EXISTS leerlingen
             (leerling_id INTEGER PRIMARY KEY AUTOINCREMENT,
              naam TEXT NOT NULL,
              gebruikersnaam TEXT NOT NULL,
              wachtwoord TEXT NOT NULL,
              rooster TEXT NOT NULL)''')

# maak een tabel voor de docenten
c.execute('''CREATE TABLE IF NOT EXISTS docenten
             (docent_id INTEGER PRIMARY KEY AUTOINCREMENT,
              naam TEXT NOT NULL,
              gebruikersnaam TEXT NOT NULL,
              wachtwoord TEXT NOT NULL)''')

# maak een tabel voor de lessen
c.execute('''CREATE TABLE IF NOT EXISTS lessen
             (les_id INTEGER PRIMARY KEY AUTOINCREMENT,
              vak TEXT NOT NULL,
              datum TEXT NOT NULL,
              starttijd TEXT NOT NULL,
              eindtijd TEXT NOT NULL,
              docent_id INTEGER NOT NULL,
              FOREIGN KEY (docent_id) REFERENCES docenten(docent_id))''')

# maak een tabel voor de aanwezigheid van leerlingen per les
c.execute('''CREATE TABLE IF NOT EXISTS aanwezigheid
             (aanwezigheid_id INTEGER PRIMARY KEY AUTOINCREMENT,
              leerling_id INTEGER NOT NULL,
              les_id INTEGER NOT NULL,
              aanwezig INTEGER NOT NULL,
              reden TEXT,
              FOREIGN KEY (leerling_id) REFERENCES leerlingen(leerling_id),
              FOREIGN KEY (les_id) REFERENCES lessen(les_id))''')

# sla de veranderingen op en sluit de database connectie
conn.commit()
conn.close()
