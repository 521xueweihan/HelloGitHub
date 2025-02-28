# HelloGitHub Vol.83
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
1、[sds](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/antirez/sds)：Simple C Language Dynamic String Library. A C language string library written by the author of Redis, which is more convenient to use compared to C strings. It features fast operation (constant complexity in obtaining string length), binary safety (for images, audio, etc.), and compatibility with some C string functions.
```c
sds mystring = sdsnew("Hello World!");
printf("%s\n", mystring);
sdsfree(mystring);

output> Hello World!
```

2、[sigma-file-manager](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/aleksey-hoffman/sigma-file-manager)：An Advanced File Manager. This is a free file manager maintained by the open source community. It supports intelligent search, customizable homepage, file sharing, file downloading, smart drag and drop, and file protection, and is suitable for Windows and Linux.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/370679811.png' style="max-width:80%; max-height=80%;"></img></p>

3、[ttyd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tsl0922/ttyd)：A Simple Command-line Tool for Web-based Terminal Sharing. This web-based terminal sharing tool is built with libuv and WebGL2. It's easy to install and convenient to use, supporting SSL, file transfer, and Sixel image output. It can run on Windows, macOS, Linux, and OpenWrt operating systems, and is suitable for scenarios such as remote operations and maintenance and online device management.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/68063511.gif' style="max-width:80%; max-height=80%;"></img></p>

### C#
4、[ambie](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jenius-apps/ambie)：White Noise App for Windows. An application that plays white noise and natural sounds such as rain and beach sounds, supporting mixing, online download of sounds, and focus features. Using it during work can help you concentrate, and it can also aid in sleep when used for relaxation.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/309191418.png' style="max-width:80%; max-height=80%;"></img></p>

5、[FluentTerminal](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/felixse/FluentTerminal)：Cool Windows Terminal Software. A UWP-based Windows terminal application with a powerful custom theme module, allowing for the easy creation of a variety of themes. It includes Chinese language options and supports multiple windows, SSH, and search functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/118322286.png' style="max-width:80%; max-height=80%;"></img></p>

6、[gsudo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gerardog/gsudo)：sudo Command-Line Tool for Windows. It is a sudo for Windows that allows users to run commands with the highest privileges, offering a similar experience to Unix/Linux sudo, supporting CMD, PowerShell, git-bash, and more.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/220251820.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++
7、[Clipboard](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Slackadays/Clipboard)：Compact and Convenient Command-Line Clipboard. A clipboard utility written in C++ that allows copying, cutting, and pasting in any terminal, as conveniently as a GUI, it's a command-line tool that's worth meeting late, compatible with Windows, Linux, and macOS operating systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/568268698.png' style="max-width:80%; max-height=80%;"></img></p>

8、[doctest](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/doctest/doctest)：Ultra-Fast C++ Single-Header Test Framework. This is a lightweight, fast C++ testing framework that is very easy to use, features a single-header file, and offers quick speed and short compilation time, supporting C++ 11/14/17/20.
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

9、[pocketpy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pocketpy/pocketpy)：A Python Interpreter Designed for Game Engines. A lightweight Python interpreter implemented in C++, including a compiler and a bytecode-based virtual machine, as well as the implementation of an interactive command window. All functionalities are integrated into a single header file 'pocketpy.h', which can be easily embedded into applications without external dependencies, instantly providing the ability to execute Python code.Shared by [@最大的梦想家](https://hellogithub.com/en/user/GvV4jfIDhMEUO5x)
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

10、[QGIS](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/qgis/QGIS)：Free and Open Source Desktop GIS Software. This project is written in C++ language, with the GUI part utilizing the Qt library. It offers functionalities for GIS data visualization, editing, and analysis, supports various GIS data formats, and is applicable to Windows, Linux, macOS, BSD, and mobile devices.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/1690480.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
11、[dragonfly](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dragonflyoss/dragonfly)：A P2P-based Intelligent Mirroring and File Distribution Tool. It offers an efficient, stable, and secure file distribution and mirroring acceleration system based on P2P technology, enhancing the efficiency and speed of large-scale file transfers while maximizing network bandwidth utilization. It is suitable for areas such as application distribution, cache distribution, log distribution, and mirror distribution.Shared by [@Gaius](https://hellogithub.com/en/user/Jn3TOfINLBjmQUS)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/309874357.jpg' style="max-width:80%; max-height=80%;"></img></p>

12、[ghz](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bojand/ghz)：Simple gRPC Stress Testing Tool. A command-line tool developed using Go specifically for stress testing gRPC services, it is easy to use, efficient, and supports custom parameters.Shared by [@禹过留声](https://hellogithub.com/en/user/4nvWkqTsd3LhXKm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/125127188.png' style="max-width:80%; max-height=80%;"></img></p>

13、[req](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/imroc/req)：Go HTTP Client with Dark Magic. This library is intelligent by default, such as automatic decoding to UTF-8 to avoid garbled text, automatic response parsing based on Content-Type, automatic server detection and selection of the optimal HTTP protocol, automatic retries, in addition to this it also provides powerful and convenient debugging capabilities.
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

14、[sqlc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sqlc-dev/sqlc)：Tool to Convert SQL to Type-Safe Go Code. It automatically converts input SQL statements into type-safe, readable Go code for database operations, supporting MySQL, PostgreSQL, and SQLite databases.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/193160679.png' style="max-width:80%; max-height=80%;"></img></p>

15、[tinykv](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/talent-plan/tinykv)：Tutorial on Building Distributed Key-Value Database. Provides an introduction on how to implement a highly available, horizontally scalable, distributed transaction-supporting key-value storage service using the Go programming language.

### Java
16、[bt](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/atomashpolskiy/bt)：A Java BitTorrent Library. A Java library supporting DHT, magnet links, encryption, and other features, allowing for the development and customization of BT tools according to personal preference, such as seeding and downloading torrents.
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

17、[RoaringBitmap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/RoaringBitmap/RoaringBitmap)：A More Efficient Java Compressed Bitmap Data Structure. Bitmaps are commonly used for quick lookups and deduplication in large datasets. This project offers RoaringBitmap, a compressed bitmap data structure that is faster and more memory-efficient compared to traditional bitmap structures. It has been proven reliable through extensive use in well-known projects such as Spark and Hive.
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

### JavaScript
18、[chatgpt-web](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Chanzhaoyu/chatgpt-web)：A Customizable API ChatGPT Demo Webpage. A GPT-3 model demo webpage built with Express and Vue3, supporting integration with GPT-3 API or the webpage ChatGPT.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/599394820.png' style="max-width:80%; max-height=80%;"></img></p>

19、[illa-builder](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/illacloud/illa-builder)：一款灵活、清秀的低代码平台。由国内团队开源的低代码平台，它更新积极、处理反馈及时。功能上内置图表、表格、表单等数十种常用组件，直接拖拽即可使用。还支持 GUI 连接数据库或 API，分分钟构建出企业内部应用，支持在线、云服务和 Docker 本地部署多种使用方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/482719022.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[memos](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/usememos/memos)：A Refreshing Lightweight Memo Center. This is a memo center developed using React, Tailwind, TypeScript, and Go, akin to a minimalist Weibo. It supports private/public memos, tags, interactive calendar, and is deployable with Docker.Shared by [@Yoshino-s](https://hellogithub.com/en/user/J6BeoT2SX1CUApN)
```shell
docker run -d --name memos -p 5230:5230 -v ~/.memos/:/var/opt/memos neosmemo/memos:latest
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/436297812.jpg' style="max-width:80%; max-height=80%;"></img></p>

21、[SingleFile](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gildas-lormeau/SingleFile)：Browser Extension for Webpage Archiving. Enables one-click downloads of webpages, capable of fully integrating text, images, and other content on the webpage into a single HTML file, supporting mainstream browsers such as Chrome, Firefox, Safari, and Microsoft Edge.Shared by [@DarkBlue](https://hellogithub.com/en/user/iZ4HE13VS5c97Ol)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/906022.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[zx](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google/zx)：Bash is fine but I choose to write scripts in JavaScript. A tool for writing shell scripts in JavaScript, supporting functions like cd, fetch, within, and allowing the use of libraries such as fs, os, yaml without the need to introduce them.
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

### Kotlin
23、[ReadYou](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Ashinch/ReadYou)：An Android RSS Reader with a Material Design Style. A minimalist and refreshing RSS reader that supports RSS feed subscription, update notifications, and immersive reading experiences.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/464981831.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
24、[eg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/srsudar/eg)：Common Linux Command Example Query Tool. It provides common usages of Linux commands, which are not only easy to use but also concise and practical examples.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/31691072.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[gel](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/geldata/gel)：A New Open-Source Database Using Graph-Relational Model. An open-source database supported by PostgreSQL at its core, combining the characteristics of relational databases with the declarative mode of ORM and the deep query style of GraphQL. It features a built-in WebUI interface, supporting online data editing, querying, and relation visualization capabilities.
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

26、[manim](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ManimCommunity/manim)：A Python Framework for Creating Mathematical Animations. It can produce beautiful mathematical animations with simple code, intuitively explaining some complex mathematical problems through animation.Shared by [@databook](https://hellogithub.com/en/user/1qC4w2Ey6bu0fgR)
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

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/265122478.gif' style="max-width:80%; max-height=80%;"></img></p>

27、[sunfish](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/thomasahle/sunfish)：A Python Chess Engine in Just Over 100 Lines of Code. A command-line chess game implemented using only Python's standard library and 131 lines of code with rich comments and a clear structure. The core code is divided into three main parts: chess logic, strategy search, and user interface.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/16690938.png' style="max-width:80%; max-height=80%;"></img></p>

28、[xalpha](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/refraction-ray/xalpha)：A Fund Investment Management Backtesting Engine Written in Python. This project can fetch fund information and net value, supports precise to the penny integration, analysis, and visualization of investment account records, simple strategy backtesting, and scheduled investment reminders based on preset strategies, making it suitable for investors with repeated capital inflows and outflows, such as those who engage in dollar-cost averaging and grid trading strategies.
```python
jiaoyidan = xa.record(path) # 额外一行先读入 path 处的 csv 账单
shipan = xa.mul(status=jiaoyidan) # Let's rock
shipan.summary() # 看所有基金总结效果
shipan.get_stock_holdings() # 查看底层等效股票持仓
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/143284193.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust
29、[lemmy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LemmyNet/lemmy)：Forum Aggregator Written in Rust. The project is built using the Rust web framework Actix and the Diesel ORM library. It is a website similar to Hacker News, where users can subscribe to topics of interest, post links, discuss, and vote.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/170729130.jpg' style="max-width:80%; max-height=80%;"></img></p>

30、[onefetch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/o2sh/onefetch)：A Command-Line Tool for Viewing Git Repository Information. A command-line tool written in Rust for viewing information about Git repositories. It can directly display detailed information of local Git repositories in the terminal, such as open-source licenses, number of commits, code statistics, and more.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/148829497.png' style="max-width:80%; max-height=80%;"></img></p>

31、[windows-rs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/windows-rs)：Rust Library for Calling Windows API. An open-source Rust library by Microsoft, providing convenience for Rust developers to call Windows API, greatly improving the development conditions of the Rust language on the Windows system.
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

### Swift
32、[Wave](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jtrivedi/Wave)：Swift Library for Smooth Animations. A animation engine library for iOS and macOS, which can easily create smooth and pleasant animations. It has no external dependencies and can be easily introduced into UIKit, SwiftUI, or AppKit based projects.
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

### AI
33、[cog](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/replicate/cog)：Tool for Packaging Machine Learning Models into Containers. This tool allows for the automatic packaging of machine learning model dependencies and environment into a container for easy deployment through configuration, eliminating the need to manually write Docker files and deal with CUDA issues. It also conveniently starts an HTTP interface service for easy access.
```shell
$ cog build -t my-colorization-model
--> Building Docker image...
--> Built my-colorization-model:latest

$ docker run -d -p 5000:5000 --gpus all my-colorization-model

$ curl http://localhost:5000/predictions -X POST \
    -H 'Content-Type: application/json' \
    -d '{"input": {"image": "https://.../input.jpg"}}'
```

34、[stable-diffusion-webui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AUTOMATIC1111/stable-diffusion-webui)：WebUI Interface for the Stable Diffusion Model. This is a project that implements the Stable Diffusion model for use in a web browser, supporting features such as generating images through text or pictures, embedding text, and adjusting image sizes.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/527591471.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
35、[blurhash](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/woltapp/blurhash)：Open Source Image Placeholder Algorithms and Implementations. This algorithm can encode an image into a short string of only 20-30 characters, and the decoded image can display a placeholder based on the original image, thereby enhancing the user's experience. The official site provides implementations in languages such as C, Swift, and TypeScript, in addition to a rich set of third-party libraries.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/193885464.png' style="max-width:80%; max-height=80%;"></img></p>

36、[esp32-weather-epd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lmarzen/esp32-weather-epd)：DIY E-Ink Weather Display. This is a weather display composed of an ESP32 microcontroller with WiFi support and a 7.5-inch E-Ink screen. It is capable of displaying real-time weather conditions and forecasts obtained through an API, as well as indoor temperature and humidity provided by sensors.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/467381275.jpg' style="max-width:80%; max-height=80%;"></img></p>

37、[localsend](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/localsend/localsend)：Open-Source Alternative to AirDrop. This project enables secure file and message sharing with nearby devices over a local network without the need for an internet connection or external server, and supports Windows, Linux, macOS, Android, and iOS devices.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/578822531.png' style="max-width:80%; max-height=80%;"></img></p>

38、[mactype](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/snowie2000/mactype)：Tool for Beautifying Windows Fonts. A Windows font beautification tool that can solve the problem of font blurring in Windows and achieve a font rendering effect similar to Apple's macOS system. It is simple to install and has an astonishing effect.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/33294473.jpg' style="max-width:80%; max-height=80%;"></img></p>

39、[raft.github.io](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/raft/raft.github.io)：A Website About Raft Consensus Algorithm. This website collects various materials related to Raft, including papers, courses, books, as well as open-source projects and visualization of Raft's operation, helping you thoroughly understand the Raft algorithm.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/13816796.gif' style="max-width:80%; max-height=80%;"></img></p>

### Book
40、[algorithmica](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/algorithmica-org/algorithmica)：Algorithms of Modern Hardware. This book from the non-profit educational organization Tinkoff Generation in Russia, which has trained about half of the Russian finalists in the Olympiad in Informatics, can provide both algorithm researchers and students with practical methods to enhance program performance.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/333536823.jpg' style="max-width:80%; max-height=80%;"></img></p>

41、[comprehensive-rust](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google/comprehensive-rust)：Comprehensive Four-Day Rust Course. This is a Rust course used by Google's Android team, covering everything from basic syntax to advanced topics like generics and error handling, including specific content for Android on the last day.

42、[scientific-visualization-book](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rougier/scientific-visualization-book)：Scientific Visualization with Python and Matplotlib. This is an open-source book about scientific visualization using Python and Matplotlib. The book is divided into four parts: the first part covers the basic principles of the Matplotlib library, the second part is dedicated to practical development, the third part deals with more advanced concepts such as 3D graphics, optimization, and animation, and the fourth part showcases a collection of demonstrations.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/83/202693400.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub82.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub84.md">『Next』</a>
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
        <a href="https://apifox.cn/a103hello">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/apifox.png" width="60px"><br>
          <sub>Apifox</sub><br>
          <sub>比 Postman 更强大</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
