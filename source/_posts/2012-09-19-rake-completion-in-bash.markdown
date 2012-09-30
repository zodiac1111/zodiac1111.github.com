---
layout: post
title: "rake 自动补全 task"
date: 2012-09-19 21:07
comments: true
categories: [rake,bash,completion]
---
在使用octopress写文章时有些命令记不太全,如`  new_post["title"]`,`rake generate`,`rake preview`,`rake deploy`,`rake gen_deploy`.

那么想到既然bash中make可以自动补全目标(target),那么rake应该也可以有这样的功能吧.  
于是在git找到了 rake-completion 这个项目:
<script src="{{ root_url }}/javascripts/libs/jquery.min.js"></script>
<div class="github-widget" data-repo="ai/rake-completion"></div>
网址:<https://github.com/ai/rake-completion>

##安装
安装也很简单,如`README`文件中`other unix-like`一节指示:

复制`rake`文件到`/etc/bash_completion.d/`目录下(需要root权限):
{% codeblock lang:bash %}
	su -c 'cp ./rake /etc/bash_completion.d/'
{% endcodeblock %}
##使用
 需要补全的时候按`Tab`键就好啦~

{% codeblock lang:bash %}
[user1@localhost octopress]$ rake <Tab>
clean                     isolate[filename]         set_root_dir[dir]
copydot[source,dest]      list                      setup_github_pages[repo]
deploy                    new_page[filename]        update_source[theme]
gen_deploy                new_post[title]           update_style[theme]
generate                  preview                   watch
install[theme]            push
integrate                 rsync
{% endcodeblock %}
