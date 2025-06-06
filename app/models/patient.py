import uuid
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from app import db


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(200))
    medical_history = db.Column(db.Text)
    emergency_contact = db.Column(db.String(120))
