# -*- coding: UTF-8 -*-

from flask import render_template

from . import main
from flask_login import current_user, login_required

__author__ = 'lpe234'


@main.route('/')
@login_required
def index():
    user = current_user
    return render_template('index.html', user=user)
