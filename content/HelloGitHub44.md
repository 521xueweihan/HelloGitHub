# 《HelloGitHub》第 44 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/44) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[netdata](https://hellogithub.com/periodical/statistics/click?target=https://github.com/netdata/netdata)：一款免费开源的 Linux 系统性能实时监控工具。它易于安装、占用资源少、功能强大，支持监控多种服务


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/10744183.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[scrcpy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Genymobile/scrcpy)：一款可以用电脑显示并控制 Android 手机的开源工具。连接方便使用方便，手机无需 root、无需安装任何应用。支持 USB、Wi-Fi 两种方式连接，支持 Windows、macOS、Linux 三种操作系统。注意电脑端需要安装 adb 工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/111583593.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
3、[musikcube](https://hellogithub.com/periodical/statistics/click?target=https://github.com/clangen/musikcube)：一个使用 C++ 编写的终端的音乐播放器，也可以作为一个音频引擎、元数据索引器和服务器。musikcube 可以在 Windows、MacOS 、Linux 以及带有 raspbian 的树莓派上轻松编译和运行。虽然它只能在终端上使用，但是功能应有尽有。使用方法详见 [User Guide](https://github.com/clangen/musikcube/wiki/user-guide)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/32483164.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Sourcetrail](https://hellogithub.com/periodical/statistics/click?target=https://github.com/CoatiSoftware/Sourcetrail)：一个免费开源、跨平台的可视化源码探索项目。能够十分高效的帮助使用者探索、熟悉陌生的代码，支持 C、C++、Python 和 Java 语言，同时提供了相关 SDK 用于拓展支持其它语言，相信在未来会提供更多语言的支持。程序员在它的帮助下可以快速熟悉陌生项目、学习开源项目、框架等，此等利器赶快去试试吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/47690142.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
5、[evans](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ktr0731/evans)：基于 Go 语言实现的支持交互模式的 gRPC 客户端，让调试、测试 gRPC API 更加容易


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/97361468.png' style="max-width:80%; max-height=80%;"></img></p>

6、[gochat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/LockGit/gochat)：纯 Go 实现的轻量级即时通讯系统。技术上各层之间通过 rpc 通讯，使用 redis 作为消息存储与投递的载体，相对 kafka 操作起来更加方便快捷。各层之间基于 etcd 服务发现，在扩容部署时将会方便很多。架构、目录结构清晰，文档详细。而且还提供了 docker 一件构建，安装运行十分方便，推荐作为学习项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/218706050.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[guide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/uber-go/guide)：Uber 内部的 Go 风格规范。[中文翻译版](https://github.com/xxjwxc/uber_go_guide_cn)


8、[mkcert](https://hellogithub.com/periodical/statistics/click?target=https://github.com/FiloSottile/mkcert)：无需配置，执行一条命令让本地的开发环境实现 HTTPS 的工具。效果如下：
```bash
$ mkcert -install
Created a new local CA at "/Users/filippo/Library/Application Support/mkcert" 💥
The local CA is now installed in the system trust store! ⚡️
The local CA is now installed in the Firefox trust store (requires browser restart)! 🦊

$ mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1
Using the local CA at "/Users/filippo/Library/Application Support/mkcert" ✨

Created a new certificate valid for the following names 📜
 - "example.com"
 - "*.example.com"
 - "example.test"
 - "localhost"
 - "127.0.0.1"
 - "::1"

The certificate is at "./example.com+5.pem" and the key at "./example.com+5-key.pem" ✅
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/138547797.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
9、[DoKit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/didi/DoKit)：一款功能齐全的 iOS 、Android、微信小程序客户端研发助手。它功能强大、接入方便、便于扩展，能够让每一个 App 快速接入一些常用的辅助开发工具、测试效率工具、视觉辅助工具，而且能够完美在 Doraemon 面板中接入一些定制的辅助工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/144705602.png' style="max-width:80%; max-height=80%;"></img></p>

10、[newbee-mall](https://hellogithub.com/periodical/statistics/click?target=https://github.com/newbee-ltd/newbee-mall)：一基于 Spring Boot 2.X 及相关技术栈开发电商系统。包括商城系统及商城后台管理系统，支持商城常见的功能。该项目代码开源、功能完备、流程完整，对于新手开发者十分友好，仅需极短的时间就可以启动这个完整的商城项目。这是一个完整的电商项目，也推荐各个阶段的 Java 开发者学习或为项目贡献代码


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/209921402.png' style="max-width:80%; max-height=80%;"></img></p>

11、[SpringCloud](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zhoutaoo/SpringCloud)：基于 SpringCloud2.1 的微服务开发脚手架


### JavaScript 项目
12、[FileSaver.js](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eligrey/FileSaver.js)：文件保存的 JavaScript 库，支持多种常见的文件存储格式：xls、txt、png 等。它可以方便的把数据转成文件，然后供用户下载。示例代码：
```javascript
// 存储文本
var blob = new Blob(["Hello, world!"], {type: "text/plain;charset=utf-8"});
FileSaver.saveAs(blob, "hello world.txt");
```


13、[glut](https://hellogithub.com/periodical/statistics/click?target=https://github.com/LeeLejia/glut)：一款用于团队内部 chrome 工具共享的工具，可以理解为 chrome 的小程序。它提供了比页面脚本更多的 API，可是实现更丰富的功能。可以随时在页面打开的小组件，它既可以作为页面的辅助工具或者也可以提供独立的功能。演示如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/212941624.png' style="max-width:80%; max-height=80%;"></img></p>

14、[kiwi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alibaba/kiwi)：还在为前端的全球化多语言而发愁吗？可以试试阿里开源的这项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/101562026.png' style="max-width:80%; max-height=80%;"></img></p>

15、[paint](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dli/paint)：在线体验下油画创作。呈上我的“杰作”：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/81142969.png' style="max-width:80%; max-height=80%;"></img></p>

16、[qier-player](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vortesnail/qier-player)：一款基于 React 的轻量级在线视频播放器组件，界面简洁、操作流畅具有视频播放器的基础功能。方便你在项目中轻松添加播放器组件，实现视频播放功能。如果你嫌原生 video 功能太少、操作太傻、界面太简陋，那这个播放器就是你的菜。你还能够通过阅读源码学习到关于生命周期执行顺序、父子组件传值的方式、以及如何利用定时器进行一些实时的状态更新的技巧。示例代码：
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import QierPlayer from 'qier-player';

ReactDOM.render(<QierPlayer srcOrigin="你的视频地址"/>, document.getElementById('root'));
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/215043826.png' style="max-width:80%; max-height=80%;"></img></p>

17、[svrx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/svrxjs/svrx)：一个易于使用、插件化的前端开发工作台。帮助前端开发人员把折腾开发环境的时间，省下来做更有意义的事。快速开始：
1. 安装：`npm install -g @svrx/cli`
2. 创建目录：`mkdir example && cd example`
3. 创建文件：`echo '<html><body>Hello svrx!</body></html>' > index.html`
4. 运行：svrx


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/180575663.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
18、[SyncMusic](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kasuganosoras/SyncMusic)：基于 PHP Swoole 开发的在线弹幕点歌台。支持自由点歌、切歌、调整排序、删除指定音乐以及基础权限分级


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/220157762.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
19、[Gooey](https://hellogithub.com/periodical/statistics/click?target=https://github.com/chriskiehl/Gooey)：一个把 Python 命令行工具转化成 GUI 桌面工具的库。就我个人还是喜欢命令行的形式😅


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/15570122.png' style="max-width:80%; max-height=80%;"></img></p>

20、[KubeOperator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/KubeOperator/KubeOperator)：用 Python 语言开发的开源容器集群管理平台。在离线网络环境下通过可视化 Web UI 在 VMware、Openstack 或者物理机上规划、部署和管理生产级别的 Kubernetes 集群。开启你的 Kubernetes 之旅


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/158171016.png' style="max-width:80%; max-height=80%;"></img></p>

21、[opendevops](https://hellogithub.com/periodical/statistics/click?target=https://github.com/opendevops-cn/opendevops)：一款基于 tornado 的开源自动化运维云管理平台。支持：ITSM、权限系统、Web Terminnal 登陆日志审计、录像回放、监控报警系统、DNS 管理、配置中心等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/157661691.png' style="max-width:80%; max-height=80%;"></img></p>

22、[pyflame](https://hellogithub.com/periodical/statistics/click?target=https://github.com/uber-archive/pyflame)：Uber 开源的 Python 性能分析工具。可以在不修改代码的情况下分析 Python 程序的性能，同时生成火焰图


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/65319101.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
23、[pock](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pock/pock)：一款在苹果电脑的触控栏中，显示 macOS 程序坞的开源工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/103053825.png' style="max-width:80%; max-height=80%;"></img></p>

24、[SwiftyGif](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alexiscreuzot/SwiftyGif)：高性能且上手容易的 Swift GIF 库。示例代码：
```swift
import SwiftyGif

do {
    let gif = try UIImage(gifName: "MyImage.gif")
    let imageview = UIImageView(gifImage: gif, loopCount: 3) // Use -1 for infinite loop
    imageview.frame = view.bounds
    view.addSubview(imageview)
} catch {
    print(error)
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/54882337.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
25、[ML-NLP](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NLP-LOVE/ML-NLP)：该项目总结了机器学习、NLP 面试中常考到的知识点和代码实现


26、[MNN](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alibaba/MNN)：一个轻量级的深度神经网络推理引擎，在端侧加载深度神经网络模型进行推理预测。架构设计如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/181436799.png' style="max-width:80%; max-height=80%;"></img></p>

27、[openpilot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/commaai/openpilot)：comma.ai 开源的自动驾驶系统


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/74627617.jpeg' style="max-width:80%; max-height=80%;"></img></p>

### 其它
28、[CoolplaySpark](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lw-lin/CoolplaySpark)：Spark 源代码分析、类库解读等


29、[funNLP](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fighting41love/funNLP)：中文词库的集合。可用于：敏感词、语言检测、拆字词典等


30、[git-quick-stats](https://hellogithub.com/periodical/statistics/click?target=https://github.com/git-quick-stats/git-quick-stats)：项目的 git 提交记录展示和统计的工具。支持：不同时间维度和用户名的统计、近期提交的概览等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/79046698.png' style="max-width:80%; max-height=80%;"></img></p>

31、[github-cards](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lepture/github-cards)：非官方的 GitHub 卡片


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/13540116.png' style="max-width:80%; max-height=80%;"></img></p>

32、[infer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/facebook/infer)：Facebook 开源的一个支持 Objective-C、Java 和 C 语言的静态分析工具，用它可以检测 Android、iOS 代码中的资源泄漏、内存泄漏、空指针等问题。建议集成到客户端发布的流程环节中，它能够将客户端应用的一些严重 Bug 扼杀在发布应用之前，同时减少应用崩溃和性能低下的情况


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/44/29857799.png' style="max-width:80%; max-height=80%;"></img></p>

33、[TeachYourselfCS-CN](https://hellogithub.com/periodical/statistics/click?target=https://github.com/izackwu/TeachYourselfCS-CN)：《TeachYourselfCS》自学计算科学的一份书单（中文翻译版）


34、[zh.javascript.info](https://hellogithub.com/periodical/statistics/click?target=https://github.com/javascript-tutorial/zh.javascript.info)：《现代 JavaScript 教程》是以最新的 JavaScript 标准为基准的教程。通过简单但详细的内容，讲解从基础到高阶的 JavaScript 相关知识，能够帮助初中级前端提升 JavaScript 等前端技术水平。[在线阅读](https://zh.javascript.info/)




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub43.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub45.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/44'>这里</a>。
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


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
