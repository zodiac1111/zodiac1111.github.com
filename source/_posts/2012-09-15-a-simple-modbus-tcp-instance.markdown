---
layout: post
title: "简单的 modbus/tcp 实现"
date: 2012-09-15 00:15
comments: true
categories: [modbus,tcp,c/c++]
---
#测试工具: modpoll(主站) diagslave(从站)
##简介
支持平台:

1. Windows
2. Linux (x86 32-bit) <-本文实验平台
3. Solaris (SPARC)
4. QNX Neutrino 6 (x86)

本文使用这两个软件进行Linux 32位平台下的Modbus/TCP程序调试.

###1. 模拟主站(Linux):

	./modpoll -m tcp -a 2 -t4:hex -r 10 -c 3  127.0.0.1 -1 -p 10001
各个选项意义如下:

1. -m <模式名>    : -m tcp即MODBUS/TCP protocol模式
2. -a <从站编号>  : Slave address (1-255, 默认 1 )
3. -t 4:hex      : 16-bit output (holding) register data type with hex display;另有其他多种参见**参考**
4. -r #          : Start reference (1-65536, 100 is default)
5. -c #          : Number of values to poll (1-100, 1 is default)
6. 127.0.0.1     : IP地址(tcp模式)
7. -1            : (数字1)发送一次,没有这个选项则连续发送
8. -p <端口号>    : tcp模式下指定端口号,默认 502

###2. 模拟从站(Linux):
	
	./diagslave -m tcp -p 10001

选项意义:

1. -m tcp :tcp模式
2. -p 10001 : 监听端口
<!-- more -->
##例子
打开连个终端分别运行:

	#从站
	./diagslave -m tcp -p 10001

和

	#主站
	./modpoll -m tcp -a 2 -t4:hex -r 10 -c 3  127.0.0.1 -1 -p 10001

则,在从站可以看到如下显示:

{% codeblock %}
diagslave 2.12 - FieldTalk(tm) Modbus(R) Diagnostic Slave Simulator
Copyright (c) 2002-2012 proconX Pty Ltd
Visit http://www.modbusdriver.com for Modbus libraries and tools.

Protocol configuration: MODBUS/TCP
Slave configuration: address = -1, master activity t/o = 3.00
TCP configuration: port = 10001, connection t/o = 60.00

Server started up successfully.
Listening to network (Ctrl-C to stop)

validateMasterIpAddr: accepting connection from 127.0.0.1 ->显示从127.0.0.1链接到从站
Slave   2: readHoldingRegisters from 10, 3 references  ->显示读取功能 和 从10读取3个寄存器
...................
{% endcodeblock %}

同时主站如下显示:

{% codeblock %}
modpoll 3.1 - FieldTalk(tm) Modbus(R) Master Simulator
Copyright (c) 2002-2011 proconX Pty Ltd
Visit http://www.modbusdriver.com for Modbus libraries and tools.

Protocol configuration: MODBUS/TCP ->模式
Slave configuration...: address = 2, start reference = 10, count = 3 ->从站地址,起始寄存器,寄存器数量
Communication.........: 127.0.0.1, port 10001, t/o 1.00 s, poll rate 1000 ms ->ip 端口
Data type.............: 16-bit register (hex), output (holding) register table ->数据类型

-- Polling slave... 
[10]: 0x0000 ->数据 (仅仅能用用来测试通路,没有实际意义)
[11]: 0x0000
[12]: 0x0000
{% endcodeblock %}

##参考:

1. 模拟主站(master)软件以及官方说明(modpoll)<http://www.modbusdriver.com/modpoll.html>
2. 模拟从站软件以及官方说明:(diagslave)<http://www.modbusdriver.com/diagslave.html>

#libmodbus 开源modbus库
##简介

使用c语言编写的modbus库

1. 官网:<http://libmodbus.org/>(墙?)
2. 代码托管:git <https://github.com/stephane/libmodbus>

#参考资料:

1. <http://www.simplymodbus.ca/TCP.htm>
2. 实现指导手册[Modbus_messaging_on_TCPIP_implementation_guide](http://www.electroind.com/pdf/Modbus_messaging_on_TCPIP_implementation_guide_V11.pdf)
3. 协议[Modbus_Application_Protocol_V1_1b.pdf](http://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b.pdf)(官网,mbap)
4. 实现指导手册[Modbus_Messaging_Implementation_Guide_V1_0b.pdf](http://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf)(官网,实现指导)
5. 说明书[www.modbus.org/specs.php](http://www.modbus.org/specs.php)(说明书)
6. 从Modbus到透明就绪 华镕 编著 第8章 (中文)

