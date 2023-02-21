from flask import Flask, render_template, request, redirect, session
from flask import Flask, render_template, request, redirect, url_for, session

import sqlite3

app = Flask(__name__)
app.secret_key = "Hogeschool Rotterdam" 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login_leerling", methods=["POST"])
def login_leerling():
    gebruikersnaam = request.form["gebruikersnaam"]
    wachtwoord = request.form["wachtwoord"]
    conn = sqlite3.connect("aanwezigheidssysteem.db")
    c = conn.cursor()
    c.execute("SELECT * FROM leerlingen WHERE gebruikersnaam = ? AND wachtwoord = ?", (gebruikersnaam, wachtwoord))
    leerling = c.fetchone()
    conn.close()

    if leerling:
        session["gebruikersnaam"] = leerling[2]
        session["leerling_id"] = leerling[0]
        return redirect("/leerling_dashboard")
    else:
        return render_template("index.html", error="Ongeldige gebruikersnaam of wachtwoord")

@app.route("/login_docent", methods=["POST"])
def login_docent():
    gebruikersnaam = request.form["gebruikersnaam"]
    wachtwoord = request.form["wachtwoord"]
    conn = sqlite3.connect("aanwezigheidssysteem.db")
    c = conn.cursor()
    c.execute("SELECT * FROM docenten WHERE gebruikersnaam = ? AND wachtwoord = ?", (gebruikersnaam, wachtwoord))
    docent = c.fetchone()
    conn.close()

    if docent:
        session["gebruikersnaam"] = docent[2]
        session["docent_id"] = docent[0]
        return redirect("/docent_dashboard")
    else:
        return render_template("index.html", error="Ongeldige gebruikersnaam of wachtwoord")


def get_db_connection():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    conn.row_factory = sqlite3.Row
    return conn
    
@app.route('/leerling_dashboard')
def leerling_dashboard():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM lessen')
    lessen = c.fetchall()
    conn.close()
    return render_template('leerling_dashboard.html', lessen=lessen)

@app.route('/aanwezigheid', methods=['POST'])
def aanwezigheid():
    conn = get_db_connection()
    c = conn.cursor()
    aanwezigheid = request.form.getlist('aanwezigheid')
    reden_afwezigheid = request.form.getlist('reden_afwezigheid')
    for i in range(len(aanwezigheid)):
        c.execute('INSERT INTO aanwezigheid (leerling_id, les_id, aanwezig, reden) VALUES (?, ?, ?, ?)',
                  (1, i+1, aanwezigheid[i], reden_afwezigheid[i]))
    conn.commit()
    conn.close()
    return 'Aanwezigheid opgeslagen!'

@app.route('/docent_dashboard')
def docent_dashboard():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lessen")
    lessen = c.fetchall()
    conn.close()
    return render_template('docent_dashboard.html', lessen=lessen)

@app.route('/les/<int:id>')
def les_overzicht(id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE les_id=?", (id,))
    aanwezigheden = c.fetchall()
    conn.close()
    return render_template('les.html', aanwezigheden=aanwezigheden, les_id=id)

@app.route('/toevoegen_les', methods=['POST'])
def toevoegen_les():
    vak = request.form['vak']
    datum = request.form['datum']
    starttijd = request.form['starttijd']
    eindtijd = request.form['eindtijd']
    docent_id = request.form['docent']
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", (vak, datum, starttijd, eindtijd, docent_id))
    conn.commit()
    conn.close()
    return redirect(url_for('docent_dashboard'))

@app.route('/les/<int:id>')
def les(id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE les_id=?", (id,))
    aanwezigheden = c.fetchall()
    conn.close()
    return render_template('les.html', aanwezigheden=aanwezigheden, les_id=id)



## DIT IS ALLEMAAL VOOR DE TOEVOEGEN LES PAGINA
@app.route('/docent/lessen/toevoegen')
def docent_lessen_toevoegen():
    return render_template('docent_lessen.html')

@app.route('/docent/lessen/toevoegen', methods=['POST'])
def docent_lessen_toevoegen_post():
    vak = request.form['vak']
    datum = request.form['datum']
    starttijd = request.form['starttijd']
    eindtijd = request.form['eindtijd']
    docent_id = request.form['docent_id']
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", (vak, datum, starttijd, eindtijd, docent_id))
    conn.commit()
    conn.close()
    return redirect(url_for('docent_lessen_overzicht'))

@app.route('/docent/lessen/overzicht')
def docent_lessen_overzicht():
    docent_id = 1 
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lessen WHERE docent_id=?", (docent_id,))
    result = c.fetchall()
    conn.close()
    return render_template('docent_lessen_overzicht.html', lessen=result)


## DEZE DOCENT/LESSEN IS VOOR DE LESSEN PAGINA IN DE NAVBAR
@app.route('/docent/lessen')
def docent_alle_lessen():
    docent_id = 1  # Vervang dit door de daadwerkelijke docent_id (bijvoorbeeld opgehaald uit de sessie)
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lessen WHERE docent_id=?", (docent_id,))
    result = c.fetchall()
    conn.close()
    return render_template('docent_overzicht_lessen.html', lessen=result)


if __name__ == "__main__":
    app.run(debug=True)
