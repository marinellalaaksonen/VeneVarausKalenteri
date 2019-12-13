from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, ValidationError
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField
from datetime import datetime, timedelta

class ReservationForm(FlaskForm):
    starting_date = DateField("Starting date", [validators.InputRequired(
            message = "Please enter a valid starting date, starting date should be within one year from now")])
    starting_time = TimeField("Starting time", [validators.InputRequired()])
    ending_date = DateField("Ending date", [validators.InputRequired(
            message = "Please enter a valid ending date, starting date should be within one year from now")])
    ending_time = TimeField("Ending time", [validators.InputRequired()])
    boats = IntegerField("Number of boats")
        
    class Meta:
        csrf = False