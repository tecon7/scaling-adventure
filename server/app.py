#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, Vendor, Sweet, VendorSweet 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/vendors', methods=['GET'])
def vendors():
    vendors = Vendor.query.all()
    data = [vendor.to_dict() for vendor in vendors]
    return make_response(jsonify(data), 200)


@app.route('/vendors/<int:id>', methods=['GET'])
def vendor_by_id(id):
    vendor = Vendor.query.filter(Vendor.id == id).first()
    if not vendor:
        return make_response(jsonify({
            'error': 'Vendor not found'
        }))
    return make_response(vendor.to_dict(), 200)


@app.route('/sweets', methods=['GET'])
def sweets():
    sweets = Sweet.query.all()
    data = [sweet.to_dict() for sweet in sweets]
    return make_response(jsonify(data), 200)

@app.route('/sweets/<int:id>', methods=['GET', 'PATCH'])
def sweet_by_id(id):
    sweet = Sweet.query.filter(Sweet.id == id).first()
    if sweet is None:
        return make_response(jsonify({"error": "Sweet not found"}), 200)
    if request.method == 'GET':
        return make_response(jsonify(sweet.to_dict()), 200)
    elif request.method == 'PATCH':
        data = request.get_json()
        for field, value in data.items():
            setattr(sweet, field, value)
        db.session.add(sweet)
        db.session.commit()
        return make_response(jsonify(sweet.to_dict()), 200)

@app.route('/vendor_sweets', methods=['POST'])
def vendor_sweets():
    body = request.get_json()
    new_vs = VendorSweet(
        price=body['price'],
        vendor_id=body['vendor_id'],
        sweet_id=body['sweet_id']
    )
    db.session.add(new_vs)
    db.session.commit()
    return make_response(jsonify(new_vs.to_dict()), 201)

@app.route('/vendor_sweets/<int:id>', methods=['DELETE'])
def vendor_sweet_by_id(id):
    vsi = VendorSweet.query.filter(VendorSweet.id == id).first()
    if vsi is None:
        return make_response(jsonify({"error": "VendorSweet"}), 200)
    else:
        db.session.delete(vsi)  
        db.session.commit()
        return make_response(jsonify({}), 200)

if __name__ == '__main__':
    app.run(port=5555)
