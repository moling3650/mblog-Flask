#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-04 23:46:16
# @Author  : moling (365024424@qq.com)
# @Link    : http://qiangtaoli.com
# @Version : $Id$
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    JSONIFY_MIMETYPE = 'application/json;charset=utf-8'
    COOKIE_NAME = 'aweSession'
    COOKIE_KEY = 'MbLog'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://moling:www-data@localhost/mblog'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
