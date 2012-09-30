---
layout: post
title: "使用 githubRepoWidget 展示 github 项目"
date: 2012-09-20 22:55
comments: true
categories: [otcopress,github,git,widget]
---
<script src="{{ root_url }}/javascripts/libs/jquery.min.js"></script>
<script type="text/javascript" src="{{ root_url }}/javascripts/libs/jquery.githubRepoWidget.min.js"></script>
使用githubRepoWidget在otcopress上展示项目的方法.

#先看效果:
例子1 Linux kernel:
<div class="github-widget" data-repo="torvalds/linux"></div>
例子2 githubRepoWidget:
<div class="github-widget" data-repo="JoelSutherland/GitHub-jQuery-Repo-Widget"></div>
<!-- more -->
#介绍:
项目地址在github上: <https://github.com/JoelSutherland/GitHub-jQuery-Repo-Widget>

###配置:
复制下载的`jquery.githubRepoWidget.min.js`到本地博客目录`octopress/source/javascripts/libs`下

###启用:

方式1:局部
{% codeblock lang:javascript %}
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
<script type="text/javascript" src="{{ root_url }}/javascripts/libs/jquery.githubRepoWidget.min.js"></script>
<div class="github-widget" data-repo="JoelSutherland/GitHub-jQuery-Repo-Widget"></div>
{% endcodeblock %}

* 优点:仅在使用widget的页面才加载jquery.min.js等文件.减少不必要的耦合.
* 缺点:引用时需要添加较多(三行)的代码.

方式2:全局

在`octopress/source/_includes/custom/head.html`或其他全局页面文件增加:
{% codeblock lang:javascript %}
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
<script type="text/javascript" src="{{ root_url }}/javascripts/libs/jquery.githubRepoWidget.min.js"></script>
{% endcodeblock %}

在需要展示项目时,这样添加:
{% codeblock lang:javascript %}
<div class="github-widget" data-repo="JoelSutherland/GitHub-jQuery-Repo-Widget"></div>
{% endcodeblock %}
`data-repo`项填写项目名称即可,如上例的`JoelSutherland/GitHub-jQuery-Repo-Widget`.

* 优点:引用方便,仅需一行代码.
* 缺点:在不需要显示widget的页面也会加载jquery.min.js等文件,浪费网络资源.  
修改otcopress项目的文件,可能会存在问题.
###其他:
暂无.

#资料:
1. 项目github:<https://github.com/JoelSutherland/GitHub-jQuery-Repo-Widget> 
2. OSCHINA 增加软件与 Github 的集成:<http://www.oschina.net/news/30679/oschina-projects-integration-with-github>

