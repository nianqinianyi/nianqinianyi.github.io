---
title: SixTools开发手记 - JavaFx控件点滴记录一
tags: ["JavaFx", "项目", "开源项目", "Java", "随笔"]
categories: ["项目"]
date: 2015-04-16 23:34:45 +08:00
description: 文章汇集了在开发SixTools应用过程中遇到的JavaFX GUI编程技巧与解决方案。
articleGPT: 本文记录了作者在凭兴趣开发JavaFX GUI程序SixTools过程中，为避免遗忘而总结的各类开发经验和解决方案。
---

在开发的SixTools，源于我个人平常的诸多需求。从最初使用Swing开发的Movie Recorder，到使用PyQt开发的Movie
Recorder，再到现在使用JavaFx开发的SixTools，GUI程序的开发完全靠自己的兴趣和百度走到现在。而有很多东西平常并不是很常用，即使现在百度到了，可是等过一段时间之后可能就已经忘记了，太浪费时间，在这把开发SixTools过程中碰到的东西都记录下来，以便未来查阅。
[toc]  

### FXML初始化控件数据

让FXML指定的Controller类实现Initializable接口，然后实现接口中的initialize()方法，在此方法中初始化控件的数据。

```java
    package org.eu.sixlab.sixtools.seisplan;
    
    import javafx.fxml.FXML;
    import javafx.fxml.Initializable;
    import javafx.scene.control.*;
    
    import java.net.URL;
    import java.util.ResourceBundle;
    
    public class PlanController implements Initializable {
        @FXML
        public TextField textField ;
        @FXML
        public Label label ;
    
        @Override
        public void initialize(URL location, ResourceBundle resources) {
            label.setText("Hello");
            textField.setText("初始化");
        }
    }
```

### TableView中双击编辑

双击编辑是针对TableView中的列来说的，如果想双击编辑某一列，则需要对相应的TableColumn调用setCellFactory()方法和setOnEditCommit()方法，这两个方法作用分别是设置编辑类型、提交编辑的时间处理。也可调用setOnEditStart()方法和setOnEditCancel()方法在开始编辑和取消编辑的时候做出处理。

```java
    //TextFieldTableCell.forTableColumn()表示使用文本框编辑，也可使用其他的如Combox等等，也可自定义
    tableColumn1.setCellFactory(TextFieldTableCell.forTableColumn());
    tableColumn1.setOnEditCommit(event->{
        String name= ((PropertyValueFactory) event.getTableColumn().getCellValueFactory()).getProperty();
        //todo 编辑提交
    });
```

### TableView中右键菜单

首先对TableView添加事件的过滤器，对鼠标点击事件进行过滤，当时右键点击的时候显示菜单。菜单是一个ContextMenu然后在ContextMenu下添加数个MenuItem。

```java
    tableView.addEventFilter(MouseEvent.MOUSE_CLICKED, e -> {
        if (e.getButton().equals(MouseButton.SECONDARY)) {
            ContextMenu contextMenu = new ContextMenu();
            MenuItem menu1 = new MenuItem("编辑");
            menu1.setOnAction(p -> {
                //todo do sth
            }
            items.add(menu1);
            MenuItem menu2 = new MenuItem("-");
            items.add(menu2);
            MenuItem menu3 = new MenuItem("查看");
            menu3.setOnAction(p -> {
                //todo do sth
            }
            items.add(menu3);
        }
    };);
```

### TextField绑定回车事件

TextField控件在按下回车键时做出处理，使用setOnAction()方法即可。

```java
    TextField textField = new TextField();
    textField.setOnAction(e->{
        System.out.println(textField.getText());
    }
```

### 动态获取TextField值（TextField监听值的改变）

TextField在输入文字过程中动态获取其值这个有点绕，和setOnAction()不太一样，之前我以为是setOnInputMethodTextChanged()这个方法，后来发现这个好像适合输入法相关的，而且每次获取的值都是输入之前的值，使用setOnKeyPressed()、setOnKeyTyped()和setOnKeyReleased()三个方法也不行，每次获取的值都是上一次的值，而且使用鼠标复制粘贴改变TextField的值也完全不像。后来发现controlsfx的演示工具左上角的搜索框就可以动态获取TextField值，于是通过Maven下载了org.controlsfx的1.0.8版本的fxsampler源代码，找到了一句代码，解决了这个问题：

```java
    final TextField searchBox = new TextField();
    searchBox.setPromptText("Search");
    searchBox.getStyleClass().add("search-box");
    searchBox.textProperty().addListener(new InvalidationListener() {
        @Override public void invalidated(Observable o) {
            buildSampleTree(searchBox.getText());
        }
    });
```
