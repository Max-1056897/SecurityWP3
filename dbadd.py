import os.path
import sqlite3
import os.path
from flask import Flask
from lib.tablemodel import DatabaseModel
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

# c.execute('''CREATE TABLE lessen
#              (id INTEGER PRIMARY KEY, name TEXT, teacher TEXT)''')


for row in data['lessen']:
    c.execute('''INSERT INTO lessen (id, name, teacher) VALUES (?, ?, ?)''',
              (row['id'], row['name'], row['teacher']))

# c.execute('''DELETE FROM lessen WHERE ID = 0''')

conn.commit()

conn.close()