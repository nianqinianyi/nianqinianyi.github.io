---
title: 重拾Python笔记五
tags: ["Python", "重拾Python笔记"]
categories: ["Python"]
date: 2013-05-10 23:17:31
description: 笔记深入探讨了Python的对象本质、函数式编程工具、异常处理方法及动态类型中变量与函数参数的传递机制。
articleGPT: 本文总结了Python中函数作为对象及高阶函数（如lambda、map、filter、reduce）的应用，并阐述了异常处理机制和动态类型与参数传递的核心概念。
---

重拾Python笔记五  

  1. Everything is Object.意味着函数也是对象。
  2. lambda表达式：func=lambda x,y:x+y，意味定义了一个函数，func，接受两个参数x和y，返回的是x和y的和。事实上lambda生成了一个函数对象赋给了func。
  3. 函数可以作为一个参数传给另一个函数。只传函数名即可。
  
```python
#这个函数同上例func函数
def func(x,y):
  return x+y

def fund(f,x,y):
  return f(x,y)

print fund(func,13,23)
```

  4. map函数：内置函数，第一个参数是一个函数对象，之后的参数是列表。`re=map(func,[1,2],[3,4])`，map会将参数中的元素依次赋值给func，然后将返回的值添加到re这个列表中。func接受多少个参数，就有多少个列表参数，列表的长度代表re这个列表的长度。
  5. filter函数：内置函数，用来过滤列表。将列表中元素依次传给函数，当函数返回True的时候，列表中的对应元素会被保存。只有两个参数。

```python
def fune(a):
  if a%2==0:
    return True
  else
    return False
  return rd=filter(fune, \[1, 2, 3, 4, 5, 6, 7, 8\])
  ```

  6. reduce函数：两个参数，第一个仍为函数对象，第二个仍为列表。依次将列表中前n个参数传给函数，然后将返回值放到剩下的列表最前端，继续赋值，一直到最后。`#计算1到10共10个数字的和： rf=reduce((lambda x,y:x+y),\[1,2,3,4,5,6,7,8,9,10\]) `
  7. 异常处理：python中的异常处理与捕捉是： 
```python
try:
  ...
catch Exception:
  ...
else:
  ...
finally:
  ...

a=[1,2,3,4,5,6,7,8,9]
try:
  for i in range(100):
    print a[i]
except Exception:
  print '越界',i
else:
  print '其他异常'
finally:
  print '无论如果都会运行的一句'
print '看捕捉异常后是否还能运行到这里'
```

  8. 自己抛出的异常，raise StopIteration，python会利用StopIteration生成一个该类的一个对象，并抛出。
  9. 动态类型，即变量和它所指的对象分离，变量实际上只是指向对象的一个参考。多个变量指向同一个对象，如果其中一个变量a重新赋值，则不会影响其他变量的值，因为没有修改变量所指向的对象，只是将a重新指向了其他对象。如果其中一个变量b修改了所指向的对象的部分值，则其他变量的值也会受到影响，因为所有变量仍然指向当前对象，只是对象自身变了。
  10. 给函数传参数：如果定义了一个函数def fun(x)，然后调用函数fun(a)，意思为：让fun()的x也指向a所指向的对象，如果在fun()中x又指向了其他对象，a不会受影响，但是如果x修改了对象的部分值，然后a也会改变。
```python
def funf(x):
  print 'x', x
  x=100

def fung(y):
  print 'y:', y
  y[1]=100

a=10
funf(a)
print a

b=[1, 2, 3]
fung(b)
print b
```
