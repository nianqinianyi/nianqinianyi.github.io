---
title: JavaFx非详细入门教程 2 - FXML
tags: ["JavaFx", "Java", "GUI"]
categories: ["JavaFx"]
date: 2015-03-21 23:33:23 +08:00
description: 文章深入探讨了FXML在JavaFX中构建用户界面的方法，涵盖其文件定义、加载、与Java控制器的联动，并介绍了国际化、CSS样式和JavaScript脚本的集成应用。
articleGPT: 本教程详细讲解了如何在JavaFX应用中使用FXML来定义用户界面，包括主Java类加载FXML布局、Java控制器处理事件，以及整合CSS样式、国际化资源和JavaScript脚本的方法。
---

本教程第二部分，讲解一下FXML的使用，本节稍微有点复杂，示例代码也会附上。 代码结构图：  
  
![图片丢失](https://sixlab.cn/wp-content/uploads/2019/10/2015120414354675.png)

代码中：

  * pic.jpg是程序的背景图片，style.css是程序使用css改变原始样式的文件，SixlabFxmlProp.properties是国际化资源文件；
  * SixlabFxml.xml文件即是FXML中定义程序界面的xml文件；
  * SixlabFxmlMain.java文件时程序的主入口，继承自Application，类似上节的代码；
  * SixlabFxmlController.java文件定义了各个控件对应的事件。

#### 1. 入口文件，载入fxml资源

首先讲解入口文件SixlabFxmlMain，此文件时一个继承了Application的类，和上节内容一样，唯一不同是start方法不一样了。

```Java
  package cn.sixlab.fxml;
  
  import javafx.application.Application;
  import javafx.fxml.FXMLLoader;
  import javafx.scene.Parent;
  import javafx.scene.Scene;
  import javafx.stage.Stage;
  import java.util.ResourceBundle;
  
  public class SixlabFxmlMain extends Application {
  
      public static void main(String\[\] args) {
          launch(args);
      }
  
      @Override
      public void start(Stage primaryStage) throws Exception {
          Parent parent = FXMLLoader.load(getClass().getResource("SixlabFxml.xml"), ResourceBundle.getBundle("cn.sixlab.fxml.SixlabFxmlProp"));
  
          Scene scene = new Scene(parent, 500, 637);
          scene.getStylesheets().add("cn/sixlab/fxml/Style.css");
  
          primaryStage.setScene(scene);
          primaryStage.setTitle("Sixlab Fxml Example");
          primaryStage.show();
      }
  }
```

此类和上一节不同的地方就是start方法，该方法主要内容：

  * 定义一个Parent，parent使用FXMLLoader的load方法获取到SixlabFxml.xml文件定义的内容。如果不使用国际化资源文件，可省略第二个参数；
  * 定义Scene（场景），将Parent作为常见的根节点。如果不自定义控件样式，可以省略加载style.css的那行代码；
  * 将Scene作为primaryStage（舞台）的当前场景，并使用show方法显示舞台。

#### 2. xml文件的定义

xml文件定义起来比较麻烦，建议使用JavaFX Scene Builder来制作，该工具功能强大，使用方便，拖拽定义之后就可导出fxml文件。
当然自己手写也可以，由于博客代码插件不太支持fxml定义的xml文件，所以将部分代码整到一行，然后截了个图（可点击在新标签页打开查看大图）：

![图片丢失](https://sixlab.cn/wp-content/uploads/2019/10/2015120414360770.png)

![图片丢失](https://sixlab.cn/wp-content/uploads/2019/10/2015120414370869-1024x465.png)

代码中的内容（每一条内容都会标注在哪一行有这个内容，方便看代码不懂的时候在下面搜索行号）：

  * 4-8行，导入要使用的Java的包；
  * 10行，定义一个BorderPane，fx:controller定义了Controller类所在路径，一些Button之类的控件的触发方法就可以去这个类找，xmlns:fx将命名空间映射到后边的链接；
  * 11行定义了BorderPane的top中的内容。top里是一个StackPane（12行），它的children是一个ImageView（14行）和一个Label（17行）；
  * 21行定义了BorderPane的center中的内容。center里是一个GridPane（22行），它的children是两个Label（24、28行），两个TextField（27、29行），两个Button（30、31行）。GridPane.rowIndex定义了元素在GridPane里是第几行，GridPane.columnIndex定义了元素在第几列（24、27、28、29、30、31行）；
  * 15行，ImageView中，Image的url属性即引用pic.jpg文件，此例中pic.jpg与xml文件在同一个文件夹。@为引用文件的意思；
  * 所有元素的fx:id属性值即Controller类中定义的变量的名字，稍后在Controller代码中可以看到。（17、27、29、30、31行）；
  * 所有元素的text属性的值可以直接是字符串，那么不会从国际化资源文件中读取值，如果字符串前添加%符号，则表示需要从国际化资源文件中获取值。（17、24、28、30、31行）；
  * TextField的prefColumnCount表示默认文本框宽度可写多少个字符。（27、29行）；
  * 30行，Button的onAction属性，表示点击button后的事件处理器，onAction的值是以#开头，所以JavaFx会自动在Controller类中查找onAction值对应的方法；
  * JavaFx除了支持java代码编写事件处理器外，还支持脚本语言，如JavaScript、Jython、Groovy、Clojure等等。第2行，表示添加JavaScript脚本的支持。第31行，Button的onAction属性，表示点击button后触发事件，onAction的值不是以#开头，所以JavaFx会自动查找脚本语言中的方法。第35行，JavaScript代码，内容是用JavaScript编写的一个方法。除了直接在xml中写代码，也可以使用<fx:script source=”sixlab.js” />将js文件写在外部；
  * 第25行，本行表示将当前Label，添加一个css样式表的class属性，值为fx:value的值，String标签需要导入Java的包（8行）。这样在代码中引入的css文件中就可以定义这个class属性的样式。这个样式的改变是全局的，即24行的Label添加了class并改变了样式，其他没有添加class的Label也会改变样式。

#### 3. Controller

Controller中是xml中控件对应的事件处理器。 示例代码：

```Java
    package cn.sixlab.fxml;
    
    import javafx.event.ActionEvent;
    import javafx.fxml.FXML;
    import javafx.scene.control.Button;
    import javafx.scene.control.Label;
    import javafx.scene.control.TextField;
    import javafx.stage.Stage;
    import cn.sixlab.fx.SixlabFxMain;
    
    public class SixlabFxmlController {
        @FXML private Button button1;
        @FXML private TextField usernameField;
        @FXML private Label hello;
    
        @FXML protected void handleUsername(ActionEvent event){
            hello.setText("你好："+usernameField.getText());
            new SixlabFxMain().start(new Stage());
        }
    }
```

代码解析：

  * @FXML注解，表示这个属性或者方法是和xml文件中对应着的，要调用或者初始化时JavaFx会自动进行。
  * 在xml中控件的fx:id属性的值，对应着Controller中有@FXML注解的属性的名字，且类型要对应。
  * xml中，Button的onAction的值为“#handleUsername”，对应着有@FXML注解的“handleUsername”方法。

#### 4. 其他【国际化、css、js脚本】

国际化有两个地方要注意：

  * FXMLLoader类的load方法第二个参数需要将资源文件引入；
  * xml文件中值引用资源文件的地方要添加%。

css有三个地方要注意：

  * Java代码中Scene要引入css文件：`scene.getStylesheets().add("cn/sixlab/fxml/Style.css");`
  * xml文件中要改变的控件添加子标签，并且xml中导入String所在的包；
  * css的属性一般是在正常属性前添加“-fx-”，例如：-fx-background-color。具体的还是百度谷歌一下吧；

js脚本要注意3个地方：

  * 要使用`<?language JavaScript?>`添加js的支持；
  * Button的onAction的值不能以#开头，而且要传递event参数；
  * 脚本可以写在xml的`fx:script`标签中，也可以使用`<fx:script source="sixlab.js" />`导入外部js。

示例代码：[百度网盘](https://pan.baidu.com/s/1ntsqaRf) | [CSDN](http://download.csdn.net/detail/nianqinianyi/8519953)

界面初始化效果图：  

![图片丢失](https://sixlab.cn/wp-content/uploads/2019/10/2015120414462975.png)

处理用户名点击效果图（Controller中处理）：  

![图片丢失](https://sixlab.cn/wp-content/uploads/2019/10/2015120414470387-1.png)

处理密码点击效果图（Js脚本处理）：  

![图片丢失](https://sixlab.cn/wp-content/uploads/2019/10/2015120414473781.png)
