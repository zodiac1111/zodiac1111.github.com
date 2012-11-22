---
layout: post
title: "Linux下avr单片机开发环境"
date: 2012-11-17 12:47
comments: true
categories: 
---
目前实现:

可以用过USBasp下载器**下载**到ATmega128a单片机中运行(厂商例程),
还未实现在线调试.

引用来源:见参考一节.

#前提:环境
##软件:
###开发平台Linux(kernel 3.6):
终端使用`uname -a`命令查看:
	Linux localhost.localdomain 3.6.3-1.fc17.i686.PAE #1 SMP Mon Oct 22 15:48:37 UTC 2012 i686 i686 i386 GNU/Linux

###Linux 发行版(Fedora)
终端使用`lsb_release -a`命令查看: 
	LSB Version:	:core-4.1-ia32:core-4.1-noarch:cxx-4.1-ia32:cxx-4.1-noarch:desktop-4.1-ia32:desktop-4.1-noarch:languages-4.1-ia32:languages-4.1-noarch:printing-4.1-ia32:printing-4.1-noarch
	Distributor ID:	Fedora
	Description:	Fedora release 17 (Beefy Miracle)
	Release:	17
	Codename:	BeefyMiracle

###IDE 平台:

	Eclipse Platform
	Version: 4.2.1
	Build id: M20120914-1800

###Eclipse 软件(插件)avr-eclipse:
	
	http://avr-eclipse.sourceforge.net

<!-- more -->

####下载软件:

#####Linux平台交叉编译avr程序交叉编译器:avr-gcc.
yum安装或者源代码编译
#####avr程序下载(烧写)软件:avrdude 
网址<http://savannah.nongnu.org/projects/avrdude/>


##硬件:
###下载器:

####USBasp,很早以前淘宝上买的[参考4]:

lsusb查看如下:

	Bus 003 Device 006: ID 16c0:05dc VOTI shared ID for use with libusb

这个好像只能下载(ISP).

####AVR-JTAG-USB仿真器,也是很久以前买的[参考8]:

lsusb识别是usb转串,应该就是这样吧 = = .

	Bus 003 Device 012: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port

除了下载功能以外,这个还能在线调试.

**以上两者任意一个都可以下载程序.**

###开发板:
	
一年多前淘宝买的开发板(ATmega128a)[参考5],原理图[参考6],扔那里也没怎么玩,最近来了兴致拿起来折腾折腾 :P .

#正文:搭建开发环境:在Linux在使用AVR-Eclipse中，AVR-GCC和AVRDUDE进行Atmel的AVR单片机开发.
[参考1]
##安装AVR-Eclipse
在Eclipse中单击帮助(Help)->安装新软件(Install New Sofrware),之后将打开一个对话框.在对话框的顶部 Work with 文本框中粘贴 AVR-Eclipse 更新服务器的地址 (<http://avr-eclipse.sourceforge.net/updatesite/>).如图:
[图:安装插件]
{% img /downloads/img/avr-eclipse-plug-in.png %}

安装好之后,点击窗口(Window)->首选项(Preferences)展开左边的AVR一栏.
[图:配置窗口]
{% img /downloads/img/avr-eclipse-config.png %}

侧边栏 编程器配置(Programmer COnfigurations)中点击添加(Add).
左侧选择"USBasp,http://www.fishchl.de/usbasp"(**注意**:需要根据实际下载器硬件选择).

[图:下载器/编程器配置]
{% img /downloads/img/avr-eclipse-config-hw.png %}

同时,在项目-属性中也可以设置.
[图:项目属性中的设置(目标硬件设置等)]
{% img /downloads/img/avr-eclipse-proj-hwset.png %}

##使用
文件(File)->新建(New)->C语言项目(C Project).项目类型(Project type)中选择AVR Cross Target Project -> Empty Project. 给项目名字.

下一步,点击高级设置(Advanced settings),选择之前配置文件. 就可以开始在Linux下进行单片机开发了.

编译完成后,点击avr菜单->上载项目到目标设备即可 
[图:上载到设备(开发板)]
{% img /downloads/img/avr-eclipse-download.png %}

环境详情参阅[参考1]

###可能遇到的问题:
####下载器(硬件)

选择好适当的下载器.USBasp在Eclipse中工程项目的属性选项中,左侧Programmer Hardwavr编程器硬件应该选择"USBasp".默认端口如果不是默认的`/dev/ttyUSB0`,必须填写正确的端口以覆盖配置.

使用AVR JTAG USB仿真器时选择"Atmel JTAG ICE(mk1)".因为默认端口(/dev/parport0)不是usb,可能会提示如下错误:

	avrdude: ser_open(): can't open device "/dev/parport0": No such file or directory
	avrdude: jtagmkI_close(): unsupported baudrate -1

所以默认端口必须覆盖,例如`/dev/ttyUSB0`. 测试可以下载,在线调试功能还在折腾中 :)

总之:硬件和设置一定必须向配合.

####软件:linux设备文件权限
默认情况下普通用户是没有linux的设备文件的读写权限的.所以avarice可能会提示访问受限.

这时只要给avarice增加权限位即可.
1. 切换到root用户
2. chmod a+s /usr/bin/avrdude #赋予权限位
3. 切换回普通用户,继续操作即可.

####快捷键无效

快捷键可能被fcitx输入法程序截获,尝试关闭输入法在试试快捷键,例如Ctrl+Shift+f 格式化(format)代码.

####编译程序下载后没反映

暂时发现 项目->属性 -> C/C++ Build栏 -> Setting -> AVR Compiler(avr编译器)  
-> Optimization(优化) -> Optimization Level(优化等级) 除了选择 (-O0)没有优化外,  
其他选项生成的程序都无法执行(没效果) 暂时不知道什么原因 :(

#参考:
1. avr开发环境搭建教程(EN),本文主要就是参考/翻译它的. <http://www.timteatro.net/2012/03/22/beginning-atmel-avr-development-in-linux-using-avr-eclipse-avr-gcc-and-avrdude/>
2. Linux下avr-Eclipse环境(EN):<http://awawa.hariko.com/eclipse_avr_en.html>
3. avrdude 命令说明(CN):<http://blog.21ic.com/user1/69/archives/2005/1551.html>
4. 淘宝上的USBasp下载器:<http://tradearchive.taobao.com/trade/detail/tradeSnap.htm?spm=a1z09.2.9.147.BquMN6&tradeID=79509563401088>
5. ATmega128a开发板淘宝:<http://tradearchive.taobao.com/trade/detail/tradeSnap.htm?spm=a1z09.2.9.184.BquMN6&tradeID=79064532741088>
6. 开发板原理图(DropBox),包括厂商提供的学习手册:<https://www.dropbox.com/sh/hyh2zcqd3px6iml/tOYBevw_Co>
7. 自制USBasp下载器(CN):<http://www.amobbs.com/thread-723786-1-1.html>
8. AVR-jtag usb仿真器(也可以用来下载):<http://item.taobao.com/item.htm?spm=0.0.0.46.W1V8IW&id=2332186600>

本文地址:<http://zodiac1111.github.com/blog/2012/11/17/avr-mega128a-linux-env-set/>
