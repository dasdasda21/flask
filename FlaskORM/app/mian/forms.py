import wtforms
from flask_wtf import FlaskForm
from wtforms import validators

from wtforms import ValidationError

def keywords_valid(form,field):
    data = field.data
    keywords = ["admin","GM","管理员","版主"]
    if data in keywords:
        raise ValidationError("敏感词no")
class TaskForm(FlaskForm):
    name = wtforms.StringField(label="name",
                               render_kw={
                                   "class":"form-control",
                                   "placeholder":"任务名称"
                               },
                               validators=[
                                   validators.DataRequired("姓名不可以为空"),
                                   keywords_valid
                               ])
    description = wtforms.TextField(
        label= "description",
        render_kw= {
            "class": "form-control",
            "placeholder":"任务描述"
        },
        validators = [
            validators.EqualTo("name")
        ]
    )
    time = wtforms.DateField(
        label="time",
        render_kw={
            "class":"form-control",
            "placeholder":"任务时间"
        }
    )
    public = wtforms.StringField(
        label= "public",
        render_kw={
            "class":"form-control",
            "placeholder":"公布任务人"
        }
    )