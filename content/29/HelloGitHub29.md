# 《HelloGitHub》第 29 期
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

🎉 最后 HelloGitHub 这个项目就诞生了 🎉

## 目录
- [C 项目](#C-项目)
- [C++ 项目](#C-项目-1)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C 项目
1、[libaco](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hnes/libaco)：一个极速、轻量级、C语言非对称协程库。[中文文档](https://github.com/hnes/libaco/blob/master/README_zh.md)，项目介绍：
- 生产级别的 C 协程库
- 核心实现不超过 700 行代码，实现了一个协程库应该有的全部功能
- 在 AWS c5d.large 机器上的性能测试，一次协程间上下文切换仅耗时 10 ns （独立执行栈）
- 一千万个协程并发执行仅消耗2.8GB的物理内存

2、[redis-3.0-annotated](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/huangz1990/redis-3.0-annotated)：[黄健宏](https://github.com/huangz1990) 在编写《Redis 设计与实现》期间，阅读 Redis 3.0 源码过程中写的注释。相信对于想要阅读 redis 源码的同学，会有很大的帮助

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
3、[BurstLinker](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bilibili/BurstLinker)：主要为 Android 开发的一个 C++ GIF 编码器。支持多种常见的颜色量化算法、颜色抖动算法

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
4、[lazygit](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jesseduffield/lazygit)：终端里的 Git 客户端。该客户端启动比各路 GUI 客户端快N倍，功能基本一致。安装 `go get github.com/jesseduffield/lazygit`，然后 `lazygit` 启动。Ready？Go！

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/lazygit.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[rclone](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rclone/rclone)：Golang 版的 rsync，与 rsync 不同的是 rclone 可以将文件同步到各种云服务的存储桶或 CDN 服务上
```
# 安装
$ curl https://rclone.org/install.sh | sudo bash
# 例如同步本地文件夹到 AWS S3 存储桶
$ rclone sync /home/local/directory remote:bucket
```

6、[dgraph](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dgraph-io/dgraph)：开源、免费的分布式图数据库。如果你在构建用户关系系统，图数据库绝对是比关系型数据库更好的选择。通过 SPARQL 查询一个用户相关的其他用户会比 SQL 快百倍。自带图形界面、RDF 导入工具等必备工具。安装：`curl https://get.dgraph.io -sSf | bash`

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/dgraph.png' style="max-width:80%; max-height=80%;"></img></p>

7、[git-bug](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MichaelMure/git-bug)：嵌入在 Git 中的分布式 bug 追踪、管理系统。用来管理 git 项目的 bug，这些信息会被存在 `.git` 文件夹里，所以其他人克隆也能看到 bug，不需要而外的存储系统。基本命令：
```
# 安装
go get github.com/MichaelMure/git-bug

# 创建新 bug
git bug new

# 把 bug 推送到远程
git bug push [<remote>]

# 列出现有的 bug
git bug ls
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/git-bug.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
8、[Heart-First-JavaWeb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/skyline75489/Heart-First-JavaWeb)：走心的 Java Web 入门开发教程，对于初学者友好。教程中列举了在初学 Java Web 的过程中，可能会遇到的问题、难点

9、[CoolViewPager](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HuanHaiLiuXin/CoolViewPager)：自定义 ViewPager 组件，支持双向自动循环、自动循环参数自由设置、界面实时刷新、自定义边缘及垂直切换效果。示例代码：
```java
public class ActivityEdgeEffectColor extends BaseActivity {
    private CoolViewPager vp;
    
    private void initViewPager(){
        vp = findViewById(R.id.vp);
        vp.setScrollMode(CoolViewPager.ScrollMode.VERTICAL);
        vp.setAutoScroll(true,1000);
        vp.setAutoScrollDirection(CoolViewPager.AutoScrollDirection.BACKWARD);
        vp.setInfiniteLoop(true);
        vp.setScrollDuration(true,600);
        vp.setDrawEdgeEffect(true);
        vp.setEdgeEffectColor(getResources().getColor(R.color.colorPrimary));
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/CoolViewPager.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[FileDownloader](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lingochamp/FileDownloader)：Android 文件下载引擎，稳定、高效、灵活、简单易用。特点：
- 单任务多线程／多连接／分块下载
- 高并发
- 独立／非独立进程
- 自动断点续传

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/FileDownloader.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
11、[react-developer-roadmap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/adam-golab/react-developer-roadmap)：该仓库中的线路图展示了学习 React 的路径，为成为一名 React 开发者指明了方向。[中文](https://github.com/adam-golab/react-developer-roadmap/blob/master/README-CN.md)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/react-developer-roadmap.png' style="max-width:80%; max-height=80%;"></img></p>

12、[pacman](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mumuy/pacman)：基于 HTML5 的吃豆人游戏。核心代码就两个文件，代码有注释、整洁。对于新手来说是个很好的实践项目。[在线试玩](http://passer-by.com/pacman/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/pacman.png' style="max-width:80%; max-height=80%;"></img></p>

13、[react-image-process](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lijinke666/react-image-process)：图片处理的 React 组件。支持压缩、裁剪、加水印、滤镜、获取主色调等功能，[在线示例](https://lijinke666.github.io/react-image-process/)
```javascript
import React from "react";
import ReactDOM from "react-dom";
import ReactImageProcess from "react-image-process";

const onComplete = data => {
  console.log("data:", data);
};

ReactDOM.render(
  <ReactImageProcess mode="base64" onComplete={onComplete}>
    <img src="YOUR_IMG_URL" />
  </ReactImageProcess>,
  document.getElementById("root")
);
```

14、[hotkeys](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jaywcjlove/hotkeys)：一个强健的 Javascript 库用于捕获键盘输入和输入的组合键。它没有依赖，压缩只有 3kb 左右。[在线展示](https://wangchujiang.com/hotkeys/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
15、[SGPlayer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/libobjc/SGPlayer)：一款基于 AVPlayer、FFmpeg 的媒体资源播放器框架。功能特点：
- 支持播放360°全景视频
- 支持手势、传感器操控360°全景视频
- 支持双眼模式，具有畸变校正、色散校正
- 支持 iOS、macOS、tvOS
- 支持 H.264 硬件解码（VideoToolBox）
- 支持 RTMP、RTSP 等直播流
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/SGPlayer.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[SBSAnimoji](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/simonbs/SBSAnimoji)：最长可以录60秒的 Animoji 画面，录制完成后可以直接按拓展按钮分享，可以学习AvatarKit的使用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/SBSAnimoji.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
17、[hue](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cloudera/hue)：开源的 Apache Hadoop UI 系统。通过使用 Hue 我们可以在浏览器端的 Web 控制台上与 Hadoop 集群进行交互来分析处理数据。核心功能：
- 数据可视化
- SQL 编辑器，支持 Hive、Impala、MySQL等
- 可进行 workflow 的编辑、查看

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/hue.png' style="max-width:80%; max-height=80%;"></img></p>

18、[FeelUOwn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/feeluown/FeelUOwn)：一个符合 Unix 哲学的跨平台的音乐播放器，主要面向 Linux/macOS 用户。特性：
- 安装简单，新手友好
- 默认提供国内各音乐平台插件（网易云、虾米、QQ）
- 较强的可扩展性可以满足大家折腾的欲望
- 核心模块有较好文档和测试覆盖

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/FeelUOwn.png' style="max-width:80%; max-height=80%;"></img></p>

19、[tinydb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/msiemens/tinydb)：TinyDB 是使用纯 Python 编写的 NoSQL 数据库，使用 json 文件存储数据。它区别于 SQLite 的关系性数据库。同样的小、不需要依赖外部服务器。适用于桌面程序、客户端，不适用于 Web 应用、高性能的数据查询。友好的 API，示例代码：
```python
>>> from tinydb import TinyDB, Query
>>> db = TinyDB('path/to/db.json')
>>> User = Query()
>>> db.insert({'name': 'John', 'age': 22})
>>> db.search(User.name == 'John')
[{'name': 'John', 'age': 22}]
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/tinydb.png' style="max-width:80%; max-height=80%;"></img></p>

20、[TGmeetup](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TGmeetup/TGmeetup)：搜集、整理、展示、报名技术类线下聚会的命令行工具，让使用者可以更加方便、及时的获取技术类活动资讯

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/TGmeetup.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
21、[snibox](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/snibox/snibox)：代码片段管理器。支持各种编程语言的代码片段、Markdown、纯文本。[在线示例](https://snibox.github.io/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/snibox.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
22、[Bartinter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MaximKotliar/Bartinter)：状态栏外观管理组件。可根据背景的颜色，动态地更改状态栏的颜色，使状态栏的信息可读

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/img/Bartinter.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
23、[chinese-independent-developer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/1c7/chinese-independent-developer)：中国独立开发者项目列表

24、[system-design-primer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/donnemartin/system-design-primer)：学习如何设计可扩展的系统将帮助你成为一个更好的工程师。这个仓库就是整理、收集系统设计方面的资源。[中文版](https://github.com/donnemartin/system-design-primer/blob/master/README-zh-Hans.md)

25、[skill-map](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TeamStuQ/skill-map)：程序员技能图谱是由极客邦科技发起的一个技术社区开源项目。汇集、整理、共建泛 IT 技术领域（人工智能，前端开发，移动开发、后端开发等）、互联网产品、运营等领域学习技能图谱，帮助程序员梳理知识框架结构。并尝试提供路径指导和精华资源，方便大家学习成长

26、[Front-End-Performance-Checklist](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thedaviddias/Front-End-Performance-Checklist)：前端性能清单，让你的网站跑的更快。性能问题不光是后端要考虑的，它也是前端需要关注的。该项目列举了在设计和编写前端项目时，性能方面需要考虑、检查的地方

27、[project-based-learning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tuvtran/project-based-learning)：编程教程仓库，这些教程分别使用不同的编程语言，从零构建应用程序。使读者通过实际项目案例，学习编译原理、操作系统、计算机网络、数据库等等。面向项目学习，比面向书本学习可操作性更高，更容易获得正向反馈

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
28、[simple_os_book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chyyuu/simple_os_book)：操作系统的基本原理与简单实现的教学项目。以操作系统基本原理为教学引导，RISC-V CPU 为底层硬件基础，设计并实现一个微型但全面的“麻雀”操作系统——ucore

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/28/HelloGitHub28.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/30/HelloGitHub30.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
