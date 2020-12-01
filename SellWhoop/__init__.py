from flask import Flask
from SellWhoop.config import configurations
from flask_sqlalchemy import SQLAlchemy
from SellWhoop.extensions import db
from SellWhoop.blueprints.products import products

def create_app(environment_name ='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])
    db.init_app(app)
    return app
