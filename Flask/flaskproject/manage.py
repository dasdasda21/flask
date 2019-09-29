import sys
import os
from models import models
from views import app
from flask_script import Manager
manage = Manager(app)
@manage.command
def hello():
    print("hello")
@manage.command
def migrate():
    print("hello")
    models.create_all()
if __name__ == "__main__":
    manage.run()  # 启动这个应用


# print(sys.argv)
# command = sys.argv[1]

# if command == "migrate":
#     models.create_all()
# elif command == "runserver":
#     app.run(host="127.0.0.1",port=8000,debug=True)

