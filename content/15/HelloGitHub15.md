# 《HelloGitHub》第 15 期
>兴趣是最好的老师，**HelloGitHub** 就是帮你找到兴趣！

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg)

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
> **以下为本期内容**｜每个月 **28** 号发布最新一期｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub#往期回顾)

#### C++ 项目
1、[Snake](https://github.com/stevennl/Snake)：贪吃蛇游戏 AI 版，通过算法实现让小蛇通过吃豆，最后蛇的身体填满整个地图算结束。该项目详细描述实现思想以及相关算法的讨论

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/snake.gif)

#### CSS 项目
2、[MDUI](https://github.com/zdhxiong/mdui)：MDUI 是一套用于开发 Material Design 网页的响应式前端框架。没有任何依赖，支持主题切换，轻量级，低学习成本，[文档](https://www.mdui.org/docs)

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/mdui-show-min.png)

#### Go 项目
3、[aliyungo](https://github.com/denverdino/aliyungo)：非官方的 Aliyun Go语言 SDK 支持API：ECS, OSS, DNS, SLB, RDS, RAM, MNS, STS, SLS, MQ, Push, OpenSearch, DM, Container Service

4、[conference](https://github.com/gopherchina/conference)：Go 语言实际项目应用的技术分享

#### Java 项目
5、[FunGameRefresh](https://github.com/Hitomis/FunGameRefresh)：好玩的下拉刷新控件

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/FunGameRefresh.gif)

6、[ProgressManager](https://github.com/JessYanCoding/ProgressManager)：一行代码即可监听 App 中所有网络链接的上传以及下载进度，包括 Glide 的图片加载进度。实现原理类似 EventBus 你可在 App 中的任何地方，将多个监听器以 URL 地址作为标识符，注册到本框架。当此 URL 地址存在下载或者上传的动作时，框架会主动调用所有使用此 URL 地址注册过的监听器，达到多个模块的同步更新

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/progressManager.gif)

#### JavaScript 项目
7、[veneno](https://github.com/zhuyingda/veneno)：一个基于 Node.js 编写的 web 安全漏洞自动化扫描框架

8、[xdomain](https://github.com/jpillora/xdomain)：纯 JavaScript 实现 CROS 的库，[在线示例](http://jpillora.com/xdomain/)

9、[font-spider](https://github.com/aui/font-spider)：字蛛是一个智能 WebFont 压缩工具，它能自动分析出页面使用的 WebFont 并进行按需压缩

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/font-spider-show-min.png)

10、[slick](https://github.com/kenwheeler/slick)：实现了几乎所有效果的轮播图插件，[在线演示](http://kenwheeler.github.io/slick/)

#### Objective-C 项目
11、[spectacle](https://github.com/eczarny/spectacle)：OS X 系统下的窗口管理工具，通过快捷键方便、快捷的调整窗口大小和位置

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/spectacle-show-min.jpg)

12、[FLEX](https://github.com/Flipboard/FLEX)：用于 iOS 开发的一组应用内调试工具，功能强大且多，多到不一一列举了


![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/flex.gif)

#### Python 项目
13、[musicbox](https://github.com/darknessomi/musicbox)：基于 Python 编写的网易云音乐**命令行**版本，使用起来简单优雅，能够快速安装及使用

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/musicbox.gif)

14、[django-blog-tutorial](https://github.com/zmrenwu/django-blog-tutorial)：基于最新版 Django 1.10 和 Python 3.5，通过 26 篇教程一步步带你使用 Django 从零开发一个个人博客系统，在实践的同时掌握 Django 的开发技巧，[完成效果展示](http://demo.zmrenwu.com/)

15、[aredis](https://github.com/NoneGG/aredis)：一款基于 Python3 asyncio 的异步 redis 客户端，支持对于单实例，连接池， 哨兵以及集群。[作者](https://github.com/NoneGG)希望可以找到志同道合的小伙伴集思广益，一起维护、优化。示例代码如下：
```Python
   >>> import asyncio
   >>> from aredis import StrictRedis
   >>>
   >>> async def example():
   >>>      client = StrictRedis(host='127.0.0.1', port=6379, db=0)
   >>>      await client.flushdb()
   >>>      await client.set('foo', 1)
   >>>      assert await client.exists('foo') is True
   >>>      await client.incr('foo', 100)
   >>>
   >>>      assert int(await client.get('foo')) == 101
   >>>      await client.expire('foo', 1)
   >>>      await asyncio.sleep(0.1)
   >>>      await client.ttl('foo')
   >>>      await asyncio.sleep(1)
   >>>      assert not await client.exists('foo')
   >>>
   >>> loop = asyncio.get_event_loop()
   >>> loop.run_until_complete(example())
```

16、[freezegun](https://github.com/spulec/freezegun)：时间漫步模块，模拟到某一个时间，使用简单方式多样，实现了装饰器、上下文等调用方式。示例代码如下：
```python
from freezegun import freeze_time
import datetime
import unittest


@freeze_time("2012-01-14")
def test():
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)

```

#### Ruby 项目
17、[mastodon](https://github.com/tootsuite/mastodon)：基于 Ruby 语言的社交网站服务器端所有的源代码，通过这个项目，你可以自己部署一个属于自己的社交网站

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/mastodon-show-min.jpeg)

#### 其它
18、[vim-galore-zh_cn](https://github.com/wsdjeg/vim-galore-zh_cn)：Vim 从入门到精通

19、[Spacemacs-rocks](https://github.com/emacs-china/Spacemacs-rocks)：用 21 天学习 Emacs 以及 Spacemacs（Emacs 的配置文件）的使用

20、[SpaceVim](https://github.com/SpaceVim/SpaceVim)：一个社区驱动的模块化 vim/neovim 配置集合，其中包含了多种功能模块，并且针对 neovim 做了功能优化。spacevim 有多种功能模块可供选择，支持多种语言。用户只需要选择需要的模块，就可以配置出一个适合自己的开发环境

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/spacevim-show-min.png)

21、[english-level-up-tips-for-Chinese](https://github.com/byoungd/english-level-up-tips-for-Chinese)：如何提高英语技能

22、[ch](https://github.com/xnum/ch)：类似 virtualenv，可以在 Linux 下建立虛拟的 home 目录並切换，以管理不同工作或项目的文件

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/img/ch.gif)

#### 开源书籍
23、[redis](https://github.com/huangz1990/redis)：《Redis Command Reference》全文的中文翻译版，[在线阅读](http://redisdoc.com/)


24、[es6tutorial](https://github.com/ruanyf/es6tutorial)：阮一峰老师的开源精品，ECMAScript 6 入门书籍，[在线阅读](http://es6.ruanyifeng.com/)





---

## 换种方式阅读
- **网站：** https://hellogithub.com
- **GitBook：** https://gitbook.hellogithub.com

## 声明
如果你发现了好玩、有意义的开源项目 [点击这里](https://github.com/521xueweihan/HelloGitHub/issues/new) 分享你觉得有意思的项目。

**欢迎转载，请注明出处和作者，同时保留声明。**
