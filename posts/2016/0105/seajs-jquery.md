---
title: jQuery在Seajs下的改造
tags: ["JavaScript", "jQuery", "Seajs"]
categories: ["JavaScript"]
date: 2016-01-05 23:38:41 +08:00
description: 文章记录了在Sea.js环境下，通过修改jQuery源码中的模块定义逻辑，成功解决其与Sea.js兼容性问题的实践过程。
articleGPT: 本文分享了作者在Sea.js中集成jQuery的艰难历程，并最终通过修改压缩版jQuery中对模块定义的判断，使其适应Sea.js的加载机制，从而成功解决了兼容问题。
---

总感觉用上模块化，js代码才显得高大上一点，可是目前还脱离不了jQuery的简洁简单，于是想着一起使用jQuery和Sea.js，但是改造了多次，在Sea.js下仍然征服不了jQuery，很是苦恼。
看网上说的有两种方法可以使jQuery在Sea.js中乖乖听话。

### 方法一的两种方式：

```JavaScript
//方式一：
define(function(){
    //原有jQuery代码
    return jQuery.noConflict();
});

//方式二：这个会有点小问题，原因与文章下方参考内容的《seajs集成jquery的一个坑》相同
define(‘jQuery’, \[\], function(){
    //原有jQuery代码
    return jQuery.noConflict();
});
```

此方法的方式一确实有效，但是我不想对原有jQuery改动太大，而且还听说jQuery本身对模块话就有支持，所以不太想用这种方式。

### 方法二：

找到jQuery中的如下代码

```JavaScript
if ( typeof define === "function" && define.amd && define.amd.jQuery ) {
    define( "jquery", \[\], function () { return jQuery; } );
}
```

修改为：

```JavaScript
if ( typeof define === "function"  ) {
    define( "jquery", \[\], function () { return jQuery; } );
}
```

此方法没有成功，但是这个方法也不是错的，不成功的原因我也搜到了：seajs的路径和ID匹配的原则

### 最终方案：

我使用的使压缩版jquery.min.js，找到的代码使下面这一段：

```JavaScript
    "function"==typeof define&&define.amd&&define("jquery",[],function(){return n});
```

将其修改为：

```JavaScript
    "function"==typeof define&&define.cmd&&define(function(){return n});
```

修改内容：

- 删除了`"jquery",[],` 原因请参考文章下方的《seajs集成jquery的一个坑》
- 将define.amd修改为define.cmd或者删除&&define.amd，甚至删除`"function"==typeof define&&define.amd&&`

参考内容：  
[seajs 2.3.0 添加jquery](http://blog.csdn.net/uikoo9/article/details/37995129)  
[seajs模块化jQuery与jQuery插件](http://julabs.com/blog/seajs-jquery-and-plugins/)  
[seajs集成jquery的一个坑](https://www.cnblogs.com/hongchenok/p/3923876.html)
