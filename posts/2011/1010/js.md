---
title: 近期学习 JavaScript 总结
tags: ["JavaScript"]
categories: ["JavaScript"]
date: 2011-10-10 22:52:54 +08:00
description: 本文记录了通过在线平台学习JavaScript所掌握的基础知识，涵盖常用功能及代码示例。
articleGPT: 本文记录了作者通过Codecademy网站学习JavaScript后所掌握的警告框、字符串操作等基础知识和常用功能，以作个人备忘。
---

我一直觉得 JavaScript 是一个强大的脚本语言。我一直想学，但是各种不给力。前几天小众软件上说有一个网站[www.codecademy.com](https://www.codecademy.com/)是一个在线互动式的学习JavaScript的网站，虽说是英文界面，但是我大致也能看懂。我就抽时间看了看，大致学会了点儿。在这里列了出来这些天学到的一点东西备忘。

1、警告框

```JavaScript
alert("文本");
```

2、确认框

```JavaScript
confirm("文本");
```

3、提示框

```JavaScript
prompt("文本","默认值");
```

4、string

```JavaScript
"JavaScript".substring(0.2) //结果为ja
"vbscript".replace("vb","java") //结果为JavaScript
"JAVAcript".toUpperCase() //结果为JavaScript
"JAVAcript".toLowerCase() //结果为JavaScript
```

5、嵌入html

```html
<html>
<body>
    <script type="text/JavaScript">
        document.write("Hello World!");
    </script>
</body>
</html>
```

6、访问外部 JavaScript 代码

```html
<html>
<head>
</head>
<body>
    <script src="/js/example_externaljs.js">
    </script>
    <p>
        实际的脚本位于名为 "xxx.js" 的外部脚本中。
    </p>
</body>
</html>
```

7、随机数字

```JavaScript
var r=Math.random(); //返回0到1之间的数字
```
