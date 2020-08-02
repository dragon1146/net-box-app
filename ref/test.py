from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/glitch/Documents/pythonRelated/IT-Toolkit/networking-toolkit/toolbox.db'

db = SQLAlchemy(app)

class Networking_toolbox(db.Model):
    # __table__ = networking_toolbox
    # id = db.Column('id', db.Integer, )
    task = db.Column('task', db.String, primary_key=True)
    command = db.Column('command', db.String)

