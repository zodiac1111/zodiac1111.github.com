---
layout: post
title: "为feodra18设置主机名"
date: 2013-04-14 15:53
comments: true
categories: 
---
参考:<http://zurlinux.com/?p=1396> .
 
在`Fedora 18`中主机名已经保存在`/etc/hostname`文件中,而不是保存在`/etc/sysconfig/network`文件的`HOSTNAME=XXX`一行中.

There are now three distinguished hostnames in use with Fedora 18.

* A high-level pretty free-form hostname
* The static hostname, i.e. the kernel hostname
* Possibly a transient temporary hostname

`hostnamectl`命令/程序可以用户设定hostname.
	
`hostnamectl --help`查看具体用法.

`hostnamectl status`查看当前设置.

更多请参考来源.
