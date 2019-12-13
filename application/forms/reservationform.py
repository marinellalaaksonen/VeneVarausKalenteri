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

    # def validate_starting_date(form, field):
    #     if field is None:
    #         raise ValidationError("Starting date should be within one year from now")

    # def validate_ending_date(form, field):
    #     if not field:
    #         raise ValidationError("Ending date should be within one year from now")

    # def validate_starting_time(form, field):
    #     starting = datetime.combine(form.starting_date.data, form.starting_time.data)
    #     if starting < datetime.now():
    #         raise ValidationError("Starting time should be in the future")

    # def validate_ending_time(form, field):
    #     starting = datetime.combine(form.starting_date.data, form.starting_time.data)
    #     ending = datetime.combine(form.ending_date.data, form.ending_time.data)

    #     if starting >= ending:
    #         raise ValidationError("Ending date or time should be after starting time")

    #     if ending >= datetime.now() + timedelta(days = 365):
    #         raise ValidationError("Ending time should be within one year from now")
        
    class Meta:
        csrf = False