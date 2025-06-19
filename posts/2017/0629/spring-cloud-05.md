---
title: 【Spring Cloud学习笔记】05：路由网关（zuul）
tags: ["Spring", "Spring Cloud"]
categories: ["Spring"]
date: 2017-06-29 00:20:21
description: 文章详细介绍了如何创建Spring Cloud Zuul路由模块，实现微服务间的API网关路由，并演示了如何添加自定义请求过滤器进行访问控制。
articleGPT: 该文章详细介绍了如何创建Spring Cloud Zuul路由模块，实现对不同微服务的请求转发（如Ribbon和Feign），并演示了如何通过自定义过滤器进行请求预处理和访问控制。
---

教程：<http://blog.csdn.net/forezp/article/details/69939114>  

## 一、创建 Zuul 路由模块

  1. 使用 IDEA 的 Spring Initializr 模块。选择 Cloud Discovery 下的 Eureka Discovery、Web 下的 Web和 Cloud Routing 下的 Zuul 共3个依赖。
  2. 在Application 类加上 @EnableEurekaClient 注解和 @EnableZuulProxy 注解。
  3. 在配置文件中添加配置，指定应用信息及注册中心地址。

配置文件：

```yaml
spring:
  application:
    name: learn-sc-service-zuul
server:
  port: 8400
eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:8000/eureka/
zuul:
  routes:
    api-a:
      path: /api-a/**
      serviceId: learn-sc-service-ribbon
    api-b:
      path: /api-b/**
      serviceId: learn-sc-service-feign
```

## 二、测试

  1. 启动 learn-sc-server 注册中心。
  2. 启动 learn-sc-service01 服务提供者。
  3. 启动 learn-sc-service-ribbon 服务消费者。
  4. 启动 learn-sc-service-feign 服务消费者。
  5. 启动 learn-sc-service-zuul 路由模块。
  6. 访问 `http://localhost:8400/api-a/hi?name=Sixlab` ，页面显示：Hello, Sixlab from 8101
  7. 访问 `http://localhost:8400/api-b/hi?name=Sixlab` ，页面显示：Hello, Sixlab from 8101
  8. 关闭 learn-sc-service01。
  9. 访问 `http://localhost:8400/api-a/hi?name=Sixlab` ，页面显示：Hello,Sixlab, ribbon error!
  10. 访问 `http://localhost:8400/api-b/hi?name=Sixlab` ，页面显示：Hello,Sixlab, feign error!

## 三、过滤器

新建 Filter 类，代码如下：

```Java
package cn.sixlab.learn.spring.cloud.learnscservicezuul.filter;

import com.netflix.zuul.ZuulFilter;
import com.netflix.zuul.context.RequestContext;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import javax.servlet.http.HttpServletRequest;

@Component
public class MyFilter extends ZuulFilter {
    private static Logger log = LoggerFactory.getLogger(MyFilter.class);

    @Override
    public String filterType() {
        return "pre";
    }

    @Override
    public int filterOrder() {
        return 0;
    }

    @Override
    public boolean shouldFilter() {
        return true;
    }

    @Override
    public Object run() {
        RequestContext ctx = RequestContext.getCurrentContext();
        HttpServletRequest request = ctx.getRequest();
        log.info(String.format("%s >>> %s", request.getMethod(), request.getRequestURL().toString()));
        Object accessToken = request.getParameter("token");
        if (accessToken == null) {
            log.warn("token is empty");
            ctx.setSendZuulResponse(false);
            ctx.setResponseStatusCode(401);
            try {
                ctx.getResponse().getWriter().write("token is empty");
            } catch (Exception e) {
            }
            return null;
        }
        log.info("ok");
        return null;
    }
}
```

  1. filterType方法返回字符串，代表过滤器类型，有四种：
     1. pre：路由之前
     2. routing：路由之时
     3. post：路由之后
     4. error：错误时调用
  2. filterOrder：返回过滤器的顺序
  3. shouldFilter：是否需要过滤，true 需要过滤
  4. run：过滤的逻辑

## 四、测试

  1. 启动 learn-sc-server 注册中心。
  2. 启动 learn-sc-service01 服务提供者。
  3. 启动 learn-sc-service-ribbon 服务消费者。
  4. 启动 learn-sc-service-feign 服务消费者。
  5. 启动 learn-sc-service-zuul 路由模块。
  6. 访问 `http://localhost:8400/api-a/hi?name=Sixlab` ，页面显示：token is empty
  7. 访问 `http://localhost:8400/api-a/hi?name=Sixlab&token=1` ，页面显示：Hello, Sixlab from 8101

## 五、代码

Github 地址：<https://github.com/nianqinianyi/demo-spring-cloud>

对应分支：<https://github.com/nianqinianyi/demo-spring-cloud/tree/lsc05>

