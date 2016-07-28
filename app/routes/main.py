# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 18:08:16

from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('.test'))


@main.route('/test')
def test():
    return render_template('test.html')
