---
title: Markdown语法学习笔记
tags: ["Markdown", "语法"]
categories: ["工具"]
date: 2013-05-05 23:09:15 +08:00
description: 文章以示例方式详尽介绍了Markdown的常用语法规则及应用。
articleGPT: 本文通过详细示例，全面介绍了Markdown的基础语法和常用排版功能，并提及其与HTML的兼容性。
---

本文内容参考了[Markdown 语法说明 (简体中文版)](http://wowubuntu.com/markdown/#editor) 。  

# 前言

Markdown兼容HTML语法，所以直接输入的HTML语句，会按HTML代码解析

# 标题

## Markdown的标题方法一：

```markdown
    一级标题
    ======
    二级标题
    ------
```

效果：

> # 一级标题
>
> ## 二级标题

## Markdown的标题方法二：

```markdown
    # 一级标题
    ## 二级标题
    ###### 直到六级标题
```

效果：

> # 一级标题
> ## 二级标题
> ###### 直到六级标题

# 区块引用

区块引用，使用`>`符号，而且能嵌套，并且其中还能再使用其他的语法

```
> 会缩进
> 
>> 还能嵌套，比上一级缩进更多
>> # 再来一条，还能使用其他语法
```

效果：

> 会缩进
>> 还能嵌套，比上一级缩进更多
>> # 再来一条，还能使用其他语法

# 列表

## 无序列表，使用*、+、-即可

```markdown
    + 列表1
    + 列表2
    - 列表3
    - 列表4
```

效果：

>  * 列表内容1
>  * 列表内容2
>
>  * 列表3
>  * 列表4

## 有序列表，数字+英文点

```markdown
    1. 有序列表1
    1. 有序列表2
    2. 有序列表3
```

效果：

>  1. 有序列表1
>  2. 有序列表2
>  3. 有序列表3

# 代码区块

代码区块每一行前面都要加四个空格或者一个tab位，预览

```markdown
    ```python
    #this is code
    print("hello, World!")
    ```
```

效果：

>```python
>    #this is code
>    print("hello, World!")
>```

# 分割线

这一行要有三个以上的*、-、_ 而且没有除了空格之外的其他符号

```markdown
    ***
    ---
    ___
```

效果：

>
> ***
> ---
> ___
>


# 链接

## 行内链接

可使用相对路径和绝对路径，title属性，可以使用单、双引号和括号

```markdown
    [六楼实验室](https://blog.sixlab.cn/ 'title属性可省略')
```

效果：

> [六楼实验室](https://sixlab.cn/)

## 参考链接

标记的冒号后边至少有一个空格或制表符，title属性可以另起一行，可以加缩进

```markdown
    [六楼实验室][mark]
    [百度][baidu]
    [Google][]

[mark]: https://blog.sixlab.cn/ (title可省略)
[baidu]: https://www.baidu.com/
[Google]: https://www.google.com/
```

效果：

>    [六楼实验室][mark]
>
>    [百度][baidu]
>
>    [Google][]
>
>[mark]: https://blog.sixlab.cn/ (title可省略)
>[baidu]: https://www.baidu.com/
>[Google]: https://www.google.com/

# 强调

使用*号或者_包围要强调的内容，就是让所包围文字粗体显示

```markdown
    *斜体*
    __粗体__
```

效果：

> _斜体_  
> **粗体**

# 行内代码段

使用反引号`包围,就是ESC键下边的那个键

```markdown
    this is how the `printf()` work。
```

效果：

> this is how the `printf()` work。

# 行内图片

支持绝对链接和相对链接，类似行内链接

```markdown
我的头像![头像](/favicon.png "title可省略")
```

效果：



> 我的头像![头像](/favicon.png)

# 参考图片，类似参考链接

```markdown
我的头像![我的头像][pic]

[pic]: /favicon.png ("title可省略")
```

效果：

> 我的头像![我的头像][pic]
> 
> [pic]: /favicon.png ("title可省略")

# 转义

强大的反斜杠，和编程时候字符串里的转义一个意思啦，就是想输出**[]之类的符号，而不想让它被识别为markdown语法符号的时候，在这些符号前加个

```markdown
    \#\#\#这不是\*标题\*,但*这个*会斜体
    
    \[六楼实验室\]\[https://blog.sixlab.cn/\]
```

效果：

> \#\#\#这不是\*标题\*,但*这个*会斜体
> 
> \[六楼实验室\]\[https://blog.sixlab.cn/\]

# OK

> 基本上主要的内容就是这些了，比较好记，文中内容可能也会有些地方不太准确，望指正。
