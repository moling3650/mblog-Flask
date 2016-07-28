# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 08:38:36


from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
