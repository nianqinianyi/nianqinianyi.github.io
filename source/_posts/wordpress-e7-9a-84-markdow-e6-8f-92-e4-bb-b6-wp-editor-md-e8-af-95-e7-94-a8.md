---
title: WordPress 的 Markdow 插件 WP Editor.MD 试用
tags:
  - Markdown
  - WordPress
url: 828.html
id: 828
categories:
  - 工具
date: 2017-10-25 12:48:30
---

1.  经过研究，这个插件将 Markdown 格式放到了`post_content_filtered`字段，将 Markdown 转为 HTML 格式后仍放到原来的`post_content`字段。
2.  编辑器内代码样式和页面上代码样式应该无关，因为使用插件后，页面代码还是按照原来的样式显示的。
3.  旧的文章打开的时候直接按 HTML 格式打开的，因为 Markdown 支持 HTML

测试是否支持 GFM 任务列表（需要在设置中开启）
=========================

*   \[ \] 待测试
*   \[x\] 已测试

测试连接
====

[WP Editor.MD](https://wordpress.org/plugins/wp-editormd/) [官网](https://iiong.com/wordpress-plugins-wp-editormd.html)

测试图片
====

图片： ![六楼实验室](https://oh7gzl219.qnssl.com/logo.png)

测试HTML 代码
=========

111

测试代码片段
======

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