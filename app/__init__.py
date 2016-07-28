# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-07-28 08:38:36
# @Last Modified by:   anchen

from flask import Flask


def index():
    return 'hello world'


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', view_func=index)

    return app
