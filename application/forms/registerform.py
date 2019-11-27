from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1, max=144)])
    username = StringField("Username", [validators.Length(min=1, max=144)])
    password = PasswordField("Password", [validators.Length(min=8, max=144),
                            validators.EqualTo("confirmpassword", message="Passwords must match")])
    confirmpassword = PasswordField("Repeat password", [validators.Length(min=8, max=144)])
    #email = StringField("Email")
  
    class Meta:
        csrf = False