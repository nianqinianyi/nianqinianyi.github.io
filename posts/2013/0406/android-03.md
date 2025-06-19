---
title: Android学习总结03之主要控件
tags: ["Android", "Android学习总结", "学习总结"]
categories: ["Android"]
date: 2013-04-06 23:05:15
description: 一篇简洁的指南，详细介绍了Android中TextView、Button和EditText等常用控件的使用、文本格式化、事件监听及样式设置。
articleGPT: 该文章介绍了Android中常用的UI控件，如TextView、Button和EditText，并详细阐述了它们的文本显示与格式化、事件监听以及外观定制等基本用法。
---

Android中的控件非常丰富，Eclipse中打开Android程序的布局文件，以可视化方式编辑布局文件，可看到有很多种的控件，平时主要用到的控件有：TextView、Button、EditText，其他的一些控件如RadioButton、CheckBox、DatePicker、TimePicker、Spinner、AutoCompleteTextView、WebView、TabWidget等等。
各种控件简单记录：

#### TextView：

在布局文件中，添加TextView控件 在代码中：

```java
TextView tv = new TextView(context);
tv.setText("abc");
setContentView(tv);
```

##### 1、HTML与TextView：

使用Html.fromHtml()可自定义TextView里显示的文本格式

```java
tv.setText(Html.fromHtml(...<font>...));
```

##### 2、使用SpannableStringBuilder定义文本格式：

```java
SpannableStringBuilder stylea=new SpannableStringBuilder(astring);
stylea.setSpan(new ForegroundColorSpan(Color.RED),2,22,
                Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
tv.setText(stylea);
```

#### Button:

Button事件需要设置监听事件

##### 方法1：实现OnClickListener接口

```java
class ButtonClick implements OnClickListener{
}

btn1.setOnClickListener(new ButtonClick());
```

##### 方法2：内部匿名类

```java
btn1.setOnClickListener(new OnClickListener(){
});
```

##### 方法3：变量方法，最优

```java
//在OnCreate()方法外部声明变量
private OnClickListener listener = new OnClickListener(){
    public void onClick(View v) {
        Button btn=(Button) v; switch(btn.getId()){
        }
    }
}
//然后将Button点击事件设置为：
btn1.setOnClickListener(listener);
```

#### EditText：

EditText是TextView的子类。 在drawable下建立一个xml文件，例如ashape.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:Android="http://schemas.Android.com/apk/res/Android"
            Android:shape="rectangle">
    <!\-\- 填充的颜色 -->
    <solid Android:color="#FFFFFF" />
    <!\-\- 设置矩形的四个角为弧形 \-\->
    <!\-\- Android:radius 弧形的半径 -->
    <corners Android:radius="22dip" />
</shape>
```

在Layout中设置为：

```
Android:background="@drawable/ashape"
```
