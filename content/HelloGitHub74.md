# 《HelloGitHub》第 74 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 目录

**Tips**：如果文中的图刷不出来，可以点击 [这里](https://hellogithub.com/periodical/volume/74/) 获取更好的阅读体验。

- [C 项目](#C-项目)
- [C# 项目](#C-项目-1)
- [C++ 项目](#C-项目-2)
- [CSS 项目](#CSS-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Kotlin 项目](#Kotlin-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [Rust 项目](#Rust-项目)
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

### C 项目
1、[entr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/eradman/entr)：在文件有改动时自动触发任意命令的工具。采用 kqueue 或 inotify 事件通知接口监听文件改动事件，避免轮询造成的资源浪费，可用于实现自动编译、重启、测试、同步等功能
```
# 自动 make 
find src/ | entr sh -c 'make | head -n 20'
# 自动重启服务
ls *.js | entr -r node app.js
```

2、[open-gpu-kernel-modules](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NVIDIA/open-gpu-kernel-modules)：英伟达开源的 Linux GPU 内核驱动。关于开源的原因网友们众说纷纭黑客勒索、被 Linus 骂的、拥抱开源，但无论如何这是件好事，至于这件事后续对 Linux 系统的影响就让我们拭目以待吧

3、[sioyek](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ahrm/sioyek)：免费开源的 PDF 阅读器。支持交互式快速搜索文档，而且就算文档中的引用没有链接也可以直接跳转，特别适合 PC 端阅读和研究论文、技术文档等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/sioyek.gif' style="max-width:80%; max-height=80%;"></img></p>

4、[ServerStatus](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cppla/ServerStatus)：多服务器云监控。轻松监控多台服务器状态的工具，用于解决多个不同平台下的服务器状态监控问题

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/ServerStatus.png' style="max-width:80%; max-height=80%;"></img></p>

5、[FreeRDP](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FreeRDP/FreeRDP)：完全免费的远程桌面管理工具。此项目为远程桌面协议（RDP）的一个开源实现，通过它可以轻松实现 macOS 或 Linux 远程操作 Windows 桌面系统反之亦可，使用起来十分方便和流畅。[下载地址](https://github.com/FreeRDP/FreeRDP/wiki/PreBuilds)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/FreeRDP.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
6、[TowerDefense-GameFramework-Demo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/DrFlower/TowerDefense-GameFramework-Demo)：开源的塔防游戏示例。此项目主要用来上手和学习基于 Unity 引擎的游戏框架 GameFramework，感兴趣的同学可以把玩一下。游戏共有五个关卡，玩家通过击杀敌人和建造能量塔获取资源，消耗能量建造防御塔阻止敌人攻击基地

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/TowerDefense-GameFramework-Demo.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
7、[Cpp_Primer_Practice](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/applenob/Cpp_Primer_Practice)：《C++ Primer》中文版第 5 版的学习笔记。该项目不仅包含学习笔记还有课后习题的答案

8、[serenity](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SerenityOS/serenity)：开源桌面操作系统。一款披着复古外衣现代的类 Unix 开源操作系统。从内核到 Web 浏览器均采用 C++ 编写，没有依赖现成的第三方库，外观模仿 90 年代操作系统界面的风格，我认为这是一封极客致敬经典的情书

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/serenity.png' style="max-width:80%; max-height=80%;"></img></p>

9、[polybar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/polybar/polybar)：超酷的 Linux 桌面状态栏工具。使用时无需精通 shell 就能上手，轻松完成高度自定义的状态栏。还有更多现成的主题，拿来即用[点击查看](https://github.com/adi1090x/polybar-themes)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/polybar.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
10、[weui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/weui)：微信开源的原生基础样式库。为微信内网页和小程序量身设计的样式库，包括按钮、徽章、进度条、图标、对话框等各式元素

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/weui.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
11、[httprunner](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/httprunner/httprunner)：开源的 API 测试工具。支持丰富的网络协议，涵盖接口测试、性能测试等测试类型的测试工具
- 多种网络协议：支持 HTTP(S)/HTTP2/WebSocket/RPC 等
- 多格式可选：测试用例支持 YAML/JSON/go test/pytest 格式
- 双执行引擎：同时支持 Golang/Python 两个执行引擎
- 一键部署：一条命令在 macOS/Linux/Windows 完成安装部署
- 网络性能采集：在场景化接口测试的基础上，可额外采集网络链路性能指标

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/httprunner.jpeg' style="max-width:80%; max-height=80%;"></img></p>

12、[fx](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/antonmedv/fx)：命令行 JSON 浏览工具。看似简单却十分实用的 JSON 命令行查询工具，支持流式和交互式两种查询方式

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/fx.gif' style="max-width:80%; max-height=80%;"></img></p>

13、[zinc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zinclabs/zinc)：轻量级全文搜索引擎。Go 语言下的轻量级搜索引擎，支持中文搜索自带 Web 管理界面

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/zinc.jpeg' style="max-width:80%; max-height=80%;"></img></p>

14、[ants](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/panjf2000/ants)：高性能 goroutine 池。实现了大规模下的 goroutine 调度和复用，从而节省资源提高执行效果。还有如任务提交、动态调整 pool 大小、查询运行状态等实用接口

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
15、[jclasslib](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ingokegel/jclasslib)：Java 字节码浏览器。支持可视化操作、查看、编辑编译好的 Java 类文件的开发工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/jclasslib.png' style="max-width:80%; max-height=80%;"></img></p>

16、[RuoYi](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yangzongzhuan/RuoYi)：开箱即用的权限管理系统。基于 SpringBoot 开发的后台管理系统，包含用户管理、部门管理、角色管理、登录日志、定时任务、服务监控等功能，可以用来快速构建 CMS、CRM、OA 等系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/RuoYi.png' style="max-width:80%; max-height=80%;"></img></p>

17、[debezium](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/debezium/debezium)：捕获数据更改(CDC)的流式处理平台。可以监控数据库中的数据变动，把每一个行级别的数据改动，通过流的方式实时同步给其他服务。适用于更新缓存、更新搜索、双写等场景

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/debezium.png' style="max-width:80%; max-height=80%;"></img></p>

18、[shardingsphere](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apache/shardingsphere)：一套开源的分布式数据库增强计算引擎。可将多种数据库转换为分布式数据库的生态系统，就是把多种不同类型的数据整合成对外是一个整体的数据库，即化零为整。充分合理地利用数据库的计算和存储能力，解决数据分片、数据加密、异构数据查询等痛点

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/shardingsphere.png' style="max-width:80%; max-height=80%;"></img></p>

19、[hertzbeat](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dromara/hertzbeat)：易用友好的云监控系统。适用于应用服务、数据库、网站、API、操作系统等监控的场景，可以帮助中小型团队快速搭建监控系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/hertzbeat.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
20、[fortune-sheet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ruilisi/fortune-sheet)：类似 Excel 的电子表格组件。使用简单无需繁琐的配置，内置多种 Excel 常用功能，并且支持在线协同编辑
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { Workbook } from "@fortune-sheet/react";
import "@fortune-sheet/react/dist/index.css"

ReactDOM.render(
  <Workbook data={[{ name: "Sheet1" }]} />,
  document.getElementById('root')
);
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/fortune-sheet.png' style="max-width:80%; max-height=80%;"></img></p>

21、[xterm.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xtermjs/xterm.js)：功能齐全的终端前端组件。用 TypeScript 编写的前端组件，提供了完整的终端功能、支持鼠标事件、丰富的 Unicode 支持。在众多流行开源项目中都能看到它的身影，比如 VS Code、Hyper 和 Theia 等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/xterm.png' style="max-width:80%; max-height=80%;"></img></p>

22、[WebGAL](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MakinoharaShoko/WebGAL)：易于开发的网页端视觉小说引擎。无需开发基础分分钟就能学会所有语法，立马开始创作自己的 Galgame。[在线尝试](https://demo.msfasr.com/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/WebGAL.png' style="max-width:80%; max-height=80%;"></img></p>

23、[bytemd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bytedance/bytemd)：掘金社区开源的 Markdown 编辑器组件。基于 Svelte 构建的 Markdown 编辑器组件，功能齐全还可以通过插件扩展功能，默认安全且兼容 SSR，适用于 React、Vue 和 Angular 框架
```javascript
// React
import { Editor, Viewer } from '@bytemd/react'
import gfm from '@bytemd/plugin-gfm'

const plugins = [
  gfm(),
  // Add more plugins here
]

const App = () => {
  const [value, setValue] = useState('')

  return (
    <Editor
      value={value}
      plugins={plugins}
      onChange={(v) => {
        setValue(v)
      }}
    />
  )
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/bytemd.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Kotlin 项目
24、[PermissionX](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/guolindev/PermissionX)：解决 Android 运行时权限的库。该项目本是作者写的一本书中的练手项目，后来经过不断优化和功能迭代，已经可以真正做到简化 Android 运行时权限处理的工作，所以就有了我们现在看到的 PermissionX。时至今日它依旧在持续更新，没有停下变得更好的脚步，或许这就是工匠精神的体现吧。[中文文档](https://blog.csdn.net/guolin_blog/category_10108528.html)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/PermissionX.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
25、[framework](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/flarum/framework)：简约大方的论坛项目。这是一个用 PHP+Mithril 开发的免费、美观、简单、速度快的论坛系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/framework.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
26、[pyenv](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pyenv/pyenv)：简单易用的 Python 版本管理工具。开发者有时候因为历史遗留问题，需要维护依赖不同 Pyhton 版本的项目，这时就需要安装和管理多个 Python 版本，这是一件十分痛苦的事情。而 pyenv 恰好完美地解决了这一痛点，它支持 global、local、shell 三种模式，开发者可以根据情况灵活地切换不同的 Python 版本，这一切仅需一条命令
```
安装 pyenv：brew install pyenv
安装 Python：pyenv install 3.10.4
切换版本：pyenv shell｜local｜global
shell：当前 shell
local：当前目录
global：全局
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/pyenv.png' style="max-width:80%; max-height=80%;"></img></p>

27、[Archery](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hhyo/Archery)：在线 SQL 审核平台。采用 Django+Bootstrap 框架开发而成，支持 MySQL、Oracle 等数据库的 SQL 上线、备份、慢日志查询等功能。[在线尝试](https://demo.archerydms.com/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/Archery.png' style="max-width:80%; max-height=80%;"></img></p>

28、[xxh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xxh/xxh)：在 SSH 服务器时带上自己喜欢的 shell。你的 shell 里是不是塞满了快捷脚本、工具和颜色，但在 SSH 远程连接服务器时，你就会失去这一切。xxh 可以把你最喜欢的 shell 带到任何地方
```
Oh My Zsh：source xxh.zsh anyhost +I xxh-plugin-zsh-ohmyzsh +if +q 
xonsh：xxh anyhost +s xonsh
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/xxh.png' style="max-width:80%; max-height=80%;"></img></p>

29、[Handright](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Gsllchb/Handright)：模拟手写体中文的 Python 库。基于 PIL 开发实现的工具库，能够输出手写体中文的图片，支持自定义背景图
```python
# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite

text = "分享 GitHub 上有趣、入门级开源项目"
template = Template(
    background=Image.new(mode="1", size=(1024, 2048), color=1),
    font=ImageFont.truetype("path/to/my/font.ttf", size=100),
)
images = handwrite(text, template)
for im in images:
    assert isinstance(im, Image.Image)
    im.show()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/Handright.png' style="max-width:80%; max-height=80%;"></img></p>

30、[OneForAll](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/shmilylty/OneForAll)：功能强大的子域收集工具。具有强大的子域收集能力、支持子域验证、速度快等特点的子域扫描工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/OneForAll.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
31、[solidus](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/solidusio/solidus)：开源的简约电商平台。基于 Ruby on Rails 构建的电商平台，界面清爽代码完全开源。[在线尝试](http://demo.solidus.io/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/solidus.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Rust 项目
32、[mdBook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rust-lang/mdBook)：Rust 官方开源的 Markdown 电子书构建工具。类似 Gitbook 可以将 Markdown 文件制作成在线书籍，简单易用非常适合创建教程、课程材料、开源书籍等文稿

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
33、[TermiWatch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kuglee/TermiWatch)：终端风格的 iWatch 手表面

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/TermiWatch.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
34、[opensource.guide](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/github/opensource.guide)：GitHub 官方的开源指南。为想学习如何创建和贡献开源项目的个人、社区和公司提供的资源集合，[中文](https://opensource.guide/zh-hans/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/opensource.png' style="max-width:80%; max-height=80%;"></img></p>

35、[pinball](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/flutter/pinball)：谷歌开源的弹珠台游戏。使用 Flutter 和  Firebase 平台开发的弹珠台游戏，可运行在 Android、iOS、Windows、macOS、Linux 操作系统。[在线试玩](https://pinball.flutter.dev/#/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/pinball.png' style="max-width:80%; max-height=80%;"></img></p>

36、[A-Programmers-Guide-to-English](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yujiangshui/A-Programmers-Guide-to-English)：专为程序员编写的英语学习指南。一位程序员提升英语水平的实践经验分享，还有相关训练方法和用到的工具，[点击查看](https://a-programmers-guide-to-english.harryyu.me/)

37、[code996](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hellodigua/code996)：根据 git 的提交时间推断工作强度的工具。通过分析 git 提交记录，得出是否加班、工作强度的可视化图表的工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/code996.png' style="max-width:80%; max-height=80%;"></img></p>

38、[Thanks-Mirror](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/eryajf/Thanks-Mirror)：国内公共仓库镜像的集合。该项目包含开发常用的库、软件、系统镜像地址以及使用的方法

39、[flutter_floatwing](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jiusanzhou/flutter_floatwing)：Flutter 的 Android 浮动窗口插件。该插件能够让开发者使用 Flutter 完成浮动窗口的功能开发，同时无需任何原生 Android 开发的背景

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/flutter_floatwing.gif' style="max-width:80%; max-height=80%;"></img></p>

40、[wechat-report](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/myth984/wechat-report)：自制微信聊天年度报告。教你如何生成和女朋友微信聊天记录的年度报告项目

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/wechat-report.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
41、[TCP-IP-NetworkNote](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/riba2534/TCP-IP-NetworkNote)：《TCP/IP 网络编程》学习笔记。除了笔记还包含书中的代码实现和课后习题回答

42、[machine-learning-yearning-cn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/deeplearning-ai/machine-learning-yearning-cn)：《Machine Learning Yearning》中文版。《机器学习训练秘籍》样稿吴恩达著，[在线阅读](https://deeplearning-ai.github.io/machine-learning-yearning-cn/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/machine-learning-yearning-cn.png' style="max-width:80%; max-height=80%;"></img></p>

43、[the-unix-workbench](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/seankross/the-unix-workbench)：《The Unix Workbench》该书面向刚接触编程和类 Unix（如 macOS）和 Linux 操作系统的开发者，帮你快速上手命令行以及搞懂相关知识。[在线阅读](https://seankross.com/the-unix-workbench/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
44、[WantWords](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thunlp/WantWords)：拯救词穷的字典。由清华大学 NLP 实验室开源，可以根据你的意思返回相关词汇，有效解决词穷、话到嘴边说不出来的窘境。[在线尝试](https://wantwords.net/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/WantWords.png' style="max-width:80%; max-height=80%;"></img></p>

45、[mindsdb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mindsdb/mindsdb)：用 SQL 开启机器学习的数据库。把机器学习引入 SQL 数据库将模型作为虚拟表（AI-table），从而省去了数据准备、预处理等步骤，可以直接用 SQL 查询时间序列、回归、分类预测的结果，实现简化机器学习开发流程的效果

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/mindsdb.png' style="max-width:80%; max-height=80%;"></img></p>

46、[machine_learning_complete](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Nyandwi/machine_learning_complete)：全面的机器学习教程库。一份包含 30 多个 Jupyter Notebook 的集合库，内容涵盖机器学习所需的 Python 基础，数据操作、清洗、分析、可视化常用的库和工具，以及经典机器学习、NLP、计算机视觉等算法，一份面面俱到的机器学习入门教程

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/74/img/machine_learning_complete.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub73.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | 『下一期』
</p>

---
<p align="center">
    👉 <a href='https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1xF2ECA89A2592'>云主机 4 元/月</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>推荐项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有各种回馈粉丝活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/74/'>这里</a> 获取更好的阅读体验。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
