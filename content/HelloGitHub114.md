# 《HelloGitHub》第 114 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/114) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[fastfetch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fastfetch-cli/fastfetch)：更快的系统信息查看工具。这是一个类似 neofetch 的命令行工具，可以在终端里概览系统的相关信息。它采用 C 语言编写，相较于 bash 写的 neofetch 更快，显示的信息包括操作系统、Shell、内核、CPU、GPU、内存等，目前支持 Linux、Android、FreeBSD、macOS 和 Windows 7+ 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/340181518.png' style="max-width:80%; max-height=80%;"></img></p>

2、[miniaudio](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mackron/miniaudio)：极简易用的 C 语言音频库。这是一个单文件、零依赖、跨平台的 C 语言音频库。它将各种主流操作系统的底层音频 API 封装成简单易用的接口，让你轻松实现音频播放、录制和处理等功能，适用于游戏引擎、实时通讯、嵌入式、离线批处理等场景。
```c
#include "miniaudio/miniaudio.h"

#include <stdio.h>

int main()
{
    ma_result result;
    ma_engine engine;

    result = ma_engine_init(NULL, &engine);
    if (result != MA_SUCCESS) {
        return -1;
    }

    ma_engine_play_sound(&engine, "sound.wav", NULL);

    printf("Press Enter to quit...");
    getchar();

    ma_engine_uninit(&engine);

    return 0;
}
```

### C# 项目
3、[ClassIsland](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ClassIsland/ClassIsland)：抬头即见的开源课表工具。这是一款专为大屏设备打造的桌面课表应用，可将课程表以简洁组件的形式常驻桌面，取代传统黑板课表。支持下课提醒、天气信息、倒计时、密码保护和课表导入等功能，适用于配备教室多媒体大屏、投影仪或智慧黑板的教室。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/663887125.png' style="max-width:80%; max-height=80%;"></img></p>

4、[CrossPlatformDiskTest](https://hellogithub.com/periodical/statistics/click?target=https://github.com/maxim-saplin/CrossPlatformDiskTest)：多平台硬盘性能测试工具。这是一款开源的存储与内存性能测试工具，适用于固态硬盘、机械硬盘、U 盘等存储设备。支持顺序和随机读写测试，提供 IOPS 和 MB/s 等性能指标，兼容 Windows、macOS、Linux、Android 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/150983217.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[Crow](https://hellogithub.com/periodical/statistics/click?target=https://github.com/CrowCpp/Crow)：类 Flask 的轻量级 C++ Web 框架。这是一款专为 C++ 开发者设计的轻量级 Web 框架，仅需引入头文件即可轻松集成。它拥有类似 Python Flask 的简洁易用路由 API，只需少量代码即可快速搭建 Web 服务，大幅降低 C++ Web 开发的门槛。
```cpp
#include "crow.h"

int main()
{
    crow::SimpleApp app;

    CROW_ROUTE(app, "/")([](){
        return "Hello world";
    });

    app.port(18080).multithreaded().run();
}
```

6、[ShaderGlass](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mausimus/ShaderGlass)：为 Windows 桌面实时添加酷炫特效。这是一款适用于 Windows 系统的着色器工具，能够实现图像特效、复古显示、视觉增强等多种叠加效果。它可以为你的屏幕或应用窗口，实时添加一层“特效滤镜”，内置 CRT、图像放大、像素化、色彩校正等经典着色器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/308317827.jpg' style="max-width:80%; max-height=80%;"></img></p>

7、[vicinae](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vicinaehq/vicinae)：极速的原生桌面启动器。这是一款基于 C++ 开发的桌面启动器，不依赖 Electron 或浏览器。它速度快、易扩展、界面简洁，专注于提升桌面操作效率，支持文件搜索、剪贴板历史、内联计算器等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1027461827.gif' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[fuck-u-code](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Done-0/fuck-u-code)：自动检测代码屎山等级的工具。这是一款用于评估代码“屎山等级”的工具，支持 Python、Java、Go 等多种编程语言。它能够自动扫描指定目录，深入分析项目代码的混乱程度，并用犀利又搞笑的方式告诉你结果。来自 [@wei-guang](https://hellogithub.com/user/JtGB5xfIQaqE1re) 的分享

9、[git-who](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sinclairtarget/git-who)：Git 目录级别的贡献分析工具。这是一个用 Go 和 Ruby 语言开发的命令行工具，用于在 Git 仓库中按目录快速统计并可视化每位贡献者的提交次数、代码修改行数和活跃时间。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/899941526.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[gonzo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/control-theory/gonzo)：终端用户界面日志分析工具。这是一个用 Go 语言开发的终端（TUI）日志分析工具，灵感来自 k9s。它支持在终端界面下实时分析、过滤和可视化日志，结合 AI 提升日志洞察能力，适用于日常开发、运维和故障排查等场景。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1040280323.png' style="max-width:80%; max-height=80%;"></img></p>

11、[ntfy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/binwiederhier/ntfy)：开箱即用的跨设备推送通知服务。该项目是基于 HTTP 协议的开源推送通知服务，支持通过 PUT/POST 请求跨设备推送消息。它采用 Go 语言开发，用户无需注册即可通过命令行工具或简单的 API 轻松发送通知，支持自定义通知内容和自托管部署，并提供配套的 Android 和 iOS 客户端。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/420503947.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[kroki](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yuzutech/kroki)：支持多语法的轻量级图表生成服务。这是一个支持多种文本描述生成图表的服务，提供统一 API 接口，支持数十种主流图表语法和格式，包括 PlantUML、Mermaid、Graphviz、C4、BlockDiag、BPMN、Excalidraw 等。来自 [@塔咖](https://hellogithub.com/user/bzJpGyu0IanC6L7) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/165063056.png' style="max-width:80%; max-height=80%;"></img></p>

13、[PeerBanHelper](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PBH-BTN/PeerBanHelper)：提升下载体验的 BT 反吸血工具。这是一款专为 BT（BitTorrent）用户设计的反吸血工具，能够自动识别并封禁只下载不上传、不受欢迎或异常节点（peer），支持 qBittorrent、Deluge、BiglyBT、BitComet 等主流 BT 客户端。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/754169590.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
14、[CubeCity](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hexianWeb/CubeCity)：卡通风格城市建设模拟游戏。这是一款轻量级、卡通风格的 2.5D 城市模拟游戏，基于 Three.js 和 Vue3 构建。玩家可在浏览器中通过点选和拖放，实时建造、搬迁和拆除建筑。建筑会自动产出金币，可用于新建或升级设施。游戏融合了环境、社会与治理（ESG）理念，城市规划需兼顾多元需求，才能打造出可持续发展的理想城市。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1013487627.png' style="max-width:80%; max-height=80%;"></img></p>

15、[lazy-brush](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dulnan/lazy-brush)：平滑手写与签名的 JavaScript 库。这是一个用于平滑绘图的 JavaScript 库，支持通过鼠标或手指流畅绘制画笔轨迹。它采用“惰性画笔”算法，有效减少手抖、锯齿等问题，让线条更加自然顺滑，适用于画板、签名、手写等多种场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/145379450.png' style="max-width:80%; max-height=80%;"></img></p>

16、[mammoth.js](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mwilliamson/mammoth.js)：将 Word 文档转换为 HTML 的库。这是一个用于将 Word 文档（.docx）内容转换为 HTML 的 JavaScript 库。它能够提取文档中的结构信息，如标题、列表、表格、脚注等，并映射为相应的 HTML 标签。同时，忽略大部分样式（如字体颜色、字号、边距等），使得生成的 HTML 代码更加简洁、干净。
```javascript
var mammoth = require("mammoth");

mammoth.convertToHtml({path: "path/to/document.docx"})
    .then(function(result){
        var html = result.value; // The generated HTML
        var messages = result.messages; // Any messages, such as warnings during conversion
    })
    .catch(function(error) {
        console.error(error);
    });
```

17、[Termix](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Termix-SSH/Termix)：高颜值一站式服务器管理平台。这是一个基于 Web 的服务器管理平台，集成了 SSH 终端、SSH 隧道、服务器监控和文件管理等功能。它完全开源免费、可自托管，支持自动重连、文件上传、分屏显示和语法高亮等特性。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/893684207.png' style="max-width:80%; max-height=80%;"></img></p>

18、[websocket-devtools](https://hellogithub.com/periodical/statistics/click?target=https://github.com/law-chain-hot/websocket-devtools)：开箱即用的 WebSocket 调试工具。这是一款专业的 WebSocket 调试与流量控制浏览器插件，安装后会在 Chrome DevTools 面板中新增一个标签页。操作便捷，支持 WebSocket 流量的实时监控、消息模拟和流量拦截等功能。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1013230576.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
19、[goodtime](https://hellogithub.com/periodical/statistics/click?target=https://github.com/adrcotfas/goodtime)：极简省电的番茄时钟工具。这是一个开源的 Android 时间管理工具，基于番茄工作法帮助用户管理时间、提升专注力。它无广告、无追踪、完全离线，支持历史记录、彩色标签、热力图统计、专注/休息比率、自定义样式等功能。来自 [@ewiro](https://hellogithub.com/user/iItGgWoJjnLsr0Y) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/61319303.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
20、[lutris](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lutris/lutris)：开源的 Linux 游戏平台。这是一款专为 Linux 用户设计的游戏管理平台，采用 Python 编写。它提供了友好的用户界面，极大地简化了 Linux 上的游戏安装和配置过程，让用户能够轻松安装和管理各种游戏，支持连接 Steam、GOG、Humble Bundle 等多种游戏平台，以及运行 Windows 游戏的功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/13419223.jpg' style="max-width:80%; max-height=80%;"></img></p>

21、[pdfplumber](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jsvine/pdfplumber)：轻松提取 PDF 文本和表格的 Python 库。该项目是基于 Python 的 PDF 解析与数据提取库，可轻松提取文本和表格。它能够精确获取 PDF 文档中每个字符、线条、矩形等元素的详细位置、尺寸和字体信息，并支持一键生成页面快照，方便调试。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/41279279.png' style="max-width:80%; max-height=80%;"></img></p>

22、[pydoll](https://hellogithub.com/periodical/statistics/click?target=https://github.com/autoscrape-labs/pydoll)：无需 WebDriver 的浏览器自动化 Python 库。这是一个用于自动化操作 Chromium 内核浏览器的 Python 库。它通过原生 DevTools 协议（CDP）直接控制浏览器，无需依赖 WebDriver，支持绕过验证码、模拟真人交互、网页截图等功能。
```python
import asyncio

from pydoll.browser import Chrome
from pydoll.constants import Key

async def baidu_search(query: str):
    async with Chrome() as browser:
        tab = await browser.start()
        await tab.go_to('https://www.baidu.com')
        search_box = await tab.find(tag_name='textarea', id='chat-textarea')
        await search_box.insert_text(query)
        await search_box.press_keyboard_key(Key.ENTER)
        await asyncio.sleep(5)

asyncio.run(baidu_search('HelloGitHub'))
```

23、[pyscript](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pyscript/pyscript)：直接在浏览器中用 Python 创建应用程序。该项目可以让开发者在 HTML 文件中直接使用 Python 编程语言，像 JavaScript 文件一样引入和执行 Python 代码，支持更小的 MicroPython、常见第三方库和操作页面元素等功能，适用于快速创建交互的数据可视化、网站原型和在线教育等 Web 应用场景。来自 [@Veeja Liu](https://hellogithub.com/user/70zTMbIqVf9dvZp) 的分享
```html
<head>
    <link rel="stylesheet" href="./core.css"/>
    <script type="module" src="./core.js"></script>
</head>
<body>
    <script type="py" terminal>
        from pyscript import display
        display("HelloGitHub!") # this goes to the DOM
        print("Hello terminal") # this goes to the terminal
    </script>
</body>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/461710233.png' style="max-width:80%; max-height=80%;"></img></p>

24、[tinyio](https://hellogithub.com/periodical/statistics/click?target=https://github.com/patrick-kidger/tinyio)：极简易用的 Python 事件循环库。这是一个仅约 300 行代码的轻量级 Python 事件循环库，为开发者提供比 asyncio 更加简洁易用的异步编程体验。
```python
import tinyio

def slow_add_one(x: int):
    yield tinyio.sleep(1)
    return x + 1

def foo():
    four, five = yield [slow_add_one(3), slow_add_one(4)]
    return four, five

loop = tinyio.Loop()
out = loop.run(foo())
assert out == (4, 5)
```

### Rust 项目
25、[rust-tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/InkSha/rust-tutorial)：新手友好的 Rust 实战教程。这是一个专为 Rust 初学者设计的快速入门教程，带你一步步实现一个可用的命令行 Todo 应用。

26、[Seelen-UI](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eythaann/Seelen-UI)：高度可定制的 Windows 桌面美化工具。这是一款免费开源的 Windows 桌面增强工具，专注于高度自定义和效率提升。它采用 Rust 语言开发，结合 Tauri 框架与 Web 技术，支持窗口平铺管理、应用启动器、Dock、任务栏、动态壁纸、插件扩展等功能。来自 [@Rainux He](https://hellogithub.com/user/EDis5NBzXAIb4qF) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/758623687.png' style="max-width:80%; max-height=80%;"></img></p>

27、[xh](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ducaale/xh)：更友好的命令行 HTTP 客户端。这是一个用 Rust 编写的命令行 HTTP 客户端，支持语法高亮、JSON 格式化、下载进度条、会话 Cookie 持久化等功能，可完美替代 cURL。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/294521053.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
28、[AirBattery](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lihaoyun6/AirBattery)：隔空查看苹果设备电量的 Mac 工具。这是一款专为 macOS 设计的电量监控工具，能在 Mac 菜单栏实时显示 iPhone、iPad、AirPods 和 Apple Watch 等设备的电池电量。无需在 iOS 端安装任何 App，即可在电脑端查看设备当前电量、充电状态，并支持低电量提醒。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/755969344.png' style="max-width:80%; max-height=80%;"></img></p>

29、[Ice](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jordanbaird/Ice)：强大的 macOS 菜单栏管理工具。该项目是适用于 macOS 系统的菜单栏管理工具，它开箱即用、操作简单，主要功能是隐藏和显示菜单栏内容，支持悬停显示、点击显示、自动隐藏、设置菜单栏阴影、快捷键、开机启动、自动更新等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/674832198.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
30、[how-to-build-a-coding-agent](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ghuntley/how-to-build-a-coding-agent)：从零实现 AI 编程助手的实战教程。这是一个教你用 Go 语言结合 Claude API，从零开发本地 AI 编程助手的项目。从简单的聊天机器人开始，逐步实现文件操作、命令执行、代码编辑和搜索等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1025300166.png' style="max-width:80%; max-height=80%;"></img></p>

31、[parlant](https://hellogithub.com/periodical/statistics/click?target=https://github.com/emcie-co/parlant)：给大模型立规矩的智能体开发框架。这是一款专为实际场景控制设计的 LLM 智能体开发框架，旨在解决传统 LLM 对话系统在复杂业务中难以精准控制的问题。它通过自然语言定义智能体行为规则，灵活控制 AI 的对话行为，避免“幻觉”或偏离业务目标。
```python
import asyncio
import parlant.sdk as p

async def main():
  async with p.Server() as server:
    agent = await server.create_agent(
        name="Otto Carmen",
        description="You work at a car dealership",
    )

    await agent.create_guideline(
        # This is when the guideline will be triggered
        condition="the customer greets you",
        # This is what the guideline instructs the agent to do
        action="offer a refreshing drink",
    )

asyncio.run(main())
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/758197374.gif' style="max-width:80%; max-height=80%;"></img></p>

32、[SwanLab](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SwanHubX/SwanLab)：AI 模型训练跟踪与可观测平台。这是一款专为 AI 模型训练打造的跟踪、记录、分析与协作工具，旨在帮助研究者优化训练过程，提升团队协作效率。它通过简洁的 Python API 和直观的界面，提供了训练可视化、自动日志记录、硬件监控、实验管理和多人协同等功能。已集成 40+ 主流训练框架，适用于大模型训练、计算机视觉、音频处理、AIGC 等任务场景。来自 [@Ze-Yi LIN](https://hellogithub.com/user/Oh5UaGjfrblg0yZ) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/722915433.png' style="max-width:80%; max-height=80%;"></img></p>

33、[WhisperLiveKit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/QuentinFuxa/WhisperLiveKit)：开箱即用的本地语音转写工具。这是一款集实时语音转文本、翻译和说话人分离于一体的开源工具，自带服务器端和 Web UI，一条命令即可私有化部署。它基于最新的增量流式技术，无需联网和写前端代码，就能实现超低延迟的会议实时记录和跨语言交流。
```
# 使用 large-v3 模型，并将英语翻译为中文
whisperlivekit-server --model large-v3 --language en --target-language zh

# 说话人分离，服务器监听 80 端口
whisperlivekit-server --host 0.0.0.0 --port 80 --model medium --diarization --language zh
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/905697354.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
34、[balatro-gba](https://hellogithub.com/periodical/statistics/click?target=https://github.com/GBALATRO/balatro-gba)：年度扑克神作 GBA 移植版。这是一个将游戏《小丑牌》（Balatro）移植到 GBA 平台的项目。为保护游戏版权，该项目仅提供简化版的《Balatro》，不会完整还原原作内容，且需要用户自行构建 ROM 文件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/925448611.png' style="max-width:80%; max-height=80%;"></img></p>

35、[CookLikeHOC](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Gar-b-age/CookLikeHOC)：老乡鸡菜谱开源版。该项目非老乡鸡官方出品，是作者基于《老乡鸡菜品溯源报告》等资料，归纳、整理了老乡鸡菜品的配方、制作流程及烹饪要点。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

36、[flip-card](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Nicholas-L-Johnson/flip-card)：一张会“流动”的电子名片。这是一个将实时流体模拟效果呈现在一张名片大小硬件上的开源项目。它基于树莓派 RP2350，采用 Rust 语言实现粒子模拟，整体硬件成本约 12 美元。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1024724696.gif' style="max-width:80%; max-height=80%;"></img></p>

37、[podman-desktop](https://hellogithub.com/periodical/statistics/click?target=https://github.com/podman-desktop/podman-desktop)：免费开源的容器桌面管理工具。这是一款跨平台、免费开源的容器与 K8s 桌面管理工具，为容器和 K8s 的构建、管理与部署提供了直观易用的桌面界面，支持 Podman、Docker、Lima、kind 等主流容器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/465844859.png' style="max-width:80%; max-height=80%;"></img></p>

38、[winboat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TibixDev/winboat)：在 Linux 系统上轻松运行 Windows 应用。这是一款无需复杂配置即可在 Linux 上运行 Windows 应用的工具。通过图形化向导自动完成镜像拉取、容器创建和 RDP 配置，全程无需手动敲命令，就能让 Windows 应用以独立窗口无缝呈现在 Linux 桌面。来自 [@moyelx](https://hellogithub.com/user/e8vnBGS9XmjYLho) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/960420129.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
39、[ml-interviews-book](https://hellogithub.com/periodical/statistics/click?target=https://github.com/chiphuyen/ml-interviews-book)：《Machine Learning Interviews Book》机器学习面试指南。这是一本免费开源的电子书，专为机器学习领域求职面试而设计，内容涵盖 ML 岗位类型、面试官评分视角、备战路线，以及 200+ 道分级面试题。



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub113.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub115.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/114'>这里</a>。
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
