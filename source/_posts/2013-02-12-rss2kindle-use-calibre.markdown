---
layout: post
title: "利用calibre推送RSS源到Kindle"
date: 2013-02-12 10:36
comments: true
categories: 
---
#抓取RSS fatch news

##安装calibre

[calibre](http://calibre-ebook.com/)是一款强大的软件,可以下载/转换/编辑/管理kindle上的电子书.

##编辑.recipeRSS源


##抓取RSS(转换格式)

都在命令行在操作,方便部署到远程主机.
[文档](http://manual.calibre-ebook.com/cli/ebook-convert.html)

	ebook-convert  <RSS源文件>.recipe   <转换后文件名>.pobi  --test --username <谷歌账号>@gmail.com --password "<谷歌密码>" >> converrt.log


#编辑修改(可选)
#推送到Kindle
[calibre-smtp使用文档](http://manual.calibre-ebook.com/cli/calibre-smtp.html)

	calibre-smtp --attachment news.mobi --relay smtp.gmail.com --port 587 --username <谷歌账号>@gmail.com --password "<谷歌密码>" --encryption-method TLS <账号>@gmail.com <kindle推送地址>@kindle.com "<邮件正文>" -v -s "<邮件主题>" >> stmp.log
#定时推送

	crontab -e
	0 0 * * * 

