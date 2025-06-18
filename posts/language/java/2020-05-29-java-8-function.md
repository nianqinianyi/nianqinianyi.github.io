---
title: Java 8 新特性系列 – 函数式接口
tags: ["Java", "Java8", "lambda", "函数式接口", "新特性"]
categories: ["Java"]
date: 2020-05-29 11:00:00
description: Java 8 新特性系列 – 函数式接口
articleGPT: Java 8 新特性系列 – 函数式接口
---

函数式接口，英文 Functional Interface。

## 1 什么是函数式接口

在 Java8 中，函数式接口指的是有且仅有一个抽象方法的接口。从 Lambda章节
得知，“接口或者抽象类，有且仅有一个方法需要实现，才能使用Lambda”，由此可见函数式接口可用于 Lambda 表达式。

### 1.1 基本语法

```java
@FunctionalInterface
public interface ClassName {
    returnType function(parameters);
}
```

### 1.2 示例

一个典型的示例就是线程的 Runnable 接口：

```java
@FunctionalInterface
public interface Runnable {
    public abstract void run();
}
```

在 Lambda 中的使用：

```java
Thread thread = new Thread(() -> System.out.println("thread run"));
```

可见，函数式接口可以看做是为 Lambda 表达式服务的，上述示例中，不加 @FunctionalInterface 注解，代码也没有问题。

## 2 Java 8 之前内置的函数式接口

 - `java.lang.Runnable`：线程
 - `java.util.concurrent.Callable`：线程并发
 - `java.security.PrivilegedAction`：未知
 - `java.util.Comparator`：比较
 - `java.io.FileFilter`：文件过滤
 - `java.nio.file.PathMatcher`：路径匹配
 - `java.lang.reflect.InvocationHandler`：调用处理
 - `java.beans.PropertyChangeListener`：属性变更监听器
 - `java.awt.event.ActionListener`：事件监听器
 - `javax.swing.event.ChangeListener`：变更监听器

## 3 Java 8 中内置的函数式接口

Java 8 中，新增了“java.util.functin”包，用来支持函数式编程，里边的函数式接口有：

 - `BiConsumer<T,U>`：接收两个泛型参数，无返回值
 - `BiFunction<T,U,R>`：接收两个泛型参数，返回泛型结果
 - `BinaryOperator<T>`：接收两个泛型参数，返回泛型结果，两个参数和返回值类型相同
 - `BiPredicate<T,U>`：接收两个泛型参数，返回 boolean 类型
 - `BooleanSupplier`：无参数，返回 boolean 类型
 - `Consumer<T>`：接收一个泛型参数，无返回值
 - `DoubleBinaryOperator`：接收两个 double 参数，返回 double 结果
 - `DoubleConsumer`：接收两个 double 参数，无返回值
 - `DoubleFunction<R>`：接收一个 double 参数，返回泛型结果
 - `DoublePredicate`：接收一个 double 参数，返回 boolean 类型
 - `DoubleSupplier`：无参数，返回 double 类型
 - `DoubleToIntFunction`：接收一个 double 参数，返回 int 类型
 - `DoubleToLongFunction`：接收一个 double 参数，返回 long 类型
 - `DoubleUnaryOperator`：接收一个 double 参数，返回 double 类型
 - `Function<T,R>`：接收一个泛型参数，返回泛型结果
 - `IntBinaryOperator`：接收两个 int 参数，返回 int 类型
 - `IntConsumer`：接收一个 int 参数，无返回值
 - `IntFunction<R>`：接收一个 int 参数，返回泛型结果
 - `IntPredicate`：接收一个 int 参数，返回 boolean 类型
 - `IntSupplier`：无参数，返回 int 类型
 - `IntToDoubleFunction`：接收一个 int 参数，返回 double 类型
 - `IntToLongFunction`：接收一个 int 参数，返回 long 类型
 - `IntUnaryOperator`：接收一个 int 参数，返回 int 类型
 - `LongBinaryOperator`：接收两个 long 参数，返回 long 类型
 - `LongConsumer`：接收一个 long 参数，无返回值
 - `LongFunction<R>`：接收一个 long 参数，返回泛型结果
 - `LongPredicate`：接收一个 long 参数，返回 boolean 类型
 - `LongSupplier`：无参数，返回 long 类型
 - `LongToDoubleFunction`：接收一个 long 参数，返回 double 类型
 - `LongToIntFunction`：接收一个 long 参数，返回 int 类型
 - `LongUnaryOperator`：接收一个 long 参数，返回 long 类型
 - `ObjDoubleConsumer<T>`：接收一个泛型和一个 double 参数，无返回值
 - `ObjIntConsumer<T>`：接收一个泛型和一个 int 参数，无返回值
 - `ObjLongConsumer<T>`：接收一个泛型和一个 long 参数，无返回值
 - `Predicate<T>`：接收一个泛型参数，返回 boolean 类型
 - `Supplier<T>`：无参数，返回泛型结果
 - `ToDoubleBiFunction<T,U>`：接收两个泛型参数，返回 double 类型
 - `ToDoubleFunction<T>`：接收一个泛型参数，返回 double 类型
 - `ToIntBiFunction<T,U>`：接收两个泛型参数，返回 int 类型
 - `ToIntFunction<T>`：接收一个泛型参数，返回 int 类型
 - `ToLongBiFunction<T,U>`：接收两个泛型参数，返回 long 类型
 - `ToLongFunction<T>`：接收一个泛型参数，返回 long 类型
 - `UnaryOperator<T>`：接收一个泛型参数，返回泛型结果，参数和返回值类型相同

## 4 限制与特殊情况

  1. FunctionalInterface 注解不加不影响代码的使用。
  2. 接口可以用数个默认方法，默认方法不影响函数式接口的使用。
  3. 抽象类是不能使用 FunctionalInterface 注解的。
  4. 如果 A 接口继承 B 接口，不实现原有方法，则 A 新增的方法只能是默认方法，A 才能使用 FunctionalInterface 注解。
  5. 如果 A 接口继承 B 接口，用默认方法实现了 B 未实现的方法，A 需要添加一个未实现的方法，A 才能使用 FunctionalInterface 注解。
