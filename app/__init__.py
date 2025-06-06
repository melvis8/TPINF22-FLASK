from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # or use your config file

    db.init_app(app)

    with app.app_context():
        from .routes.patient_routes import patient_bp
        app.register_blueprint(patient_bp, url_prefix='/patients')


        db.create_all()  # create tables if not using Flask-Migrate

    return app
