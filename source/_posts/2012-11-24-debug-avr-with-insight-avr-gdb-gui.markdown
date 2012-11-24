---
layout: post
title: "编译avr-insight"
date: 2012-11-24 18:16
comments: true
categories: [avr,linux,insight]
---
[上次](/blog/2012/11/19/avr-jtag-debug-with-eclipse-on-linux/)进行到可以调试avr程序,但是不能以汇编语言单步执行/调试程序.而且eclipse的调试界面也不是很喜欢,还是用insight比较习惯.但是insight不能直接调用avr-gdb,这点ddd就比较方便,可以指定各种命令行的调试器.所以还是决定编译avr-insight来调试程序.
#完成效果:

调试环境:
{% img /downloads/img/调试环境.png %}

基本的代码,汇编代码,寄存器,堆栈等功能都可以使用了. :)

<!-- more -->

远程调试设置:
{% img /downloads/img/远程调试设置.png %}

#编译avr-insight

构建avr-gcc: <http://wiki.vandenbussche.nl/index.php?title=Building_AVR_GCC>

insight下载的地址: <http://mirrors.kernel.org/sources.redhat.com/insight/releases/>  
下载`insight-6.8-1a.tar.bz2`

{% codeblock %}
$ ./configure --target=avr --program-prefix="avr-"
$ make
as root
# make install
{% endcodeblock %}

##出现的问题

###警告升级为错误1

在`make`阶段发生如下错误:

{% codeblock %}
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.././bfd -I. -I. -I.././bfd -I.././bfd/../include -W -Wall -Wstrict-prototypes -Wmissing-prototypes -Werror -g -O2 -c elf32-avr.c -o elf32-avr.o
elf32-avr.c: In function 'elf32_avr_relocate_section':
elf32-avr.c:1204:34: error: variable 'warned' set but not used [-Werror=unused-but-set-variable]
elf32-avr.c:1204:16: error: variable 'unresolved_reloc' set but not used [-Werror=unused-but-set-variable]
elf32-avr.c:1183:11: error: variable 'r_type' set but not used [-Werror=unused-but-set-variable]
elf32-avr.c: In function 'elf32_avr_relax_delete_bytes':
elf32-avr.c:1414:15: error: variable 'shrinked_insn_address' set but not used [-Werror=unused-but-set-variable]
elf32-avr.c:1382:22: error: variable 'irelalign' set but not used [-Werror=unused-but-set-variable]
elf32-avr.c: In function 'elf32_avr_relax_section':
elf32-avr.c:1596:29: error: variable 'last_reloc' set but not used [-Werror=unused-but-set-variable]
elf32-avr.c: In function 'avr_mark_stub_not_to_be_necessary':
elf32-avr.c:2459:37: error: variable 'htab' set but not used [-Werror=unused-but-set-variable]
cc1: all warnings being treated as errors
make[4]: *** [elf32-avr.lo] 错误 1
make[4]: 离开目录“/home/zodiac1111/test/insight-6.8-1/bfd”
make[3]: *** [all-recursive] 错误 1
make[3]: 离开目录“/home/zodiac1111/test/insight-6.8-1/bfd”
make[2]: *** [all] 错误 2
make[2]: 离开目录“/home/zodiac1111/test/insight-6.8-1/bfd”
make[1]: *** [all-bfd] 错误 2
make[1]: 离开目录“/home/zodiac1111/test/insight-6.8-1”
make: *** [all] 错误 2
{% endcodeblock %}

将文件insight-6.8-1/bfd/Makefile,修改为:

`201: WARN_CFLAGS = -W -Wall -Wstrict-prototypes -Wmissing-prototypes #-Werror`

注销掉`-Werror`

###警告升级为错误2

在`make`阶段发生如下错误:
{% codeblock %}
gcc -c -g -O2   -I. -I.././gdb -I.././gdb/config -DLOCALEDIR="\"/usr/local/share/locale\"" -DHAVE_CONFIG_H -I.././gdb/../include/opcode -I.././gdb/../readline/.. -I../bfd -I.././gdb/../bfd -I.././gdb/../include -I../libdecnumber -I.././gdb/../libdecnumber   -DMI_OUT=1 -DGDBTK -DTUI=1  -Wall -Wdeclaration-after-statement -Wpointer-arith -Wformat-nonliteral -Wno-pointer-sign -Wno-unused -Wno-switch -Wno-char-subscripts -Werror cp-name-parser.c
cp-name-parser.y: 在函数‘cp_comp_to_string’中:
cp-name-parser.y:1980:20: 错误：在‘enum demangle_component_type’和‘enum <匿名>’间比较 [-Werror=enum-compare]
cp-name-parser.y:1985:25: 错误：在‘enum demangle_component_type’和‘enum <匿名>’间比较 [-Werror=enum-compare]
cc1: all warnings being treated as errors
make[2]: *** [cp-name-parser.o] 错误 1
make[2]: 离开目录“/home/zodiac1111/test/insight-6.8-1/gdb”
make[1]: *** [all-gdb] 错误 2
make[1]: 离开目录“/home/zodiac1111/test/insight-6.8-1”
make: *** [all] 错误 2
{% endcodeblock %}

文件insight-6.8-1/gdb/Makefile修改为:

`145:WERROR_CFLAGS = #-Werror`

注销掉`-Werror`

##使用 insight-6.8a.tar.bz2  可能的问题

开始的时候没注意,下载了6.8a版本,后来编译完运行时发现了这个问题.  
来源: <http://forums.fedoraforum.org/showthread.php?p=1349223#post1349223>

{% codeblock %}
Tk_Init failed: Can't find a usable tk.tcl in the following directories: 
/usr/local/share/tk8.4 /usr/local/lib/tk8.4 /usr/lib/tk8.4 /usr/local/library /usr/library /usr/tk8.4.1/library /tk8.4.1/library

/usr/local/share/tk8.4/tk.tcl: no event type or button # or keysym
no event type or button # or keysym
while executing
"bind Listbox <MouseWheel> {
%W yview scroll [expr {- (%D / 120) * 4}] units
}"
(file "/usr/local/share/tk8.4/listbox.tcl" line 182)
invoked from within
"source /usr/local/share/tk8.4/listbox.tcl"
(in namespace eval "::" script line 1)
invoked from within
"namespace eval ::[list source [file join $::tk_library $file.tcl]]"
(procedure "SourceLibFile" line 2)
invoked from within
"SourceLibFile listbox"
(in namespace eval "::tk" script line 4)
invoked from within
"namespace eval ::tk {
SourceLibFile button
SourceLibFile entry
SourceLibFile listbox
SourceLibFile menu
SourceLibFile panedwindow
SourceLibFile ..."
invoked from within
"if {$::tk_library ne ""} {
if {[string equal $tcl_platform(platform) "macintosh"]} {
proc ::tk::SourceLibFile {file} {
if {[catch {
namesp..."
(file "/usr/local/share/tk8.4/tk.tcl" line 393)
invoked from within
"source /usr/local/share/tk8.4/tk.tcl"
("uplevel" body line 1)
invoked from within
"uplevel #0[list source $file]"
This probably means that tk wasn't installed properly.
{% endcodeblock %}

按照来源里说的,6.8-1已经修复了这个bug.

