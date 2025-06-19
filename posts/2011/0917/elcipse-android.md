---
title: Eclipse与Android开发环境的安装，纯手工
tags: ["Eclipse", "adt", "Android", "环境搭建", "工具"]
categories: ["工具"]
date: 2011-09-17 22:33:10
description: 详细说明了Android开发环境的准备与安装步骤。
articleGPT: 本文详细指导如何通过下载、安装并配置JDK、Eclipse、Android SDK及ADT插件，来搭建一套完整的Android开发环境。
---

# 准备工作：

1、JDK：这个要去Oracle官网下载，<http://www.oracle.com/technetwork/java/javase/downloads/index.html>，我的是原来下载的Java
SE 6 Update 26，现在有Java SE 7和Java SE 6 Update 27，都差不多。这个安装完eclipse才能运行，所以要先安装。

2、eclipse：打开eclipse官网的下载页面：[http://www.eclipse.org/downloads/](https://www.eclipse.org/downloads/)，找到
Eclipse IDE for Java EE Developers，这个版本是比较全的，也有人使用其他版本，但是好像有些版本不是很全，装ADT的时候出问题。下载之后解压
eclipse文件夹到某个文件夹，我解压到了 `E:\program` 文件夹。

3、Android SDK: 现在Android的官网已经解封了，可以到Android的官网下载
[http://developer.Android.com/sdk/index.html](https://developer.Android.com/sdk/index.html)，当然压缩包的SDK比较常用一些，我下载到也是这个版本的。解压 
Android-sdk-windows 文件夹到某个文件夹，我解压到 `E:\program` 文件夹。

4、ADT：这个一般可以在eclipse里在线安装，这样可以自动升级，不过安装的时候一般都很慢很慢甚至无法安装，没办法，众所周知的网络环境。在
eclipse里无法安装的可以直接在Android官网下载
[http://developer.Android.com/sdk/eclipse-adt.html](https://developer.Android.com/sdk/eclipse-adt.html)。

# 安装

1、配置java环境：我的jdk装在了C:Program FilesJava文件夹。在环境变量中添加以下用户变量：

```
    变量名：Path          变量值：C:\Program Files\Java\jdk1.6.0_26\bin;
    变量名：ClassPath     变量值：.;C:\Program Files\Java\jdk1.6.0\_26\lib\dt.jar;C:\Program Files\Java\jdk1.6.0\_26\lib\tools.jar;
```

测试java环境变量是否成功，在windows命令行中运行javac命令，查看是否正常。

2、安装SDK：打开Android-sdk-windows文件夹里的SDK Manager.exe文件，命令行神马的等一下就过去了。在
Choose Package to Install界面，根据自己需要对不同版本或者不同功能的API包选择accept或者Reject，如果不知道怎么选可以直接选择
accept all。当然可以在Android SDK and AVD Manager界面的Available packages
里选择安装。等待安装吧，要不少时间，因为这些package都需要下载的。安装过程会蹦出几个要点OK对框，点了之后安装包界面会显示done。

3、配置SDK环境变量：我的Android-sdk-windows在E:program文件夹。添加如下环境变量：

```
    变量名：Path      变量值：E:\program\Android-sdk-windows\tools;
```

测试环境变量是否成功，在命令行里运行Android -h，查看是否正常。

4、ADT插件的安装：打开eclipse，点击Help->Install New Software，在Work with中输入
<https://dl-ssl.google.com/Android/eclipse/>，然后按Enter键，如果链接不到把 https
改为 http 再试试。实在不行就把ADT下载下来，点输入框后边的ADD，点击Archive找到下载下来的
ADT插件也可行。接着在下方选择Select All，并且最好把下方
Contact all update sites during install to find required software
前方的勾去掉。OK，Next，最后点Finish，开始安装，速度也很慢，要有耐心.

5、OVER
