from flask import Flask
from .extensions import db, migrate
from flask_migrate import Migrate 
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Chargement des variables d'environnement
load_dotenv()

# Initialisation directe ici
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuration de base
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:melvis123@localhost:5432/hospital'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZWQyNTUxOQAAACBIuQNrZ8/MqLGjk1JMx8CW2s0itbKJMQYlNxvfgAaO5QAAALDv/IlC7/yJQgAAAAtzc2gtZWQyNTUxOQAAACBIuQNrZ8/MqLGjk1JMx8CW2s0itbKJMQYlNxvfgAaO5QAAAEB9WPK5UfqOdQx+yGstOQCd1gSFIdDXMoj20CX7TOwU9Ei5A2tnz8yosaOTUkzHwJbazSK1sokxBiU3G9+ABo7lAAAAJm1lbHZpcy1kZXZAbWVsdmlzLWRldi1IUC1FTlZZLU5vdG"
    app.config['DEBUG'] = True

    # Initialisation des extensions
    db.init_app(app)
    migrate.init_app(app, db)

     # Importer les modèles ici (exemple avec Doctor et Patient)
    from app.models.doctor import Doctor
    from app.models.patient import Patient
    from app.models.appointment import Appointment
    from app.models.diagnosis import Diagnosis
    from app.models.prescription import Prescription

    # 🔐 Configuration Gemini
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment.")
    genai.configure(api_key=gemini_api_key)

    # 📦 Import et enregistrement des blueprints
    from app.routes.patient_routes import patient_bp
    from app.routes.appointment_routes import appointment_bp
    from app.routes.doctor_routes import doctor_bp
    from app.routes.diagnosis_routes import diagnosis_bp
    from app.routes.prescription_routes import prescription_bp
    from app.routes.gemini_routes import gemini_bp

    app.register_blueprint(patient_bp, url_prefix="/patients")
    app.register_blueprint(appointment_bp, url_prefix="/appointments")
    app.register_blueprint(doctor_bp, url_prefix="/doctors")
    app.register_blueprint(diagnosis_bp, url_prefix="/diagnoses")
    app.register_blueprint(prescription_bp, url_prefix="/prescriptions")
    app.register_blueprint(gemini_bp, url_prefix="/ai")


    return app
