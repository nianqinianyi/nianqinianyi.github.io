---
title: 【Spring Cloud学习笔记】06：分布式配置中心（Spring Cloud Config）
tags: ["Spring", "Spring Cloud"]
categories: ["Spring"]
date: 2017-06-30 00:24:06
description: 文章演示了如何通过Spring Cloud Config Server与Client，实现应用配置在Git仓库中的集中管理与动态获取。
articleGPT: 本教程阐述了如何通过Spring Cloud Config实现服务配置的集中管理与实时更新，即由Config Server从Git仓库统一拉取配置，并由Config Client端动态获取使用。
---

教程：<http://blog.csdn.net/forezp/article/details/70037291>

目的：为了统一管理大量的服务，并做到实时更新。可放到内存中，可放到 Git 中。  
  
有两个角色：config server，config client

## 一、 创建 Config Server 模块

  1. 使用 IDEA 的 Spring Initializr 模块。选择 Cloud Discovery 下的 EurekaDiscovery 和 Cloud Config 下的 Config Server 共2个依赖。
  2. 在Application 类加上 @EnableConfigServer 注解。
  3. 在配置文件中添加配置，指定应用信息及 Git 信息。

配置文件：

```yaml
spring:
  application:
    name: learn-sc-config-server
  cloud:
    config:
      label: master
      server:
        git:
          uri: https://github.com/nianqinianyi/demo-spring-cloud
          search-paths: config
#          username:公开仓库不需要用户名
#          password:公开仓库不需要密码
server:
  port: 8500
```

在 Git 仓库中添加配置文件：

learn-sc-config-client-dev.properties 文件：

```properties
foo = foo version 1
hello.message = hello world
```

## 二、测试

  1. 启动 learn-sc-config-server
  2. 访问 `http://localhost:8500/learn-sc-config-client/dev`
  3. 页面显示 XML 或者 JSON

XML 显示如下：

```XML
<Environment>
    <name>config-client</name>
    <profiles>
        <profiles>dev</profiles>
    </profiles>
    <label/>
    <version>7a7859fbfb5530a29ba5d3c30cb89386ff333cf4</version>
    <state/>
    <propertySources>
        <propertySources>
            <name>
                https://github.com/nianqinianyi/demo-spring-cloud/config/config-client-dev.properties
            </name>
            <source>
                <hello.message>hello world</hello.message>
                <foo>foo version 1</foo>
            </source>
        </propertySources>
    </propertySources>
</Environment>
```

## 三、解释

http 请求路径为：/{application}/{profile}[/{label}]

资源文件与请求路径的匹配规则为：

  * /{application}-{profile}.yml
  * /{label}/{application}-{profile}.yml
  * /{application}-{profile}.properties
  * /{label}/{application}-{profile}.properties

## 四、创建 Config Client 模块

  1. 使用 IDEA 的 Spring Initializr 模块。选择 Web 下的 web 和 Cloud Config 下的 Config Client 共2个依赖。
  2. 在配置文件中添加配置，指定应用信息及 Git 信息。**注意：application.(properties|yaml) 和 bootstrap**.(properties|yaml)两类配置文件时不同的，application 里面配置的大部分都有用，但是 spring.cloud.config.uri 必需配置在 bootstrap 才生效，否则它会使用 `http://localhost:8888/` 这个值**  。**

配置文件（application.yaml）：

```yaml
spring:
  application:
    name: learn-sc-config-client
  cloud:
    config:
      label: master
      profile: dev
server:
  port: 8600
```

配置文件(bootstrap.yaml)：

```yaml
spring:
  cloud:
    config:
      uri: http://localhost:8500/
```

新建 Controller 类，代码如下：

```Java
package cn.sixlab.learn.spring.cloud.learnscconfigclient.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ValueController {

    @Value("${foo}")
    String foo;

    @Value("${hello.message}")
    String hello;

    @RequestMapping(value = "/foo")
    public String foo() {
        return foo;
    }

    @RequestMapping(value = "/hello")
    public String hello() {
        return hello;
    }
}
```

## 五、测试

  1. 启动 learn-sc-config-server 模块
  2. 启动 learn-sc-config-client 模块
  3. 访问 `http://localhost:8600/foo` ，页面显示：foo version 1
  4. 访问 `http://localhost:8600/hello` ，页面显示：hello world

## 六、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc06>
