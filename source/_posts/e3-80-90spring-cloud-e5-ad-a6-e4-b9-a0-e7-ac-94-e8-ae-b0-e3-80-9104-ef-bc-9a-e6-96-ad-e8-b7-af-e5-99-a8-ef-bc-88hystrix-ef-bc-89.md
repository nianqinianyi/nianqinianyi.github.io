---
title: 【Spring Cloud学习笔记】04：断路器（Hystrix）
tags:
  - 【Spring Cloud学习笔记】
url: 702.html
id: 702
categories:
  - Spring
date: 2017-06-29 00:29:30
---

教程：[http://blog.csdn.net/forezp/article/details/69934399](http://blog.csdn.net/forezp/article/details/69934399)   为了解决某个服务阻塞，导致故障传递并造成服务器瘫痪。

一、Ribbon 中使用断路器
---------------

1.  在 learn-sc-service-ribbon 模块中添加依赖：spring-cloud-starter-hystrix
2.  在 Application 类上添加@EnableHystrix注解开启Hystrix
3.  修改learn-sc-service-ribbon 模块中的  HelloService 类：

HelloService 类代码：

    package cn.sixlab.learn.spring.cloud.service;
    
    import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Service;
    import org.springframework.web.client.RestTemplate;
    
    @Service
    public class HelloService {
        
        @Autowired
        RestTemplate restTemplate;
        
        @HystrixCommand(fallbackMethod = "helloError")
        public String helloService(String name){
            return restTemplate.getForObject("http://LEARN-SC-SERVICE/hello?name=" + name, String.class);
        }
        
        public String helloError(String name) {
            return "Hello," + name + ", ribbon error!";
        }
    }

二、Feign 中使用断路器
--------------

1.  Feign 自带断路器，修改配置文件打开断路器，添加：feign.hystrix.enabled=true
2.  新建错误处理类 HelloServiceError，实现 IHelloService 接口。
3.  在 IHelloService 接口的 @FeignClient 注解中添加 fallback 参数，指定错误处理类 HelloServiceError.class

配置文件添加内容：

    feign:
      hystrix:
        enabled: true

HelloServiceError 类的代码：

    package cn.sixlab.learn.spring.cloud.error;
    
    import cn.sixlab.learn.spring.cloud.inter.IHelloService;
    import org.springframework.stereotype.Component;
    
    @Component
    public class HelloServiceError implements IHelloService{
        @Override
        public String sayHiFromClientOne(String name) {
            return "Hello," + name + ", feign error!";
        }
    }

IHelloService 接口的注解部分修改：

    @FeignClient(value = "learn-sc-service", fallback = HelloServiceError.class)
    public interface IHelloService {...}

三、Hystrix Dashboard 仪表盘
-----------------------

1.  在learn-sc-service-ribbon 和 learn-sc-service-feign 添加依赖spring-boot-starter-actuator和spring-cloud-starter-hystrix-dashboard
2.  在 Application 类添加@EnableHystrixDashboard注解，开启hystrixDashboard
3.  访问 [http://localhost:8200/hystrix](http://localhost:8200/hystrix)  或者 [http://localhost:8300/hystrix](http://localhost:8300/hystrix)
4.  输入 [http://localhost:8200/hystrix.stream](http://localhost:8200/hystrix.stream)  或者 [http://localhost:8300/hystrix.stream](http://localhost:8300/hystrix.stream)  点击 Monitor Stream 进入监控

三、测试
----

1.  启动 learn-sc-server 注册中心。
2.  启动 learn-sc-service01 服务提供者。
3.  启动 learn-sc-service-ribbon 服务消费者。
4.  启动 learn-sc-service-feign 服务消费者。
5.  访问 [http://localhost:8200/hi?name=Patrick](http://localhost:8200/hi?name=Patrick) ，多次刷新，显示的输出为：Hello, Patrick from 8101
6.  访问 [http://localhost:8300/hi?name=Patrick](http://localhost:8300/hi?name=Patrick)  ，多次刷新，显示的输出为：Hello, Patrick from 8101
7.  关闭 learn-sc-service01
8.  访问[http://localhost:8200/hi?name=Patrick](http://localhost:8200/hi?name=Patrick)，显示为：Hello, Patrick, ribbon error!
9.  访问[http://localhost:8300/hi?name=Patrick](http://localhost:8300/hi?name=Patrick)，显示为：Hello, Patrick, feign error!

四、代码
----

Github 地址：[https://github.com/PatrickRoot/learn-spring-cloud](https://github.com/PatrickRoot/learn-spring-cloud)

对应分支：[https://github.com/PatrickRoot/learn-spring-cloud/tree/lsc04](https://github.com/PatrickRoot/learn-spring-cloud/tree/lsc04)