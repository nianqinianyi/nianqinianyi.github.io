---
title: 重拾Python笔记六
tags:
  - python
  - 重拾Python笔记
url: 81.html
id: 81
categories:
  - Python
date: 2013-05-11 11:30:08
---

1.  name：指定代码的调用方式：
    
    if \_\_name\_\_=="\_\_main\_\_":
        print '以当前python文件调用方式启动则执行'
        print '其他文件import本文件，则不执行'
    
2.  查询函数的参数
    
    import inspect
    print(inspect.getargspec(function_name))
    
3.  确认某个对象是否有指定的属性
    
    #第二参数是一个字符串
    a = \[1,2,3\]
    print(hasattr(a,'append'))
    
4.  查询对象所属的类和类名称
    
    a = \[1, 2, 3\]
    print a.\_\_class\_\_           #<type 'list'>
    print a.\_\_class\_\_.\_\_name\_\_  #list
    
5.  查询父类
    
    print(list.\_\_base\_\_)
    print(tuple.\_\_base\_\_)  #都是object类
    
6.  指定编码字符集，在python文件第一行添加一行注释，一般有两种形式
    
    #coding:utf-8
    
    \# -*- coding:cp936 -*-
    
7.  二进制(0b)、八进制(0o)、十六进制(0x)
    
    print 0b10101101
    print 0o10340566061357
    print oxABCDEF123560
    
8.  python单行注释是#，多行注释可以用”’实现。
    
    '''多行注释第一行
      多行注释第二行
      多行注释最后一行'''
    
9.  字符串的几个特殊操作
    
    s='This is the string'
    sc=s.center(20)         #返回一个长度20的字符串，s位于其中间
    sl=s.ljust(20)          #返回一个长度20的字符串，s位于其左边
    sr=s.rjust(20)          #返回一个长度20的字符串，s位于其右边
    sw=s.swapcase()         #大写变小写，小写变大写
    sd=sw.capitalize()      #将第一个字符大写
    
10.  类、对象及其属性
    
    class testclass():
        def test(self):
            print "hello"
        def testfunc():
            print "world"
    thetest=testclass()
    print hasattr(thetest,"test")              # 是否有test方法
    print getattr(thetest, "test")             # 返回test属性
    print isinstance(thetest, testclass)       # thetest对象是否为testclass类生成的对象 (一个instance)
    print issubclass(testclass, object)        # Me类是否为object类的子类