---
title: 使用POI操作word文档中文本框中的内容
tags: ["POI", "Java", "Word"]
categories: ["Java"]
date: 2014-03-22 23:20:47 +08:00
description: 文章记录了如何利用POI结合XMLBeans的XMLCursor，攻克了Word文档中修改文本框内容的挑战。
articleGPT: 本文介绍如何使用Apache POI通过XMLBeans的`XMLCursor`功能，修改Word `.docx`文件中文本框内的文字内容。
---

近几日，公司项目要求使用一个已存在的word文件，从数据库读取数据来修改这个word文件，并保存，此为背景。 模板word是一个office
2007的docx文件，在2003版本的的doc文件中，POI可以使用HWPF很方便的获取range，然后replace，不过好像背景图片什么都没有了。在docx中，正常的文本段落还是比较方便替换的，但是遇到文本框中的文字就无力了。还好POI提供了获取文档的XML内容的方法，因此可以通过XML来修改文本框中的内容，但是此xml非dom4j，而是XMLbeans，一个很少有人用的XML框架，唉，无力吐槽了。
在网上找了很多教程，finally，在伟大的IBM
Developers发现了一篇介绍XMLbeans的文字，找到了一个有用的东西XMLCursor，即游标，哈哈，开始我伟大的代码之旅了：

```Java
FileInputStream fis = new FileInputStream("e:/file.docx");
XWPFDocument doc = new XWPFDocument(fis);
//XWPFParagraph可以通过迭代处理，我这里已经测试过所要用的文档了，所以后边直接使用paragraphList.get(10)
List<XWPFParagraph> paragraphList = doc.getParagraphs();

// 文本框中的內容很麻煩
// 第一步，通过XWPF的XWPFDocument->XWPFParagraph获取XWPFParagraph对象 XWPFParagraph paragraph = paragraphList.get(10);
// 第二部，获取XWPFParagraph的XmlObject，然后使用XmlObject对象，new一个XmlCursor
XmlObject object = paragraph.getCTP().getRArray(1);
XmlCursor cursor = object.newCursor();

// 可以打印XmlObject对象来查看当前xml文件内容
// 也可通过XmlCursor的getName和getTextValue方法查看当前所在Node及其值
// 我的第一个要修改的内容所在node为:注意index
// <xml-fragment> -> <w:pict> -> <v:shape> -> <v:textbox> ->
// <w:txbxContent> -> <w:p> -> <w:r> -> <w:t>
cursor.toChild(1);
cursor.toChild(0);
cursor.toChild(3);
cursor.toChild(0);

cursor.toChild(0);
cursor.toChild(3);
cursor.toChild(1);
cursor.setTextValue("First");

// 我的第二个要修改的内容所在node为：注意index
// <w:txbxContent> -> <w:p> -> <w:r> -> <w:t>
cursor.toParent();
cursor.toParent();
cursor.toParent();
cursor.toChild(1);
cursor.toChild(3);
cursor.toChild(1);
cursor.setTextValue("Second");
FileOutputStream fos = new FileOutputStream("e:/export.docx");
doc.write(fos);
fos.flush();
fos.close();
fis.close();
```

搞定。 附链接：[使用 XMLBeans 进行编程](http://www.ibm.com/developerworks/cn/xml/x-beans1/)
