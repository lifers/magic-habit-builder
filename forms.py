from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField
from wtforms.validators import DataRequired


class ThreeBoxForm(FlaskForm):
    box1 = StringField('One habit you want to have', validators=[DataRequired()])
    box2 = StringField('One habit you want to have', validators=[DataRequired()])
    box3 = StringField('One habit you want to have', validators=[DataRequired()])
    date = TimeField(validators=[DataRequired()])
    submit = SubmitField('Let\'s get started!')

