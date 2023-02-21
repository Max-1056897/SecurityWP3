from flask import Flask, render_template, request, redirect, session
from flask import Flask, render_template, request, redirect, url_for, session

import sqlite3

app = Flask(__name__)
app.secret_key = "geheime-sleutel" # voeg hier je eigen geheime sleutel toe

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

# route voor het inzien van het leerling dashboard
# route voor het dashboard van de leerling

# functie om verbinding te maken met de database
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

# route voor het opslaan van de aanwezigheidsstatus en reden van afwezigheid
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

# Route voor het docenten dashboard
@app.route('/docent_dashboard')
def docent_dashboard():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lessen")
    lessen = c.fetchall()
    conn.close()
    return render_template('docent_dashboard.html', lessen=lessen)

# Route voor het tonen van de aanwezigheid per les
@app.route('/les/<int:id>')
def les_overzicht(id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE les_id=?", (id,))
    aanwezigheden = c.fetchall()
    conn.close()
    return render_template('les.html', aanwezigheden=aanwezigheden, les_id=id)

# Route voor het toevoegen van een les
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


if __name__ == "__main__":
    app.run(debug=True)
