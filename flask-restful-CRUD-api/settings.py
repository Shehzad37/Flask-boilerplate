import os

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db/db.sqlite'
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:gujrat123@localhost/practice'
SQLALCHEMY_TRACK_MODIFICATIONS = False