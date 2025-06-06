from app import db
import uuid
from datetime import datetime

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_id = db.Column(db.String, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.String, db.ForeignKey('doctors.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='scheduled')

    patient = db.relationship('Patient', backref='appointments')
    doctor = db.relationship('Doctor', backref='appointments')
