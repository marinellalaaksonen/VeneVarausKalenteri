from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///venevarauskalenteri.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application.routes import home
from application.models import boats
from application.routes import boats

db.create_all()