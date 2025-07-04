---
title: Centos 7 开发环境之 MongoDB 的安装及配置(yum源)
tags: ["CentOS", "MongoDB", "运维"]
categories: ["运维"]
date: 2017-11-22 00:38:50 +08:00
description: 记录了在服务器上安装、配置MongoDB及用户授权的详细过程，以避免未来重复踩坑。
articleGPT: 本文详细记录了在服务器上安装和配置 MongoDB 的过程，包括添加 YUM 源、执行安装、调整网络访问（bindIp）以及设置用户授权。
---

最近需要在服务器上安装 MySQL、MongoDB、Redis 和 ELK 等，记录一下过程，防止下次继续踩坑。  

# 一、添加 MongoDB 的源

  1. 进入yum源配置的目录`cd /etc/yum.repos.d/ `
  2. 创建 MongoDB 源文件并编辑`touch mongodb-org-3.4.repo`，然后`vi mongodb-org-3.4.repo `
  3. 源文件中添加如下内容
```
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=0
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc
```
  4. 更新源`yum update `

# 二、安装 MongoDB

  1. 使用命令安装 MongoDB`yum install -y mongodb-org `
  2. 查找 MongoDB 目录`whereis mongod `

# 三、配置 MongoDB

  1. 默认外网无法访问 MongoDB，一个是防火墙的原因，关掉就好了，一个是需要修改 MongoDB 配置文件，修改`/etc/mongod.conf`文件，将bindIp值修改如下`bindIp: 0.0.0.0 `
  2. 启动、关闭、设置开机启动、取消开机启动 MongoDB 命令

```shell
systemctl start mongod
systemctl stop mongod
systemctl enable mongod
systemctl disable mongod
```

# 四、配置用户授权

默认配置下，用户不需要授权，直接访问 MongoDB 即可链接。添加用户授权步骤如下：

  1. 先无授权启动 MongoDB，然后连接上 MongoDB：`mongo 127.0.0.1:27017`
  2. 使用如下命令创建一个超级管理员用户，之后创建新用户就可以使用管理员连接上 MongoDB 然后去创建：`use admin; db.createUser({user:'root',pwd:'root',roles:[{ "role" : "root", "db" : "admin" }]}); `
  3. 修改 `/etc/mongod.conf` 文件，取消 `security` 前的注释，并添加 `authorization`，如下`security: authorization: enabled `
  4. 启动 MongoDB 服务器即可。
