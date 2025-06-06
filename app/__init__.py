from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialisation directe ici (plus besoin d'extensions.py)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuration de base
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:melvis123@localhost:5432/hospital_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "dev_secret_key_change_later"
    app.config['DEBUG'] = True

    # Initialisation des extensions
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.patient_routes import patient_bp
    from app.routes.appointment_routes import appointment_bp
    from app.routes.doctor_routes import doctor_bp
    from app.routes.diagnosis_routes import diagnosis_bp
    from app.routes.prescription_routes import prescription_bp


    # Enregistrement des blueprints
    app.register_blueprint(patient_bp, url_prefix="/patients")
    app.register_blueprint(appointment_bp, url_prefix="/appointments")
    app.register_blueprint(doctor_bp, url_prefix="/doctors")
    app.register_blueprint(diagnosis_bp, url_prefix="/diagnoses")
    app.register_blueprint(prescription_bp, url_prefix="/prescriptions")

    return app
