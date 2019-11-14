from flask_wtf import FlaskForm
from wtforms import StringField, validators

class BoatForm(FlaskForm):
    name = StringField("Boat name", [validators.Length(min=1)])
 
    class Meta:
        csrf = False