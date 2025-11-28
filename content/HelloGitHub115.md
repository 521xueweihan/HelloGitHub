# 《HelloGitHub》第 115 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/115) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[iotop](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Tomas-M/iotop)：终端下的 IO 资源监控工具。这是一款用于监控 Linux 系统 I/O 的命令行工具，拥有类似 top 命令的交互界面和操作方式，支持实时按 I/O 使用率对进程进行排序和展示。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/23103328.png' style="max-width:80%; max-height=80%;"></img></p>

2、[libsodium](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jedisct1/libsodium)：开箱即用的 C 语言加密库。这是一个现代易用、跨平台的 C 语言加密库，为开发者提供全面的加密操作 API。它集成了多种加密、签名和哈希算法，适用于安全通信、数据保护等场景。来自 [@沐怡旸](https://hellogithub.com/user/76dhrs54nQGLuge) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/7710647.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[DepotDownloader](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SteamRE/DepotDownloader)：Steam 游戏资源命令行下载工具。这是一款用于从 Steam 平台批量下载指定内容的命令行工具，无需安装 Steam 客户端。用户可通过命令行直接下载指定游戏或应用的文件，支持仓库标识（depot）、清单（manifest）等参数，轻松获取任意版本的游戏文件。

4、[PKHeX](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kwsch/PKHeX)：宝可梦存档编辑工具。这是一款开源的宝可梦存档编辑器，支持多种宝可梦游戏存档文件的读取与编辑。用户可自由修改宝可梦属性、技能、道具、图鉴完成度等信息，并内置存档合法性验证功能，确保修改后的存档安全可用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/21311240.png' style="max-width:80%; max-height=80%;"></img></p>

5、[SlideSCI](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Achuan-2/SlideSCI)：开源的 PPT 编辑插件。这是一款专为提升 PPT 编辑效率的插件，支持一键添加图片标题、自动对齐、复制/粘贴图片位置，以及插入 Markdown 文本和 LaTeX 数学公式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/914468340.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
6、[chrome_plus](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Bush2021/chrome_plus)：开箱即用的 Chrome 增强工具。这是一款基于 DLL 劫持技术的 Chrome 浏览器增强工具，支持双击或右键关闭标签、鼠标悬停标签栏时滚轮切换、强制保留最后一个标签防止浏览器意外关闭，以及自定义老板键快速隐藏窗口等功能。兼容所有 Chromium 内核浏览器，只需将 DLL 文件放入浏览器目录即可使用。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

7、[quill](https://hellogithub.com/periodical/statistics/click?target=https://github.com/odygrd/quill)：低延迟的异步 C++ 日志库。这是一款高性能异步 C++ 日志库，专为低延迟、性能敏感型应用设计。它通过将日志格式化与 I/O 操作交由后台线程处理，减少对主线程的性能影响，适用于高频交易、游戏引擎等场景。来自 [@沐怡旸](https://hellogithub.com/user/76dhrs54nQGLuge) 的分享
```c++
int main()
{
  quill::Backend::start();

  quill::Logger* logger = quill::Frontend::create_or_get_logger(
    "root", quill::Frontend::create_or_get_sink<quill::ConsoleSink>("sink_id_1"));

  LOG_INFO(logger, "Hello from {}!", std::string_view{"Quill"});
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/234192998.gif' style="max-width:80%; max-height=80%;"></img></p>

8、[Vita3K](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Vita3K/Vita3K)：开源的 PSV 游戏模拟器。这是一款实验性的 PS Vita 模拟器，支持 Windows、Linux、macOS 和 Android 平台，能够运行大多数 PSV 游戏和自制程序。目前已成功运行《女神异闻录 4：黄金版》等热门游戏，并提供详细的游戏兼容性列表。项目正处于活跃开发阶段，尽管可能存在崩溃或卡顿等问题，但整体体验已相当出色。来自 [@天涯孤雁](https://hellogithub.com/user/gf67BzSc528eYP9) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/119111364.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
9、[Ech0](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lin-snow/Ech0)：清爽的轻量级内容分享平台。这是一款开源、自托管的轻量级内容发布平台，专注于思想流动和快速分享。它拥有简洁直观的操作界面，支持发布和分享想法、文字、图片和链接。同时，支持类似 ActivityPub 的联邦协议，实现不同实例（站点）之间的互联互通，让内容不再局限于单一孤立的网站。来自 [@L1nSn0w](https://hellogithub.com/user/fdQ7xwPoCGy2UKD) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/952272279.png' style="max-width:80%; max-height=80%;"></img></p>

10、[eget](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zyedidia/eget)：一键获取 GitHub Release 安装包。这是一个用 Go 编写的命令行工具，可自动从 GitHub 检索、下载并安装开源项目已发布的二进制文件（Releases），无需手动查找和下载安装包。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/397091905.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[HAMi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Project-HAMi/HAMi)：面向 K8s 的异构 AI 计算虚拟化中间件。这是一款专为异构计算环境打造的 GPU 共享与调度管理平台，致力于最大化提升 GPU 利用率。它提供灵活、可靠、按需和弹性的多元异构 GPU 虚拟化、调度与管理能力，支持包括 NVIDIA、Ascend 等主流厂商的多种硬件及虚拟化技术，适用于深度学习、数据处理、科学计算等高性能计算场景。来自 [@ysq](https://hellogithub.com/user/JaYG07AHXmhzIQn) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/406346103.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[allure2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/allure-framework/allure2)：灵活的测试报告生成工具。这是一款基于 Java 开发的测试报告工具，支持多种编程语言和测试框架，能够生成统一、详细的测试报告，涵盖测试结果明细、测试用例执行情况、测试覆盖率等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/59838788.jpg' style="max-width:80%; max-height=80%;"></img></p>

13、[strimzi-kafka-operator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/strimzi/strimzi-kafka-operator)：在 K8s 上轻松部署 Kafka 集群。该项目能够帮助开发者在 K8s 或 OpenShift 上轻松部署和管理 Apache Kafka 集群，简化了 Kafka 集群的安装、配置、升级、扩展和监控等流程。

### JavaScript 项目
14、[chronoframe](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HoshinoSuzumi/chronoframe)：极简的个人云相册平台。这是一款功能强大的自托管个人相册应用，专为展示与分享个人摄影作品而设计。它提供简洁易用的 Web 界面，可轻松管理和浏览照片，支持 Live Photo 与 Motion Photo 格式，并具备 EXIF 信息解析、地理位置识别和地图探索等功能。来自 [@星野鈴美](https://hellogithub.com/user/kLVoiAFPJaBtr1D) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1042231422.png' style="max-width:80%; max-height=80%;"></img></p>

15、[OpenStock](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Open-Dev-Society/OpenStock)：免费炫酷的股票市场应用。这是一款基于 Next.js、TailwindCSS 和 MongoDB 构建的股票市场平台，提供实时行情、图表（K 线图、热力图）、新闻资讯和个性化监控等功能，专注于数据展示与分析，不支持交易。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1065936302.png' style="max-width:80%; max-height=80%;"></img></p>

16、[pages-cms](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pages-cms/pages-cms)：专为静态网站打造的 CMS。这是一个专为静态网站生成器设计的内容管理系统（CMS），支持 Jekyll、Next.js、VuePress 和 Hugo 等。它提供友好的用户界面，让非技术人员也能轻松编辑和更新网站内容，所有更改将自动转化为 GitHub 上的提交。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/732374797.png' style="max-width:80%; max-height=80%;"></img></p>

17、[twake-drive-legacy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/linagora/twake-drive-legacy)：免费开源的 Google Drive 替代品。这是一款基于 Node.js 和 MongoDB 构建的云存储平台，提供类似 Google Drive 的文件管理和存储功能，支持 Docker 一键部署。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/617880579.png' style="max-width:80%; max-height=80%;"></img></p>

18、[zustand](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pmndrs/zustand)：让 React 状态管理更轻松。这是一款轻量、快速、易扩展的 React 状态管理库，为开发者提供简洁且高效的状态管理体验。它拥有简洁的 API，支持直接定义和使用状态，并通过自定义 Hooks 来管理状态，帮你远离传统状态管理方案的繁琐与陷阱。
```typescript
import { create } from 'zustand'

type Store = {
  count: number
  inc: () => void
}

const useStore = create<Store>()((set) => ({
  count: 1,
  inc: () => set((state) => ({ count: state.count + 1 })),
}))

function Counter() {
  const { count, inc } = useStore()
  return (
    <div>
      <span>{count}</span>
      <button onClick={inc}>one up</button>
    </div>
  )
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/180328715.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
19、[local-dream](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xororz/local-dream)：在 Android 设备上运行 Stable Diffusion。这是一款专为 Android 用户打造的本地 Stable Diffusion AI 绘画应用，完全离线运行，兼容高通骁龙 NPU、CPU 和 GPU，支持文生图、图生图和图片修复等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/922050275.jpg' style="max-width:80%; max-height=80%;"></img></p>

20、[Voice-Recorder](https://hellogithub.com/periodical/statistics/click?target=https://github.com/FossifyOrg/Voice-Recorder)：极简的 Android 语音录音应用。这是一款极简易用的 Android 语音录音应用，支持离线录音、无广告、界面清爽，适用于会议记录、课堂笔记、采访、日常备忘等场景。来自 [@ewiro](https://hellogithub.com/user/iItGgWoJjnLsr0Y) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/595828370.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
21、[checkov](https://hellogithub.com/periodical/statistics/click?target=https://github.com/bridgecrewio/checkov)：开源的 IaC 静态代码分析工具。这是一款基础设施即代码（IaC）的静态代码分析工具，旨在帮助开发者在构建阶段及时发现和防止云基础设施配置错误及安全漏洞。支持对 AWS、Azure、GCP、Kubernetes 等多种云平台的 IaC 文件（如 Terraform、CloudFormation、Kubernetes YAML 等）进行静态检测，同时可分析容器镜像和开源依赖包中的安全风险。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/224386599.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[docling](https://hellogithub.com/periodical/statistics/click?target=https://github.com/docling-project/docling)：多格式文档解析和导出工具。这是一个由 IBM 开源的 Python 工具，专门用于将各类文档转化为适合生成式 AI 使用的格式。它能够将 PDF、DOCX、PPTX、图片、HTML、Markdown 等多种流行文档格式，导出为 Markdown 和 JSON 格式，支持多种 OCR 引擎（PDF）、统一的文档对象（DoclingDocument），轻松集成检索增强生成（RAG）和问答应用，适用于需要将文档作为生成式 AI 模型输入的场景。
```python
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # PDF path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "### Docling Technical Report[...]"
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/826168160.png' style="max-width:80%; max-height=80%;"></img></p>

23、[gpu-hot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/psalias2006/gpu-hot)：实时的 NVIDIA GPU 网页监控面板。这是一个基于 FastAPI 开发的实时 NVIDIA GPU 监控仪表盘，支持利用率、内存、温度、功耗、风扇转速等多项 GPU 指标。它通过 WebSocket 实时推送数据，支持多 GPU、单机和 GPU 集群环境，并可通过 Docker 一键部署。来自 [@wanzij](https://hellogithub.com/user/QkXB6ugmwMTqteF) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1070160746.png' style="max-width:80%; max-height=80%;"></img></p>

24、[PyQt-Frameless-Window](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zhiyiYo/PyQt-Frameless-Window)：基于 PyQt5 的跨平台无边框窗口。该项目是基于 PyQt/PySide 的跨平台无边框窗口组件，在实现无边框窗口效果的同时，保留窗口的基本功能，兼容 Windows、Linux 和 macOS，并支持 Acrylic、Mica 等窗口特效。
```python
import sys

from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow


class Window(FramelessWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("PyQt-Frameless-Window")
        self.titleBar.raise_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/347549476.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[quark-auto-save](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Cp0204/quark-auto-save)：夸克网盘自动转存工具。这是一款基于 Python 开发的夸克网盘自动化工具，支持网盘签到、自动转存、文件命名整理、推送提醒和自动刷新 Emby 媒体库等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/735799919.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
26、[touchHLE](https://hellogithub.com/periodical/statistics/click?target=https://github.com/touchHLE/touchHLE)：让经典 iPhone 游戏在现代设备上重获新生。该项目是用 Rust 开发的 iOS 游戏模拟器，可运行 iPhone OS 2.x 和 3.x 等早期版本的 iOS 游戏。它采用高级模拟（HLE）技术，通过实现 UIKit、OpenGL ES 等原生框架来运行应用，而非直接模拟底层硬件，支持 Windows、macOS 和 Android 平台。来自 [@kero990](https://hellogithub.com/user/c3Y4NR1rq6neVoD) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/573107980.png' style="max-width:80%; max-height=80%;"></img></p>

27、[yaak](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mountain-loop/yaak)：离线优先的桌面 API 客户端。这是一款快速、离线优先的桌面 API 客户端，支持 REST、GraphQL、SSE、WebSocket 和 gRPC 协议。它基于 Rust、Tauri 和 React 构建，界面友好、跨平台可用，无遥测和云端锁定，提供简洁纯粹、不受干扰的使用体验。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/602379707.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
28、[bitchat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/permissionlesstech/bitchat)：基于蓝牙的即时通信应用。这是一款无需服务器的蓝牙即时通讯应用，专为无网络环境设计。它通过结合蓝牙 Mesh 和 Nostr 协议，实现端到端加密的点对点通信，支持消息重试、离线转发、多用户、自动发现等功能，适用于救灾志愿者、野外探险队等小范围即时沟通场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1013830656.jpg' style="max-width:80%; max-height=80%;"></img></p>

29、[Dayflow](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JerryZLiu/Dayflow)：自动生成每日时间线的 macOS 应用。这是一款用 Swift 开发的 macOS 应用，通过录制屏幕活动并结合 AI，自动生成每日时间线。它以每秒 1 帧的频率录制屏幕，每 15 分钟利用 AI 分析录像内容，生成简洁的活动总结。同时，自动删除超过 3 天的录制文件，节省存储空间。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1062234789.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
30、[BrowserOS](https://hellogithub.com/periodical/statistics/click?target=https://github.com/browseros-ai/BrowserOS)：开源的 AI 浏览器。该项目是基于 Chromium 的开源 AI 浏览器，能够在本地浏览器中运行 AI Agents，可作为 ChatGPT Atlas、Perplexity Comet 和 Dia 的开源替代方案。在保留 Chrome 熟悉界面与扩展兼容性的同时，帮助用户实现 AI 驱动的浏览器自动化与智能问答任务，并支持自定义 LLM 服务或本地大模型。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/985839104.gif' style="max-width:80%; max-height=80%;"></img></p>

31、[cache-dit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vipshop/cache-dit)：免训练的 DiT 模型缓存加速框架。该项目是为 Diffusers 提供统一缓存加速的框架，支持几乎所有的 DiT 扩散模型，包括 Qwen-Image-Lightning、Qwen-Image、HunyuanImage、Wan、FLUX 等。它通过简单的代码即可实现高效的缓存加速功能，无需重新训练模型即可显著提升推理速度。来自 [@DefTruth](https://hellogithub.com/user/ofSCbzTmdeQk3FD) 的分享
```python
import cache_dit
from diffusers import DiffusionPipeline
pipe = DiffusionPipeline.from_pretrained("Qwen/Qwen-Image") # Can be any diffusion pipeline
cache_dit.enable_cache(pipe) # One-line code with default cache options.
output = pipe(...) # Just call the pipe as normal.
stats = cache_dit.summary(pipe) # Then, get the summary of cache acceleration stats.
cache_dit.disable_cache(pipe) # Disable cache and run original pipe.
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1000711946.png' style="max-width:80%; max-height=80%;"></img></p>

32、[graphiti](https://hellogithub.com/periodical/statistics/click?target=https://github.com/getzep/graphiti)：为 AI 智能体构建实时知识图谱。这是一个专为 AI 智能体设计的框架，用于构建和查询实时、具有时间感知能力的知识图谱。它能够持续集成用户交互、结构化或非结构化等动态数据，形成连贯且可查询的知识图谱。支持增量数据更新、高效检索和历史查询，适用于开发交互式、上下文感知的 AI 应用。来自 [@塔咖](https://hellogithub.com/user/bzJpGyu0IanC6L7) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/840056306.gif' style="max-width:80%; max-height=80%;"></img></p>

33、[LEANN](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yichuan-w/LEANN)：超低存储占用的向量数据库。这是一款开源的轻量级向量数据库，通过按需计算嵌入向量，实现极低的存储占用。用户可以在个人设备（笔记本电脑）上构建强大且完全私有的检索增强生成 (RAG) 系统，支持对本地文件、电子邮件、浏览器历史、聊天记录等多种数据源进行语义搜索。来自 [@Yichuan Wang](https://hellogithub.com/user/Tj5AEF9BDNXpKnk) 的分享
```python
from leann import LeannBuilder, LeannSearcher, LeannChat
from pathlib import Path
INDEX_PATH = str(Path("./").resolve() / "demo.leann")

# Build an index
builder = LeannBuilder(backend_name="hnsw")
builder.add_text("LEANN saves 97% storage compared to traditional vector databases.")
builder.add_text("Tung Tung Tung Sahur called—they need their banana‑crocodile hybrid back")
builder.build_index(INDEX_PATH)

# Search
searcher = LeannSearcher(INDEX_PATH)
results = searcher.search("fantastical AI-generated creatures", top_k=1)

# Chat with your data
chat = LeannChat(INDEX_PATH, llm_config={"type": "hf", "model": "Qwen/Qwen3-0.6B"})
response = chat.ask("How much storage does LEANN save?", top_k=1)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/998732712.png' style="max-width:80%; max-height=80%;"></img></p>

34、[surf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/deta/surf)：跨媒体的个人 AI 笔记应用。这是一款本地优先的 AI 笔记本工具，能够将多种媒体类型（如本地文件、网页、视频等）整合至本地资料库，并借助 AI 快速生成笔记。它帮助用户在学习和研究过程中，免去在浏览器、笔记应用、PDF 阅读器等多个应用和媒体之间切换、搜索和手动复制粘贴的繁琐操作，同时支持灵活选择 AI 模型。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1079906817.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
35、[anki-jlpt-decks](https://hellogithub.com/periodical/statistics/click?target=https://github.com/5mdld/anki-jlpt-decks)：万词语音全配的日语卡组。这是一个为学习软件 Anki 制作的高质量日语单词卡组，涵盖 JLPT（日本语能力测试）N1~N5 等级，共计一万词汇，每个词条都包含释义、例句、词性，以及关联词和反义词等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/902164245.png' style="max-width:80%; max-height=80%;"></img></p>

36、[Berkeley-Humanoid-Lite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)：开源的人形机器人。该项目是由伯克利 Hybrid Robotics 团队开源，旨在提供低成本、模块化、可定制的人形机器人解决方案。机器人采用 3D 打印和常见组件，整体成本在 5000 美元以内，适用于机器人科研、算法开发和教学实验等多个领域。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/950286225.png' style="max-width:80%; max-height=80%;"></img></p>

37、[document](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ranuts/document)：Office 文件在线编辑器。这是一个基于 OnlyOffice 和 WebAssembly 的本地 Web 文档编辑器，纯前端实现、无需服务器端处理，用户可直接在浏览器中打开和编辑 DOCX、XLSX、PPTX 等格式的文档。

38、[leetgpu-challenges](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AlphaGPU/leetgpu-challenges)：GPU 编程实战挑战。该项目提供了一系列类似 LeetCode 风格的 GPU 编程练习题，内含参考答案、测试用例和多种 GPU 编程框架的模板代码。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1022920558.png' style="max-width:80%; max-height=80%;"></img></p>

39、[NCE](https://hellogithub.com/periodical/statistics/click?target=https://github.com/iChochy/NCE)：《新概念英语》全四册在线课文朗读。该项目为《新概念英语》学习者提供了一个方便的在线学习平台，结合美式发音音频与 Gemini AI 生成的中文字幕，支持课文朗读与单句点读。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1063065062.png' style="max-width:80%; max-height=80%;"></img></p>

40、[pandoc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jgm/pandoc)：通用的标记语言转换工具。该项目能够将多种文档格式相互转换，支持 Markdown、HTML、LaTeX、Word、PDF、EPUB 等格式，广泛应用于写作、学术论文、出版等场景。来自 [@Xuefeng Xu](https://hellogithub.com/user/k4oyT8wSU5Qfx6H) 的分享

### 开源书籍
41、[agentic-design-patterns-cn](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ginobefun/agentic-design-patterns-cn)：《Agentic Design Patterns》中文翻译版。该项目是《Agentic Design Patterns》一书的中英文对照版，这本书系统性地介绍了构建现代 AI 智能体（Agent）的实践方法与设计模式，包括提示链、RAG、MCP 和多智能体协作等内容。



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub114.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub116.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/115'>这里</a>。
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
    </tr>
  </thead>
</table>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
