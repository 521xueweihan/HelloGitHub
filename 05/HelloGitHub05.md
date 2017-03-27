# 《HelloGitHub》第05期
>兴趣是最好的老师，[《HelloGitHub》](https://github.com/521xueweihan/HelloGitHub)就是帮你找到兴趣！

![](https://github.com/521xueweihan/HelloGitHub/blob/master/01/img/hello-github.jpg)

## 简介
最开始我只是想把自己在浏览 [GitHub](https://github.com/) 过程中，发现的有意思、高质量、容易上手的项目收集起来，这样便于以后查找和学习。后来一想，如果给这些 GitHub 项目都加上简单的效果图和一些通俗易懂的中文介绍。应该能够帮助到我这样的新手激发兴趣去参与、学习这些优秀、好玩的开源项目。

所以，我就做了一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 的人群的月刊，月刊的内容包括：**各种编程语言的项目**、**各种让生活变得更美好的工具**、**书籍、学习笔记、教程等**。这些项目都是非常容易上手，而且非常 Cool，主要是希望大家能动手用起来，加入到**开源社区**中。会编程的可以贡献代码，不会编程的可以反馈使用这些工具中的 Bug、帮着宣传你觉得优秀的项目、Star 项目⭐️。同时你将学习到更多编程知识、提高自己的编程技巧、发现自己的**兴趣**。

最后[《HelloGitHub》](https://github.com/521xueweihan/HelloGitHub)这个项目就诞生了！😁

---
>**以下为本期内容**｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub)｜每个月 28 号发布最新一期，首发在我的 [GitHub](https://github.com/521xueweihan) 上。

#### Python项目
1、[superset](https://github.com/airbnb/superset)：**企业级项目**，airbnb做的数据探索、展示平台。功能很强大，可以用来做数据分析、展示。如下图：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/05/img/superset-min.gif)

2、[flaskbb](https://github.com/sh4nks/flaskbb)：基于flask框架做的论坛，功能有限，轻量级的论坛应用[在线文档](http://flaskbb.readthedocs.io/en/latest/index.html)，可以在这个项目上进行二次开发，实现更加复杂的功能。[在线预览](https://forums.flaskbb.org)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/05/img/flask-bb-show-min.png)

3、[fuck-login](https://github.com/xchaoinfo/fuck-login)：模拟登录一些知名的网站，为了方便爬取需要登录的网站。**注意**：控制爬虫的爬取频率！

#### Go项目
4、[gogs](https://github.com/gogits/gogs)：国人用GO写的一款极易搭建的自助Git服务，支持所有平台。就像Gitlab一样的服务，但是Gitlab是基于ruby语言的。另外：完善的中文文档、支持 Go 语言支持的 所有平台，包括 Linux、Mac OS X、Windows 以及 ARM 平台。[中文介绍](https://github.com/gogits/gogs/blob/master/README_ZH.md)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/05/img/gogs-show-min.png)

5、[gh-ost](https://github.com/github/gh-ost)：gh-ost 是 GitHub 最近几个月开发出来的，目的是解决一个经常碰到的问题：不断变化的产品需求会不断要求更改 MySQL 表结构。gh-ost 通过一种影响小、可控制、可审计、操作简单而且安全的方式来改变线上表结构。[中文简介](http://www.infoq.com/cn/news/2016/08/GitHub-MySQL-gh-ost?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/05/img/gh-ost-general-flow-min.png)

#### C#项目
6、[WeiXinMPSDK](https://github.com/JeffreySu/WeiXinMPSDK)：微信公众平台SDK Senparc.Weixin for C#，支持.NET Framework及.NET Core。已支持微信公众号、企业号、开放平台、微信支付、JSSDK。此项目开源、免费、持续维护。

#### Javascript项目
7、[share.js](https://github.com/overtrue/share.js)：一键分享到微博、QQ空间、QQ好友、微信、腾讯微博、豆瓣等社交网站的js项目。[在线演示](http://overtrue.me/share.js/)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/05/img/share-js-show-min.png)

#### PHP项目
8、[pinyin](https://github.com/overtrue/pinyin): PHP写的基于[CC-CEDICT](https://cc-cedict.org/wiki/)词典的中文转拼音工具，更准确的支持多音字的汉字转拼音解决方案，示例代码：
```php
use Overtrue\Pinyin\Pinyin;

$pinyin = new Pinyin();

$pinyin->convert('带着希望去旅行，比到达终点更美好');
// ["dai", "zhe", "xi", "wang", "qu", "lv", "xing", "bi", "dao", "da", "zhong", "dian", "geng", "mei", "hao"]

$pinyin->convert('带着希望去旅行，比到达终点更美好', PINYIN_UNICODE);
// ["dài","zhe","xī","wàng","qù","lǚ","xíng","bǐ","dào","dá","zhōng","diǎn","gèng","měi","hǎo"]

$pinyin->convert('带着希望去旅行，比到达终点更美好', PINYIN_ASCII);
//["dai4","zhe","xi1","wang4","qu4","lv3","xing2","bi3","dao4","da2","zhong1","dian3","geng4","mei3","hao3"]
```

#### UI
9、[bytesize-icons](https://github.com/danklammer/bytesize-icons)：极小、极简的SVG图标集合，[在线演示](http://danklammer.com/articles/svg-stroke-ftw/#give-it-a-spin)。

![](https://github.com/521xueweihan/HelloGitHub/blob/master/05/img/bytesize-icons-show-min.png)

#### 其它
10、[gitignore](https://github.com/github/gitignore)：各种`gitignore`模版，特别全，应该能找到你需要的。[什么是gitignore文件](http://gitbook.liuhui998.com/4_1.html)。

11、[Solve-App-Store-Review-Problem](https://github.com/wg689/Solve-App-Store-Review-Problem)：App Store审核未通过的解决方案。

12、[Security Guide for Developers 实用性开发人员安全须知](https://github.com/FallibleInc/security-guide-for-developers)：这是一个checklist，作为一个 real word web developer 你应该在实际工作中不断地谨慎使用这套列表，减少安全隐患。[中文翻译版](https://github.com/FallibleInc/security-guide-for-developers/blob/master/README-zh.md)

---


## 声明
如果你发现了好玩、有意义的开源项目，[点击这里](https://github.com/521xueweihan/HelloGitHub/issues/new) 分享你觉得有意思的项目。

- 分享项目格式：项目名称——项目地址：项目描述(中文)，追求完美👉项目上手 Demo、有图有真相～

或许你分享的项目会让别人由衷的感慨：“原来还有这么有意思的项目！编程可以这么酷！”

**欢迎转载，请注明出处和作者，同时保留声明和联系方式。**

## 联系方式
- [削微寒](https://github.com/521xueweihan)

- [博客园](http://www.cnblogs.com/xueweihan/)

- [知乎专栏](https://zhuanlan.zhihu.com/hellogithub)
