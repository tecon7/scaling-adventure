#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Vendor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/vendors')
def vendors():
    return ''

@app.route('/vendors/<int:id>')
def vendor_by_id(id):
    return ''

@app.route('/sweets')
def sweets():
    return ''

@app.route('/sweets/<int:id>')
def sweet_by_id(id):
    return ''

@app.route('/vendor_sweets')
def vendor_sweets():
    return ''

@app.route('vendor_sweets/<int:id>')
def vendor_sweet_by_id(id):
    return ''


if __name__ == '__main__':
    app.run(port=5555)
