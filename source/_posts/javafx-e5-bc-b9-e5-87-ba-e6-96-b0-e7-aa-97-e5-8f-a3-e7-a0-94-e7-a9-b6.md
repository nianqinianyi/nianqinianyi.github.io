---
title: JavaFx 弹出新窗口研究
tags:
  - JavaFx
url: 191.html
id: 191
categories:
  - JavaFx
date: 2015-04-17 08:31:06
---

自从前段时间接触到JavaFx之后，就喜欢上了JavaFx，因为一直以来需要都在写一些GUI的程序供自己使用，但是Swing之流设计界面太复杂，看着也巨丑，PyQt只有用Eric的时候才比较方便，其他时候不会用，而且自己的Python水平也实在不咋地。JavaFx发展时间较短，而且一直以来Java在GUI上不怎么被人重视，所以JavaFx有很多功能只能靠自己搜索和摸索了。 \[toc\]

### 1、JavaFx弹出模态窗口

这个一直以来都觉得好麻烦，后来研究controlsfx-samples的源代码才发现，原来只要给弹出的窗口的Stage加上stage.initModality(Modality.APPLICATION_MODAL) 就可以实现模态化了。

    public void b2click(ActionEvent event) {
        Stage stage = new Stage();
        Group group = new Group();
        Scene scene = new Scene(group,200,200);
        stage.setScene(scene);
        stage.initModality(Modality.APPLICATION_MODAL);
        stage.show();
    }

### 2、Not on FX application thread;

调用new Stage() 、stage.hide()、stage.show()的时候报错： java.lang.IllegalStateException: Not on FX application thread。这是因为在非JavaFx线程中进行JavaFx操作，所以这些操作放在Platform.runLater()中就可以了：

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

### 3、 未解决问题

1.  A、B两个窗口都是有FXML来进行控件的布局。在A中点击按钮的时候回弹出B，如果让A、B之间互相传送数据、更新控件数据。