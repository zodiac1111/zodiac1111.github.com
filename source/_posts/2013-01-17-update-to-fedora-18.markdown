---
layout: post
title: "升级到fedora18"
date: 2013-01-17 18:55
comments: true
categories: 
---

从fedora17升级到fedora18

#参考
* 官网:<https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum>

#大致步骤
1. <b>备份(数据无价)</b>
2. 阅读已知bug和发行说明,确保自己升级到的版本对自己无害,且有升级的必要
3. 清理目前的系统
4. 升级
5. 安装grub引导程序
##升级
到文本界面(我没有切换到文本界面,直接在gnome3下升级的,阿门)

	ctrl + alt + F2

升级yum

	yum update yum

清除cache

	yum clean all

升级所有包(先删除一些自己不用的包可以加快这一步)

	yum --releasever=18 distro-sync

验证升级

	yum repolist 
	
安装所有的包都是新的版本

	yum groupupdate 'Minimal Install'

安装/列举一些自己必要的组
	
	yum grouplist

##安装grub

	/sbin/grub2-install <引导设备>

如,我是将fedora17安装在本机唯一一块硬盘上,使用了这样硬盘的所有空间.磁盘仅2搞分区,boot分区和lvm逻辑卷分区. 
我的grub是安装在boot分区上的.我使用如下命令:

	/sbin/grub2-install --recheck /dev/sda

#其他
* 从 alpha, beta, preview, 或其他 Rawhide 版本升级的,参见:<https://fedoraproject.org/wiki/Upgrading_from_pre-release_to_final>
* 升级到开发者版本:`yum --releasever=rawhide distro-sync --nogpgcheck`.
* 升级过程中不要中途停止,那样你的系统可能会处于版本混合状态(17和18混合).那样可能会十分麻烦甚至是不可解的.





