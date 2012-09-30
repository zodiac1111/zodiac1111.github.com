---
layout: post
title: "在线分析转换标准 float 型数据"
date: 2012-09-20 19:54
comments: true
categories: [float,IEEE-754]
---
计算机中float型数据以IEEE-754标准存储,例如`1234.5678`存储为`0x449A522B`(32位).

使用二进制表示即:

	01000100 10011010 01010010 00101011

根据IEEE754 Single precision 32-bit标准的定义:

{% img /downloads/img/IEEE-754-float.png %}
通用公式: `实际数值 = sign * 2^exponent * mantissa`

一些特殊的值,如正无穷等,参见维基百科.

更多的分析和在线转换参见参考资料.

##参考资料
1. 维基百科:<https://zh.wikipedia.org/zh/IEEE_754>
1. 在线分析:<http://babbage.cs.qc.cuny.edu/IEEE-754/>
2. 在线转换:<http://www.binaryconvert.com/>

