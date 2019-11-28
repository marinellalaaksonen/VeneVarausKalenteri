from flask_wtf import FlaskForm
from wtforms import IntegerField, validators
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField

class ReservationForm(FlaskForm):
    starting_date = DateField("Starting date")
    starting_time = TimeField("Starting time")
    ending_date = DateField("Ending date")
    ending_time = TimeField("Ending time")
    boats = IntegerField("Number of boats")
 
    class Meta:
        csrf = False