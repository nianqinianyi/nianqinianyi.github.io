---
title: Android学习总结02之布局
tags: ["Android", "Android学习总结", "学习总结"]
categories: ["Android"]
date: 2013-03-31 23:04:04
description: 本文阐述了Android应用界面通过XML文件定义的方式，并详细介绍了线性、相对、绝对、帧以及表格等多种布局的类型与特性。
articleGPT: Android应用的界面在`/res/layout`的XML文件中定义，并通过线性、相对、绝对、帧和表格等多种布局类型来组织UI元素。
---

基本了解了Android的目录结构之后，就能知道APP运行之后显示的界面是在`/res/layout`下的xml文件中定义的，ADT在Eclipse中提供了一个可视化的编辑页面，可以直接拖放控件或者预览xml文件都修改。  

Android的布局有：

  * LinearLayout：线性布局，垂直或者水平并列排放。通过orientation属性设置水平还是垂直方式排列，gravity设置对齐方式，layout_weight设置权重
  * RelativeLayout：相对布局，相对于其他控件的布局方式，不能产生循环依赖 AbsoluteLayout：绝对布局，直接指定控件的X和Y坐标 `Android:layout_x="10px"和 Android:layout_y="10px"`。
  * FrameLayout：层叠的布局，第一个控件在最底层，最后一个空间在最上边。
  * TableLayout：表格布局，类似HTML中和标签，collapseColumns隐藏指定列，shrinkColumns收缩指定列以适应屏幕宽度，stretchColumns指定列填充空白以适应屏幕宽度。是整个的布局，是每一行的布局，每个中放置多个控件
