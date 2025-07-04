---
title: 重拾Python笔记四
tags: ["Python", "重拾Python笔记"]
categories: ["Python"]
date: 2013-05-09 23:15:54 +08:00
description: 内容涵盖Python中函数参数的灵活封装与解包、高效迭代机制，以及生成器与列表推导式等核心数据处理与生成技巧。
articleGPT: 该文介绍了Python中灵活的参数传递（包裹与解包裹）、高效的数据迭代（enumerate, zip）以及内存优化的数据生成方式（生成器、列表解析）等核心特性。
---

重拾Python笔记四  

  1. 包裹(packing)位置传递：有时候定义的方法不知道要接受多少个参数，可以在定义的时候使用包裹位置传递：def fun(*name):，在fun方法中可使用type(name)查看name的类型为元组(tuple)。
  2. 包裹关键字传递：定义方法的时候：def fun(**name):，在fun()方法中可使用type(name)查看name的类型为字典(dict)，此定义意味着按字典里的键所对应的值来给方法参数赋值。
  3. 解包裹(unpacking)：不在定义的时候加 _，而是在传给方法时候fun(\_ a)，a是一个元组,表明依次将元组中的元素赋值给fun方法所定义的参数；或者使用fun(**a)，a是字典，表示按a中的键所对应的值给fun方法中的元素赋值。
  4. 当多种赋值方法混合使用的时候，有一个基本原则：位置 > 关键字 > 包裹位置 > 包裹关键字。
  5. for a in enumerate(str):，如果str是一个字符串的话，每一次a都是一个元组，包含两个值(index,char)，分别是当前字符的索引和当前字符。
  6. 若定义了数个列表，长度一样，则在循环中，for (a,b,c) in zip(lista,listb,listc):表明同时遍历三个列表，将得到的值赋给a，b，c。
  7. 循环对象：一个包含了next()方法的对象(在python 3x中是next()方法)，该方法会得到对象的下一个结果，当没有下一个结果的时候举出StopIteration错误，for line in open(‘a.txt’):中open(‘a.txt’)返回的就是一个循环对象，for每次都会自动调用其next()方法。循环对象比序列的优点在于，序列要事先生成全部元素，而循环对象只在调用next()的时候生成要使用的元素，节省了空间。
  8. 生成器：生成一个自定义的循环对象，和定义方法一样，不过不使用return，而是用yield，当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield：`def gen(): a = 100 yield a a = a*8 yield a yield 1000 for i in gen(): print i `生成器有一个简便的写法，即使用生成器表达式(Generator Expression)：G = (x for x in range(4))，这个写法相当于`def gen(): for i in range(4): yield i; `
  9. 表理解(list comprehension)：一种快速生成表的方式，对于L = [x**2 for x in range(10)]，相当于：`L = [] for x in range(10): L.append(x**2) `
  10. iter()函数和循环器(iterator)：for循环调用循环对象的时候，是通过iter()方法先将循环对象转换为循环器(iterator)。但这只是技术层面，逻辑层面可以忽略这层关系。
