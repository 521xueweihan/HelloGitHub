# 《HelloGitHub》第 47 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 目录

**Tips**：如果文中的图刷不出来，可以点击 [这里](https://hellogithub.com/periodical/volume/47/) 获取更好的阅读体验。

- [C++ 项目](#C-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [机器学习](#机器学习)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C++ 项目
1、[modern-cpp-features](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AnthonyCalandra/modern-cpp-features)：该项目介绍了现代 C++（C++11 以及之后的版本）语言和库的新特性。它能够帮助大家更快地入手新时代的 C++

2、[CPlusPlusThings](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Light-City/CPlusPlusThings)：这是一个适合 C++ 初学者从入门到进阶的教程。解决了面试者想要深入 C++ 及如何入坑 C++ 的问题。除此之外，该仓库拓展了更加深入的语法分析、多线程并发等的知识，是一个比较全面的 C++ 从入门学习到进阶提升的项目

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
3、[7days-golang](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/geektutu/7days-golang)：用 Go 在 7 天时间内实现 Web 框架、分布式缓存等应用的实战教程

4、[cli](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cli/cli)：GitHub 官方基于 Go 语言开发的命令行 GitHub 工具。用它可以在终端中执行 GitHub 的常用的管理 Issue、切分支、Clone 等操作

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/cli.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
5、[FXGLGames](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AlmasB/FXGLGames)：此项目包含 FXGL 框架构建的游戏示例。该游戏框架无需安装或设置开箱即用，游戏可以轻松打包到单个可执行文件.jar。示例代码：
```java
public class BasicGameApp extends GameApplication {
    @Override
    protected void initSettings(GameSettings settings) {
        settings.setWidth(800);
        settings.setHeight(600);
        settings.setTitle("Basic Game App");
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/FXGLGames.png' style="max-width:80%; max-height=80%;"></img></p>

6、[quarkus-quickstarts](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/quarkusio/quarkus-quickstarts)：Quarkus 开源的 Java 多种框架 demo 项目集合。这些示例项目可以快速启动、结构清晰，初学者可用作 Java 的实战项目，老手可以当作项目脚手架。启动示例：

```bash
mvn quarkus:dev
mvn clean package -Pnative
./target/amqp-quickstart-1.0-SNAPSHOT-runner
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
7、[showdoc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/star7th/showdoc)：一款基于 JavaScript 实现的开源在线文档工具。支持：多端编辑查看、权限管理、文档导出、Markdown 语法等，功能虽不多但已足够用了。推荐自建自用、小团队内部使用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/showdoc.png' style="max-width:80%; max-height=80%;"></img></p>

8、[qier-progress](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vortesnail/qier-progress)：这是一个用于缓解用户焦虑，给予用户请求回馈的顶部进度条。该项目使用 ts 重构了万星 star 的 nprogress 项目，打包体积更小、且支持了多彩模式、自定义高度和颜色等，最重要的是有良好的类型注解。该项目结构简单、代码量也比较少，非常利于学习 ts 相关用法和作为实战项目。示例代码：
```javascript
const qprogress = new QProgress()
qprogress.start()
qprogress.finish()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/qier-progress.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[image-compress-without-backend](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zerosoul/image-compress-without-backend)：一个纯前端在线图片压缩小工具。即无需上传照片到服务器，一切都在浏览器端完成，快速而高效。非常适用于图片压缩后质量要求不是很高的场景，比如：移动端图片展示等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/image-compress-without-backend.png' style="max-width:80%; max-height=80%;"></img></p>

10、[breathe-relaxer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zerosoul/breathe-relaxer)：一个在线放松网站的项目。带上耳机，[点开网站](https://works.yangerxiao.com/breathe-relaxer/)然后深呼吸

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/breathe-relaxer.png' style="max-width:80%; max-height=80%;"></img></p>

11、[wx-promise-pro](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/youngjuning/wx-promise-pro)：支持 finnaly、typescript 的微信小程序异步解决方案。特性：
- 方便集成：一处引用，处处使用
- 把微信小程序所有异步 API promise 化并挂在到 wx.pro 对象下
- 支持 ES2018 finally 特性
- 支持 TypeScript 开发

```javascript
import { promisifyAll, promisify } from 'wx-promise-pro'
// promisify all wx‘s api
promisifyAll()
// promisify single api
promisify(wx.getSystemInfo)().then(console.log)
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
12、[simplenote-macos](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Automattic/simplenote-macos)：一款 macOS 上免费开源的记事本应用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/simplenote-macos.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
13、[clean-code-php](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jupeter/clean-code-php)：PHP 代码的整洁之道，整理了一系列整洁代码实操。小到变量细道 SOLID 都有涉猎，[中文译版](https://github.com/php-cpm/clean-code-php)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
14、[wttr.in](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chubin/wttr.in)：一个 Python 实现的命令行查看天气工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/wttr.png' style="max-width:80%; max-height=80%;"></img></p>

15、[activitywatch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ActivityWatch/activitywatch)：一个记录你的时间都花在那的 Python 项目。支持 Web 可视化，效果如下

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/activitywatch.png' style="max-width:80%; max-height=80%;"></img></p>

16、[akshare](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jindaxiang/akshare)：一款基于 Python 的开源金融数据接口库。提供了股票、期货、期权、基金、数字货币等金融产品的基本数据、实时和历史行情数据、衍生数据，包含数据采集、数据清洗、到数据落地的一套开源工具。满足了金融数据科学家、数据科学爱好者在金融数据获取方面的需求。示例代码：
```python
import akshare as ak
bond_df = ak.bond_spot_deal()
print(bond_df)

   债券简称 成交净价(元) 最新收益率(%)  涨跌(BP) 加权收益率(%) 交易量(亿)
0          19国开15   98.97   3.5750    1.00   3.5826   None
1        19附息国债03   99.82   2.7714    0.14   2.7772   None
2        19附息国债11   99.87   2.8000    0.25   2.7963   None
3        19附息国债04  100.82   2.9832   -1.54   2.9747   None
4        15附息国债05  102.95   3.0359   -1.41   3.0359   None
```

17、[repoll](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NaNShaner/repoll)：基于 Django 开发的 redis 集群管理、监控工具。功能包括：标准化申请流程、管理配置、监控接口等，减轻了运维人员的痛苦

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/repoll.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
18、[Mos](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Caldis/Mos)：一个用于在 macOS 上平滑鼠标滚动效果或单独设置滚动方向的小工具。让你的滚轮爽如触控板般丝滑

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/Mos.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
19、[devops-exercises](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bregman-arie/devops-exercises)：这个仓库包含了 DevOps（开发运维）常见、流行服务相关的面试问题和回答，推荐给从事运维的同学

20、[book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rust-lang/book)：《Rust 编程语言》这是官方出品的关于 Rust 的入门书籍

21、[OnlineToolsBook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zhaoolee/OnlineToolsBook)：该项目收集了一些有趣、实用的在线工具网站，点开即用

22、[my-mac-os](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nikitavoloboev/my-mac-os)：该项目罗列了作者自用、收集的 macOS 上实用、炫酷的软件。我从中找到好几个炫酷、实用提高工作的工具，你也赶快来挑挑吧

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/my-mac-os.png' style="max-width:80%; max-height=80%;"></img></p>

23、[structured-text-tools](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dbohdan/structured-text-tools)：用于处理结构化文本数据（日志、JSON、YAML 等）的命令行工具列表

24、[apisix](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apache/apisix)：一个云原生、高性能、可扩展的微服务 API 网关。它是基于 Nginx 和 etcd 来实现，和传统 API 网关相比，APISIX 具备动态路由和插件热加载，适合微服务体系下的 API 管理

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/incubator-apisix.png' style="max-width:80%; max-height=80%;"></img></p>

25、[app-ideas](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/florinpop17/app-ideas)：该收集了各类应用的想法，并按照易学程度把应用进行划分。你可以通过这个项目提高编程技术、学习新技术

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
26、[cookbook-2nd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ipython-books/cookbook-2nd)：《IPython Cookbook 第二版》

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/47/img/cookbook-2nd.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
27、[google-research](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google-research/google-research)：非官方整理的 Google AI Research 集合项目

28、[Retinanet-Pytorch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yatengLG/Retinanet-Pytorch)：一个以 Pytorch 深度学习库实现的 retinanet 目标检测模型。项目拥有清晰的结构、完善的注释以及详细的使用说明。适用于有些许深度学习基础的初学者进行学习或在实际的目标检测项目中使用

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/46/HelloGitHub46.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/48/HelloGitHub48.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='http://gk.link/a/10q2z'>快速上手 Python 的方法</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>推荐项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有各种回馈粉丝活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/47/'>这里</a> 获取更好的阅读体验。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
