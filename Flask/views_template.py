import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)


class Calendar:
    def __init__(self,month = "now"):
        self.result = []
        big_month = [1,3,5,7,8,10,12]
        small_month = [4,6,9,11]

        now = datetime.datetime.now()
        if month == "now":
            month = now.month
            first_data = datetime.datetime(now.year,now.month,1,0,0)


# if __name__ == "__main__":
#     app.run(host="127.0.0.1",port=8000,debug=True)

