# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 23:39:14

from flask import abort, Blueprint, g, jsonify, request
from app import db
from ..models import User, Blog, Comment
from ..helper import Paginate, set_positive_int, check_admin, check_string


api = Blueprint('api', __name__, url_prefix='/api')

TABLES = dict(users=User, blogs=Blog, comments=Comment)


# 取（用户、博客、评论）表中一页的元素
@api.route('/<tablename>')
def api_get_items(tablename):
    table = TABLES[tablename]
    page = set_positive_int(request.args.get('page'))
    size = set_positive_int(request.args.get('size'), 10)
    item_count = table.query.count()
    p = Paginate(item_count, page, size)
    items = table.query.order_by(table.created_at.desc())\
                       .offset(p.offset).limit(p.limit + item_count % p.limit).all()
    return jsonify(items=[item.to_json() for item in items], page=p.__dict__)


# 取（用户、博客、评论）表中一个元素
@api.route('/<tablename>/<id>')
def api_get_item(tablename, id):
    return jsonify(TABLES[tablename].query.get_or_404(id).to_json())


# 取某篇博客的所有评论
@api.route('/blogs/<id>/comments')
def api_get_blog_comments(id):
    comments = Comment.query.filter_by(blog_id=id).order_by(Comment.created_at.desc()).all()
    return jsonify(comments=[c.to_json(marked=True) for c in comments])


# 创建新博客
@api.route('/blogs', methods=['POST'])
def api_create_blog():
    # 检查用户是否管理员，以及表单所有内容不为空
    check_admin(g.__user__)
    name = request.json.get('name')
    summary = request.json.get('summary')
    content = request.json.get('content')
    check_string(name=name, summary=summary, content=content)
    # 将博客存入数据库
    blog = Blog(
        user_id=g.__user__.get('id'),
        user_name=g.__user__.get('name'),
        user_image=g.__user__.get('image'),
        name=name.strip(),
        summary=summary.strip(),
        content=content.lstrip('\n').rstrip()
    )
    return jsonify(id=blog.id)


# 修改某篇博客
@api.route('/blogs/<id>', methods=['POST'])
def api_edit_blog(id):
    # 检查用户是否管理员，以及表单所有内容不为空
    check_admin(g.__user__)
    name = request.json.get('name')
    summary = request.json.get('summary')
    content = request.json.get('content')
    check_string(name=name, summary=summary, content=content)
    # 修改博客的信息后存入数据库
    blog = Blog.query.get_or_404(id)
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.lstrip('\n').rstrip()
    return jsonify(id=id)


# 创建新评论
@api.route('/blogs/<blog_id>/comments', methods=['POST'])
def api_create_comment(blog_id):
    # 检查用户和评论内容，以及博客id是否正确
    if g.__user__ is None:
        abort(403, 'Please signin first.')
    content = request.json.get('content')
    check_string(content=content)
    blog = Blog.query.get_or_404(blog_id)
    # 将评论存入数据库
    Comment(
        blog_id=blog.id,
        user_id=g.__user__.get('id'),
        user_name=g.__user__.get('name'),
        user_image=g.__user__.get('image'),
        content=content.lstrip('\n').rstrip()
    )
    # 查询数据库中所有比原页面更新的评论，markdown化返回结果
    time = request.json.get('time', 0)
    comments = Comment.query.filter(Comment.blog_id == blog_id and Comment.created_at > time)\
                            .order_by(Comment.created_at.desc()).all()
    return jsonify(comments=[c.to_json(marked=True) for c in comments])


# 删除表中的元素
@api.route('/<tablename>/<id>/delete', methods=['POST'])
def api_delete_item(tablename, id):
    check_admin(g.__user__)
    # 删除表中一个元素
    item = TABLES[tablename].query.get_or_404(id)
    db.session.delete(item)
    # 如果是Blog表的话，也把此博客的全部评论都删除
    if tablename == 'blogs':
        comments = Comment.query.filter_by(blog_id=id).all()
        for c in comments:
            db.session.delete(c)
    return jsonify(id=id)
