from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, ValidationError
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField
from datetime import datetime

class ReservationForm(FlaskForm):
    starting_date = DateField("Starting date")
    starting_time = TimeField("Starting time")
    ending_date = DateField("Ending date")
    ending_time = TimeField("Ending time")
    boats = IntegerField("Number of boats")

    def validate_ending_time(form, field):
        starting = datetime.combine(form.starting_date.data, form.starting_time.data)
        ending = datetime.combine(form.ending_date.data, form.ending_time.data)

        if starting >= ending:
            raise ValidationError("Ending date or time should be after starting time")
        
    class Meta:
        csrf = False