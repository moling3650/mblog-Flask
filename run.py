# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-07-28 16:35:35
# @Last Modified by:   anchen
# @Last Modified time: 2016-07-28 16:37:09

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
