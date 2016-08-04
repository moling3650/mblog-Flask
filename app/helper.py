#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-01 00:16:00
# @Author  : moling (365024424@qq.com)
# @Link    : http://qiangtaoli.com
# @Version : $Id$
import re
from flask import abort

_RE_EMAIL = re.compile(r'^[a-zA-Z0-9\.\-\_]+\@[a-zA-Z0-9\-\_]+(\.[a-zA-Z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


# 网页翻页信息类
class Paginate(object):

    def __init__(self, item_count, index=1, size=10):
        self.last = item_count // size + (1 if item_count % size > 0 else 0)  # 尾页
        self.index = min(index, self.last) if item_count > 0 else 1           # 当前页
        self.offset = size * (index - 1)    # 数据库查询用，偏移N个元素
        self.limit = size                   # 一页有N个元素


# 设置一个正整数
def set_positive_int(num_str, default=1):
    try:
        num = int(num_str)
    except:
        return default
    return num if num > 0 else default


# 检查用户是否管理员
def check_admin(user):
    if user is None or not user.get('admin'):
        abort(403, 'current user must be admin')


# 检查字符串是否为空
def check_string(**kw):
    for key, string in kw.items():
        if not string or not string.strip():
            abort(400, '%s cannot be empty.' % key)


# 检查邮箱和密码的格式是否合法
def check_email_and_password(email, password):
    if not email or not _RE_EMAIL.match(email):
        abort(400, 'Invalid email')
    if not password or not _RE_SHA1.match(password):
        abort(400, 'Invalid password')
