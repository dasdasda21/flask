import wtforms
from flask_wtf import Form
from wtforms import validators
class TaskForm(Form):
    name = wtforms.StringField(
        render_kw={
            "class": "form-control",
            "placeholder":"任务名称"
        }
    )
    description = wtforms.TextField(
        render_kw={
            "class":"form-control",
            "placehoder":"任务描述"
        }
    )
    time = wtforms.DateField(
        render_kw={
            "class":"form-control",
            "placeholder":"任务时间"
        }
    )
    public = wtforms.StringField(
        render_kw={
            "class":"form-control",
            "placeholder":"公布任务人"
        }
    )
