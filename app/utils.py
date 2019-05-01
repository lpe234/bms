# -*- coding: UTF-8 -*-
from urllib.parse import urlparse, urljoin

import bcrypt
from flask import request

__author__ = 'lpe234'


def password_encrypt(password: str):
    """
    password hash
    :param password:
    :return:
    """
    return bcrypt.hashpw(password, bcrypt.gensalt())


def password_check(password_raw: str, password_hash: str):
    """
    password check
    :param password_raw:
    :param password_hash:
    :return:
    """
    return bcrypt.checkpw(password_raw, password_hash)


def is_safe_url(url):
    """
    check if the url is safe.
    :param url:
    :return:
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, url))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
