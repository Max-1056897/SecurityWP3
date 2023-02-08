from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index'

@main.route('/profile')
def profile():
    return 'Profile'