import sqlite3

class AdminModel:
    def get_alle_leerlingen(self):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("SELECT * FROM leerlingen")
        leerlingen = c.fetchall()
        conn.close
        return leerlingen
    
    def get_alle_docenten(self):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("SELECT * FROM docenten")
        docenten = c.fetchall()
        conn.close()
        return docenten
    
    def update_leerling(self, naam, gebruikersnaam, wachtwoord, rooster, leerling_id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('UPDATE leerlingen SET naam = ?, gebruikersnaam = ?, wachtwoord = ?, rooster = ? WHERE leerling_id = ?', (naam, gebruikersnaam, wachtwoord, rooster, leerling_id))
        conn.commit()
        conn.close()
        return naam, gebruikersnaam, wachtwoord, rooster, leerling_id
    
    
    def get_docent_id(self, docent_id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('SELECT * FROM docenten WHERE docent_id = ?', (docent_id,))
        docent = c.fetchone()
        return docent

    def update_docent(self,naam, gebruikersnaam, wachtwoord, docent_id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('UPDATE docenten SET naam = ?, gebruikersnaam = ?, wachtwoord = ? WHERE docent_id = ?', (naam, gebruikersnaam, wachtwoord, docent_id))
        conn.commit()
        conn.close()
        return naam, gebruikersnaam, wachtwoord, docent_id

    def leerling_add(self,naam, gebruikersnaam, wachtwoord, rooster):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES (?, ?, ?, ?)', (naam, gebruikersnaam, wachtwoord, rooster))
        conn.commit()
        conn.close()
        return naam, gebruikersnaam, wachtwoord, rooster

    def docent_add(self,naam, gebruikersnaam, wachtwoord):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)', (naam, gebruikersnaam, wachtwoord))
        conn.commit()
        conn.close()
        return naam, gebruikersnaam, wachtwoord