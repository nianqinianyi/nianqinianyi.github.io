---
title: WordPress 的 Markdow 插件 WP Editor.MD 试用
tags: ["Markdown", "Wordpress"]
categories: ["工具"]
date: 2017-10-25 00:35:26
description: 文章阐述了某Markdown插件在WordPress中处理内容存储、实现格式转换，以及编辑器与页面代码样式独立性的具体行为。
articleGPT: 这份文档详细阐述了一个WordPress插件如何处理Markdown格式，包括其存储方式和HTML转换，并通过各种示例展示了对链接、图片、HTML和代码片段等Markdown特性的支持。
---

  1. 经过研究，这个插件将 Markdown 格式放到了`post_content_filtered`字段，将 Markdown 转为 HTML 格式后仍放到原来的`post_content`字段。
  2. 编辑器内代码样式和页面上代码样式应该无关，因为使用插件后，页面代码还是按照原来的样式显示的。
  3. 旧的文章打开的时候直接按 HTML 格式打开的，因为 Markdown 支持 HTML测试是否支持 GFM 任务列表（需要在设置中开启）

  *  待测试
  *  已测试

# 测试连接

[WP Editor.MD](https://wordpress.org/plugins/wp-editormd/)
[官网](https://iiong.com/wordpress-plugins-wp-editormd.html)

# 测试图片

图片：

![六楼实验室](/logo.png)

# 测试HTML 代码

111

# 测试代码片段

```JavaScript
var https = require('https');

https.get("https://sixlab.cn", function (req, res) {
    var html = '';
    req.on('data', function (data) {
        html += data;
    });
    req.on('end', function () {
        console.info(html);
    });
});
```
