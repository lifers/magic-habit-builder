from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, FieldList, FormField
from wtforms.validators import DataRequired
from typing import Optional


class ThreeBoxForm(FlaskForm):
    box1: Optional[StringField]
    box2: Optional[StringField]
    box3: Optional[StringField]

    box1 = StringField('', validators=[DataRequired()], render_kw={'placeholder': 'e.g. Run 5 km a day'})
    box2 = StringField('', validators=[DataRequired()], render_kw={'placeholder': 'e.g. Saving 5$ everyday'})
    box3 = StringField('', validators=[DataRequired()], render_kw={'placeholder': 'e.g. Apply for a job everyday'})
    date = TimeField()
    submit = SubmitField('Let\'s get started!')


class IntervalForm(FlaskForm):
    begin = TimeField(label="begin", validators=[DataRequired()])
    end = TimeField(label="end", validators=[DataRequired()])


class BlockTimeForm(FlaskForm):
    fields = FieldList(FormField(IntervalForm), min_entries=3, max_entries=3)
    submit = SubmitField('Next')
