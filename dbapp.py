from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///aanmeldingstool.db"
# initialize the app with the extension
db.init_app(app)

class Klas(db.Model):
    Klas_ID = db.Column(db.Integer, primary_key=True)
    Klas_Naam = db.Column(db.String, unique=True, nullable=False)

class Student(db.Model):
    Student_ID = db.Column(db.Integer, primary_key=True)
    Student_Naam = db.Column(db.String, unique=True, nullable=False)
    Klas_ID = db.Column(db.Integer, db.ForeignKey(Klas.Klas_ID))

class Docent(db.Model):
    Docent_ID = db.Column(db.Integer, primary_key=True)
    Docent_Naam = db.Column(db.String, unique=True, nullable=False)

class Les(db.Model):
    Les_ID = db.Column(db.Integer, primary_key=True)
    Start_Tijd = db.Column(db.Integer, unique=False, nullable=False)
    Eind_Tijd = db.Column(db.Integer, unique=False, nullable=False)
    Docent_ID = db.Column(db.Integer, db.ForeignKey(Docent.Docent_ID))

class Aanwezigheid(db.Model):
    Aanwezigheid_ID = db.Column(db.Integer, primary_key=True)
    Tijdstip = db.Column(db.Integer, unique=False, nullable=False)
    Les_ID = db.Column(db.Integer, db.ForeignKey(Les.Les_ID))
    Student_ID = db.Column(db.Integer, db.ForeignKey(Student.Student_ID))

class Vraag(db.Model):
    Vraag_ID = db.Column(db.Integer, primary_key=True)
    Vraag_Tekst = db.Column(db.String, unique=True, nullable=False)

class Antwoord(db.Model):
    Antwoord_ID = db.Column(db.Integer, primary_key=True)
    Antwoord_Tekst = db.Column(db.String, unique=True, nullable=False)
    Vraag_ID = db.Column(db.Integer, db.ForeignKey(Vraag.Vraag_ID))
    Aanwezigheid_ID = db.Column(db.Integer, db.ForeignKey(Aanwezigheid.Aanwezigheid_ID))

with app.app_context():
    db.create_all()