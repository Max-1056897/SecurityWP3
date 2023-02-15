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

# Flask Settings
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)
app.secret_key = 'Hogeschoolrotterdam'

DATABASE = os.path.join(app.root_path, 'database', 'aanmeldingstool.db')
dbm = DatabaseModel(DATABASE)

login_manager = LoginManager(app)
login_manager.login_view = "login"

# Flaskform Login
class LoginForm(FlaskForm):
 username = StringField('Username',validators=[DataRequired()])
 password = PasswordField('Password',validators=[DataRequired()])
 remember = BooleanField('Remember Me')
 submit = SubmitField('Login')
 def validate_username(self, username):
    conn = sqlite3.connect(DATABASE)
    curs = conn.cursor()
    curs.execute("SELECT username FROM Users where username = (?)",[username.data])
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
    curs.execute("SELECT * from Users where user_id = (?)",[user_id])
    lu = curs.fetchone()
    if lu is None:
      return None
    else:
      return User(int(lu[0]), lu[1], lu[2])

# Login Route
@app.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('leerlingdashboard'))
  form = LoginForm()
  if form.validate_on_submit():
    conn = sqlite3.connect(DATABASE)
    curs = conn.cursor()
    curs.execute("SELECT * FROM Users where username = (?)",    [form.username.data])
    user = curs.fetchone()
    Us = load_user(user[0])
    if form.username.data == Us.username and form.password.data == Us.password:
        login_user(Us)
        return redirect(('leerling-dashboard'))
    else:
        flash('Login Unsuccessfull.')
  return render_template('login.html',title='Login', form=form)

@app.route("/")
def redirectpage():
    return redirect("login")

@app.route("/leerling-dashboard", methods=['GET','POST'])
@login_required
def leerlingdashboard():
    return render_template('leerling-dashboard.html')



if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)