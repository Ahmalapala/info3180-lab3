from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import Email, DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], description= "Enter your full name.")
    email = EmailField('Email', validators= [DataRequired(), Email()], description= "Enter your email address.")
    subject = StringField('Subject', validators= [DataRequired()], description= "Enter the subject for your message.")
    text = TextAreaField('Message', validators= [DataRequired()], description= "Enter the message you wish to send.")
