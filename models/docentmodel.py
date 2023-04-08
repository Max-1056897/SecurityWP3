import sqlite3

class DocentModel:
    def get_docent_login(self, gebruikersnaam, wachtwoord):
        conn = sqlite3.connect("aanwezigheidssysteem.db")
        c = conn.cursor()
        c.execute("SELECT * FROM docenten WHERE gebruikersnaam = ? AND wachtwoord = ?", (gebruikersnaam, wachtwoord))
        docent = c.fetchone()
        conn.close()
        return docent
    
    def get_alle_lessen(self):
          conn = sqlite3.connect('aanwezigheidssysteem.db')
          c = conn.cursor()
          c.execute("SELECT * FROM lessen")
          lessen = c.fetchall()
          return lessen

    def get_leerling_details(self):
         conn = sqlite3.connect('aanwezigheidssysteem.db')
         c = conn.cursor()
         c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, lessen.vak, docenten.naam FROM aanwezigheid INNER JOIN lessen ON aanwezigheid.les_id = lessen.les_id INNER JOIN leerlingen ON aanwezigheid.leerling_id = leerlingen.leerling_id INNER JOIN docenten ON lessen.docent_id = docenten.docent_id")
         rows = c.fetchall()
         conn.close()
         return rows
    
    def get_docent_lessen_overzicht(self, docent_id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("SELECT * FROM lessen WHERE docent_id=?", (docent_id,))
        result = c.fetchall()
        conn.close()
        return result