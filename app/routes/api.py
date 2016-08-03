# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 23:39:14

from flask import Blueprint, jsonify, request
from ..models import User, Blog, Comment
from ..helper import Paginate, set_positive_int

api = Blueprint('api', __name__, url_prefix='/api')

TABLES = dict(users=User, blogs=Blog, comments=Comment)


@api.route('/test')
def test():
    return jsonify({
        'test': 'success'
    })


@api.route('/user')
def api_get_user():
    user = User.query.get("001462522483997f2b422e199124d698ddf1179a92cf986000")
    return jsonify(user=user.to_json())


# 取（用户、博客、评论）表的条目
@api.route('/<tablename>')
def api_get_items(tablename):
    table = TABLES[tablename]
    page = set_positive_int(request.args.get('page'))
    size = set_positive_int(request.args.get('size'), 10)
    item_count = table.query.count()
    p = Paginate(item_count, page, size)
    items = table.query.order_by(table.created_at.desc()).offset(p.offset).limit(p.limit).all()
    return jsonify(items=[item.to_json() for item in items], page=p.__dict__)


# 取某篇博客
@api.route('/blogs/<id>')
def api_get_blog(id):
    return jsonify(Blog.query.get_or_404(id).to_json())


# 取某篇博客的所有评论
@api.route('/blogs/<id>/comments')
def api_get_blog_comments(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    return jsonify(comments=[c.to_json() for c in comments])
