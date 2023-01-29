# 《HelloGitHub》第 63 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/63) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[mgba](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mgba-emu/mgba)：用 C 语言实现的 GBA 模拟器。唤起你童年回忆的同时，还能边学边玩，然后再约上三两好友一起看看源码和实现，快乐就是这么简单


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/27788471.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
2、[rocksdb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/facebook/rocksdb)：用 C++ 编写的高性能键值存储引擎。该项目是由 Fackbook 数据库团队基于 levelDB 开发，键值均支持二进制流，能够充分利用多核 CPU 获得高性能，并兼容 levelDB 的 API 可谓是青出于蓝而胜于蓝。RocksDB 当下十分流行，一些开源数据库底层存储用的就是它


### Go 项目
3、[fzf](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/junegunn/fzf)：能够搜“一切”的模糊搜索命令行工具。它能够搜文件、历史命令、进程、git 提交记录等信息，支持预览内容、整合到 Vim/Neovim 编辑器，而且搜索速度极快


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/13807606.png' style="max-width:80%; max-height=80%;"></img></p>

4、[glab](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/profclems/glab)：用 Go 写的 GitLab 命令行工具。通过它除了能够在命令行管理项目、issues、合并提交之外，还能够查看 CI 的运行状态
```
  api:         Make authenticated REST/GRAPHQL
  auth:        Manage glab's authentication state
  issue:       Work with GitLab issues
  label:       Manage labels on remote
  mr:          Create, view and manage merge requests
  ci:          Work with GitLab CI pipelines and jobs
  release:     Manage GitLab releases
  repo:        Work with GitLab repositories and projects
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/282311579.png' style="max-width:80%; max-height=80%;"></img></p>

5、[godis](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HDT3213/godis)：用 Go 语言写的 Redis 服务器。它实现了 Redis 通信协议并兼容 redis-cli 客户端，包含 5 种常用的数据结构和命令比如：TTL、发布订阅、地理位置以及 AOF 持久化等，Go 的初学者可以通过该项目能够学习到关于 TCP、通信协议实现、常用的数据结构等知识，Web 开发学烦了？换一个口味，写个 Redis 作为实战项目吧


6、[learngo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/inancgumus/learngo)：适合新手学习 Go 语法的开源项目。学习一门编程语言最好的方法就是动手写，该仓库拥有 1000 多个 Go 语法的问题，让你可以跟着练并附有答案


7、[tunny](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Jeffail/tunny)：可设置固定数量协程的 goroutine pool 库。通过这个项目可实现 goroutine 重复使用，从而避免过度创建 goroutine 而造成的内存占用过多等问题
```go
package main

import (
	"io/ioutil"
	"net/http"
	"runtime"

	"github.com/Jeffail/tunny"
)

func main() {
	numCPUs := runtime.NumCPU()

	pool := tunny.NewFunc(numCPUs, func(payload interface{}) interface{} {
		var result []byte

		// TODO: Something CPU heavy with payload

		return result
	})
	defer pool.Close()

	http.HandleFunc("/work", func(w http.ResponseWriter, r *http.Request) {
		input, err := ioutil.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "Internal error", http.StatusInternalServerError)
		}
		defer r.Body.Close()

		// Funnel this work into our pool. This call is synchronous and will
		// block until the job is completed.
		result := pool.Process(input)

		w.Write(result.([]byte))
	})

	http.ListenAndServe(":8080", nil)
}
```


### Java 项目
8、[airbyte](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/airbytehq/airbyte)：一个开源的 EL(T) 平台。能简单快速地把用户提供的应用、数据库等地方的数据聚合到平台，从而可以在一个平台查询、展示、更新、管理这些数据


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/283046497.png' style="max-width:80%; max-height=80%;"></img></p>

9、[ExoPlayer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/ExoPlayer)：谷歌官方开源的 Android 媒体播放器。易于定制和扩展，支持丰富的数据格式比如：FMP4、FLV、SmoothStreaming、MP3 等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/20818126.png' style="max-width:80%; max-height=80%;"></img></p>

10、[traccar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/traccar/traccar)：GPS 追踪平台。此项目支持 170 多种 GPS 协议，1500 多种型号的 GPS 设备，功能包含：实时 GPS 追踪、数据统计报告、报警和通知等等


11、[Ward](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Rudolf-Barbu/Ward)：拥有漂亮仪表盘的服务器监控工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/258748710.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
12、[cusdis](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/djyde/cusdis)：这是一个界面清爽、注重隐私的轻量级博客评论系统。可以很方便地与 React、Vue 或其他博客系统结合，并且还提供了一个后台来管理所有的评论。除此之外，还支持一键从 Disqus 导入、邮件通知等强大的功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/358607805.png' style="max-width:80%; max-height=80%;"></img></p>

13、[eruda](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/liriliri/eruda)：一个专为手机端设计的前端页面调试工具。类似手机端迷你版开发者模式，可用于在手机端调试页面。主要功能包括：显示 console 日志、检查元素状态、捕获 XHR 请求、显示本地存储和 Cookie 等信息


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/53256950.jpeg' style="max-width:80%; max-height=80%;"></img></p>

14、[lowdb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/typicode/lowdb)：支持浏览器和 Electron 的轻量级 JSON 文件数据库。如果是创建没有后端的小型前端项目，但还有存储和管理数据的需求，那就快试试 lowdb 吧
```javascript
import { join } from 'path'
import { Low, JSONFile } from 'lowdb'

// 新建 JSON 文件用于存储数据
const file = join(__dirname, 'db.json')
const adapter = new JSONFile(file)
const db = new Low(adapter)

// 把内容更新到 db.data 并写入 JSON 文件
db.data.posts.push({ id: 1, title: 'lowdb is awesome' }).write()
db.get('posts')
  .filter({title: 'lowdb is awesome'})
  .sortBy('id')
  .take(5)
  .value()
```


15、[moovie.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/BMSVieira/moovie.js)：专注于电影的 HTML5 播放器。容易上手和使用，支持倍速播放、快捷键操作、字幕偏移即时调整等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/346184658.png' style="max-width:80%; max-height=80%;"></img></p>

16、[nativefier](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nativefier/nativefier)：能够把 Web 页面变成本地应用的命令行工具。通过 Electron+Chromium 把网站包装成本地 .app、.exe 等可执行文件，支持运行在 Windows、macOS 和 Linux 操作系统上


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/38558578.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
17、[mirai](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mamoe/mirai)：由 Kotlin 语言编写的 QQ 机器人框架。该项目提供了 Android QQ 协议的 API，通过这些 API 可以实现自动化操作，比如：群管理等功能，注意！该项目不支持一切商业使用。最后项目的 Kotlin 代码写的很好，感兴趣的同学可以去看下源码


### Python 项目
18、[GitHubPoster](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yihong0618/GitHubPoster)：能够把多个平台上的数据，生成类似 GitHub 绿墙图像的工具。比如能够把发推的频率、扇贝单词打卡等情况生成类似 GitHub 绿墙图像，使用简单感兴趣的同学可以把玩一下


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/360028025.png' style="max-width:80%; max-height=80%;"></img></p>

19、[guietta](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alfiopuglisi/guietta)：用于制作简单 GUI 程序的 Python 库。换一种简单的方式写 GUI（图形用户界面）程序
```python
from guietta import _, Gui, Quit
gui = Gui(
	[ "Enter numbers:",  "__a__", "+", "__b__", ["Calculate"] ],
	[    "Result: -->", "result",   _,       _,             _ ],
	[                _,        _,   _,       _,          Quit ]
)

with gui.Calculate:
	gui.result = float(gui.a) + float(gui.b)

gui.run()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/260990585.png' style="max-width:80%; max-height=80%;"></img></p>

20、[pygame](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pygame/pygame)：用来开发游戏的 Python 库。Pygame 已经持续更新多年，网上的教程和资料十分充足，虽然在游戏开发领域 Python 只是个弟弟，但如果只是用这个库开发个 2D 小游戏还是很顺手的。推荐给想用 Python 写个小游戏的朋友


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/86245815.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby 项目
21、[forem](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/forem/forem)：用来构建社区的 Ruby 开源项目。一款开源、现成的论坛项目，能够让你快速搭建起来一个社区平台。国外知名的程序员社区 dev 用的就是它


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/73648678.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
22、[azul](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fschutt/azul)：一个跨平台的 Rust 和 C/C++ 的 GUI 框架。使用 WebRender 渲染引擎和 CSS/HTML-like DOM 构建，可用于开发漂亮的原生桌面应用程序
```rust
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use azul::prelude::*;
use azul_widgets::table_view::*;

struct TableDemo {
    // cells: BTreeMap<TableCell, String>,
}

extern "C" fn layout(data: &mut RefAny, _: LayoutCallbackInfo) -> StyledDom {

    let mut table_view_state = TableViewState::default();
    table_view_state.set_cell_content(TableCellIndex { row: 2, column: 2 }, "Hello World");
    table_view_state.set_selection(Some(TableCellSelection::from(3, 4).to(3, 4)));

    TableView::new(table_view_state).dom().style(Css::empty())
}

fn main() {
    let app = App::new(RefAny::new(TableDemo { }), AppConfig::new(LayoutSolver::Default));
    app.run(WindowCreateOptions::new(layout));
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/117740918.png' style="max-width:80%; max-height=80%;"></img></p>

23、[indicatif](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/console-rs/indicatif)：样式丰富的 Rust 终端进度条库
```rust
use indicatif::ProgressBar;

let bar = ProgressBar::new(1000);
for _ in 0..1000 {
    bar.inc(1);
    // ...
}
bar.finish();
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/89145566.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[rustdesk](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rustdesk/rustdesk)：免费开源的远程桌面软件。开箱即用无需任何配置，支持 Linux/Mac/Win/Android 等平台。还能够自行搭建服务器，由用户自己掌控数据，不必担心隐私数据泄露的问题。在当下越来越多的远程桌面软件都收费的情况下的另一个选择


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/299354207.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
25、[Grid](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/exyte/Grid)：受 CSS Grid 启发，用 SwiftUI 编写关于视图（view）布局的开源项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/255865003.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[SwiftyJSON](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SwiftyJSON/SwiftyJSON)：一个 Swift JSON 三方库，用更简单的方式处理 JSON
```swift
let json = JSON(data: dataFromNetworking)
if let userName = json[0]["user"]["name"].string {
  //Now you got your value
}
```


### 其它
27、[aind](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/aind-containers/aind)：实现在 Docker 中启动安卓应用的项目
```
docker run -td --name aind --privileged -p 5900:5900 -v /lib/modules:/lib/modules:ro ghcr.io/aind-containers/aind
docker exec aind cat /home/user/.vnc/passwdfile
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/254071342.png' style="max-width:80%; max-height=80%;"></img></p>

28、[android-foss](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/offa/android-foss)：开源的安卓客户端应用集合


29、[hello-world](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/leachim6/hello-world)：汇集了 800 多种编程语言 Hello World 的项目


30、[Kanmail](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Oxygem/Kanmail)：以看板的方式管理邮件的客户端应用。适用于 Mac/Windows 操作系统，支持 Gmail、Outlook 等邮箱


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/141852287.png' style="max-width:80%; max-height=80%;"></img></p>

31、[librime](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rime/librime)：一款开源的中文输入法。市面上的输入法有很多，但你找到让自己称心如意的那款了吗？或许通过今天的开源项目你就能找到它。RIME 这款开源的输入法，它不追踪输入的内容源码完全开放，可自由切换繁/简中文，选择/设计输入方案和主题，对繁体字输入尤为优秀。作为输入法给予用户无限的自由和个性化，作为输入法框架让开发者有更多的发挥空间。比如支持不同操作系统的版本：Linux（中州韵）、Windows（小狼毫）、macOS（鼠须管）、Android（同文）由于自由度较高上手需要一些时间，这大概就是获得自由的代价吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/3776878.png' style="max-width:80%; max-height=80%;"></img></p>

32、[material-theme-jetbrains](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ChrisRM/material-theme-jetbrains)：一款 JetBrains IDE 的 Material 风格主题


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/42984727.png' style="max-width:80%; max-height=80%;"></img></p>

33、[secguide](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/secguide)：腾讯开源的代码安全指南。该项目包含：C/C++、Python、JavaScript、Java、Go 等语言的安全编码指南，内容简单易懂能够帮助开发者，在代码源头规避安全风险减少漏洞


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/368525749.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
34、[awesome-fenix](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fenixsoft/awesome-fenix)：讲述“如何构建大型且可靠的分布式系统”的开源书籍。推荐给想成为架构师的你，[在线阅读](https://icyfenix.cn/) 


35、[google-sre-ebook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/captn3m0/google-sre-ebook)：Google SRE 相关的书籍。Google SRE 是谷歌的专业运维团队的工程师，他们有一个共同的名字：Site Reliability Engineer，而这本书由 Google SRE 们撰写，分享了谷歌运维相关的一些技术和知识


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/82082721.png' style="max-width:80%; max-height=80%;"></img></p>

### 机器学习
36、[AugLy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/facebookresearch/AugLy)：Facebook 开源的一个数据增强 Python 库。该库目前支持音频、图像、文本和视频四种模式，一方面可以用现实数据对数据进行增强，另一方面还可以检测出相似内容，消除重复数据带来的干扰


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/375445655.png' style="max-width:80%; max-height=80%;"></img></p>

37、[Real-Time-Voice-Cloning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CorentinJ/Real-Time-Voice-Cloning)：克隆某个人说话声音的 AI 项目。仅需几秒音频，就能模仿出原音频的人声


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/63/188660663.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub62.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub64.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/63'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
