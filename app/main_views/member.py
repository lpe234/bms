# -*- coding: UTF-8 -*-

from flask import request, render_template, flash, redirect, url_for
from sqlalchemy import or_
from wtforms import ValidationError
from flask_login import login_user, logout_user

from app.main_views import main
from app.main_views.forms import RegisterForm, LoginForm
from app.models import User, db
from app.utils import is_safe_url

__author__ = 'lpe234'


@main.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('main/register.html', form=form)
    else:
        if form.validate_on_submit():
            user = User(form.username.data, form.email.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering.')
            return redirect(url_for('main.login'))
        return render_template('main/register.html', form=form)


@main.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('main/login.html', form=form)
    if form.validate_on_submit():
        user = User.query.filter(or_(User.username == form.account.data, User.email == form.account.data)).first()
        if user and user.check_password(form.password.data.encode('utf-8')):
            if not user.is_active:
                # todo:
                raise ValidationError('User is not active.')
            # login
            login_user(user, form.remember_me.data)
            # next
            next = request.args.get('next')
            if not is_safe_url(next):
                next = None
            return redirect(next or url_for('main.index'))
        # todo:
        raise ValidationError('User does not exist, or password is wrong.')
    return render_template('main/login.html', form=form)


@main.route('/logout/', methods=['GET', 'POST'])
def logout():
    # logout
    logout_user()
    return redirect(url_for('main.login'))
