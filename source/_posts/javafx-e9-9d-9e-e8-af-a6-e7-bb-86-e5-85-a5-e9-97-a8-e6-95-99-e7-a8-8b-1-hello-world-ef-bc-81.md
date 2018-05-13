---
title: JavaFx非详细入门教程 1 - Hello World！
tags:
  - JavaFx
url: 122.html
id: 122
categories:
  - JavaFx
date: 2015-03-21 08:23:02
---

本教程不是详细的JavaFx入门教程，不讲解JavaFx的前世今生，不讲解JavaFx优缺点，不讲解JavaFx具体控件的用法，有一定Java基础的人看完本教程可以拿着API手册写JavaFx程序了。废话不多说，上干货。 在JavaFx中：

*   每个窗口是一个舞台（Stage）【这句话应该不完全正确，不过基本可以这样理解】；
*   舞台必需有场景（Scene）；
*   场景中可以有各种控件（Control）、形状（Shape）等等。

JavaFx界面的绘制可以直接在Java代码中写，也可以使用FXML的方式在xml中定义，本节先介绍在Java代码中定义的方式。 代码：

package org.eu.sixlab.fx;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.StrokeType;
import javafx.stage.Stage;

public class SixlabFxMain extends Application {
    
    public static void main(String\[\] args) {
        launch(args);
    }
    
    @Override
    public void start(Stage primaryStage) {
        Group root = new Group();
        Scene scene = new Scene(root, 500, 500);

        Circle circle = new Circle(150,200,100);
        circle.setStrokeType(StrokeType.OUTSIDE);
        circle.setStroke(Color.web("#688668",0.4));
        circle.setStrokeWidth(5);
        
        Label label = new Label("text label");
        label.setTextFill(Color.web("white"));
        label.setLayoutX(200);
        label.setLayoutY(150);

        TextField textField = new TextField();
        textField.setLayoutX(270);
        textField.setLayoutY(150);
    
        Button button = new Button("OK");
        //设置Button的点击事件
        button.setOnAction(e -> {
            label.setText(textField.getText());
            label.setTextFill(Color.BLUE);
            circle.setFill(Color.web("#3300FF", 0.1));
        });
        button.setLayoutX(200);
        button.setLayoutY(200);
    
        root.getChildren().add(circle);
        root.getChildren().addAll(label, textField, button);

        primaryStage.setScene(scene);
        primaryStage.setTitle("Sixlab Fx Example");
        primaryStage.show();
    }
}

JavaFx程序一般直接继承Application类，并在main方法中调用launch方法【据说是最佳实践什么的】，并重写public void start(Stage primaryStage)方法，在start方法中：

*   接受的参数就是Stage（舞台）；
*   定义了一个Group作为Scene（场景）的根；
*   定义Circle、Button、Label、TextField等间接继承自Node的元素；
*   将定义的元素作为Group的子节点，添加到Scene（场景）中；
*   将Scene（场景）作为Stage（舞台）当前的场景，并使用show方法显示舞台。

OK，本教程第一部分就此结束，到这里，怎么写一段简单的JavaFx程序应该是可以了，至于这些控件怎么用，可以百度谷歌或者搜API文档，这里就不讲了。下一节将会讲一下如何使用FXML来定义JavaFx程序的界面，学完之后基本可以不再使用本节的方法来定义界面了，而且可以通过JavaFX Scene Builder使用拖拽的方式来编写FXML文件。 程序初始效果图： \[caption id="attachment_384" align="alignnone" width="287"\][![点击处理用户名时弹出窗口](https://blog.sixlab.cn/wp-content/uploads/2015/03/2015120414470387-287x300.png)](https://blog.sixlab.cn/wp-content/uploads/2015/03/2015120414470387.png) button点击前\[/caption\]   Button点击后程序效果图 \[caption id="attachment_384" align="alignnone" width="287"\][![button按钮点击后](https://blog.sixlab.cn/wp-content/uploads/2015/03/2016030604280023-287x300.png)](https://blog.sixlab.cn/wp-content/uploads/2015/03/2016030604280023.png) button按钮点击后\[/caption\]