# 《HelloGitHub》第 87 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/87) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[kilo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/antirez/kilo)：不到 1 千行代码实现的迷你文本编辑器。该项目是 Redis 作者用 C 语言写的迷你文本编辑器，支持语法高亮和搜索等功能。它不依赖第三方库、代码简洁优雅，去掉注释和空行后不到 1000 行，且只有一个文件，源码阅读起来十分清爽。

2、[Logan](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Meituan-Dianping/Logan)：面向终端的统一日志服务。由美团技术团队开源的一整套前端日志系统，包含客户端 SDK、日志处理和管理平台。它适用于移动端 APP、Web、小程序、IoT 等终端场景下的实时日志收集。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/150354367.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[winsw](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/winsw/winsw)：将可执行文件包装成 Windows 服务的工具。该项目可以将原本不支持开机启动的 Windows 应用，设置成开机自动启动，整个过程只需要两条命令。

### C++ 项目
4、[geometrize](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tw1ddle/geometrize)：将图像用几何图形重绘的工具。该项目可以用圆形、三角形、矩形等几何图形重新绘制图像，并将结果导出为 SVG、PNG、JPG、GIF 等格式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/78338311.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[primihub](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/primihub/primihub)：由密码学专家团队打造的开源隐私计算平台。随着《数据安全法》和《个人信息保护法》的相继颁布，隐私计算技术在近两年迎来了前所未有的热度。该项目是由密码学专家团队打造的隐私计算平台，它开箱即用、安全可靠，支持隐匿查询、隐私求交、联合统计、数据资源管理等功能，实现了“数据可用不可见”，为数据安全流通保驾护航。
```
# 第一步：下载
git clone https://github.com/primihub/primihub.git
# 第二步：启动容器
cd primihub && docker-compose up -d
# 第三步：进入容器
docker exec -it primihub-node0 bash
# 第四步：执行隐私求交计算
./primihub-cli --task_config_file="example/psi_ecdh_task_conf.json"
I20230616 13:40:10.683375    28 cli.cc:524] all node has finished
I20230616 13:40:10.683745    28 cli.cc:598] SubmitTask time cost(ms): 1419
# 查看结果
cat data/result/psi_result.csv
"intersection_row"
X3
...
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/469566735.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[redpanda](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/redpanda-data/redpanda)：与 Kafka API 完全兼容的流数据平台。这个项目可以看作是用 C++ 重新编写的 Kafka，它更轻、更快、更省钱，部署简单使用方便，完全不受 JVM、ZooKeeper 等外部依赖的影响。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/309512982.png' style="max-width:80%; max-height=80%;"></img></p>

7、[shotcut](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mltframework/shotcut)：一款功能强大的免费视频剪辑软件。这款软件虽然免费但在功能上完全不输收费的视频剪辑工具，可作为 Pr 的开源替代品。它拥有中文和直观的操作界面，支持数百种音频和视频格式、素材原生编辑、多时间线等功能，适用于 Windows、Linux、macOS 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/4118776.png' style="max-width:80%; max-height=80%;"></img></p>

8、[sqlitebrowser](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sqlitebrowser/sqlitebrowser)：SQLite 可视化管理工具。这是一款实用的 SQLite 数据库桌面管理工具，它支持创建和编辑 SQLite 数据库文件，可通过图形化界面创建、定义、修改、删除表和索引，以及执行 SQL 和导出数据等操作。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/19416551.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
9、[gotenberg](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gotenberg/gotenberg)：基于 Docker 的生成 PDF 文件服务。它支持通过 Docker 启动一个服务，该服务可以通过 API 与 Chromium 和 LibreOffice 进行交互。让你可以通过调用接口，轻松地将网页、HTML、Markdown、Word、Excel 等格式的文档转换为 PDF 文件。
```
curl \
--request POST 'https://demo.gotenberg.dev/forms/chromium/convert/url' \
--form 'url="https://sparksuite.github.io/simple-html-invoice-template/"' \
-o my.pdf
```

10、[httprouter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/julienschmidt/httprouter)：Go 语言的高性能 HTTP 请求路由器。该项目结构简洁，核心代码仅三个文件。它通过 Radix tree 数据结构，实现了高效的路由处理。值得一提的是，著名的 Gin 框架也使用了它。
```go
package main

import (
    "fmt"
    "net/http"
    "log"

    "github.com/julienschmidt/httprouter"
)

func Index(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "Welcome!\n")
}

func Hello(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
    fmt.Fprintf(w, "hello, %s!\n", ps.ByName("name"))
}

func main() {
    router := httprouter.New()
    router.GET("/", Index)
    router.GET("/hello/:name", Hello)

    log.Fatal(http.ListenAndServe(":8080", router))
}
```

11、[slides](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/maaslalani/slides)：一款命令行演示工具。这款命令行工具可以让你在终端中轻松创建和演示幻灯片，它开箱即用、支持 Markdown 语法。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/364729022.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[sourcegraph](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sourcegraph/sourcegraph)：一款强大的代码搜索平台。该项目能够对代码库进行语义索引和分析，支持正则表达式搜索、输入搜索条件时的自动补全、类似 IDE 的跳转到定义和引用。它可以用于构建公司内部的代码搜索平台，帮助程序员完成跨项目的代码查找、代码审查、代码追踪等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/41288708.png' style="max-width:80%; max-height=80%;"></img></p>

13、[tinygo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tinygo-org/tinygo)：专为“小场面”而生的 Go 编译器。这是一个基于 LLVM 的小型 Go 编译器，它能够将 Go 代码编译成可运行在开发板、物联网、WebAssembly 等场景的程序。

### Java 项目
14、[FXGL](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AlmasB/FXGL)：你的第一款 Java 游戏开发框架。该项目是基于 JavaFX 的 2D 游戏开发引擎，它无需安装、API 简单，能够轻松地将开发的游戏打包成一个可执行的 jar 包，一切的一切都是为了让你喜欢上开发游戏。
```java
public class BasicGameApp extends GameApplication {

    @Override
    protected void initSettings(GameSettings settings) {
        settings.setWidth(800);
        settings.setHeight(600);
        settings.setTitle("Basic Game App");
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/32761091.jpg' style="max-width:80%; max-height=80%;"></img></p>

15、[SurveyKing](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/javahuang/SurveyKing)：功能强大的调查问卷系统。这是一款 Java 写的问卷调查和考试系统，支持 20 多种题型、Excel 导入问卷、白名单答卷、公开查询、数据导出等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/403634780.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
16、[AFFiNE](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/toeverything/AFFiNE)：类似 Notion 的协同知识库系统。它拥有清爽、简洁的界面，支持离线使用。集成了笔记、知识库、数据表格等功能，同时这些内容之间还可以灵活组合。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/519859998.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[ChatGPT-Next-Web](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Yidadaa/ChatGPT-Next-Web)：免费部署私人 ChatGPT 网页应用。该项目不仅提供了更加人性化的 ChatGPT 聊天界面，还支持一键部署到 Vercel。你只需要提供 OpenAI API Key，就能免费拥有私人 ChatGPT 服务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/612344730.png' style="max-width:80%; max-height=80%;"></img></p>

18、[giscus](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/giscus/giscus)：基于 GitHub Discussions 的评论系统。该项目是基于 GitHub Discussions API 实现的评论系统，它免费、无广告、无需数据库，支持自定义主题、多语言等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/351958053.png' style="max-width:80%; max-height=80%;"></img></p>

19、[Painter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Kujiale-Mobile/Painter)：小程序生成图片库。该项目可以让小程序开发者通过 JSON 的方式绘制图片，支持绘制文本、图片、二维码、多种布局、自定义字体、圆角等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/139574940.png' style="max-width:80%; max-height=80%;"></img></p>

20、[patch-package](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ds300/patch-package)：给 npm 依赖项打补丁的库。如果项目依赖的第三方库有个 bug，需要手动添加一段代码才能解决，这个时候用它打个补丁就轻松搞定，支持 npm、yarn、pnpm 等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/90669846.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
21、[legado](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gedoor/legado)：一款免费的安卓小说阅读器。这款阅读器体积小、无广告、界面简洁，支持自定义书源、本地导入小说、多种翻页模式、替换净化等功能。需要注意的是，它只是一个阅读器，不提供小说内容，初次安装后需要自行导入书源。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/187961907.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
22、[Auto_Bangumi](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/EstrellaXD/Auto_Bangumi)：全自动追番工具。该项目是 Python 写的自动订阅更新和下载动画的工具，用户只需在 Mikan Project 上订阅番剧，然后简单配置一下就可以安心追番了。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/488069222.png' style="max-width:80%; max-height=80%;"></img></p>

23、[edx-platform](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/openedx/edx-platform)：Django 写的开源慕课平台。该项目是由麻省理工和哈佛大学联合开源的大规模开放式在线课堂(MOOC)平台，它提供了内容管理和学习管理服务。该平台支持在线讲课、创建课程、发布前预览、内容库、学生反馈、考试等功能。虽然它功能丰富，但界面十分简陋。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/10391073.png' style="max-width:80%; max-height=80%;"></img></p>

24、[PyQt-Fluent-Widgets](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zhiyiYo/PyQt-Fluent-Widgets)：Fluent Design 风格的 PyQt 组件库。基于 PyQt/PySide 的 Fluent Design 风格组件库，内含多种美观、实用的组件，支持亮暗主题切换和自定义主题色。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/390782193.jpg' style="max-width:80%; max-height=80%;"></img></p>

25、[stitching](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/OpenStitching/stitching)：强大的图片拼接 Python 库。这是一个基于 OpenCV 的拼接模块开发的用于快速拼接图片的 Python 库，支持在 Python 脚本中使用和命令行方式。
```python
import stitching

stitcher = stitching.Stitcher()
# 多个文件
panorama = stitcher.stitch(["img1.jpg", "img2.jpg", "img3.jpg"])
# 通配符
panorama = stitcher.stitch(["img?.jpg"])
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/489887699.png' style="max-width:80%; max-height=80%;"></img></p>

26、[sympy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sympy/sympy)：进行符号运算的 Python 库。这是一个功能齐全、纯 Python 写的计算机代数系统(CAS)，可用于计算复杂的数学问题。它支持解方程、离散数学、微积分、逻辑计算、几何、概率与统计等功能。
```
>>> from sympy import Symbol, cos
>>> x = Symbol('x')
>>> e = 1/cos(x)
>>> print(e.series(x, 0, 10))
1 + x**2/2 + 5*x**4/24 + 61*x**6/720 + 277*x**8/8064 + O(x**10)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/640534.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
27、[hexyl](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sharkdp/hexyl)：命令行十六进制查看器。这是一款 Rust 写的命令行十六进制查看器，它简单纯粹、彩色输出效果十分舒服。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/156294298.png' style="max-width:80%; max-height=80%;"></img></p>

28、[ruffle](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ruffle-rs/ruffle)：Rust 写的 Flash Player 替代品。这是一个用 Rust 语言开发的 Adobe Flash Player 模拟器，它不仅可以通过 WebAssembly 嵌入网站，还支持浏览器插件的方式使用以及在本地通过命令行播放 Flash 文件。来自 [@浮生若夢](https://hellogithub.com/user/hKmH64UjOdwgCEi) 的分享

### Swift 项目
29、[LocationSimulator](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Schlaubischlump/LocationSimulator)：iOS 设备的定位模拟器。这是一个能够轻松修改 iOS 和 iPadOS 位置信息的 macOS 应用，使用时手机端无需越狱和安装应用，只需通过 USB 或 WiFi 将设备连接上电脑，即可轻松完成位置修改。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/205137861.png' style="max-width:80%; max-height=80%;"></img></p>

30、[SwiftUI-Cheat-Sheet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SimpleBoilerplates/SwiftUI-Cheat-Sheet)：SwiftUI 小抄。该项目是一份 SwiftUI 2.0 速查表，内容包含复制即用的代码片段和运行效果截图。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/190864373.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
31、[awesome-macos-screensavers](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/agarrharr/awesome-macos-screensavers)：令人惊艳的 macOS 屏保集合。这里有不同风格、样式、趣味性十足的 macOS 屏保，相信总有一款适合你。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/30559599.png' style="max-width:80%; max-height=80%;"></img></p>

32、[BlackHole](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Sangwan5688/BlackHole)：一款高颜值的音乐播放器应用。该项目是用 Flutter 写的高颜值、无广告、免费音乐播放器，拥有歌词、专辑、艺术家、播放列表、定时关闭等功能，支持 Android、iOS、macOS 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/338028961.png' style="max-width:80%; max-height=80%;"></img></p>

33、[personal-security-checklist](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Lissy93/personal-security-checklist)：保护你的数字安全和隐私的清单。这是一份教你如何保护个人信息的列表，包括密码、浏览网页、电子邮件、社交网络、手机、电脑等方面。

34、[radian](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/randy3k/radian)：更先进的 R 语言控制台。该项目可作为 R 语言自带控制台的替代品，它支持自动补全、多行编辑和语法高亮，更方便、更好用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/86867223.png' style="max-width:80%; max-height=80%;"></img></p>

35、[web-vitals](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/GoogleChrome/web-vitals)：Google 开源的核心页面指标。该指标可以帮助站长提升网站的用户体验，它分为 LCP(加载性能)、FID(交互性)、CLS(视觉稳定性) 三个方面。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/249512698.png' style="max-width:80%; max-height=80%;"></img></p>

36、[XiangShan](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/OpenXiangShan/XiangShan)：一款国产的开源 RISC-V 处理器。“香山”是由中国科学院计算技术研究所牵头发起的开源 RISC-V 处理器项目。

### 开源书籍
37、[Clean-Code-Notes](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/JuanCrg90/Clean-Code-Notes)：一本关于如何写出 Clean Code 的书。该书从什么是 Clean Code 讲起，一步步教你如何写出简洁、容易理解和维护的代码，帮助你养成良好的编码习惯。

### 机器学习
38、[AI-For-Beginners](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/AI-For-Beginners)：微软开源的入门级人工智能教程。这是一份完全免费、面向零基础人群的 AI 课程，为期 12 周共计 24 节课。你将学习到关于 AI 的历史、基本知识、主流框架、CV 和 NLP 等知识。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/344190478.png' style="max-width:80%; max-height=80%;"></img></p>

39、[DragGAN](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/XingangPan/DragGAN)：拖动 GAN 完成 P 图。这是 DragGAN 的官方源码，它支持通过鼠标拖拽的方式对图像进行编辑。任何人都可以通过精确控制像素去向，轻松修改图像中物体的姿态、表情、形状、布局等。例如，可以让图片上原本站着的小狗坐下。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/642323624.gif' style="max-width:80%; max-height=80%;"></img></p>

40、[mediapipe](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/mediapipe)：谷歌开源的跨平台机器学习框架。它是一个能够轻松部署到移动端、Web、PC 和物联网设备的机器学习工具库，包含了物体检测、图像分类、人脸识别、手势识别、文本分类、语言检测、音频分类等模型。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/191820100.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub86.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub88.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/87'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
