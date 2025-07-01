---
title: 重拾Python笔记一
tags: ["Python", "重拾Python笔记"]
categories: ["Python"]
date: 2013-05-06 23:11:18 +08:00
description: 本笔记仅收录了Python语言中部分需要关注或加深理解的基础概念，内容涵盖数据类型、运算符、程序结构及函数定义等方面。
articleGPT: 这份笔记总结了作者当时对Python中一些不熟悉的基础语法、数据类型和函数等核心概念。
---

笔记中仅仅记录一些不太熟悉的东西。  

  1. `type(a)`可返回a的类型。
  2. 元组tuple不可变，列表list可变。
  3. 元组和列表的索引为`a[index]`形式，且支持切片`a[起：终：步长]`。
  4. 字符串其实就是元组。
  5. `and`、`or`和`not`是逻辑运算符。
  6. 其他语言中的`else if`在python中是`elif`。
  7. for循环为：`for i in a`，a是tuple或者list。
  8. `range(a)`函数定义一个从0到a(不包含)的列表。
  9. `def fun_name(para):`为定义一个函数，可以有多个参数，可以返回多个值(实际返回的是元组)，如果没有返回默认其实返回的是None(python的数据类型)。
  10. 给函数传参数，基本数据类型是传的值，其他的是传的指针。

这篇文章是我于2013-05-06发表于oschina.net的文章。[http://my.oschina.net/sixlab/blog/127789](https://my.oschina.net/sixlab/blog/127789)
