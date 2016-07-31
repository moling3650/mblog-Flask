#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-30 14:23:19
# @Author  : moling (365024424@qq.com)
# @Link    : http://qiangtaoli.com

import time
import uuid
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
