import json
import os.path
import sqlite3
import os.path
from flask import Flask, jsonify
from flask import render_template, url_for, flash, request, redirect, send_file
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from lib.tablemodel import DatabaseModel
<<<<<<< HEAD
=======
import json

# Flask Settings
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)
app.secret_key = 'Hogeschoolrotterdam'

with open('rooster.json') as f:
    data = json.load(f)

DATABASE = os.path.join(app.root_path, 'database', 'aanmeldingstool.db')
dbm = DatabaseModel(DATABASE)
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

# c.execute('''CREATE TABLE Users
#              (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
>>>>>>> fcf1c3a51001a2ac827b88cc693285f892d7cd58

# c.execute("DROP TABLE users")

<<<<<<< HEAD
def automatisch_db_fill():
    app = Flask(__name__)
    app.secret_key = 'Hogeschoolrotterdam'
    DATABASE = os.path.join(app.root_path, 'database', 'aanmeldingstool.db')
    dbm = DatabaseModel(DATABASE)
    
=======
# c.execute("ALTER TABLE users ADD COLUMN id INTEGER PRIMARY KEY AUTOINCREMENT;")

# c.execute("ALTER TABLE users DROP COLUMN user_id;")
# for row in data['lessen']:
#     c.execute('''INSERT INTO lessen (id, name, teacher) VALUES (?, ?, ?)''',
#               (row['id'], row['name'], row['teacher']))
>>>>>>> fcf1c3a51001a2ac827b88cc693285f892d7cd58

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

<<<<<<< HEAD
=======
c.execute("INSERT INTO Users(username, password) VALUES (?,?)", ('admin', 'admin'))

conn.commit()
>>>>>>> fcf1c3a51001a2ac827b88cc693285f892d7cd58

    # Load the data from the JSON file
    with open('rooster.json', 'r') as f:
        data = json.load(f)

    # Process the data and update the database
    for record in data.get('lessen', []):
        if 'id' not in record:
            print("Error: missing 'id' key in dictionary")
            continue

        if not isinstance(record, dict):
            print(f"Error: expected a dictionary, got {type(record)}")
            continue

        # Check if the record already exists in the database
        cursor.execute('SELECT id FROM lessen WHERE id=?', (record['id'],))
        result = cursor.fetchone()

        if result:
            # Record already exists, update it
            cursor.execute('UPDATE lessen SET classroom=?, name=?, teacher=? WHERE id=?',
                (record.get('classroom'), record.get('name'), record.get('teacher'), record['id']))
        else:
            # Record doesn't exist, insert it
            cursor.execute('INSERT INTO lessen (id, name, teacher, classroom) VALUES (?, ?, ?, ?)',
                (record['id'], record.get('classroom'), record.get('name'), record.get('teacher')))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
