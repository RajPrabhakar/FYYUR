import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = False
ENV = 'prod'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://wjszegaakgtnak:db90efe1108441db48d177ab98df9ae679a6fb88e1ac6182e54aa1d4b36fc249@ec2-3-233-7-12.compute-1.amazonaws.com:5432/d721tgln18l8u1'
