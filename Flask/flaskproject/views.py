# import datetime
# from flask import render_template
# from main import app
# from models import *
# from flask import redirect
# class Calendar:
#     """
#     当前类实现日历功能
#     1、返回列表嵌套列表的日历
#     2、安装日历格式打印日历
#
#     # 如果一号周周一那么第一行1-7号   0
#         # 如果一号周周二那么第一行empty*1+1-6号  1
#         # 如果一号周周三那么第一行empty*2+1-5号  2
#         # 如果一号周周四那么第一行empty*3+1-4号  3
#         # 如果一号周周五那么第一行empyt*4+1-3号  4
#         # 如果一号周周六那么第一行empty*5+1-2号  5
#         # 如果一号周日那么第一行empty*6+1号   6
#         # 输入 1月
#         # 得到1月1号是周几
#         # [] 填充7个元素 索引0对应周一
#         # 返回列表
#         # day_range 1-30
#     """
#     def __init__(self,month = "now"):
#         self.result = []
#
#         big_month = [1, 3, 5, 7, 8, 10, 12]
#         small_month = [4, 6, 9, 11]
#
#         #获取当前月
#         now = datetime.datetime.now()
#         if month == "now":
#             month = now.month
#             first_date = datetime.datetime(now.year, now.month, 1, 0, 0)
#             # 年 月 日 时 分
#         else:
#             #assert int(month) in range(1,13)
#             first_date = datetime.datetime(now.year, month, 1, 0, 0)
#
#         if month in big_month:
#             day_range = range(1, 32)  # 指定月份的总天数
#         elif month in small_month:
#             day_range = range(1, 31)
#         else:
#             day_range = range(1, 29)
#
#         # 获取指定月天数
#         self.day_range = list(day_range)
#         first_week = first_date.weekday()  # 获取指定月1号是周几 6
#
#         line1 = []  # 第一行数据
#         for e in range(first_week):
#             line1.append("empty")
#         for d in range(7 - first_week):
#             line1.append(
#                 str(self.day_range.pop(0))+"—django开发"
#                          )
#         self.result.append(line1)
#         while self.day_range:  # 如果总天数列表有值，就接着循环
#             line = []  # 每个子列表
#             for i in range(7):
#                 if len(line) < 7 and self.day_range:
#                     line.append(str(self.day_range.pop(0))+"—django开发")
#                 else:
#                     line.append("empty")
#             self.result.append(line)
#     def return_month(self):
#         """
#         返回列表嵌套列表的日历
#         """
#         return self.result
#     def print_month(self):
#         """
#         安装日历格式打印日历
#         """
#         print("星期一  星期二  星期三  星期四  星期五  星期六  星期日")
#         for line in self.result:
#             for day in line:
#                 day = day.center(6)
#                 print(day, end="  ")
#             print()
# # @app.route("/")
# # # def index():
# # #     name = "laobian"
# # #     return render_template("index.html",**locals())
#
#
#
# @app.route("/base/")
# def base():
#     return render_template("base.html")
#
# @app.route("/index/")
# def exindex():
#     return render_template("ex_index.html")
# import time
# @app.route("/user_info/")
# def userinfo():
#     calendar = Calendar().return_month()
#     now = datetime.datetime.now()
#     return render_template("user_info.html",**locals())
# from flask import request
# from models import User
# @app.route("/register/",methods=["GET","POST"])
# def register():
#     if request.method == "POST":
#         username =request.form.get("username")
#         password = request.form.get("password")
#         email = request.form.get("email")
#         user =User()
#         user.user_name = username
#         user.password =password
#         user.email =email
#         user.save()
#     return render_template("register.html")
#
# @app.route("/login/",methods=["get","post"])
# def login():
#     error =""
#     if request.method == "POST":
#         form_data = request.form
#         email = form_data.get("email")
#         password = form_data.get("password")
#
#         user = User.query.filter_by(email = email).first()
#         if user:
#             db_password = user.password
#             if password ==db_password:
#                 response = redirect("/index/")
#                 response.set_cookie("username",user.user_name)
#                 response.set_cookie("email",user.email)
#                 response.set_cookie("id",str(user.id))
#                 return response
#             else:
#                 error = "密码错误"
#         else:
#             error = "用户名不存在"
#     return render_template("login.html",error = error)
#
# def loginValid(fun):
#     def inner(*args,**kwargs):
#         username = request.cookies.get("username")
#         id = request.cookies.get("id")
#         user = User.query.get(int(id))
#         if user.user_name == username:
#             return fun(*args,**kwargs)
#         else:
#             return redirect("/login/")
#     return inner
#
# @app.route("/logout/")
# def logout():
#     response = redirect("/login/")
#     response.delete_cookie("username")
#     response.delete_cookie("email")
#     response.delete_cookie("id")
#     return response
# @app.route("/holiday/",methods=["GET","POST"])
# def holiday():
#     if request.method == "POST":
#         data = request.form
#         request_user= data.get("request_user")
#         request_type = data.get("request_type")
#         start_time = data.get("start_time")
#         end_time = data.get("end_time")
#         phone = data.get("phone")
#         request_description = data.get("request_description")
#
#         leave = Leave()
#         leave.request_id = request.cookies.get("id")
#         leave.request_name = request_user
#         leave.request_type = request_type  # 假期类型
#         leave.request_start_time = start_time  # 起始时间
#         leave.request_end_time = end_time  # 结束时间
#         leave.request_description = request_description  # 请假事由
#         leave.request_phone = phone  # 联系方式
#         leave.request_status = "0"  # 假条状态
#         leave.save()
#         return redirect("/leave_list/")
#     return render_template("holiday.html")
# from page import *
# @app.route("/leave_list/<int:page>/")
# def leave_list(page):
#     leaves = Leave.query.all()
#     pager = Pager(leaves,2)
#     page_data = pager.page_data(page)
#     return render_template("leave_list.html",**locals())
#
# from form import *
# @app.route("/add_task/",methods=["GET","POST"])
# def add_task():
#     task = TaskForm
#     return render_template("add_task.html",**locals())
# from main import api
# from flask_restful import Resource
# @api.resource("/Api/leave/")
# class LeaveApi(Resource):
#     def __init__(self):
#         super(LeaveApi,self).__init__()
#         self.result = {
#             "version":"1.0",
#             "data":""
#         }
#     def set_data(self,leave):
#         result_data = {
#             "request_name":leave.request_name,
#             "request_type":leave.request_type,
#             "request_start_time":leave.request_start_time,
#             "request_end_time":leave.request_end_time,
#             "request_description":leave.request_description,
#             "request_phone":leave.request_phone
#         }
#         return result_data
#     def get(self):
#         deta = request.args
#         id = data.get("id")
#         if id:
#             leave = Leave.query.get(int(id))
#             result_data = self.set_data(leave)
#         else:
#             leaves = Leave.query.all()
#             result_data=[]
#             for leave in leaves:
#                 result_data.append(self.set_data(leave))
#         self.result["data"] = result_data
#         return self.result
#     def post(self):
#         data = request.form
#         return {"method":"post保存"}
#     def put(self):
#         data = request.form
#         return {"method":"put修改"}
#     def delete(self):
#         data = request.form
#         return {"method":"delete删除"}
#
# from main import csrf
# @app.route("/picture/",methods=["GET","POST"])
# @csrf.exempt
# def picture():
#     if request.method =="POST":
#         file = request.files.get("picture")
#         print([ i for i in dir(file) if not i.startswith("_")])
#     return render_template("picture.html")
#
#
#
#
#
# if __name__ == "__main__":
#     app.run(host="127.0.0.1" ,port=8000 ,debug=True)  # 启动这个应用

from flask import Flask
from flask import render_template

app = Flask(__name__)   #创建一个应运
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/content/<username>/<int:age>/")
def content(username,age):
    return "heelo,i am %s %s old"%(username,age)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)                      #启动应运