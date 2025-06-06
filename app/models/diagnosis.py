from app import db
import uuid

class Diagnosis(db.Model):
    __tablename__ = 'diagnoses'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    appointment_id = db.Column(db.String, db.ForeignKey('appointments.id'), nullable=False)
    patient_id = db.Column(db.String, db.ForeignKey('patients.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)

    appointment = db.relationship('Appointment', backref='diagnoses')
    patient = db.relationship('Patient', backref='diagnoses')
