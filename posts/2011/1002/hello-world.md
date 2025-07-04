---
title: 什么才是真正的Hello World！
tags: ["Hello World"]
categories: ["随笔"]
date: 2011-10-02 22:49:50 +08:00
description: 文章阐述了合格的编程入门“Hello World”教程，应深入剖析程序结构与关键组成，而非仅停留于展示运行结果。
articleGPT: 文章指出，安卓开发教程中的“Hello World”示例未能有效教授代码和项目结构背后的含义，而仅仅停留在演示输出，这不符合其作为编程起点的真正作用。
---

前两天看一个Android开发的教程，开始配置Android开发环境的一部分还不错，但是当看到经典的hello
world的时候，我果断放弃了这个教程，为什么呢？看我慢慢道来： 看百度百科咋介绍hello world的：


> Hello World 中文意思是『你好,世界』。
> 因为《The C Programme Language》中使用它做为第一个演示程序，非常著名，
> 所以后来的程序员在学习编程或进行设备调试时延续了这一习惯。

也就是说hello world是一个起点，是编程的第一步。为什么把hello world当第一步呢，为什么不把计算1+1=2的程序当第一步呢？因为hello
world的简洁+实用，它包含了一个程序应具备的一切！那么，hello world是编写出一个打印出hello
world的程序就一切OK了吗？不是的，hello world不仅要出结果，也应该要教会看hello
world的人每一个语句是什么意思。在Android开发中，google默认一个空的Android程序就是一个hello
world，所以很多教程教大家hello
world的时候都是建立一个空的Android程序，编译，一切OK。你一切做完了，看教程的人还是不知道为什么会出现一个hello world。
真正的hello world应该是什么样子？我以c语言为例，大致的说一下：

```c++
    #include <studio.h>;       //头文件……
    int main(void)             //主函数……       函数……
    {                                //函数块……
        print("Hello World!");      //输出函数……
    }
```

所以一个hello world至少至少应该包含“头文件”、“主函数”、“函数块”这三部分内容，hello
world应该达到这样一种效果：初学者看完hello world之后，当看到某一个程序里有一个#include
<stdlib.h>，初学者可以不知道stdlib.h里边有哪些功能，但是他会知道stdlib.h是一个头文件。 所以，回到Android的hello
world上，教程里的hello world应该包括以下内容：

1、创建一个Android应用程序的步骤。（很多教程仅仅停留在这一步）  
2、Android应用程序目录结构。  
3、Android里一些重要文件的作用，如AndroidMainfest.xml等。

ps：很感谢mars老师的视频教程，我受益匪浅，Android的 hello world 
应该包含的内容参考了mars老师的视频教程。有学习Android兴趣的可以去mars老师的论坛看看
[http://www.mars-droid.com/](http://www.mars-droid.com/bbs/forum.php)
