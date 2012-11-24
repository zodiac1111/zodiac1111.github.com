---
layout: post
title: "在Linux系统下通过JTAG调试atmega128a"
date: 2012-11-19 20:00
comments: true
categories: [avr,linux,eclipse]
---
[前篇](/blog/2012/11/17/avr-mega128a-linux-env-set/)搭建了平台,基本完成了下载的功能,于是乎乘热打铁开始折腾jtag的在线调试.

#前言
首先说说我对编译开发调试环境的大概认识,如下图:

{% img /downloads/img/结构示意图.png %}


PC(编译下载)大约就是[前篇](/blog/2012/11/17/avr-mega128a-linux-env-set/)所涉及的部分.

而PC(调试服务器)和PC(调试)就是本文涉及的内容.

稍微解释下我的理解:

1. 调试器:使用JTAG调试器,淘宝上几十块钱买的.看样子是兼容AVR JTAG ICE(mk1)的山寨版,能用.
2. avarice:这里avr-gdb远程调试通过TCP服务,显然板子是不能提供这个服务的,那么avarice大致功能就是将串口(USB)(连着JTAG)转化成为TCP协议,这样通过这个TCP协议可以远程调试
3. avr-gdb:调试器,可以是使用target remote 指定远程调试

<!-- more -->
#效果
如图:

{% img /downloads/img/avr-debug.png %}

#配置
##调试器(eclipse)
主要参考 参考[1]和参考[2],对于Linux和win几乎没什么区别.

对于调试配置,找着参考[1]的设置:

{% img /downloads/img/调试配置1.png %}

1. 确保使用GDB Hardware Debugging,也有说(参考[2])C/C++ Application也行,反正我没弄成
2. 执行 调试器命令.就是在命令行中输入 avr-gdb能启动调试器就可以.
3. 调试目标 等同于命令行中进入avr-gdb后 敲的 `target remote localhost:4242`
4. 确保是 “Standard GDB Hardware Debugging 启动程序”

以上是调试器的设置.光设置完调试器并不能调试,还要配置好调试服务器,这样调试器才能连接上调试服务器进行调试.这时就需要上面说的 avarice 了.

##调试服务器
avarice在终端运行,并且只有他运行着才能在eclipse上正确进行调试;

指令:
	avarice -P atmega128 -j /dev/ttyUSB0 :4242

参数意义是

1. -P <型号> :指定型号 ,atmega128a使用 atmega128 
2. -j <JTAG端口> : 指定使用JTAG的端口,我使用的是 /dev/ttyUSB0 **注意设备文件的权限**
3. :4242 指定开放本机TCP4242端口,之后其他程序(调试器)就可以连接到这个端口进行调试了.**注意和前面参数空格空开**

然后看到类似下面的提示:

	AVaRICE version 2.12, Jan 12 2012 23:36:05

	Defaulting JTAG bitrate to 250 kHz.

	JTAG config starting.
	Hardware Version: 0xc3
	Software Version: 0x80
	Reported JTAG device ID: 0x9702
	Configured for device ID: 0x9702 atmega128 -- Matched with atmega128
	JTAG config complete.
	Preparing the target device for On Chip Debugging.
	Waiting for connection on port 4242.

JTAG已经能正确识别,单片机型号也读出来了,这时光标闪烁提示等待别的程序连接到4242端口.

这时如果使用avr-gdb命令行指定`target remote localhost:4242`或者IDE中运行调试,则可以看到如下如是有程序从本机(127.0.0.1)的56443端口连接上来了.

	....
	Preparing the target device for On Chip Debugging.
	Waiting for connection on port 4242.
	Connection opened by host 127.0.0.1, port 56443.

这时就可以调试了.

##其他
小技巧:在eclipse调试配置的Startup启动选项卡中Runtime Options选择在"mian函数设置断点"和"Resume"则可以开始调试时直接让程序停在主函数,不然可能需要按"继续"开继续运行,或者开始执行初始化代码.
{% img /downloads/img/调试配置main.png %}

#遗留问题

1. 反汇编还不能正确运行,无法一步一步执行(查看)汇编代码

#参考:
1. 使用eclipse调试avr(EN) <http://tobias.schroepf.de/doku/doku.php?id=garage:atmel_avr_debugging_with_eclipse>
2. avr-eclipse 调试wiki(EN) <http://avr-eclipse.sourceforge.net/wiki/index.php/Debugging>


