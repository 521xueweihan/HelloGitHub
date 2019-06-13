# 《HelloGitHub》第 05 期
>兴趣是最好的老师，**HelloGitHub** 就是帮你找到兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 简介
分享 GitHub 上有趣、入门级的开源项目。

这是一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 人群的月刊，月刊的内容包括：**各种编程语言的项目**、**让生活变得更美好的工具**、**书籍、学习笔记、教程等**，这些开源项目大多都是非常容易上手，而且非常 Cool。主要是希望大家能动手用起来，加入到**开源社区**中。
- 会编程的可以贡献代码
- 不会编程的可以反馈使用这些工具中的 Bug
- 帮着宣传你觉得优秀的项目
- Star 项目⭐️

在浏览、参与这些项目的过程中，你将学习到**更多编程知识**、**提高编程技巧**、**找到编程的乐趣**。

🎉 最后 [HelloGitHub](https://hellogithub.com) 这个项目就诞生了 🎉

---
> **以下为本期内容**｜每个月 **28** 号发布最新一期｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub#内容)

#### C# 项目
1、[WeiXinMPSDK](https://github.com/JeffreySu/WeiXinMPSDK)：微信公众平台 SDK，支持 .NET Framework 及 .NET Core。已支持微信公众号、企业号、开放平台、微信支付、JSSDK。此项目开源、免费、持续维护。

#### Go 项目
2、[gogs](https://github.com/gogits/gogs)：用 Go 写的一款极易搭建的自助 Git 服务，支持所有平台。就像 GitLab 一样的服务，但是 GitLab 是基于 ruby 语言的。另外：完善的中文文档、支持 Go 语言支持的所有平台，包括 Linux、Mac OS X、Windows 以及 ARM 平台。[中文介绍](https://github.com/gogits/gogs/blob/master/README_ZH.md)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/05/img/gogs-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

3、[gh-ost](https://github.com/github/gh-ost)：gh-ost 是 GitHub 最近几个月开发出来的，目的是解决一个经常碰到的问题：不断变化的产品需求会不断要求更改 MySQL 表结构。gh-ost 通过一种影响小、可控制、可审计、操作简单而且安全的方式来改变线上表结构。[中文简介](http://www.infoq.com/cn/news/2016/08/GitHub-MySQL-gh-ost?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/05/img/gh-ost-general-flow-min.png' style="max-width:80%; max-height=80%;"></img></p>

#### JavaScript 项目
4、[share.js](https://github.com/overtrue/share.js)：一键分享到微博、QQ 空间、QQ 好友、微信、腾讯微博、豆瓣等社交网站的 JavaScript 项目。[在线演示](http://overtrue.me/share.js/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/05/img/share-js-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

#### PHP 项目
5、[pinyin](https://github.com/overtrue/pinyin)：PHP 写的基于 [CC-CEDICT](https://cc-cedict.org/wiki/) 词典的中文转拼音工具，更准确的支持多音字的汉字转拼音解决方案，示例代码：
```php
use OvertruePinyinPinyin;

$pinyin = new Pinyin();

$pinyin->convert('带着希望去旅行，比到达终点更美好');
// ["dai", "zhe", "xi", "wang", "qu", "lv", "xing", "bi", "dao", "da", "zhong", "dian", "geng", "mei", "hao"]

$pinyin->convert('带着希望去旅行，比到达终点更美好', PINYIN_UNICODE);
// ["dài","zhe","xī","wàng","qù","lǚ","xíng","bǐ","dào","dá","zhōng","diǎn","gèng","měi","hǎo"]

$pinyin->convert('带着希望去旅行，比到达终点更美好', PINYIN_ASCII);
//["dai4","zhe","xi1","wang4","qu4","lv3","xing2","bi3","dao4","da2","zhong1","dian3","geng4","mei3","hao3"]
```

#### Python 项目
6、[superset](https://github.com/apache/incubator-superset)：**企业级项目**，airbnb 做的数据探索、展示平台。功能很强大，可以用来做数据分析、展示。如下图：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/05/img/superset-min.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[flaskbb](https://github.com/sh4nks/flaskbb)：基于 Flask 框架做的论坛，功能有限，轻量级的论坛应用[在线文档](https://flaskbb.readthedocs.io/en/latest/index.html)，可以在这个项目上进行二次开发，实现更加复杂的功能。[在线预览](https://forums.flaskbb.org)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/05/img/flask-bb-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

8、[fuck-login](https://github.com/xchaoinfo/fuck-login)：模拟登录一些知名的网站，为了方便爬取需要登录的网站。**注意**：控制爬虫的爬取频率！

#### 其它
9、[bytesize-icons](https://github.com/danklammer/bytesize-icons)：极小、极简的 SVG 图标集合，[在线演示](http://danklammer.com/articles/svg-stroke-ftw/#give-it-a-spin)。


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/05/img/bytesize-icons-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

10、[gitignore](https://github.com/github/gitignore)：各种 `gitignore` 模版，特别全，应该能找到你需要的。[什么是 gitignore 文件](http://gitbook.liuhui998.com/4_1.html)。

11、[Solve-App-Store-Review-Problem](https://github.com/wg689/Solve-App-Store-Review-Problem)：App Store 审核未通过的解决方案。

12、[security-guide-for-developers](https://github.com/FallibleInc/security-guide-for-developers)：这是一个 checklist，作为一个 real world web developer 你应该在实际工作中不断地谨慎使用这套列表，减少安全隐患。[中文翻译版](https://github.com/FallibleInc/security-guide-for-developers/blob/master/README-zh.md)



---
<p align="center">
    “看完了，还不够？<a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a> | 还不过瘾，那就看看每天更新的前端日报吧 <a href='https://daily.fairyever.com/'><今日前端></a>”<br>
    如果你发现了好玩、有意义的开源项目 <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击这里</a> 分享你觉得有趣的项目。
</p>

## 公众号
最近开了公众号，后续公众号会针对月刊推荐过的内容精选、梳理，做成系列的文章发布。月刊也会同时发布在公众号，便于第一时间阅读。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:70%;"></img><br>
欢迎关注 HelloGitHub 公众号，获取更多开源项目的资料和内容。
</p>

## 声明
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">知识共享署名-相同方式共享 4.0 国际许可协议</a>进行许可。

**欢迎转载，请注明出处和作者，同时保留声明。**
