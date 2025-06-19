---
title: 重拾Python笔记二
tags: ["Python", "重拾Python笔记"]
categories: ["Python"]
date: 2013-05-07 23:12:58
description: 这篇Python笔记主要概述了类定义、面向对象特性，以及字典的基础操作和常用方法。
articleGPT: 这篇Python笔记主要回顾了类的定义、对象特性、运算符重载，并详细阐述了字典的创建、访问、操作和遍历方法。
---

重拾Python笔记二

  1. `class clss_name(parent_class):`定义一个父类为parent_calss的类class_name。
  2. 在类中定义的函数，第一个参数必需是self，这样在函数内就可以调用类，相当于其他语言中的this。
  3. 在类中可以定义有一个`__init__()`方法，相当于其他语言中的构造方法，同样，它的第一个参数必需是self。
  4. `Everything is object.`所以元组、列表等等都是对象，我们定义的列表其实是list类的一个对象。
  5. 运算符+、-、*、/等等都是类内部的方法，类内部定义的`__add__()`方法就是+运算符，`__sub__()`就是-运算符。
  6. 词典其实就是map，键值对。`adict={'tom':23,'jim':25,'loki':24}`。
  7. 词典没有顺序，不能通过下标访问。应该通过键来访问：`adict['tom']==20`。
  8. 创建空词典：`adict={}`,词典添加值`adict['New']=22`，词典删除某一个值del adict[‘tom’]，清空词典`adict.clear()`。
  9. `adict.keys()`、`adict.values()`、`adict.items()`分别返回字典的所有键、所有值、所有键值对，返回的都是列表，其中`items()`中每一个元素都是一个元组。
  10. 对于词典`for a in adict:`则a将遍历词典中所有的键。

