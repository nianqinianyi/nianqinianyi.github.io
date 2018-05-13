---
title: 【Spring Cloud学习笔记】01：服务注册与发现 (Eureka)
tags:
  - 【Spring Cloud学习笔记】
url: 696.html
id: 696
categories:
  - Spring
date: 2017-06-26 01:37:21
---

教程：[http://blog.csdn.net/forezp/article/details/69696915](http://blog.csdn.net/forezp/article/details/69696915)   eureka是一个服务注册和发现模块，每一个 Eureka Server 也是一个 Eureka Client，至少要指定一个 Server。   一、新建 Eureka 服务注册中心模块步骤

1.  可以使用 IDEA 的 Spring Initializr 更加方便的创建 Eureka 模块。新建 Eureka 模块可选择 Cloud Discovery 下的 Eureka Server。
2.  在Application 类加上 @EnableEurekaServer 注解。
3.  在配置文件中添加配置，eureka.client.registerWithEureka：false和fetchRegistry：false来表明自己是一个eureka server。

配置文件：

    server:
      port: 8000
    eureka:
      instance:
        hostname: localhost
      client:
        registerWithEureka: false
        fetchRegistry: false
        serviceUrl:
          defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/

完成新建 Eureka 模块后，可以访问 [http://localhost:8000/](http://localhost:8000/)  来查看已注册的服务，端口即为配置文件中的端口。

二、新建 Eureka 服务提供者模块步骤
---------------------

1.  可以使用 IDEA 的 Spring Initializr 更加方便的创建 Eureka 模块。新建 Eureka 模块可选择 Cloud Discovery 下的 Eureka Discovery。
2.  在Application 类加上 @EnableEurekaClient 注解。
3.  在配置文件中添加配置，指定应用信息及注册中心地址。

配置文件：

    spring:
      application:
        name: learn-sc-service
    server:
      port: 8101
    eureka:
      client:
        service-url:
          defaultZone: http://localhost:8000/eureka/

在服务提供者中新建 Controller：

Controller 代码：

    package cn.sixlab.learn.spring.cloud.controller;
    
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestParam;
    import org.springframework.web.bind.annotation.RestController;
    
    @RestController
    public class HelloController {
        
        @Value("${server.port}")
        String port;
        
        @RequestMapping("/hello")
        public String home(@RequestParam String name) {
            return "Hello, " + name + " from " + port;
        }
    }

三、测试
----

1.  启动服务注册中心模块，访问 [http://localhost:8000/](http://localhost:8000/)  来查看已注册的服务，显示：No instances available
2.  启动服务提供者模块，访问  [http://localhost:8101/hello?name=Patrick](http://localhost:8101/hello?name=Patrick) ，页面显示 Hello, Patrick from 8101，服务提供者正常启动
3.  再访问[http://localhost:8000/](http://localhost:8000/)来查看已注册的服务，显示了一个已注册的服务提供者：LEARN-SC-SERVICE

四、代码
----

Github 地址：[https://github.com/PatrickRoot/learn-spring-cloud](https://github.com/PatrickRoot/learn-spring-cloud)

对应分支：[https://github.com/PatrickRoot/learn-spring-cloud/tree/lsc01](https://github.com/PatrickRoot/learn-spring-cloud/tree/lsc01)