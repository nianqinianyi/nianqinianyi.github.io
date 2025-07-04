---
title: 重读设计模式 - 里氏替换原则
tags: ["设计模式", "里氏替换"]
categories: ["设计模式"]
date: 2018-08-15 00:55:10 +08:00
description: 文章阐述了里氏替换原则，强调子类必须保持与父类的行为一致性，以确保在任何父类出现的地方都能被无缝替换。
articleGPT: 里氏替换原则（LSP）指出，子类对象可以在不改变程序正确性和原有行为逻辑的前提下，替代父类对象使用。
---

# 一、总览

LSP: Liskov Substitution Principle.  
Functions that use pointers or references to base classes must be able to use
objects of derived classes without knowing it.  
基本思想：在任意父类出现的地方，都可以直接使用子类来代替。  
  
例：Father 类有方法 f1。为了拓展，实现了 Son 类，在 Son 类中添加方法 f2。那么 Son 应该尽量达到：即使覆写 f1 方法，覆写后的
f1 方法应该和 Father 类的 f1 的预期行为是一致的。这样的话，以前所有调用 Father 类 f1 方法的地方，都可以替换为对 Son 类 f1
方法的调用，而不会出现不一样的结果。

# 二、举例说明

## 1、 例：有一个手机类，描述手机有打电话、发短信、看时间功能，用一个类描述这件事。

```java
class Phone {
    public void call(String number) {
        System.out.println("拨打电话：" + number);
    }

    public void sendSms(String number, String text) {
        System.out.println("发送短信给：" + number + "，内容：" + text);
    }

    public void showTime() {
        System.out.println(new Date());
    }
}

public class Client {
    public static void main(String[] args){
        Phone phone = new Phone();
        phone.call("1XXXXXXX");
        phone.sendSms("2XXXXXXX", "Hello sixlab.");
        phone.showTime();
    }
}
```

## 2、 现在有了智能手机，不仅能打电话，发短信、看时间，还能玩游戏。

```java
class SmartPhone extends Phone {
    public void call(String number) {
        System.out.println("拨打电话：" + number);
    }

    public void showTime() {
        System.out.println(LocalDateTime.now());
    }

    public void playGame(String gameName) {
        System.out.println("玩游戏：" + gameName);
    }
}

public class Client {
    public static void main(String[] args){
        Phone phone = new Phone();
        phone.call("1XXXXXXX");      // 此方法的调用 Phone 类可以替换为 SmartPhone 类，因为虽然覆写，但行为是一致的
        phone.sendSms("2XXXXXXX", "Hello sixlab.");  // 此方法的调用 Phone 类也可以替换为 SmartPhone 类，因为没有覆写，行为一致
        phone.showTime();      // 此方法的调用 Phone 类不能替换为 SmartPhone 类，因为覆写后修改了行为，行为不一致

        SmartPhone phone1 = new SmartPhone();
        phone1.call("1XXXXXXX");
        phone1.sendSms("2XXXXXXX", "Hello sixlab.");
        phone1.showTime();
        phone1.playGame("羞羞的游戏");
    }
}
```

在此例中，如果不考虑`showTime`方法，那么是符合里氏替换原则的，但是因为`SmartPhone`类修改了`showTime`方法的行为，导致与`Phone`类的此方法行为不一致，所以不符合里氏替换原则。

# 三、总结

  1. 子类可以实现父类的抽象方法，但不能覆盖父类的非抽象方法。
  2. 子类中可以增加自己特有的方法。
  3. 当子类的方法重载父类的方法时，方法的前置条件（即方法的形参）要比父类方法的输入参数更宽松。
  4. 当子类的方法实现父类的抽象方法时，方法的后置条件（即方法的返回值）要比父类更严格。
