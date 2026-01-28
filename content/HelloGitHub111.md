# 《HelloGitHub》第 111 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/111) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[mimikatz](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gentilkiwi/mimikatz)：探索 Windows 安全机制的工具。这是一款采用 C 语言编写的用于研究 Windows 安全机制的工具。它能够从内存中提取明文密码、哈希值、PIN 码、Kerberos 票据等敏感信息，支持 pass-the-hash、Golden Ticket、DCSync 等高级操作，广泛应用于安全研究、渗透测试和系统安全分析等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/18496166.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
2、[AutoUpdater.NET](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ravibpatel/AutoUpdater.NET)：WPF 桌面应用自动升级组件。这是一个专为 WinForms 和 WPF 桌面应用设计的自动更新库。只需几行代码，即可为桌面应用轻松集成自动检测新版本、弹窗提示、下载安装包等功能。

3、[ExplorerTabUtility](https://hellogithub.com/periodical/statistics/click?target=https://github.com/w4po/ExplorerTabUtility)：Windows 文件管理多标签扩展工具。这是一款专为 Windows 11 打造的文件资源管理器增强工具，能够自动将多个窗口合并为单窗口多标签页模式。支持路径去重、标签搜索、批量打开/关闭/还原等功能，轻松告别桌面窗口杂乱的烦恼。来自 [@iKineticate](https://hellogithub.com/user/JCrYzT28cH9twxQ) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/722973124.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[defendnot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/es3n1n/defendnot)：一键关闭 Windows Defender 的工具。这是一款用于禁用 Windows Defender 的工具，支持一键安装和持久生效。它通过直接调用 Windows 安全中心（WSC）接口，注册虚拟杀毒软件，实现对系统自带的 Defender 实时防护服务的彻底禁用。同时，支持开机自启，确保重启后禁用状态依旧生效。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/979241345.png' style="max-width:80%; max-height=80%;"></img></p>

5、[OpenSpeedy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/game1024/OpenSpeedy)：开箱即用的游戏变速器。这是一款完全免费、开源的 Windows 游戏加速工具。它通过 Hook 系统时间函数，实现对游戏速度的灵活调节，并提供简单易用的界面，兼容多种单机游戏。请勿用于网络游戏，以免导致账号被封！来自 [@game1024](https://hellogithub.com/user/kmUCncHJr9SpNV7) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/984862298.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[USearch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/unum-cloud/USearch)：更快且小巧的向量检索与聚类引擎。这是一款高性能、轻量级的相似搜索和聚类引擎，单头文件设计，可嵌入主流数据库，支持向量和多模态数据（文本、图像、地理坐标）。它基于 HNSW 算法实现高效的近似最近邻搜索，兼容多种编程语言和精度类型，适用于推荐系统、向量数据库、智能检索、地理空间分析等场景。
```c++
#include <usearch/index.hpp>
#include <usearch/index_dense.hpp>

using namespace unum::usearch;

int main(int argc, char **argv) {
    metric_punned_t metric(3, metric_kind_t::l2sq_k, scalar_kind_t::f32_k);

    // If you plan to store more than 4 Billion entries - use `index_dense_big_t`.
    // Or directly instantiate the template variant you need - `index_dense_gt<vector_key_t, internal_id_t>`.
    index_dense_t index = index_dense_t::make(metric);
    float vec[3] = {0.1, 0.3, 0.2};

    index.reserve(10); // Pre-allocate memory for 10 vectors
    index.add(42, &vec[0]); // Pass a key and a vector
    auto results = index.search(&vec[0], 5); // Pass a query and limit number of results

    for (std::size_t i = 0; i != results.size(); ++i)
        // You can access the following properties of every match:
        // results[i].element.key, results[i].element.vector, results[i].distance;
        std::printf("Found matching key: %zu", results[i].member.key);
    return 0;
}
```

### Go 项目
7、[f2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ayoisaiah/f2)：跨平台的批量重命名工具。这是一款命令行批量重命名工具，完全用 Go 语言编写，支持正则表达式、自动解决冲突、撤销等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/259488212.png' style="max-width:80%; max-height=80%;"></img></p>

8、[logdy-core](https://hellogithub.com/periodical/statistics/click?target=https://github.com/logdyhq/logdy-core)：自带 Web 界面的实时日志查看工具。这是一款轻量级的实时日志查看工具，无需安装、开箱即用。它内置 Web 界面，可通过浏览器像 tail -f 一样实时查看与过滤日志，支持多种输入模式和自定义解析器。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享
```
# Use with any shell command
$ tail -f file.log | logdy
WebUI started, visit http://localhost:8080

# Read log files
$ logdy follow app-out.log --full-read
WebUI started, visit http://localhost:8080
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/747929369.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[OpenList](https://hellogithub.com/periodical/statistics/click?target=https://github.com/OpenListTeam/OpenList)：支持多种存储的文件列表程序。这是一个基于 Gin 和 SolidJS 的文件列表程序，支持本地存储、阿里云盘、OneDrive、Google Drive 等多种存储方式。它完全开源（fork 自 AList），由社区共同维护。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/1000524955.png' style="max-width:80%; max-height=80%;"></img></p>

10、[tldx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/brandonyoungdev/tldx)：一键查找可用域名的工具。这是一款快速查询可用域名的命令行工具。它能够根据关键词、前缀、后缀和多种顶级域名，智能生成域名组合，并快速检测其可用性。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/791194177.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
11、[booklore](https://hellogithub.com/periodical/statistics/click?target=https://github.com/booklore-app/booklore)：Java 开发的个人数字图书馆。这是一款开源、自托管的电子书管理 Web 应用，支持 PDF 和 ePub 电子书格式。它采用 Java（Spring Boot）+ Angular 开发，支持自动获取书籍信息、分享书籍、阅读进度同步、多用户管理等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/903039267.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[forge](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Card-Forge/forge)：开源的策略类卡牌游戏。这是一款为《万智牌》玩家打造的开源规则引擎和模拟器，玩法类似炉石的卡牌游戏。它提供单人冒险、任务、多种 AI 对战模式，支持在线对战、自定义卡牌和扩展功能，兼容 Windows、macOS、Linux 和 Android 平台。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/479890272.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
13、[eslint-plugin-unicorn](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sindresorhus/eslint-plugin-unicorn)：提升 JavaScript 代码质量的 ESLint 插件。这是一款集成了 100 多条高质量 JavaScript 代码检查规则的 ESLint 插件，全面覆盖代码风格、性能、安全性和可读性等多个方面。

14、[heynote](https://hellogithub.com/periodical/statistics/click?target=https://github.com/heyman/heynote)：专为程序员打造的记事本。这是一款专供开发者的便签应用，它的强大之处在于可以轻松将不同的内容分块暂存起来，不管是代码片段还是 Markdown 文字都可以往里放！支持自动语法高亮、自动格式化、计算器模式、多光标编辑、全局热键等功能，适用于 Windows、macOS 和 Linux。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/582974355.png' style="max-width:80%; max-height=80%;"></img></p>

15、[remotion](https://hellogithub.com/periodical/statistics/click?target=https://github.com/remotion-dev/remotion)：用 React 制作动态视频。这是一个能够通过代码生成视频的平台，开发者可以用 Web 技术（如 CSS、Canvas、SVG、WebGL）、React 组件、变量和函数动态生成视频内容，支持复杂的动画和效果。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/274495425.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[TypeWords](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zyronon/TypeWords)：极简的打字背单词网站。这是一款基于网页的背单词软件，帮助用户通过键盘输入来记忆单词。它界面简洁、交互流畅，支持单词发音、错误统计和生词本等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/674186516.png' style="max-width:80%; max-height=80%;"></img></p>

17、[workout-cool](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Snouzy/workout-cool)：开源的健身指导平台。这是一款免费、开源的健身指导平台，提供丰富的健身动作和视频演示。它采用 Next.js+TailwindCSS 构建，支持创建健身计划、进度跟踪和多语言功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/1000235209.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
18、[flashdim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cyb3rko/flashdim)：专业级 Android 手电筒应用。这是一款免费、无广告、可离线使用的手电筒应用，适配 Android 13 及以上系统。它通过硬件接口实现多级亮度调节，支持 SOS、摩斯码信号、BMP、定时闪烁等模式，非常适合徒步、露营、夜跑等场景使用。来自 [@ewiro](https://hellogithub.com/user/iItGgWoJjnLsr0Y) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/555295333.png' style="max-width:80%; max-height=80%;"></img></p>

19、[Trail-Sense](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kylecorry31/Trail-Sense)：野外生存必备 Android 应用。这是一款专为徒步、露营、野外生存等场景设计的开源 Android 应用。它利用手机的传感器，提供离线导航、日落提醒、照片地图、路径追踪等实用功能，所有功能均可在无网络环境下使用。来自 [@ewiro](https://hellogithub.com/user/iItGgWoJjnLsr0Y) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/215154276.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C 项目
20、[mac-mouse-fix](https://hellogithub.com/periodical/statistics/click?target=https://github.com/noah-nuebling/mac-mouse-fix)：macOS 鼠标增强工具。这是一款专为 macOS 打造的鼠标增强工具，弥补系统对非苹果鼠标支持的不足。用户可自定义第三方鼠标在 Mac 上的各种行为，支持平滑滚动、方向反转、鼠标手势和按钮映射等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/201134801.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
21、[borg](https://hellogithub.com/periodical/statistics/click?target=https://github.com/borgbackup/borg)：高效的数据去重备份工具。这是一个高效、安全的去重备份工具，即使文件结构或位置发生变化，也能精准识别重复数据。它采用内容定义分块去重算法，能显著节省存储空间，内置 lz4、zstd、zlib、lzma 等多种压缩选项，并支持 SSH 远程备份。

22、[bunkerweb](https://hellogithub.com/periodical/statistics/click?target=https://github.com/bunkerity/bunkerweb)：开源的 Web 应用防火墙。该项目是用 Python 开发的 Web 应用防火墙，可以无缝集成至现有环境（Linux、Docker、K8s 等）。它基于 Nginx 构建、默认配置安全，拥有简单易用的 Web 界面，支持自动配置 HTTPS A+ 评级、安全 Header 和丰富的插件系统，可检测常见的攻击模式、限制访问、防止机器人和爬虫等恶意访问，保护你的网站、API 和 Web 应用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/203456148.png' style="max-width:80%; max-height=80%;"></img></p>

23、[ebook2audiobook](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DrewThomasson/ebook2audiobook)：电子书转有声书的工具。这款开源工具可以轻松将电子书转换为有声书，支持多种常见格式，如 EPUB、MOBI、PDF 等。它通过 calibre 提取电子书文本，并运用语音合成技术（Text-to-Speech），能够生成包含章节和元数据的有声书，支持包括中文在内的 1000 多种语言。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/746935181.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[isd](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kainctl/isd)：终端交互式 systemd 管理工具。这是一个带终端用户界面（TUI）的 systemd 管理工具，支持模糊搜索、自动预览、智能 sudo、快捷键等功能，简化了对 systemd 单元（如服务、定时任务等）的管理体验。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/917864037.png' style="max-width:80%; max-height=80%;"></img></p>

25、[romm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rommapp/romm)：模拟器游戏玩家必备的 ROM 管理器。这是一个基于 Python 开发的 ROM 管理和模拟器平台，支持在浏览器中直接运行游戏。用户可通过简洁的 Web 界面，轻松扫描本地游戏、自动抓取游戏封面、统一管理多平台 ROM 资源，兼容 400 多种游戏平台。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/611338935.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
26、[microbin](https://hellogithub.com/periodical/statistics/click?target=https://github.com/szabodanika/microbin)：极简的文件分享和短链接平台。这是一款用 Rust 编写的轻量级 Web 应用，集共享文件、在线剪贴板和 URL 短链接于一体。它安全可靠且易于部署，支持自动过期、设置密码和保护级别等功能。来自 [@xici](https://hellogithub.com/user/OzQPpgo5Hw1W9lk) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/480154226.png' style="max-width:80%; max-height=80%;"></img></p>

27、[mise](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jdx/mise)：一站式多语言开发环境管理工具。这是一款用 Rust 编写的开发环境管理工具，集多语言工具链切换、环境变量管理和任务自动化于一体，轻松解决多版本编程语言、环境隔离和自动化构建等问题，可替代 asdf、nvm、pyenv、direnv、make 等多种工具。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/586920414.gif' style="max-width:80%; max-height=80%;"></img></p>

28、[somo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/theopfr/somo)：更友好的端口查看工具。这是一款专为 Linux 设计的人性化、界面友好的命令行工具，用于监控 socket 和本地端口。它以美观紧凑的表格实时展示端口与进程的网络连接信息，支持筛选、排序和格式化输出，可作为 netstat 替代品。来自 [@kero990](https://hellogithub.com/user/c3Y4NR1rq6neVoD) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/641143821.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
29、[container](https://hellogithub.com/periodical/statistics/click?target=https://github.com/apple/container)：苹果开源的轻量级虚拟机。这是一款苹果官方开源的轻量级虚拟化容器工具，用于在 Mac 上创建和运行 Linux 容器。它采用 Swift 开发，并针对 Apple 芯片（如 M1、M2 芯片）进行了优化，旨在为 macOS 用户提供高效、原生的容器体验，支持 OCI 标准容器镜像，并可无缝对接 Docker Hub 等主流镜像仓库。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/993475914.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[FlashSpace](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wojciech-kulik/FlashSpace)：让 macOS 的工作区切换变得瞬间完成。这是一款专为 macOS 设计的虚拟工作区管理器，可实现多任务间的极速无动画切换。它通过消除 macOS 切换应用的等待动画，提供即时的工作区切换体验，支持多显示器、画中画、焦点/光标管理等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/919165314.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
31、[claude-code](https://hellogithub.com/periodical/statistics/click?target=https://github.com/anthropics/claude-code)：终端里的 Claude 编码助手。该项目是 Claude 官方开源的 AI 编码助手，集成于终端内，能够理解整个代码库，并通过简单的自然语言命令，帮助开发者更高效地完成各类编码任务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/937253475.gif' style="max-width:80%; max-height=80%;"></img></p>

32、[gemini-cli](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google-gemini/gemini-cli)：谷歌 Gemini 命令行工具。该项目是 Gemini 官方开源的命令行工具，将 Google Gemini 的强大能力集成到终端环境。它基于百万级上下文，能够理解大型代码库的架构和逻辑，支持多模态输入输出、Google 搜索以及 MCP 等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/968197216.png' style="max-width:80%; max-height=80%;"></img></p>

33、[happy-llm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/datawhalechina/happy-llm)：从零开始的 LLM 原理与实践教程。该项目是帮助初学习者系统地学习大语言模型（LLM）原理与实践的教程。通过详细的教程和实战案例，循序渐进地带领读者深入了解自然语言处理（NLP）基础、Transformer 架构、预训练语言模型的基本原理，并动手实现和训练自己的大语言模型。来自 [@大痴小乙](https://hellogithub.com/user/aDd1NUpVvKHAJmE) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/806854629.jpg' style="max-width:80%; max-height=80%;"></img></p>

34、[nano-vllm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/GeeeekExplorer/nano-vllm)：从零开始构建的轻量级 vLLM。该项目是用 Python 实现的轻量级 vLLM（大语言模型推理引擎）项目，核心代码仅 1000 多行。它结构清晰、易于阅读，推理速度媲美 vLLM 原版，并集成了前缀缓存（Prefix Caching）、张量并行（Tensor Parallelism）和 Torch 编译等推理优化技术。
```python
from nanovllm import LLM, SamplingParams
llm = LLM("/YOUR/MODEL/PATH", enforce_eager=True, tensor_parallel_size=1)
sampling_params = SamplingParams(temperature=0.6, max_tokens=256)
prompts = ["Hello, Nano-vLLM."]
outputs = llm.generate(prompts, sampling_params)
outputs[0]["text"]
```

35、[prompt-optimizer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/linshenkx/prompt-optimizer)：优化 AI 提示词的工具。这是一款纯前端实现的提示词优化器，帮助用户快速编写更高质量的提示词。支持多种主流 AI 模型与自定义 API 地址，并可实时对比优化前后的效果。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/931352845.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
36、[daily-arXiv-ai-enhanced](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dw-dengwei/daily-arXiv-ai-enhanced)：每日自动生成 arXiv 论文摘要的工具。该项目能够自动获取 arxiv 上的论文，并利用大语言模型进行总结，生成中文摘要。来自 [@WeiTFw0B](https://hellogithub.com/user/lbNO5oE0sy1KGYW) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/951746200.png' style="max-width:80%; max-height=80%;"></img></p>

37、[ESP32-BlueJammer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/EmenstaNougat/ESP32-BlueJammer)：自制无线信号干扰器。这是一个基于 ESP32 和 nRF24 模块的 2.4GHz 通信干扰器，代码开源可自制或二次开发。它通过生成噪声和发送无效数据包来干扰蓝牙、BLE、WiFi 和 RC 设备的通信，使其无法正常工作。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/825347997.jpg' style="max-width:80%; max-height=80%;"></img></p>

38、[hoverzoom](https://hellogithub.com/periodical/statistics/click?target=https://github.com/extesy/hoverzoom)：悬停放大图片的浏览器插件。这是一款能够在鼠标悬停在图片上时，自动放大网页上的视频和图片的浏览器插件，支持 Chrome、Firefox、Edge 浏览器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/16063480.png' style="max-width:80%; max-height=80%;"></img></p>

39、[kubernetes-the-hard-way](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kelseyhightower/kubernetes-the-hard-way)：笨方法搭建 Kubernetes 集群的教程。该项目旨在通过手动从零搭建 Kubernetes 集群的方式，帮助初学者深入理解 K8s 的核心组件和工作原理。它提供一份不用自动化工具，纯手动安装、配置并运行一个高可用的 K8s 集群的详细指南。

40、[LeetCUDA](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xlite-dev/LeetCUDA)：面向高性能计算初学者的 CUDA 教程。这是一份专为高性能计算（HPC）初学者准备的 CUDA 教程与题库，包含 200 个 CUDA 实现的算子、学习笔记以及手搓性能对标官方的 HGEMM、FlashAttention-2 实战。适用于模型推理优化和算子优化相关面试准备。来自 [@DefTruth](https://hellogithub.com/user/ofSCbzTmdeQk3FD) 的分享

41、[obs-backgroundremoval](https://hellogithub.com/periodical/statistics/click?target=https://github.com/royshil/obs-backgroundremoval)：OBS 背景移除插件。这是一个开源的 OBS Studio 插件，可以在录制或直播过程中自动识别人像并去除背景，让用户能够轻松更换视频背景，支持 Windows、macOS 和 Ubuntu 等平台。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/358081783.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub110.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub112.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/111'>这里</a>。
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
