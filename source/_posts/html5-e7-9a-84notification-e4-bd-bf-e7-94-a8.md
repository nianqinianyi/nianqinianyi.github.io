---
title: HTML5的Notification使用
url: 475.html
id: 475
categories:
  - JavaScript
date: 2016-03-21 21:16:21
tags:
---

本文不涉及webkitNotification，仅包括HTML5标准的Notification。

Notification使用步骤
----------------

1.  检查浏览器是否支持HTML5的Notification
2.  检查浏览器的通知权限（是否允许通知）
3.  若权限不够则获取浏览器的通知权限
4.  创建并显示消息通知

检查浏览器是否支持Notification
---------------------

检查Notification或者window.Notification对象，如果存在，说明浏览器支持Notification，目前最新的Chrome/Firefox/Opera都支持Notification，但是IE11和Edge不支持。

if (window.Notification) {
    //浏览器支持 Notification，进行下一步
} else {
    //浏览器不支持 Notification 特性
}

检查浏览器的通知权限
----------

可使用Notification.permission获取浏览器对当前网站的通知的权限，默认情况下权限为"default",和"denied"类似，没有通知的权限，当权限为"granted"时，浏览器才会允许通知。

if (Notification.permission === 'granted') {
    //允许通知，常见通知并展示。
} else {
    //不允许通知，请求用户许可
}

获取浏览器的通知权限
----------

使用Notification.requestPermission()即可让用户选择是否允许通知，调用此方法之后，浏览器会询问用户是否允许显示通知。

Notification.requestPermission()

创建并显示Notification
-----------------

创建并显示一条Notification的代码如下所示：

var options = {body:"This is a Notification!"};
var notification = new Notification('Hello Notification',options);

第一个参数是通知的标题，第二个参数是一个Js对象，参数如下所示：

var options = {
    dir: "auto",//文字方向，水平/垂直
    lang: "",   //语言
    body: "This is a Notification!",  //通知的内容
    tag: "notificationId",                  //通知示例的ID，同一个ID的通知会更新内容，而不是新建一个通知。
    icon: "http://sixlab.cn/favicon.ico"  //通知的图标
};

Notification的事件
---------------

通知默认会一直显示，而且点击是没有任何反应的。但是，一般使用通知的时候，会让通知在一段时间后关闭，点击的时候会打开一个链接并关闭通知。 3s后关闭通知：

var msg = new Notification('Hello Notification',{body:"This is a Notification!"});
msg.onshow = function () {
    setTimeout(function () {
        msg.close();
    }, 3000);
};

点击后打开链接：

var msg = new Notification('Hello Notification',{body:"This is a Notification!"});
msg.onclick = function () {
    window.open("http://www.baidu.com/");
};

全部代码

function showSixNotification(){
    if (window.Notification) {
        if (Notification.permission === 'granted') {
            var options = {
                dir: "auto",
                lang: "",
                body: "This is a Notification!",
                tag: "notificationId",
                icon: "http://sixlab.cn/favicon.ico"
            };
            var msg = new Notification('Hello Notification',options);
            msg.onshow = function () {
                setTimeout(function () {
                    msg.close();
                }, 3000);
            };
            msg.onclick = function () {
                window.open("http://sixlab.cn/");
            };
        } else {
            Notification.requestPermission();
        }
    } else {
        alert('你的浏览器不支持此特性，请下载谷歌浏览器试用该功能');
    }
}