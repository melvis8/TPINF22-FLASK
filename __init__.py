from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Enregistrement des blueprints
    from app.routes.patient_routes import patient_bp
    from app.routes.doctor_routes import doctor_bp
    # Add at the top:
    from app.routes.appointment_routes import appointment_bp
    from app.routes.diagnosis_routes import diagnosis_bp
    from app.routes.prescription_routes import prescription_bp

    # Inside create_app() before return:
    app.register_blueprint(appointment_bp, url_prefix='/api/appointments')
    app.register_blueprint(diagnosis_bp, url_prefix='/api/diagnoses')
    app.register_blueprint(prescription_bp, url_prefix='/api/prescriptions')
    app.register_blueprint(patient_bp, url_prefix='/api/patients')
    app.register_blueprint(doctor_bp, url_prefix='/api/doctors')

    return app
