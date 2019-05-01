# -*- coding: UTF-8 -*-

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.declarative import declared_attr

from app import bms_app
from app.utils import password_encrypt, password_check


__author__ = 'lpe234'


db = SQLAlchemy(bms_app)


class IDModelMixin(object):
    id = db.Column(db.Integer, comment='ID', primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls):
        return '{}{}'.format(bms_app.config.get('TABLE_PREFIX'), cls.__name__.lower())

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return self.__repr__()


class BaseModel(IDModelMixin):
    create_at = db.Column(db.DateTime, comment='创建时间', default=sqlalchemy.func.now())
    update_at = db.Column(db.DateTime, comment='更新时间', default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now())
    remarks = db.Column(db.String(length=64), comment='备注')


class User(db.Model, BaseModel):
    username = db.Column(db.String(length=32), comment='用户名', nullable=False, unique=True)
    email = db.Column(db.String(length=32), comment='邮箱', nullable=False, unique=True)
    password_hash = db.Column(db.String(length=64), comment='密码', nullable=False)
    active = db.Column(db.Boolean, comment='是否有效')
    admin = db.Column(db.Boolean, comment='是否为管理员', default=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.active = False

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        if password:
            self.password_hash = password_encrypt(password.encode('utf-8'))

    def check_password(self, password):
        if not password:
            return False
        return password_check(password, self.password_hash.encode('utf-8'))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Book(db.Model, BaseModel):
    name = db.Column(db.String(length=64), comment='名称', nullable=False, index=True)
    cover_img = db.Column(db.String(length=128), comment='封面图')
    author = db.Column(db.String(length=64), comment='作者')
    publish = db.Column(db.String(length=64), comment='出版社')
    isbn = db.Column(db.String(length=64), comment='ISBN')
    brand = db.Column(db.String(length=64), comment='品牌')
    ename = db.Column(db.String(length=64), comment='英文名称')
    pubdate = db.Column(db.Date, comment='初版时间')








