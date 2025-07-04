---
title: 重拾Python笔记六
tags: ["Python", "重拾Python笔记"]
categories: ["Python"]
date: 2013-05-11 23:18:43 +08:00
description: 本文总结了Python基础语法中的常见用法和技巧，涵盖模块导入、函数参数查询、对象属性检查、字符串操作及类与对象关系等内容。
articleGPT: 本文总结了Python编程中的常见技巧，涵盖脚本入口判断、函数参数检查、对象属性操作、类与继承、编码声明、数据表示、注释使用、字符串处理及面向对象基础等核心知识点。
---

重拾Python笔记六  

  1. name：指定代码的调用方式：
  
```python
if __name__ == "__main__":
  print '以当前python文件调用方式启动则执行'
  print '其他文件import本文件，则不执行'
```

  2. 查询函数的参数
```python
import inspect
print(inspect.getargspec(function_name))
```

  3. 确认某个对象是否有指定的属性
```python
#第二参数是一个字符串
a = [1,2,3]
print(hasattr(a,'append'))
```

  4. 查询对象所属的类和类名称
```python
a = [1, 2, 3]
print a.__class__ #<type 'list'>
print a.__class__.__name__ #list
```

  5. 查询父类

```python
print(list.__base__)
print(tuple.__base__) #都是object类
```

  6. 指定编码字符集，在python文件第一行添加一行注释，一般有两种形式`#coding:utf-8 # -*- coding:cp936 -*- `
  7. 二进制(0b)、八进制(0o)、十六进制(0x)
```python
print 0b10101101
print 0o10340566061357
print oxABCDEF123560
```
  8. python单行注释是#，多行注释可以用”’实现。`'''多行注释第一行 多行注释第二行 多行注释最后一行''' `
  9. 字符串的几个特殊操作
```python
s='This is the string'
sc=s.center(20) #返回一个长度20的字符串，s位于其中间
sl=s.ljust(20) #返回一个长度20的字符串，s位于其左边
sr=s.rjust(20) #返回一个长度20的字符串，s位于其右边
sw=s.swapcase() #大写变小写，小写变大写
sd=sw.capitalize() #将第一个字符大写
```

  10. 类、对象及其属性

```python
class testclass():
  def test(self):
    print "hello"
  
  def testfunc():
    print "world"

thetest=testclass()
print hasattr(thetest,"test") # 是否有test方法

print getattr(thetest, "test") # 返回test属性

print isinstance(thetest, testclass) # thetest对象是否为testclass类生成的对象 (一个instance) 

print issubclass(testclass, object) # Me类是否为object类的子类`
```
