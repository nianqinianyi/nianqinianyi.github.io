---
title: Weex 入门01 - 环境搭建与初步体验
url: 607.html
id: 607
categories:
  - 其他
date: 2017-03-14 06:02:10
tags:
---

一、开发工具 Intellij IDEA IDEA 中的两个 Weex 插件   二、安装环境 1. 安装 node.js，官网下载，一步到底安装。 2. 使用 npm 安装 weex-toolkit，在 shell 输入下面的命令：  

1.  `npm install -g weex-toolkit`

三、快速体验

1\. 创建一个文件：demo.we。

1.  `<template>`
2.  `<div class="container" >`
3.  `<div class="cell">`
4.  `<image class="thumb" src="https://oh7gzl219.qnssl.com/logo.png"></image>`
5.  `<text class="title">六楼实验室：https://sixlab.cn/</text>`
6.  `</div>`
7.  `</div>`
8.  `</template>`

10.  `<style>`
11.  `.cell{margin-top:10 ; margin-left:10 ; flex-direction: row; }`
12.  `.thumb {width: 200; height: 200; }`
13.  `.title {text-align: center ; flex: 1; color: grey; font-size: 50; }`
14.  `</style>`

2\. 在 demo.we 所在目录使用 shell 输入下面命令：

1.  `weex demo.we`

3\. 浏览器会自动打开，也可以使用 PlayGround 应用扫描网页上的二维码在手机上查看。