#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-30 14:23:19
# @Author  : moling (365024424@qq.com)
# @Link    : http://qiangtaoli.com
import hashlib
import time
import uuid
from flask import current_app
from app import db


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(50), nullable=False, primary_key=True, default=next_id)
    email = db.Column(db.String(50), nullable=False, unique=True, index=True)
    password = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    name = db.Column(db.String(50), nullable=False, unique=True, index=True)
    image = db.Column(db.String(500), nullable=False, default='/static/img/user.jpg')
    created_at = db.Column(db.Float, nullable=False, default=time.time)

    def to_json(self):
        json_user = self.__dict__.copy()
        json_user['password'] = '******'
        json_user.pop('_sa_instance_state')
        return json_user

    @classmethod
    def find_by_cookie(cls, cookie):
        if not cookie:
            return None
        try:
            L = cookie.split('-')
            if len(L) != 3:
                return None
            uid, expires, sha1 = L
            if int(expires) < time.time():
                return None
            user = cls.query.get(uid)
            if user is None:
                return None
            s = '%s-%s-%s-%s' % (uid, user.password, expires, current_app.config['COOKIE_KEY'])
            if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
                return None
            user.passwd = '******'
            return user
        except:
            return None

    def signin(self, response, max_age=86400):
        expires = str(int(time.time() + max_age))
        s = '%s-%s-%s-%s' % (self.id, self.password, expires, current_app.config['COOKIE_KEY'])
        L = [self.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
        response.set_cookie(current_app.config['COOKIE_NAME'], '-'.join(L), max_age, httponly=True)
        return response

    @classmethod
    def signout(cls, response):
        response.set_cookie(current_app.config['COOKIE_NAME'], '-deleted-', max_age=0, httponly=True)
        return response


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.String(50), nullable=False, primary_key=True, default=next_id)
    user_id = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_image = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    summary = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.Float, nullable=False, default=time.time)

    def to_json(self):
        json_blog = self.__dict__.copy()
        json_blog.pop('_sa_instance_state')
        return json_blog


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.String(50), nullable=False, primary_key=True, default=next_id)
    blog_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_image = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.Float, nullable=False, default=time.time)

    def to_json(self):
        json_comment = self.__dict__.copy()
        json_comment.pop('_sa_instance_state')
        return json_comment
