# HelloGitHub Vol.87
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
1、[kilo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/antirez/kilo)：A Mini Text Editor Implemented with Less Than 1,000 Lines of Code. This project is a mini text editor written in C by the author of Redis, which supports syntax highlighting and search functions. It does not rely on third-party libraries, and the code is concise and elegant, with less than 1,000 lines after removing comments and blank lines, and it is contained in a single file, making the source code very refreshing to read.

2、[Logan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Meituan-Dianping/Logan)：Unified Log Service for Terminals. Open-sourced by Meituan's tech team, this is a complete front-end logging system that includes client SDK, log processing, and management platform. It is suitable for real-time log collection in terminal scenarios such as mobile APPs, Web, mini-programs, and IoT.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/150354367.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[winsw](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/winsw/winsw)：Tool for Wrapping Executable Files as Windows Service. This project allows Windows applications that originally do not support startup at boot to be set as automatically starting at boot, with the entire process only requiring two commands.

### C++
4、[geometrize](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Tw1ddle/geometrize)：Tool for Redrawing Images with Geometric Shapes. This project allows images to be redrawn using geometric shapes such as circles, triangles, and rectangles, and the results can be exported in formats like SVG, PNG, JPG, and GIF.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/78338311.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[primihub](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/primihub/primihub)：Ready-to-Use Open Source Privacy Computing Platform. Typically when we query data, the data provider will certainly know our query conditions, otherwise, the results cannot be returned. However, in some cases, the querying party does not want others to know the query conditions, yet still wants to obtain results. This may sound like an impossible task to complete. But don't worry, there's a specialized technical field called privacy computing. If you don't understand it, this open source privacy computing platform, PrimiHub, allows you to experience the charm of privacy computing without a background in privacy computing technology, enabling easy achievement of 'data is usable but not visible'!
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

6、[redpanda](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/redpanda-data/redpanda)：A Streaming Data Platform Fully Compatible with the Kafka API. This project can be regarded as a rewrite of Kafka in C++, designed to be lighter, faster, and more cost-effective. It is simple to deploy and user-friendly, with no external dependencies such as JVM or ZooKeeper.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/309512982.png' style="max-width:80%; max-height=80%;"></img></p>

7、[shotcut](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mltframework/shotcut)：A Powerful Free Video Editing Software. Although this software is free, it doesn't lag behind paid video editing tools in terms of functionality, and it can be used as an open-source alternative to Premiere. It features a Chinese interface and intuitive operation, supports hundreds of audio and video formats, native material editing, and multiple timeline features, and is applicable to Windows, Linux, and macOS systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/4118776.png' style="max-width:80%; max-height=80%;"></img></p>

8、[sqlitebrowser](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sqlitebrowser/sqlitebrowser)：SQLite Visualization Management Tool. This is a practical desktop management tool for SQLite databases that supports the creation and editing of SQLite database files. It allows users to create, define, modify, and delete tables and indexes through a graphical interface, as well as perform operations such as executing SQL and exporting data.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/19416551.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
9、[gotenberg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gotenberg/gotenberg)：Docker-based PDF File Generation Service. It supports launching a service through Docker that interacts with Chromium and LibreOffice through an API. You can easily convert documents in formats such as web pages, HTML, Markdown, Word, Excel, etc., into PDF files by calling the interface.
```
curl \
--request POST 'https://demo.gotenberg.dev/forms/chromium/convert/url' \
--form 'url="https://sparksuite.github.io/simple-html-invoice-template/"' \
-o my.pdf
```

10、[httprouter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/julienschmidt/httprouter)：High-Performance HTTP Request Router in Go Language. This project features a streamlined structure with only three core files. It implements efficient routing through the use of a Radix tree data structure. Notably, the well-known Gin framework also leverages it.
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

11、[slides](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/maaslalani/slides)：A Command-Line Presentation Tool. This command-line tool allows you to easily create and present slides in the terminal. It comes ready-to-use and supports Markdown syntax.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/364729022.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[sourcegraph-public-snapshot](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sourcegraph/sourcegraph-public-snapshot)：A Powerful Code Search Platform. This project enables semantic indexing and analysis of code repositories, supports regular expression search, provides auto-completion when inputting search criteria, and has IDE-like functionality for jumping to definitions and references. It can be used to build an internal code search platform for a company, assisting programmers with cross-project code search, code review, and code tracking.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/41288708.png' style="max-width:80%; max-height=80%;"></img></p>

13、[tinygo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tinygo-org/tinygo)：Go Compiler Built for 'Small-scale' Situations. This is a lightweight Go compiler based on LLVM that can compile Go code into executables for scenarios such as development boards, the Internet of Things, WebAssembly, and more.

### Java
14、[FXGL](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AlmasB/FXGL)：Your First Java Game Development Framework. This project is a 2D game development engine based on JavaFX. It requires no installation and features a simple API, enabling you to easily package your developed game into an executable JAR file. Everything has been designed to make you fall in love with game development.
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

15、[SurveyKing](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/javahuang/SurveyKing)：Powerful Survey Questionnaire System. This is a Java-based survey and examination system that supports more than 20 types of questions, import questionnaires from Excel, whitelist responses, public inquiries, data export, and more features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/403634780.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
16、[AFFiNE](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/toeverything/AFFiNE)：A Collaborative Knowledge Base System Similar to Notion. It features a refreshing and clean interface with support for offline use. It integrates note-taking, knowledge base, and data table functionalities, and these elements can be combined flexibly.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/519859998.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[giscus](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/giscus/giscus)：Comment System Based on GitHub Discussions. This project is a comment system implemented using the GitHub Discussions API. It is free, ad-free, and database-free, supporting features like custom themes and multi-language.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/351958053.png' style="max-width:80%; max-height=80%;"></img></p>

18、[NextChat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ChatGPTNextWeb/NextChat)：Deploy Your Personal ChatGPT Web Application for Free. This project offers not only a more user-friendly chat interface for ChatGPT, but also supports one-click deployment to Vercel. All you need to do is provide an OpenAI API Key to have your own private ChatGPT service for free.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/612344730.png' style="max-width:80%; max-height=80%;"></img></p>

19、[Painter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/manycore-maas/Painter)：Mini Program Image Library Generator. This project allows developers of mini programs to create images through JSON, supporting the drawing of text, images, QR codes, various layouts, custom fonts, rounded corners, and more.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/139574940.png' style="max-width:80%; max-height=80%;"></img></p>

20、[patch-package](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ds300/patch-package)：A Library for Patching npm Dependencies. When there is a bug in a third-party library that your project depends on, and you need to manually add a piece of code to fix it, this library makes it easy to apply the patch, and supports npm, yarn, pnpm, and more.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/90669846.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
21、[legado](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gedoor/legado)：Customizable Novel Reader. This lightweight Android reader is ad-free, features a clean interface, and supports custom book sources, local import of novels, multiple page-turning modes, and filtering. Please note, it only functions as a reader and does not provide novel content itself. Importing book sources is required upon initial installation.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/187961907.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
22、[Auto_Bangumi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/EstrellaXD/Auto_Bangumi)：Fully Automated Anime Subscription and Download Tool. This project is a tool written in Python for automatically subscribing to and downloading animations. Users simply need to subscribe to anime on Mikan Project and make a few configuration adjustments to comfortably follow their favorite series.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/488069222.png' style="max-width:80%; max-height=80%;"></img></p>

23、[openedx-platform](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/openedx/openedx-platform)：Open Source MOOC Platform Built with Django. This project is a Massive Open Online Course (MOOC) platform jointly open-sourced by MIT and Harvard University. It provides content management and learning management services. The platform supports online lectures, course creation, previewing before publishing, content libraries, student feedback, exams, and other functions. Although it is rich in features, the interface is quite rudimentary.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/10391073.png' style="max-width:80%; max-height=80%;"></img></p>

24、[PyQt-Fluent-Widgets](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zhiyiYo/PyQt-Fluent-Widgets)：Fluent Design Style PyQt Component Library. A Fluent Design style component library for PyQt/PySide, which includes various aesthetically pleasing and practical components, supporting the switching of light and dark themes as well as customizable theme colors.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/390782193.jpg' style="max-width:80%; max-height=80%;"></img></p>

25、[stitching](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/OpenStitching/stitching)：Powerful Python Library for Image Stitching. This is a Python library developed based on the stitching module of OpenCV for quickly stitching images, supporting use in Python scripts and command-line modes.
```python
import stitching

stitcher = stitching.Stitcher()
# 多个文件
panorama = stitcher.stitch(["img1.jpg", "img2.jpg", "img3.jpg"])
# 通配符
panorama = stitcher.stitch(["img?.jpg"])
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/489887699.png' style="max-width:80%; max-height=80%;"></img></p>

26、[sympy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sympy/sympy)：Python Library for Symbolic Computation. This is a comprehensive and pure Python-written computer algebra system (CAS), suitable for solving complex mathematical problems. It supports functions such as equation solving, discrete mathematics, calculus, logical computation, geometry, probability, and statistics.
```
>>> from sympy import Symbol, cos
>>> x = Symbol('x')
>>> e = 1/cos(x)
>>> print(e.series(x, 0, 10))
1 + x**2/2 + 5*x**4/24 + 61*x**6/720 + 277*x**8/8064 + O(x**10)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/640534.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust
27、[hexyl](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sharkdp/hexyl)：Command Line Hex Viewer. This is a command line hex viewer written in Rust, which is simple and pure with a very comfortable color output effect.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/156294298.png' style="max-width:80%; max-height=80%;"></img></p>

28、[ruffle](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ruffle-rs/ruffle)：Open-Source Flash Player Simulator. This is an Adobe Flash Player simulator developed in Rust, capable of being embedded on websites through WebAssembly, used with browser plugins, or played locally via the command line for Flash files. It leverages Rust and WebAssembly technology to address the various memory safety issues inherent in the original Flash Player. Although Flash has become a thing of the past, it still contains many enjoyable animations and games that should not be forgotten.Shared by [@浮生若夢](https://hellogithub.com/en/user/hKmH64UjOdwgCEi)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/183483988.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift
29、[LocationSimulator](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Schlaubischlump/LocationSimulator)：Location Simulator for iOS Devices. This is a macOS application that can easily modify the location information of iOS and iPadOS devices. There is no need to jailbreak or install apps on the mobile device. Just connect the device to the computer via USB or WiFi, and you can easily complete location modification.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/205137861.png' style="max-width:80%; max-height=80%;"></img></p>

30、[SwiftUI-Cheat-Sheet](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SimpleBoilerplates/SwiftUI-Cheat-Sheet)：SwiftUI Cheat Sheet. This project is a SwiftUI 2.0 cheat sheet that includes code snippets ready for copy-paste and screenshots of the running effects.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/190864373.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
31、[AI-For-Beginners](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/AI-For-Beginners)：Microsoft's Open-Sourced Beginner's Guide to AI. This is a completely free AI course for those with no prior knowledge, consisting of 24 lessons over 12 weeks. You will learn about the history of AI, basic concepts, mainstream frameworks, as well as knowledge in the fields of Computer Vision (CV) and Natural Language Processing (NLP).

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/344190478.png' style="max-width:80%; max-height=80%;"></img></p>

32、[DragGAN](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/XingangPan/DragGAN)：Drag-to-Edit GAN Completes P-Graph Editing. This is the official source code of DragGAN, which supports image editing through mouse dragging. Anyone can easily modify the posture, expression, shape, layout, and more of objects in the image by precisely controlling the direction of pixels. For example, it enables a dog that was originally standing in the picture to sit down.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/642323624.gif' style="max-width:80%; max-height=80%;"></img></p>

33、[mediapipe](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google-ai-edge/mediapipe)：Google’s Open-Source Cross-Platform Machine Learning Framework. This is a machine learning toolkit that can be effortlessly deployed to mobile devices, the web, PCs, and IoT devices. It includes models for object detection, image classification, face recognition, gesture recognition, text classification, language detection, and audio classification.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/191820100.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
34、[awesome-macos-screensavers](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/agarrharr/awesome-macos-screensavers)：Amazing macOS Screensavers Collection. Here you will find a variety of macOS screensavers with different styles, patterns, and fun elements, sure to have one that suits your taste.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/30559599.png' style="max-width:80%; max-height=80%;"></img></p>

35、[personal-security-checklist](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Lissy93/personal-security-checklist)：A Checklist to Protect Your Digital Security and Privacy. This is a list that teaches you how to safeguard your personal information, including aspects such as passwords, web browsing, emails, social networks, mobile phones, and computers.

36、[radian](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/randy3k/radian)：Advanced R Language Console. This project serves as an alternative to the default R console, supporting features like auto-completion, multi-line editing, and syntax highlighting, making it more convenient and user-friendly.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/86867223.png' style="max-width:80%; max-height=80%;"></img></p>

37、[web-vitals](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GoogleChrome/web-vitals)：Google's Open Source Core Web Vitals. These metrics can help webmasters improve the user experience of their websites, encompassing three aspects: LCP (Loading Performance), FID (Interactivity), and CLS (Visual Stability).

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/87/249512698.png' style="max-width:80%; max-height=80%;"></img></p>

38、[XiangShan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/OpenXiangShan/XiangShan)：An Open-Source RISC-V Processor Made in China. The 'XiangShan' is an open-source RISC-V processor project initiated by the Institute of Computing Technology, Chinese Academy of Sciences.

### Book
39、[Clean-Code-Notes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/JuanCrg90/Clean-Code-Notes)：A Book on How to Write Clean Code. This book begins with an explanation of what constitutes Clean Code and step-by-step teaches you how to write code that is concise, easy to understand, and maintainable, to help you develop good coding habits.



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub86.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub88.md">『Next』</a>
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
