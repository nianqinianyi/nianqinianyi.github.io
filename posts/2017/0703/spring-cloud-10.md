---
title: 【Spring Cloud学习笔记】10：断路器监控(Hystrix Dashboard)+断路器聚合监控(Hystrix Turbine)
tags: ["Spring", "Spring Cloud"]
categories: ["Spring"]
date: 2017-07-03 00:28:09 +08:00
description: 文章指导在Spring Cloud应用中集成并配置Hystrix Dashboard以监控断路器数据，以及Hystrix Turbine以聚合多个监控流。
articleGPT: 本教程详细讲解了如何在Spring Cloud项目中，利用Hystrix Dashboard对单个服务，以及Hystrix Turbine对多个微服务的断路器数据进行可视化监控与聚合。
---

教程：
<http://blog.csdn.net/forezp/article/details/70217283>

<http://blog.csdn.net/forezp/article/details/70233227>

Hystrix Dashboard 是断路器的一个组件，提供了数据监控和友好的图形化界面。

Hystrix Turbine 可以聚合多个 Hystrix Dashboard 的数据。

## 一、改造 service01 模块

1. 修改 learn-sc-service01 模块 pom.xml 添加 spring-boot-starter-actuator、spring-cloud-starter-hystrix-dashboard、spring-cloud-starter-hystrix 的依赖。
2. 在 Application 类上添加 @EnableHystrix 注解开启断路器、加上 @EnableHystrixDashboard 组件开启 Dashboard。
3. 再需要的短路点方法上添加 @HystrixCommand 注解，此处是 HelloController 的 “/hello” 的方法。

## 二、测试

1. 启动 learn-sc-server 模块
2. 启动 learn-sc-service01 模块
3. 访问 `http://localhost:8101/hystrix` ，在一个文本框输入 `http://localhost:8101/hystrix.stream` ，点击下方按钮，可以查看数据
4. 访问 `http://localhost:8101/hello?name=Sixlab` ，查看数据变化

## 三、创建 service turbine 模块

1. 使用 IDEA 的 Spring Initializr 创建 learn-sc-service-turbine 模块。选择Spring Circuit Breaker 下的 Turbine 和 Ops 下的 Actuator。
2. 在 Application 类上添加 @EnableTurbine 注解开启 Turbine。
3. application.yaml 内容：

```yaml
spring:
  application.name: learn-sc-service-turbine
server:
  port: 8900
turbine:
  aggregator:
    clusterConfig: default   # 指定聚合哪些集群，多个使用","分割，默认为default。可使用http://.../turbine.stream?cluster={clusterConfig之一}访问
  appConfig: learn-sc-service-01,learn-sc-service-02  ### 配置Eureka中的serviceId列表，表明监控哪些服务
  clusterNameExpression: new String("default")
  # 1. clusterNameExpression指定集群名称，默认表达式appName；此时：turbine.aggregator.clusterConfig需要配置想要监控的应用名称
  # 2. 当clusterNameExpression: default时，turbine.aggregator.clusterConfig可以不写，因为默认就是default
  # 3. 当clusterNameExpression: metadata['cluster']时，假设想要监控的应用配置了eureka.instance.metadata-map.cluster: ABC，则需要配置，同时turbine.aggregator.clusterConfig: ABC
eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8000/eureka/
security:
  basic:
    enabled: false
```

## 四、测试

1. 先将 learn-sc-service02 模块改造，和 learn-sc-service01 一样。
2. 启动 learn-sc-server 模块
3. 启动 learn-sc-service01 模块，启动 learn-sc-service02 模块。
4. 启动 learn-sc-service-turbine 模块。
5. 访问 `http://localhost:8101/hystrix` 或 `http://localhost:8102/hystrix` ，在一个文本框输入 `http://localhost:8900/turbine.stream` ，点击下方按钮，可以查看数据
6. 访问 `http://localhost:8101/hello?name=Sixlab` 或者 `http://localhost:8102/hello?name=Sixlab` ，查看数据变化

## 五、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc10>
