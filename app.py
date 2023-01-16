from flask import Flask
from routes.address import address
from flask_sqlalchemy import SQLAlchemy
from config import DATA_BASE_CONNECTION_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATA_BASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(address, url_prefix='/address')
