#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-02 19:56:51
# @Author  : moling (365024424@qq.com)
# @Link    : http://qiangtaoli.com
# @Version : $Id$

from flask import abort, Blueprint, redirect, request, jsonify, url_for
from ..models import User
from ..helper import check_string, check_email_and_password


auth = Blueprint('auth', __name__)


# 注册新用户
@auth.route('/register', methods=['POST'])
def register():
    # 检查用户名
    name = request.json.get('name')
    check_string(name=name)
    # 检查邮箱和密码的格式
    email = request.json.get('email')
    sha1_pw = request.json.get('sha1_pw')
    check_email_and_password(email, sha1_pw)
    # 检查邮箱是否已占用
    if User.query.filter_by(email=email).count():
        abort(400, 'email: used')
    # 注册成功
    user = User(name=name.strip(), email=email, password=sha1_pw)
    return user.signin(jsonify(user=user.to_json()))


# 登陆验证
@auth.route('/authenticate', methods=['POST'])
def authenticate():
    # 检查邮箱和密码的格式
    email = request.json.get('email')
    sha1_pw = request.json.get('sha1_pw')
    check_email_and_password(email, sha1_pw)
    # 验证密码是否正确
    user = User.query.filter_by(email=email).first_or_404()
    if not user.verify_password(sha1_pw):
        return abort(400, 'Invaild password')
    return user.signin(jsonify(user=user.to_json()))


# 注销用户
@auth.route('/signout')
def signout():
    return User.signout(redirect(request.referrer or url_for('main.index')))
