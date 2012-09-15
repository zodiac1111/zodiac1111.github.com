---
layout: post
title: "使用octopress一些错误和解决方式"
date: 2012-09-15 19:21
comments: true
categories: [octopress]
---
#生成错误
错误现象类似这样:
{% codeblock %}
/home/use1/.gem/ruby/1.9.1/gems/maruku-0.6.0/lib/maruku/input/parse_doc.rb:22:in `<top (required)>': iconv will be deprecated in the future, use String#encode instead.
Configuration from /home/use1/blog/octopress/_config.yml
Building site: source -> public
/usr/share/ruby/psych.rb:203:in `parse': (<unknown>): found unexpected end of stream while scanning a quoted scalar at line 3 column 8 (Psych::SyntaxError)
	from /usr/share/ruby/psych.rb:203:in `parse_stream'
	from /usr/share/ruby/psych.rb:151:in `parse'
	from /usr/share/ruby/psych.rb:127:in `load'
	from /home/use1/.gem/ruby/1.9.1/gems/jekyll-0.11.2/lib/jekyll/convertible.rb:33:in `read_yaml'
	from /home/use1/.gem/ruby/1.9.1/gems/jekyll-0.11.2/lib/jekyll/post.rb:39:in `initialize'
	from /home/use1/blog/octopress/plugins/preview_unpublished.rb:23:in `new'
	from /home/use1/blog/octopress/plugins/preview_unpublished.rb:23:in `block in read_posts'
	from /home/use1/blog/octopress/plugins/preview_unpublished.rb:21:in `each'
	from /home/use1/blog/octopress/plugins/preview_unpublished.rb:21:in `read_posts'
	from /home/use1/.gem/ruby/1.9.1/gems/jekyll-0.11.2/lib/jekyll/site.rb:128:in `read_directories'
	from /home/use1/.gem/ruby/1.9.1/gems/jekyll-0.11.2/lib/jekyll/site.rb:98:in `read'
	from /home/use1/.gem/ruby/1.9.1/gems/jekyll-0.11.2/lib/jekyll/site.rb:38:in `process'
	from /home/use1/.gem/ruby/1.9.1/gems/jekyll-0.11.2/bin/jekyll:250:in `<top (required)>'
	from /home/use1/bin/jekyll:23:in `load'
	from /home/use1/bin/jekyll:23:in `<main>'
{% endcodeblock %}
<!-- more -->
造成以上错误的原因很多,多数是修改博客文章属性(如果不是修改博客框架代码的话)失误造成的,下面就是的错误的范例:
{% codeblock %}
---
layout: post
title: "my title
date: 2012-09-15 19:21
comments: true
categories:[tag1],[tag2]
---
{% endcodeblock %}
1. title 一栏的值应为 `"my title"` ,少了个引号
2. categories 一栏的写法应该为 `[tag1,tag2]` .
3. categories一栏的冒号后面应该空一格,像这样: `categories: [tag1,tag2]`

是需要眼睛足够"雪亮"啊.

###参考
1. [blog.micronarrativ.org](http://blog.micronarrativ.org/blog/2012/09/07/wordpress-til-octopress)
2. [cnblogs.com](http://www.cnblogs.com/heart-runner/archive/2012/02/14/2351136.html)


#关于Codeblock代码高亮
现象:
{% codeblock %}
/home/use1/.gem/ruby/1.9.1/gems/ffi-1.0.11/lib/ffi/library.rb:121:in `block in ffi_lib': Could not open library 'lib.so': lib.so: cannot open shared object file: No such file or directory (LoadError)
........
{% endcodeblock %}
看说明貌似是某个库没有.因为这种代码高亮是在本地将语法通过一些程序直接生成再上传到网上的,而高亮程序需要这个库.在fedora上直接`yum install python-devel`安装这个软件包即可解决.

###参考:
1. [github.com/tmm1/pygments.rb/issues](https://github.com/tmm1/pygments.rb/issues/10)


