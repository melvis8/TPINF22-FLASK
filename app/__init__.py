# app/__init__.py

from flask import Flask
from config import Config
from app.extensions import db  # Import de l'extension SQLAlchemy

# Importation des blueprints pour chaque ressource
from app.routes.patient_routes import patient_bp
from app.routes.appointment_routes import appointment_bp
from app.routes.doctor_routes import doctor_bp
from app.routes.diagnosis_routes import diagnosis_bp
from app.routes.prescription_routes import prescription_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialisation de la base de données
    db.init_app(app)
    # migrate.init_app(app, db)  # Active-le si tu utilises Flask-Migrate

    # Enregistrement des blueprints avec des URL prefixes clairs
    app.register_blueprint(patient_bp, url_prefix='/patients')
    app.register_blueprint(appointment_bp, url_prefix='/appointments')
    app.register_blueprint(doctor_bp, url_prefix='/doctors')
    app.register_blueprint(diagnosis_bp, url_prefix='/diagnoses')
    app.register_blueprint(prescription_bp, url_prefix='/prescriptions')

    # Création des tables si tu n’utilises pas Flask-Migrate
    with app.app_context():
        db.create_all()

    return app
