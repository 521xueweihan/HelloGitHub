# 《HelloGitHub》第 71 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 目录

**Tips**：如果文中的图刷不出来，可以点击 [这里](https://hellogithub.com/periodical/volume/71/) 获取更好的阅读体验。

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
- [Rust 项目](#Rust-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [机器学习](#机器学习)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[h2o](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/h2o/h2o)：高性能 HTTP 服务器。相较于传统 Web 服务器，它充分利用了 HTTP/2 的资源加载优先级和服务器推送技术，所以在静态文件方面性能明显优于 Nginx 服务器

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/h2o.png' style="max-width:80%; max-height=80%;"></img></p>

2、[chibicc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rui314/chibicc)：迷你 C 编译器。虽然它只是一个玩具级的编译器，但是实现了大多数 C11 特性，而且能够成功编译几十万行的 C 语言项目，其中包括 Git、SQLite 等知名项目。而且它项目结构清晰、每次提交都是精心设计、代码容易理解，对编译器感兴趣的同学可以从[第一个提交](https://github.com/rui314/chibicc/commit/0522e2d77e3ab82d3b80a5be8dbbdc8d4180561c)开始学习

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
3、[CliWrap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tyrrrz/CliWrap)：执行外部命令的 C# 库。提供启动进程、输入/输出重定向、等待完成、管道等功能，支持 Windows、Linux、macOS 操作系统
```csharp
using CliWrap;

var result = await Cli.Wrap("path/to/exe")
    .WithArguments("--foo bar")
    .WithWorkingDirectory("work/dir/path")
    .ExecuteAsync();
    
// 输出包括：
// -- result.ExitCode        (int)
// -- result.StartTime       (开始时间)
// -- result.ExitTime        (结束时间)
// -- result.RunTime         (执行命令耗时)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/CliWrap.png' style="max-width:80%; max-height=80%;"></img></p>

4、[DreamScene2](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/he55/DreamScene2)：小巧的 Windows 动态桌面工具。适用于 Windows10/11 系统，支持视频、网页动画播放

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/DreamScene2.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
5、[vcpkg](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/vcpkg)：微软开源的 C/C++ 包管理工具。安装和管理 C/C++ 依赖的命令行工具，适用于 Windows、Linux 和 macOS 操作系统。[快速入门](https://github.com/microsoft/vcpkg/blob/master/README_zh_CN.md#%E5%85%A5%E9%97%A8)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/vcpkg.png' style="max-width:80%; max-height=80%;"></img></p>

6、[finalcut](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gansm/finalcut)：用于创建基于文本的用户界面的 C++ 库。它除了支持鼠标操作和同时处理多个文本窗，还提供了常见的对话框、按钮、复选框、单选按钮、输入行、列表框、状态栏等控件

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/finalcut.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
7、[magic](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/miniMAC/magic)：炫酷的 CSS3 动画库。[在线体验](https://www.minimamente.com/project/magic/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/magic.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
8、[nali](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zu1k/nali)：离线查询 IP 地理信息和 CDN 服务提供商的命令行工具
```
$ nali 1.2.3.4
1.2.3.4 [澳大利亚 APNIC Debogon-prefix网络]
```

9、[revive](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mgechev/revive)：快速且易扩展的 Go 代码检查工具。它比 golint 更快、更灵活，深受广大 Go 开发者的喜爱

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/revive.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[go-chart](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wcharczuk/go-chart)：Go 原生图表库。支持折线图、柱状图、饼图等
```go
package main
import (
	"os"
	"github.com/wcharczuk/go-chart/v2"
)

func main() {
	graph := chart.Chart{
		Series: []chart.Series{
			chart.ContinuousSeries{
				XValues: []float64{1.0, 2.0, 3.0, 4.0, 5.0},
				YValues: []float64{1.0, 2.0, 3.0, 4.0, 5.0},
			},
		},
	}
	f, _ := os.Create("output.png")
	defer f.Close()
	graph.Render(chart.PNG, f)
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/go-chart.png' style="max-width:80%; max-height=80%;"></img></p>

11、[filestash](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mickael-kerjean/filestash)：在线文件管理工具。在浏览器上管理 FTP、SFTP、Git、S3、MySQL、Dropbox 等服务中的文件和数据，支持编辑文件、图片管理、视频转码、Office 文档、全文搜索等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/filestash.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[vitess](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vitessio/vitess)：用于横向扩展 MySQL 数据库的集群系统。基于 Go 语言的并发特性，它能够轻松处理数千个连接。还可以根据配置好的规则，自动优化影响数据库性能的查询，运维方面支持自动处理主故障转移和备份等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/vitess.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
13、[thingsboard](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thingsboard/thingsboard)：完全开源的物联网 IoT 平台。它使用行业的标准物联网协议 MQTT、CoAP 和 HTTP 连接设备，支持数据收集、处理、可视化和设备管理等功能。通过该项目可快速实现物联网平台搭建，从而成为众多大型企业的首选，行业覆盖电信、智慧城市、环境监测等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/thingsboard.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[from-java-to-kotlin](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MindorksOpenSource/from-java-to-kotlin)：展示 Java 和 Kotlin 语法上差别的项目。让有 Java 基础的程序员可以快速上手 Kotlin，[中文](https://github.com/MindorksOpenSource/from-java-to-kotlin/blob/master/README-ZH.md)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/from-java-to-kotlin.png' style="max-width:80%; max-height=80%;"></img></p>

15、[graal](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/oracle/graal)：Oracle 开源的高性能跨语言虚拟机。用它启动的程序占用内存更低、启动时间更短，而且支持运行多种编程语言，比如 Python、Ruby、C/C++、Java 等。通过 Polyglot API 更是打破了不同语言之间的壁垒，实现多语言混合编程。目前部分功能还处于实验阶段，生产环境慎用。[官网](https://www.graalvm.org/)
```java
import org.graalvm.polyglot.*;

class Polyglot {
    public static void main(String[] args) {
        Context context = Context.newBuilder().allowIO(true).build();
        Value array = context.eval("python", "[1,2,42,4]");
        int result = array.getArrayElement(2).asInt();
        System.out.println(result);
    }
}

/**
 * 运行结果
 * 执行：javac Polyglot.java
 * 输出：42
 */
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/graal.png' style="max-width:80%; max-height=80%;"></img></p>

16、[glide](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bumptech/glide)：流畅快速的 Android 图片加载库。为了实现快速加载和展示图像，Glide 会自动缩减像素采样、缓存、积极重用减少垃圾回收。使用上一行代码就可以实现图片加载和展示，同时网络请求部分可灵活接入任何库
```java
Glide.with(fragment).load(url).into(imageView);
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/glide.png' style="max-width:80%; max-height=80%;"></img></p>

17、[jjwt](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jwtk/jjwt)：适用于 Java 和 Android 的 JWT（JSON Web Token）库
```java
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import java.security.Key;

Key key = Keys.secretKeyFor(SignatureAlgorithm.HS256);
String jws = Jwts.builder().setSubject("HelloGitHub").signWith(key).compact();
// 得到 JWS 字符串
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
18、[handle](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/antfu/handle)：汉字版 Wordle 游戏。[在线试玩](https://handle.antfu.me/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/handle.png' style="max-width:80%; max-height=80%;"></img></p>

19、[noclip.website](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/magcius/noclip.website)：电子游戏关卡的数字博物馆。该项目包含了很多游戏的场景模型，可在线自由浏览。[在线体验](https://noclip.website/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/noclip.png' style="max-width:80%; max-height=80%;"></img></p>

20、[ts-node](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TypeStrong/ts-node)：可直接在 Node.js 上执行 TypeScript 代码的库。通过 JIT 方式将 TypeScript 代码转换成 JavaScript，实现不需要预编译即可在 Node.js 上运行 TypeScript 代码

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/ts-node.png' style="max-width:80%; max-height=80%;"></img></p>

21、[summernote](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/summernote/summernote)：基于 jQuery 的编辑器库。可用来创建所见即所得（WYSIWYG）编辑器，支持 Bootstrap 3、4 和 5

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/summernote.png' style="max-width:80%; max-height=80%;"></img></p>

22、[yn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/purocean/yn)：面向程序员的本地 Markdown 笔记工具。一款适合程序员的笔记工具，拥有和其它工具不一样的体验
- 技术笔记：可直接在文档中运行代码块（默认支持 JS 代码，其它语言需配置）
- 制作辅助工具：可在文档中嵌入 HTML 组件来制作辅助工具
- 画图和图表：支持嵌入多种图形、思维导图、Plantunl、Drawio、Mermaid 、ECharts
- 工作日报：支持任务代办列表，使用“宏替换”功能可以方便地生成日报周报

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/yn.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Kotlin 项目
23、[RocketX](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/trycatchx/RocketX)：加速 Android APK 编译的插件。它会自动识别未改动模块并在编译流程中替换为 AAR，最后只编译改动过的模块，从而实现加速的效果
```
// app module 的 build.gradle 加入
apply plugin: 'com.rocketx'

// 在根目录的 build.gradle 加入
buildscript {
    dependencies {
        classpath 'io.github.trycatchx:rocketx:1.0.17'
    }
}
依赖 AS 插件 android studio setting->plugins-> marketplace 搜索 RocketX 安装
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/RocketXPlugin.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
24、[codefever](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/PGYER/codefever)：由蒲公英团队开源的代码托管平台。界面清爽后端采用 PHP 编写，支持 Docker 一键部署
- ❤️ 完整开源：毫无保留的完整开源，无任何编译或加密代码
- ⌨️ 代码对比：支持提交代码的不同版本支持高亮显示对比
- 🙅🏻‍♀️ 分支保护：分支保护功能让代码提交安全可控，代码 Review 更容易清晰
- 👥 多人协作：支持多人团队协作，并可以设置每个成员的角色和权限
- 🔌 Webhook：支持 Webhook 功能，可轻松和其它系统进行集成

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/codefever.png' style="max-width:80%; max-height=80%;"></img></p>

25、[PrestaShop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/PrestaShop/PrestaShop)：PHP 写的开源电商平台。功能齐全、部署方便、适配移动端。虽然前端支持高度自定义，但是现成的前端模版需要付费

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/PrestaShop.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
26、[Python](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TheAlgorithms/Python)：用 Python 实现所有算法。该项目是用 Python 语言实现各种算法的集合，主要用于教育和学习。包括搜索、排序、数据结构、机器学习、密码、神经网络等方面

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/Python.png' style="max-width:80%; max-height=80%;"></img></p>

27、[drf-yasg](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/axnsan12/drf-yasg)：为 Django Rest Framework 接口自动生成 Swagger 接口文档的库

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/drf-yasg.png' style="max-width:80%; max-height=80%;"></img></p>

28、[tstock](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Gbox4/tstock)：在命令行看股票走势的工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/tstock.png' style="max-width:80%; max-height=80%;"></img></p>

29、[python-mini-projects](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Python-World/python-mini-projects)：一个简单的 Python 迷你脚本集合。虽然代码简单但其中不乏实用的 Python 脚本，比如图片添加水印、批量下载图片、发送电子邮件、定时截屏等

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Rust 项目
30、[tui-rs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fdehau/tui-rs)：用来构建丰富的终端用户界面的库

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/tui-rs.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
31、[vapor](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vapor/vapor)：流行的 Swift 语言 Web 框架。核心框架基于非阻塞事件驱动库 SwiftNIO 构建，除此之外还提供了 ORM、模版引擎、用户身份验证等模块，可用来快速创建网站、接口等服务。[中文文档](https://cn.docs.vapor.codes)
```swift
import Vapor
 
let app = try Application(.detect())
defer { app.shutdown() }

app.get("hello") { req in
    return "Hello, world."
}
try app.run()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/vapor.png' style="max-width:80%; max-height=80%;"></img></p>

32、[DevUtils-app](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/DevUtilsApp/DevUtils-app)：macOS 上的开发者实用工具箱。单机应用无需联网，内含开发者开发时经常用到的 30 多种工具，比如：URL 解码、JSON 格式化、正则匹配、时间戳转化等，而且还会根据剪贴板的内容，自动推荐对应的处理工具，实用且高效

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/DevUtils-app.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
33、[svg-path-editor](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Yqnn/svg-path-editor)：在线 SVG 编辑器。[在线体验](https://yqnn.github.io/svg-path-editor/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/svg-path-editor.png' style="max-width:80%; max-height=80%;"></img></p>

34、[Arduino](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/arduino/Arduino)：开源电子平台，可用来制作嵌入式项目。Arduino 提供的电路板安装简单、价格便宜，而且电路图完全开源。官方还提供了配套的开发工具，加上交互式的开发模式使得上手变得极为简单。软硬件的完全开源让开发者社区十分活跃，为社区提供了丰富的教程、实战项目、三方资源。如果你想动手做个机器人，就从 Arduino 开始吧！[官网](https://www.arduino.cc/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/Arduino.png' style="max-width:80%; max-height=80%;"></img></p>

35、[macos-web](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/PuruVJ/macos-web)：在线体验 macOS 系统。该项目使用 Svelte 复刻了 macOS 操作系统的部分操作体验，虽然已实现的功能较少，但更新积极未来可期。[在线查看](https://macos-web.app/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/macos-web.png' style="max-width:80%; max-height=80%;"></img></p>

36、[resume](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/billryan/resume)：简历模板。不需要懂 LaTeX 语法就可以用，适合用来做一页纸简历

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/resume.png' style="max-width:80%; max-height=80%;"></img></p>

37、[teslamate](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/adriankumpf/teslamate)：自建特斯拉的日志平台。该项目可以将车主的特斯拉行驶数据收集、存储、展示，而且方便地支持 Docker 部署

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/teslamate.png' style="max-width:80%; max-height=80%;"></img></p>

38、[HowToCook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Anduin2017/HowToCook)：程序员做饭指南。一份极其详尽的菜谱，里面没有模糊的量词和看不懂的操作，菜品从主食到甜品应有尽有

39、[db-tutorial](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dunwu/db-tutorial)：一份关于数据库的教程。内容涵盖了 MySQL、Redis、ES、MongoDB 从入门到面试等多方面的知识

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/db-tutorial.png' style="max-width:80%; max-height=80%;"></img></p>

40、[pushdeer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/easychen/pushdeer)：无 APP 推送服务。该项目可以实现不安装庞大的应用，就可以收到自定义的及时推送、告警和通知。还可以选择自行搭建服务（免费）或使用已有的在线服务（收费），支持快应用、iOS、macOS、Android 等客户端

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/pushdeer.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
41、[ColossalAI](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hpcaitech/ColossalAI)：高效的分布式人工智能训练系统。它能帮助用户在提升人工智能训练效率的同时降低训练成本，从而适应快速迭代的算法和模型，将 AI 大模型以低成本便捷推广到更多应用场景

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/71/img/ColossalAI.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub70.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub72.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1xF2ECA89A2592'>云主机 4 元/月</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>推荐项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有各种回馈粉丝活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/71/'>这里</a> 获取更好的阅读体验。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
