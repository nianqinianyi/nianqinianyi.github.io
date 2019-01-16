---
title: Hexo 主题 hexo-theme-tranquilpeak 部分功能总结
id: 2018/08/30/theme-tranquilpeak
date: 2018-08-30 22:21:24
categories:
  - 工具
tags:
  - Hexo 主题
  - hexo-theme-tranquilpeak
  - tranquilpeak
keywords: 
  - hexo-theme-tranquilpeak
  - Hexo 主题
clearReading: true
thumbnailImagePosition: left
thumbnailImage: /images/2018-08-30-theme-tranquilpeak/preview.png
autoThumbnailImage: true
toc: true
tocNumber: true
comments: true
---

 最近发现了一个 Hexo 主题，又好看功能又强大，[hexo-theme-tranquilpeak](https://github.com/LouisBarranqueiro/hexo-theme-tranquilpeak)，这里总结一下遇到的问题，以及注意事项。

<!-- more -->

# 安装使用问题

1. 要安装说明，使用 Github 仓库中 Release 里边的压缩包来使用，不要直接拉仓库，因为有些文件不存在。

# 使用注意事项

1. 想要在文章后边添加画廊功能，在文章上添加 gallery 字段，可以有多个值。
2. more/excerpt 都是摘要，more 的摘要也在正文显示，excerpt 的不显示。
3. toc: true 显示目录的功能是我自己加的，还在修改中，原使用方式类似摘要，添加一个 toc 即可。
4. 可以使用 Tags，示例在下边。

# Tags 使用示例

```
Syntax :

{% alert [classes] %}
content
{% endalert %}
E.g :

{% alert danger no-icon %}
Here is a danger alert without icon
{% endalert %}

{% alert danger no-icon %}
共有下列几种 class:
{% endalert %}
- info
- success
- warning
- danger
- no-icon
```

# 高亮文本 使用示例

```
Syntax :

{% hl_text [(classes | hexa code | rgb color | rgba color)] %} 
content
{% endhl_text %}
E.g :

{% hl_text danger %}
your highlighted text
{% endhl_text %}

可以使用使用 hexa 颜色, rgb 颜色, rgba 颜色，或者以下 {% hl_text danger %}class{% endhl_text %}:
- red
- green
- blue
- purple
- orange
- yellow
- cyan
- primary
- success
- warning
- danger
```

# 图片 使用示例

```
Syntax : 

{% image [classes] 
group:group-name /path/to/image [/path/to/thumbnail] 
[width of thumbnail]
[height of thumbnail]
[title text]
%}
E.g : 

{% image fancybox right clear 
group:travel /images/2018-08-24-idea-tips/2018-08-26.png
/images/2018-08-30-theme-tranquilpeak/preview.png 150px 300px 
"A image" 
%}

{% image fancybox right clear 
group:travel /images/2018-08-24-idea-tips/2018-08-25.png
/images/2018-08-30-theme-tranquilpeak/preview.png 150px 300px 
"A image" 
%}

{% image fancybox right clear 
group:travel /images/2018-08-24-idea-tips/2018-08-26.png
/images/2018-08-30-theme-tranquilpeak/preview.png 150px 300px 
"A image" 
%}
```

# 代码块
```
 {% tabbed_codeblock [name] [link] %}
      <!-- tab [lang] -->
          source code
      <!-- endtab -->
  {% endtabbed_codeblock %}

{% tabbed_codeblock "代码示例" https://sixlab.cn %}
    <!-- tab js -->
        console.log("https://sixlab.cn");
    <!-- endtab -->
    <!-- tab css -->
          .btn {
              color: red;
          }
      <!-- endtab -->
{% endtabbed_codeblock %}
```

# 大图

```
Syntax : {% wide_image /path/to/image [title text] %}
E.g : {% wide_image /images/2018-08-30-theme-tranquilpeak/preview.png "A image" %}


{% wide_image /images/2018-08-30-theme-tranquilpeak/preview.png "A image" %}
```


