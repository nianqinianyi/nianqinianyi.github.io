---
title: 我又回来啦
tags: [随想]
categories: [随想]
date: 2025-06-19 15:34:40 +08:00
description: 文章系统梳理了从WordPress迁移至Vitepress博客平台的技术路径，包括内容格式转换、AI工具链应用及主题定制优化等关键环节，并规划了Rust语言与AI技术的后续研究方向。
articleGPT: 作者回顾了从2015年使用WordPress建站到2020年断更的博客历程，后因服务器到期导出内容并尝试通过博客园导入但未续更。近期为重建博客，采用Vitepress框架及vitepress-theme-curve主题部署于GitHub Pages，借助AI工具Trae将旧WordPress XML内容转换为Markdown格式，并通过多轮优化解决代码块处理、死链修正及文件结构化问题，最终利用Gemini模型生成文章摘要。未来计划分享Rust语言学习及AI技术相关内容。
---

上一次写博客还是在2020年的5月份，之后就一直断更了。

在此之前，我的博客最开始是在 csdn/开源中国/博客园 等网站更新。在2015年买了域名，部署了 WordPress，开始在 WordPress 上更新博客。后来又用过 hexo。中间想过自己开发博客，但是我又比较懒，一直没有完成开发。然后又切回了 WordPress，最终因为服务器到期，不想续费了，就把 WordPress 的内容导出了。后来由此偶然看到有人说他的把WordPress博客导出的xml文件通过邮件发给博客园，博客园帮忙把内容导入了，我就试了试，没想到真的导入进去了，工作人员还给我回复说只有xml，没有图片，所以导入文章没有图片，真的很让人感动，因为在我眼里博客园一直是个纯粹的技术博客社区，活的很艰难，甚至几度传出要倒闭，还能帮我做到这些微小的工作，不过很惭愧我之后也没有继续更新博客。

前段时间，定期回顾近几个月的工作、学习与生活的时候，感觉还是要把我的一些学习心得做一下输出，调研之后发现了 vitepress 这个工具，发现它构建非常快，之后又发现了一款很好看的主题 [vitepress-theme-curve][vitepress-theme-curve]，觉得非常不错，然后决定用这个主题重建博客，我花了一点时间把主题作了修改，然后部署到了 Github Pages 上。

然后就是之前 WordPress 导出的文章，得益于现在AI技术的发展，我让 Trae 帮忙把之前从 WordPress 博客导出的 xml 文件按照这个主题的文章格式转换了一下，它给我生成了一个 Python 脚本 [wordpress_to_md.py][wordpress_to_md]，我稍作修改之后把 markdown 文件生成了，不过生成之后的文章有很多地方是错误的，比如代码快都没有处理，需要我自己添加，还有文章中有些链接是 locathost 的死链，dev不会报错，但是build会报错，我把这些错误挨个修改了。最后我挨个修改了文件名称，然后又让 Trae 帮我生成了一个脚本，把文件按照 年份/月日/xxx.md 格式生成到 posts 文件夹去。

最后这个主题还有一个功能是基于AI生成摘要显示再页面上，摘要是放在 markdown 文件中 Front Matter 的 articleGPT 字段，然后我就让 Trae 帮我把所有的文章读取一遍，帮我读取文章内容并生成摘要，第一遍的时候还是可以的，虽然它的思考过程中来了一句“身为一个AI，我能总结文章内容？”，但是他还是一次读取十个文件，然后挨个去总结并直接替换内容。
但是因为比较晚了，我就结束了它的任务，结果第二天同样的提示词，它只会帮我生成一个脚本，取文章的第一句话作为总结，看它思考过程，它说总结文章再工具链调用中没法实现，头大。当我提示它使用AI总结的时候，他就生成一个python脚本，调用openai来生成总结内容，并使用 frontmatter 库来替换内容，而不是直接帮我总结内容并修改文件了。
最后没办法，我只能修改了几版提示词，让他使用字符串替换来修改文件，因为 frontmatter 会打乱 frontmatter 的顺序，还会修改 list 形式参数的格式。
最终我用脚本，调用了 gemini 的 gemini-2.5-flash-preview-05-20 来生成了 description 和 articleGPT 字段的内容。

> 现在，一切终于完工了，后续我会继续使用它来写博客，也可能会对博客的主题做一些微调和优化。

接下来我可能会分享的主要内容：

1. Rust：这是我最近想要研究的编程语言，我计划在未来的时间里，深入研究它的语法、标准库以及相关工具链。

2. AI 相关内容：AI 这几年一直是大火，包括这次博客的迁移，我都用了 AI 相关的工具，所以后续我还会持续关注并研究 AI 相关内容。

[vitepress-theme-curve]: https://github.com/imsyy/vitepress-theme-curve
[wordpress_to_md]: https://github.com/nianqinianyi/nianqinianyi.github.io/blob/master/tools/wordpress_to_md.py
