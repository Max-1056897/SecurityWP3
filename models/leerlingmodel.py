import sqlite3


class LeerlingModel:
<<<<<<< HEAD
    def alle_lessen(self):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('SELECT * FROM lessen')
        lessen = c.fetchall()
        conn.close()
        return lessen


    def leerling_aanwezigheid_toevoegen(self, code, leerling_id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("SELECT * FROM lessen WHERE code=?", (code,))
        vak = c.fetchone()
        if vak is None:
            conn.close()
            return False
        else:
            les_id = vak[0] # haal de les_id op uit de database
            c.execute("INSERT INTO aanwezigheid (aanwezigheid_id, leerling_id, les_id, aanwezig, reden) VALUES (?, ?, ?, ?, ?)", (None, leerling_id, les_id, True, ''))
            conn.commit()
            conn.close()
            return True
    

    def alle_leerlingen(self):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM leerlingen")
        rows = cur.fetchall()
        leerlingen = []
        for row in rows:
            leerlingen.append(dict(row))
        conn.close()
        return leerlingen

    def toevoegen_aanwezigheid(self, leerling_id, les_id, aanwezigheid, reden_afwezigheid):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        for i in range(len(aanwezigheid)):
            c.execute('INSERT INTO aanwezigheid (leerling_id, les_id, aanwezig, reden) VALUES (?, ?, ?, ?)',
                    (leerling_id, les_id[i], aanwezigheid[i], reden_afwezigheid[i]))
        conn.commit()
        conn.close()

=======
    def leerling_aanwezigheid(self):
        conn =- 1
    
>>>>>>> origin/David
