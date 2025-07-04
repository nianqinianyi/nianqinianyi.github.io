---
title: Centos 7 开发环境之 Gogs 的安装及配置（二进制）
tags: ["CentOS", "Git", "Gogs", "运维"]
categories: ["运维"]
date: 2018-06-07 00:52:52 +08:00
description: 详述了在服务器上安装和配置Gogs这一轻量级Git服务器的整个过程，以此替代繁琐的GitLab。
articleGPT: 本文记录了因Gitlab过于臃肿复杂而转用Gogs，并在服务器上下载、配置及启动这个轻量级Git服务端的详细过程。
---

最近需要在服务器上安装了 Git 服务器，本来安装了Gitlab，但是太重了，还集成了Nginx
Gem一堆东西，改个端口都特别麻烦还报502错误，所以换成了 Gogs，简单好用，记录一下过程，防止下次继续踩坑。  

# 一、下载并配置

  1. 访问官网，打开二进制安装页面：`https://gogs.io/docs/installation/install_from_binary#官网`

  1. 找到 linux 64位服务器的tar包，当前最新版本`0.11.53 @ 2018-06-05`，复制下载地址：`https://dl.gogs.io/0.11.53/gogs_0.11.53_linux_amd64.tar.gz`
  2. 在服务器创建 Git 用户并切换至git用户，并访问该用户home目录：`adduser git su git cd ~`
  3. 下载Gogs的tar包`wget https://dl.gogs.io/0.11.53/gogs_0.11.53_linux_amd64.tar.gz`
  4. 解压Gogs的tar包`tar -xzvf gogs_0.11.53_linux_amd64.tar.gz `
  5. 创建Gogs的自定义配置文件：`cd gogs mkdir -p custom/conf cd custom/conf vi app.ini`
  6. 设置端口为自定义端口(例：9000)`[server] HTTP_PORT = 9000`

# 二、安装配置

  1. 使用git用户启动 Gogs 服务器:`cd ~/gogs/ ./gogs web`
  2. 浏览器访问Gogs服务器的安装页面（例：192.168.1.100）`http://192.168.1.100:9000/install`
  3. 浏览器访问Gogs服务器的安装页面（例：192.168.1.100）`http://192.168.1.100:9000/install`
