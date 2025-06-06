from app import db
import uuid

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    specialization = db.Column(db.String(100))
    license_number = db.Column(db.String(50))
    department = db.Column(db.String(100))
    experience_years = db.Column(db.Integer)
    qualification = db.Column(db.String(100))
    consultation_fee = db.Column(db.Float)
    is_available = db.Column(db.Boolean, default=True)
