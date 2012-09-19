---
layout: page
title: "测试各种插件"
date: 2012-09-15 11:53
comments: true
sharing: true
footer: true
---
这是一个插件测试页面,我在这里测试各种网上看到的插件和语法.这个页面的源代码将在[源代码页面](https://github.com/zodiac1111/zodiac1111.github.com/blob/source/source/test/index.markdown)直接找到 :)

以下就是测试咯
---
#1代码测试
codeblock:c
{% codeblock lang:c %}
int main(void)
{
	int i;
	return 0;
}
{% endcodeblock %}

codeblock :
{% codeblock %}
	$ sudo make me a sandwich
{% endcodeblock %}

codeblock title:
{% codeblock Here's an example .rvmrc file. lang:ruby %}
rvm ruby-1.8.6 # ZOMG, seriously? We still use this version?
{% endcodeblock %}

include_code 1.c:
{% include_code 1.c %}

<!-- more -->
#2影片测试

<div class="video-container">
	<embed src="http://player.youku.com/player.php/sid/XNDQ4ODQxNTI0/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>
</div>

<div class="video-container">
http://player.youku.com/player.php/sid/XNDQ4ODQxNTI0/v.swf
</div>

影片测试2失效中:

	{% video http://player.youku.com/player.php/sid/XNDQ4ODQxNTI0/v.swf %}

#3图片测试
{% img https://www.google.com/images/srpr/logo3w.png %}

Bacon ipsum dolor sit amet exercitation ball tip consectetur tempor. Biltong exercitation aliqua, ribeye consequat veniam consectetur.
Aliquip nulla do tempor, ball tip dolore anim esse strip steak nisi nostrud. Tri-tip mollit deserunt ut duis, commodo brisket short loin est hamburger sunt consequat rump meatloaf. Exercitation enim aliqua tempor dolore. Non eu venison, officia boudin tri-tip enim beef ribs flank cupidatat in aute. Tail voluptate fugiat aute flank, venison sint.
Filler text courtesy of Bacon Ipsum, Images courtesy of Place Kitten.
Brisket quis velit bresaola. Pork loin pork chop beef duis. Short loin fugiat officia short ribs magna. Ullamco eu proident jerky, fugiat chuck nostrud ham rump meatloaf eiusmod adipisicing. Qui et reprehenderit, magna biltong consequat short ribs pancetta. Tail tenderloin sausage, hamburger corned beef drumstick ad. Eu labore enim velit.
{% img left https://www.google.com/images/srpr/logo3w.png Place Kitten #2 %}
{% img right https://www.google.com/images/srpr/logo3w.png 150 250 Place Kitten #3 %}
{% img right https://www.google.com/images/srpr/logo3w.png 150 250 'Place Kitten #4' 'An image of a very cute kitten' %}
