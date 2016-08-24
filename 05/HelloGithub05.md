#《HelloGithub》第五期
>兴趣是最好的老师，** [《HelloGithub》](https://github.com/521xueweihan/HelloGithub) ** 就是帮你找到兴趣！

欢迎各路人士加入本项目，丰富月刊的内容，也可以直接在[Issue](https://github.com/521xueweihan/HelloGithub/issues/new)（需要登录github账号）分享你觉得好的项目。

## 简介
最开始只是我自己浏览github过程中收集的一些有中文介绍，通俗易懂，简单容易上手的项目。后来一想，如果每个github都有个简单的效果图和一些通俗易懂的中文介绍。这样应该更容易让我这样的新手接受。

所以，我就想做一个月刊的形式，面向新手的github月刊，月刊的内容主要包括：中文项目、少许英文项目、翻译的书籍以及教程。项目越容易上手越好，看起来越cool越好！主要是能动手用起来，我觉得这样会有助于编程能力的提高。然后[《HelloGithub月刊》](https://github.com/521xueweihan/HelloGithub)
这个项目就诞生了！😄

---
>**以下为本期内容**｜[点击查看往期内容](https://github.com/521xueweihan/HelloGithub)

#### Python项目
1、[caravel](https://github.com/airbnb/caravel)：**企业级项目**，airbnb做的数据探索、展示平台。功能很强大，可以用来做数据分析、展示。如下图：

![](https://github.com/521xueweihan/HelloGithub/blob/master/05/img/caravel-show-min.png)

2、[flaskbb](https://github.com/sh4nks/flaskbb)：基于flask框架做的论坛，功能有限，轻量级的论坛应用[在线文档](http://flaskbb.readthedocs.io/en/latest/index.html)，可以在这个项目上进行二次开发，实现更加负责的功能。[在线预览](https://forums.flaskbb.org)

![](https://github.com/521xueweihan/HelloGithub/blob/master/05/img/flask-bb-show-min.png)

3、[fuck-login](https://github.com/xchaoinfo/fuck-login)：模拟登录一些知名的网站，为了方便爬取需要登录的网站。**注意**：控制爬虫的爬取频率！

#### Go项目
4、[gogs](https://github.com/gogits/gogs)：国人用GO写的一款极易搭建的自助Git服务，支持所有平台。就像Gitlab一样的服务，但是Gitlab是基于ruby语言的。另外：完善的中文文档、支持 Go 语言支持的 所有平台，包括 Linux、Mac OS X、Windows 以及 ARM 平台。[中文介绍](https://github.com/gogits/gogs/blob/master/README_ZH.md)

![](https://github.com/521xueweihan/HelloGithub/blob/master/05/img/gogs-show-min.png)

5、[gh-ost](https://github.com/github/gh-ost)：gh-ost 是 GitHub 最近几个月开发出来的，目的是解决一个经常碰到的问题：不断变化的产品需求会不断要求更改 MySQL 表结构。gh-ost 通过一种影响小、可控制、可审计、操作简单而且安全的方式来改变线上表结构。[中文简介](http://www.infoq.com/cn/news/2016/08/GitHub-MySQL-gh-ost?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)

![](https://github.com/521xueweihan/HelloGithub/blob/master/05/img/gh-ost-general-flow-min.png)

#### C#项目
6、[WeiXinMPSDK](https://github.com/JeffreySu/WeiXinMPSDK)：微信公众平台SDK Senparc.Weixin for C#，支持.NET Framework及.NET Core。已支持微信公众号、企业号、开放平台、微信支付、JSSDK。此项目开源、免费、持续维护。

#### Javascript项目
7、[share.js](https://github.com/overtrue/share.js)：一键分享到微博、QQ空间、QQ好友、微信、腾讯微博、豆瓣等社交网站的js项目。[在线演示](http://overtrue.me/share.js/)

![](https://github.com/521xueweihan/HelloGithub/blob/master/05/img/share-js-show-min.png)

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

![](https://github.com/521xueweihan/HelloGithub/blob/master/05/img/bytesize-icons-show-min.png)

#### 其它
10、[gitignore](https://github.com/github/gitignore)：各种`gitignore`模版，特别全，应该能找到你需要的。[什么是gitignore文件](http://gitbook.liuhui998.com/4_1.html)。

11、[Solve-App-Store-Review-Problem](https://github.com/wg689/Solve-App-Store-Review-Problem)：App Store审核未通过的解决方案。

12、[Security Guide for Developers 实用性开发人员安全须知](https://github.com/FallibleInc/security-guide-for-developers)：这是一个checklist，作为一个 real word web developer 你应该在实际工作中不断地谨慎使用这套列表，减少安全隐患。[中文翻译版](https://github.com/FallibleInc/security-guide-for-developers/blob/master/README-zh.md)

---
## 声明
不管你是大神，还是菜鸟，只要你发现了好玩的开源项目，都可以直接在[Issue](https://github.com/521xueweihan/HelloGithub/issues/new)（需要登录github账号），分享你觉得有意思的项目。同时有可能会被收录到下一期的月刊中，让更多人知道。

- 分享项目格式：项目名称——项目地址：项目描述(中文)，追求完美👉项目上手demo、有图有真相～

或许你分享的项目会让别人由衷的感慨：“原来还有这么有意思的项目！编程可以这么酷！”

欢迎转载，请注明出处和作者，同时保留声明和联系方式。

## 联系方式
- Github：[削微寒](https://github.com/521xueweihan)

- 博客园：[削微寒](http://www.cnblogs.com/xueweihan/)

- 邮箱：595666367@qq.com
