import sqlite3
import random


class LessenModel:
    def lessen_overzicht(self, id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()

        c.execute("SELECT vak FROM lessen WHERE les_id=?", (id,))
        vak = c.fetchone()

        # Haal de lesgegevens op
        c.execute("SELECT * FROM lessen WHERE les_id=?", (id,))
        les = c.fetchone()

        if les:
            # De les is gevonden, haal de aanwezigheidsgegevens op voor deze les
            c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE aanwezigheid.les_id=?", (id,))
            aanwezigheden = c.fetchall()
            c.execute("SELECT COUNT(*) FROM aanwezigheid WHERE les_id=? AND aanwezig=1", (id,))
            count = c.fetchone()[0]

            conn.close()

            # Return de aanwezigheidsgegevens en de lesgegevens
            return (aanwezigheden, les, vak, count)
        else:
            # De les is niet gevonden, return None
            conn.close()
            return None

    def alle_lessen(self):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM lessen")
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(dict(row))
        conn.close()
        return result

    
    def get_all_klassen(self):
            conn = sqlite3.connect('aanwezigheidssysteem.db')
            c = conn.cursor()
            klassen = c.execute("SELECT klas_id, lesnaam FROM klassen").fetchall()
            conn.close()
            return klassen

    def add_lesson(self, vak, datum, starttijd, eindtijd, docent_id, klas_id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id, code) VALUES (?, ?, ?, ?, ?, ?)",
                (vak, datum, starttijd, eindtijd, docent_id, klas_id))
        conn.commit()
        conn.close()

    def lessen_toevoegen(self, vak, datum, starttijd, eindtijd, docent_id):
        import sqlite3
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)',(vak, datum, starttijd, eindtijd, docent_id))
        conn.commit()
        conn.close()
        import sqlite3

    def get_les(self, les_id):
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()

        # Haal de lesgegevens op
        c.execute("SELECT * FROM lessen WHERE les_id=?", (les_id,))
        les = c.fetchone()

        if les:
            # De les is gevonden, haal de aanwezigheidsgegevens op voor deze les
            c.execute("SELECT leerlingen.naam FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE aanwezigheid.les_id=?", (les_id,))
            aanwezigheid_naam = c.fetchall()
            c.execute("SELECT aanwezigheid.aanwezig FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE aanwezigheid.les_id=?", (les_id,))
            aanwezigheid_aanwezig = c.fetchall()
            
            # Sluit de databaseverbinding en geef de aanwezigheidsgegevens en de lesgegevens terug
            conn.close()
            return {'aanwezigheid_naam': aanwezigheid_naam, 'aanwezigheid_aanwezig': aanwezigheid_aanwezig, 'les': les}
        else:
            # De les is niet gevonden, geef een foutmelding en sluit de databaseverbinding
            conn.close()
            return {'error': 'Les niet gevonden'}
        
    def code_update(self, vak):
        code = random.randint(1000, 9999)
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("UPDATE lessen SET code=? WHERE vak=?", (code, vak))
        conn.commit()
        conn.close()
