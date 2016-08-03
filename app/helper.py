#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-01 00:16:00
# @Author  : moling (365024424@qq.com)
# @Link    : http://qiangtaoli.com
# @Version : $Id$
from flask import abort


# 网页翻页信息类
class Paginate(object):

    def __init__(self, item_count, index=1, size=10):
        self.last = item_count // size + (1 if item_count % size > 0 else 0)  # 尾页
        self.index = min(index, self.last) if item_count > 0 else 1           # 当前页
        self.offset = size * (index - 1)    # 数据库查询用，偏移N个元素
        self.limit = size                   # 一页有N个元素


def set_positive_int(num_str, default=1):
    try:
        num = int(num_str)
    except:
        return default
    return num if num > 0 else default


def check_admin(user):
    if user is None or not user.admin:
        abort(403, 'current user must be admin')


def check_string(**kw):
    for key, string in kw.items():
        if not string or not string.strip():
            abort(400, '%s cannot be empty.' % key)
