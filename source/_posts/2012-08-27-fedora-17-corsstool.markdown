---
layout: post
title: "fedora-17-corsstool"
date: 2012-08-27 11:15
comments: true
categories: 
---
##crosstool在fedora 17下的编译一到的问题/解决
>参考 http://blog.chinaunix.net/space.php?uid=20543672&do=blog&id=94268
问题:
###解决gcc: error trying to exec ‘cc1obj’: execvp: No such file or directory问题
obj-c的库问题,参看 >http://lok.me/a/1182.html 解决
主要`yum install gcc-objc gcc-objc++ libobjc`

###flat_bl.m:2:2: 错误：expected identifier or ‘(’ before ‘%’ token 
>http://forums.fedoraforum.org/archive/index.php/t-267449.html
Makefile 依赖*.m文件错误,删除.m文件,更改Makefile依赖关系

### These critical programs are missing or too old: gcc
/ Check the INSTALL file for required versions.
>http://lidu678.blog.163.com/blog/static/898060062010498571444/
修改`crosstool-0.43/patches/glibc-2.3.2/glibc-2.3.3-allow-gcc-4.0-configure.patch`
检查版本时gcc 4.7.0 过高, 在该文件中可以看出`4.[01]*`改为`|4.[017]*`使其通过检查

###make[2]: 进入目录“/home/zodiac1111/test/crosstool-0.43/build/arm-9tdmi-linux-gnu/gcc-4.1.0-glibc-2.3.2/glibc-2.3.2/manual”
Makefile:250: *** 混和的隐含和普通规则。 停止。
fedora make程序特有有的对混和目标的规则,如
目标1<空格>目标2:
(tab)命令
分解成为:
目标1:
(tab)命令
目标2:
(tab)命令 
即可.
参考 "fedora make 混和的隐含和普通规则" 
>http://blog.csdn.net/melong100/article/details/6238273
