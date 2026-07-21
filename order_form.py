from flask_wtf import FlaskForm
from wtforms import DecimalField, DateField, SubmitField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')