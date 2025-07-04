---
title: 【Spring Cloud学习笔记】07：高可用的分布式配置中心(Spring Cloud Config)
tags: ["Spring", "Spring Cloud"]
categories: ["Spring"]
date: 2017-06-30 00:25:00 +08:00
description: 本文详细介绍了如何将Spring Cloud配置中心（Config Server）及其客户端（Config Client）注册到Eureka服务注册中心，以实现服务发现和动态配置。
articleGPT: 本教程详细指导了如何将Spring Cloud配置中心（Config Server）和配置客户端（Config Client）与Eureka注册中心集成，以实现配置服务的微服务化、动态发现和集群部署。
---

教程：<http://blog.csdn.net/forezp/article/details/70037513>

服务实例多的时候，可以将配置中心做成微服务，集群部署  

## 一、创建 配置中心 Eureka 注册中心模块

  1. 使用 IDEA 的 Spring Initializr 模块。选择 Cloud Discovery 下的 Eureka Server、Web 下的 Web共2个依赖。
  2. 在Application 类加上 @EnableEurekaServer 注解。
  3. 在配置文件中添加配置，指定应用信息。

配置文件：

```yaml
server:
  port: 8700
eureka:
  instance:
    hostname: localhost
  client:
    register-with-eureka: false
    fetch-registry: false
    service-url:
      defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
```

## 二、改造 Config Server 模块

  1. 如果没有，修改 learn-sc-config-server 的 pom.xml 添加 spring-cloud-starter-eureka 依赖（第六节创建的时候应该已经添加了）。
  2. 在Application 类加上 @EnableEurekaClient注解
  3. 修改 learn-sc-config-server的 application.yaml ，添加注册中心地址。
```yaml
server:
  port: 8600
spring:
  application:
    name: learn-sc-config-server
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8700/eureka/
```
  4. 重启 learn-sc-config-server 模块。

## 三、改造 Config Client 模块

* * *

  1. 修改 learn-sc-config-client 的 pom.xml 添加 spring-cloud-starter-eureka 依赖
  2. 修改learn-sc-config-client 的 bootstrap.yaml 文件为：

```yaml
spring:
  application:
    name: learn-sc-config-client
  cloud:
    config:
      label: master
      profile: dev
      discovery:
        enabled: true
        service-id: learn-sc-config-server
  eureka:
    client:
      service-url:
        defaultZone: http://localhost:8700/eureka/
```

* * *

  1. 启动 learn-sc-server-config 注册中心
  2. 启动 learn-sc-config-server 模块并等待一小会儿
  3. 启动 learn-sc-config-client 模块
  4. 访问 `http://localhost:8600/foo` ，页面显示：foo version 1
  5. 访问 `http://localhost:8600/hello` ，页面显示：hello world

## 五、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc07>
