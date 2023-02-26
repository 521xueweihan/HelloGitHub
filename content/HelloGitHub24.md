# 《HelloGitHub》第 24 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/24) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[reading-code-of-nginx-1.9.2](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/y123456yz/reading-code-of-nginx-1.9.2)：nginx-1.9.2 源码通读分析注释，带详尽函数中文分析注释以及相关函数流程调用注释


### Go 项目
2、[knowledge](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gocn/knowledge)：Go 知识图谱


3、[lux](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/iawia002/lux)：Go 编写的快速、简单、干净的视频下载程序。支持哔哩哔哩、YouTube 视频网站
```
$ annie -c cookies.txt https://www.bilibili.com/video/av20203945/

 Site:      哔哩哔哩 bilibili.com
 Title:     【2018拜年祭单品】相遇day by day
 Type:      video
 Stream:
     [default]  -------------------
     Quality:         高清 1080P60
     Size:            220.65 MiB (231363071 Bytes)
     # download with: annie -f default "URL"

 16.03 MiB / 220.65 MiB [==>----------------------------]   7.26% 9.65 MiB/s 19s
```


### Java 项目
4、[PreLoader](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/luckybilly/PreLoader)：Android 页面在打开后需要在 UI 初始化完成后才能发起网络请求，以免网络请求返回后展示到 UI 时出现错误。但这种串行的做法导致页面的整个初始化时间变长。使用该工具可以在打开页面之前预加载数据，然后在页面 UI 初始化完成后提取预加载好的数据进行展示，从而缩短页面初始化时间，提升用户体验。示例代码如下：
```java
// 开启预加载任务
int preLoaderId = PreLoader.preLoad(new Loader());
Intent intent = new Intent(this, PreLoadBeforeLaunchActivity.class);
intent.putExtra("preLoaderId", preLoaderId);
startActivity(intent);
// 预加载任务：模拟网络接口请求获取数据
class Loader implements DataLoader<String> {
    @Override
    public String loadData() {
        //此方法在线程池中运行，无需再开子线程去加载数据
        try {
            Thread.sleep(600);
        } catch (InterruptedException ignored) {
        }
        return "data from network server";
    }
}

// 在Activity(或Fragment)中UI初始化完成后开始监听预加载数据
PreLoader.listenData(preLoaderId, new Listener());

// 数据加载完成后，会调用DataListener.onDataArrived(...)来处理加载后的数据
class Listener implements DataListener<String> {
    @Override
    public void onDataArrived(String data) {
        //此方法在主线程中运行，无需使用Handler切换线程运行
        Toast.makeText(activity, data, Toast.LENGTH_SHORT).show();
    }
}
```


5、[SuperLike](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Qiu800820/SuperLike)：仿今日头条点赞喷射表情动画


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/124360505.gif' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
6、[30-seconds-of-code](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/30-seconds/30-seconds-of-code)：精选可以在 30秒 或更短的时间内理解的实用 JavaScript 代码片段集合


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/112507086.png' style="max-width:80%; max-height=80%;"></img></p>

7、[chrome-music-lab](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/googlecreativelab/chrome-music-lab)：Chrome 音乐实验室是一个网站，让学习音乐变得更加简单、好玩。完全基于Web端，国内可直接访问、老少皆宜、支持多种乐器，圆你一个音乐梦


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/52817073.jpg' style="max-width:80%; max-height=80%;"></img></p>

8、[mpvue](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Meituan-Dianping/mpvue)：小程序的前端框架。框架基于 Vue.js 核心，修改了 Vue.js 的 runtime 和 compiler 实现。使其可以运行在小程序环境中，为小程序开发引入了整套 Vue.js 开发体验。[5 分钟上手视频](http://mpvue.com/mpvue/quickstart/)
- 彻底的组件化开发能力：提高代码复用性
- 完整的 Vue.js 开发体验
- 方便的 Vuex 数据管理方案：方便构建复杂应用
- 快捷的 webpack 构建机制：自定义构建策略、开发阶段 hotReload
- 支持使用 npm 外部依赖
- 使用 Vue.js 命令行工具 vue-cli 快速初始化项目
- H5 代码转换编译成小程序目标代码的能力


9、[node-in-debugging](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nswbmw/node-in-debugging)：《Node.js 调试指南》作者整理了使用 Node.js 开发这几年的调试经验和思路


### Objective-C 项目
10、[LSAnimator](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Lision/LSAnimator)：通过使用 LSAnimator（Objective-C）或者 CoreAnimator（Swift）可以用少量的代码实现复杂而又易于维护的动画，并且弥补了 JHChainableAnimations 的致命缺陷。[详细描述](https://github.com/Lision/LSAnimator/blob/master/README_ZH-CN.md)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/90097004.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[WeChatPlugin-MacOS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TKkk-iOSer/WeChatPlugin-MacOS)：Mac 版微信小助手，支持自动回复、消息防撤回、远程控制、微信多开、会话置底、免认证登录、通知快捷回复等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/88876034.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
12、[dzzoffice](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zyx0814/dzzoffice)：一套开源办公套件，适用于企业、团队搭建自己的 类似 Google 企业应用套件、微软 Office365 的企业协同办公平台。[在线演示](http://demo.dzzoffice.com/)


### Python 项目
13、[haipproxy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SpiderClub/haipproxy)：使用 Scrapy＋Redis 实现的高可用分布式 IP 代理池，为大型分布式爬虫提供高可用低延迟的代理 IP 资源。
```python
from client.py_cli import ProxyFetcher
args = dict(host='127.0.0.1', port=6379, password='123456', db=0)
＃　这里`zhihu`的意思是，去和`zhihu`相关的代理ip校验队列中获取ip
＃　这么做的原因是同一个代理IP对不同网站代理效果不同
fetcher = ProxyFetcher('zhihu', strategy='greedy', redis_args=args)
# 获取一个可用代理
print(fetcher.get_proxy())
# 获取可用代理列表
print(fetcher.get_proxies()) # or print(fetcher.pool)
```

以知乎为目标抓取网站，该代理IP池的实际性能测试结果如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/103733273.png' style="max-width:80%; max-height=80%;"></img></p>

14、[MovieHeavens](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/LeetaoGoooo/MovieHeavens)：基于 Pyqt4 的电影天堂电影搜索工具，再也不用忍受各种广告和点击跳转了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/54641857.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[WechatSogou](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chyroc/WechatSogou)：基于搜狗微信搜索的微信公众号爬虫库，极易上手。示例代码：
```python
import wechatsogou

ws_api = wechatsogou.WechatSogouAPI()
ws_api.get_gzh_info('微信名称')
```


### Swift 项目
16、[iina](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/iina/iina)：Mac 下开源多媒体播放器，支持多国语言、高逼格 UI。安装：`brew cask install iina`


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/76838017.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
17、[blog](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ProtoTeam/blog)：蚂蚁数据体验技术团队的博客


18、[CS-Notes](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CyC2018/CS-Notes)：该项目整理了技术面试中需要掌握的基础知识，包含了网络、操作系统、算法、数据库、Java、分布式等


19、[front-end-interview-handbook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yangshun/front-end-interview-handbook)：与典型的软件工程师面试不同，前端面试对算法的重视比较低。面试会更多考查错综复杂的前端知识，像 HTML、CSS、JavaScript 等等。这个项目整理了这些问题，并给出了答案以及参考连接。[中文版](https://github.com/yangshun/front-end-interview-handbook/blob/master/Translations/Chinese/README.md)


20、[work-in-australia](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wahyd4/work-in-australia)：介绍程序员如何申请到澳洲工作


### 机器学习
21、[ailearning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apachecn/ailearning)：ApacheCN 制作的《机器学习实战》。配套视频：编码能力强，建议观看[《机器学习实战 - 教学版》](https://space.bilibili.com/97678687/#/channel/detail?cid=22486)。
编码能力弱，建议观看[《机器学习实战 - 讨论版》](https://space.bilibili.com/97678687/#/channel/detail?cid=13045)


22、[DeepLeague](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/farzaa/DeepLeague)：英雄联盟的机器学习项目，规模不大，适合研究一些 CV 和 ML 的算法应用


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/24/118192626.gif' style="max-width:80%; max-height=80%;"></img></p>

23、[tensorflow-docs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xitu/tensorflow-docs)：TensorFlow Docs 是由掘金翻译计划实时维护的 TensorFlow 官方文档中文版，维护者为全球各大公司开发人员和各著名高校研究者及学生




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub23.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub25.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/24'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
