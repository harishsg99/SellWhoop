from flask import Flask
from SellWhoop.config import configurations
from flask_sqlalchemy import SQLAlchemy


def create_app(environment_name ='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])
    return app
