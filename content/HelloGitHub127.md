# 《HelloGitHub》第 127 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/127) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[cbirds](https://hellogithub.com/periodical/statistics/click?target=https://github.com/clainstone/cbirds)：在终端里看鸟群飞舞。这是一款用 C 语言编写的终端鸟群动画工具，基于 Boids 算法模拟群飞。它可以在终端中用盲文点阵画出鸟群，支持 3D 模式、老鹰捕猎、鸟群拼字显示时钟和屏保模式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1067126172.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[colibri](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JustVugg/colibri)：无需显卡运行千亿参数模型。这是一个用纯 C 编写的混合专家模型推理引擎，零依赖、不需要 GPU。它只把模型每次都要用到的部分留在内存，其余的专家权重在需要时再从硬盘读取，最低 8GB 内存就能运行 GLM、Kimi、DeepSeek、Qwen 等开源大模型，并提供兼容 OpenAI 和 Anthropic 的 API，适用于 Windows、Linux 和 macOS 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1286080397.png' style="max-width:80%; max-height=80%;"></img></p>

3、[DEsk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fyzugx/DEsk)：把 Linux 桌面变成一张书桌。该项目是基于 Wayland 的 Linux 桌面环境，整个房间采用光线追踪渲染。桌面是一张木书桌，窗口是一页页纸，最小化时像信一样折起，关闭时揉成纸团扔掉。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1413289247.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
4、[Filee](https://hellogithub.com/periodical/statistics/click?target=https://github.com/KnifeLemon/Filee)：拖一下就能转换格式的工具。这是一款用 C# 开发的离线文件格式转换器，支持图片、PDF、Office 文档、电子书、音视频、压缩包、CAD 等 200 多种格式。操作简单，按住 Ctrl 拖动文件，光标旁就会弹出格式圆环，放到目标格式上即可完成转换，文件全程不上传，适用于 Windows、Linux 和 macOS 系统。来自 [@Adnan Bhaldar](https://hellogithub.com/user/jAlIvVMhn0kcEsU) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1396526702.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[EditHere](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Inginnng/EditHere)：用截图告诉 AI 界面该怎么改。这是一款面向 AI 编程的截图批注工具，可以把具体怎么改整理成 AI 能直接读取的 JSON。支持悬停识别界面元素、点和框批注、拖动组件调整布局、暂停视频按帧批注，以及 OCR 和长截图，所有处理均在本地完成。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1365889199.gif' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
6、[gocryptfs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rfjakob/gocryptfs)：用 Go 写的加密文件系统。该项目是基于 Go 和 FUSE 的文件加密工具，可将密文目录挂载为可读写的明文目录，文件内容和名称分别加密。生成的密文目录既能放入 Dropbox 等云盘，也可通过 rsync 增量同步。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/41997606.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[magpie](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yetone/magpie)：一键切换 AI 编程助手的模型。这是一款用 Go 开发的 AI 编程助手模型管理工具，让 Claude Code 用上 Kimi、Codex 用上 DeepSeek。它通过本地网关转换 OpenAI、Anthropic 和 Gemini 的接口格式，支持多种编程助手和模型服务商，还能把订阅共享给其他助手使用，额度用完后自动切换账号。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1383809012.png' style="max-width:80%; max-height=80%;"></img></p>

8、[matcha](https://hellogithub.com/periodical/statistics/click?target=https://github.com/floatpane/matcha)：在终端里收发邮件的客户端。这是一款用 Go 和 Bubble Tea 开发的终端邮件客户端，通过命令就能收发邮件，支持多账户、Markdown 写邮件和插件市场等功能。来自 [@Drew Smirnoff](https://hellogithub.com/user/FYa6zrBtyeSOsLu) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1027531184.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[pocket-id](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pocket-id/pocket-id)：无需密码的自托管身份认证服务。该项目是用 Go 开发的 OIDC 和 OAuth 2.0 身份认证服务，支持用 Passkey 替代密码。用户不用记密码，插上 YubiKey 等硬件密钥就能登录。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/841141075.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
10、[GeoLibre](https://hellogithub.com/periodical/statistics/click?target=https://github.com/opengeos/GeoLibre)：在浏览器里就能用的开源 GIS 平台。该项目是用 TypeScript 开发的地理信息系统，可用于可视化、浏览和分析地理空间数据，数据保留在本地。它内置 1000 多个通过 WebAssembly 在浏览器中运行的分析工具，涵盖地形、水文、激光雷达和遥感分析，可以运行在浏览器、桌面、手机和 Jupyter Notebook 中，还提供月球、火星等行星底图。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1251648409.png' style="max-width:80%; max-height=80%;"></img></p>

11、[omni-tools](https://hellogithub.com/periodical/statistics/click?target=https://github.com/iib0011/omni-tools)：可自托管的全能在线工具箱。这是一款基于 React 开发的在线工具集合，提供图片、音视频、PDF、文本、日期时间、数学计算和数据处理等日常工具，所有文件都在本地浏览器中处理。它提供图片缩放与格式转换、视频裁剪、PDF 拆分与合并、时区转换、JSON 处理等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/814882742.png' style="max-width:80%; max-height=80%;"></img></p>

12、[openGym](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DuarteSantos8/openGym)：数据由自己掌控的健身记录应用。这是一款可自托管的健身和体重记录应用，没有订阅、广告和遥测，用 Docker 一行命令即可部署。它内置 5000 多个带动画演示的动作，支持按星期安排训练计划、引导式训练、组间休息计时、自动识别个人最佳成绩，并能通过肌肉热力图查看各部位训练情况，还可以从 Strong、Hevy 等应用导入数据，提供 iPhone、Apple Watch 和 Android 版本。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1305213943.png' style="max-width:80%; max-height=80%;"></img></p>

13、[puter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HeyPuter/puter)：运行在浏览器里的云电脑。这是一个运行在浏览器里的桌面操作系统，把文件、应用和游戏集中在一处，随时随地访问。它内置记事本、录音机、电子表格、相机等应用，还为开发者提供 AI、云存储、键值数据库和 Serverless Workers 等能力，开发的 Web 应用和游戏可以发布到它的应用商店。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/766341786.png' style="max-width:80%; max-height=80%;"></img></p>

14、[word-atlas](https://hellogithub.com/periodical/statistics/click?target=https://github.com/designfuchen/word-atlas)：一词一画的雅思背单词工具。这是一款免费开源的雅思背单词网页应用，打开浏览器就能用，无需注册。它收录 7000 多个雅思核心词，每个词都配有一幅原创插画、两条原创例句和英美发音，基于 FSRS 算法安排复习，学会的单词会在 3D 词汇星图上点亮一颗星。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1432980411.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
15、[aerial-tv](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pengchujin/aerial-tv)：给电视换上 Apple TV 风格的桌面。这是一款参照 tvOS 设计的开源 Android TV 桌面，没有广告和推荐流，开机自动进入，适用于小米、TCL、创维等国产电视，以及盒子和投影仪。它支持整理应用、建文件夹、隐藏系统 App 和扫码用手机排序，安装无需 root，随时可以还原。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1426780056.jpg' style="max-width:80%; max-height=80%;"></img></p>

16、[DiPlay](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shihabal3amri/DiPlay)：在安卓设备上用 CarPlay。这是一款运行在安卓车机上的 CarPlay 应用，装在车机上即可使用有线或无线 CarPlay。它支持 Wi-Fi 直连和车载热点，可以把导航转向箭头、距离和路名投到抬显上，还能调整图标大小、分辨率和帧率，支持安卓 7.0 及以上系统和简体中文界面。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1385817306.png' style="max-width:80%; max-height=80%;"></img></p>

17、[DroidDeck](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Droid-Deck/DroidDeck)：在安卓手机上玩 Steam 游戏。这是一款将 SteamOS 带到 Android 的应用，可在搭载 Adreno GPU 的安卓设备上运行 Steam 客户端，支持运行 Windows 游戏、安装 Linux 应用、登录 GOG、Epic 和 Amazon 游戏商店。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1385776214.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
18、[genanki](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kerrickstaley/genanki)：用 Python 生成 Anki 卡组。这是一个用于生成 Anki 记忆卡组的 Python 库，支持自定义笔记字段、卡片模板和 CSS 样式，还可添加图片和音频。修改内容并重新生成卡组后，再次导入即可覆盖已有的同名卡片，适合从单词表、题库等数据批量制作卡片。

19、[kcc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ciromattia/kcc)：让漫画适配电子墨水屏。这是一款面向 Kindle、Kobo 等墨水屏阅读器优化漫画显示的转换工具，可将图片、CBZ、PDF 等文件转换为电子书，并按设备分辨率缩放和裁切页边。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/6938242.png' style="max-width:80%; max-height=80%;"></img></p>

20、[manimgx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/academa-labs/manimgx)：更快的数学动画引擎。该项目是兼容 Manim 社区版 API 的 3D 数学动画引擎，采用 GPU 渲染，速度比社区版快 90 倍。它支持 Claude Code、Codex 等 AI 编程助手直接编写动画，可通过 WebGPU 在浏览器中运行或导出 MP4 视频。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1406372374.png' style="max-width:80%; max-height=80%;"></img></p>

21、[pywinauto](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pywinauto/pywinauto)：用 Python 自动操作 Windows 桌面应用。这是一个 Windows 图形界面自动化 Python 库，能够模拟鼠标和键盘操作窗口、对话框和控件，还可以读取界面上的文本数据。它支持 Win32 API 和 MS UI Automation 两种后端，可以通过窗口标题、控件名称等文本属性定位元素，几行代码就能完成打开菜单、点击按钮、输入文字等操作，适用于桌面软件的自动化测试和重复操作。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/36223210.png' style="max-width:80%; max-height=80%;"></img></p>

22、[tilelang](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tile-ai/tilelang)：用 Python 写高性能 GPU 算子。这是一个专为编写高性能 GPU/CPU/NPU 算子设计的领域专用语言，底层基于 TVM 编译器构建，让开发者不必手写底层代码也能实现 GEMM、FlashAttention 等算子的极致优化。它支持 NVIDIA CUDA、AMD ROCm、Apple Metal 和华为昇腾等多种硬件，内置自动调优和调试可视化工具，并提供 DeepSeek MLA 等大模型算子示例。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/867004514.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
23、[esp32sim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mikroverk/esp32sim)：开源的 ESP32 模拟器。这是一款用 Rust 编写的 ESP32 模拟器，无需开发板即可在电脑或浏览器中运行未经修改的真实固件。它完整模拟引导程序到 FreeRTOS 的启动流程，还能模拟屏幕、触摸、LED、音频、摄像头和 WiFi 等外设，支持 ESP32-S3、C3、C6、P4 等芯片。

24、[miniserve](https://hellogithub.com/periodical/statistics/click?target=https://github.com/svenstaro/miniserve)：极简的共享文件 HTTP 服务器。这是一款用 Rust 编写的命令行工具，只需一个文件就能通过 HTTP 共享文件和目录。它支持用户名密码认证、文件上传、文件夹打包下载、按名称搜索、扫码访问、TLS 和 WebDAV，还能像 GitHub 一样渲染 README.md 文件，并提供浅色和深色主题，适用于临时分享文件等场景。来自 [@size_t](https://hellogithub.com/user/6xC1sQERhkZVB7A) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/131135585.png' style="max-width:80%; max-height=80%;"></img></p>

25、[OpenShell](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NVIDIA/OpenShell)：英伟达开源的 AI 智能体安全沙箱。这是一个专为自主 AI 智能体设计的安全运行时，让智能体可以读写文件、安装软件包和调用 API，又不会随意接触你的数据、密钥和网络。每个智能体都运行在隔离的沙箱中，在内核层面按策略管控文件访问、系统调用和网络连接，真实凭据只会在请求发往已批准的地址时才被注入。

### Skills
26、[anatomy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wheresryan22/anatomy)：把技术概念画成会动的机械图。这是一个为 AI 编程助手打造的插画技能，能把抽象的技术概念转化为真实可动的机械装置，绘制成精致的等距视角交互插图，比如把缓存命中画成只有每根锁销都对齐才能转动的锁芯。它支持 SVG、SVG+WebGL 着色器和 3D 三种形式，可导出为 HTML 页面、SVG 文件或 React 组件。来自 [@JRZYgit](https://hellogithub.com/user/0Aj4ipeQrDYuHBX) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1410124849.png' style="max-width:80%; max-height=80%;"></img></p>

27、[asd-ste100-skill](https://hellogithub.com/periodical/statistics/click?target=https://github.com/danyuchn/asd-ste100-skill)：用简化英语改写 AI 指令。该项目是基于航空航天业的简化技术英语规范，能把含糊、冗长的英文改写成不会被误读的句子，然后输入给 AI 智能体。它会逐句检查被动语态、复杂时态、一句多指令、长句和营销形容词等问题，改写时不丢失原文的任何事实和条件。

28、[diagram-design](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cathrynlavery/diagram-design)：让 AI 画出有设计感的图。这是一个为 AI 编程助手打造的图表设计技能，能生成可直接在浏览器中打开的 HTML+SVG 文件。它支持架构图、流程图、时序图、甘特图、桑基图等 45 种图表类型，能从网站自动提取品牌配色和字体，还能将 Mermaid、draw.io 和 Excalidraw 中已有的图表按统一风格重绘，并导出为 PNG 或 SVG。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1212769188.png' style="max-width:80%; max-height=80%;"></img></p>

29、[impeccable](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pbakaus/impeccable)：让 AI 设计的界面更有品味。这是一个为 AI 编程助手打造的前端设计技能，在 Anthropic 官方 frontend-design 的基础上扩展而来，用来避免 AI 生成千篇一律的界面，比如处处用 Inter 字体、紫蓝渐变、卡片里套卡片。它提供 polish、audit、critique 等 24 个设计命令和 62 条确定性检测规则，支持 Claude Code、Cursor、Codex、Gemini CLI 等工具。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1097346685.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
30、[tendedero](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alejandrobujan/tendedero)：把截图晾在屏幕顶部的 macOS 工具。这是一款有趣、小巧的 macOS 截图整理工具，它会把每张截图像晾衣服一样挂在屏幕顶部的绳上，鼠标移到菜单栏时绳子滑下，移开后自动收起，让桌面不再堆满截图文件。单击即可复制，长按进入标注，拖到应用里直接发送，拖进废纸篓即可删除，还支持录屏剪辑。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1408099862.gif' style="max-width:80%; max-height=80%;"></img></p>

31、[xtool](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xtool-org/xtool)：跨平台的 Xcode 替代品。这是一款用 Swift 编写的跨平台 Xcode 替代工具，可在 Linux、Windows 和 macOS 上用 SwiftPM 构建 iOS 应用并部署到真机。支持创建项目、构建运行、签名安装应用和管理设备等功能，还可以通过命令行操作 Apple 开发者服务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/889784913.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
32、[artemis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google/artemis)：谷歌开源的 AI 手机自动化工具。这是一款 AI 驱动的 Android 自动化工具，只需用自然语言描述任务，AI 就会自动操作手机或模拟器，完成跨应用的测试流程和日常任务。它内置 MCP 服务，能让 Claude Code、Codex 等 AI 编程助手直接操控手机并收集日志和截图，支持 Gemini、Claude、GPT-4o 等多模态模型。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1333399642.png' style="max-width:80%; max-height=80%;"></img></p>

33、[DeepInfer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/deepseek-ai/DeepInfer)：DeepSeek 开源的大模型推理框架。该项目是 DeepSeek 线上大规模服务所用的高性能推理框架，提供离线推理和大规模部署所需的核心功能。它集成了 FlashMLA、DeepGEMM、DeepEP 等自研优化算子，支持注意力数据并行、MoE 专家并行、异步调度、确定性采样和结构化输出，可运行在英伟达和华为昇腾 NPU 上。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1421825221.png' style="max-width:80%; max-height=80%;"></img></p>

34、[harness2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google-research/harness2)：谷歌开源的智能体自我进化框架。这是一个让 AI 智能体在不改动模型权重的情况下，遇到陌生任务时自我改进的框架。它会针对当前任务提出修改方案，比如调整系统提示词、记忆、技能、子智能体和插件等，然后实际试跑对比效果，最后把经验沉淀下来，供后续任务使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1407951147.png' style="max-width:80%; max-height=80%;"></img></p>

35、[UniMate](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Friedrich-M/UniMate)：一句话让任意 3D 角色动起来。该项目能为不同骨骼结构的 3D 模型生成动作，输入一个带骨骼的 3D 模型和一句文字描述，它就能实时生成对应的动作，不需要针对每种骨骼重新训练，适用于人形、四足动物、鸟类、海洋生物、昆虫和机械等多种骨骼结构。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1309249926.png' style="max-width:80%; max-height=80%;"></img></p>

36、[VoiceStudio](https://hellogithub.com/periodical/statistics/click?target=https://github.com/debpalash/VoiceStudio)：开源的本地 AI 语音工作室。这是一款完全本地运行的语音克隆与配音工具，可作为 ElevenLabs 的开源替代品，支持 600 多种语言。它集成了 CosyVoice、IndexTTS、GPT-SoVITS、WhisperX 等多种语音合成和识别引擎，支持音色设计、视频配音、人声分离、听写和有声书制作等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1206390571.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
37、[everything](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HeyPuter/everything)：从零打造商业软件的开源替代品。这是由 Puter 团队发起的开源项目，目标是从零开始重新打造商业软件的免费开源替代品。目前已有 50 多款应用，包括 Excel、PPT、PS、AutoCAD、Zoom 和 Slack 的替代品，还有国际象棋、数独等小游戏，大部分都可以直接在浏览器中使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1417456983.png' style="max-width:80%; max-height=80%;"></img></p>

38、[Future-Style-Periodic-Table](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SeanWong17/Future-Style-Periodic-Table)：赛博朋克风格的元素周期表。这是一个运行在浏览器中的交互式化学元素周期表，采用深色赛博朋克风格，涵盖全部 118 种元素的原子序数、电子排布、同位素和化合价等数据。它支持按原子半径、电负性、熔点等属性切换热力图，点击元素即可拖拽旋转 3D 原子模型，查看电子层结构，并提供中英文双语界面。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1107726420.png' style="max-width:80%; max-height=80%;"></img></p>

39、[gpu-unlock](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Zagitta/gpu-unlock)：解锁 RTX 30 系显卡的算力。这是一个 Linux 内核模块，可以把 NVIDIA RTX 30 系消费级显卡的 FP16/BF16 指令发射速率解锁到对应专业卡的水平，让矩阵运算吞吐量大幅提升。比如 RTX 3090 Ti 的 BF16 算力能从 87.5 提升到 157.4 TFLOPS，大模型预填充速度提升 14%~36%。它在 NVIDIA 官方驱动加载前完成解锁，无需修改驱动，也不用在每次驱动更新后重新打补丁。

40、[navigation2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ros-navigation/navigation2)：开源的移动机器人导航框架。这是一个机器人自主导航框架，提供感知、定位、路径规划、运动控制和避障等功能，通过行为树编排各个模块化服务。除了基础的导航，还支持航点巡航、目标跟随和全覆盖导航等任务。

41、[PicLite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/amiaoapp/PicLite)：极简的本地图片压缩工具。这是一款图片与动图的本地处理工具，支持批量压缩、拖动对比画质、格式转换、缩放和添加水印，会自动比较 JPEG、WebP、PNG 等候选结果并选出体积更小的文件。它提供 Windows、macOS 和 Linux 桌面端，也可在浏览器或 Docker 中使用，图片全程在本机处理，桌面端还支持文件夹监测、剪贴板自动优化和 MCP 接入。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/127/1314868034.jpg' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
42、[HowToLiveBetter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eternity4719/HowToLiveBetter)：《高性价比人生指南》。这是一本介绍用少的钱、时间和精力，换回更多寿命、金钱的生活指南，涵盖长寿防病、急救、省钱理财、法律红线、失业救助、医保社保、恋爱婚育和创业合规等内容。



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub126.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | 『下一期』
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/127'>这里</a>。
</p>

## 赞助


<table>
  <thead>
    <tr>
      <th align="center" style="width: 80px;">
        <a href="https://www.ucloud.cn/?ytag=geo_waituo_HelloGitHub">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/ucloud.png" width="60px"><br>
          <sub>UCloud</sub><br>
          <sub>聚合200+主流大模型</sub>
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
        <a href="https://ofox.ai/zh?utm_source=github&utm_medium=hellogithub&utm_campaign=sponsor">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/0foxai.png" width="60px"><br>
          <sub>OfoxAI</sub><br>
          <sub>100+ 模型官方直连不掉线</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://serpapi.com/hello-github">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/main/logo/serpapi.png" alt="SerpApi" width="60px"><br>
          <sub>SerpApi</sub><br>
          <sub>AI Agent 实时搜索数据 API</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
