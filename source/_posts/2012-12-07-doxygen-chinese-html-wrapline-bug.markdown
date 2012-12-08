---
layout: post
title: "修正doxygen中文显示html不换行bug"
date: 2012-12-07 19:31
comments: true
categories: [doxygen]
---
#描述

doxygen在 `OUTPUT_LANGUAGE` 选项设置成为 Chinese 后,  
生成的html页面中关于函数的**参考**项目.  
列出很多项的时候会超出框架,一直在一行上,没有按照框架的宽度换行.

效果如图:{% img /downloads/img/bug.png %}

如图长长的一行文字十分不方便查看.

该问题在1.8.1.1和1.8.2(目前版本)都存在,且只有以简体中文作为输出语言是存在.

#解决

修改doxygen源代码.

* 下载源代码包:<http://sourceforge.net/projects/doxygen/files/rel-1.8.2/>    doxygen-1.8.2.src.tar.gz 

* 修改 `/doxygen-1.8.2/src/translator_cn.h` 文件   
第546行`virtual QCString trWriteList(int numEntries)` 函数中的:
  
{% codeblock lang:c %}
if (i!=numEntries-1)  // not the last entry, so we need a separator
        {
          if (i<numEntries-2) // not the fore last entry 
            result+=",";
          else                // the fore last entry
            result+=CN_SPC", 以及"CN_SPC;
        }
{% endcodeblock %}
修改为:
{% codeblock lang:c %}
if (i!=numEntries-1)  // not the last entry, so we need a separator
        {
          if (i<numEntries-2) // not the fore last entry 
            result+=","CN_SPC;
          else                // the fore last entry
            result+=CN_SPC", 以及"CN_SPC;
        }
{% endcodeblock %}
即在`","`后面加上`CN_SPC`(其实就是一个空格)

编译,安装之后即可.

完成效果:{% img /downloads/img/now-ok.png %}
这样所有的参考就都很在页面中看到了 :)


