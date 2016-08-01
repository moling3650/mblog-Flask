# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 18:08:16
from flask import Blueprint, render_template, redirect, request, url_for
from ..models import Blog
from ..helper import Paginate, set_positive_int

main = Blueprint('main', __name__)


# 跳转到模板首页
@main.route('/')
def index():
    return redirect(url_for('.show_blogs', template='bootstrap'))


# 模板首页
@main.route('/<template>/')
def show_blogs(template):
    page = set_positive_int(request.args.get('page'))
    size = set_positive_int(request.args.get('size'), 10)
    p = Paginate(Blog.query.count(), page, size)
    blogs = Blog.query.order_by(Blog.created_at.desc()).offset(p.offset).limit(p.limit).all()
    return render_template('%s-blogs.html' % template, page=p, blogs=blogs)


# 注册页面
@main.route('/<template>/register')
def register(template):
    return render_template('%s-register.html' % template)


# 登陆页面
@main.route('/<template>/signin')
def signin(template):
    return render_template('%s-signin.html' % (template))


# 博客页面
@main.route('/<template>/blog/<id>')
def show_blog(template, id):
    return render_template('%s-blog.html' % template, blog=Blog.query.get(id))


# @main.route('/<template>/manage')
# def manage(template):
#     redirect(url_for('.manage_table', template=template, tablename='blogs'))


# @main.route('/<template>/manage/<tablename>')
# def manage_table(template, tablename):
#     return render_template('%s-manage.html' % (template), table=tablename)
