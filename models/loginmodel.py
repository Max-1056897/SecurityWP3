import sqlite3

class LoginModel:
    def login_admin(self):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("SELECT * FROM admin WHERE gebruikersnaam = ? AND wachtwoord = ?", (username, password))
        user = c.fetchone()


    def login_leerling(self):
        conn = sqlite3.connect("aanwezigheidssysteem.db")
        c = conn.cursor()
        c.execute("SELECT * FROM leerlingen WHERE gebruikersnaam = ? AND wachtwoord = ?", (gebruikersnaam, wachtwoord))
        leerling = c.fetchone()
        conn.close()