---
title: 【Spring Cloud学习笔记】03：服务消费者（Feign）
tags: ["Spring", "Spring Cloud"]
categories: ["Spring"]
date: 2017-06-27 00:18:22
description: 本文通过创建Feign服务模块并结合Eureka实现服务发现，演示了如何基于Spring Cloud构建具备负载均衡能力的微服务调用架构。
articleGPT: 文章介绍了如何使用Spring Cloud Feign创建服务消费者模块，步骤包括：通过IDEA创建包含Eureka Discovery、Web和Feign依赖的项目，在Application类添加@EnableDiscoveryClient和@EnableFeignClients注解，配置Eureka注册中心地址；定义Feign客户端接口调用服务提供者接口，编写Controller调用Feign接口；启动注册中心、服务提供者和服务消费者后，通过访问特定URL测试服务调用，结果会轮询显示不同服务实例的响应，附有GitHub代码仓库地址。
---

教程：<http://blog.csdn.net/forezp/article/details/69808079>  

## 一、创建 Feign 服务模块

  1. 使用 IDEA 的 Spring Initializr 模块。选择 Cloud Discovery 下的 Eureka Discovery、Web 下的 Web和 Cloud Routing 下的 Feign 共3个依赖。
  2. 在Application 类加上 @EnableDiscoveryClient 注解和 @EnableFeignClients 注解。
  3. 在配置文件中添加配置，指定应用信息及注册中心地址。

配置文件：

```yaml
spring:
  application:
    name: learn-sc-service-feign
server:
  port: 8300
eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8000/eureka/
```

## 二、编写调用代码

定义 Feign 接口，来指定调用服务。

IHelloService 代码：

```Java
package cn.sixlab.learn.spring.cloud.inter;

import org.springframework.cloud.netflix.feign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@FeignClient(value = "learn-sc-service")
public interface IHelloService {
    @RequestMapping("/hello")
    String sayHiFromClientOne(@RequestParam(value = "name")String name);
}
```

编写 Controller，来调用接口。

  HelloController 代码：

```Java
package cn.sixlab.learn.spring.cloud.controller;

import cn.sixlab.learn.spring.cloud.inter.IHelloService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @Autowired
    IHelloService helloService;

    @RequestMapping(value = "/hi", method = RequestMethod.GET)
    public String sayHi(@RequestParam String name) {
        return helloService.sayHiFromClientOne(name);
    }
}
```

## 三、测试

  1. 启动 learn-sc-server 注册中心。
  2. 启动 learn-sc-service01 服务提供者。
  3. 启动 learn-sc-service02 服务提供者。
  4. 启动 learn-sc-service-feign 服务消费者。
  5. 访问 `http://localhost:8300/hi?name=Sixlab` ，多次刷新，显示的输出分别为：Hello, Sixlab from 8101 和 Hello, Sixlab from 8102

## 四、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc03>

