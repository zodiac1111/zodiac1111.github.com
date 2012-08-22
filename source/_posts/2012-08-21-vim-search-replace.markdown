---
layout: post
title: "vim查找替换"
date: 2012-08-21 17:15
comments: true
categories: vim
---
`#vim查找替换`
参考资料:http://www.chinavim.org/vivim-%E6%9F%A5%E6%89%BE%E6%9B%BF%E6%8D%A2%E5%A4%A7%E5%85%A8.html

 可以使用 # 作为分隔符，此时中间出现的 / 不会作为分隔符

 :替换当前行第一个 vivian/ 为 sky/

 <code>:n,$s/vivian/sky/</code> 替换第 n 行开始到最后一行中每一行的**第一个** vivian 为 sky

 <code>:n,$s/vivian/sky/g</code> 替换第 n 行开始到最后一行中每一行**所有** vivian 为 sky
`
:[地址/范围]s/<搜索字>/<替换字>[/g]
`
<!-- more -->
1. 地址/范围有:
`
 无 :当前行
 1,10 : 1~10行
 1,$  1~最后一行/文件结束 ps : 1,$ 等价于 % 
 .,.+10 从当前行(".") 到偏置10行(".+10") "+"表示向下偏移 "-"表示向上偏移 
`
2. s=sed 风格的搜索
3. / 分割符
4. g  表示继续匹配(没有 表示匹配一次)

(n 为数字，若 n 为 .<句号>，表示从当前行开始到最后一行)
##删除
删除括号内的东西 不包含括号 di) =delet in )  
光标在一个word内部删除这个整个单词 diw  del in word  
删除并进入insert模式方便修改 ciw change in word  
