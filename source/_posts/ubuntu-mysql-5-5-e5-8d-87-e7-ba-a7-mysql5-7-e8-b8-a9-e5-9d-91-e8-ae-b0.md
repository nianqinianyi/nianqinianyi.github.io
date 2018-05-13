---
title: Ubuntu Mysql 5.5升级 Mysql5.7踩坑记
url: 643.html
id: 643
categories:
  - 其他
date: 2017-04-18 00:41:49
tags:
---

由于 Mysql5.7支持 Json 格式字段，为了试验新功能，准备把我的阿里云服务器上的 Mysql 数据库升级一下，查了一下数据库版本，我勒个去，是5.5版本的，网上一搜教程，全是5.6升级5.7的，只能看着这些教程踩踩坑了。

1.备份 MySQL 数据
-------------

其实不备份应该问题不太，但是备份的话，万一出问题有数据可以恢复。 假定备份目录在 /backup。

### 1.1 备份配置文件

 	sudo tar cvfvz /backup/mysql_conf.tgz /etc/mysql

1.2 备份数据库表和数据

 	sudo sh -c 'mysqldump -u root -p -A --events > /backup/backup_db.sql'
 	sudo tar cvfvz /backup/mysql_data.tgz /var/lib/mysql

2\. 卸载旧版本 MySQL
---------------

### 2.1 停止 mysql

 	sudo service mysql stop

### 2.2 卸载 Mysql

 	sudo apt-get remove mysql-server mysql-client mysql-common

这一步有些要注意的，因为除了上边几个包，还有 mysql-server-5.5,mysql-server-core-5.5......等一大堆的包，建议使用下面的命令查一下一起卸载，多运行几次，直到没有包可以卸载了

 	dkpg -l|grep mysql

此命令查出来的所有包基本都要卸载，除了 php-mysql。没有包可卸载后，运行下面的命令，注意，不能使用 purge 选择，否则配置文件及数据也会被清除  

 	sudo apt-get autoremove
 	sudo apt-get autoclean

3\. 安装新版本 Mysql
---------------

### 3.1 下载最新版本 MySql 包

去 Mysql 官网找到 Ubuntu 14.04下的所有包，下载 bundle 版本，就是最大的那个，是一个 tar 格式压缩包。

### 3.2 安装依赖包

 	sudo apt-get install libaio1
 	sudo apt-get install libmecab2

### 3.3 解压并安装 MySql

按照参考文章\[2\]中的顺序依次使用 dkpg 安装：

 	dkpg-i mysql-common\_5.7.18-1ubuntu14.04\_amd64.deb
 	dkpg-i libmysqlclient20\_5.7.18-1ubuntu14.04\_amd64.deb
 	dkpg-i libmysqlclient-dev\_5.7.18-1ubuntu14.04\_amd64.deb
 	dkpg-i libmysqld-dev\_5.7.18-1ubuntu14.04\_amd64.deb
 	dkpg-i mysql-community-client\_5.7.18-1ubuntu14.04\_amd64.deb
 	dkpg-i mysql-client\_5.7.18-1ubuntu14.04\_amd64.deb
 	dkpg-i mysql-community-source\_5.7.18-1ubuntu14.04\_amd64.deb
 	dkpg-i mysql-community-server\_5.7.18-1ubuntu14.04\_amd64.deb

### 3.4 升级 Mysql 数据库

 	mysql-upgrade -p

这句命令会使用 root 用户升级 mysql 的数据

4\. 坑
-----

### 4.1 升级完成，远程无法连接

去 /etc/mysql/mysql.conf.d/mysqld.cnf 文件中，把下面一行话注释掉

 	bind-address = 127.0.0.1

### 4.2 mysql-upgrade报错

 	error    : Table rebuild required. Please do "ALTER TABLE \`wp_comments\` FORCE" or dump/reload to fix it! 

原因：5.7不允许 datetime 字段的默认值是 0000-00-00 00:00:00 ，但是 WordPress 有几张表的部分字段默认值是0000-00-00 00:00:00 。

使用下面语句修改下

 	ALTER TABLE wp_comments                                                                                                                                                                             
 	ALTER COLUMN comment_date  SET DEFAULT '1970-01-01 00:00:01',                                                                                                                                                                  
 	ALTER COLUMN comment\_date\_gmt  SET DEFAULT '1970-01-01 00:00:01';     

  主要参考文章： \[1\]:教你在 Debian 和 Ubuntu 上升级 MySQL：[http://www.linuxidc.com/Linux/2014-01/95181.htm](http://www.linuxidc.com/Linux/2014-01/95181.htm) \[2\]:ubuntu14.04上安装Mysql-5.7.11：[http://jingyan.baidu.com/article/4f7d5712d5f8181a2019270e.html](http://jingyan.baidu.com/article/4f7d5712d5f8181a2019270e.html) \[3\]: mysql 5.7.16 远程连接：[http://www.cnblogs.com/Nice-Boy/p/6224189.html](http://www.cnblogs.com/Nice-Boy/p/6224189.html)