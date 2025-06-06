from app import db
import uuid

class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    appointment_id = db.Column(db.String, db.ForeignKey('appointments.id'), nullable=False)
    patient_id = db.Column(db.String, db.ForeignKey('patients.id'), nullable=False)
    medication = db.Column(db.Text, nullable=False)
    dosage = db.Column(db.String(100))
    instructions = db.Column(db.Text)

    appointment = db.relationship('Appointment', backref='prescriptions')
    patient = db.relationship('Patient', backref='prescriptions')
