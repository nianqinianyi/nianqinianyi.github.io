---
title: 重拾Python笔记三
tags:
  - python
  - 重拾Python笔记
url: 75.html
id: 75
categories:
  - Python
date: 2013-05-08 11:27:17
---

 

*   打开文件，创建文件对象`f=open('filename','r')`，第一个参数为文件名，第二个参数为读写模式，常用r或者w。
*   读取文件内容使用`f.read(N)`、`f.readline()`、`f.readlines()`，分别是读取N bytes、读取一行、所有行并存在列表中这三种方式。
*   写入文件方法使用`f.write('string')`、`f.write(list)`，分别是将string写入文件、将列表写入文件并每行一个列表的元素。
*   最后要关闭文件f.close()。
*   `for line in file(filename)`，则通过`file()`函数，循环读取文件内容，依次将文件中每一行赋值给line。
*   一个py文件就是一个模块，使用`import filename`来导入`filename.py`的模块，调用函数时使用`filename.method()`。其他导入方式为`import a as b`、`from a import *`。
*   import的搜索路径为：程序所在文件夹 > 标准库路径 > 系统环境变量。
*   将多个模块放在一个文件夹下，并在改文件夹下创建一个`__init.py__`的空文件表明这是一个模块包，然后使用`import filepath.filename`来导入。
*   函数传递参数可以不通过位置，而是自定义顺序，一个函数的定义`def f(a,b,c):`，传递参数时可使用关键字传递参数`f(2,c=2,b=3)`，但是位置传递的参数必需在关键字传递参数的前面。
*   函数在定义时候可以指定默认值`def f(a=12,b='str',c=2):`。