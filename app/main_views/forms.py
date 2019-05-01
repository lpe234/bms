# -*- coding: UTF-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators

__author__ = 'lpe234'


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=2, max=32),
                                        validators.Regexp('[0-9a-zA-Z]+', message='Username can only use 0-9,a-z,A-Z')])
    email = StringField('Email', [validators.Email(),
                                  validators.Length(min=4, max=32)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Password Repeat')


class LoginForm(FlaskForm):
    account = StringField('Account', [validators.DataRequired(),
                                      validators.Length(min=2, max=32)])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    remember_me = BooleanField('Remember', validators=[validators.Optional()])

