---
title: 重读设计模式 - 单一职责原则
tags: ["设计模式", "单一职责"]
categories: ["设计模式"]
date: 2018-08-15 00:54:01 +08:00
description: 本文阐述了单一职责原则的定义，通过具体案例说明其应用，并探讨了该原则在实际软件设计中的权衡与考量。
articleGPT: 单一职责原则（SRP）要求一个类只负责一个职责，即只有一个引起其变化的原因，旨在实现高内聚、低耦合，从而简化维护并提高代码可读性，尽管实践中可能增加类的数量。
---

# 一、总览

SRP: Single responsibility principle  
There should never be more than one reason for a class to change.  
基本思想：高内聚，低耦合。  
  
引起一个类变化的原因只有有一个。即每个类只能负责一个单独的职责，它应该仅仅关注自身自责的完成。

# 二、举例说明

## 1、例：有一个手机类，描述用手机打电话扣费，用一个类描述这件事。

```java
class Phone {
    public void call(String number, String money) {
        System.out.println("拨打电话：" + number + "，扣掉话费：" + money);
    }
}

public class Client {
    public static void main(String[] args){
        Phone phone = new Phone();
        phone.call("1XXXXXXX", "1元");
        phone.call("2XXXXXXX", "2元");
    }
}
```

## 2、 现在有个新问题，微信也能打电话，这个是走流量的。

在工作中，常用的有两种修改方法。

### 2.1 第一种：修改 call 方法，添加新参数（可选），并判断。

但是如果未来出现新的需求，还是需要修改，而且改动风险也大，弄不好会出现`拨打电话：QQ号码，扣掉话费：5M`这样的问题：

```java
class Phone {
    public void call(String number, String type, String money) {
        if("wechat".equals(type)){
            System.out.println("拨打微信：" + number + "，扣掉流量：" + money);
        }else{
            System.out.println("拨打电话：" + number + "，扣掉话费：" + money);
        }
    }
}
```

### 2.2 第二种：添加新的方法

```java
class Phone {
    public void call(String number, String money) {
        System.out.println("拨打电话：" + number + "，扣掉话费：" + money);
    }

    public void callWechat(String number, String money) {
        System.out.println("拨打微信：" + number + "，扣掉流量：" + money);
    }
}
```

### 2.3 在根据单一职责来说，应该修改如下：

```java
class NormalPhone {
    public void call(String number, String money) {
        System.out.println("拨打电话：" + number + "，扣掉话费：" + money);
    }
}
class WechatPhone {
    public void call(String number, String money) {
        System.out.println("拨打微信：" + number + "，扣掉流量：" + money);
    }
}
```

但是根据单一职责来划分的话，开销太大，所以实际工作中，添加新方法应该更好一点。

# 三、总结

  1. 单一职责原则比较简单，容易理解，但难于实际运用。
  2. 单一职责降低类的复杂度，但是会增加很多类。
  3. 单一职责提高了代码的可读性。
