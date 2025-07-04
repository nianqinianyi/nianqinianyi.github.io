---
title: 【Spring Cloud学习笔记】02：服务消费者（rest+ribbon）
tags: ["Spring", "Spring Cloud"]
categories: ["Spring"]
date: 2017-06-26 00:16:01 +08:00
description: 本文详细介绍了如何在Spring Cloud中，通过Ribbon与RestTemplate实现客户端负载均衡的服务调用。
articleGPT: 本文详细演示了如何在Spring Cloud中，通过配置多个服务提供者和使用带有Ribbon客户端负载均衡的RestTemplate，实现客户端负载均衡的服务调用。
---

教程：<http://blog.csdn.net/forezp/article/details/69788938> Spring Cloud
有两种服务调用方式：  

  1. ribbon+restTemplate，ribbon 是一种负载均衡客户端
  2. feign，默认集成了 ribbon

## 〇、添加多个服务提供者模块

  1. 复制上节建立的 learn-sc-service01 模块，命名模块为 learn-sc-service02。
  2. learn-sc-service02 的配置文件中：端口使用8102。其他不作修改。包括 spring.application.name 要和 learn-sc-service01 一样。

## 一、新建 Ribbon 服务消费者模块

  1. 使用 IDEA 的 Spring Initializr 模块。选择 Cloud Discovery 下的 Eureka Discovery、Web 下的 Web和 Cloud Routing 下的 Ribbon 共3个依赖。
  2. 在Application 类加上 @EnableDiscoveryClient注解。
  3. 通过 IOC 注入一个 bean：restTemplate；通过 LoadBalanced 注解表明这个 restTemplate 开启负载均衡。
  4. 在配置文件中添加配置，指定应用信息及注册中心地址。

Application 代码：

```Java
package cn.sixlab.learn.spring.cloud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

@EnableDiscoveryClient
@SpringBootApplication
public class LearnScServiceRibbonApplication {

    public static void main(String[] args) {
        SpringApplication.run(LearnScServiceRibbonApplication.class, args);
    }

    @Bean
    @LoadBalanced
    RestTemplate restTemplate(){
        return new RestTemplate();
    }
}
```

配置文件：

```yaml
spring:
  application:
    name: learn-sc-service-ribbon
server:
  port: 8200
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8000/eureka/
```

## 二、编写调用的代码

新建 Service，通过注入的 restTemplate 来消费 service01 服务的 /hello 接口。新建 Controller，调用
service。

Service 代码：

```Java
package cn.sixlab.learn.spring.cloud.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class HelloService {

    @Autowired
    RestTemplate restTemplate;

    public String helloService(String name){
        return restTemplate.getForObject("http://LEARN-SC-SERVICE/hello?name=" + name, String.class);
    }
}
```

Controller 代码：

```Java
package cn.sixlab.learn.spring.cloud.controller;

import cn.sixlab.learn.spring.cloud.service.HelloService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Autowired
    HelloService helloService;

    @RequestMapping(value = "/hi")
    public String hi(@RequestParam String name) {
        return helloService.helloService(name);
    }
}
```

## 三、测试

  1. 启动上节建立的 learn-sc-server 注册中心。
  2. 启动 learn-sc-service01 服务提供者。
  3. 启动 learn-sc-service02 服务提供者。
  4. 启动 learn-sc-service-ribbon 服务消费者。
  5. 访问 `http://localhost:8000/` ，可以看到LEARN-SC-SERVICE 有2个服务提供者，分别是8101端口和8102端口的。
  6. 访问 `http://localhost:8200/hi?name=Sixlab` ，多次刷新，显示的输出分别为：Hello, Sixlab from 8101 和 Hello, Sixlab from 8102

## 四、解释

  1. service01、service02、servicer-ribbon 在启动时候，向 Eureka Server 注册，并获取服务提供者的信息。
  2. 用户访问servicer-ribbon时，restTemplate 通过 ribbon 负载均衡直接调用 service01、service02，不经Eureka Server。

## 五、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc02>
