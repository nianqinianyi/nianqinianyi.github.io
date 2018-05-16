---
title: Android学习总结01之Hello World
tags:
  - android
  - Android学习总结
url: 63.html
id: 63
categories:
  - Android
date: 2013-03-27 11:20:56
---

先Hello World，后学会编程。   新建Android项目后，会生成最初始的Android代码。

#### 一、Android代码目录

assets：资源目录，目录内的文件不会再R.java中生成ID bin：生成的二进制文件等，一般不会使用，apk文件在此目录 gen：系统自动生成，不需修改，包含R.java文件，里边是一个类名为R的类，会对res文件夹下的每一个文件都自动生成一个ID libs：外部库 res：资源目录，每一个文件都会在R.java中生成ID，方便代码中调用，如果代码中未使用目录下的某些资源，这些资源不会在最终生成apk时候打包

> drawable：一般会有四个文件夹：drawable-hdpi，drawable-ldpi，drawable-mdpi，是放图片的文件夹，分别是高DPI、低DPI、中等DPI屏幕下的图片显示 layout：布局文件，包括但不限于Activity、Widgets、自定义通知栏、自定义视图 menu：菜单的布局文件 values：包含一个strings.xml文件，可自定义添加字符串的键值对，布局文件、源代码可从中读取字符串，便于制作国际化程序的制作。

src：自己编写的代码 AndroidManifest.xml：apk程序的配置文件，包括注册Activity、权限、Broadcast等内容。

#### 二、Hello World运行原理

##### 1、显示哪个Activity

初始AndroidManifest.xml的部分代码：

<application> <activity> <intent-filter> <action android:name="android.intent.action.MAIN" /> <category android:name="android.intent.category.LAUNCHER" /> </intent-filter> </activity> </application>

其中<application>表示整个程序，<activity>表示某个Activity，而<intent-filter>中的<action android:name=”android.intent.action.MAIN” />表示当前Activity是程序启动时的默认Activity，即apk程序启动时，默认显示当前这个Activity。

##### 2、Activity显示哪些内容

从android:name=”com.sixlab.activitytest.MainActivity”可知道此Activity的java文件是MainActivity.java文件，MainActivity.java部分代码：

public class MainActivity extends Activity { protected void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}

在代码中onCreate()即为Activity初始是调用的方法setContentView(R.layout.activity\_main)，即设置Activity的视图为R.layout.activity\_main的文件，R.java中部分文件内容：

public final class R { public static final class layout { public static final int activity_main=0x7f030000;
    }
}

代码中指出布局文件即Layout目录下的activity\_main文件。activity\_main.xml文件部分内容：

<RelativeLayout> <TextView android:text="@string/hello_world" /> </RelativeLayout>

此布局内容为：相对布局，布局里有一个TextView，这个View里显示一段text，内容为string.xml中hello_world签对应的字符串Hello world!，所以apk后如下图所示。 [![20130327134300310](http://images.cnitblog.com/blog/469028/201303/27134326-d5a110dcebbc406d955f707489c661bb.png "20130327134300310")](http://images.cnitblog.com/blog/469028/201303/27134324-29eb341c6ad0411dbf7c1712bc1e3685.png)