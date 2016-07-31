# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 18:08:16

from flask import Blueprint, render_template, redirect, url_for
from ..models import Blog
main = Blueprint('main', __name__)


# 网页翻页信息类
class Page(object):

    def __init__(self, item_count, index=1, size=10):
        self.last = item_count // size + (1 if item_count % size > 0 else 0)  # 尾页
        self.index = min(index, self.last) if item_count > 0 else 1           # 当前页
        self.offset = size * (index - 1)    # 数据库查询用，偏移N个元素
        self.limit = size


@main.route('/')
def index():
    return redirect(url_for('.test'))


@main.route('/test')
def test():
    return render_template('test.html')


@main.route('/bootstrap')
def bootstrap():
    blogs = Blog.query.all()
    return render_template('bootstrap-blogs.html', page=Page(18), blogs=blogs)
