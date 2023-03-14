from flask import Flask, render_template, request, redirect, session
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)
app.secret_key = "Hogeschool Rotterdam" 
CORS(app)

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
    
@app.route('/leerling_dashboard', methods=["POST", "GET"])
def leerling_dashboard():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM lessen')
    lessen = c.fetchall()
    if request.method == 'POST':
        # Invoer van de student ophalen uit het formulier
        code = request.form['code']

        # Controleren of de code overeenkomt met de code in de database
        c.execute("SELECT * FROM lessen WHERE code=?", (code,))
        vak = c.fetchone()
        if vak is None:
            print('Nee')
        else:
            # Student aanwezigheid in de database opslaan
            leerling_id = session.get('leerling_id')
            les_id = vak[0] # haal de les_id op uit de database
            c.execute("INSERT INTO aanwezigheid (aanwezigheid_id, leerling_id, les_id, aanwezig, reden) VALUES (?, ?, ?, ?, ?)", (None, leerling_id, les_id, True, ''))
            conn.commit()
            return redirect('/leerling_dashboard')
    conn.close()
    return render_template('leerling_dashboard.html', lessen=lessen)


@app.route('/aanwezigheid', methods=['POST'])
def aanwezigheid():
    conn = get_db_connection()
    c = conn.cursor()
    aanwezigheid = request.form.getlist('aanwezigheid')
    reden_afwezigheid = request.form.getlist('reden')
    for i in range(len(aanwezigheid)):
        c.execute('INSERT INTO aanwezigheid (leerling_id, les_id, aanwezig, reden) VALUES (?, ?, ?, ?)',
                  (1, i+1, aanwezigheid[i], reden_afwezigheid[i]))
    conn.commit()
    conn.close()
    return 'Aanwezigheid opgeslagen!'

@app.route('/docent_dashboard', methods=['GET', 'POST'])
def docent_dashboard():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()

    if request.method == 'POST':
        les_id = request.form['les_id']
        aanwezigheid = request.form['aanwezigheid']

        c.execute("UPDATE lessen SET aanwezigheid=? WHERE id=?", (aanwezigheid, les_id))
        conn.commit()

        flash('Aanwezigheidsstatus bijgewerkt!')

    c.execute("SELECT * FROM lessen")
    lessen = c.fetchall()

    conn.close()
    return render_template('docent_dashboard.html', lessen=lessen)

@app.route('/les/<int:id>')
def les_overzicht(id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()

    # Haal de lesgegevens op
    c.execute("SELECT * FROM lessen WHERE les_id=?", (id,))
    les = c.fetchone()

    if les:
        # De les is gevonden, haal de aanwezigheidsgegevens op voor deze les
        c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE aanwezigheid.les_id=?", (id,))
        aanwezigheden = c.fetchall()
        conn.close()

        # Render de template met de aanwezigheidsgegevens en de lesgegevens
        return render_template('les.html', aanwezigheden=aanwezigheden, les=les)
    else:
        # De les is niet gevonden, geef een foutmelding
        conn.close()
        return "Les niet gevonden"



# @app.route('/les/<int:id>')
# def les(id):
#     conn = sqlite3.connect('aanwezigheidssysteem.db')
#     c = conn.cursor()
#     c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE les_id=?", (id,))
#     aanwezigheden = c.fetchall()
#     conn.close()
#     return render_template('les.html', aanwezigheden=aanwezigheden, les_id=id)



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

@app.route('/docent/lessen/overzicht', methods= ["GET", "POST"])
def docent_lessen_overzicht():
    docent_id = 1 
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lessen WHERE docent_id=?", (docent_id,))
    result = c.fetchall()
    conn.close()
    return render_template('docent_lessen.html', lessen=result)

@app.route('/add_les', methods=['POST'])
def add_les():  
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    vak = request.form['vak']
    datum = request.form['datum']
    starttijd = request.form['starttijd']
    eindtijd = request.form['eindtijd']
    docent_id = request.form['docent_id'] 
    c.execute('INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)',
    (vak, datum, starttijd, eindtijd, docent_id))
    conn.commit()
    conn.close()     
    return redirect('/docent/lessen')

## DEZE DOCENT/LESSEN IS VOOR DE LESSEN PAGINA IN DE NAVBAR
@app.route('/docent/lessen', methods=["GET","POST"])
def docent_alle_lessen():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lessen")
    result = c.fetchall()
    conn.close()
    return render_template('docent_overzicht_lessen.html', lessen=result)

@app.route("/docent/lessen.json", methods=["GET", "POST"])
def lessen():

    json_path = os.path.join('lessen.json')


    with open(json_path, 'r') as json_file:
        json_data = json_file.read()

    return jsonify(json_data)




## API ROUTES
@app.route('/API/leerlingen')
def export_leerlingen():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM leerlingen")
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(dict(row))
    return jsonify(result)

@app.route('/API/lessen', methods=["GET", "POST"])
def export_lessen():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM lessen")
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(dict(row))
    return jsonify(result)

@app.route('/API/aanwezigheid')
def export_aanwezigheid():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, aanwezigheid.reden FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id = leerlingen.leerling_id")
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(dict(row))
    return jsonify(result)






@app.route('/docent/lessen/code', methods=['GET', 'POST'])
def docent_lessen_code():
    if request.method == 'POST':
        vak = request.form['vak']
        code = random.randint(1000, 9999)
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("UPDATE lessen SET code=? WHERE vak=?", (code, vak))
        conn.commit()
        c.execute("SELECT code FROM lessen WHERE vak=?", (vak,))
        row = c.fetchone()
        conn.close()
        code = row[0] if row else None
        return redirect(url_for('docent_lessen_code', code=code))

    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT vak FROM lessen")
    vakken = c.fetchall()
    conn.close()

    code = request.args.get('code')

    return render_template('docent_lessen_code.html', vakken=vakken, code=code)


if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)