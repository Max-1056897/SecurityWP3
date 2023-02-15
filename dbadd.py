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
conn = sqlite3.connect(DATABASE)
c = conn.cursor()
                   
c.execute("INSERT INTO users (user_id, username, password) VALUES (1,'admin', '1234')")

conn.commit()