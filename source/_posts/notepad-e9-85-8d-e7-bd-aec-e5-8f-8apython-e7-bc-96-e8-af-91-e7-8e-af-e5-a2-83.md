---
title: notepad++配置C++及python编译环境
tags:
  - c++
  - notepad++
  - python
  - 环境配置
url: 56.html
id: 56
categories:
  - 工具
date: 2012-05-13 20:38:19
---

原先写过一篇《在notepad++中配置Python和php环境》，详见 [https://blog.sixlab.cn/2011/09/48](https://blog.sixlab.cn/2011/09/48) notepad++这个编辑器相当不错，相当轻量级，一直以来是我的最爱。每次重装系统都要重新配置notepad++，烦不胜烦，最可恶的是每次配置的时候都要上网搜上一阵，浪费时间，效果也不是很好。在这里总结一些，便于以后使用。 首先是安装插件部分，菜单上的 插件-Plugin Manager-Show Plugin Manager。在Plugin Manager里找到NppExec这个插件，安装。 接着，配置C++环境，我使用的是visual studio 2008环境，估计很多人使用的也是这个环境。我参照了《[为Notepad++配备Visual C++ 2010编译器](http://www.cnblogs.com/Realh/archive/2011/12/12/2284741.html)》这篇文章。 1、添加环境变量：

lib：
C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\lib;C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\Lib;
include：
C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\Include;C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\include;
path：
C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\bin;

2、调整编译器需要的文件： 将C:\\Program Files\\Microsoft Visual Studio 9.0\\Common7\\IDE目录下的mspdb80.dll和mspdbsrv.exe文件拷贝到C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\bin目录下。 3、notepad++添加命令： notepad++菜单  插件 – NppExec – execute… 分别输入下面命令并保存

调试：
cmd /k chdir /d "$(CURRENT\_DIRECTORY)" & cl "$(FILE\_NAME)" & echo Running: & "$(NAME_PART).exe" & PAUSE & EXIT
编译：
cmd /k chdir /d "$(CURRENT\_DIRECTORY)" & cl "$(FILE\_NAME)" & PAUSE & EXIT
运行：
cmd /k chdir /d "$(CURRENT\_DIRECTORY)" & echo Running: & "$(NAME\_PART).exe" & PAUSE & EXIT

可将调试、编译、运行命令显示在notepad++ 菜单  宏  下边，方式是点击 notepad++菜单  插件 – NppExec – Advanced Options。选中“Place to the Macros submenu”，同时在NppExec  Advanced Options左下方，选中命令并修改要显示的名字，然后点击“Add/Modify”。每次只能添加一条，添加完成后点“OK”，重启之后再添加下一条。 然后是配置Python的环境变量，这个就简单多了。 1、添加path：

C:\\Python27

2、添加notepad++命令： Python：

cmd /k cd "$(CURRENT\_DIRECTORY)" &  python "$(FULL\_CURRENT_PATH)" & ECHO. & PAUSE & EXIT

网上大多使用cmd /k python “$(FULL\_CURRENT\_PATH)” & ECHO. & PAUSE & EXIT这个命令，但是看了一篇文章《[Notepad++搭建Python开发环境的一个小改进](http://www.cnblogs.com/tt-0411/archive/2011/10/30/2229544.html)》，决定还是改一下。 最后推荐几个notepad++的小插件，挺不错。 TextFX Characters：默认安装，功能很强大，很多人认为这个最好的插件，格式化C++、XML、HTML等代码，替换字符，删除空行或者空格等，功能太多，不一一列举，不过没有中文版，命令又多，可参考一下《[notepad++5.9.6 官方中文语言汉化增补，插件汉化](http://hi.baidu.com/homeylife/blog/item/e59176868e13062767096e13.html)》或者《[Notepad++ 插件之 TextFX (安装及作用)](http://zhibin07.iteye.com/blog/1287234)》 Subversion：使用SVN的能用到。 Explorer或者Light Explorer：在notepad++左侧可生成一个文件列表，浏览文件，我觉得Explorer很好用，但很多人认为Light Explorer是仅次于TextFX Characters的插件。