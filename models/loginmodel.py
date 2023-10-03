import sqlite3


class LoginModel:
    def get_docent_login(self, gebruikersnaam, wachtwoord):
            conn = sqlite3.connect('aanwezigheidssysteem.db')
            c = conn.cursor()
            c.execute("SELECT * FROM docenten WHERE gebruikersnaam = ? AND wachtwoord = ?", (gebruikersnaam, wachtwoord))
            docent = c.fetchone()
            conn.close()
            return docent

    def get_leerling_login(self, gebruikersnaam, wachtwoord):
            conn = sqlite3.connect('aanwezigheidssysteem.db')
            c = conn.cursor()
            c.execute("SELECT * FROM leerlingen WHERE gebruikersnaam = ? AND wachtwoord = ?", (gebruikersnaam, wachtwoord))
            leerling = c.fetchone()
            conn.close()
            return leerling
                
