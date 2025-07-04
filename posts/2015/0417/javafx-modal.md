---
title: JavaFx 弹出新窗口研究
tags: ["JavaFx", "Java", "GUI"]
categories: ["JavaFx"]
date: 2015-04-17 23:36:54 +08:00
description: 文章分享了JavaFX GUI开发中，关于模态窗口设置和跨线程操作的解决方案，并提及了FXML窗口间数据传递的待解决难题。
articleGPT: 文章分享了作者在使用JavaFx进行GUI编程时，关于模态窗口和线程问题的解决方案，并提出了FXML窗口间数据传递的未解决挑战。
---

自从前段时间接触到JavaFx之后，就喜欢上了JavaFx，因为一直以来需要都在写一些GUI的程序供自己使用，但是Swing之流设计界面太复杂，看着也巨丑，PyQt只有用Eric的时候才比较方便，其他时候不会用，而且自己的Python水平也实在不咋地。JavaFx发展时间较短，而且一直以来Java在GUI上不怎么被人重视，所以JavaFx有很多功能只能靠自己搜索和摸索了。  

### 1、JavaFx弹出模态窗口

这个一直以来都觉得好麻烦，后来研究 [controlsfx-samples](http://fxexperience.com/controlsfx/)
的源代码才发现，原来只要给弹出的窗口的Stage加上`stage.initModality(Modality.APPLICATION_MODAL)`就可以实现模态化了。

```Java
public void b2click(ActionEvent event) {
    Stage stage = new Stage();
    Group group = new Group();
    Scene scene = new Scene(group,200,200);
    stage.setScene(scene);
    stage.initModality(Modality.APPLICATION_MODAL);
    stage.show();
}
```

### 2、Not on FX application thread;

调用 `new Stage()`、`stage.hide()`、`stage.show()` 的时候报错：
`java.lang.IllegalStateException: Not on FX application
thread`。这是因为在非JavaFx线程中进行JavaFx操作，所以这些操作放在 `Platform.runLater()` 中就可以了：

```Java
private void launchStage() {
    Platform.runLater(() -> {
        stage = new Stage();
    });
    Platform.setImplicitExit(false);
    if(stage.isShowing()){
        Platform.runLater(() -> {
            stage.hide();
        });
    }else{
        Platform.runLater(()->{
            stage.show();
        });
    }
}
```

### 3、 未解决问题

  1. A、B两个窗口都是有FXML来进行控件的布局。在A中点击按钮的时候回弹出B，如果让A、B之间互相传送数据、更新控件数据。
