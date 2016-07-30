# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 23:39:14

from flask import Blueprint, jsonify
from ..models import User

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test')
def test():
    return jsonify({
        'test': 'success'
    })


@api.route('/users')
def api_get_users():
    users = User.query.all()
    return jsonify(users=[user.to_json() for user in users])
