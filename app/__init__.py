from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
    
    migrate = Migrate(app, db)
    
    from .routes import bp
    app.register_blueprint(bp)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app