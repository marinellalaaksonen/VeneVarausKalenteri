from flask_wtf import FlaskForm
from wtforms import DateTimeField, IntegerField, validators

class ReservationForm(FlaskForm):
    starting_time = DateTimeField("Starting time")
    ending_time = DateTimeField("Ending time")
    boats = IntegerField("Number of boats")

    # def validate(self):
    #     if not FlaskForm.validate(self):
    #         return False
    #     if self.ending_time.data < self.starting_time.data:
    #         self.ending_time.errors.append("Ending time should be after starting time")
    #         return False
    #     else:
    #         return True
        
 
    class Meta:
        csrf = False