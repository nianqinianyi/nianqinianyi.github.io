---
title: Android学习总结01之Hello World
tags: ["Android", "Android学习总结", "学习总结"]
categories: ["Android"]
date: 2013-03-27 23:03:06 +08:00
description: 文章介绍了Android项目的基本目录结构及Hello World程序的运行原理，包括AndroidManifest.xml的配置、Activity的启动过程以及资源文件的管理。
articleGPT: 本文概述了Android项目的基本目录结构，并深入解析了“Hello World”应用从配置到代码再到资源文件如何协作显示内容的完整运行机制。
---

先Hello World，后学编程。  
新建Android项目后，会生成最初始的Android代码。  

#### 一、Android代码目录

  1. assets：资源目录，目录内的文件不会再R.java中生成ID
  2. bin：生成的二进制文件等，一般不会使用，apk文件在此目录
  3. gen：系统自动生成，不需修改，包含R.java文件，里边是一个类名为R的类，会对res文件夹下的每一个文件都自动生成一个ID
  4. libs：外部库
  5. res：资源目录，每一个文件都会在R.java中生成ID，方便代码中调用，如果代码中未使用目录下的某些资源，这些资源不会在最终生成apk时候打包
  6. drawable：一般会有四个文件夹：drawable-hdpi，drawable-ldpi，drawable-mdpi，是放图片的文件夹，分别是高DPI、低DPI、中等DPI屏幕下的图片显示
  7. layout：布局文件，包括但不限于Activity、Widgets、自定义通知栏、自定义视图
  8. menu：菜单的布局文件
  9. values：包含一个strings.xml文件，可自定义添加字符串的键值对，布局文件、源代码可从中读取字符串，便于制作国际化程序的制作。
  10. src：自己编写的代码
  11. AndroidManifest.xml：apk程序的配置文件，包括注册Activity、权限、Broadcast等内容。

#### 二、Hello World运行原理

##### 1、显示哪个Activity

初始AndroidManifest.xml的部分代码：

```xml
    <application>
      <activity>
        <intent-filter>
          <action Android:name="Android.intent.action.MAIN" />
          <category Android:name="Android.intent.category.LAUNCHER" />
        </intent-filter>
      </activity>
    </application>
  ```

其中`<application>`表示整个程序，`<activity>`表示某个Activity，而
`<intent-filter>`中的`<action Android:name="Android.intent.action.MAIN"/>` 
表示当前Activity是程序启动时的默认Activity，即apk程序启动时，默认显示当前这个Activity。

##### 2、Activity显示哪些内容

从`Android:name="com.sixlab.activitytest.MainActivity"`可知道此Activity的java文件是MainActivity.java文件，MainActivity.java部分代码：

```Java
    public class MainActivity extends Activity {
      protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
      }
    }
```

在代码中`onCreate()`即为Activity初始是调用的方法`setContentView(R.layout.activity_main)`，即设置Activity的视图为`R.layout.activity_main`的文件，R.java中部分文件内容：

```Java
    public final class R {
      public static final class layout {
        public static final int activity_main=0x7f030000;
      }
    }
```

代码中指出布局文件即Layout目录下的`activity_main`文件。`activity_main.xml`文件部分内容：

    
    
```xml
    <RelativeLayout>
      <TextView Android:text="@string/hello_world" />
    </RelativeLayout>
```

此布局内容为：相对布局，布局里有一个TextView，这个View里显示一段text，内容为`string.xml`中`hello_world`签对应的字符串Hello
world!，所以apk后如下图所示。  

![图片已丢失](https://sixlab.cn/wp-content/uploads/2019/10/201303.png)
