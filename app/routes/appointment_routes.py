from flask import Blueprint, request, jsonify, abort
from app.models.appointment import Appointment
from app.extensions import db
from datetime import datetime

appointment_bp = Blueprint('appointments', __name__)

@appointment_bp.route('/', methods=['GET'])
def get_all_appointments():
    appointments = Appointment.query.all()
    result = []
    for a in appointments:
        result.append({
            'id': a.id,
            'patient_id': a.patient_id,
            'doctor_id': a.doctor_id,
            'appointment_date': a.appointment_date.isoformat(),
            'status': a.status
        })
    return jsonify(result), 200

@appointment_bp.route('/<string:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        abort(404, description="Appointment not found")
    return jsonify({
        'id': appointment.id,
        'patient_id': appointment.patient_id,
        'doctor_id': appointment.doctor_id,
        'appointment_date': appointment.appointment_date.isoformat(),
        'status': appointment.status
    }), 200

@appointment_bp.route('/', methods=['POST'])
def create_appointment():
    data = request.get_json()
    required_fields = ['patient_id', 'doctor_id', 'appointment_date']
    if not data or not all(field in data for field in required_fields):
        abort(400, description=f"Required fields: {required_fields}")

    try:
        appt_date = datetime.fromisoformat(data['appointment_date'])
    except ValueError:
        abort(400, description="appointment_date must be ISO format datetime string")

    appointment = Appointment(
        patient_id=data['patient_id'],
        doctor_id=data['doctor_id'],
        appointment_date=appt_date,
        status=data.get('status', 'scheduled')
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify({'id': appointment.id}), 201

@appointment_bp.route('/<string:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        abort(404, description="Appointment not found")

    data = request.get_json()
    if 'patient_id' in data:
        appointment.patient_id = data['patient_id']
    if 'doctor_id' in data:
        appointment.doctor_id = data['doctor_id']
    if 'appointment_date' in data:
        try:
            appointment.appointment_date = datetime.fromisoformat(data['appointment_date'])
        except ValueError:
            abort(400, description="appointment_date must be ISO format datetime string")
    if 'status' in data:
        appointment.status = data['status']

    db.session.commit()
    return jsonify({'message': 'Appointment updated'}), 200

@appointment_bp.route('/<string:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        abort(404, description="Appointment not found")

    db.session.delete(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment deleted'}), 200
