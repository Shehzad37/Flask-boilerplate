from flask import Flask

from extensions import db, ma

def init(config='settings.py'):

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    return app


