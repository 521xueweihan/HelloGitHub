# 《HelloGitHub》第 112 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/112) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[AltSnap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/RamonUnch/AltSnap)：Windows 全局 Alt 键窗口管理器。这是一款将 Linux 系统中高效的窗口管理方式复刻到 Windows 平台的工具。你只需按住 Alt 键，即可用鼠标在窗口的任何位置轻松拖动、缩放和停靠，彻底告别繁琐地寻找并点击标题栏和边框的传统操作。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/315453540.png' style="max-width:80%; max-height=80%;"></img></p>

2、[libpostal](https://hellogithub.com/periodical/statistics/click?target=https://github.com/openvenues/libpostal)：兼容全球地址格式的解析库。该项目是用 C 语言编写的全球地址解析库，支持多种语言、格式和国家的地址字符串，能够将地址信息转换为结构化数据。
```c
#include <stdio.h>
#include <stdlib.h>
#include <libpostal/libpostal.h>

int main(int argc, char **argv) {
    // Setup (only called once at the beginning of your program)
    if (!libpostal_setup() || !libpostal_setup_parser()) {
        exit(EXIT_FAILURE);
    }

    libpostal_address_parser_options_t options = libpostal_get_address_parser_default_options();
    libpostal_address_parser_response_t *parsed = libpostal_parse_address("781 Franklin Ave Crown Heights Brooklyn NYC NY 11216 USA", options);

    for (size_t i = 0; i < parsed->num_components; i++) {
        printf("%s: %s\n", parsed->labels[i], parsed->components[i]);
    }

    // Free parse result
    libpostal_address_parser_response_destroy(parsed);

    // Teardown (only called once at the end of your program)
    libpostal_teardown();
    libpostal_teardown_parser();
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/31570906.gif' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[dlss-swapper](https://hellogithub.com/periodical/statistics/click?target=https://github.com/beeradmoore/dlss-swapper)：免更新切换游戏 DLSS 版本的工具。这是一款用于管理和替换游戏的 DLSS、FSR 和 XeSS DLL 文件的工具，支持 Steam、GOG、Epic Games 等主流游戏平台。它可以在不更新游戏的情况下，升级或降级游戏的 DLSS、FSR 和 XeSS 版本，从而优化游戏画质与性能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/393538656.gif' style="max-width:80%; max-height=80%;"></img></p>

4、[Mate-Engine](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shinyflvre/Mate-Engine)：开源的 VRM 桌面虚拟伴侣。这是一款开源的桌面虚拟伴侣应用，可作为 Desktop Mate 的开源替代品，支持将自定义的 3D 虚拟角色置于桌面，并内置流畅的闲置动画、点击互动、随音乐舞动等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/951665915.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[d2mcpp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mcpp-community/d2mcpp)：动手学现代 C++ 语言特性。这是一套完全开源的现代 C++ 语言特性互动教程。它把 C++11 的核心语言特性（如类型自动推导、移动语义等），拆成可运行的迷你练习，通过自研的 xlings 工具，实现一键安装依赖和实时判题等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/964948225.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[LunaTranslator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HIllya51/LunaTranslator)：开源的视觉小说翻译工具。这是一款专为 Windows 平台设计的视觉小说（Galgame）翻译器，支持 HOOK、OCR、剪贴板等多种文本提取方式，可灵活切换，并提供在线翻译、离线翻译、语音合成等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/542386106.png' style="max-width:80%; max-height=80%;"></img></p>

7、[WindowsAppSDK](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/WindowsAppSDK)：为旧桌面应用注入新活力的 SDK。该项目是微软官方开源的 Windows 桌面应用开发组件和工具集，旨在帮助传统的 Win32、WPF、WinForms 等应用，轻松集成最新的 Windows UI 和平台功能。只需引入一个 NuGet 包，就能为原应用引入更美观的 UI 和推送通知、窗口圆角等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/256049233.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[evcc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/evcc-io/evcc)：个人电车充电智能管理平台。这是一个开源的 EV（电动汽车）充电器控制平台，为电车车主提供灵活且易于安装的充电解决方案。它提供了可视化且适配移动端的 Web 平台，用户可以通过该平台远程启动、停止和监控车辆的充电状态，支持多种充电设备和车辆型号。智能充电功能还可以根据电价、太阳储能和日程安排，智能安排充电时间，从而节约电费。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/226368338.png' style="max-width:80%; max-height=80%;"></img></p>

9、[genai-toolbox](https://hellogithub.com/periodical/statistics/click?target=https://github.com/googleapis/genai-toolbox)：Google 开源的数据库 MCP 工具。该项目是 Google 开源的 MCP 服务器，专为 LLM 应用与各类数据库之间提供统一、安全、可扩展的数据访问层。它集成了连接池、身份验证、监控等功能，让 AI agent 快速拥有查询数据库的能力，支持 PostgreSQL、MySQL 等多种数据库。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/812044182.png' style="max-width:80%; max-height=80%;"></img></p>

10、[gpt-load](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tbphp/gpt-load)：企业级的多渠道大模型 API 管理平台。这是一款用 Go 语言开发的企业级大模型接口管理平台，支持 OpenAI、Gemini、Claude 等多种服务。它开箱即用、内置 Web 管理界面、保留原生 API 格式，支持密钥自动轮询、故障切换和水平扩展，专为高并发生产环境而设计。来自 [@tbphp](https://hellogithub.com/user/Qlh8vzrWJ0HCneG) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/997490512.png' style="max-width:80%; max-height=80%;"></img></p>

11、[zenta](https://hellogithub.com/periodical/statistics/click?target=https://github.com/e6a5/zenta)：快速恢复专注的命令行工具。这是一个 Go 语言开发的命令行工具，旨在帮助开发者在心烦意乱或注意力不集中时，通过简单的呼吸练习，快速找回专注和内心的平静。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1008849671.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[javacv](https://hellogithub.com/periodical/statistics/click?target=https://github.com/bytedeco/javacv)：全能的计算机视觉 Java 库。该项目让开发者能够在 Java 虚拟机（JVM）直接调用如 OpenCV、FFmpeg、Tesseract 等常用的计算机视觉库，快速开发出实时图像分析、视频编解码、流式传输和 OCR 等功能模块。
```java
import org.bytedeco.opencv.opencv_core.*;
import org.bytedeco.opencv.opencv_imgproc.*;
import static org.bytedeco.opencv.global.opencv_core.*;
import static org.bytedeco.opencv.global.opencv_imgproc.*;
import static org.bytedeco.opencv.global.opencv_imgcodecs.*;

public class Smoother {
    public static void smooth(String filename) {
        Mat image = imread(filename);
        if (image != null) {
            GaussianBlur(image, image, new Size(3, 3), 0);
            imwrite(filename, image);
        }
    }
}
```

13、[JsonPath](https://hellogithub.com/periodical/statistics/click?target=https://github.com/json-path/JsonPath)：像操作 XML 一样轻松读写 JSON。该项目为 Java 开发者提供类似路径查询的方式，能够轻松从复杂的 JSON 结构中提取数据，无需手动遍历即可定位目标节点。来自 [@塔咖](https://hellogithub.com/user/bzJpGyu0IanC6L7) 的分享
```java
String json = "...";
Object document = Configuration.defaultConfiguration().jsonProvider().parse(json);

String author0 = JsonPath.read(document, "$.store.book[0].author");
String author1 = JsonPath.read(document, "$.store.book[1].author");
```

14、[nifi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/apache/nifi)：可视化拖拽的数据流管理平台。这是一个基于流程编程理念的数据流管理系统。它提供可视化的 Web 管理界面，支持数据溯源、断点续传、弹性扩展和丰富的处理器。用户可以像画流程图一样设计、控制和监控各系统间的数据流动，适用于数据湖、实时风控、AI 数据管道等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/27911088.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
15、[base-ui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mui/base-ui)：轻松定制的无样式 React 组件库。该项目提供了一套基础、无样式的 React 组件，仅包含必要的功能逻辑，不附带任何预设样式。帮助开发者摆脱传统 UI 库的样式束缚，无需耗费大量精力覆盖和修改默认样式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/762289766.png' style="max-width:80%; max-height=80%;"></img></p>

16、[cap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tiagozip/cap)：轻量级的 CAPTCHA 替代方案。这是一个轻量级、开源的验证码方案，适用于防止机器人滥用和数据抓取等场景。它基于 SHA-256 工作量证明（Proof-of-Work）技术，易于集成、即插即用，为网站提供自托管的防滥用验证机制。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/915378930.png' style="max-width:80%; max-height=80%;"></img></p>

17、[drawnix](https://hellogithub.com/periodical/statistics/click?target=https://github.com/plait-board/drawnix)：极简的在线白板工具。这是一款免费、开源的在线白板工具。它提供一个无限画布，支持自由绘制、思维导图、流程图、画笔、插入图片、自动保存等功能，以及移动端适配、Docker 部署和插件机制等特性。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/810364325.png' style="max-width:80%; max-height=80%;"></img></p>

18、[FossFLOW](https://hellogithub.com/periodical/statistics/click?target=https://github.com/stan-smith/FossFLOW)：开源的伪 3D 图绘制工具。这是一款专为创建专业的等距（isometric）基础架构图而设计的绘图工具，支持离线使用。等距图是以 2D 形式呈现 3D 效果，能够更直观、精准地展现复杂的设计和系统架构。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1011253718.png' style="max-width:80%; max-height=80%;"></img></p>

19、[snapdom](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zumerlab/snapdom)：精准的网页内容截图库。这是一个高效的网页截图 JavaScript 库，可将网页上的任意 Dom 元素快速、精确地转化为高质量图片，并支持导出为 PNG、JPG、WebP 或 Canvas 格式，适用于网页自动化测试、生成预览图、内容保存等场景。来自 [@Yee1014](https://hellogithub.com/user/1B5n92jVikAMPpc) 的分享
```javascript
const el = document.querySelector('#target');
const result = await snapdom(el, { scale: 2 });

const img = await result.toPng();
document.body.appendChild(img);

await result.download({ format: 'jpg', filename: 'my-capture' });
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/973606777.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
20、[Iconify](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Mahmud0808/Iconify)：深度定制你的 Android 系统界面。这是一款功能强大的 Android 系统级美化工具，专为 Android 12 及以上的 Pixel 或 AOSP 类 ROM 设计。它支持对设备用户界面（UI）进行深度定制和修改，包括但不限于状态栏图标（如 Wi-Fi、信号）、系统图标、图标形状、锁屏时钟样式、通知面板布局和颜色等。来自 [@ewiro](https://hellogithub.com/user/iItGgWoJjnLsr0Y) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/529537665.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
21、[jupyterlite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jupyterlite/jupyterlite)：在浏览器中运行的 JupyterLab。这是一个完全在浏览器中运行的 JupyterLab，无需安装 Python 或配置服务器。它提供在线交互式 Python 编程环境，可作为静态文件部署到任何静态网站托管平台（如 GitHub Pages）。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/352160885.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[mediacms](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mediacms-io/mediacms)：基于 Django 的在线视频平台。这是一个基于 Django 和 React 构建的视频内容管理平台，可快速搭建中小型视频网站。它内置转码、搜索、播放列表、权限管理和移动端适配等功能，支持视频、音频、图像、PDF 等多媒体格式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/321785127.jpg' style="max-width:80%; max-height=80%;"></img></p>

23、[requests-futures](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ross/requests-futures)：优雅的异步 Python HTTP 请求库。这是一个为 Python requests 库提供异步 HTTP 请求的轻量级封装库。它结合了 requests 库的易用性和标准库 concurrent.futures 的并发能力，支持以非阻塞方式发送单个或多个 HTTP 请求，从而显著提升 I/O 密集型应用的性能。
```python
from concurrent.futures import as_completed
from pprint import pprint
from requests_futures.sessions import FuturesSession

session = FuturesSession()

futures=[session.get(f'http://httpbin.org/get?{i}') for i in range(3)]

for future in as_completed(futures):
    resp = future.result()
    pprint({
        'url': resp.request.url,
        'content': resp.json(),
    })
```

24、[UavNetSim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Zihao-Felix-Zhou/UavNetSim)：无人机通信网络仿真平台。这是一款基于 Python（SimPy）的无人机通信网络仿真平台，专为组建无人机集群通信而设计。它提供无人机网络的多个层级（如网络层、MAC 层、物理层），以及无人机移动性和能量模型的全面建模，适用于无人机网络的协议设计、性能评估和可视化分析。来自 [@凝望，划过星空](https://hellogithub.com/user/yc7sS80jimthluU) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/955363828.png' style="max-width:80%; max-height=80%;"></img></p>

25、[ZSim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ZSim-Dev/ZSim)：《绝区零》战斗模拟器。这是一个专为游戏《绝区零》设计的伤害模拟和战斗仿真工具，支持全自动仿真、可视化报告、自定义 APL 等功能。玩家可自由选择游戏中的角色与装备，并配置属性参数，然后通过模拟器计算出在特定队伍组合下的预期伤害。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1012686024.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
26、[rustfs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rustfs/rustfs)：基于 Rust 的高性能分布式存储系统。该项是用 Rust 构建的高性能分布式对象存储系统，致力于成为 MinIO 的开源替代品。它安装简单、兼容 S3 协议，采用更友好的开源协议，并内置界面清爽的 Web 管理后台。同时，支持国产保密设备和系统，适用于海量数据存储、大数据、互联网、工业和保密存储等场景。来自 [@SR.李](https://hellogithub.com/user/vQ0IpLkHo3T9lO1) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/722597620.png' style="max-width:80%; max-height=80%;"></img></p>

27、[tabiew](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shshemi/tabiew)：命令行数据文件可视化浏览工具。这是一款用于浏览和查询表格数据文件（如 CSV、Parquet、Arrow、Excel 等）的命令行工具。它提供交互式界面体验、支持 SQL 查询、多表操作、模糊搜索和 Vim 风格快捷键等功能。来自 [@HBSpy](https://hellogithub.com/user/rIXCy0ZT2L49Ysj) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/792805133.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
28、[KeyboardCowboy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zenangst/KeyboardCowboy)：重塑你的 macOS 快捷键。这是一款能够重塑 macOS 快捷键体验的键盘工作流工具，可为任意应用创建强大且具备上下文感知能力的快捷键，无需手动触发。它不仅能模拟点击没有原生快捷键的按钮、选择菜单项，还能将多步操作串联为一键执行的高效流程，提升工作流效率。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/292346804.png' style="max-width:80%; max-height=80%;"></img></p>

29、[TrackWeight](https://hellogithub.com/periodical/statistics/click?target=https://github.com/KrishKrosh/TrackWeight)：MacBook 触控板秒变电子秤。这是一款有趣的 macOS 应用，可以将 MacBook 的触控板变身为数字电子秤。它利用触控板内置的 Force Touch 压力传感器，只需将物体放在触控板上，应用即可实时显示其重量。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1023406764.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
30、[gitingest](https://hellogithub.com/periodical/statistics/click?target=https://github.com/coderamp-labs/gitingest)：一键将代码库转换为 AI 友好格式的工具。该项目可将任意 GitHub 仓库快速转换为适合大语言模型处理的纯文本摘要。使用起来十分方便，只需将 GitHub 项目地址中的 hub 替换为 ingest 即可得到文本摘要。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/895942941.png' style="max-width:80%; max-height=80%;"></img></p>

31、[ManimML](https://hellogithub.com/periodical/statistics/click?target=https://github.com/helblazer811/ManimML)：用 Python 动态演示神经网络。这是一个基于 Manim 的 Python 库，用于制作机器学习相关概念的动画和可视化效果。只需编写简单的 Python 代码，即可轻松生成神经网络结构、卷积操作、Dropout 过程等动画效果，帮助理解和展示复杂的机器学习原理。
```python
from manim_ml.neural_network import NeuralNetwork, FeedForwardLayer

nn = NeuralNetwork([
    FeedForwardLayer(num_nodes=3),
    FeedForwardLayer(num_nodes=5),
    FeedForwardLayer(num_nodes=3)
])
self.add(nn)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/454906591.gif' style="max-width:80%; max-height=80%;"></img></p>

32、[unsloth](https://hellogithub.com/periodical/statistics/click?target=https://github.com/unslothai/unsloth)：新手友好的 LLM 微调工具库。该项目是用于微调和优化大型语言模型（LLM）的 Python 工具库。它通过动态量化和显存优化技术，提高了模型微调速度，同时将显存占用降低 70%-80%，并支持多种硬件配置、LLM、超长上下文任务等功能。除此之外，还提供了可直接在线体验的 Jupyter Notebook 示例，降低了大模型微调的门槛。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/725205304.png' style="max-width:80%; max-height=80%;"></img></p>

33、[uzu](https://hellogithub.com/periodical/statistics/click?target=https://github.com/trymirai/uzu)：MacBook 专属的高性能 AI 推理引擎。这是一个专为 Apple M 系列芯片打造的高性能、轻量级 AI 模型推理引擎。它充分利用 Apple 硬件的特性提升推理速度，并提供简单易用的 API，助你一键部署高效本地大模型服务。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1007360921.png' style="max-width:80%; max-height=80%;"></img></p>

34、[VideoCaptioner](https://hellogithub.com/periodical/statistics/click?target=https://github.com/WEIFENG2333/VideoCaptioner)：开箱即用的智能字幕助手。这是一款基于大语言模型的智能视频字幕处理工具。它界面简洁、操作便捷，支持语音识别、智能校对和自动生成多语言字幕等功能。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/881171866.jpg' style="max-width:80%; max-height=80%;"></img></p>

### 其它
35、[12-factor-agents](https://hellogithub.com/periodical/statistics/click?target=https://github.com/humanlayer/12-factor-agents)：构建生产级 LLM 应用的设计指南。这是一份为打造生产级大模型应用而编写的设计指南。作者在与多位 AI 领域优秀创始人交流后，提炼出 12 条系统化、切实可行的设计原则。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/957658915.png' style="max-width:80%; max-height=80%;"></img></p>

36、[60s](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vikiboss/60s)：每日 60 秒资讯 API 集合。该项目集合了包括每日新闻、实时票房、汇率、热搜榜、随机段子等多种数据的 API 服务。

37、[bitwise-challenge-2048](https://hellogithub.com/periodical/statistics/click?target=https://github.com/izabera/bitwise-challenge-2048)：基于位运算的 2048 游戏。这是一个通过位运算实现了经典的 2048 游戏，仅一个文件（.bash）、零依赖、不到 200 行代码。与常见的二维数组模拟棋盘方式不同，该项目巧妙地利用位运算管理游戏状态和逻辑，将整个 4x4 棋盘压缩存储在一个 64 位整数中，所有移动、合并和生成均通过位操作实现。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1004964759.png' style="max-width:80%; max-height=80%;"></img></p>

38、[CSS-Minecraft](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BenjaminAster/CSS-Minecraft)：这个“世界”只有 HTML 和 CSS。该项仅用 CSS 和 HTML 实现了类似《我的世界》（Minecraft）的界面交互，没用一行 JavaScript 代码，支持方块的放置、移除、切换视角等基础操作。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/562157524.png' style="max-width:80%; max-height=80%;"></img></p>

39、[pomodoro](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Rukenshia/pomodoro)：自制电子墨水屏番茄时钟。这是一个基于 ESP32 的实体番茄钟计时器，配备 4.26 英寸黑白 ePaper 屏幕和旋钮式操作。通过旋转旋钮可快速设定工作和休息时长，按下旋钮即可立即开始计时。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/956984646.png' style="max-width:80%; max-height=80%;"></img></p>

40、[scriptcat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/scriptscat/scriptcat)：可执行用户脚本的浏览器插件。这是一款开源的浏览器插件，支持用户安装和运行第三方的 JavaScript 代码片段，可用于屏蔽广告、增强网站功能、自动化网页操作等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/327265659.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
41、[book](https://hellogithub.com/periodical/statistics/click?target=https://github.com/crypto101/book)：《Crypto 101》密码学入门。这是一本面向程序员的密码学入门书籍，从 XOR 和一次性密码本开始，循序渐进地讲解对称加密、公钥加密、哈希、MAC、签名、密钥交换、随机数等密码学“积木”，并把它们组装成 TLS、OpenPGP、OTR 等真实系统。

42、[ThinkStats](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AllenDowney/ThinkStats)：《Think Stats》统计思维。这是一本写给程序员的统计学电子书，所有代码示例和练习均以 Python 实现。全书围绕真实数据集展开，通过探索性数据分析、概率分布、假设检验、相关性与回归分析等统计方法，用统计思维解决实际问题。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/815214314.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub111.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub113.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/112'>这里</a>。
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
