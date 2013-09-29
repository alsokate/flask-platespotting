from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID
from config import basedir



plate = Flask(__name__)
plate.config.from_object('config')
db = SQLAlchemy(plate)


from spot import views, models

