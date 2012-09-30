---
layout: post
title: "编译 goldendict 笔记"
date: 2012-09-29 22:30
comments: true
categories: [linux,goldendict]
---
官网:<http://goldendict.org/>.

官方编译介绍:<http://goldendict.org/buildfromgit.php>.

在Fedora 17上编译可能出现的一些小问题:

**1.**`articleview.hh:7:20: 致命错误：QWebView：没有那个文件或目录`

缺少qt的某个东西的头文件,安装即可:`yum install qtwebkit-devel`

**2.**`hotkeywrapper.hh:11:35: 致命错误：X11/extensions/record.h：没有那个文件或目录`

缺少X11开发用的头文件,安装:`yum install libXtst-devel`

**3.**`articleview.cc:37:32:致命错误：phonon/audiooutput.h：没有那个文件或phonon-devel.i686目录`

安装:`yum install phonon-devel`

**4.**`decompress.cc:5:19: 致命错误：bzlib.h：没有那个文件或目录`

安装:`yum install bzip2-devel`

**5.**安装到应用程序目录

执行完`make`之后可以执行` su -c 'make install' `将图标等复制到特定的目录中.

##goldendict词典下载
星际译王词典:<http://abloz.com/huzheng/stardict-dic>
