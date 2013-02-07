---
layout: post
title: "Kindle Paperwhite越狱"
date: 2013-02-05 14:52
comments: true
categories: 
---
kindle是linux系统,arm处理器.关于系统架构可以参考<http://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#Architecture>

这次主要目的是将Kindle Paperwhite越狱,在PC(Fedora18 Linux)上.
实现通用的ssh访问.其实PW入手才不到24小时.果然我就是喜欢拆呵 :)

<!-- more -->

##越狱
###降级(非必须)
因为不小心升级到5.3.3需要降级才可以使用,如降级到5.3.1

5.3.1文件 <http://kindle.s3.amazonaws.com/update_kindle_5.3.1.bin>

复制到Kindle"根目录".

在Kindle上 设置图标->设置选项->更新.

###越狱
参考:Kindle Paperwhite Jailbreak (5.2.0 - 5.3.1):

<http://www.mobileread.com/forums/showthread.php?t=198446>

如果又什么不同的地方,请以参考文档为准.

解压附件,按照`README.txt`指示.(RTFM!)

* 把Kindle插到PC机上,会有一个磁盘Kindle.把三个文件如下放置到Kindle根目录
{% codeblock lang:bash %}
	.
	|-- documents
	|   `-- jailbreak.mobi
	|-- jailbreak.sh
	`-- MOBI8_DEBUG
{% endcodeblock %}
* 在PC上"弹出"磁盘.  

* Kindle上有一本书,打开,按照其指示操作.  

{% img  /downloads/img/一本书.png 300 %}
{% img  /downloads/img/点击.png 300 %}

* 按住左上角  

{% img  /downloads/img/按住.png 300 %}

* 等待  

{% img  /downloads/img/等待.png 300 %}

###SSH登陆

USBnet 网络登陆,参考:

<http://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#USB_Networking>

根据`README_FIRST`文件指引:

1. 复制 update_usbnet_0.7.N_install.bin到Kindle根目录
2. 弹出.
3. 更新您的Kindle:在Kindle上 设置图标->设置选项->更新.

4. 诊断模式.
5. PC上启动USBnet.  
		host ifconfig usb0 192.168.15.201
可能需要在网络连接中设置网关.  
		IP 192.168.15.201
		Subnet 255.255.255.0
		网关192.168.15.1
6. ping下看看:)  
		[zodiac1111@localhost octopress]$ ping 192.168.15.244
		PING 192.168.15.244 (192.168.15.244) 56(84) bytes of data.
		64 bytes from 192.168.15.244: icmp_seq=1 ttl=64 time=1.23 ms
		64 bytes from 192.168.15.244: icmp_seq=2 ttl=64 time=0.189 ms
7. 登陆  
{% codeblock lang:bash %}
	[zodiac1111@localhost octopress]$ ssh root@192.168.15.244
	The authenticity of host '192.168.15.244 (192.168.15.244)' can't be established.
	RSA key fingerprint is 78:80:25:41:49:59:52:9c:30:89:b3:3f:c8:b6:e2:e3.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added '192.168.15.244' (RSA) to the list of known hosts.
	root@192.168.15.244's password: 
	#################################################
	#  N O T I C E  *  N O T I C E  *  N O T I C E  # 
	#################################################
	Rootfs is mounted read-only. Invoke mntroot rw to
	switch back to a writable rootfs.
	#################################################
{% endcodeblock %}
8. 到处看看  
{% codeblock lang:bash %}
[root@[192_168_15_244] etc]# df
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/root                63703     26170     34333  43% /
tmpfs                   128096         4    128092   0% /dev
tmpfs                   128096         0    128096   0% /dev/shm
/dev/mmcblk0p3           63461     14573     45612  24% /var/local
fsp                    1392632     11824   1380808   1% /mnt/us
/dev/loop/0            1392632     11824   1380808   1% /mnt/base-us
[root@[192_168_15_244] /]# ls -l
drwxrwxr-x    2 root     root          2048 Sep 26  2012 bin
drwxr-xr-x    2 root     root          1024 Jan  1  1970 cust
drwxr-xr-x   12 root     root          1000 Jan  1 00:01 dev
drwxrwxr-x   16 root     root          1024 Jan  1 00:02 etc
drwxrwxr-x    5 root     root          2048 Sep 26  2012 lib
drwxrwxr-x    8 root     root          1024 Sep 26  2012 mnt
drwxrwxr-x    5 root     root          1024 Jan  1  1970 opt
dr-xr-xr-x   70 root     root             0 Jan  1 00:00 proc
drwxrwxr-x    2 root     root          2048 Sep 26  2012 sbin
drwxr-xr-x   12 root     root             0 Jan  1 00:00 sys
lrwxrwxrwx    1 root     root             8 Jan  1 00:00 tmp -> /var/tmp
drwxrwxr-x    8 root     root          1024 Sep 26  2012 usr
drwxrwxr-x    9 root     root           180 Jan  1 00:01 var
[root@kindle etc]# uname -a
Linux kindle 2.6.31-rt11-lab126 #1 Thu Nov 29 23:37:38 PST 2012 armv7l GNU/Linux
[root@[192_168_15_244] /]# ifconfig 
lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

usb0      Link encap:Ethernet  HWaddr EE:59:00:00:00:15  
          inet addr:192.168.15.244  Bcast:192.168.15.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1318 errors:0 dropped:0 overruns:0 frame:0
          TX packets:459 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:85456 (83.4 KiB)  TX bytes:64533 (63.0 KiB)
#这个时候只有usb
{% endcodeblock %}

##通过Wi-Fi登陆
老是接着usb线太不方便了,无绳论的我当然要追求利用无线咯.参考:<http://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#SSH_access_over_Wifi>

1. 改个密码.方便使用,谁没事记序列号或者在线猜测密码,关键是那密码不一定对:(
```
#文件系统本来是只读的,先让它可以读写.	
mntroot rw
#修改root用户密码
passwd
```
2. 编辑配置文件
```
cd mnt/us/usbnet/etc
#有一种信仰叫做vi >_< 
vi config

#!/bin/sh
#
# $Id: config 8742 2012-10-21 20:04:06Z NiLuJe $
#

# WARNING: Take note that we're essentially a shell script, se we absolutely *MUST* use UNIX line endings!
# WARNING: To avoid leaving your system in an undefined state,
#          do *NOT* modify this file while usb over ethernet is enabled!
#          (That means when the the auto enable feature is in use, too!)

# Tweak this to your liking (IPv4 only, no hostname aliases)
KINDLE_IP=192.168.15.244

# Allow SSH over WiFi
# NOTE: If you set this to true, the SSHD *WILL* check your passwords!
# Make sure you know your root password, or auth via shared keys!
USE_WIFI="true"

# Don't switch to Ethernet over USB, and only launch SSHD
# NOTE: Make sure you're able to properly login over SSH before enabling this...
# It's obviously only useful with WiFi devices, so leave to false on non-WiFi devices
USE_WIFI_SSHD_ONLY="false"

# Use OpenSSH instead of dropbear (somewhat faster login)
# NOTE: OpenSSH *WILL* check your passwords!
# Make sure you know your root password, or auth via shared keys!
USE_OPENSSH="false"
- config 1/27 3%
```
忘了要不要重启.

我是没有设置开机启动USBnet.而是通过`;un`来手动启动.一些指令:<http://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#Search_Bar_Shortcuts>

再登陆,这时就不需要USB电缆了.连上Wi-Fi.Kindle的IP是192.168.0.101(我家的路由D-link的),IP就根据实际情况好了.
{% codeblock lang:bash %}
	ssh root@192.168.0.101
{% endcodeblock %}
{% codeblock lang:bash %}
[root@kindle etc]# ifconfig 
lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:476 errors:0 dropped:0 overruns:0 frame:0
          TX packets:476 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:112343 (109.7 KiB)  TX bytes:112343 (109.7 KiB)

usb0      Link encap:Ethernet  HWaddr EE:19:00:00:00:00  
          inet addr:192.168.15.244  Bcast:192.168.15.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2878 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1291 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:151737 (148.1 KiB)  TX bytes:227383 (222.0 KiB)

wlan0     Link encap:Ethernet  HWaddr F0:4F:7C:F8:0A:75  
          inet addr:192.168.0.101  Bcast:192.168.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2021 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1434 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:535079 (522.5 KiB)  TX bytes:280214 (273.6 KiB)
{% endcodeblock%}

取消诊断模式时出现错误?参考:<http://www.mobileread.com/forums/showthread.php?p=2041719>

启动USBnet ;un

##定制字体
参考1:<http://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#Custom_Fonts>

参考2:<http://www.mobileread.com/forums/showthread.php?t=168765> 5.3.1版本

各种字体,文泉驿等宽正黑效果图:

{% img /downloads/img/各种字体.png 300 %}
{% img /downloads/img/文泉驿等宽正黑.png  300 %}



