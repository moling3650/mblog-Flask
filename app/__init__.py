# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 08:38:36
from flask import Flask, g, request
from flask_sqlalchemy import SQLAlchemy
from app.filters import datetime_filter, marked_filter
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://moling:www-data@localhost/mblog'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'
    app.config['COOKIE_NAME'] = 'aweSession'
    app.config['COOKIE_KEY'] = 'MbLog'
    db.init_app(app)
    app.jinja_env.filters['datetime'] = datetime_filter
    app.jinja_env.filters['marked'] = marked_filter

    from app.models import User

    @app.before_request
    def before_request():
        g.__user__ = None
        cookie = request.cookies.get(app.config['COOKIE_NAME'])
        if cookie:
            user = User.find_by_cookie(cookie)
            if user:
                g.__user__ = user

    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from app.routes.api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
