# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 08:38:36


from flask import Flask, render_template


def index():
    return render_template('test.html')


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', view_func=index)

    return app
