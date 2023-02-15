from flask import Flask
import sqlite3

# create the extension
sqlite3.connect('aanmeldingstool.db')
# create the app
app = Flask(__name__)
conn = sqlite3.connect('aanmeldingstool') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS student
          ([Student_id] INTEGER PRIMARY KEY, [Student_Naam] TEXT, [Student_Nummer] INTEGER)
          ''')
                     
conn.commit()




# class Klas(db.Model):
#     Klas_ID = db.Column(db.Integer, primary_key=True)
#     Klas_Naam = db.Column(db.String, unique=True, nullable=False)

# class Student(db.Model):
#     Student_ID = db.Column(db.Integer, primary_key=True)
#     Student_Nummer = db.Column(db.Integer, unique=True, nullable=False)
#     Student_Naam = db.Column(db.String, unique=True, nullable=False)
#     Klas_ID = db.Column(db.Integer, db.ForeignKey(Klas.Klas_ID))

# class Docent(db.Model):
#     Docent_ID = db.Column(db.Integer, primary_key=True)
#     Docent_Naam = db.Column(db.String, unique=True, nullable=False)

# class Les(db.Model):
#     Les_ID = db.Column(db.Integer, primary_key=True)
#     Start_Tijd = db.Column(db.Integer, unique=False, nullable=False)
#     Eind_Tijd = db.Column(db.Integer, unique=False, nullable=False)
#     Docent_ID = db.Column(db.Integer, db.ForeignKey(Docent.Docent_ID))

# class Aanwezigheid(db.Model):
#     Aanwezigheid_ID = db.Column(db.Integer, primary_key=True)
#     Tijdstip = db.Column(db.Integer, unique=False, nullable=False)
#     Les_ID = db.Column(db.Integer, db.ForeignKey(Les.Les_ID))
#     Student_ID = db.Column(db.Integer, db.ForeignKey(Student.Student_ID))

# class Vraag(db.Model):
#     Vraag_ID = db.Column(db.Integer, primary_key=True)
#     Vraag_Tekst = db.Column(db.String, unique=True, nullable=False)

# class Antwoord(db.Model):
#     Antwoord_ID = db.Column(db.Integer, primary_key=True)
#     Antwoord_Tekst = db.Column(db.String, unique=True, nullable=False)
#     Vraag_ID = db.Column(db.Integer, db.ForeignKey(Vraag.Vraag_ID))
#     Aanwezigheid_ID = db.Column(db.Integer, db.ForeignKey(Aanwezigheid.Aanwezigheid_ID))

# with app.app_context():
#     db.create_all()