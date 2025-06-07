from flask import Blueprint, request, jsonify, abort
from app.models.doctor import Doctor
from app.extensions import db

doctor_bp = Blueprint('doctors', __name__)

@doctor_bp.route('/', methods=['GET'])
def get_all_doctors():
    doctors = Doctor.query.all()
    result = []
    for d in doctors:
        result.append({
            'id': d.id,
            'name': d.name,
            'email': d.email,
            'phone': d.phone,
            'specialization': d.specialization,
            'license_number': d.license_number,
            'department': d.department,
            'experience_years': d.experience_years,
            'qualification': d.qualification,
            'consultation_fee': d.consultation_fee,
            'is_available': d.is_available
        })
    return jsonify(result), 200

@doctor_bp.route('/<string:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if not doctor:
        abort(404, description="Doctor not found")
    return jsonify({
        'id': doctor.id,
        'name': doctor.name,
        'email': doctor.email,
        'phone': doctor.phone,
        'specialization': doctor.specialization,
        'license_number': doctor.license_number,
        'department': doctor.department,
        'experience_years': doctor.experience_years,
        'qualification': doctor.qualification,
        'consultation_fee': doctor.consultation_fee,
        'is_available': doctor.is_available
    }), 200

@doctor_bp.route('/', methods=['POST'])
def create_doctor():
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Name is required")

    doctor = Doctor(
        name=data['name'],
        email=data.get('email'),
        phone=data.get('phone'),
        specialization=data.get('specialization'),
        license_number=data.get('license_number'),
        department=data.get('department'),
        experience_years=data.get('experience_years'),
        qualification=data.get('qualification'),
        consultation_fee=data.get('consultation_fee'),
        is_available=data.get('is_available', True)
    )
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'id': doctor.id}), 201

@doctor_bp.route('/<string:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if not doctor:
        abort(404, description="Doctor not found")

    data = request.get_json()
    if 'name' in data:
        doctor.name = data['name']
    if 'email' in data:
        doctor.email = data['email']
    if 'phone' in data:
        doctor.phone = data['phone']
    if 'specialization' in data:
        doctor.specialization = data['specialization']
    if 'license_number' in data:
        doctor.license_number = data['license_number']
    if 'department' in data:
        doctor.department = data['department']
    if 'experience_years' in data:
        doctor.experience_years = data['experience_years']
    if 'qualification' in data:
        doctor.qualification = data['qualification']
    if 'consultation_fee' in data:
        doctor.consultation_fee = data['consultation_fee']
    if 'is_available' in data:
        doctor.is_available = data['is_available']

    db.session.commit()
    return jsonify({'message': 'Doctor updated'}), 200

@doctor_bp.route('/<string:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if not doctor:
        abort(404, description="Doctor not found")

    db.session.delete(doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor deleted'}), 200
