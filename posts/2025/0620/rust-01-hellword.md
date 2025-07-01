---
title: Rust 学习笔记 01 - Hello world 和 格式化输出
tags: [Rust, 学习, 笔记]
categories: [Rust]
date: 2025-06-20 12:55:41 +08:00
description: 通过Hello World示例，介绍了Rust程序的入口函数main及println!宏的多种格式化输出方法。
articleGPT: 文章介绍了Rust语言中编写Hello world程序的方法，重点讲解了入口函数main的结构和使用println!宏进行格式化输出的多种方式，包括普通占位符、位置参数、命名参数、格式化参数（如调试字符串、十六进制、二进制）、宽度设置、对齐方式、填充字符以及变量宽度的应用，通过代码示例展示了如何灵活控制输出格式。
broadcast: true
---

学习编程语言第一件事就是写个 Hello world，通过输出 Hello world 能学会两件事：

1. 知道这个编程的入口函数怎么编写。
2. 知道最简单的输出一句话应该怎么写。

# Hello world

## 入口函数

Rust 程序的入口函数也是 `main`，关键字 `fn` 表明这是一个函数,`//` 表示后边是一个段注释。

```rust
fn main() {
    // 代码将写在这里
}
```

## 输出Hello world

如果需要输出 Hello world， Rust 提供了 `println!` 宏来进行格式化输出。`println!` 宏接受一个字符串参数，并将其打印到终端。

```rust
fn main() {
    println!("Hello, world!");
}
```

# 格式化输出

打印操作是由 `std::fmt` 模块提供的，`println!` 宏是 `std::fmt` 模块提供的一个宏。

## 基础输出

`println!` 宏可以使用占位符来格式化输出。占位符用 `{}` 表示：

```rust
fn main() {
    let domain = "sixlab.cn";
    let year = 2015;
    println!("我的域名是：{}，注册于{}年。", domain, year);
}
```

`println!` 宏的占位符还可以使用位置参数，例如 `{0}` 表示第一个参数，`{1}` 表示第二个参数。

> ps: `let` 是定义变量的关键字，后续会提到，这里就先不讲了。

```rust
fn main() {
    let domain = "sixlab.cn";
    let year = 2015;
    println!("我的域名是：{0}，注册于{1}年。欢迎访问：{0}", domain, year);
}
```

`println!` 宏的占位符还可以使用命名参数，例如 `{domain}` 表示 `domain` 变量的值。普通占位符、位置参数、命名参数可以混合使用。

```rust
fn main() {
    let domain = "sixlab.cn";
    let year = 2015;
    println!("我的域名是：{}，注册于{year}年。欢迎访问：{0}", domain, year = year);
}
```

## 进阶输出

`println!` 宏的占位符还可以使用格式化参数。例如：

1. `{:?}` 表示输出参数的调试字符串。
2. `{:x}` 表示输出参数的十六进制表示。
3. `{:b}` 表示输出参数的二进制表示。

```rust
fn main() {
    let number = 2015;
    println!("数字： {:?}", number); // 输出：数字： 2015
    println!("数字： {:x}", number); // 输出：数字： 7df
    println!("数字： {:b}", number); // 输出：数字： 11111011111
}
```

`println!` 宏可以使用宽度参数，例如 `{:10}` 表示输出参数的宽度为 10 个字符，不足 10 个字符的用空格填充。

```rust
fn main() {
    let number0 = 2015;
    let number1 = 15;
    println!("数字： {:10}。", number0); // 输出：数字：       2015。
    println!("数字： {:10}。", number1); // 输出：数字：         15。
}
```

`println!` 宏可以使用对齐参数，例如 `{:<10}` 表示输出参数的宽度为 10 个字符，不足 10 个字符的用空格填充，且左对齐。

```rust
fn main() {
    let number0 = 2015;
    let number1 = 15;
    println!("数字： {:<10}。", number0); // 输出：数字： 2015      。
    println!("数字： {:<10}。", number1); // 输出：数字： 15        。
}
```

`println!` 宏可以使用填充参数，例如 `{:010}` 表示输出参数的宽度为 10 个字符，不足 10 个字符的用 0 填充。

```rust
fn main() {
    let number0 = 2015;
    let number1 = 15;
    println!("数字： {:010}。", number0); // 输出：数字： 0000002015。
    println!("数字： {:010}。", number1); // 输出：数字： 0000000015。
}
```

`println!` 宏的宽度参数也可以是变量。

```rust
fn main() {
    let number0 = 2015;
    let number1 = 15;
    let width = 10;
    println!("数字： {:>width$}。", number0, width = width); // 输出：数字：       2015。
    println!("数字： {:0width$}。", number1, width = width); // 输出：数字： 0000000015。
}
```
