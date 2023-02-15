import os.path
import sqlite3
import os.path
from flask import Flask
from flask import render_template, url_for, flash, request, redirect, send_file
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from lib.tablemodel import DatabaseModel
import random



# Flask Settings
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)
app.secret_key = 'Hogeschoolrotterdam'

DATABASE = os.path.join(app.root_path, 'Database', 'aanmeldingstool.db')
dbm = DatabaseModel(DATABASE)

login_manager = LoginManager(app)
login_manager.login_view = "login"

conn = sqlite3.connect(DATABASE)
curs = conn.cursor()

# Flaskform Login
class LoginForm(FlaskForm):
 username = StringField('Student_Naam',validators=[DataRequired()])
 password = PasswordField('Student_ID',validators=[DataRequired()])
 remember = BooleanField('Remember Me')
 submit = SubmitField('Login')
 def validate_username(self, username):
    conn = sqlite3.connect(DATABASE)
    curs = conn.cursor()
    curs.execute("SELECT Student_Naam FROM Student where Student_ID = (?)",[username.data])
    valusername = curs.fetchone()
    if valusername is None:
      raise ValidationError('This username ID is not registered. Please register before login')

class User(UserMixin):
    def __init__(self, id, username, password):
         self.id = id
         self.username = username
         self.password = password
         self.authenticated = False
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(DATABASE)
    curs = conn.cursor()
    curs.execute("SELECT * from student where Klas_ID = (?)",[user_id])
    lu = curs.fetchone()
    if lu is None:
      return None
    else:
      return User(int(lu[0]), lu[1], lu[2])

@app.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('random-code-generator'))
  form = LoginForm()
  if form.validate_on_submit():
    conn = sqlite3.connect(DATABASE)
    curs = conn.cursor()
    curs.execute("SELECT * FROM student where Student_Naam = (?)",    [form.username.data])
    user = curs.fetchone()
    Us = load_user(user[0])
    if form.username.data == Us.username and form.password.data == Us.password:
        login_user(Us)
        return redirect(('random-code-generator'))
    else:
        flash('Login Unsuccessfull.')
  return render_template('student-attendence.html',title='Login', form=form)


@app.route("/")
def redirectpage():
    return redirect("login")

@app.route('/teacher-portal', methods=['GET','POST'])
def techerPortal():
    return render_template("teacher-portal.html")

def get_value():
    low = 100000
    high = 999999
    num = random.randint(low, high)
    value = num
    print (value)
    return value

@app.route('/random-code-generator', methods=['GET','POST'])
@login_required
def randomCodeGenerator():
    value_generator = ""
    if request.method == 'POST':
        value_generator = get_value()
    return render_template("random-code-generator.html", value_generator=value_generator)



# @app.route("/get_value", methods=["POST"])
def get_value():
    low = 0
    high = 999999
    num = random.randint(low, high)
    value = num
    print (value)
    return value

# @app.route('/student-attendence', methods=['GET','POST'])
# def studentAttendence():
#     value_generator = ""
#     if request.method == 'POST':
#         value_generator = get_value()
#     #low = 0
#     #high = 999999
#     #num = random.randint(low, high)
#     # if form.validate_on_submit():
#     #x = ("Jouw unieke aanwezigheids code voor vandaag is:" + str(num))
    
#     return render_template("student-attendence.html", value_generator=value_generator)

    

@app.route('/logout')
def logout():
    return "<p>Logout</p>"

@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email= request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 5:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 3:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        else: 
            flash('Account created', category='succes')
            pass
    return render_template("sign_up.html")

if __name__ == '__main__':
     app.run(debug=True)