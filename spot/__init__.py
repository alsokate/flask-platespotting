from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



plate = Flask(__name__)
plate.config.from_object('config')
db = SQLAlchemy(plate)


from spot import views, models

