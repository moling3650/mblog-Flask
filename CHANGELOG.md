# 更新日志

### 2016.08.01
- 添加ORM的Comment模型
- 添加查询comments的api
  - /api/comments： 查询所有的comment
  - /api/blogs/<blog_id>/comments：查询某篇博客的所有comments
- 采用新的模式markdown博客，以前后台处理好再渲染，现在改成用jinja2的filter
- 基本实现首页和博客页面的搭建

### 2016.07.31
- 添加ORM的Blog模型
- 添加查询blogs的api
 - /api/blogs
- 添加jinja2的filters
  - datetime_filter: 智能显示创建文章的时间
  - marked_filter：markdown文本，包括代码高亮
- 修复api的json显示，可以支持显示汉字，压缩容量

### 2016.07.30
- 添加ORM的User模型
- 添加查询users的api

### 2016.07.29
- 添加main、api蓝图

### 2016.07.28
- 创建项目
- 添加最简单的app
- 测试渲染模板
