---
title: Java 8 新特性系列 – Lambda表达式
tags: [Java, Java8, Lambda, 新特性]
categories: [Java]
date: 2020-03-19 12:54:17 +08:00
description: 文章阐述了 Java 8 引入的 Lambda 表达式，聚焦其作为匿名函数的概念、简化代码的语法，并列举了具体示例和使用限制。
articleGPT: Java 8 引入了 Lambda 表达式，它是一种匿名函数，通过简洁的语法有效替代了冗余的代码写法（尤其适用于只有一个待实现方法的接口），从而大幅节省代码量。
---

Java8 终于引入了 Lambda 表达式，在此之前，传言会在 Java 7 中引入次功能。

## 1 什么是 Lambda

使用过 Python、C# 的应该对此不会陌生，百度百科对 Lambda 表达式的解释为：

> Lambda 表达式（lambda
> expression）是一个匿名函数，Lambda表达式基于数学中的λ演算得名，直接对应于其中的lambda抽象（lambda
> abstraction），是一个匿名函数，即没有函数名的函数。Lambda表达式可以表示闭包（注意和数学传统意义上的不同）。

由解释可以大致知道，Lambda 表达式基本上就是匿名函数的一种简单写法，相当于语法糖，使用 Lambda 可以有效的节省代码量。

### 1.1 基本语法

```java
(parameters) ->{statements;}
```

### 1.2 示例

典型的一个示例就是线程的使用，不过为了演示参数，暂以 Android 中给按钮绑定事件的代码为例，Java8以前的写法：

```java
button.addActionListener(new ActionListener(){
    @Override
    public void actionPerformed(ActionEvent actionEvent){
        System.out.println("Action detected");
    }
});
```

使用 Lambda 的写法：

```java
button.addActionListener((actionEvent)-> {
    System.out.println("Action detected");
});
```

可以看到，以前的写法，要先 new 一个 接口/类，然后在类中 override
未实现的方法，而新写法，省去了类名、方法名等内容，只留下了方法参数名、方法体。

## 2 限制与特殊情况

  1. 接口或者抽象类，有且仅有一个方法需要实现，才能使用Lambda
  2. 有且仅有一个参数，则参数外的小括号可省略
  3. 无返回值，且方法体只有一句话，则方法体的大括号可以省略，这句代码的分号要省略掉。

根据特殊情况，上个段落的代码最终可以简写为：

```java
button.addActionListener(actionEvent-> System.out.println("Action detected"));
```
