---
title: IDEA 常用设置
tags: ["IDEA", "Intellij", "设置", "工具"]
categories: ["工具"]
date: 2018-05-16 00:40:37
description: 文章分享了一系列IDE配置，旨在让开发工具更好用、更好看。
articleGPT: 文章介绍了如何通过调整各项配置，优化IDE的使用体验和界面显示，使其更高效、美观。
---

# 为了更好用

### 代码补全不区分大小写

![](/images/posts/2018-05-16-idea-config/001.png)

### 粘贴代码时自动格式化

![](/images/posts/2018-05-16-idea-config/002.png)

### 修改properties编码为UTF-8

![](/images/posts/2018-05-16-idea-config/003.png)

### 自动导入类，无需按快捷键

![](/images/posts/2018-05-16-idea-config/004.png)

### 选中文本时输入括号/引号，自动包裹

当有选中的文本时候，输入括号、引号等符号，自动将选中的文本外加上开闭符号  
不会将选中的内容替换为括号、引号  

![](/images/posts/2018-05-16-idea-config/005.png)

### 生成main方法

使用 main 关键字生成main方法

![](/images/posts/2018-05-16-idea-config/006.png)

# 为了更好看

### 取消注释在首行

共两处设置，第一处设置：

![](/images/posts/2018-05-16-idea-config/007.png)

共两处设置，第二处设置：

![](/images/posts/2018-05-16-idea-config/008.png)

### 在右下角显示内存占用

![](/images/posts/2018-05-16-idea-config/009.png)

### 显示代码分割

方法之间会有一条虚线分开；  
并且显示空白字符，更容易区分空格和 tab 位，跟容易看是否有行尾空格  

![](/images/posts/2018-05-16-idea-config/010.png)

### 取消部分内容的报错/警告

Javadoc中有报错，不影响代码运行，将错误提示级别调低  

StringBuffer/StringBuilder的append方法为了更容易看，使用了append(strA+strB),降低错误提示级别  
