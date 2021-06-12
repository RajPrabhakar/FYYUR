import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = False
# ENV = 'prod'
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
ENV = 'development'

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:alpha@localhost:5432/fyyur'