---
title: Android学习记录 - 四大组件
tags: ["Android"]
categories: ["Android"]
date: 2015-04-17 23:35:54 +08:00
description: 文章详述了Android应用开发的四大基本组件Activity、Service、BroadcastReceiver和Content Provider的定义、功能、实现方式及相互作用机制。
articleGPT: Android应用程序的核心由Activity（用户界面）、Service（后台运行）、BroadcastReceiver（处理系统事件）和Content Provider（跨应用数据共享）四大组件构成，其中Activity、Service和BroadcastReceiver主要通过Intent进行通信。
---

Android四大基本组件分别是Activity，Service，BroadcastReceiver，Content
Provider。其中Activity相当于程序的每个界面，当界面不可见的时候Activity就会处于暂停或被终止的状态，Service相当于没有界面的后台程序，看不到界面，但是可以进行一些操作，BroadcastReceiver可以在系统发送某些消息的时候调用Service、Activity或者进行其他操作，Content
Provider可以进行数据的存储。Activity，Service，BroadcastReceiver之间是通过叫做Intent的异步消息机制互相调用。  

### 1\. Activity

Activity是Android最重要的组件，所有app打开后看到的界面、弹出框都是Activity。Activity上控件的布局等一般是在xml文件中配置，当然也可以手动在代码中写。实现一个Activity需要进行几步操作：

  1. 创建Java文件，例：SecondActivity，并继承Activity类。
  2. 在layout文件夹中，添加一个xml文件，例：sec.xml。
  3. 在AndroidManifest.xml中添加一个activity标签。配置Activity。
  4. 修改xml布局文件，添加控件。
  5. 在Java类中重写onCreate()方法。

Activity的声明周期主要分为三类：

  1. 整个生命周期，这是一个完整的Android声明周期，从开始运行到结束运行：
     * onCreate -> onStart -> onResume -> 启动 -> onPause -> onStop - > onDestory
  2. 前台可见生命周期，在此阶段，当前Activity在所有其他Activity前端，Activity的组件是可以操作的：
     * onResume -> 启动 -> onPause -> onResume - > …
  3. 前台可见生命周期，在此阶段，当前Activity在所有其他Activity前端，Activity的组件是可以操作的：
     * onStart -> onResume -> 启动 -> onPause -> onStop -> onRestart - > onStart ->…

Activity是讲的最多的，也是最熟悉的，所以就少总结一点。

### 2\. Service

Service是不可见的组件，可以在后台进行操作。实现步骤如下：

  1. 继承Service类。
  2. 在AndroidManifest.xml中配置service标签。

Service不能自己运行，有两种方式启动Service：

  1. 通过Contex.startService()方式启动Service，Service启动后一直运行，直到调用stopService()方法才会停止，且启动Service的组件与其没有关联，无法交互数据，启动Service的组件关闭后，Service会一直运行，
  2. 通过Contex.bindService()来启动Service，则启动Service的组件与Service绑定了，启动Service的组件关闭后，Service也会被关闭。启动Service的组件与Service可以通信来相互传送数据。

Service类中的方法：

  * onBind()方法：抽象方法，必需实现，返回一个Ibinder对象，可通过其与启动Service的组件进行通信。
  * onCreate()方法：当Service没有运行的时候，启动Service会被自动调用。
  * onDestory()方法：Service关闭前会被自动调用。
  * onStartCommand()方法：startService()被调用时，会被自动调用。
  * onUnBind()方法：当Service与所有绑定的组件都断开时，会被自动调用。

### 3\. BroadcastReceiver

BroadcastReceiver没有界面，当外部事件发生时，可以对外部事件的消息进行过滤，并作出相应，启动Activity、启动Service、使用NotificationManager通知用户等等。BroadcastReceiver运行10s后就会被系统结束，所以不能做耗时操作。实现步骤：

  1. 创建Java类，集成BroadcastReceiver类，实现onReceive()方法。
  2. 注册BroadcastReceiver，在AndroidManiFest.xml中注册或者在Java中调用ContextWrapper的registerReceive()。xml中静态注册的如果app未打开，也可以接收广播。但是Java中动态注册的话，当Activity结束，接收器也就结束了。
  3. 启动，sendBroadcast()或sendOrderedBroadcast()分别启动普通广播、有序广播。
  4. 接受BroadcastReceiver。

广播分类：

  1. 普通广播：异步，所有接收者都能接收，其没有顺序，互不影响，互不通信，无法终止广播传播。
  2. 有序广播：所有接收者依次接收，使用setResultExtras()向广播中添加数据，使用getResultExtras()获取被添加的数据，某个接收者可以终止广播的传播。

### 4\. Content Provider

Content Provider可以使一个app可以向其他app提供数据，其他app可以通过 
ContentResolver类获取数据。多个app间共享数据才需要Content Provider。 实现步骤：

  1. 实现Content Provider基类，并在清单xml文件中配置。
  2. 重写增删改查的方法:query、update、insert、delete，并重写onCreate和getType(URI)方法。

URI规则：content://packageName/key/id 几个重要的类：

  * ContentResolver，抽象类，通过Context.getContentResolver()获取。
  * ContentValue，类似HashTable，以键值对存储，键必需是String类型。
  * URIMatcher，通过addURI()添加可以匹配的URI；通过match(URI)类匹配URI。
  * ContentUris，withAppendedId()未URI加上id；parseId(URI)获取URI的id
