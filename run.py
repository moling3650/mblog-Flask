# -*- coding: utf-8 -*-
# @Author: moling
# @Date:   2016-07-28 16:35:35


from app import create_app

if __name__ == '__main__':
    app = create_app('development')
    app.run()
