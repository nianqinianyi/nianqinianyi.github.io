---
title: JavaFX 对话框及弹出框
tags: ["JavaFx", "Java", "GUI"]
categories: ["JavaFx"]
date: 2016-03-06 23:42:26 +08:00
description: 该文详尽展示了JavaFX 8u40中新增的官方对话框和弹出框的使用方法，涵盖了多种类型及其自定义实现，并强调了其无需引入第三方库的便利性。
articleGPT: 文章介绍了JavaFX 8u40及更高版本中新增的官方对话框和弹出框功能，并通过多种示例展示了如何无需引入第三方库，即可实现各种提示、确认、输入及自定义对话框。
---

之前JavaFx的对话框和弹出框都是使用[ControlsFX](http://fxexperience.com/controlsfx/)，前段时间看到了一篇文章
([JavaFX Dialogs (official)](http://code.makery.ch/blog/javafx-dialogs-official/))，介绍了JavaFX
8u40里新添加了对话框和弹出框。试了JavaFx官方的Dialogs和Alerts，简直不能太爽啊，还不用引第三方的库。  
  
注意：需要java的版本要高于8u40 本文基本上算是[JavaFX Dialogs (official)](http://code.makery.ch/blog/javafx-dialogs-official/)文章的翻译了。

## 提示信息

代码：

```Java
Alert alert = new Alert(Alert.AlertType.INFORMATION);  
alert.setTitle(“信息提示对话框”);  
alert.setHeaderText(“头部内容”);  
alert.setContentText(“文本内容”);  
alert.showAndWait();
```

样式：

![信息提示](/images/posts/2016-03-06-javafx-dialog/001.png)

## 简单信息

代码：

```Java
Alert alert = new Alert(Alert.AlertType.INFORMATION);  
alert.setTitle(“信息提示对话框”);  
alert.setHeaderText(null);  
alert.setContentText(“只显示文本内容”);  
alert.showAndWait();
```

样式：

## 警告信息

代码：

```Java
Alert alert = new Alert(Alert.AlertType.WARNING);  
alert.setTitle(“警告对话框”);  
alert.setHeaderText(“头部内容”);  
alert.setContentText(“文本内容”);  
alert.showAndWait();
```

样式：

![警告信息](/images/posts/2016-03-06-javafx-dialog/002.png)

## 错误信息

代码：

```Java
Alert alert = new Alert(Alert.AlertType.ERROR);  
alert.setTitle(“错误提示对话框”);  
alert.setHeaderText(“头部内容”);  
alert.setContentText(“文本内容”);  
alert.showAndWait();
```

样式：

![错误信息](/images/posts/2016-03-06-javafx-dialog/003.png)

## 异常信息

代码：

```Java
Alert alert = new Alert(Alert.AlertType.ERROR);  
alert.setTitle(“异常堆栈对话框”);  
alert.setHeaderText(“头部内容”);  
alert.setContentText(“文本内容”);

Exception ex = new ClassNotFoundException(“找不到类”);

StringWriter sw = new StringWriter();  
PrintWriter pw = new PrintWriter(sw);  
ex.printStackTrace(pw);  
String exceptionText = sw.toString();

Label label = new Label(“异常堆栈信息为:”);

TextArea textArea = new TextArea(exceptionText);  
textArea.setEditable(false);  
textArea.setWrapText(true);

textArea.setMaxWidth(Double.MAX_VALUE);  
textArea.setMaxHeight(Double.MAX_VALUE);  
GridPane.setVgrow(textArea, Priority.ALWAYS);  
GridPane.setHgrow(textArea, Priority.ALWAYS);

GridPane expContent = new GridPane();  
expContent.setMaxWidth(Double.MAX_VALUE);  
expContent.add(label, 0, 0);  
expContent.add(textArea, 0, 1);

alert.getDialogPane().setExpandableContent(expContent);

alert.showAndWait();
```

样式：

![异常信息](/images/posts/2016-03-06-javafx-dialog/004.png)

## 确认对话框

代码：

```Java
Alert alert = new Alert(Alert.AlertType.CONFIRMATION);  
alert.setTitle(“确认信息对话框”);  
alert.setHeaderText(“头部内容”);  
alert.setContentText(“文本内容”);

Optional result = alert.showAndWait();  
if (result.get() == ButtonType.OK) {  
info.setText(“btn6 点击了确定”);  
} else {  
info.setText(“btn6 点击了取消”);  
}
```

样式：

![确认对话框](/images/posts/2016-03-06-javafx-dialog/005.png)

## 自定义按钮

代码：

```Java
Alert alert = new Alert(Alert.AlertType.CONFIRMATION);  
alert.setTitle(“自定义按钮的确认信息对话框”);  
alert.setHeaderText(“头部内容”);  
alert.setContentText(“文本内容”);

ButtonType btnType1 = new ButtonType(“1”);  
ButtonType btnType2 = new ButtonType(“2”);  
ButtonType btnType3 = new ButtonType(“3”);  
ButtonType btnType4 = new ButtonType(“取消”, ButtonBar.ButtonData.CANCEL_CLOSE);

alert.getButtonTypes().setAll(btnType1, btnType2, btnType3, btnType4);

Optional result = alert.showAndWait();  
if (result.get() == btnType1) {  
info.setText(“btn7 点击了 1”);  
} else if (result.get() == btnType2) {  
info.setText(“btn7 点击了 2”);  
} else if (result.get() == btnType3) {  
info.setText(“btn7 点击了 3”);  
} else {  
info.setText(“btn7 点击了取消”);  
}
```

样式：

![自定义按钮](/images/posts/2016-03-06-javafx-dialog/006.png)

## 文本框输入

代码：

```Java
TextInputDialog dialog = new TextInputDialog(“默认值”);  
dialog.setTitle(“文本输入对话框”);  
dialog.setHeaderText(“头部内容”);  
dialog.setContentText(“文本内容”);

// 传统的获取输入值的方法  
Optional result = dialog.showAndWait();  
if (result.isPresent()) {  
info.setText(“btn8 输入了” + result.get());  
}

// lambda表达式获取输入值  
result.ifPresent(value -> info.setText(info.getText() + “\nbtn8(lambda) 输入了” +
value));
```

样式：

![文本框输入](/images/posts/2016-03-06-javafx-dialog/007.png)

## 选择对话框

代码：

```Java
List choices = new ArrayList<>();  
choices.add(“Java”);  
choices.add(“Python”);  
choices.add(“JavaScript”);

ChoiceDialog dialog = new ChoiceDialog<>(“Python”, choices);  
dialog.setTitle(“选择对话框”);  
dialog.setHeaderText(“头部内容”);  
dialog.setContentText(“文本内容”);

// 传统的获取输入值的方法  
Optional result = dialog.showAndWait();  
if (result.isPresent()) {  
info.setText(“btn9 选择了” + result.get());  
}

// lambda表达式获取输入值  
result.ifPresent(value -> info.setText(info.getText() + “\nbtn9(lambda) 选择了” +
value));
```

样式：

![选择对话框](/images/posts/2016-03-06-javafx-dialog/008.png)

## 自定义内容

代码：

```Java
Dialog<Pair<String, String>> dialog = new Dialog<>();  
dialog.setTitle(“自定义对话框”);  
dialog.setHeaderText(“头部内容”);

// 设置头部图片  
dialog.setGraphic(new
ImageView(this.getClass().getResource(“favicon64-w.png”).toString()));

ButtonType loginButtonType = new ButtonType(“登录”,
ButtonBar.ButtonData.OK_DONE);  
dialog.getDialogPane().getButtonTypes().addAll(loginButtonType,
ButtonType.CANCEL);

GridPane grid = new GridPane();  
grid.setHgap(10);  
grid.setVgap(10);  
grid.setPadding(new Insets(20, 150, 10, 10));

TextField name = new TextField();  
name.setPromptText(“用户名”);  
PasswordField password = new PasswordField();  
password.setPromptText(“密码”);

grid.add(new Label(“用户名:”), 0, 0);  
grid.add(name, 1, 0);  
grid.add(new Label(“密码:”), 0, 1);  
grid.add(password, 1, 1);

Node loginButton = dialog.getDialogPane().lookupButton(loginButtonType);  
loginButton.setDisable(true);

// 使用功能 Java 8 lambda 表达式进行校验  
name.textProperty().addListener((observable, oldValue, newValue) -> {  
loginButton.setDisable(newValue.trim().isEmpty() ||
password.getText().trim().isEmpty());  
});

password.textProperty().addListener((observable, oldValue, newValue) -> {  
loginButton.setDisable(newValue.trim().isEmpty() ||
name.getText().trim().isEmpty());  
});

dialog.getDialogPane().setContent(grid);

// 默认光标在用户名上  
Platform.runLater(() -> name.requestFocus());

// 登录按钮后，将结果转为username-password-pair  
dialog.setResultConverter(dialogButton -> {  
if (dialogButton == loginButtonType) {  
return new Pair<>(name.getText(), password.getText());  
}  
return null;  
});

Optional<Pair<String, String>> result = dialog.showAndWait();

result.ifPresent(usernamePassword -> {  
info.setText(“btn10\n” + usernamePassword.getKey() + “ : “ +
usernamePassword.getValue());  
});
```

样式：

![自定义内容](/images/posts/2016-03-06-javafx-dialog/009.png)

# 自定义对话框样式

## 自定义icon图标

代码：

```Java
Stage stage = (Stage) dialog.getDialogPane().getScene().getWindow();

stage.getIcons().add(new
Image(this.getClass().getResource(“favicon64-w.png”).toString()));
```

样式：(有时候可能有问题：详见[自定义icon图标](http://code.makery.ch/blog/javafx-dialogs-official/#custom-icon))

![自定义icon图标](/images/posts/2016-03-06-javafx-dialog/010.png)

# 其他选项

## 设置对话框拥有者

代码：

```Java
dialog.initOwner(parentWindow);
```

## 设置模态

```Java
dialog.initModality(Modality.NONE);
```

# 链接

[Alert API文档](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/control/Alert.html)
[Dialog API文档](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/control/Dialog.html)
[TextInputDialog API文档](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/control/TextInputDialog.html)
[ChoiceDialog API文档](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/control/ChoiceDialog.html)
[DialogPane API文档](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/control/DialogPane.html)
[JavaFX Dialogs (official)](http://code.makery.ch/blog/javafx-dialogs-official/)
