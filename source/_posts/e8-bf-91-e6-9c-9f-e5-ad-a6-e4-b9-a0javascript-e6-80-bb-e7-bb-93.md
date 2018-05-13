---
title: 近期学习javascript总结
tags:
  - javascript
url: 54.html
id: 54
categories:
  - JavaScript
date: 2011-10-10 20:37:33
---

我一直觉得javascript是一个强大的脚本语言。我一直想学，但是各种不给力。前几天小众软件上说有一个网站[www.codecademy.com](http://www.codecademy.com/)是一个在线互动式的学习javascript的网站，虽说是英文界面，但是我大致也能看懂。我就抽时间看了看，大致学会了点儿。在这里列了出来这些天学到的一点东西备忘。 1、警告框

alert("文本");

2、确认框

confirm("文本");

3、提示框

prompt("文本","默认值");

4、string

"javascript".substring(0.2) //结果为ja
"vbscript".replace("vb","java") //结果为javascript
"JAVAcript".toUpperCase() //结果为JAVASCRIPT
"JAVAcript".toLowerCase() //结果为javascript

5、嵌入html

<html>
<body>
    <script type="text/javascript">
        document.write("Hello World!");
    </script>
</body>
</html>

6、访问外部javascript代码

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

7、随机数字

var r=Math.random(); //返回0到1之间的数字