from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
    test = StringField("Название теста", validators=[DataRequired()])
    name = StringField("Фамилия и имя", validators=[DataRequired()])
    end_date = StringField("Дата и время завершения теста", validators=[DataRequired()])
    time = StringField("Потрачено времени", validators=[DataRequired()])
    score = StringField("Максимальный балл", validators=[DataRequired()])
    submit = SubmitField("Получить")