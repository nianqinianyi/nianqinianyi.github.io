---
title: Centos 7 开发环境之 Redis 的安装及配置
tags: ["CentOS", "Redis", "运维"]
categories: ["运维"]
date: 2017-11-22 00:39:39 +08:00
description: 本文记录了服务器上 Redis 软件的下载、编译、安装及配置的详细步骤。
articleGPT: 文章详细记录了在服务器上下载、编译、安装及配置 Redis 的完整过程，包括设置开机启动、后台运行、允许远程访问和密码保护。
---

最近需要在服务器上安装 MySQL、MongoDB、Redis 和 ELK 等，记录一下过程，防止下次继续踩坑。  

# 一、下载 Redis 的源码包

  1. 访问 <https://redis.io/download> ，在 Download 按钮上右键复制链接地址并下载：`http://download.redis.io/releases/redis-4.0.2.tar.gz `
  2. SSH 连上服务器，运行命令：`wget http://download.redis.io/releases/redis-4.0.2.tar.gz `

# 二、编译 Redis

  1. 安装 gcc 环境，如果已安装，可以跳过`yum install gcc-c++ `
  2. 解压 Redis 源码，并进入源码目录`tar -zxvf redis-4.0.2.tar.gz cd redis-4.0.2 `
  3. make 编译 Redis`make MALLOC=libc `
  4. 安装 Redis`make install `
  5. 配置 Redis 开机启动`./utils/install_server.sh `
  6. 开启、关闭 Redis
  
```shell
service redis_6379 start
/etc/init.d/redis_6379 start
service redis_6379 stop
/etc/init.d/redis_6379 stop
```

# 三、修改配置文件

  1. 根据`install_server.sh`运行结果可知配置文件在`/etc/redis/6379.conf`，打开并编辑。
  2. 设置 Redis 在后台运行，找到`daemonize`，将值改为`yes`。
  3. 运行其他机器访问，注释掉 `bind 127.0.0.1`。
  4. 设置访问密码，找到`requirepass`，改为`requirepass my_pwd`。
