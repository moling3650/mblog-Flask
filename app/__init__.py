# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-07-28 08:38:36
# @Last Modified by:   anchen
# @Last Modified time: 2016-07-28 08:45:57

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)