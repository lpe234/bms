# -*- coding: UTF-8 -*-

from flask_script import Manager

from app import bms_app
from app.models import db

__author__ = 'lpe234'


manager = Manager(bms_app)


@manager.command
def create_all():
    """
    create all database tables.
    """
    db.create_all()


@manager.command
def drop_all():
    """
    Drop all databases tables.
    """
    db.drop_all()


if __name__ == '__main__':
    manager.run()
