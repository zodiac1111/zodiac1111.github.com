---
layout: post
title: "使rake自动补全task"
date: 2012-09-19 21:07
comments: true
categories: [rake,completion]
---
在使用octopress写文章时有些命令记不太全,如`  new_post["title"]`,`rake generate`,`rake preview`,`rake deploy`,`rake gen_deploy`.那么想到既然make可以自动补全目标(target),那么rake应该也可以有这样的功能吧.于是在git找到了下面这个项目:

rake-completion 网址:<https://github.com/ai/rake-completion>

##安装
安装也能简单,如README所示:

> other unix-like:

	#复制`rake`文件到`/etc/bash_completion.d/`目录下:
	su -c 'cp ./rake /etc/bash_completion.d/'

##使用
 需要补全的时候按`Tab`键就好啦~

```
[user1@localhost octopress]$ rake <Tab>
clean                     isolate[filename]         set_root_dir[dir]
copydot[source,dest]      list                      setup_github_pages[repo]
deploy                    new_page[filename]        update_source[theme]
gen_deploy                new_post[title]           update_style[theme]
generate                  preview                   watch
install[theme]            push
integrate                 rsync
```
