from flask import Flask
from flask import render_template
import datetime
#创建一个应用
app = Flask(__name__)

@app.route("/")
def index():  #视图
    return "hello world"
@app.route("/content/<username>/<int:age>")
def content(age,username,):
    return "hello,i am %s,i am %s yeas old"%(username,age)
@app.route("/days/")
def days():
    now = datetime.datetime.now()
    old = datetime.datetime(now.year,1,1,0,0,0)
    day = (now -old).days
    return str(day)
@app.route("/base/")
def base():
    return render_template("base.html",)
@app.route("/login/")
def login():
    return render_template("login.html")
@app.route("/user_info/")
def user_info():
    return render_template("/user_info.html/")


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)   #启动这个项目