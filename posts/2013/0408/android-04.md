---
title: Android学习总结04之Intent
tags: ["Android", "Android学习总结", "学习总结"]
categories: ["Android"]
date: 2013-04-08 23:07:51 +08:00
description: 文章聚焦Android四大组件间的通信枢纽Intent，并通过实例阐释了其在发起系统动作、传递数据以及实现Activity间数据回传中的应用。
articleGPT: Android的四大组件（Activity、Service、Content Provider和BroadcastReceiver）主要通过Intent进行通信，Intent封装了动作、数据和附加属性，从而实现拨打电话、启动组件以及组件间的数据传递与返回等多种功能。
---

Android中主要有四大组件，Activity、Service、Content
Provider（内容提供者）和BroadcastReceiver（广播接收器），这四大组件之间的通讯由Intent解决。
Intent包含了要执行的动作、要操作的数据和一些其他的附加属性。

#### 例1.打电话

首先在AndroidMainfest.xml中声明权限，然后

```java
Intent aintent = new Intent();
aintent.setAction(Intent.ACTION_CALL);
aintent.setData(Uri.parse("tel:10086"));
startActivity(aintent);
```

#### 例2.启动其他Activity

首先使用setClass设置目标Activity

```java
aintent.setClass(dangqianActivity.this,mubiaoActivity.class,);
aintent.putExtra("key","value");//要传送的数据 startActivity(aintent);
```

在目标Activity中接受数据

```java
Intent bintent=getIntent();
Bundle bd=bintent.getExtra();
```

然后使用数据的时候使用类似’类型 变量名 = bd.get类型(“key”)’方式获取数据。

#### 例3.使用Intent返回数据

在此不能使用startActivity()，需要使用startActivityForResult(aintent,requestcode)，其中requestcode是一个大于0的常量，作用是区分是哪个按钮调用的目标Activity。
然后重写OnActivityResult(int requestcode,int resulecode,Intent
Data)方法。通过requestcode判断是哪个按钮调用的目标Activity，而Date就是返回的数据。 同时在目标Activity中

```java
Intent bintent=new Intent();
bintent.putExtra("key","value");
setResult(Result_code,bintent);
```
