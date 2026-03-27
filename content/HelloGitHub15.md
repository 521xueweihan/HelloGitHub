# 《HelloGitHub》第 15 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/15) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### CSS 项目
1、[mdui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zdhxiong/mdui)：MDUI 是一套用于开发 Material Design 网页的响应式前端框架。没有任何依赖，支持主题切换，轻量级，低学习成本，[文档](https://www.mdui.org/docs)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/63088743.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
2、[aliyungo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/denverdino/aliyungo)：非官方的 Aliyun Go语言 SDK 支持API：ECS, OSS, DNS, SLB, RDS, RAM, MNS, STS, SLS, MQ, Push, OpenSearch, DM, Container Service


3、[conference](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gopherchina/conference)：Go 语言实际项目应用的技术分享


### Java 项目
4、[FunGameRefresh](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Hitomis/FunGameRefresh)：好玩的下拉刷新控件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/52857175.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[ProgressManager](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JessYanCoding/ProgressManager)：一行代码即可监听 App 中所有网络链接的上传以及下载进度，包括 Glide 的图片加载进度。实现原理类似 EventBus 你可在 App 中的任何地方，将多个监听器以 URL 地址作为标识符，注册到本框架。当此 URL 地址存在下载或者上传的动作时，框架会主动调用所有使用此 URL 地址注册过的监听器，达到多个模块的同步更新


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/93503295.gif' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
6、[font-spider](https://hellogithub.com/periodical/statistics/click?target=https://github.com/aui/font-spider)：字蛛是一个智能 WebFont 压缩工具，它能自动分析出页面使用的 WebFont 并进行按需压缩


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/27417231.png' style="max-width:80%; max-height=80%;"></img></p>

7、[slick](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kenwheeler/slick)：基于 jQuery 的触摸式幻灯片插件。支持动态增加、筛选、轮播、自动播放、延迟加载等功能，[中文官网](https://www.slickjs.cn/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/18049133.png' style="max-width:80%; max-height=80%;"></img></p>

8、[veneno](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zhuyingda/veneno)：一个基于 Node.js 编写的 web 安全漏洞自动化扫描框架


9、[xdomain](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jpillora/xdomain)：纯 JavaScript 实现 CROS 的库，[在线示例](http://jpillora.com/xdomain/)


### Objective-C 项目
10、[FLEX](https://hellogithub.com/periodical/statistics/click?target=https://github.com/FLEXTool/FLEX)：用于 iOS 开发的一组应用内调试工具，功能强大且多，多到不一一列举了



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/20277829.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[spectacle](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eczarny/spectacle)：OS X 系统下的窗口管理工具，通过快捷键方便、快捷的调整窗口大小和位置


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/768345.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
12、[aredis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NoneGG/aredis)：一款基于 Python3 asyncio 的异步 redis 客户端，支持对于单实例，连接池， 哨兵以及集群。[作者](https://github.com/NoneGG)希望可以找到志同道合的小伙伴集思广益，一起维护、优化。示例代码如下：
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


13、[django-blog-tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jukanntenn/django-blog-tutorial)：基于最新版 Django 1.10 和 Python 3.5，通过 26 篇教程一步步带你使用 Django 从零开发一个个人博客系统，在实践的同时掌握 Django 的开发技巧，[完成效果展示](http://demo.zmrenwu.com/)


14、[freezegun](https://hellogithub.com/periodical/statistics/click?target=https://github.com/spulec/freezegun)：时间漫步模块，模拟到某一个时间，使用简单方式多样，实现了装饰器、上下文等调用方式。示例代码如下：
```python
from freezegun import freeze_time
import datetime
import unittest


@freeze_time("2012-01-14")
def test():
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)

```


15、[musicbox](https://hellogithub.com/periodical/statistics/click?target=https://github.com/darknessomi/musicbox)：基于 Python 编写的网易云音乐**命令行**版本，使用起来简单优雅，能够快速安装及使用


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/22628919.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[snake](https://hellogithub.com/periodical/statistics/click?target=https://github.com/chynl/snake)：贪吃蛇游戏 AI 版，通过算法实现让小蛇通过吃豆，最后蛇的身体填满整个地图算结束。该项目详细描述实现思想以及相关算法的讨论


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/61924149.gif' style="max-width:80%; max-height=80%;"></img></p>

### Ruby 项目
17、[mastodon](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mastodon/mastodon)：基于 Ruby 语言的社交网站服务器端所有的源代码，通过这个项目，你可以自己部署一个属于自己的社交网站


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/52281283.jpeg' style="max-width:80%; max-height=80%;"></img></p>

### 其它
18、[English-level-up-tips](https://hellogithub.com/periodical/statistics/click?target=https://github.com/byoungd/English-level-up-tips)：如何提高英语技能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/92807616.png' style="max-width:80%; max-height=80%;"></img></p>

19、[Spacemacs-rocks](https://hellogithub.com/periodical/statistics/click?target=https://github.com/emacs-china/Spacemacs-rocks)：用 21 天学习 Emacs 以及 Spacemacs（Emacs 的配置文件）的使用


20、[SpaceVim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wsdjeg/SpaceVim)：一个社区驱动的模块化 vim/neovim 配置集合，其中包含了多种功能模块，并且针对 neovim 做了功能优化。spacevim 有多种功能模块可供选择，支持多种语言。用户只需要选择需要的模块，就可以配置出一个适合自己的开发环境


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/15/77358263.png' style="max-width:80%; max-height=80%;"></img></p>

21、[vim-galore-zh_cn](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wsdjeg/vim-galore-zh_cn)：Vim 从入门到精通


### 开源书籍
22、[es6tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ruanyf/es6tutorial)：阮一峰老师的开源精品，ECMAScript 6 入门书籍，[在线阅读](http://es6.ruanyifeng.com/)




23、[redis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/huangzworks/redis)：《Redis Command Reference》全文的中文翻译版，[在线阅读](http://redisdoc.com/)





<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub14.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub16.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/15'>这里</a>。
</p>

## 赞助


<table>
  <thead>
    <tr>
      <th align="center" style="width: 80px;">
        <a href="https://www.compshare.cn/?utm_term=logo&utm_campaign=hellogithub&utm_source=otherdsp&utm_medium=display&ytag=logo_hellogithub_otherdsp_display">          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/ucloud.png" width="60px"><br>
          <sub>UCloud</sub><br>
          <sub>超值的GPU云服务</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://www.upyun.com/?from=hellogithub">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/upyun.png" width="60px"><br>
          <sub>CDN</sub><br>
          <sub>开启全网加速</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://github.com/OpenIMSDK/Open-IM-Server">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/im.png" width="60px"><br>
          <sub>OpenIM</sub><br>
          <sub>开源IM力争No.1</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://www.qiniu.com/products/ai-token-api?utm_source=hello">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/qiniu.jpg" width="60px"><br>
          <sub>七牛云</sub><br>
          <sub>百万 Token 免费体验</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
