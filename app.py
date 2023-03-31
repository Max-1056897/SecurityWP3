from flask import Flask, render_template, request, redirect, session
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random
import threading
import time

from models.lessenmodel import LessenModel
from models.loginmodel import LoginModel
from models.leerlingmodel import LeerlingModel

LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)
app.secret_key = "Hogeschool Rotterdam"
CORS(app)

lessen_model = LessenModel()
login_model = LoginModel()
leerling_model = LeerlingModel()


# Login routes
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login_docent", methods=["POST"])
def login_docent():
    gebruikersnaam = request.form["gebruikersnaam"]
    wachtwoord = request.form["wachtwoord"]
    docent = login_model.docent_login(gebruikersnaam, wachtwoord)

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


# @app.route('/login', methods=['GET', 'POST'])
# def login_admin():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         login = login_model.login_admin()
#         if user:
#             session['user'] = user
#             return redirect(url_for('admin'))
#         else:
#             return render_tedocentmplate('login.html', error='Invalid username or password')
#     else:
#         return render_template('login.html', login=login)


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


# Leerling routes 
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


@app.route('/leerling_dashboard', methods=["POST", "GET"])
def leerling_dashboard():
    lessen = leerling_model.alle_lessen()
    if request.method == 'POST':
        # Invoer van de student ophalen uit het formulier
        code = request.form['code']

        # Student aanwezigheid controleren en opslaan in de database
        leerling_id = session.get('leerling_id')
        success = leerling_model.leerling_aanwezigheid_toevoegen(code, leerling_id)
        if success:
            return redirect('/leerling_dashboard')
        else:
            print('Nee')
    return render_template('leerling_dashboard.html', lessen=lessen)


@app.route('/API/leerlingen')
def export_leerlingen():
    leerlingen = leerling_model.alle_leerlingen()
    return jsonify(leerlingen)


@app.route('/aanwezigheid', methods=['POST'])
def aanwezigheid():
    leerling_id = 1 # Voeg hier de juiste leerling_id toe
    les_id = request.form.getlist('les_id')
    aanwezigheid = request.form.getlist('aanwezigheid')
    reden_afwezigheid = request.form.getlist('reden')
    leerling_model.toevoegen_aanwezigheid(leerling_id, les_id, aanwezigheid, reden_afwezigheid)
    return 'Aanwezigheid opgeslagen!'



# Docent routes
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


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

    c.execute("SELECT leerlingen.naam, aanwezigheid.aanwezig, lessen.vak, docenten.naam FROM aanwezigheid INNER JOIN lessen ON aanwezigheid.les_id = lessen.les_id INNER JOIN leerlingen ON aanwezigheid.leerling_id = leerlingen.leerling_id INNER JOIN docenten ON lessen.docent_id = docenten.docent_id")
    rows = c.fetchall()

    docent_dict = {}
    c.execute("SELECT docent_id, naam FROM docenten")
    for docent in c.fetchall():
        docent_dict[docent[0]] = docent[1]

    conn.close()

    les_dict = {}
    for les in lessen:
        les_dict[les[0]] = {'vak': les[1], 'datum': les[2], 'starttijd': les[3], 'eindtijd': les[4], 'docent_id': les[5], 'code': les[6]}

    return render_template('docent_dashboard.html', les_dict=les_dict, rows=rows, docent_dict=docent_dict, lessen=lessen)


@app.route('/docent/lessen/toevoegen', methods=['GET'])
def docent_lessen_toevoegen():
    klassen = lessen_model.get_all_klassen()
    return render_template('docent_lessen.html', klassen=klassen)


@app.route('/docent/lessen/toevoegen', methods=['POST'])
def docent_lessen_toevoegen_post():
    vak = request.form['vak']
    datum = request.form['datum']
    starttijd = request.form['starttijd']
    eindtijd = request.form['eindtijd']
    docent_id = request.form['docent_id']
    klas_id = request.form['klas_id']
    lessen_model.add_lesson(vak, datum, starttijd, eindtijd, docent_id, klas_id)
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

        # Start de update_code() functie in een aparte thread
        t = threading.Thread(target=update_code, args=(vak,))
        t.start()

        return redirect(url_for('docent_lessen_code', code=code))

    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT vak FROM lessen")
    vakken = c.fetchall()
    conn.close()

    code = request.args.get('code')

    return render_template('docent_lessen_code.html', vakken=vakken, code=code)


@app.route('/delete_code/<int:id>', methods=['POST', 'GET'])
def delete_code(id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()

    # Verwijder de code uit de database
    c.execute("UPDATE lessen SET code=NULL WHERE les_id=?", (id,))
    conn.commit()

    conn.close()

    flash('Code verwijderd!')

    # Stuur de gebruiker terug naar de docent dashboard pagina
    return redirect(url_for('docent_dashboard',id=id))


# Les routes
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


@app.route('/les/<int:id>')
def les_overzicht(id):
    data = lessen_model.lessen_overzicht(id)
    if data:
        # De les is gevonden, render de template met de aanwezigheidsgegevens en de lesgegevens
        aanwezigheden, les, vak, count = data
        return render_template('les.html', aanwezigheden=aanwezigheden, les=les, vak=vak, count=count)
    else:
        # De les is niet gevonden, geef een foutmelding
        return "Les niet gevonden"


@app.route('/add_les', methods=['POST'])
def add_les():
    vak = request.form['vak']
    datum = request.form['datum']
    starttijd = request.form['starttijd']
    eindtijd = request.form['eindtijd']
    docent_id = request.form['docent_id']
    lessen = lessen_model.lessen_toevoegen(vak, datum, starttijd, eindtijd, docent_id)
    return redirect('/docent/lessen', lessen=lessen)


def exporteer_lessen():
        lessen = lessen_model.alle_lessen()
        return jsonify(lessen)

@app.route('/API/lessen', methods=["GET", "POST"])
def export_lessen():
    lessen = exporteer_lessen()
    return lessen


@app.route('/API/les/<int:id>')
def les_overzicht_api(id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()

    # Haal de lesgegevens op
    c.execute("SELECT * FROM lessen WHERE les_id=?", (id,))
    les = c.fetchone()

    if les:
        # De les is gevonden, haal de aanwezigheidsgegevens op voor deze les
        c.execute("SELECT leerlingen.naam FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE aanwezigheid.les_id=?", (id,))
        aanwezigheid_naam = c.fetchall()
        c.execute("SELECT aanwezigheid.aanwezig FROM aanwezigheid JOIN leerlingen ON aanwezigheid.leerling_id=leerlingen.leerling_id WHERE aanwezigheid.les_id=?", (id,))
        aanwezigheid_aanwezig = c.fetchall()
        conn.close()
        # Geef een JSON-response met de aanwezigheidsgegevens en de lesgegevens
        return jsonify(aanwezigheid_naam=aanwezigheid_naam,aanwezigheid_aanwezig=aanwezigheid_aanwezig, les=les)
    else:
        # De les is niet gevonden, geef een foutmelding
        conn.close()
        return jsonify(error="Les niet gevonden")


def update_code(vak):
    while True:
        code = random.randint(1000, 9999)
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute("UPDATE lessen SET code=? WHERE vak=?", (code, vak))
        conn.commit()
        conn.close()
        time.sleep(1.5)


# Admin grud paneel routes
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


@app.route('/admin')
def admin():
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leerlingen")
    leerlingen = c.fetchall()
    c.execute("SELECT * FROM docenten")
    docenten = c.fetchall()
    conn.close()
    return render_template('admin.html', leerlingen=leerlingen, docenten=docenten)


@app.route('/edit_leerling/<int:leerling_id>', methods=['GET', 'POST'])
def edit_leerling(leerling_id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute('SELECT * FROM leerlingen WHERE leerling_id = ?', (leerling_id,))
    leerling = c.fetchone()
    conn.close()
    if request.method == 'POST':
        naam = request.form['naam']
        gebruikersnaam = request.form['gebruikersnaam']
        wachtwoord = request.form['wachtwoord']
        rooster = request.form['rooster']
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('UPDATE leerlingen SET naam = ?, gebruikersnaam = ?, wachtwoord = ?, rooster = ? WHERE leerling_id = ?', (naam, gebruikersnaam, wachtwoord, rooster, leerling_id))
        conn.commit()
        conn.close()
        # flash('Leerling updated successfully', 'success')
        return redirect(url_for('admin'))
    return render_template('edit_leerling.html', leerling=leerling)


@app.route('/save_leerling/<int:leerling_id>')
def save_leerling(leerling_id):
    flash('Leerling not updated', 'danger')
    return redirect(url_for('admin'))


@app.route('/edit_docent/<int:docent_id>', methods=['GET', 'POST'])
def edit_docent(docent_id):
    conn = sqlite3.connect('aanwezigheidssysteem.db')
    c = conn.cursor()
    c.execute('SELECT * FROM docenten WHERE docent_id = ?', (docent_id,))
    docent = c.fetchone()
    conn.close()
    if request.method == 'POST':
        naam = request.form['naam']
        gebruikersnaam = request.form['gebruikersnaam']
        wachtwoord = request.form['wachtwoord']
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('UPDATE docenten SET naam = ?, gebruikersnaam = ?, wachtwoord = ? WHERE docent_id = ?', (naam, gebruikersnaam, wachtwoord, docent_id))
        conn.commit()
        conn.close()
        # flash('Docent updated successfully', 'success')
        return redirect(url_for('admin'))
    return render_template('edit_docent.html', docent=docent)


@app.route('/add_leerling', methods=['GET', 'POST'])
def add_leerling():
    if request.method == 'POST':
        naam = request.form['naam']
        gebruikersnaam = request.form['gebruikersnaam']
        wachtwoord = request.form['wachtwoord']
        rooster = request.form['rooster']
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES (?, ?, ?, ?)', (naam, gebruikersnaam, wachtwoord, rooster))
        conn.commit()
        conn.close()
        flash('Leerling toegevoegd', 'success')
        return redirect(url_for('admin'))
    return render_template('admin.html')


@app.route('/add_docent', methods=['GET', 'POST'])
def add_docent():
    if request.method == 'POST':
        naam = request.form['naam']
        gebruikersnaam = request.form['gebruikersnaam']
        wachtwoord = request.form['wachtwoord']
        conn = sqlite3.connect('aanwezigheidssysteem.db')
        c = conn.cursor()
        c.execute('INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)', (naam, gebruikersnaam, wachtwoord))
        conn.commit()
        conn.close()
        flash('Docent toegevoegd', 'success')
        return redirect(url_for('admin'))
    return render_template('admin.html')




if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)
