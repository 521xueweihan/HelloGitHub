# 《HelloGitHub》第 102 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/102) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[Ditto](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sabrogden/Ditto)：Windows 的剪贴板历史管理工具。这是一款免费的 Windows 剪贴板增强工具。它能够将复制到剪贴板的内容存储到数据库中（SQLite），方便日后检索，支持设定保存日期、条目总数、合并粘贴、分组、快速搜索和热键粘贴等功能。此外，还可以通过网络共享剪贴板内容，并对传输数据进行加密保护。来自 [@Veeja Liu](https://hellogithub.com/user/70zTMbIqVf9dvZp) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/312430210.png' style="max-width:80%; max-height=80%;"></img></p>

2、[FlappyBird](https://hellogithub.com/periodical/statistics/click?target=https://github.com/VadimBoev/FlappyBird)：仅 100KB 的像素鸟游戏。该项目是用 C 语言编写的飞翔的小鸟游戏（Flappy Bird），它运行流畅、安装包不到 100KB，适用于 Android 5.1 及以上系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/857252347.png' style="max-width:80%; max-height=80%;"></img></p>

3、[system-bus-radio](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fulldecent/system-bus-radio)：用电脑轻松发射无线电信号。该项目通过控制计算机系统总线在特定频率上切换电流，实现了无需额外硬件设备，仅用电脑发送 AM 无线电信号的功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/52827329.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
4、[eShop](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dotnet/eShop)：开源的 .NET 电商平台。该项目是由 .NET 官方开源的电子商务平台，基于 .NET Aspire 构建。作为示例项目，它采用最新的 .NET 8 和微服务架构，并实现了核心的电商功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/706944893.png' style="max-width:80%; max-height=80%;"></img></p>

5、[Loaf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DinoChan/Loaf)：假装 Windows 更新的工具。这是一款专为摸鱼设计的小工具。点击“摸鱼”按钮后，它会显示 Windows Update 界面，营造电脑正在升级的假象，让你能够名正言顺地摸鱼。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/432108375.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
6、[alien](https://hellogithub.com/periodical/statistics/click?target=https://github.com/chrxh/alien)：强大的人工生命模拟工具。该项目是基于 CUDA 的 2D 粒子引擎构建的人工生命模拟工具。它提供了图形化用户界面和粒子编辑器，能够轻松模拟软体、流体、数字生物体、遗传和进化等过程。生物行为由神经网络控制，支持实时交互和模拟百万量级的粒子。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/305438235.jpg' style="max-width:80%; max-height=80%;"></img></p>

7、[vcmi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vcmi/vcmi)：《英雄无敌 III》的开源重制版。该项目是经典策略游戏《魔法门之英雄无敌 III》的开源重制版，它采用 C++ 重新编写了游戏引擎，支持更高的分辨率、多人游戏和自定义地图等功能，可以在 Windows、macOS、Android 和 iOS 等系统上运行，但需要自行准备启动游戏所需的数据文件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/18490421.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[clickhouse-sql-parser](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AfterShip/clickhouse-sql-parser)：纯 Go 实现的 ClickHouse SQL 解析器。这是一款用 Go 实现的 ClickHouse SQL 解析器，兼容大多数 DML/DDL/Query 语句。它的代码简洁易懂，可作为 Go 开发者学习 SQL 解析器的入门项目。
```go
package main

import (
    clickhouse "github.com/AfterShip/clickhouse-sql-parser/parser"
)

query := "SELECT * FROM clickhouse"
parser := clickhouse.NewParser(query)
// Parse query into AST
statements, err := parser.ParseStmts()
if err != nil {
    return nil, err
}
```

9、[go2rtc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AlexxIT/go2rtc)：支持各种流媒体协议的处理工具。这是一个用 Go 语言编写的库，支持 RTSP、WebRTC、HomeKit、FFmpeg、RTMP 等视频流协议的处理。在 FFMPEG 的加持下，它几乎能将任何媒体格式作为输入源，转换为适用于主流流媒体服务和浏览器的格式。来自 [@猎隼丶止戈reNo7](https://hellogithub.com/user/Ew59HqRWjPe0zZO) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/526081371.png' style="max-width:80%; max-height=80%;"></img></p>

10、[maroto](https://hellogithub.com/periodical/statistics/click?target=https://github.com/johnfercher/maroto)：用 Go 生成样式美观的 PDF 文件。这一个 Go 语言开发的用于创建 PDF 文件的库，其灵感来源于 Bootstrap 框架。它允许你像使用 Bootstrap 创建网站一样，轻松编写和生成不同样式的 PDF 文件。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/187727138.png' style="max-width:80%; max-height=80%;"></img></p>

11、[nginx-ui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/0xJacky/nginx-ui)：全新的 Nginx 在线管理平台。该项目是用 Go+Vue.js 构建的 Nginx 在线管理平台，它开箱即用、功能丰富，支持流量统计、在线查看 Nginx 日志、编辑 Nginx 配置文件、自动检查和重载配置文件等功能。来自 [@kekylin](https://hellogithub.com/user/ux7SYGoKUMv461E) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/340339997.png' style="max-width:80%; max-height=80%;"></img></p>

12、[watchtower](https://hellogithub.com/periodical/statistics/click?target=https://github.com/containrrr/watchtower)：自动更新 Docker 容器的工具。该项目能够自动监测并更新正在运行的 Docker 容器。它会定期检查并拉取 Docker Hub 或私有镜像仓库中的最新镜像版本，并自动重启容器。适用于开发、测试和个人使用场景，但不建议在生产环境中使用。
```
docker run -d \
--name watchtower \
-v /var/run/docker.sock:/var/run/docker.sock \
containrrr/watchtower
```

### Java 项目
13、[graphhopper](https://hellogithub.com/periodical/statistics/click?target=https://github.com/graphhopper/graphhopper)：高效灵活的开源路线规划引擎。该项目是用 Java 开发的高性能路径规划引擎，能够快速计算两点或多点之间的距离。它支持 Dijkstra、A* 和收缩层级（CH）等算法，可以作为 Java 库或 Web 服务使用。基于 OpenStreetMap 地图数据，可实现汽车、自行车、步行等多种交通方式的路线规划和导航服务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/3480666.png' style="max-width:80%; max-height=80%;"></img></p>

14、[J2ME-Loader](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nikita36078/J2ME-Loader)：在 Android 上玩 J2ME 游戏。这是一款 Android 的 J2ME 模拟器，支持大多数 2D 和 3D 游戏。它内置虚拟键盘，适用于 Android 4.0+ 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/91971028.png' style="max-width:80%; max-height=80%;"></img></p>

15、[spring-ai](https://hellogithub.com/periodical/statistics/click?target=https://github.com/spring-projects/spring-ai)：帮助开发 AI 应用的 Spring 框架。这是由 Spring 官方开源的用于简化包含 AI 功能的应用开发的 Java 框架，它可以轻松接入 OpenAI、Microsoft、Amazon、Google 和 Huggingface 等主流模型供应商，以及聊天、文本生成图像的模型类型，支持提示工程、AI 模型转 POJO 对象、矢量数据库、RAG（检索增强生成）等有助于开发 AI 应用的功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/659402878.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
16、[create-t3-app](https://hellogithub.com/periodical/statistics/click?target=https://github.com/t3-oss/create-t3-app)：创建全栈、类型安全的 Next.js 项目的工具。这是一个用于创建全栈且类型安全的 Next.js 项目的脚手架工具。它开箱即用，仅需一条命令就能快速创建一个全新的 Next.js 项目。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/495836457.png' style="max-width:80%; max-height=80%;"></img></p>

17、[markmap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/markmap/markmap)：将 Markdown 可视化为思维导图。这是一个支持使用 Markdown 语法绘制思维导图的工具。它开箱即用并提供多种使用方式，包括在线、命令行以及 VSCode、Vim 和 Emacs 插件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/233568787.png' style="max-width:80%; max-height=80%;"></img></p>

18、[pglite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/electric-sql/pglite)：在浏览器中运行 Postgres 数据库。该项目将 PostgreSQL 数据库编译成 WebAssembly (WASM)，并打包成一个 TypeScript/JavaScript 客户端库。它压缩后体积不到 3MB，可以在浏览器、Node.js、Bun 和 Deno 环境中运行，无需安装任何额外的依赖。提供灵活的存储选项，支持内存存储、本地持久化或 IndexedDB。
```typescript
import { PGlite } from "@electric-sql/pglite";

const db = new PGlite();
await db.query("select 'Hello world' as message;");
// -> { rows: [ { message: "Hello world" } ] }
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/759893102.png' style="max-width:80%; max-height=80%;"></img></p>

19、[staticrypt](https://hellogithub.com/periodical/statistics/click?target=https://github.com/robinmoisson/staticrypt)：为静态网站提供密码保护功能。该项目无需服务器端支持，即可实现对 HTML 页面进行密码认证访问的功能。它使用 AES-256 加密算法和设定的密码，对需要保护的页面进行加密。生成的页面包含密码输入框，只有在输入正确的密码后，才会显示原始的 HTML 页面内容。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/89785877.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[ui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shadcn-ui/ui)：流行、设计精美的 UI 组件集合。这是一款由 Vercel 开源、基于 React 开发的 UI 组件集合，包括仪表板、卡片、模型对话、表单、登录等组件，拿来即用。通过 CLI 引入组件后，将得到该组件的源码，可随意修改和定制。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/585146387.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
21、[game2048](https://hellogithub.com/periodical/statistics/click?target=https://github.com/andstatus/game2048)：开源的 2048 游戏。该项目是基于 Kotlin 和 KorGe 游戏引擎开发的 2048 游戏。它免费、开源且没广告，支持存档、无限撤回、AI 模式和回放等功能。作者仅提供了 Android 安装包，其他平台需要自行编译。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/299049641.png' style="max-width:80%; max-height=80%;"></img></p>

22、[ImageToolbox](https://hellogithub.com/periodical/statistics/click?target=https://github.com/T8RIN/ImageToolbox)：Android 的多功能图像编辑工具。这是一款专为 Android 设计的图像编辑工具。它完全免费，支持批量处理、滤镜、背景移除、尺寸调整和裁剪等多种功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/478710402.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
23、[aiofiles](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Tinche/aiofiles)：Python 异步文件处理库。在 Python 中，传统的文件 I/O 是阻塞的，该项目提供了异步（非阻塞）的文件操作。它的 API 与 Python 标准库相似，支持 async/await 语法。
```python
async with aiofiles.open('filename', mode='r') as f:
    contents = await f.read()
print(contents)
'My file contents'
```

24、[cupy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cupy/cupy)：GPU 版的 NumPy 和 SciPy。这是一个利用 GPU 加速数值计算的 Python 库，与 NumPy 和 SciPy 兼容。你可以轻松地将现有的 NumPy/SciPy 代码，迁移到 NVIDIA CUDA 或 AMD ROCm 平台上运行，部分情况下速度可提升 100 倍以上。
```python
>>> import cupy as cp
>>> x = cp.arange(6).reshape(2, 3).astype('f')
>>> x
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.]], dtype=float32)
>>> x.sum(axis=1)
array([  3.,  12.], dtype=float32)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/72523920.png' style="max-width:80%; max-height=80%;"></img></p>

25、[curl_cffi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lexiforest/curl_cffi)：模拟浏览器指纹的 HTTP 客户端。这是一个用 Python 写的 HTTP 客户端库，可以模拟浏览器 TLS、JA3 和 HTTP/2 指纹。它开箱即用、速度快，并且支持 WebSocket 和异步。
```python
from curl_cffi import requests

# Notice the impersonate parameter
r = requests.get("https://tools.scrapfly.io/api/fp/ja3", impersonate="chrome")

print(r.json())
# output: {..., "ja3n_hash": "aa56c057ad164ec4fdcb7a5a283be9fc", ...}
# the js3n fingerprint should be the same as target browser

# To keep using the latest browser version as `curl_cffi` updates,
# simply set impersonate="chrome" without specifying a version.
# Other similar values are: "safari" and "safari_ios"
r = requests.get("https://tools.scrapfly.io/api/fp/ja3", impersonate="chrome")
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/468168223.png' style="max-width:80%; max-height=80%;"></img></p>

26、[LibreTranslate](https://hellogithub.com/periodical/statistics/click?target=https://github.com/LibreTranslate/LibreTranslate)：可离线部署的翻译 API 服务。该项目是基于离线翻译引擎 Argos Translate 构建的翻译 API 服务。它不依赖第三方翻译服务，可轻松自建翻译 API 服务，支持自动语言检测、API 密钥和访问频率限制等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/322921248.png' style="max-width:80%; max-height=80%;"></img></p>

27、[s-tui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/amanusk/s-tui)：基于终端的 CPU 监控和压测工具。这是一个 Python 写的命令行工具，可在终端中以图形方式实时显示 CPU 温度、频率、功率和利用率等信息。它还支持安装 FIRESTARTER 等工具，对 CPU 进行压力测试。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/87705200.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
28、[uv](https://hellogithub.com/periodical/statistics/click?target=https://github.com/astral-sh/uv)：超快的 Python 包管理工具。该项目是基于 Rust 开发的下一代 Python 包管理工具，可用于替代传统的 Python 包和环境管理工具。它兼容 pip、pip-tools 和 virtualenv 命令，速度比这些工具快 10-100 倍，并通过全局依赖缓存节省更多的硬盘空间，开箱即用支持 Windows、Linux 和 macOS 系统。
```
# On macOS and Linux.
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
$ powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
$ pip install uv
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/699532645.png' style="max-width:80%; max-height=80%;"></img></p>

29、[yazi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sxyazi/yazi)：超快的终端文件管理器。这是一个用 Rust 编写的终端文件管理器，所有 I/O 操作均为异步。它提供了友好的界面、自由可定制和流畅的使用体验，支持图片预览、代码高亮、滚动预览和插件系统，并集成了 ripgrep、fd、fzf 等高效的命令行工具。来自 [@fortystory](https://hellogithub.com/user/pnOrTEBk9I1QKx5) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/663900193.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
30、[BBackupp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Lakr233/BBackupp)：轻松备份 iOS 设备数据的工具。这是一款免费的 iOS 备份工具，支持显示备份进度、自动备份计划、无线备份、加密保护等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/677801474.png' style="max-width:80%; max-height=80%;"></img></p>

31、[OpenScanner](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pencilresearch/OpenScanner)：适用于 iPhone 的免费文档扫描工具。这是一款用 Swift 编写的文档扫描工具，完全免费，没广告且无内购。它可以扫描收据、合同、笔记等，支持自动识别文本、编辑扫描件、签名和导出 PDF 文件等功能，适用于 iOS 16.0+ 和 visionOS 1.2+ 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/858437661.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
32、[miniMNIST-c](https://hellogithub.com/periodical/statistics/click?target=https://github.com/konrad-gajdus/miniMNIST-c)：C 语言实现的极简神经网络。该项目展示了如何用 C 语言从头实现一个最小的神经网络。它用不到 200 行代码和 C 标准库，实现了一个极简的神经网络，能够对 MNIST 数据集中的手写数字进行分类。

33、[openvino](https://hellogithub.com/periodical/statistics/click?target=https://github.com/openvinotoolkit/openvino)：优化和部署深度学习模型的工具包。该项目是英特尔开源的工具库，旨在加速和优化深度学习模型部署。它能帮助开发者将训练好的模型部署到多种硬件平台，支持 TensorFlow、PyTorch 和 ONNX 等深度学习框架。
```python
import openvino as ov
import torch
import torchvision

# load PyTorch model into memory
model = torch.hub.load("pytorch/vision", "shufflenet_v2_x1_0", weights="DEFAULT")

# convert the model into OpenVINO model
example = torch.randn(1, 3, 224, 224)
ov_model = ov.convert_model(model, example_input=(example,))

# compile the model for CPU device
core = ov.Core()
compiled_model = core.compile_model(ov_model, 'CPU')

# infer the model on random data
output = compiled_model({0: example.numpy()})
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/153097643.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
34、[90DaysOfDevOps](https://hellogithub.com/periodical/statistics/click?target=https://github.com/MichaelCade/90DaysOfDevOps)：为期 90 天的 DevOps 免费教程。该项目最初是作者记录自己学习 DevOps 知识的笔记，如今已发展为一个由社区驱动的 DevOps 免费教程，内容涵盖了 DevOps 概念、Linux 基础、计算机网络、容器、Kubernetes、CI/CD、监控和云服务商等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/441903012.png' style="max-width:80%; max-height=80%;"></img></p>

35、[Atlas](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Atlas-OS/Atlas)：开源的精简版 Windows 操作系统。这是一个经过优化的 Windows 操作系统，移除了许多用不到但会拖慢系统的组件。瘦身后减少了系统进程数、网络和内存占用，获得了更快的启动速度和更流畅的操作体验。该系统能够正常运行各种 Windows 软件和游戏，是一份送给游戏爱好者和追求高性能用户的开源礼物。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/336920522.png' style="max-width:80%; max-height=80%;"></img></p>

36、[GPU-Puzzles](https://hellogithub.com/periodical/statistics/click?target=https://github.com/srush/GPU-Puzzles)：学习 GPU 并行编程的互动式教程。该项目提供了 14 道题，帮助学习 GPU 编程。你需要编写代码来解决这些问题。尽管代码看起来像 Python，但实际上是使用 numba 库编写 CUDA 代码。更有趣的是，运行代码后会生成一张示意图，帮助你理解代码运行过程。此外，作者还制作了讲解视频，指导如何运行项目并查看答案。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/512867291.png' style="max-width:80%; max-height=80%;"></img></p>

37、[kando](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kando-menu/kando)：跨平台的环形状菜单工具。这是一款桌面圆形菜单（Pie menu）工具，可用于启动应用、模拟键盘快捷键、打开文件等，尤其适合与触控笔和触摸屏配合使用，支持 Windows、Linux 和 macOS 等系统。来自 [@有故事的徐同学](https://hellogithub.com/user/dsBIQo8K4UaFPR2) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/628600520.gif' style="max-width:80%; max-height=80%;"></img></p>

38、[omakub](https://hellogithub.com/periodical/statistics/click?target=https://github.com/basecamp/omakub)：精美的 Ubuntu 配置方案。该项目可以将全新的 Ubuntu 24.04 系统配置成美观、功能齐全、适合 Web 开发的系统。只需简单的一条命令，即可拥有配置好的 GNOME 桌面环境、窗口管理工具、Alacritty 终端、Neovim 和 VSCode 编辑器等应用，还会将 Chrome 设置成默认浏览器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/805916722.png' style="max-width:80%; max-height=80%;"></img></p>

39、[weather_landscape](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lds133/weather_landscape)：用有趣的动画显示天气预报。这是一个基于气象数据生成景观图的项目，通过动画形式生动地展现天气，替代了枯燥的气象数值显示。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/102/860493834.jpg' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
40、[DictionaryByGPT4](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Ceelog/DictionaryByGPT4)：用 GPT-4 生成的英语单词书。该项目通过 GPT-4 分析中考、高考、及四六级考试中的 8000 多个英语单词，生成了一本英语词汇书。书中详细介绍了每个单词的词义、词根、词缀、例句，以及发展历史和文化背景等。

41、[SystemDesign](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Admol/SystemDesign)：《System Design Interview: An Insider’s Guide》中文翻译。该项目是《系统设计面试：内幕指南》一书的中文翻译，内容是传授面试中关于系统设计架构的技巧，例如如何设计一个 YouTube 等系统。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub101.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub103.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/102'>这里</a>。
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
