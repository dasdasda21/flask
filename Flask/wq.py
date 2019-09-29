import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True
app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] =True

models = SQLAlchemy(app)
class Curriculum(models.Model):
    __tablename__ ="curriculum"
    id = models.Column(models.Integer,primary_key = True)
    c_id =models.Column(models.String(32))
    c_name = models.Column(models.String(32))
    c_time = models.Column(models.Date)

models.create_all()

import datetime
session = models.session()
# c1 = Curriculum(c_id = "0002",c_name="html",c_time=datetime.datetime.now())
# c2 = Curriculum(c_id = "0003",c_name="mysql",c_time=datetime.datetime.now())
# c3 = Curriculum(c_id = "0004",c_name="linux",c_time=datetime.datetime.now())
# session.add_all([c1,c2,c3])
# session.commit()

f_c =Curriculum.query.get(2)
print(f_c)
session.delete(f_c)
session.commit()
