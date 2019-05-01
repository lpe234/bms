# -*- coding: UTF-8 -*-

import os

from flask import Flask, redirect, url_for

from app.config import DevelopmentConfig, ProductionConfig


__author__ = 'lpe234'


# create application
bms_app = Flask(__name__)

if os.environ.get('BMS_ENV') == 'PRODUCTION':
    bms_app.config.from_object(ProductionConfig)
else:
    bms_app.config.from_object(DevelopmentConfig)

# db
from app.models import db
db.init_app(bms_app)

# login
from app.login_utils import login_manager
login_manager.init_app(bms_app)

# main blueprint
from app.main_views import main
bms_app.register_blueprint(main, url_prefix='/main/')

# api blueprint
from app.api import api
bms_app.register_blueprint(api, url_prefix='/api/')


@bms_app.route('/')
def index():
    return redirect(url_for('main.index'))


if __name__ == '__main__':
    bms_app.run()
