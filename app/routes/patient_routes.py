from flask import Blueprint, request, jsonify, abort
from ..models.patient import Patient
from app.extensions import db
from datetime import datetime

patient_bp = Blueprint('patients', __name__)

@patient_bp.route('/', methods=['GET'])
def get_all_patients():
    patients = Patient.query.all()
    result = []
    for p in patients:
        result.append({
            'id': p.id,
            'name': p.name,
            'email': p.email,
            'phone': p.phone,
            'date_of_birth': p.date_of_birth.isoformat() if p.date_of_birth else None,
            'gender': p.gender,
            'address': p.address,
            'medical_history': p.medical_history,
            'emergency_contact': p.emergency_contact
        })
    return jsonify(result), 200

@patient_bp.route('/<string:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        abort(404, description="Patient not found")
    return jsonify({
        'id': patient.id,
        'name': patient.name,
        'email': patient.email,
        'phone': patient.phone,
        'date_of_birth': patient.date_of_birth.isoformat() if patient.date_of_birth else None,
        'gender': patient.gender,
        'address': patient.address,
        'medical_history': patient.medical_history,
        'emergency_contact': patient.emergency_contact
    }), 200

@patient_bp.route('/', methods=['POST'])
def create_patient():
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Name is required")

    dob = None
    if 'date_of_birth' in data:
        try:
            dob = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        except ValueError:
            abort(400, description="date_of_birth must be in YYYY-MM-DD format")

    patient = Patient(
        name=data['name'],
        email=data.get('email'),
        phone=data.get('phone'),
        date_of_birth=dob,
        gender=data.get('gender'),
        address=data.get('address'),
        medical_history=data.get('medical_history'),
        emergency_contact=data.get('emergency_contact')
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify({'id': patient.id}), 201

@patient_bp.route('/<string:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        abort(404, description="Patient not found")

    data = request.get_json()
    if 'name' in data:
        patient.name = data['name']
    if 'email' in data:
        patient.email = data['email']
    if 'phone' in data:
        patient.phone = data['phone']
    if 'date_of_birth' in data:
        try:
            patient.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        except ValueError:
            abort(400, description="date_of_birth must be in YYYY-MM-DD format")
    if 'gender' in data:
        patient.gender = data['gender']
    if 'address' in data:
        patient.address = data['address']
    if 'medical_history' in data:
        patient.medical_history = data['medical_history']
    if 'emergency_contact' in data:
        patient.emergency_contact = data['emergency_contact']

    db.session.commit()
    return jsonify({'message': 'Patient updated'}), 200

@patient_bp.route('/<string:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        abort(404, description="Patient not found")

    db.session.delete(patient)
    db.session.commit()
    return jsonify({'message': 'Patient deleted'}), 200
