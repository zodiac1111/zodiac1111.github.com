---
layout: post
title: "配置gcc编译警告选项"
date: 2012-11-22 19:17
comments: true
categories: 
---
#在各个层次关闭或开启编译警告选项

从上到下覆盖

 推荐的警告选项:`-Wall -Wextra`

##1. 符号级:指定某个变量警告

主要使用`__attribute__`这个扩展,指定某个函数/变量等的属性(参考1,2,3).当然`__attribute__`还能指定其他很多中属性,例如结构体变量的对齐方式,指定声明的函数的属性等,但这里仅关注在警告方面的变量的属性.

	int a __attribute__ ((unused));

指定该变量为"未使用的".即使这个变量没有被使用,编译时也会忽略则个警告输出.

##2. 源代码级:在文件中诊断

能在编译期间规定一段代码的警告属性,如某个文件中后半部分不要求输出某些类型的警告使用编译指示([6.57 Pragmas](http://gcc.gnu.org/onlinedocs/gcc/Pragmas.html#Pragmas))中的诊断编译指示([6.57.10 Diagnostic Pragmas](http://gcc.gnu.org/onlinedocs/gcc/Diagnostic-Pragmas.html#Diagnostic-Pragmas))

语法: 
	#pragma GCC diagnostic <类型> <选项>

其中类型包括:

* `error` :诊断为错误.
* `warning`:争端为警告.
* `ignored`:忽略警告.

选项则是命令行选项中的类似`-Wformat`的选项.

例如:

诊断-忽略:(关闭警告) 
	#pragma  GCC diagnostic ignored  "-Wformat"

诊断-警告:(开启警告) 
	#pragma  GCC diagnostic warning  "-Wformat"

诊断-错误:(开启警告-升级为错误) 
	#pragma  GCC diagnostic error  "-Wformat"

用法:  
在文件开头处关闭警告,在文件结尾出再开启警告,这样可以忽略该文件中的指定警告.

##3 文件或工程级:命令行编译参数指定

警告: 
	gcc main.c -Wall

忽略: 

	gcc mian.c -Wall -Wno-unused-parameter  #开启all警告,但是忽略 -unused-parameter警告

选项格式: `-W[no-]<警告选项>`  
如	: `-Wno-unused-parameter	#no- 表示诊断时忽略这个警告`

#参考:
1. 通过`__attribute__`指定变量的属性(如`unused`,`packed`):  
<http://gcc.gnu.org/onlinedocs/gcc/Variable-Attributes.html#i386%20Variable%20Attributes>
2. 通过`__attribute__`指定函数的属性(如`always_inline`):  
<http://gcc.gnu.org/onlinedocs/gcc/Function-Attributes.html#Function-Attributes>
3. `__attribute__`的语法:  
<http://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html#Attribute-Syntax>
4. 编译指示(#pragam):  
<http://gcc.gnu.org/onlinedocs/gcc/Pragmas.html#Pragmas>
5. 编译诊断指示(Diagnostic Pragmas):  
<http://gcc.gnu.org/onlinedocs/gcc/Diagnostic-Pragmas.html#Diagnostic-Pragmas>
6. 编译警告选项:  
<http://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html>

