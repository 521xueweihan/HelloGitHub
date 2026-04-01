# 《HelloGitHub》第 75 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/75) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[fontforge](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fontforge/fontforge)：免费开源的字体编辑器。适用于 Windows、macOS、Linux 的编辑字体桌面工具，支持创建和编辑多种格式的字体，可用来构建自己的字体。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/5390156.png' style="max-width:80%; max-height=80%;"></img></p>

2、[micropython](https://hellogithub.com/periodical/statistics/click?target=https://github.com/micropython/micropython)：可运行在单片机上的 Python。众所周知 Python 是一门语法非常简单的编程语言，如果能用 Python 操控硬件岂不美哉！该项目就是单片机上的“迷你” Python，通过它就可以用 Python3 进行单片机开发了，大大地降低了硬件开发的入门门槛。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/15337142.jpg' style="max-width:80%; max-height=80%;"></img></p>

3、[TobudOS](https://hellogithub.com/periodical/statistics/click?target=https://github.com/OpenAtomFoundation/TobudOS)：腾讯开源的物联网终端操作系统。精简的实时操作系统(RTOS)内核，可移植到多种主流单片机，内部集成了多种物联网协议栈，具有占用资源少、低功耗、模块化、易移植、安全等特点。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/203957456.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
4、[lively](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rocksdanister/lively)：Windows 动态桌面壁纸工具。支持 Windows 用户设置多种动画文件为桌面壁纸的工具，不仅安装简单效果炫酷，而且完全免费。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/201188122.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[async_simple](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alibaba/async_simple)：阿里开源的轻量级 C++ 异步框架。提供了基于 C++20 无栈协程(Lazy)、有栈协程(Uthread) 以及 Future/Promise 等异步组件，能够轻松完成 C++ 异步的开发，广泛应用于阿里的图计算引擎、时序数据库、搜索引擎等系统。
```c++
template <class T>
using Lazy = async_simple::coro::Lazy<T>;

Lazy<int> bar() {
  // ...
  int r = co_await read_some();
  // ...
  co_return r;
}

Lazy<int> read_some() {
  // ...
  int r = co_await read_coro();
  // ...
  co_return r;
}
```

6、[folly](https://hellogithub.com/periodical/statistics/click?target=https://github.com/facebook/folly)：Facebook 开源的 C++ 工具库。包含一系列高性能的 C++ 组件库，方便且高效在 Facebook 内部被广泛应用。该项目不仅代码规范测试用例充足，而且源码中包含丰富的注释。同样功能的函数为什么别人写的性能好还健壮，这次终于可以一探究竟了。
```
AtomicHashMap.h：高性能原子数据结构
Bits.h：处理各种位操作的工具
Conv.h：处理各种数据类型的转换
dynamic.h：动态类型的对象，可用来处理 json-> map
...
```

### CSS 项目
7、[NES.css](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nostalgic-css/NES.css)：NES 风格的 CSS 框架。NES 就是我们小时候玩的“红白机”，如果你喜欢这种像素风格的画面，该项目可以让你轻松实现类似“红白机”复古游戏风格的网页。
```html
<head>
    <link href="fonts_url" rel="stylesheet">
    <link href="nes.css_url" rel="stylesheet" />

    <style>
      html, body, pre, code, kbd, samp {
          font-family: "font-family you want to use";
      }
    </style>
</head>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/150042589.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[go-best-practice](https://hellogithub.com/periodical/statistics/click?target=https://github.com/llitfkitfk/go-best-practice)：编写可维护 Go 代码的建议。《Go 语言最佳实践》一文的中文翻译版。

9、[natpass](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lwch/natpass)：多功能主机管理平台。Go 写的主机管理 Web 平台，支持 shell 和远程桌面管理 Linux、Windows 和 macOS 系统的主机。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/390982669.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[navidrome](https://hellogithub.com/periodical/statistics/click?target=https://github.com/navidrome/navidrome)：Go 写的开源音乐服务器。该项目可以用来搭建自己的音乐网站，功能丰富支持中文界面、专辑封面、多用户、各种音频格式、播放列表等功能，而且硬件要求低即使是在树莓派上也能流畅地运行。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/52481933.png' style="max-width:80%; max-height=80%;"></img></p>

11、[paopao-ce](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rocboss/paopao-ce)：一个 Go 写的轻量级社区。采用 Gin+Vue 实现的微社区，界面清爽拥有话题、发布短内容、评论等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/495645548.png' style="max-width:80%; max-height=80%;"></img></p>

12、[server](https://hellogithub.com/periodical/statistics/click?target=https://github.com/screego/server)：多用户的屏幕分享服务。该项目可以快速启动一个在线共享屏幕的服务，让用户无需安装任何软件，仅使用浏览器就能分享自己的屏幕画面。它基于网页实时通信(WebRTC) 实现，由 STUN/TURN 协议完成内网穿透和浏览器端对端的连接，既实用又有源码可以学习。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/280232135.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
13、[baritone](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cabaletta/baritone)：Minecraft 游戏机器人 。它可以帮你自动完成寻路、采集矿石等操作。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/143175496.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[cat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dianping/cat)：Java 开发的实时应用监控平台。美团开源的实时监控告警服务，能够帮助开发者快速定位线上的问题。功能丰富包括全量采集指标数据、分布式跨机房部署、性能分析报表等，还支持多种编程语言客户端。
```
Cat-client：提供给业务以及中间层埋点的底层 SDK
Cat-consumer：用于实时分析从客户端提供的数据
Cat-home：作为用户给用户提供展示的控制端
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/7010724.png' style="max-width:80%; max-height=80%;"></img></p>

15、[concurrency-limits](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Netflix/concurrency-limits)：奈飞开源的自适应限流库。当服务在面对高并发处理不过来的时候，通常会采用限流的方式来保证服务可以正常运行，但限流的阈值很难精准把控，设置小了会损失流量、大了又容易搞挂服务。该项目基于 TCP 拥塞控制算法，实现了自适应并发限制，即自动设置最佳限流阈值，从而能够在保证服务稳定的前提下，尽可能多地处理请求。
```java
// Create and configure a server builder
ServerBuilder builder = ...;

builder.addService(ServerInterceptor.intercept(service,
    ConcurrencyLimitServerInterceptor.newBuilder(
        new GrpcServerLimiterBuilder()
            .partitionByHeader(GROUP_HEADER)
            .partition("live", 0.9)
            .partition("batch", 0.1)
            .limit(WindowedLimit.newBuilder()
                    .build(Gradient2Limit.newBuilder()
                            .build()))
            .build();

    ));
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/113899964.png' style="max-width:80%; max-height=80%;"></img></p>

16、[DataX](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alibaba/DataX)：高效的离线数据同步工具。阿里开源的数据同步框架，可用于解决各种主流关系数据库、HDFS、HBase 等数据源之间的数据同步问题。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/117965972.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
17、[dicebear](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dicebear/dicebear)：供设计师和开发者使用的头像库。可根据传入的字符串，自动生成对应用户头像的库，还有免费的接口服务。支持多种不同的风格，比如：像素、冒险家、标识等。
```javascript
// 安装：npm install --save @dicebear/avatars @dicebear/micah

import { createAvatar } from '@dicebear/avatars';
import * as style from '@dicebear/micah';

let svg = createAvatar(style, {
  seed: 'custom-seed',
  // ... and other options
});
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/85701992.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[FFCreator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tnfe/FFCreator)：轻量级的视频加工库。完全基于 Node.js 实现的快速制作视频的工具，能够根据添加的图片、视频和音乐，轻松地制作出新的视频。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/307274978.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[payload](https://hellogithub.com/periodical/statistics/click?target=https://github.com/payloadcms/payload)：完全由 TypeScript 编写的“无头” CMS 系统。该项目采用 TypeScript +Node.js+React+MongoDB 构建而成，提供了完整的内容管理功能。相较于传统的 CMS 系统 Django，它没有前台部分和模版引擎（无头 headless）仅通过接口为前端提供数据，从而可以轻松地实现前后端分离，让后端程序员可以更加专注于接口开发。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/327089870.png' style="max-width:80%; max-height=80%;"></img></p>

20、[react-illustration-series](https://hellogithub.com/periodical/statistics/click?target=https://github.com/7kms/react-illustration-series)：图解 React 源码。作者从 React 项目结构和运行机制入手，先介绍 React 的整体结构，然后讲解运行核心、数据管理以及用到的高频算法。篇篇到“肉”干货满满，推荐给想要深入学习 React 源码的小伙伴。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/261826424.png' style="max-width:80%; max-height=80%;"></img></p>

21、[type-challenges](https://hellogithub.com/periodical/statistics/click?target=https://github.com/type-challenges/type-challenges)：在线挑战 TypeScript 类型问题。该项目包含了不同难度的关于 TypeScript 类型的问题以及答案，通过这些挑战可以更好地理解 TypeScript 的类型系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/281975310.png' style="max-width:80%; max-height=80%;"></img></p>

22、[visual-drag-demo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/woai3c/visual-drag-demo)：教你做低代码平台的项目。低代码平台的核心功能就是拖拽组件生成页面，该项目用 Vue 实现了一个可视化拖拽组件库，不仅如此还有配套讲解技术要点和原理分析的文章。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/321979911.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
23、[SmsForwarder](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pppscn/SmsForwarder)：Android 上的消息转发应用。可以监控 Android 手机上的短信、来电和应用通知，并根据配置好的规则自动转发给其它手机，以及包括钉钉、飞书、企业微信在内的多种主流消息平台。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/337594329.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
24、[freenom](https://hellogithub.com/periodical/statistics/click?target=https://github.com/luolongfei/freenom)：免费域名自动续期工具。因为顶级免费域名供应商 Freenom，提供的免费域名需要每年续期，该项目可以自动完成域名续期，让你轻松拥有免费的顶级域名。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/404921727.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
25、[DearPyGui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hoffstadt/DearPyGui)：强大的 Python GUI 库。底层采用 GPU 渲染提供了卓越的性能，内置多种现成的部件和样式控制，文档详细包含丰富的示例，可以轻松上手。
```python
import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/267649918.png' style="max-width:80%; max-height=80%;"></img></p>

26、[kopf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nolar/kopf)：用 Python 操作 Kubernetes 的框架。Kubernetes(k8s) 是一个容器编排系统，它本身提供了命令行工具(kubectl)，但有时无法实现较为复杂的操作。通过该项目可以用 Python 轻松完成，需要条件判断、事件触发等复杂的 k8s 操作。
```python
import kopf

@kopf.timer('kopfexamples', interval=1)
def my_timer(spec, **kwargs):
    print(f"Object's spec: {spec}")
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/288234242.png' style="max-width:80%; max-height=80%;"></img></p>

27、[nonebot2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nonebot/nonebot2)：Python 异步聊天机器人框架。该项目基于 Python 的异步特性，可以轻松处理大量的消息。提供命令行脚手架、支持多种 IM 平台，能够快速构建聊天机器人、消息通知等项目。
```shell
$ pip install nb-cli
$ nb
[?] What do you want to do?
❯ Create a New Project
  Run the Bot in Current Folder
  Driver ->
  Adapter ->
  Plugin ->
  ...
```

28、[sqlfluff](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sqlfluff/sqlfluff)：SQL 代码风格检查工具。编程语言的 linter 工具随处可见，但是少有 SQL 的工具。该项目就是用来检查、统一 SQL 代码风格的工具，支持 MySQL、BigQuery、Hive 等多种 SQL 方言。
```shell
$ pip install sqlfluff
$ echo "  SELECT a  +  b FROM tbl;  " > test.sql
$ sqlfluff lint test.sql --dialect ansi
== [test.sql] FAIL
L:   1 | P:   1 | L050 | Files must not begin with newlines or whitespace.
L:   1 | P:   3 | L003 | First line has unexpected indent
L:   1 | P:  11 | L039 | Unnecessary whitespace found.
L:   1 | P:  14 | L039 | Unnecessary whitespace found.
L:   1 | P:  27 | L001 | Unnecessary trailing whitespace.
```

### Ruby 项目
29、[gollum](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gollum/gollum)：基于 Git 的轻量级 wiki 系统。后端采用 Ruby 编写，然后 Git 作为文件存储的 wiki 系统。功能够用部署简单，但界面比较“简朴”。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/585285.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
30、[lapce](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lapce/lapce)：纯 Rust 编写的代码编辑器。基于 Rust 的 Druid 和 Xi-Editor 构建的轻快代码编辑器，内置终端、LSP 协议支持、远程开发、VIM 模式，支持 Windows、Linux、macOS。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/120425779.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
31、[Runestone](https://hellogithub.com/periodical/statistics/click?target=https://github.com/simonbs/Runestone)：适用于 iOS 的高亮文本编辑器。基于 Tree-sitter 实现的高性能 iOS 文本编辑器，支持多种编程语言的语法高亮，以及行数、显示不可见字符、插入符号对等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/448941447.png' style="max-width:80%; max-height=80%;"></img></p>

32、[SwiftFormat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nicklockwood/SwiftFormat)：用于格式化 Swift 代码的工具。当多人合作开发项目的时候，一致的代码风格就变得至关重要。该项目可以自动统一 Swift 代码风格，支持多种编辑器和命令行方式调用，适用于 macOS 和 Linux，让 Swift 代码风格统一变得十分简单和方便。
```shell
# macOS
$ brew install swiftformat
# Linux
$ mint install nicklockwood/SwiftFormat
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/66302557.png' style="max-width:80%; max-height=80%;"></img></p>

33、[WhatsNewKit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SvenTiigi/WhatsNewKit)：轻松展示应用新功能的 Swift 组件。当开发者为应用增加了新功能，就需要在用户更新后告知新功能和内容。通过该组件可以轻松展示新功能，支持高度自定义、SwiftUI、iOS 和 macOS 系统。
```swift
import SwiftUI
import WhatsNewKit

struct ContentView: View {
    
    var body: some View {
        NavigationView {
            // ...
        }
        .whatsNewSheet()
    }
    
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/134316697.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
34、[dalle-mini](https://hellogithub.com/periodical/statistics/click?target=https://github.com/borisdayma/dalle-mini)：根据文字生成图片的 AI 模型。可以按照文字提示自动生成图片，我试了下感觉生成的图片有些“抽象”。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/382680786.png' style="max-width:80%; max-height=80%;"></img></p>

35、[shap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shap/shap)：解释机器学习模型输出的库。它基于博弈论中的 Shapley Value 理论，将所有特征视为贡献者，然后计算每个特征对于模型输出结果的贡献。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/74505259.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
36、[checkchan-dist](https://hellogithub.com/periodical/statistics/click?target=https://github.com/easychen/checkchan-dist)：网页内容监控工具。能监测网页内容变化，并发送异动通知，可用来跟踪网站内容、追番剧和小说。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/494715749.png' style="max-width:80%; max-height=80%;"></img></p>

37、[codi.vim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/metakirby5/codi.vim)：显示每一行代码结果的 Vim 插件。在 Vim 编辑器里交互式展示，输入的每一行代码的运行结果，支持如 Python、Ruby、PHP、JavaScript 等多种编程语言。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/65144724.gif' style="max-width:80%; max-height=80%;"></img></p>

38、[IoT-For-Beginners](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/IoT-For-Beginners)：微软开源的物联网入门教程。如果你想学习物联网但不知道如何开始，这有一份微软制作和开源的物联网教程，课程循序渐进制作精良，包含文字、插图、视频、课后练习和边学边做的项目，非常适合初学者。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/344192338.png' style="max-width:80%; max-height=80%;"></img></p>

39、[jiffyreader-public-archive](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ansh/jiffyreader-public-archive)：仿生阅读英文的浏览器插件。通过加粗单词的首字母部分提高阅读效率，实现更轻松、快速地浏览英文网站、文章等内容的功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/494567206.png' style="max-width:80%; max-height=80%;"></img></p>

40、[live2d-widget](https://hellogithub.com/periodical/statistics/click?target=https://github.com/stevenjoezhang/live2d-widget)：网页的 Live2D 看板娘。通过该项目可以轻松地在网页上，添加可爱的“看板娘”。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/140525341.png' style="max-width:80%; max-height=80%;"></img></p>

41、[Ventoy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ventoy/Ventoy)：一个制作可启动 U 盘的开源工具。。重装系统时不用再格式化 U 盘，该项目支持直接将系统镜像拷贝进 U 盘就能启动，无需其它操作。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/246335987.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
42、[cpp-game-engine-book](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ThisisGame/cpp-game-engine-book)：《游戏引擎浅入浅出》。该书介绍了如何从零制作一个完整的游戏引擎，内容包含从基础的环境搭建，到后面的骨骼动画、多线程渲染、阴影实现等方面。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/75/345923708.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub74.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub76.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/75'>这里</a>。
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
