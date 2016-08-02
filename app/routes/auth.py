#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-02 19:56:51
# @Author  : moling (365024424@qq.com)
# @Link    : http://qiangtaoli.com
# @Version : $Id$

from flask import Blueprint, redirect, request, jsonify, url_for
from app import db
from ..models import User
auth = Blueprint('auth', __name__)


# 注册新用户
@auth.route('/register', methods=['POST'])
def register():
    name = request.json.get('name')
    email = request.json.get('email')
    sha1_pw = request.json.get('sha1_pw')
    user = User(name=name, email=email, password=sha1_pw)
    db.session.add(user)
    db.session.commit()
    return user.signin(jsonify(user=user.to_json()))


# 登陆验证
@auth.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.json.get('email')
    # sha1_pw = request.json.get('sha1_pw')
    user = User.query.filter_by(email=email).first()
    return user.signin(jsonify(user=user.to_json()))


# 注销用户
@auth.route('/signout')
def signout():
    return User.signout(redirect(request.referrer or url_for('main.index')))
