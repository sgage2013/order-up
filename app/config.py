import os
from flask import Flask
from os import environ
from flask_sqlalchemy import SQLAlchemy

class Configuration:
    SECRET_KEY = os.environ.get('qp02348jrqj43rpqj34pqjr')
    SQLALCHEMY_DATABASE_URI = environ.get("DATABSE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

