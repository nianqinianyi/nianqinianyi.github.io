---
title: Python实现迅雷看看xv格式转换为flv格式
tags: ["Python", "xv", "flv"]
categories: ["Python"]
date: 2012-11-19 22:58:15 +08:00
description: 文章介绍了将XV格式视频文件转换为FLV格式的方法，通过删除起始数据、解密特定加密块并拼接剩余内容实现，并提供了Python脚本实现这一自动化转换过程。
articleGPT: 该文章提供了一个Python脚本，用于将XV视频文件转换为FLV格式，其原理是删除文件开头部分，通过计算密钥解密特定偏移量处的加密数据块，并拼接后续内容。
---

用editplus的十六进制查看器查看xv格式的数据，可以发现把xv格式的0到0×200000之间的数据删除，把0×200000到0×200400之间的数据解密，再加上后边的所有的数据，就是flv格式的视频了。  
  
由于flv格式数据最开始的3个二位十六进制数据为：46 4C
56，对应的ASCII码分别为FLV，设第一个二位十六进制数据0×46为newmagicnum。xv格式从0×200000开始的数据不一定，但都是按照一定的密钥加密的，就是flv从0到0×400的所有数据分别加上密钥的值，设第一个二位十六进制数据为oldmagicnum。则密钥magicnum就是newmagicnum减去oldmagicnum。  
例子： flv格式数据为：46 4C 56 xv格式数据为：62 68 72 由于0×46比0×62小，所以密钥为：0×46+0×100-0×62
解密的过程为：删除xv文件0到0×200000之间的数据。0×200000到0×200400之间的数据分别加上magicnum，如果结果数据大于0xFF，则减去0×100。后边添加上所有未加密数据。

代码如下，使用方法为：建立一个python文件，放在要转码的xv格式所在文件夹，程序会遍历文件夹内的xv格式的数据，然后新建一个“转码后文件”的文件夹，转码后的文件都在“转码后文件”文件夹内：

```python
    \# -*- coding: utf-8 -*-
    import os
    currepath=unicode(os.getcwd(),"utf-8")
    oldfileslist=os.listdir(currepath)
    if os.path.exists(u'转码后文件')==False:
        os.mkdir(u'转码后文件')
    
    for oldfilename in oldfileslist:
        filename=os.path.splitext(oldfilename)
        if filename\[1\]!='.xv':
            continue
        oldfile = open(oldfilename,'rb')
        newfilename = u'转码后文件/'+filename\[0\]+'.flv'
        newfile = open(newfilename,'wb')
    
        temp=oldfile.read()
        tempfile=temp\[0x00200000:\]
        tempfile1=tempfile\[:0x400\]
    
        oldmagic=ord(tempfile1\[0\])
        newmagic=0x46
    
        if newmagic<oldmagic:
            newmagic += 0x100
        magicnum=newmagic-oldmagic
    
        for i in range(0,0x400):
            tempnum=ord(tempfile1\[i\])+magicnum
            if tempnum>0xFF:
                tempnum -= 256
            tempfile1=tempfile1\[:i\]+chr(tempnum)+tempfile1\[i+1:\]
    
        tempfile=tempfile1+tempfile\[0x400:\]
        newfile.write(tempfile)
    
        newfile.close()
        oldfile.close()
        filefinish=u'%s 已经完成'% filename\[0\]
        print filefinish
```
