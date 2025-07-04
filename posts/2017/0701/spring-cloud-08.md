---
title: 【Spring Cloud学习笔记】08：消息总线(Spring Cloud Bus)
tags: ["Spring", "Spring Cloud"]
categories: ["Spring"]
date: 2017-07-01 00:25:45 +08:00
description: 文章探讨了 Spring Cloud Bus 如何利用消息代理（如 RabbitMQ）实现分布式服务配置的动态刷新，无需重启应用。
articleGPT: 该教程演示了如何通过Spring Cloud Bus和RabbitMQ，实现Spring Cloud Config Client动态刷新配置，而无需重启服务。
---

教程：<http://blog.csdn.net/forezp/article/details/70148235>

Spring cloud bus通过轻量消息代理连接各个分布的节点。本例使用 RabbitMq，使用前需要先弄好 RabbitMq。  

## 一、改造 Config Client 模块

  1. 修改 learn-sc-config-client 的 pom.xml 添加 spring-cloud-starter-bus-amqp 依赖
  2. 修改 learn-sc-config-client 的代码，给需要刷新参数值的类加上 @RefreshScope 注解，例：ValueController 类。
  3. 修改learn-sc-config-client 的 application.yaml 文件为，（其中 rabbitmq 默认就是下面的配置，默认配置的时候可以不配置）：

```yaml
spring:
  application:
    name: learn-sc-config-client
  cloud:
    config:
      label: master
      profile: dev
  rabbitmq:
    host: localhost
    port: 5672
    username: guest
    password: guest
  management:
    security:
      enabled: false
  server:
    port: 8600
```

* * *

  1. 启动 learn-sc-server-config 注册中心
  2. 启动 learn-sc-config-server 模块并等待一小会儿（不然，启动3的时候会报错）
  3. 启动 learn-sc-config-client 模块
  4. 访问 `http://localhost:8600/foo` ，页面显示：foo version 1
  5. 提交代码修改 git 仓库中 foo 参数的值，例：foo=foo version 2
  6. 访问 `http://localhost:8600/foo` ，页面显示：foo version 1
  7. 使用工具发送 POST 请求至 `http://localhost:8600/bus/refresh`
  8. 访问 `http://localhost:8600/foo` ，页面显示：foo version 2

## 三、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc08>
