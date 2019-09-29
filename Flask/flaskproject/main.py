from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import pymysql
from flask_wtf import CSRFProtect
from blueprint01 import simple_1
from blueprint02 import simple_2
pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config.from_pyfile("settings.py")
models =SQLAlchemy(app)
csrf = CSRFProtect(app)
api = Api(app)
app.register_blueprint(simple_1)
app.register_blueprint(simple_2)
app.run()