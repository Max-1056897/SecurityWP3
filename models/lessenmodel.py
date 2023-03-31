import sqlite3


class LessenModel:
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
