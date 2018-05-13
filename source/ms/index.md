---
title: Minesite
url: 840.html
id: 840
comments: false
date: 2017-10-25 13:40:36
---

Minesite
========

由于`GitHub`国内访问不畅，所以两个 Git 仓库作同步： 码云：[https://gitee.com/PatrickRoot/Minesite](https://gitee.com/PatrickRoot/Minesite "码云 Git 地址") GitHub：[https://github.com/PatrickRoot/Minesite](https://github.com/PatrickRoot/Minesite "GitHub")

Minesite
========

基于 Spring Boot 开发的插件式网站，理想的拓展方式是：加新功能只需要引用新 jar 包。 之前正在用 Spring Cloud 实现一个MinesiteX([Github](https://github.com/PatrickRoot/MinesiteX)、[Gitee 码云](https://gitee.com/PatrickRoot/MinesiteX))，其实更符合我的想法，仍在继续缓慢更新，但是微服务要启动的东西还是太多，我担心我的服务器要爆掉，用 Spring Boot 实现一个 lite 版。

### Minesite 需求

开发这个项目的主要目的是为了满足自己的以下几个需求：

*   个人网站，不需要复杂的用户管理，一个账号即可。
*   页面管理，可以添加、修改、删除页面。
*   菜单管理，增删改菜单。
*   方便添加一些额外的新功能，不影响原有系统及功能的使用。

### Minesite 模块

各模块如下：

*   mine-site 是 parent 模块，管理依赖和所有模块
*   ms-lib-XXX 是一些公用模块
    *   ms-lib-core 是基本模块，含一些基本的 bean 和 util 类
*   待定

技术栈
===

*   Spring Boot
*   Thymeleaf
*   MongoDB
*   待定

版本规划
====

*   \[X\] V0.1.0 完成基本的初始化
*   \[ \] V0.2.0 完成登录功能及其页面
*   \[ \] V0.3.0 完成页面的管理
*   \[ \] V0.5.0 完成菜单的管理
*   \[ \] V1.0.0 基本功能完成