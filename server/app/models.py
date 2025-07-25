# app/models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    clerk_user_id = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    address = db.Column(db.String(255))
    aadhar_number = db.Column(db.String(12), unique=True)
    role = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    emergency_contact_name = db.Column(db.String(100))
    emergency_contact_phone = db.Column(db.String(15))
    registration_date = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(20))


class LostItem(db.Model):
    __tablename__ = 'lost_items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    placeofloss = db.Column(db.String(255))
    loss_datetime = db.Column(db.DateTime, nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255))
    document_type = db.Column(db.LargeBinary, nullable=False)
    police_station = db.Column(db.String(100))
    district = db.Column(db.String(100))

class cyberCrime(db.Model):
    __tablename__ = 'cyber_crimes'

    id = db.Column(db.Integer, primary_key=True)
    crimeCategory = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(100))
    date_of_incident = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(50))
    IpAddress = db.Column(db.String(50))
    description = db.Column(db.Text, nullable=False)
    digitalEvidence = db.Column(db.LargeBinary, default='')
    full_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100))
    address = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    relation = db.Column(db.String(50))
    policeStation = db.Column(db.String(100), nullable=False)

