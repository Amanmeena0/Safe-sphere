from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from app.config import Config
from app.models import db

bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    db.init_app(app)
    CORS(app)

    from app.routes.search_routes import search_bp
    from app.routes.hello_auth import hello_bp 
    from app.routes.sos_route.police_services import police_bp  
    from app.routes.sos_route.crime_data import crime_data_bp
    from app.routes.profile_route.user_registration import user_bp
    from app.routes.profile_route.profile import profile_bp

    app.register_blueprint(hello_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(police_bp)  
    app.register_blueprint(crime_data_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)

    # Create tables
    with app.app_context():
        from app import models  # Import models to ensure they're registered
        db.create_all()

    return app