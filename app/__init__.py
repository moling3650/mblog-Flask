# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 08:38:36
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.filters import datetime_filter, marked_filter

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    app.jinja_env.filters.update(datetime=datetime_filter, marked=marked_filter)

    from app.middleware import logined_user
    app.before_request_funcs.setdefault(None, []).append(logined_user)

    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from app.routes.api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
