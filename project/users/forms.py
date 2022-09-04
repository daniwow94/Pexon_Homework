from flask import flash
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from project.models import User


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=100)])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=40)])
    first_name = StringField('First_name', validators=[DataRequired(), Length(min=3, max=40)])
    last_name = StringField('Last_name', validators=[DataRequired(), Length(min=3, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            flash('Dieser Username existiert bereits. Bitte wähle einen anderen.')
            raise ValidationError('Dieser Username existiert bereits. Bitte wähle einen anderen.')



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CertificateForm(FlaskForm):
    certificate_name = StringField('Name der Zertifizierung', validators=[DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('Zertifizierung Hinzufügen')