from flask import Flask, request
from extensions import db, ma
import os


def init(config='settings.py'):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()

    return app
