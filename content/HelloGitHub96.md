# 《HelloGitHub》第 96 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/96) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[cosmopolitan](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jart/cosmopolitan)：让 C 成为构建一次，可随处运行的语言。这个工具可以将 C 语言编写的程序，编译成可无缝运行在多种操作系统上的可执行文件。它采用自包含式二进制文件的设计，能够将程序所有依赖打包进可执行文件中，实现真正的跨平台运行，支持 Windows、macOS 和 Linux 等主流操作系统。
```
// 编译
cosmocc -o hello hello.c
// 运行
./hello
// 调试
./hello --strace
./hello --ftrace
```

2、[linenoise](https://hellogithub.com/periodical/statistics/click?target=https://github.com/antirez/linenoise)：一个 C 语言写的命令行编辑库。该项目是 Redis 作者用 C 语言实现的用于提升命令行交互体验的单文件库，整体代码大约 800 多行，轻量且易上手，提供了单/多行编辑模式、左右移动光标、上下回滚输入历史记录、命令补全等功能。来自 [@9Ajiang](https://hellogithub.com/user/SMTnPZI9BxYvVXr) 的分享

3、[xxHash](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Cyan4973/xxHash)：超快的非加密哈希算法。哈希算法是一种将任意长度的输入数据转换为固定长度输出哈希值的算法。xxHash 是一种专为快速计算大型数据集哈希值而设计的非加密哈希算法。它具有出色的速度、零依赖和优秀的分布特性，支持流式计算模式和多种编程语言实现，适用于对计算性能要求很高的数据完整性检查、数据流分析、键值对检索等场景。
```c
#include <string.h>
#include "xxhash.h"
 
// Example for a function which hashes a null terminated string with XXH32().
XXH32_hash_t hash_string(const char* string, XXH32_hash_t seed)
{
    // NULL pointers are only valid if the length is zero
    size_t length = (string == NULL) ? 0 : strlen(string);
    return XXH32(string, length, seed);
}
```

### C# 项目
4、[reverse-proxy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/reverse-proxy)：微软开源的反向代理工具包。该项目是微软团队用 C# 开发的一个提供核心代理功能的工具库，可作为库和项目模板，用于创建反向代理服务器的项目，内含简单的反向代理服务器示例项目。

5、[Snap.Hutao](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DGP-Studio/Snap.Hutao)：实用的多功能原神工具箱。这是一款专为 Windows 平台设计的原神工具箱，支持多账号切换、自定义帧率上限、祈愿记录、成就管理、签到奖励、查询角色资料、养成计算器等功能。它不对游戏客户端进行任何破坏性修改，只为改善原神桌面端玩家的游戏体验。来自 [@Masterain](https://hellogithub.com/user/0xVspWlUv3kdeX5) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/482734649.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
6、[ada](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ada-url/ada)：快如闪电的 URL 解析利器。该项目是用 C++ 写的符合 WHATWG 规范的 URL 解析器，解析速度是 curl 的数倍，目前已成为 Node.js 默认 URL 解析器（18.16.0 及以上），注意仅仅是 URL 地址解析不是请求。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/579485798.png' style="max-width:80%; max-height=80%;"></img></p>

7、[keepassxc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/keepassxreboot/keepassxc)：一款开源、安全、跨平台的密码管理器。该项目是采用 C++ 开发的免费、离线、无广告的密码管理工具，它提供了简洁直观的用户界面，可轻松管理各种应用/网站的账号密码，支持多平台、浏览器插件、自动填充、密码生成等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/52729242.png' style="max-width:80%; max-height=80%;"></img></p>

8、[TranslucentTB](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TranslucentTB/TranslucentTB)：自定义 Windows 任务栏透明度的小工具。该项目是采用 C++ 开发的用于调整 Windows 任务栏透明度的工具，它体积小、免费、简单易用，支持 5 种任务栏状态、6 种动态模式、Windows 10/11 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/78483432.png' style="max-width:80%; max-height=80%;"></img></p>

9、[tugraph-db](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TuGraph-family/tugraph-db)：支付宝背后的分布式图数据库。该项目是由蚂蚁集团和清华大学共同研发的高性能分布式图数据库，支持事务处理、TB 级大容量、低延迟查找和快速图分析等功能。

### CSS 项目
10、[easings.net](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ai/easings.net)：CSS 缓动函数速查表。缓动函数（Easing Functions）是一种用于控制 CSS 动画速度的函数，该项目提供了一系列优雅的缓动函数示例代码和效果展示。
```css
.block {
	transition: transform 0.6s cubic-bezier(0.7, 0, 0.84, 0);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/3796591.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
11、[codapi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nalgeon/codapi)：在线运行代码片段的 Go 服务。该项目提供了一个 API 服务，可以在线运行 Python、TypeScript、C、Go 等 30 种编程语言的代码片段，可用于在文档和教程中展示交互式的代码示例。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/723189658.png' style="max-width:80%; max-height=80%;"></img></p>

12、[focalboard](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mattermost-community/focalboard)：开源的项目管理和团队协作工具。这是一款开源、多语言、自托管的项目管理工具，兼容了 Trello 和 Notion 的特点。它支持看板、表格和日历等视图管理任务，并提供评论同步、文件共享、用户权限等功能。该工具还提供了适用于 Windows、macOS、Linux 系统的客户端。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/301793434.jpg' style="max-width:80%; max-height=80%;"></img></p>

13、[go-pretty](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jedib0t/go-pretty)：美化控制台输出的 Go 库。这是一个用于美化表格、列表、进度条、文本等控制台输出的库，你可以用它输出精美的表格、多层级的列表以及多任务进度条等内容。

14、[gopeed](https://hellogithub.com/periodical/statistics/click?target=https://github.com/GopeedLab/gopeed)：一款由 Go+Flutter 开发的高速下载器。这款下载工具后端用的是 Go 语言，支持 HTTP、BitTorrent、Magnet 等多种协议，并使用协程实现高速并发下载。前端部分采用 Flutter 开发，提供了适用于 Windows、macOS、Linux、Android、iOS 和 Web 等全平台的客户端。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/182502850.png' style="max-width:80%; max-height=80%;"></img></p>

15、[teleport](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gravitational/teleport)：一款 Go 写的企业级开源堡垒机。这是一个专为基础设施提供连接、身份验证、访问控制和安全审计的平台，它支持对内网的 Linux 服务器、Kubernetes 集群、Web 应用、PostgreSQL 和 MySQL 数据库的安全访问。该平台采用自动下发证书的方式进行认证，无需在目标机器上管理密码和 SSH Key。此外，用户可以方便地使用 ssh、mysql、kubectl 等远程连接工具，轻松接入受管理的资源。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/31558937.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
16、[javers](https://hellogithub.com/periodical/statistics/click?target=https://github.com/javers/javers)：用于追踪数据历史记录和审计的 Java 库。该项目是将版本管理的想法应用于数据（Java 对象）变更管理的 Java 库，它支持查看复杂的对象结构差异，保留修改数据的历史记录，并能追踪对象变化。来自 [@猎隼丶止戈reNo7](https://hellogithub.com/user/Ew59HqRWjPe0zZO) 的分享

17、[source-code-hunter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/doocs/source-code-hunter)：Spring 全家桶源码解读。该项目提供了一系列互联网主流框架和中间件的源码讲解，包括 Spring 全家桶、Mybatis、Netty、Dubbo 等框架。

### JavaScript 项目
18、[aspoem](https://hellogithub.com/periodical/statistics/click?target=https://github.com/meetqy/aspoem)：现代化的古诗词学习网站。这是一个更加注重阅读体验和 UI 的诗词网站，采用 TypeScript、Next.js、Tailwind CSS 构建。它拥有简洁清爽的界面和好看的字体，提供了古诗词的拼音、注释、译文以及移动端适配、搜索和一键分享等功能。来自 [@meetqyhvkXU](https://hellogithub.com/user/5Flg6I2oHsSUdEk) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/733312562.png' style="max-width:80%; max-height=80%;"></img></p>

19、[MyIP](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jason5ng32/MyIP)：好用的 IP 工具箱。该项目的作者是一位产品经理，这是他借助 ChatGPT 完成的第一个 Vue.js 项目。通过该项目，你可以在线查看自己的 IP 信息（多源），并进行网站可用性、网速、MTR、DNS 泄漏、WebRTC 等检测。来自 [@Jason Ng](https://hellogithub.com/user/9CU82obLc56qzAg) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/722152303.png' style="max-width:80%; max-height=80%;"></img></p>

20、[nutui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jdf2e/nutui)：京东风格的移动端 Vue 组件库。该项目是由京东开源的移动端 Vue 组件库，专为移动端 H5 和小程序开发场景而设计。它内含 80 多个高质量组件，支持按需引用、TypeScript、国际化等特性。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/118392397.png' style="max-width:80%; max-height=80%;"></img></p>

21、[pikachu-volleyball](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gorisanson/pikachu-volleyball)：用 JavaScript 实现的皮卡丘排球游戏。该项目通过逆向工程解析原版的皮卡丘排球游戏，并使用 JavaScript 重新实现，包括物理引擎和对战机器人部分。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/243930206.png' style="max-width:80%; max-height=80%;"></img></p>

22、[wasp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wasp-lang/wasp)：一个类似 Rails 的 React、Node.js 全栈 Web 框架。该项目是一个面向 Web 开发人员的全栈 Web 框架，开发者只需编写简单的 .wasp 配置文件，就能自动生成基于 React 和 Node.js 构建的 Web 应用，而且内置了数据库、身份验证、路由等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/237222619.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
23、[marker](https://hellogithub.com/periodical/statistics/click?target=https://github.com/VikParuchuri/marker)：将 PDF 转换为 Markdown 文件的项目。这是一个能够将 PDF、EPUB 和 MOBI 格式的文件转换为 Markdown 文件的 Python 项目。相较于 Nougat，它具有更快的速度和更高的准确度，在处理英语类内容时效果最佳，但对中文的处理就要差一些。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/712111618.png' style="max-width:80%; max-height=80%;"></img></p>

24、[Paper-Piano](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Mayuresh1611/Paper-Piano)：在纸上弹钢琴。该项目使用 Python 和 OpenCV 实现图像处理和识别，通过摄像头捕获手指动作和手指下方的阴影，让用户可以通过触摸纸张来演奏钢琴。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/768431034.png' style="max-width:80%; max-height=80%;"></img></p>

25、[pelican](https://hellogithub.com/periodical/statistics/click?target=https://github.com/getpelican/pelican)：Python 语言的静态网站生成器。这是一个用 Python 编写的静态网站生成器，让你可以通过编写 Markdown、reStructuredText 等格式的文本文件来创建网站，支持生成 RSS、代码语法高亮、插件扩展等功能。

26、[posthog](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PostHog/posthog)：开源的产品分析平台。这是一款基于 Django 构建的产品分析和用户追踪平台，它提供了丰富的功能，包括事件跟踪、漏斗分析、群体分析、A/B 测试等，适用于了解用户行为、改善产品体验的场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/235901813.png' style="max-width:80%; max-height=80%;"></img></p>

27、[taipy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Avaiga/taipy)：快速打造数据驱动的 Web 应用。这是一个基于 Python 和 Flask 的项目，结合了 React 等前端技术，为开发者提供了一个简洁、高效的开发框架。它能够简化数据处理、API 开发和用户界面构建的开发过程。不论是数据科学家、机器学习工程师还是 Web 开发者，都能够利用 Taipy 快速完成从原型到 Web 应用的全过程。来自 [@刘三非](https://hellogithub.com/user/VhrXCAs7cMxL08W) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/460914281.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
28、[genact](https://hellogithub.com/periodical/statistics/click?target=https://github.com/svenstaro/genact)：假装很忙的摸鱼神器。该项目可以在终端上模拟一些很忙的假象，比如编译、扫描、下载等。这些操作都是假的，实际上什么都没有发生，所以不会影响你的电脑，适用于 Windows、Linux、macOS 操作系统。来自 [@39499740](https://hellogithub.com/user/7eRBdwFSrtPxipV) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/1345495.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[rnote](https://hellogithub.com/periodical/statistics/click?target=https://github.com/flxzt/rnote)：跨平台的手写笔记和绘图应用。这是一款用 Rust 和 GTK4 编写的绘图应用，可用于绘制草图、手写笔记和注释文档等。它支持导入/导出 PDF 和图片文件，以及无限画布、拖放、自动保存等功能。适用于 Windows、Linux 和 macOS 系统，需要搭配手写板使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/393045142.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
30、[Applite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/milanvarady/Applite)：Homebrew Cask 的桌面应用。这是一款采用 Swift 开发的免费 macOS 应用，它为 Homebrew Cask 提供了一个图形化界面，实现一键安装、更新和卸载应用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/674388699.png' style="max-width:80%; max-height=80%;"></img></p>

31、[BLEUnlock](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ts1/BLEUnlock)：使用蓝牙设备解锁你的 Mac 电脑。这款工具是可以在 macOS 上实现通过蓝牙设备解锁/锁定电脑。使用该工具时，蓝牙设备无需安装任何应用程序。当蓝牙设备靠近 Mac 电脑时，可以解锁屏幕并唤醒电脑；而当蓝牙设备远离时，自动锁定屏幕并暂停播放音乐/视频。支持 iPhone、Apple Watch、蓝牙耳机等设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/183878515.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
32、[FastChat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lm-sys/FastChat)：用于训练和评估大型语言模型的开放平台。这是一个用于训练、部署和评估大型语言模型的平台，你可以用它在本地部署和评估各种大模型。除此之外，它还提供了一个在线评估大模型的平台，用户可以向两个不同的大模型，问同一个问题，然后根据回答选出你认为更好用的大模型。在此过程中，你可以免费使用 Claude、ChatGPT 等对话机器人。来自 [@浮生若夢](https://hellogithub.com/user/hKmH64UjOdwgCEi) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/615882673.png' style="max-width:80%; max-height=80%;"></img></p>

33、[generative-ai-for-beginners](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/generative-ai-for-beginners)：面向初学者的生成式人工智能教程。这是由微软开源的面向初学者的生成式 AI 免费课程，课程共 18 节，涵盖了创建生成式 AI 应用所需要了解的一切，包括生成式 AI 和 LLMs 的简介、提示词、构建文本生成应用、聊天应用、图像生成应用、向量数据库等方面的内容。

34、[jan](https://hellogithub.com/periodical/statistics/click?target=https://github.com/janhq/jan)：一站式体验 LLMs 的桌面应用。这是一个支持在本地运行开源 LLMs 和连接 ChatGPT 服务的 AI 对话桌面应用，它开箱即用、界面清爽、不挑硬件，支持设置代理、接入 ChatGPT、一键下载/接入适配当前电脑配置的大模型、离线运行等功能，适用于 Windows、Linux、macOS 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/679506386.png' style="max-width:80%; max-height=80%;"></img></p>

35、[open-interpreter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/OpenInterpreter/open-interpreter)：让 LLM 在你的计算机上运行代码。该项目可以让大语言模型在本地运行代码，支持 Python、JavaScript、Shell 等编程语言。相当于大语言模型是一个解释器，它会理解你的意图，将自然语言转化成相应的代码脚本并运行。安装后，用户就可以在终端通过聊天的方式操作计算机，比如创建和编辑图片、视频和文件，控制 Chrome 浏览器进行搜索等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/666299222.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
36、[candle](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mitxela/candle)：自制 3D 电子蜡烛。该项目作者使用简单的 LED 板和小型电路板，制作了一个微型电子蜡烛，并通过旋转底座和流体模拟算法，模拟出 3D 的烛光效果。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/726135770.gif' style="max-width:80%; max-height=80%;"></img></p>

37、[docker-android](https://hellogithub.com/periodical/statistics/click?target=https://github.com/budtmo/docker-android)：运行在 Docker 容器里的 Android。这是一个 Android 模拟器的 Docker 镜像，支持 Android 9-14 版本、VNC（远程桌面）、ADB（Android 调试桥）、日志查看等功能，适用于 Android 客户端测试和调试等场景。
```
docker run -d -p 6080:6080 \
-e EMULATOR_DEVICE="Samsung Galaxy S10" \
-e WEB_VNC=true \
--device /dev/kvm \
--name android-container \
budtmo/docker-android:emulator_11.0
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/77145066.png' style="max-width:80%; max-height=80%;"></img></p>

38、[excelCPU](https://hellogithub.com/periodical/statistics/click?target=https://github.com/InkboxSoftware/excelCPU)：仅用 Excel 构建出一颗 CPU 。该项目是一颗运行在 Excel 文件中的 16 位 CPU 处理器，它具有 3Hz 主频、128KB RAM 和一块 128x128 像素的显示屏，为此作者还创建了一门汇编语言。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/748991484.png' style="max-width:80%; max-height=80%;"></img></p>

39、[Mr.-Ranedeer-AI-Tutor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)：打造你的个性化 AI 老师。该项目通过提示词让 AI 对话机器人充当老师和学习助手的角色，为你生成学习计划、授课解惑、出练习题等，还可以选择不同的授课风格和深度。它可搭配任意大模型，作者推荐 GPT-4 效果最佳。
```
===
Author: JushBJJ
Name: "Mr. Ranedeer 提示词"
Version: 2.7
===

[Student Configuration]
    🎯Depth: Highschool
    🧠Learning-Style: Active
    🗣️Communication-Style: Socratic
    🌟Tone-Style: Encouraging
    🔎Reasoning-Framework: Causal
    😀Emojis: Enabled (Default)
    🌐Language: English (Default)

    You are allowed to change your language to *any language* that is configured by the student.

[Overall Rules to follow]
    1. Use emojis to make the content engaging
    2. Use bolded text to emphasize important points
    3. Do not compress your responses
    4. You can talk in any language
...
```

40、[ugly-avatar](https://hellogithub.com/periodical/statistics/click?target=https://github.com/txstc55/ugly-avatar)：丑头像生成器。该项目可以用来随机生成一个很丑的手绘头像，不要怀疑真的很丑、很抽象，仅供娱乐。来自 [@puz_zle](https://hellogithub.com/user/hpUacD34bC7zAgw) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/777080032.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
41、[Real-Time-Rendering-4th-CN](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Morakito/Real-Time-Rendering-4th-CN)：《Real-Time Rendering 4th》中文翻译版。这是《Real-Time Rendering》第四版的中文翻译项目，该书是实时渲染领域的经典之作，非常适合从事游戏开发、3D 图形、VR/AR 等领域的开发者学习。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/721135559.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub95.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub97.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/96'>这里</a>。
</p>

## 赞助


<table>
  <thead>
    <tr>
      <th align="center" style="width: 80px;">
        <a href="https://www.ucloud.cn/site/active/gpu.html?utm_term=logo&utm_campaign=hellogithub&utm_source=otherdsp&utm_medium=display&ytag=logo_hellogithub_otherdsp_display">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/ucloud.png" width="60px"><br>
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


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
