#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-15 10:00:00
# @Author  : moling (365024424@qq.com)
# @Link    : http://www.qiangtaoli.com
# @Version : $Id$
from flask import current_app, g, request
from app.models import User


def logined_user():
    cookie = request.cookies.get(current_app.config['COOKIE_NAME'])
    g.__user__ = User.find_by_cookie(cookie)
