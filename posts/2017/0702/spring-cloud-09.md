---
title: 【Spring Cloud学习笔记】09：服务链路追踪(Spring Cloud Sleuth)
tags: ["Spring Cloud"]
categories: ["Spring"]
date: 2017-07-02 00:27:11
description: 本教程详细演示了如何通过搭建Zipkin服务器并配置互相调用的服务，利用Spring Cloud Sleuth实现分布式服务链路追踪。
articleGPT: 该教程详细介绍了如何集成Spring Cloud Sleuth和Zipkin，以实现分布式服务链路的追踪与可视化。
---

教程：<http://blog.csdn.net/forezp/article/details/70162074>

Spring Cloud Sleuth 继承了服务链路追踪组件 Zipkin。  

## 一、创建 Zipkin Server 模块

  1. 使用 IDEA 的 Spring Initializr 创建 learn-sc-server-zipkin 模块。选择Web 下的 Web。
  2. 修改 pom.xml 添加 spring-boot-starter、zipkin-server 和 zipkin-autoconfigure-ui 的依赖。
  3. 在 Application 类上添加 @EnableZipkinServer 注解。
  4. 修改 application.yaml 文件：`server: port: 8800 `

## 二、创建两个有调用关系的 Service 模块

* * *

  1. 使用 IDEA 的 Spring Initializr 模块。选择Web 下的 Web、Cloud Tracking 下的 Zipkin Client。
  2. 修改 application.yaml 文件：
```
spring:
  zipkin:
    base-url: http://localhost:8800
  application:
    name: learn-sc-service03
server:
  port: 8103
```
  3. 再创建一个使用 8104端口的 learn-sc-service04 模块。

在learn-sc-service03 模块中创建 Controller：

```java
package cn.sixlab.learn.spring.cloud.learnscservice03.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.sleuth.sampler.AlwaysSampler;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.logging.Level;
import java.util.logging.Logger;

@RestController
public class Service03Controller {
    private static final Logger LOG = Logger.getLogger(Service03Controller.class.getName());

    @Autowired
    private RestTemplate restTemplate;

    @Bean
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }

    @RequestMapping("/hi")
    public String callHome() {
        LOG.log(Level.INFO, " 03/hi is being called, next-> ");
        return restTemplate.getForObject("http://localhost:8104/hi04", String.class);
    }

    @RequestMapping("/hi03")
    public String info() {
        LOG.log(Level.INFO, " 03/hi03 is being called ");

        return "hi03 is service from 03";
    }

    @Bean
    public AlwaysSampler defaultSampler() {
        return new AlwaysSampler();
    }
}
```

在learn-sc-service03 模块中创建 Controller：

```Java
package cn.sixlab.learn.spring.cloud.learnscservice04.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.logging.Level;
import java.util.logging.Logger;

@RestController
public class Service04Controller {
    private static final Logger LOG = Logger.getLogger(Service04Controller.class.getName());

    @Autowired
    private RestTemplate restTemplate;

    @Bean
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }

    @RequestMapping("/hi")
    public String home() {
        LOG.log(Level.INFO, " 04/hi is being called ");
        return "hi is service from 04";

    }

    @RequestMapping("/hi04")
    public String info() {
        LOG.log(Level.INFO, " 04/hi04 is being called, next-> ");
        return restTemplate.getForObject("http://localhost:8103/hi03", String.class);
    }
}
```

## 四、测试

  1. 启动 learn-sc-server-zipkin
  2. 启动 learn-sc-service03 模块
  3. 启动 learn-sc-service04 模块
  4. 访问 `http://localhost:8800/zipkin/` 并点击“Find Traces”按钮 和 `http://localhost:8800/zipkin/dependency` 查看依赖关系，数据为空
  5. 依次访问 `http://localhost:8103/hi03` 、`http://localhost:8104/hi` 、`http://localhost:8104/hi04` 、`http://localhost:8103/hi` ，每次访问后进行第4步查看依赖关系。

## 五、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc09>
