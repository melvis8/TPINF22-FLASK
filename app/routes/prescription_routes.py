from flask import Blueprint, request, jsonify, abort
from app.models.prescription import Prescription
from app.extensions import db

prescription_bp = Blueprint('prescriptions', __name__)

@prescription_bp.route('/', methods=['GET'])
def get_all_prescriptions():
    prescriptions = Prescription.query.all()
    result = []
    for p in prescriptions:
        result.append({
            'id': p.id,
            'appointment_id': p.appointment_id,
            'patient_id': p.patient_id,
            'medication': p.medication,
            'dosage': p.dosage,
            'instructions': p.instructions
        })
    return jsonify(result), 200

@prescription_bp.route('/<string:prescription_id>', methods=['GET'])
def get_prescription(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        abort(404, description="Prescription not found")
    return jsonify({
        'id': prescription.id,
        'appointment_id': prescription.appointment_id,
        'patient_id': prescription.patient_id,
        'medication': prescription.medication,
        'dosage': prescription.dosage,
        'instructions': prescription.instructions
    }), 200

@prescription_bp.route('/', methods=['POST'])
def create_prescription():
    data = request.get_json()
    required_fields = ['appointment_id', 'patient_id', 'medication']
    if not data or not all(field in data for field in required_fields):
        abort(400, description=f"Required fields: {required_fields}")

    prescription = Prescription(
        appointment_id=data['appointment_id'],
        patient_id=data['patient_id'],
        medication=data['medication'],
        dosage=data.get('dosage'),
        instructions=data.get('instructions')
    )
    db.session.add(prescription)
    db.session.commit()
    return jsonify({'id': prescription.id}), 201

@prescription_bp.route('/<string:prescription_id>', methods=['PUT'])
def update_prescription(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        abort(404, description="Prescription not found")

    data = request.get_json()
    if 'appointment_id' in data:
        prescription.appointment_id = data['appointment_id']
    if 'patient_id' in data:
        prescription.patient_id = data['patient_id']
    if 'medication' in data:
        prescription.medication = data['medication']
    if 'dosage' in data:
        prescription.dosage = data['dosage']
    if 'instructions' in data:
        prescription.instructions = data['instructions']

    db.session.commit()
    return jsonify({'message': 'Prescription updated'}), 200

@prescription_bp.route('/<string:prescription_id>', methods=['DELETE'])
def delete_prescription(prescription_id):
    prescription = Prescription.query.get(prescription_id)
    if not prescription:
        abort(404, description="Prescription not found")

    db.session.delete(prescription)
    db.session.commit()
    return jsonify({'message': 'Prescription deleted'}), 200
