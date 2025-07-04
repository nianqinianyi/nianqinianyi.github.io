---
title: 在notepad++中配置Python和php环境
tags: ["Notepad++", "PHP", "Python", "环境配置", "工具"]
categories: ["工具"]
date: 2011-09-19 22:43:33 +08:00
description: 本文详细介绍了如何在Notepad++中配置Python和PHP的运行命令，旨在为开发者提供更便捷的程序调试环境。
articleGPT: 本文主要介绍了如何在Notepad++中配置F5运行命令，以便方便地调试和运行Python和PHP程序。
---

话说我使用过无数个编辑器，神马gvim、emacs、ultraedit、editplus、SciTE、EmEditor，当然少不了微软的记事本，但是前面这几款编辑器中，没有一款让我用着很爽快的。唯有notepad2和notepad++还能较为让我满意。今天的主角就是notepad++。由于我比较喜欢Python语言的简洁（神马分号大括号，神马变量类型的声明，统统滚开，也经常做一些php的东西，所以我就想在notepad++的运行里加一些东西，让我更方便的调试Python、php程序。  

1. 打开notepad++，貌似废话，不打开没办法添加；  
2. 按F5键，出现运行框，在里边分别输入以下内容后点保存：

```
Python：
cmd /k C:\Python25\python.exe “$(FULL_CURRENT_PATH)” & ECHO. & PAUSE & EXIT

Php：
cmd /k E:\program\Wamp\bin\php\php5.3.5\php.exe “$(FULL_CURRENT_PATH)” & ECHO.
& PAUSE & EXIT
```

稍微解释一下：

  * cmd /k dir：执行完cmd命令不关闭窗口；
  * $(FULL_CURRENT_PATH)”：这个是notepad++里边的宏定义，可以在notepad点帮助文档的Commands标签下找到，是当前文件的完整路径。
  * EXIT：退出cmd.exe程序；
  * PAUSE：暂停批处理程序，并显示出：请按任意键继续…
  * ECHO.：换行，可用ECHO代替。

Python 部分已经更换，详见 [notepad++配置C++及python编译环境](/posts/2012/0513/npp-cpp-python)
