# 《HelloGitHub》第 77 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/77) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[EasyLogger](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/armink/EasyLogger)：超轻量级 C/C++ 日志库。占用资源少适合物联网和单片机等项目，功能简单容易上手，能够通过插件形式扩展功能。特性：
- 支持终端、文件、串口、Flash 等多种输出方式
- 支持多种操作系统
- 线程安全
- 不同颜色显示

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/35313328.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[foolrenderer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cadenji/foolrenderer)：用 C 语言从零实现的软件渲染器。不用图形 API 仅用几千行 C 代码，实现了一套类似 OpenGL 的基本图形功能，以及应用于游戏开发的实时渲染技术，如阴影、切线空间法线映射、基于物理的材质系统等。该项目包含丰富的注释和数学计算推导过程的说明，可用于帮助理解和学习 GPU 的基本工作原理、基础渲染知识和着色器原理。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/410835658.gif' style="max-width:80%; max-height=80%;"></img></p>

3、[unicorn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/unicorn-engine/unicorn)：轻量级的多平台、多架构 CPU 仿真器框架。基于 QEMU 开发的 CPU 模拟器，多用于逆向、执行恶意代码等。特点：
- 多架构：ARM、ARM64、RISC-V、TriCore 等
- 多种编程语言：Python、Rust、Java、Go、JS 等
- 支持各种级别的细粒度检测

### C# 项目
4、[Bili.Uwp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Richasy/Bili.Uwp)：非官方的 B 站桌面应用。基于 UWP 框架开发的哔哩哔哩 Windows 客户端，简单易用、界面清爽，适用于 Windows 10/11 桌面系统和 Xbox。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/372096057.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[annoy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/spotify/annoy)：用于近似最近邻搜索的算法库。近似最近邻(ANN)方法是指一系列解决最近邻查找问题的近似算法，多用于内容推荐、搜索等场景。该项目是封装好的 C++/Python Annoy 算法库。Annoy 是用树为数据结构的 ANN 算法实现，它通过随机投影创建二叉树构建索引提升查询效率，采用优先队列和“森林”查询方法提高准确率，实现海量数据下的实时搜索。
```python
from annoy import AnnoyIndex
import random

f = 40  # Length of item vector that will be indexed

t = AnnoyIndex(f, 'angular')
for i in range(1000):
    v = [random.gauss(0, 1) for z in range(f)]
    t.add_item(i, v)

t.build(10) # 10 trees
t.save('test.ann')

# ...

u = AnnoyIndex(f, 'angular')
u.load('test.ann') # super fast, will just mmap the file
print(u.get_nns_by_item(0, 1000)) # will find the 1000 nearest neighbors
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/9155431.png' style="max-width:80%; max-height=80%;"></img></p>

6、[RedPanda-CPP](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/royqh1979/RedPanda-CPP)：易用的轻量级 C/C++ 集成开发环境。小熊猫 C++ 是一款专为编程新手和学生准备的 IDE，它没有复杂的安装和配置过程开箱即用。支持开发所需的自动补全、语法高亮、编译运行和调试 C/C++ 程序等功能。不仅如此，它还整合了 ege、海龟作图、raylib 等多种学习库，以及试题集和 OJ 功能，便于编程新手学习和使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/356104267.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[Stockfish](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/official-stockfish/Stockfish)：强大的国际象棋引擎。它在众多国际象棋引擎评级列表中均名列前茅，棋艺基本上是吊打职业选手。它不仅可以对战，还支持棋局分析、评估棋艺，帮助国际象棋爱好者提升棋技。虽然这是一个引擎不能单独运行，但是社区提供了丰富的 GUI 软件下载就能用，甚至还可以用来解说国际象棋比赛。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/20976138.png' style="max-width:80%; max-height=80%;"></img></p>

8、[xbmc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xbmc/xbmc)：强大自由的媒体中心软件。这是一个媒体播放器软件，但折腾一下就是家庭媒体娱乐中心。它不仅支持播放本地视频，还能够安装各种插件以及播放网络存储设备(NAS)、投屏、直播、电视、播客等源。能够运行在 Linux、macOS、Windows、Android、iOS 等设备，界面支持中文更多功能等待你的挖掘。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/1217614.gif' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
9、[Cnblogs-Theme-SimpleMemory](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/BNDong/Cnblogs-Theme-SimpleMemory)：一款以阅读为主的博客园皮肤。博客园是一个博客平台，它支持用户自定义皮肤。该项目就是一款开源的博客园皮肤，文档有详细的安装步骤，一看就会立马就能用上。虽然皮肤会让博客的访问速度变慢一点，但是皮肤效果简洁好看值得一试。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/142394932.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
10、[bk-cmdb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TencentBlueKing/bk-cmdb)：腾讯开源的配置平台。面向资产及应用的企业级配置管理平台，拥有主机管理、组织架构管理、通用权限管理、操作审计等功能。该项目的代码审核很严格，此举不仅保证了项目的代码质量，还提高了代码的可读性，推荐阅读源码。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/76221943.png' style="max-width:80%; max-height=80%;"></img></p>

11、[CasaOS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/IceWhaleTech/CasaOS)：简单易用的家庭云系统。只需一键即可安装在 NAS、树莓派等各种家庭智能设备上，让你可以随时随地管理个人数据和设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/410430370.jpg' style="max-width:80%; max-height=80%;"></img></p>

12、[colly](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gocolly/colly)：可能是最知名的 Go 爬虫框架。它拥有友好的 API 和丰富代码示例，短时间内即可上手。性能方面单核能达到 1K 请求/秒，还可以轻松管理请求方式、间隔和最大并发数，功能强大且优雅。
```go
func main() {
	c := colly.NewCollector()

	// Find and visit all links
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		e.Request.Visit(e.Attr("href"))
	})

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	c.Visit("https://go-colly.org/")
}
```

13、[ddns-go](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jeessy2/ddns-go)：简单易用的 DDNS 工具。众所周知域名解析中域名对应的是固定 IP，但是本地机器的 IP 一般是动态的，所以无法完成域名解析实现公网访问。动态 DNS(DDNS) 技术就是用来解决动态 IP 的域名解析问题，该项目能够自动获取你本机的公网 IP，并自动更新到域名服务商，从而实现公网访问本地机器。

14、[nightingale](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ccfos/nightingale)：开源的云原生监控系统。支持 Docker 等多种部署方式，集数据采集、监控告警、可视化为一体的企业级监控平台。借助高性能时序库，可以满足数亿时间线的采集、存储和告警分析的场景。该项目已在上千家企业部署落地，经历了各种生产环境的检验。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/244694886.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
15、[doris](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apache/doris)：高性能的分析数据库。一个基于 MPP 架构的高性能、实时的分析型数据库，尤其是在海量数据和高并发场景下表现优异。目前，在众多知名企业中均有使用，可用来构建用户分析、日志检索分析、用户画像等应用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/99919302.png' style="max-width:80%; max-height=80%;"></img></p>

16、[plantuml](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/plantuml/plantuml)：从文本描述生成 UML 图的工具。该项目可根据简单的文字描述画出 UML 图，支持顺序图、用例图、时序图等，除此之外还支持架构图、甘特图、思维导图、实体关系图等非 UML 图。支持在线、命令行、桌面应用等多种使用方式，可根据情况自行选择。
```
java -jar plantuml.jar 文本文件
将得到一个同名的 png 文件
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/1051476.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
17、[koodo-reader](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/troyeguo/koodo-reader)：先进的电子书阅读工具。该阅读器支持 EPUB、Kindle、PDF、漫画等多种常见文本格式，界面清爽功能丰富，拥有自定义字体、添加笔记、书签、划词翻译、导入图书、数据同步等功能。提供了 Windows、macOS 和 Linux 客户端，还支持网页版可在线使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/245049028.png' style="max-width:80%; max-height=80%;"></img></p>

18、[nocobase](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nocobase/nocobase)：易扩展的无代码开发平台。这个项目可以让你不写代码，仅通过点击和拖拽，分分钟搭建出协作和内部管理系统。项目还处于早期开发阶段，请勿用于生产环境。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/306829688.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[vanblog](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Mereithhh/vanblog)：实用的一站式个人博客系统。一款简洁优雅的博客系统，追求极致响应速度和博客体验。前后台均为响应式，支持 Docker 一键部署。前台为静态页面并支持增量渲染，按需构建更新页面。拒绝花里胡哨的功能，专注于个人博客场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/493495527.png' style="max-width:80%; max-height=80%;"></img></p>

20、[video.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/videojs/video.js)：流行的 HTML5 视频播放器。一款开箱即用的 Web 视频播放器，它支持 HTML5 视频和流媒体格式，至今有超过 45 万个网站在使用它。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/667006.png' style="max-width:80%; max-height=80%;"></img></p>

21、[vue-idle-game](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Couy69/vue-idle-game)：挂机放置类小游戏。用 Vue.js 写的在线 RPG 游戏，装备完全随机全靠刷，没有任务就是刷。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/307320394.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
22、[Unciv](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yairm210/Unciv)：一款类似《文明》的单机策略手游。仅 6M 的回合制策略游戏，玩家可以在游戏中模拟创建帝国文明，相当于开源版的《文明》安卓手游。虽然游戏画面是像素风格，但并未影响游戏体验，游戏支持中文、内容丰富可玩性非常高。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/111605778.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
23、[dooit](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kraanzu/dooit)：命令行待办事项工具。用 Python 写的交互式命令行 todo 工具，操作简单支持快捷键和鼠标，界面精致可自定义主题和图标。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/483289068.png' style="max-width:80%; max-height=80%;"></img></p>

24、[gradio](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gradio-app/gradio)：用 Python 为模型创建演示界面。这是一个用于构建机器学习和数据科学演示的 Python 库，它包含多种输入和展示的组件，使用起来极其方便，只用几行代码就可以创建出演示机器学习模型的 Web 界面。
```python
import gradio as gr
def sketch_recognition(img):
    pass# Implement your sketch recognition model here...

gr.Interface(fn=sketch_recognition, inputs="sketchpad", outputs="label").launch()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/162405963.jpg' style="max-width:80%; max-height=80%;"></img></p>

25、[label-studio](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HumanSignal/label-studio)：开源的数据标注工具。支持音频、文本、图像、视频、时间序列等，多种类型数据的标注和注释工具。
```
# 安装
pip install -U label-studio
# 运行
label-studio
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/192640529.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[libtmux](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tmux-python/libtmux)：用 Python 操作 tmux 的库。通过该项目就可以使用 Python 代码，自动操控 tmux 应用的会话、窗口、窗格。
```python
import libtmux
server = libtmux.Server()
server.list_sessions()
# [Session($3 foo), Session($1 libtmux)]
```

27、[nas-tools](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NAStool/nas-tools)：NAS 媒体库资源自动整理工具。支持资源检索和订阅、媒体库整理和通知服务的 NAS 媒体库工具，这是一个用爱发电的项目，可以不爱但请不要伤害。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/392603437.png' style="max-width:80%; max-height=80%;"></img></p>

28、[whoogle-search](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/benbusby/whoogle-search)：自架纯净谷歌搜索服务。这是一个注重保护用户隐私的元搜索引擎，它会返回过滤掉广告后的 Google 搜索结果，而且不追踪 IP、不存 Cookie。支持 Docker 部署既简单又快速，适合注重隐私的用户。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/235434204.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
29、[cheats.rs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ralfbiedert/cheats.rs)：Rust 编程语言小抄。这里不仅有 Rust 基础语法，还有执行顺序详解和编写时需要关注的注意事项。如果你觉得还不够，该项目还包含了示例代码(EX)、书籍(BK)、标准库(STD) 等 Rust 相关资料。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/157261368.png' style="max-width:80%; max-height=80%;"></img></p>

30、[py-spy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/benfred/py-spy)：用 top 的方式分析 Python 程序性能的工具。一款 Python 程序性能分析工具，它可以让你在不重启程序或修改代码的情况，直观地看到 Python 程序中每个函数花费的时间。
```shell
# 安装
pip install py-spy

# record 命令将配置文件记录到文件中，可用来生成火焰图
py-spy record -o profile.svg --pid 进程ID

# top 命令实时展示函数花费时间
py-spy top --pid 进程ID

# dump 命令显示每个 Python 线程的当前调用堆栈
py-spy dump --pid 进程ID
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/143092994.gif' style="max-width:80%; max-height=80%;"></img></p>

31、[reqwest](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/seanmonstar/reqwest)：Rust 语言的 HTTP 客户端。纯 Rust 编写的 HTTP 客户端，简单好用、支持异步、API 友好。
```rust
use std::collections::HashMap;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let resp = reqwest::blocking::get("https://httpbin.org/ip")?
        .json::<HashMap<String, String>>()?;
    println!("{:#?}", resp);
    Ok(())
}
```

### Swift 项目
32、[MonitorControl](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MonitorControl/MonitorControl)：控制 macOS 外接显示器的工具。一款 macOS 多显示器控制工具，有了它就能够在菜单栏或使用快捷键，轻松地控制外接显示器的音量、亮度、对比度。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/103784142.png' style="max-width:80%; max-height=80%;"></img></p>

33、[SwiftMessages](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SwiftKickMobile/SwiftMessages)：一个非常灵活的 iOS 消息库。用 Swift 编写的消息组件，它可以将消息灵活地显示在屏幕顶部、底部、中央，还提供了几款好看的布局和主题，拿来即用十分方便。
```swift
// 例化一个消息视图
let view = MessageView.viewFromNib(layout: .cardView)

// 带有警告样式的主题消息元素
view.configureTheme(.warning)

// 增加阴影
view.configureDropShadow()

// 设置消息标题、正文和图标
let iconText = ["🤔", "😳", "🙄", "😶"].randomElement()!
view.configureContent(title: "Warning", body: "Consider yourself warned.", iconText: iconText)

// 增加卡片周围的外部边距
view.layoutMarginAdditions = UIEdgeInsets(top: 20, left: 20, bottom: 20, right: 20)

// 显示消息
SwiftMessages.show(view: view)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/65219683.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
34、[all-contributors](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/all-contributors/all-contributors)：表彰非代码贡献者的工具。这是一个 GitHub 机器人，可以在 issues 使用指令，将贡献者增添到项目首页，进行展示和表彰。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/52710065.png' style="max-width:80%; max-height=80%;"></img></p>

35、[gibMacOS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/corpnewt/gibMacOS)：macOS 系统下载工具。通过 Python 脚本直接下载 macOS 系统文件，可用来制作 macOS 安装镜像。

36、[mackup](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lra/mackup)：自动同步应用程序设置的工具。能够帮你快速备份、同步 macOS 和 Linux 上应用配置文件的工具，包括 Zsh、Vim、iTerm2、MySQL 在内的多种开发相关应用，还支持 Dropbox、iCloud、Git 等丰富的同步方式。
```shell
# 安装
brew install mackup
# 备份
mackup backup
# 恢复
mackup restore
```

37、[sql-injection-payload-list](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/payloadbox/sql-injection-payload-list)：关于 SQL 注入知识的集合。该项目解释了什么是 SQL 注入和一些常见的例子，以及如何发现、利用、防范各种 SQL 注入漏洞。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/218447149.png' style="max-width:80%; max-height=80%;"></img></p>

38、[system-design](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/karanpratapsingh/system-design)：系统设计从入门到面试。该教程从基础协议讲起，然后介绍常见的数据库、消息队列等服务，最后是面试和实际的案例分析。内容循序渐进、图文并茂，强烈推荐大家学习。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/525105056.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
39、[babel-handbook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jamiebuilds/babel-handbook)：Babel 使用手册。内容分为「用户手册」如何安装和配置 Babel 和「插件手册」如何为 Babel 创建插件 两部分。

40、[EffectiveModernCppChinese](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CnTransGroup/EffectiveModernCppChinese)：《Effective Modern C++》中文翻译版。教你如何写出正确、高效、可维护的 C++ 代码的书，该项目为中文翻译版本(已完成)。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/74014284.png' style="max-width:80%; max-height=80%;"></img></p>

### 机器学习
41、[fauxpilot](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fauxpilot/fauxpilot)：自建 GitHub Copilot 服务。它采用 NVIDIA 的 Triton Inference Server 的 SalesForce CodeGen 模型，自建 AI 编码辅助服务。支持接入 VSCode Copilot 插件，使用起来十分方便。

42、[mmdetection](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/open-mmlab/mmdetection)：OpenMMLab 开源的目标检测工具箱。基于 PyTorch 的目标检测开源工具箱，支持 Faster R-CNN、Mask R-CNN、RetinaNet 等主流算法。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/77/145670234.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub76.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub78.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/77'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
