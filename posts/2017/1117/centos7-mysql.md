---
title: Centos 7 开发环境之 MySQL 5.7 的安装及配置(rpm)
tags: ["CentOS", "MySQL", "运维"]
categories: ["运维"]
date: 2017-11-17 00:37:11 +08:00
description: 本文详细记录了在服务器上安装MySQL的完整过程，包括下载、配置、初始化及用户设置，并提供了针对常见问题的解决方案。
articleGPT: 这篇文章记录了在服务器上安装 MySQL 5.7 的详细过程，包括下载安装包、卸载冲突的 MariaDB、安装、数据库初始化、启动服务以及创建和配置新用户权限等步骤。
---

最近需要在服务器上安装 MySQL、MongoDB、Redis 和 ELK 等，记录一下过程，防止下次继续踩坑。  

# 一、下载 MySQL 安装包

  1. 访问 <https://dev.mysql.com/downloads/mysql/> ，按如下选择：
     1. 操作系统：`Red Hat Enterprise Linux / Oracle Linux`
     2. 版本：`Red Hat Enterprise Linux 7 / Oracle Linux 7 (x86, 64-bit) `
  2. 选择 `RPM Bundle`，点击后边的`download`
  3. 在`No thanks, just start my download`上右键复制链接地址：
     1. `https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.20-1.el7.x86_64.rpm-bundle.tar `
  4. SSH 连上服务器，运行命令：
     1. `wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.20-1.el7.x86_64.rpm-bundle.tar`

# 二、卸载 mariadb

趁着下载文件，卸载一下mariadb。之所以把这一部分单独列出来，是因为踩坑了。当时我安装的时候不知道，结果安装的时候一直提示有错误，原来 Centos 7
上默认安装有 `mariadb-libs`，需要卸载掉。

  1. 运行命令，查看`mariadb-libs`：`rpm -qa | grep mariadb `
  2. 得到`mariadb-libs`的包名，如：`mariadb-libs-5.5.37-1.el7_0.x86_64`，运行命令卸载掉：`rpm -e mariadb-libs-5.5.37-1.el7_0.x86_64 --nodeps `

# 三、安装 Mysql

  1. 解压tar 文件，解压获得12个文件，其中3个`embedded`、2个`minimal`和1个`test`的可以删除，剩余6个：`tar -xvf mysql-5.7.20-1.el7.x86_64.rpm-bundle.tar `
  2. 按照顺序运行下列命令安装即可：
     1. `rpm -ivh mysql-community-common-5.7.20-1.el7.x86_64.rpm`
     2. `rpm -ivh mysql-community-libs-5.7.20-1.el7.x86_64.rpm`
     3. `rpm -ivh mysql-community-libs-compat-5.7.20-1.el7.x86_64.rpm`
     4. `rpm -ivh mysql-community-client-5.7.20-1.el7.x86_64.rpm`
     5. `rpm -ivh mysql-community-server-5.7.20-1.el7.x86_64.rpm`
     6. `rpm -ivh mysql-community-devel-5.7.20-1.el7.x86_64.rpm `

# 四、数据库初始化

  1. 如果是以 root 用户登录，需要`--user`选项，如果是以 mysql 身份运行，则不需要：
     1. `mysqld --initialize --user=mysql `
  2. initialize会以安全模式初始化数据库，然后创建一个默认密码，并标记为过期，需要登录后修改密码。使用下面命令获取密码` cat /var/log/mysqld.log|grep password `
  3. 修改服务器默认端口号，编辑`/etc/my.cnf`文件，在`[mysqld]`下添加一行：` port=9000 `

# 五、启动数据库

  1. 运行命令：`service mysqld start`
  2. 事实上 Centos7已经使用`systemctl` 命令替换掉了`service` 命令，所以也可以用下面命令：`systemctl start mysqld.service `
  3. 使用`systemctl` 命令设置开机启动，取消开机启动用`disable`：`systemctl enable mysqld.service `

# 六、登录数据库

  1. 使用命令登录数据库，密码为初始化数据库时获取的密码`mysql -u root -p `
  2. 修改密码：`SET PASSWORD = PASSWORD("123456"); `

# 七、创建新用户并赋权

  1. 默认的用户 root 不能够远程访问，需要创建一个新用户：
     1. `GRANT ALL PRIVILEGES ON *.* TO "myuser"@"%" IDENTIFIED BY "mypwd";`
     2. 用户 myuser，密码 mypwd，可以远程访问，有所有数据库所有表的权限，比 root 用户只少了一个 grant 权限。
  2. 如果不想给用户这么多权限，只需要增删改查等常规操作，去掉上述命令中的`ALL`
  3. 如果不想给用户所有数据库的权限，那么把上述命令的`*.*`修改为`mydb.*`，则只附于用户`mydb` 这个数据库所有的表的权限。
