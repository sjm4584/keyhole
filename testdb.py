#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Spoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(40), unique=True)
    ip_addr = db.Column(db.String(15), unique=False)
    username = db.Column(db.String(40), unique=False)
    password = db.Column(db.String(60), unique=False)

    def __init__(self, hostname, ip_addr, username, password):
        self.hostname = hostname
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
    
