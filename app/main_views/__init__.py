# -*- coding: UTF-8 -*-

from flask import Blueprint

__author__ = 'lpe234'


main = Blueprint('main', __name__)


from . import index, member
