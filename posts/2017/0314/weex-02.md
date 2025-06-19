---
title: Weex 入门02 - 创建项目
tags: []
categories: ["其他"]
date: 2017-03-14 23:52:10
description: 介绍Weex项目的初始化、依赖安装和启动运行步骤。
articleGPT: 本文介绍了Weex项目从初始化、安装依赖到启动服务的整个过程所需命令。
---

1\. 使用命令初始化项目：  

```shell
weex init
```

2\. 安装依赖，进入项目目录，使用 npm 命令安装依赖

```shell
npm install
```

3\. 启动 Server

```shell
npm run build // 编译`
npm run dev //webpack 监听，可以自动监听修改`
npm run serve //启动服务,可修改 package.json 对应命令来修改端口`
npm run test`
```

访问： `http://localhost:8080`
