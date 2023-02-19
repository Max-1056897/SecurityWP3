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


def automatisch_db_fill():
    app = Flask(__name__)
    app.secret_key = 'Hogeschoolrotterdam'
    DATABASE = os.path.join(app.root_path, 'database', 'aanmeldingstool.db')
    dbm = DatabaseModel(DATABASE)
    

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


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
