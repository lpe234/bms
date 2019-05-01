# -*- coding: UTF-8 -*-

from datetime import timedelta

__author__ = 'lpe234'


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''
    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite://memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TABLE_PREFIX = 'bms_'
    # cookie
    REMEMBER_COOKIE_DURATION = timedelta(days=7)


class ProductionConfig(Config):
    """
    Production Config
    """
    pass


class DevelopmentConfig(Config):
    """
    Development Config
    """
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Tyk?NmaWa6hZB,GdCga2zE'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bms'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
