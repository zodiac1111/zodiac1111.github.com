---
layout: post
title: "chromium 预览 pdf 文件"
date: 2012-09-20 19:46
comments: true
categories: [pdf,chromium,chrome]
---
chrome使用libpdf.so库,这个库不是自由软件,所以chromium默认没有带.
chrome默认自带的库默认路径为:`/opt/google/chrome/libpdf.so`

##复制chrome的pdf库
复制 `/opt/google/chrome/libpdf.so `到chrome-linux(chromium)下

或许需要在浏览器中键入`chrome://plugins/`,使能Chrome PDF Viewer插件.

#参考资料

1. 简单的解决方式:<http://askubuntu.com/questions/12584/why-doesnt-chromium-have-chrome-pdf-viewer-plugin>
2. chromium issues:<https://code.google.com/p/chromium/issues/detail?id=50852#c16>
3. libpdf.so
