---
title: Weex 入门01 - 环境搭建与初步体验
tags: ["Weex", "APP开发"]
categories: ["APP开发"]
date: 2017-03-14 23:51:25 +08:00
description: 详细介绍了Weex开发环境的配置、工具的安装以及快速创建和运行Weex应用示例的步骤。
articleGPT: 本文介绍了安装Weex开发工具、创建.we文件以及在浏览器或手机上快速预览其运行效果的步骤。
---

一、开发工具 Intellij IDEA IDEA 中的两个 Weex 插件  
  
二、安装环境

  1. 安装 node.js，官网下载，一步到底安装。
  2. 使用 npm 安装 weex-toolkit，在 shell 输入下面的命令：` npm install -g weex-toolkit` `

三、快速体验

1. 创建一个文件：demo.we。

```html
<template>
  <div class="container" >
    <div class="cell">
      <image class="thumb" src="https://oh7gzl219.qnssl.com/logo.png"></image>
      <text class="title">六楼实验室：https://blog.sixlab.cn/</text>
    </div>
  </div>
</template>

<style>
.cell{margin-top:10 ; margin-left:10 ; flex-direction: row; }
.thumb {width: 200; height: 200; }
.title {text-align: center ; flex: 1; color: grey; font-size: 50; }
</style>
```

2. 在 demo.we 所在目录使用 shell 输入下面命令：

```shell
weex demo.we
```

3. 浏览器会自动打开，也可以使用 PlayGround 应用扫描网页上的二维码在手机上查看。
