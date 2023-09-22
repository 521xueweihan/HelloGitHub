# 《HelloGitHub》第 83 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/83) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[sds](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/antirez/sds)：简单的 C 语言动态字符串库。Redis 作者写的 C 语言字符串库，它相较于 C 字符串，使用起来更加方便。具有速度快(常数复杂度获取字符串长度)、二进制安全(图片、音频等)、兼容部分 C 字符串函数等特点。
```c
sds mystring = sdsnew("Hello World!");
printf("%s\n", mystring);
sdsfree(mystring);

output> Hello World!
```

2、[sigma-file-manager](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/aleksey-hoffman/sigma-file-manager)：一款先进的文件管理器。这是一款免费的文件管理器，由开源社区维护。支持智能搜索、自定义主页、文件共享、文件下载、智能拖放、文件保护等功能，适用于 Windows 和 Linux。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/370679811.png' style="max-width:80%; max-height=80%;"></img></p>

3、[ttyd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tsl0922/ttyd)：简单的网络共享终端的命令行工具。基于 libuv 和 WebGL2 构建的 Web 共享终端工具，安装简单使用方便，支持 SSL、文件传输、Sixel 图像输出等功能。可运行在 Windows、macOS、Linux、OpenWrt 等操作系统上，适用于远程运维、在线管理设备等场景。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/68063511.gif' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
4、[ambie](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jenius-apps/ambie)：Windows 上的白噪声应用。一款播放白噪声和自然声音的应用，比如下雨、海滩等声音，支持混合、在线下载声音和专注功能。工作时使用可以帮助你集中注意力，还能在放松时使用有助于睡眠。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/309191418.png' style="max-width:80%; max-height=80%;"></img></p>

5、[FluentTerminal](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/felixse/FluentTerminal)：炫酷的 Windows 终端软件。基于 UWP 的 Windows 终端应用，拥有强大的自定义主题模块，能够轻松定制出风格各异的主题。提供了中文选项，支持多窗口、SSH 和搜索等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/118322286.png' style="max-width:80%; max-height=80%;"></img></p>

6、[gsudo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gerardog/gsudo)：适用于 Windows 的 sudo 命令行工具。它是 Windows 上的 sudo，允许用户以最高权限运行命令，拥有与 Unix/Linux sudo 类似的使用体验，支持 CMD、PowerShell、git-bash 等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/220251820.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
7、[Clipboard](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Slackadays/Clipboard)：小巧便捷的命令行剪贴板。一款用 C++ 编写的剪贴板工具，可以在终端的任何地方复制、剪切和粘贴东西，使用起来就像 GUI 一样方便，相见恨晚的命令行工具，适用于 Windows、Linux 和 macOS 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/568268698.png' style="max-width:80%; max-height=80%;"></img></p>

8、[doctest](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/doctest/doctest)：超快的 C++ 单头文件测试框架。这是一款轻量级、快速的 C++ 测试框架，它使用起来十分方便，引入头文件即可使用，而且速度快、编译时间短，支持 C++ 11/14/17/20。
```c++
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"

int factorial(int number) { return number <= 1 ? number : factorial(number - 1) * number; }

TEST_CASE("testing the factorial function") {
    CHECK(factorial(1) == 1);
    CHECK(factorial(2) == 2);
    CHECK(factorial(3) == 6);
    CHECK(factorial(10) == 3628800);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/22660515.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[pocketpy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/blueloveTH/pocketpy)：为嵌入游戏引擎而设计的 Python 解释器。一个 C++ 实现的轻量级的 Python 解释器，包含一个编译器和基于字节码的虚拟机，以及交互式命令窗的实现。所有功能均集成在单个头文件 pocketpy.h 中，不包含外部依赖项可以很方便地嵌入应用，立刻拥有执行 Python 代码的能力。来自 [@最大的梦想家](https://hellogithub.com/user/GvV4jfIDhMEUO5x) 的分享
```c
#include "pocketpy.h"

int main(){
    // 创建一个虚拟机
    VM* vm = pkpy_new_vm(true);
    
    // Hello world!
    pkpy_vm_exec(vm, "print('Hello world!')");

    // 构建一个列表
    pkpy_vm_exec(vm, "a = [1, 2, 3]");

    // 对列表进行求和
    char* result = pkpy_vm_eval(vm, "sum(a)");
    printf("%s", result);   // 6

    // 释放资源
    pkpy_delete(result);
    pkpy_delete(vm);
    return 0;
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/562353733.png' style="max-width:80%; max-height=80%;"></img></p>

10、[QGIS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/qgis/QGIS)：自由开源的桌面 GIS 软件。该项目采用 C++ 语言编写，GUI 部分使用的是 Qt 库。它提供了 GIS 数据可视化、编辑和分析的功能，支持多种 GIS 数据格式，适用于 Windows、Linux、macOS、BSD 和移动设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/1690480.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
11、[Dragonfly2](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dragonflyoss/Dragonfly2)：一款基于 P2P 的智能镜像和文件分发工具。它提供了高效、稳定、安全的基于 P2P 技术的文件分发和镜像加速系统，能够提高大规模文件传输的效率和速率，最大限度地利用网络带宽，适用于应用分发、缓存分发、日志分发和镜像分发等领域。来自 [@Gaius](https://hellogithub.com/user/Jn3TOfINLBjmQUS) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/309874357.jpg' style="max-width:80%; max-height=80%;"></img></p>

12、[ghz](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bojand/ghz)：简单的 gRPC 压测工具。一款用 Go 开发的专门用来压测 gRPC 服务的命令行工具，它使用简单、高效、支持自定义参数。来自 [@禹过留声](https://hellogithub.com/user/4nvWkqTsd3LhXKm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/125127188.png' style="max-width:80%; max-height=80%;"></img></p>

13、[req](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/imroc/req)：带黑魔法的 Go HTTP 客户端。该库默认就很智能，比如自动解码成 UTF-8 以避免乱码、根据 Content-Type 自动解析响应、自动检测服务器端并选择最优的 HTTP 协议、自动重试等，除此之外还提供了强大且便捷的调试功能。
```go
package main

import (
    "github.com/imroc/req/v3"
)

func main() {
    req.DevMode() // Treat the package name as a Client, enable development mode
    req.MustGet("https://httpbin.org/uuid") // Treat the package name as a Request, send GET request.

    req.EnableForceHTTP1() // Force using HTTP/1.1
    req.MustGet("https://httpbin.org/uuid")
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/83145406.png' style="max-width:80%; max-height=80%;"></img></p>

14、[sqlc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sqlc-dev/sqlc)：将 SQL 转成类型安全的 Go 代码的工具。它可以将输入的 SQL 语句，自动转化成类型安全、可读的操作数据库的 Go 代码，支持 MySQL、PostgreSQL 和 SQLite 数据库。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/193160679.png' style="max-width:80%; max-height=80%;"></img></p>

15、[tinykv](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/talent-plan/tinykv)：构建分布式 Key-Value 数据库的教程。介绍了如何用 Go 语言实现一个高可用、可水平扩展、支持分布式事务的键-值存储服务。

### Java 项目
16、[bt](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/atomashpolskiy/bt)：一个 Java 的 BitTorrent 库。支持 DHT、磁力链接、加密等功能的 Java 库，可以根据自己的喜好开发和定制 BT 工具，比如播种、下载种子等。
```java
// Create a torrent
Path torrentRoot = Paths.get("/home/torrents/mytorrent");
Path file1 = Paths.get("/home/torrents/mytorrent/file1.bin");
Path file2 = Paths.get("/home/torrents/mytorrent/file2.bin");
Path dirToAdd = Paths.get("/home/torrents/mytorrent/dir_with_files");
byte[] torrentBytes = new TorrentBuilder()
        .rootPath(torrentRoot)
        .addFiles(file1, file2, dirToAdd)
        .announce("http://example.com/announce")
        .build();
Files.write(Paths.get("/home/torrents/mytorrent.torrent"), torrentBytes);
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/58881448.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[RoaringBitmap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/RoaringBitmap/RoaringBitmap)：更好用的 Java 压缩位图数据结构。位图常用于大数据集的快速查找和去重，该项目提供的 RoaringBitmap 是一种压缩位图，相较于传统的位图数据结构，它更快、更节省内存，而且久经沙场值得信赖，比如 Spark、Hive 等知名项目上都有它的身影。
```java
import org.roaringbitmap.RoaringBitmap;

public class Basic {

  public static void main(String[] args) {
        RoaringBitmap rr = RoaringBitmap.bitmapOf(1,2,3,1000);
        RoaringBitmap rr2 = new RoaringBitmap();
        rr2.add(4000L,4255L);
        rr.select(3); // would return the third value or 1000
        rr.rank(2); // would return the rank of 2, which is index 1
        rr.contains(1000); // will return true
        rr.contains(7); // will return false

        RoaringBitmap rror = RoaringBitmap.or(rr, rr2);// new bitmap
        rr.or(rr2); //in-place computation
        boolean equals = rror.equals(rr);// true
        if(!equals) throw new RuntimeException("bug");
        // number of values stored?
        long cardinality = rr.getLongCardinality();
        System.out.println(cardinality);
        // a "forEach" is faster than this loop, but a loop is possible:
        for(int i : rr) {
          System.out.println(i);
        }
  }
}
```

### JavaScript 项目
18、[chatgpt-web](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Chanzhaoyu/chatgpt-web)：一款可自定义 API 的 ChatGPT 演示网页。基于 Express 和 Vue3 构建的 GPT-3 模型演示网页，支持接入 GPT-3 API 或网页 ChatGPT。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/599394820.png' style="max-width:80%; max-height=80%;"></img></p>

19、[illa-builder](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/illacloud/illa-builder)：一款灵活、清秀的低代码平台。由国内团队开源的低代码平台，它更新积极、处理反馈及时。功能上内置图表、表格、表单等数十种常用组件，直接拖拽即可使用。还支持 GUI 连接数据库或 API，分分钟构建出企业内部应用，支持在线、云服务和 Docker 本地部署多种使用方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/482719022.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[memos](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/usememos/memos)：一款清爽的轻量级备忘录中心。采用 React+Tailwind+TypeScript+Go 开发的备忘录中心，相当于极简的微博。支持私有/公开备忘录、标签、互动式日历等功能，以及 Docker 部署。来自 [@Yoshino-s](https://hellogithub.com/user/J6BeoT2SX1CUApN) 的分享
```shell
docker run -d --name memos -p 5230:5230 -v ~/.memos/:/var/opt/memos neosmemo/memos:latest
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/436297812.jpg' style="max-width:80%; max-height=80%;"></img></p>

21、[SingleFile](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gildas-lormeau/SingleFile)：用于网页存档的浏览器扩展。可实现一键下载网页，能够将网页上的文字、图片等内容，完整地整合到单个 HTML 文件里，支持 Chrome、Firefox、Safari、Microsoft Edge 等主流浏览器。来自 [@DarkBlue](https://hellogithub.com/user/iZ4HE13VS5c97Ol) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/906022.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[zx](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/zx)：Bash 很好但我选择用 JavaScript 写脚本。实现用 JavaScript 写 shell 脚本的工具，支持 cd、fetch、within 等函数，无需引入就可以使用 fs、os、yaml 等库。
```shell
#!/usr/bin/env zx

await $`cat package.json | grep name`

let branch = await $`git branch --show-current`
await $`dep deploy --branch=${branch}`

await Promise.all([
  $`sleep 1; echo 1`,
  $`sleep 2; echo 2`,
  $`sleep 3; echo 3`,
])

let name = 'foo bar'
await $`mkdir /tmp/${name}`
```

### Kotlin 项目
23、[ReadYou](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Ashinch/ReadYou)：一款 Material 风格的 Android RSS 阅读器。界面简洁清爽的 RSS 阅读器，支持订阅 RSS 链接、更新通知、沉浸式阅读等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/464981831.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
24、[edgedb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/edgedb/edgedb)：一款采用图-关系模型的新型开源数据库。一个底层由 PostgreSQL 提供支持的开源数据库，在兼容关系数据库特性的同时，结合了 ORM 的声明模式和 GraphQL 式的深度查询。自带 WebUI 界面，支持在线编辑数据、查询、关系可视化等功能。
```
type Person {
  required property name -> str;
}

type Movie {
  required property title -> str;
  multi link actors -> Person;
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/95817032.jpg' style="max-width:80%; max-height=80%;"></img></p>

25、[eg](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/srsudar/eg)：常用的 Linux 命令示例查询工具。它提供了 Linux 命令的常见用法，不仅使用方便而且示例简洁实用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/31691072.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[manim](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ManimCommunity/manim)：用于创建数学动画的 Python 框架。它可以用简单的代码制作出精美的数学动画，通过动画的方式直观地解释一些复杂的数学问题。来自 [@databook](https://hellogithub.com/user/1qC4w2Ey6bu0fgR) 的分享
```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

# 运行：manim -p -ql example.py SquareToCircle
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/265122478.png' style="max-width:80%; max-height=80%;"></img></p>

27、[sunfish](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thomasahle/sunfish)：100 多行代码的 Python 国际象棋引擎。一个仅用 Python 标准库和 131 行代码实现的命令行国际象棋游戏。它注释丰富结构清晰，核心代码由国际象棋逻辑、策略搜索和用户界面三个部分组成。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/16690938.png' style="max-width:80%; max-height=80%;"></img></p>

28、[xalpha](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/refraction-ray/xalpha)：Python 写的基金投资管理回测引擎。该项目可以获取基金的信息与净值，支持精确到分的投资账户记录整合、分析和可视化，简单的策略回测以及根据预设策略的定时投资提醒，适合资金反复进出的定投型和网格型投资者。
```python
jiaoyidan = xa.record(path) # 额外一行先读入 path 处的 csv 账单
shipan = xa.mul(status=jiaoyidan) # Let's rock
shipan.summary() # 看所有基金总结效果
shipan.get_stock_holdings() # 查看底层等效股票持仓
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/143284193.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
29、[lemmy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/LemmyNet/lemmy)：Rust 写的链接聚合论坛。该项目基于 Rust 的 Web 框架 Actix 和 Diesel ORM 库构建，它是一个类似 Hacker News 的网站，用户可以在上面订阅感兴趣的话题、发布链接、讨论和投票。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/170729130.jpg' style="max-width:80%; max-height=80%;"></img></p>

30、[onefetch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/o2sh/onefetch)：查看 Git 仓库信息的命令行工具。一款由 Rust 编写的命令行查看 Git 信息的工具，它可以直接在终端中展示本地 Git 仓库的详细信息，比如开源协议、提交次数、代码统计等信息。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/148829497.png' style="max-width:80%; max-height=80%;"></img></p>

31、[windows-rs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/windows-rs)：Rust 调用 Windows API 的库。由微软开源的 Rust 库，为 Rust 开发人员调用 Windows API 提供了方便，极大地改善了 Rust 语言在 Windows 系统上的开发条件。
```rust
use windows::{
    core::*, Data::Xml::Dom::*, Win32::Foundation::*, Win32::System::Threading::*,
    Win32::UI::WindowsAndMessaging::*,
};

fn main() -> Result<()> {
    let doc = XmlDocument::new()?;
    doc.LoadXml(h!("<html>hello world</html>"))?;

    let root = doc.DocumentElement()?;
    assert!(root.NodeName()? == "html");
    assert!(root.InnerText()? == "hello world");

    unsafe {
        let event = CreateEventW(None, true, false, None)?;
        SetEvent(event).ok()?;
        WaitForSingleObject(event, 0);
        CloseHandle(event).ok()?;

        MessageBoxA(None, s!("Ansi"), s!("Caption"), MB_OK);
        MessageBoxW(None, w!("Wide"), w!("Caption"), MB_OK);
    }

    Ok(())
}
```

### Swift 项目
32、[Wave](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jtrivedi/Wave)：轻松实现丝滑动画的 Swift 库。用于 iOS 和 macOS 的动画引擎库，可以轻松创建流畅、感觉很棒的动画。它没有外部依赖，可以很容易地引入进基于 UIKit、SwiftUI 或 AppKit 的项目。
```swift
if panGestureRecognizer.state == .ended {

    // Create a spring with some bounciness. `response` affects the animation's duration.
    let animatedSpring = Spring(dampingRatio: 0.68, response: 0.80)

    // Get the gesture's lift-off velocity, and pass it into the Wave animation.
    let gestureVelocity = panGestureRecognizer.velocity(in: view)

    Wave.animate(withSpring: animatedSpring, gestureVelocity: gestureVelocity) {
        // Update animatable properties on the view's `animator` property, _not_ the view itself.
        pipView.animator.center = pipViewDestination     // Some target CGPoint that you calculate.
        pipView.animator.scale = CGPoint(x: 1.1, y: 1.1)
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/498385616.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
33、[blurhash](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/woltapp/blurhash)：开源的图片占位符算法和实现。该算法可将图片编码成一段仅 20-30 个字符的短字符串，解码后可展示一张基于原图的占位图，从而提升用户的访问体验。官方提供了 C、Swift、TypeScript 等编程语言的实现，除此之外还有丰富的第三方库。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/193885464.png' style="max-width:80%; max-height=80%;"></img></p>

34、[esp32-weather-epd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lmarzen/esp32-weather-epd)：自制电子墨水屏的天气显示器。这是由一块支持 WiFi 的 ESP32 单片机和一个 7.5 英寸电子墨水屏组成的天气显示器。它能够展示通过 API 获得的天气实况和预报，以及传感器提供的室内温度和湿度。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/467381275.jpg' style="max-width:80%; max-height=80%;"></img></p>

35、[localsend](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/localsend/localsend)：AirDrop 的开源替代方案。可以通过本地网络与附近的设备，安全地共享文件和消息，此过程不需要互联网，不需要外部服务器，支持 Windows、Linux、macOS、Android、iOS 设备。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/578822531.png' style="max-width:80%; max-height=80%;"></img></p>

36、[mactype](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/snowie2000/mactype)：美化 Windows 字体的工具。一款 Windows 字体美体工具，可以解决 Windows 字体虚化的问题，实现类似苹果 macOS 系统的字体渲染效果，安装简单效果惊人。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/33294473.jpg' style="max-width:80%; max-height=80%;"></img></p>

37、[raft.github.io](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/raft/raft.github.io)：一个关于 Raft 共识算法的网站。该网站收录了关于 Raft 的论文、课程、书籍等资料，以及相关开源项目和 Raft 的运行情况可视化，帮你彻底搞懂 Raft。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/13816796.gif' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
38、[algorithmica](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/algorithmica-org/algorithmica)：《现代硬件的算法》。该书来自俄罗斯非营利性的教育组织 Tinkoff Generation，它培养了大约一半的俄罗斯奥林匹克信息学决赛选手。不管你是算法研究员还是学生，这本书都可以让你学到更多提升程序性能的实用方法。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/333536823.jpg' style="max-width:80%; max-height=80%;"></img></p>

39、[comprehensive-rust](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/comprehensive-rust)：《Comprehensive Rust》为期四天的 Rust 课程。这是谷歌 Android 团队使用的 Rust 课程，它涵盖了 Rust 的基本语法到高级主题，如泛型和错误处理，还包括最后一天的 Android 特定内容。

40、[scientific-visualization-book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rougier/scientific-visualization-book)：《科学可视化：Python+Matplotlib》。这是一本关于使用 Python 和 Matplotlib 进行科学可视化的开源书籍。该书分为四个部分：第一部分 Matplotlib 库的基本原理，第二部分致力于实战开发，第三部分是更高级的概念，即 3D 图形、优化和动画，第四部分是展示集合。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/202693400.png' style="max-width:80%; max-height=80%;"></img></p>

### 机器学习
41、[cog](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/replicate/cog)：将机器学习模型打包到容器的工具。可通过配置将机器学习模型所需的环境和依赖，自动打包到容器里方便部署，让你不再为编写 Docker 文件和 CUDA 而痛苦，还能自动启动 HTTP 接口服务方便调用。
```shell
$ cog build -t my-colorization-model
--> Building Docker image...
--> Built my-colorization-model:latest

$ docker run -d -p 5000:5000 --gpus all my-colorization-model

$ curl http://localhost:5000/predictions -X POST \
    -H 'Content-Type: application/json' \
    -d '{"input": {"image": "https://.../input.jpg"}}'
```

42、[stable-diffusion-webui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AUTOMATIC1111/stable-diffusion-webui)：Stable Diffusion 模型的 WebUI 界面。这是一个实现在浏览器上使用的 Stable Diffusion 模型的项目，支持通过文本/图片生成图片、嵌入文本、调整图片大小等功能。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/527591471.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub82.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub84.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/83'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
