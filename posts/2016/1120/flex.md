---
title: 【笔记】Flex布局
tags: [Flex, CSS]
categories: [CSS]
date: 2016-11-20 23:47:57 +08:00
description: Flex布局的定义、核心概念，及其容器和项目各项属性在此得到了详细阐述。
articleGPT: Flex布局是CSS中一种强大的弹性布局方式，允许开发者通过设置容器和子元素的属性，灵活控制项目在主轴和交叉轴上的排列、对齐与空间分配。
---

## 一、简介

Flex布局意为弹性布局。任何容器可以指定为Flex布局，则其子元素自动成为容器成员，称为Flex Item(Flex项目)，且子元素的float
clear vertical-align属性失效。

```css
.box{
  display: flex;
}

/*行内元素*/
.box{
  display: inline-flex;
}

/* Webkit */
.box{
  display: -webkit-flex;/* Safari */
  display: flex;
}
```

二、概念

![](/images/posts/2016-11-20-flex/001.png)

采用Flex布局的元素：flex container(flex容器)

子元素：flex item(flex项目)

容器默认存在两根轴：水平的主轴（main axis）和垂直的交叉轴（cross axis）。主轴的开始位置（与边框的交叉点）叫做main
start，结束位置叫做main end；交叉轴的开始位置叫做cross start，结束位置叫做cross end。

项目默认沿主轴排列。单个项目占据的主轴空间叫做main size，占据的交叉轴空间叫做cross size。

## 三、容器属性

容器属性主要有六个：

  1. flex-direction：主轴方向，row(水平向右) | row-reverse(水平向左) | column(垂直向下) | column-reverse(垂直向上)
  2. flex-wrap：换行方式，nowrap(不换行) | wrap(向下换行) | wrap-reverse(向上换行)
  3. flex-flow：flex-direction 与 flex-wrap的简写，默认值为row nowrap
  4. justify-content：主轴上对齐方式，flex-start(左对齐) | flex-end(右对齐) | center(居中对齐) | space-between(两端对齐，间隔相等) | space-around(子元素与容器间隔x，两个子元素间隔2x)
  5. align-items：交叉轴上对齐方式，flex-start(交叉轴起点) | flex-end(交叉轴终点) | center(交叉轴中点) | baseline(第一行文字的基线) | stretch(默认，如果项目未设置高度或设为auto，将占满整个容器的高度)
  6. align-content：多跟轴线对齐方式，一根轴线时不起作用。flex-start(交叉轴起点) | flex-end(交叉轴终点) | center(交叉轴中点) | space-between(两端对齐，间隔相等) | space-around(子元素与容器间隔x，两个子元素间隔2x) | stretch(默认，轴线占满整个交叉轴)

## 四、项目属性

项目属性主要有6个：

  1. order：项目排列顺序。越小越靠前，默认0
  2. flex-grow：项目放大比例，默认0，即不放大，多个元素根据此属性百分百占据剩余空间
  3. flex-shrink：项目缩小比例，默认为1，即空间不足时缩小，0为不缩小
  4. flex-basis：初始情况占据主轴空间的多少，之后会计算剩余空间并缩放，默认auto
  5. flex：flex-grow, flex-shrink 和 flex-basis的简写，默认值为0 1 auto，后两个可选
  6. align-self：覆盖align-items属性。默认值为auto，表示继承父元素align-items，无父元素，等同stretch。auto | flex-start | flex-end | center | baseline | stretch
