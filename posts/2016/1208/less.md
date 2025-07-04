---
title: 【笔记】Less基础知识点
tags: [Less, CSS]
categories: ["CSS"]
date: 2016-12-08 23:50:48 +08:00
description: 文章展示了Less CSS的安装、编译过程，并深入探讨了变量、Mixins、嵌套、运算和函数等核心特性。
articleGPT: Less是一个CSS预处理器，通过提供变量、混合（mixins）、嵌套、运算和函数等功能，增强了CSS的表达力与可维护性，并需要编译为标准CSS才能在浏览器中使用。
---

#### 安装和使用Less

1. 安装`npm install -g less`
2. 编译`lessc styles.less > styles.css`

#### 变量

```less
/* 定义变量 */
@background-color: #ffffff;
@text-color: #1a237e;

p {
  /* 使用变量 */
  background-color: @background-color;
  color: @text-color;
  padding: 15px;
}

ul {
  background-color: @background-color;
}

li {
  color: @text-color;
}
```

Mixins

```less
#circle {
  background-color: #4caf50;
  border-radius: 100%;
}

#small-circle {
  width: 50px;
  height: 50px;
  /* 引用#circle的样式 */
  #circle;
}

/*  id 为 circle1 的元素不会应用此样式 */
#circle1() {
  background-color: #4caf50;
  border-radius: 100%;
}

#big-circle {
  width: 100px;
  height: 100px;
  /* 引用#circle1的样式 */
  #circle1;
}

/* Mixins可以定义参数，如果不传参，默认是25  */
#circle2(@size: 25px) {
  background-color: #4caf50;
  border-radius: 100%;

  width: @size;
  height: @size;
}

#big-circle2 {
  width: 100px;
  height: 100px;
  /* 引用#circle2的样式 */
  #circle2(100px);
}
```

#### 嵌套

注：嵌套时使用的变量会从当前层向上层查找，直到找到

```less
ul {
  background-color: #03a9f4;
  padding: 10px;
  list-style: none;

  li {
    background-color: #fff;
    border-radius: 3px;
    margin: 10px 0;
  }
}
```

会被转换为

```less
ul {
  background-color: #03a9f4;
  padding: 10px;
  list-style: none;
}
ul li {
  background-color: #fff;
  border-radius: 3px;
  margin: 10px 0;
}
```

#### 运算

```less
@div-width: 100px;
@color: #03a9f4;

div {
  height: 50px;
  display: inline-block;
}

#left {
  width: @div-width;
  background-color: @color - 100;
}

#right {
  width: @div-width * 2;
  background-color: @color;
}
```

#### 函数

```less
@var: #004590;

div {
  height: 50px;
  width: 50px;
  background-color: @var;

  &:hover {
    background-color: fadeout(@var, 50%);
  }
}
```

编译为

```less
div {
  height: 50px;
  width: 50px;
  background-color: #004590;
}
div:hover {
  background-color: rgba(0, 69, 144, 0.5);
}
```
