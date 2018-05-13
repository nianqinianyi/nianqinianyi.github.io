---
title: Android学习总结02之布局
tags:
  - android
  - Android学习总结
url: 65.html
id: 65
categories:
  - Android
date: 2013-03-31 11:21:52
---

基本了解了Android的目录结构之后，就能知道APP运行之后显示的界面是在/res/layout下的xml文件中定义的，ADT在Eclipse中提供了一个可视化的编辑页面，可以直接拖放控件或者预览xml文件都修改。 Android的布局有： LinearLayout：线性布局，垂直或者水平并列排放。通过orientation属性设置水平还是垂直方式排列，gravity设置对齐方式，layout\_weight设置权重 RelativeLayout：相对布局，相对于其他控件的布局方式，不能产生循环依赖 AbsoluteLayout：绝对布局，直接指定控件的X和Y坐标 android:layout\_x=”10px”和 android:layout_y=”10px”。不推荐 FrameLayout：层叠的布局，第一个控件在最底层，最后一个空间在最上边。不推荐 TableLayout：表格布局，类似HTML中<tr>和<td>标签，collapseColumns隐藏指定列，shrinkColumns收缩指定列以适应屏幕宽度，stretchColumns指定列填充空白以适应屏幕宽度。<TableLayout >是整个的布局，<TableRow>是每一行的布局，每个<TableRow>中放置多个控件