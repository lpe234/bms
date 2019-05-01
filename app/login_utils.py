# -*- coding: UTF-8 -*-

from flask_login import LoginManager

from app.models import User

__author__ = 'lpe234'


login_manager = LoginManager()


# login url
login_manager.login_view = "main.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@login_manager.request_loader
def load_user_from_request(request):
    token = request.headers.get('Authorization')
    if token:
        # todo: find user by token.
        # fake user
        if token == 'bms12345':
            return User('FakeUser', 'fake@fake.com', 'fakepwd')
    return None

