import sqlite3

class LoginModel:
    def docent_login(self, gebruikersnaam, wachtwoord):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("SELECT * FROM docenten WHERE gebruikersnaam = ? AND wachtwoord = ?", (gebruikersnaam, wachtwoord))
        docent = c.fetchone()
        conn.close()
        return docent
