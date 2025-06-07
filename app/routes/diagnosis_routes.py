from flask import Blueprint, request, jsonify, abort
from app.models.diagnosis import Diagnosis
from app.extensions import db

diagnosis_bp = Blueprint('diagnoses', __name__)

@diagnosis_bp.route('/', methods=['GET'])
def get_all_diagnoses():
    diagnoses = Diagnosis.query.all()
    result = []
    for d in diagnoses:
        result.append({
            'id': d.id,
            'appointment_id': d.appointment_id,
            'patient_id': d.patient_id,
            'description': d.description
        })
    return jsonify(result), 200

@diagnosis_bp.route('/<string:diagnosis_id>', methods=['GET'])
def get_diagnosis(diagnosis_id):
    diagnosis = Diagnosis.query.get(diagnosis_id)
    if not diagnosis:
        abort(404, description="Diagnosis not found")
    return jsonify({
        'id': diagnosis.id,
        'appointment_id': diagnosis.appointment_id,
        'patient_id': diagnosis.patient_id,
        'description': diagnosis.description
    }), 200

@diagnosis_bp.route('/', methods=['POST'])
def create_diagnosis():
    data = request.get_json()
    required_fields = ['appointment_id', 'patient_id', 'description']
    if not data or not all(field in data for field in required_fields):
        abort(400, description=f"Required fields: {required_fields}")

    diagnosis = Diagnosis(
        appointment_id=data['appointment_id'],
        patient_id=data['patient_id'],
        description=data['description']
    )
    db.session.add(diagnosis)
    db.session.commit()
    return jsonify({'id': diagnosis.id}), 201

@diagnosis_bp.route('/<string:diagnosis_id>', methods=['PUT'])
def update_diagnosis(diagnosis_id):
    diagnosis = Diagnosis.query.get(diagnosis_id)
    if not diagnosis:
        abort(404, description="Diagnosis not found")

    data = request.get_json()
    if 'appointment_id' in data:
        diagnosis.appointment_id = data['appointment_id']
    if 'patient_id' in data:
        diagnosis.patient_id = data['patient_id']
    if 'description' in data:
        diagnosis.description = data['description']

    db.session.commit()
    return jsonify({'message': 'Diagnosis updated'}), 200

@diagnosis_bp.route('/<string:diagnosis_id>', methods=['DELETE'])
def delete_diagnosis(diagnosis_id):
    diagnosis = Diagnosis.query.get(diagnosis_id)
    if not diagnosis:
        abort(404, description="Diagnosis not found")

    db.session.delete(diagnosis)
    db.session.commit()
    return jsonify({'message': 'Diagnosis deleted'}), 200
