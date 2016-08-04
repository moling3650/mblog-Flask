# 更新日志
### 2016.08.04
- 添加三个check函数，如有错误直接BAD_REQUEST
- 修复前端的ajax函数，使它可以获取flask的abort的报错信息
- 添加api
 - GET /api/<tablename>：取（用户、博客、评论）表中一页的元素
 - GET /api/<tablename>/<id>：取（用户、博客、评论）表中一个元素
 - POST /api/blogs：创建一个博客
 - POST /api//blogs/<id>：修改某篇博客
 - POST /api/blogs/<blog_id>/comments：创建新评论
 - POST /api/<tablename>/<id>/delete：删除表中的元素
- Comment类的to_json方法支持markdown正文
- User、Blog、Comment初始化时直接写入数据库
- User类添加验证密码的方法

### 2016.08.03
- 修复登陆bug，原来是flask的全局变量用错了，*g*是全局的，*request*却不是
- `User`类添加`signin`、`signout`、`find_by_cookie`的方法
- 添加`before_requesrt`装饰器，在每个请求前通过`User.find_by_cookie`获取到当前用户的信息
- 添加管理页面的route
- 添加查询某篇博客的api
  - GET /api/blogs/<id>：查询某篇博客


### 2016.08.02
- 实现简单的注册登陆功能，没加验证，有bug

### 2016.08.01
- 添加ORM的Comment模型
- 添加查询comments的api
  - GET /api/comments： 查询所有的comment
  - GET /api/blogs/\<blog_id\>/comments：查询某篇博客的所有comments
- 采用新的模式markdown博客，以前后台处理好再渲染，现在改成用jinja2的filter
- 基本实现首页和博客页面的搭建

### 2016.07.31
- 添加ORM的Blog模型
- 添加查询blogs的api
 - GET /api/blogs：查询所有的blogs
- 添加jinja2的filters
  - datetime_filter： 智能显示创建文章的时间
  - marked_filter：markdown文本，包括代码高亮
- 修复api的json显示，可以支持显示汉字，压缩容量

### 2016.07.30
- 添加ORM的User模型
- 添加查询users的api
  - GET /api/users：查询所有的users

### 2016.07.29
- 添加main、api蓝图

### 2016.07.28
- 创建项目
- 添加最简单的app
- 测试渲染模板
