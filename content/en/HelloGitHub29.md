# HelloGitHub Vol.29
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C
1、[libaco](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hnes/libaco)：一个极速、轻量级、C语言非对称协程库。[中文文档](https://github.com/hnes/libaco/blob/master/README_zh.md)，项目介绍：
- 生产级别的 C 协程库
- 核心实现不超过 700 行代码，实现了一个协程库应该有的全部功能
- 在 AWS c5d.large 机器上的性能测试，一次协程间上下文切换仅耗时 10 ns （独立执行栈）
- 一千万个协程并发执行仅消耗2.8GB的物理内存


2、[redis-3.0-annotated](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/huangzworks/redis-3.0-annotated)：[黄健宏](https://github.com/huangz1990) 在编写《Redis 设计与实现》期间，阅读 Redis 3.0 源码过程中写的注释。相信对于想要阅读 redis 源码的同学，会有很大的帮助


### C++
3、[BurstLinker](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bilibili/BurstLinker)：主要为 Android 开发的一个 C++ GIF 编码器。支持多种常见的颜色量化算法、颜色抖动算法


### Go
4、[dgraph](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dgraph-io/dgraph)：开源、免费的分布式图数据库。如果你在构建用户关系系统，图数据库绝对是比关系型数据库更好的选择。通过 SPARQL 查询一个用户相关的其他用户会比 SQL 快百倍。自带图形界面、RDF 导入工具等必备工具。安装：`curl https://get.dgraph.io -sSf | bash`


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/41349039.png' style="max-width:80%; max-height=80%;"></img></p>

5、[git-bug](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/git-bug/git-bug)：嵌入在 Git 中的分布式 bug 追踪、管理系统。用来管理 git 项目的 bug，这些信息会被存在 `.git` 文件夹里，所以其他人克隆也能看到 bug，不需要而外的存储系统。基本命令：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/140680839.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[lazygit](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jesseduffield/lazygit)：终端里的 Git 客户端。该客户端启动比各路 GUI 客户端快N倍，功能基本一致。安装 `go get github.com/jesseduffield/lazygit`，然后 `lazygit` 启动。Ready？Go！


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/134017286.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[rclone](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rclone/rclone)：Golang 版的 rsync，与 rsync 不同的是 rclone 可以将文件同步到各种云服务的存储桶或 CDN 服务上
```
# 安装
$ curl https://rclone.org/install.sh | sudo bash
# 例如同步本地文件夹到 AWS S3 存储桶
$ rclone sync /home/local/directory remote:bucket
```


### Java
8、[CoolViewPager](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/HuanHaiLiuXin/CoolViewPager)：自定义 ViewPager 组件，支持双向自动循环、自动循环参数自由设置、界面实时刷新、自定义边缘及垂直切换效果。示例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/135672169.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[FileDownloader](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lingochamp/FileDownloader)：Android 文件下载引擎，稳定、高效、灵活、简单易用。特点：
- 单任务多线程／多连接／分块下载
- 高并发
- 独立／非独立进程
- 自动断点续传


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/48427914.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[Heart-First-JavaWeb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/skyline75489/Heart-First-JavaWeb)：走心的 Java Web 入门开发教程，对于初学者友好。教程中列举了在初学 Java Web 的过程中，可能会遇到的问题、难点


### JavaScript
11、[hotkeys-js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jaywcjlove/hotkeys-js)：一个强健的 Javascript 库用于捕获键盘输入和输入的组合键。它没有依赖，压缩只有 3kb 左右。[在线展示](https://wangchujiang.com/hotkeys/)


12、[pacman](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mumuy/pacman)：基于 HTML5 的吃豆人游戏。核心代码就两个文件，代码有注释、整洁。对于新手来说是个很好的实践项目。[在线试玩](http://passer-by.com/pacman/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/48824336.png' style="max-width:80%; max-height=80%;"></img></p>

13、[react-developer-roadmap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/adam-golab/react-developer-roadmap)：该仓库中的线路图展示了学习 React 的路径，为成为一名 React 开发者指明了方向。[中文](https://github.com/adam-golab/react-developer-roadmap/blob/master/README-CN.md)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/137583435.png' style="max-width:80%; max-height=80%;"></img></p>

14、[react-image-process](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lijinke666/react-image-process)：图片处理的 React 组件。支持压缩、裁剪、加水印、滤镜、获取主色调等功能，[在线示例](https://lijinke666.github.io/react-image-process/)
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


### Objective-C
15、[SBSAnimoji](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/simonbs/SBSAnimoji)：最长可以录60秒的 Animoji 画面，录制完成后可以直接按拓展按钮分享，可以学习AvatarKit的使用


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/109750717.png' style="max-width:80%; max-height=80%;"></img></p>

16、[SGPlayer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/libobjc/SGPlayer)：一款基于 AVPlayer、FFmpeg 的媒体资源播放器框架。功能特点：
- 支持播放360°全景视频
- 支持手势、传感器操控360°全景视频
- 支持双眼模式，具有畸变校正、色散校正
- 支持 iOS、macOS、tvOS
- 支持 H.264 硬件解码（VideoToolBox）
- 支持 RTMP、RTSP 等直播流
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/84404175.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python
17、[FeelUOwn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/feeluown/FeelUOwn)：一个符合 Unix 哲学的跨平台的音乐播放器，主要面向 Linux/macOS 用户。特性：
- 安装简单，新手友好
- 默认提供国内各音乐平台插件（网易云、虾米、QQ）
- 较强的可扩展性可以满足大家折腾的欲望
- 核心模块有较好文档和测试覆盖


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/38036470.png' style="max-width:80%; max-height=80%;"></img></p>

18、[hue](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cloudera/hue)：开源的 Apache Hadoop UI 系统。通过使用 Hue 我们可以在浏览器端的 Web 控制台上与 Hadoop 集群进行交互来分析处理数据。核心功能：
- 数据可视化
- SQL 编辑器，支持 Hive、Impala、MySQL等
- 可进行 workflow 的编辑、查看


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/732593.png' style="max-width:80%; max-height=80%;"></img></p>

19、[TGmeetup](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TGmeetup/TGmeetup)：搜集、整理、展示、报名技术类线下聚会的命令行工具，让使用者可以更加方便、及时的获取技术类活动资讯


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/115522323.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[tinydb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/msiemens/tinydb)：TinyDB 是使用纯 Python 编写的 NoSQL 数据库，使用 json 文件存储数据。它区别于 SQLite 的关系性数据库。同样的小、不需要依赖外部服务器。适用于桌面程序、客户端，不适用于 Web 应用、高性能的数据查询。友好的 API，示例代码：
```python
>>> from tinydb import TinyDB, Query
>>> db = TinyDB('path/to/db.json')
>>> User = Query()
>>> db.insert({'name': 'John', 'age': 22})
>>> db.search(User.name == 'John')
[{'name': 'John', 'age': 22}]
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/11380094.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby
21、[snibox](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/snibox/snibox)：代码片段管理器。支持各种编程语言的代码片段、Markdown、纯文本。[在线示例](https://snibox.github.io/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/116063695.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
22、[Bartinter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/MaximKotliar/Bartinter)：状态栏外观管理组件。可根据背景的颜色，动态地更改状态栏的颜色，使状态栏的信息可读


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/29/137921876.gif' style="max-width:80%; max-height=80%;"></img></p>

### Other
23、[chinese-independent-developer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/1c7/chinese-independent-developer)：中国独立开发者项目列表


24、[Front-End-Performance-Checklist](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/thedaviddias/Front-End-Performance-Checklist)：前端性能清单，让你的网站跑的更快。性能问题不光是后端要考虑的，它也是前端需要关注的。该项目列举了在设计和编写前端项目时，性能方面需要考虑、检查的地方


25、[project-based-learning](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/practical-tutorials/project-based-learning)：编程教程仓库，这些教程分别使用不同的编程语言，从零构建应用程序。使读者通过实际项目案例，学习编译原理、操作系统、计算机网络、数据库等等。面向项目学习，比面向书本学习可操作性更高，更容易获得正向反馈


26、[skill-map](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TeamStuQ/skill-map)：程序员技能图谱是由极客邦科技发起的一个技术社区开源项目。汇集、整理、共建泛 IT 技术领域（人工智能，前端开发，移动开发、后端开发等）、互联网产品、运营等领域学习技能图谱，帮助程序员梳理知识框架结构。并尝试提供路径指导和精华资源，方便大家学习成长


27、[system-design-primer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/donnemartin/system-design-primer)：学习如何设计可扩展的系统将帮助你成为一个更好的工程师。这个仓库就是整理、收集系统设计方面的资源。[中文版](https://github.com/donnemartin/system-design-primer/blob/master/README-zh-Hans.md)


### Book
28、[simple_os_book](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chyyuu/simple_os_book)：操作系统的基本原理与简单实现的教学项目。以操作系统基本原理为教学引导，RISC-V CPU 为底层硬件基础，设计并实现一个微型但全面的“麻雀”操作系统——ucore




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub28.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub30.md">『Next』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/en/periodical'>Submit open-source project!</a> 👈<br>
</p>

## Sponsor


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
      <th align="center" style="width: 80px;">
        <a href="https://ofox.ai/zh?utm_source=github&utm_medium=hellogithub&utm_campaign=sponsor">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/0foxai.png" width="60px"><br>
          <sub>OfoxAI</sub><br>
          <sub>100+ 模型官方直连不掉线</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
