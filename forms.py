# Backend of the Form

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired

class SignupForm(Form):
    #first_name = StringField('First name', validators=[DataRequired("Please Enter your First Name")])
    #last_name = StringField('Last name', validators=[DataRequired("Please Enter your Last Name")])
    #email = StringField('Email', validators=[DataRequired("Please Enter your Email ID")])
    #password = PasswordField('Password', validators=[DataRequired("Please enter the correct password")])
    #submit = SubmitField('Sign Up')

    first_name = StringField('First name', [validators.Required("Please Enter your First Name"), validators.Length(min=4, max=25)])
    last_name = StringField('Last name', [validators.Required("Please Enter your Last Name")])
    email = StringField('Email', [validators.Required("Please Enter your Email ID"), validators.Email("Please enter a valid email address")])
    password = PasswordField('Password', [validators.Required("Please enter the correct password"), validators.Length(min=8, max=25)])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email', [validators.Required("Please Enter your Email ID"), validators.Email("Please enter a valid email address")])
    password = PasswordField('Password', [validators.Required("Please enter the correct password"), validators.Length(min=8, max=25)])
    submit = SubmitField('Sign In')
