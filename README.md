# mblog-Flask
mblog by Flask
此项目的前端部分是基于项目[mblog][0]，为了加深对后端框架的认识理解，决定用Flask框架改写[mbolg][0]项目的后端部分，前端部分尽可能保持一致。

### 更新日志
创建了更新日志，记录此项目的进展，预期一周内可以完成
[可以点击我查看更新日志][1]




[0]: https://github.com/moling3650/mblog
[1]: https://github.com/moling3650/mblog-Flask/blob/master/CHANGELOG.md

### 项目结构
> + app
  + routes:         所有的view functions，俗称的控制层
    + api.py: 模型层的api蓝图
    + auth.py: 用户验证的蓝图
    + main.py: 模板渲染的蓝图
  + static:         所有的静态文件
  + template:       所有的视图模板
  + \_\_init\_\_.py:    app构造器
  + filters.py:     过滤器，主要用于jinja2
  + helper.py:      辅助函数库
  + middleware.py: 中间件
  + models.py:     模型层，主要业务处理
+ config.py:   配置文件
+ run.py:      app运行器
