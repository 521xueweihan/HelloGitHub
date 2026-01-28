# 《HelloGitHub》第 104 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/104) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[deskhop](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hrvach/deskhop)：基于树莓派的双机鼠标键盘共享方案。这是一款用于快速切换鼠标和键盘的桌面切换工具，解决了用户在多台计算机之间共享键盘和鼠标时遇到的繁琐和延迟问题。它通过硬件中介设备，支持在不同操作系统（Linux、macOS、Windows）之间通过拖动鼠标或使用快捷键实现输入的无缝切换。该项目完全开源，且不需要安装额外的驱动。硬件则是基于 Raspberry Pi Pico 和 USB 输入/输出协议，支持自定义配置并提供多种附加功能，如慢速鼠标模式、屏幕锁定和游戏模式。来自 [@无间之钟](https://hellogithub.com/user/rnlYFdQcyhRm50p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/735426820.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[kyanos](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hengyoush/kyanos)：深入内核的网络流量分析工具。这是一个基于 eBPF 的网络问题分析工具，能够实时监控和分析 HTTP、Redis 和 MySQL 请求。它支持强大的流量过滤功能，可根据进程、容器、协议信息和耗时等条件进行精确过滤，并提供多维度聚合抓取的数据包信息，适用于排查远程服务慢查询等问题。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/793985221.gif' style="max-width:80%; max-height=80%;"></img></p>

3、[minisign](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jedisct1/minisign)：简单易用的文件签名工具。这是一个开箱即用的文件数字签名与验证工具，只需要简单的命令即可生成和验证文件签名。它基于 Ed25519 公钥签名系统，提供可靠的文件完整性验证功能，适用于软件分发和文件共享等场景。
```
# 创建密钥
minisign -G
# 对文件进行签名
minisign -Sm HelloGitHub.txt
# 验证签名
$ minisign -Vm HelloGitHub.txt -P xxxx
```

### C# 项目
4、[AvaloniaVisualBasic6](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BAndysc/AvaloniaVisualBasic6)：经典的 VB6 IDE 跨平台重生计划。该项目使用 C# 语言和 Avalonia 框架复刻了经典的 Visual Basic 6 IDE，支持创建、保存、加载和运行 VB6 语言的项目，能够在 Windows、macOS、Linux 和浏览器中运行。来自 [@39499740](https://hellogithub.com/user/7eRBdwFSrtPxipV) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/884565845.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[FileConverter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Tichau/FileConverter)：右键轻松转换和压缩文件的工具。这是一个专为 Windows 设计的文件转换和压缩工具，用户可以通过右键菜单轻松完成文件格式转换和压缩操作。它完全免费开源，支持多种文件格式、批量处理等功能，并提供包括中文在内的多语言支持。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/33476566.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
6、[carla](https://hellogithub.com/periodical/statistics/click?target=https://github.com/carla-simulator/carla)：开源的自动驾驶研发模拟平台。这是一款用于自动驾驶研究的开源模拟器，专为自动驾驶系统的开发、训练和验证提供虚拟环境。它包含免费的数字资产库，包括城市布局、建筑和车辆模型等，支持灵活配置传感器套件和环境条件。还提供了容易上手的 Python API，方便开发者进行车辆控制、传感器配置和环境参数调整。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/108102826.png' style="max-width:80%; max-height=80%;"></img></p>

7、[PrismLauncher](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PrismLauncher/PrismLauncher)：开源的 Minecraft 启动器。该项目是基于 MultiMC 开发的 Minecraft 启动器，旨在帮助用户轻松管理多个 Minecraft 版本和实例。它优化了启动器的使用体验，支持快速切换不同版本、模组配置和游戏设置，兼容 Windows、Linux 和 macOS 平台。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/553135896.png' style="max-width:80%; max-height=80%;"></img></p>

8、[zeal](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zealdocs/zeal)：实用的离线文档浏览工具。该项目是受 Dash 启发、专为开发者打造的离线文档查询工具，无需联网即可访问各种编程语言和框架的 API 文档。它提供简洁的界面和多种编辑器插件，并支持自定义文档的创建和导入，适合在没网的环境下查看技术文档。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/7711472.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
9、[dpanel](https://hellogithub.com/periodical/statistics/click?target=https://github.com/donknap/dpanel)：轻量级的 Docker 可视化管理面板。这是一款专为国内用户设计的 Docker 可视化管理面板，采用全中文界面。它安装简单且资源占用低，运行在容器内部对宿主机无侵入，支持容器管理、镜像管理、文件管理以及 Compose 管理等功能。来自 [@donknap](https://hellogithub.com/user/ekhLfDOxR5U0mVw) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/722655859.png' style="max-width:80%; max-height=80%;"></img></p>

10、[go-blueprint](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Melkeydev/go-blueprint)：快速生成 Go Web 项目结构的工具。这是一个用于快速搭建 Go 语言 Web 项目的命令行工具，集成了 Chi、Gin、Fiber、Echo 等多种流行的 Go 框架。它支持选择 MySQL、Postgres、Redis 等主流数据库，还提供了 WebSocket 和 Docker 等高级设置。用户只需选择技术栈，即可生成一套完整的 Go Web 项目架子。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/703404066.png' style="max-width:80%; max-height=80%;"></img></p>

11、[lute](https://hellogithub.com/periodical/statistics/click?target=https://github.com/88250/lute)：对中文更友好的 Markdown 引擎。这是一个用 Go 语言编写的 Markdown 引擎，实现了最新的 GFM/CM 规范。它是将 Markdown 文本转换成一个抽象语法树（AST），无需正则表达式解析速度更快，支持 GFM/CM 规范、内置代码高亮、术语修正、格式化（中英文间自动插入空格）和 Emoji 解析等功能。来自 [@两双筷子sqldc](https://hellogithub.com/user/5dGtvaZ6H3L4QMY) 的分享
```go
func main() {
	luteEngine := lute.New() // 默认已经启用 GFM 支持以及中文语境优化
	html:= luteEngine.MarkdownStr("demo", "**Lute** - A structured markdown engine.")
	fmt.Println(html)
	// <p><strong>Lute</strong> - A structured Markdown engine.</p>
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/225160662.png' style="max-width:80%; max-height=80%;"></img></p>

12、[OliveTin](https://hellogithub.com/periodical/statistics/click?target=https://github.com/OliveTin/OliveTin)：极简的 Shell 命令 Web 管理平台。该项目提供了一个简单直观的 Web 界面，让用户能够快速执行预先设定好的 Shell 命令。它开箱即用、配置简单、占用资源少，可以将复杂的命令简化成网页上的一个按钮。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/365300077.png' style="max-width:80%; max-height=80%;"></img></p>

13、[wanderer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/open-wanderer/wanderer)：开源的探险轨迹记录与分享平台。该项目是用于记录和管理用户的户外探险轨迹的 Web 平台，帮助你保存珍贵的行程数据。它采用 Go+Svelte 开发，提供上传、保存、查看（多种视图）和分享冒险轨迹的功能，并支持自托管。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/749092533.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
14、[moodist](https://hellogithub.com/periodical/statistics/click?target=https://github.com/remvze/moodist)：免费、高颜值的白噪音网站。这是一个有助于专注与放松的听觉网站，无需注册完全免费。它界面简洁、操作方便，内置 75 种白噪音，用户可根据个人喜好自由选择与组合，找到适合自己的声音环境。同时，Moodist 还支持定时关闭、番茄时钟、快捷键等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/700879222.png' style="max-width:80%; max-height=80%;"></img></p>

15、[rot.js](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ondras/rot.js)：开发 Roguelike 游戏的 JavaScript 工具包。这是一个无依赖的 JavaScript 库，专为开发 Roguelike（肉鸽）游戏而设计，包含地图生成、随机数生成、路径寻找、按键处理和照明等多个模块。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/4391145.png' style="max-width:80%; max-height=80%;"></img></p>

16、[slugify](https://hellogithub.com/periodical/statistics/click?target=https://github.com/simov/slugify)：将字符串转化成 URL 友好的 JS 库。该项目是用于将字符串转换为适合在 URL 中使用的格式，输出由小写字母、数字和短横线组成的字符串，不含空格和特殊字符，这种格式有助于搜索引擎优化（SEO）。
```javascript
var slugify = require('slugify')

slugify('some string') // some-string

// if you prefer something other than '-' as separator
slugify('some string', '_')  // some_string
```

17、[starlight](https://hellogithub.com/periodical/statistics/click?target=https://github.com/withastro/starlight)：基于 Astro 的一站式文档解决方案。该项目是基于 Astro 框架打造的文档主题，可用于快速搭建和部署文档网站。它界面美观、开箱即用、访问速度快，支持网站导航、搜索、国际化、SEO 和各种插件。来自 [@小小修真者](https://hellogithub.com/user/OJpriDKTWlq0ZHI) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/614933136.png' style="max-width:80%; max-height=80%;"></img></p>

18、[xiaoju-survey](https://hellogithub.com/periodical/statistics/click?target=https://github.com/didi/xiaoju-survey)：企业级的问卷调研平台。这是一款免费且专业的调研系统，旨在为个人和企业提供一站式产品级的调研解决方案。它前后端均已开源，并支持 Docker 一键部署，内置了多种题型和模版，支持逻辑编排、自定义品牌、权限管理、数据分析以及 AI 生成问卷等功能，可用于创建问卷、考试、测评和复杂表单。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/713210442.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
19、[ab-download-manager](https://hellogithub.com/periodical/statistics/click?target=https://github.com/amir1376/ab-download-manager)：Kotlin 开发的下载工具。这是一款开源的桌面下载工具，专为提供便捷快速的下载体验而设计。它拥有现代化的界面和更快的下载速度，支持下载队列、速度限制和浏览器插件功能，兼容 Windows 和 Linux 平台。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/825187044.png' style="max-width:80%; max-height=80%;"></img></p>

20、[Olauncher](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tanujnotes/Olauncher)：极简的 Android 启动器。这是一款免费、无广告的 Android 启动器，主屏幕上最多可设置 8 个应用，提供极简的 Android 使用体验，并支持手势、双击锁屏和每日壁纸等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/278638069.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
21、[ASCII-generator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vietnh1009/ASCII-generator)：生成文字图的 Python 库。该项目是一款将图片和视频转换为 ASCII 艺术风格作品的工具，即用字符艺术化地表达图像内容。它使用简单，支持将图片转换为文本或 ASCII 风格图片，以及将视频转换为 ASCII 风格视频，并提供颜色选择等多种功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/168572824.jpg' style="max-width:80%; max-height=80%;"></img></p>

22、[icloud_photos_downloader](https://hellogithub.com/periodical/statistics/click?target=https://github.com/icloud-photos-downloader/icloud_photos_downloader)：iCloud 照片下载工具。这是一款用 Python 开发的工具，可用于批量下载 iCloud 照片。它提供了复制、同步和移动三种操作模式，支持 Live Photos、自动删除重复数据、增量下载等功能，适合用于 iCloud 照片迁移和备份等场景。

23、[imagehash](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JohannesBuchner/imagehash)：基于哈希值识别相似图像的 Python 库。该项目的算法不同于传统的加密哈希算法（如 MD5、SHA-1），它专注于图像内容的相似度分析，对有细微不同的图片可生成相似的哈希值，用于计算图片相似度，支持平均哈希、感知哈希、差分哈希等算法，适用于快速识别版权图片等场景。
```python
from PIL import Image
import imagehash

# 计算第一个图像的哈希值
hash = imagehash.average_hash(Image.open('tests/data/imagehash.png'))
print(hash)
# 哈希值：ffd7918181c9ffff

# 计算第二个图像的哈希值
otherhash = imagehash.average_hash(Image.open('tests/data/peppers.png'))
print(otherhash)
# 哈希值：9f172786e71f1e00

# 比较两个图像哈希值是否相等
print(hash == otherhash)  # False

# 计算并输出哈希值的汉明距离
print(hash - otherhash)  # 33 汉明距离（差异度）
```

24、[mopidy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mopidy/mopidy)：Python 写的音乐服务器。这是一个易扩展的 Python 音乐服务器，支持扫描和播放本地音乐，并集成多个在线音乐流媒体，还可通过插件扩展音乐源、管理界面和在线播放器等功能。

25、[pyarmor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dashingsoft/pyarmor)：强大的 Python 脚本加密工具。这是一个用于对 Python 脚本进行混淆处理的命令行工具，仅需一条命令即可完成加密操作。它提供丰富的加密选项，用来平衡安全与性能，支持将加密后的脚本绑定到特定机器、设置加密有效期和 Themida 保护等功能。来自 [@Xuefeng Xu](https://hellogithub.com/user/k4oyT8wSU5Qfx6H) 的分享

### Rust 项目
26、[kanata](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jtroo/kanata)：跨平台的键盘重映射工具。这是一个用 Rust 语言开发的键盘重映射工具，用户可根据自身需求自定义键盘布局和功能，支持点击按住、组合键编程、设置按键响应速度，适用于 Windows、Linux 和 macOS 系统。

27、[surrealdb](https://hellogithub.com/periodical/statistics/click?target=https://github.com/surrealdb/surrealdb)：端到端的云原生数据库。这是一个用 Rust 开发的多模型数据库，支持表格（Table）、文档（Documents）和图（Graph）数据模型。它既可以作为数据库使用，也可作为 API 后端服务，支持 SQL、GraphQL、ACID 事务、图查询和全文索引等多种查询方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/436658287.png' style="max-width:80%; max-height=80%;"></img></p>

28、[tauri](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tauri-apps/tauri)：Rust 驱动的跨平台桌面应用开发框架。这是一个用于构建更小、更快、更安全的桌面和移动应用的框架，支持 macOS、Windows、Linux、Android 和 iOS 平台。它允许使用前端框架构建用户界面，并内置应用打包器、系统托盘图标和原生通知等功能。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/196701619.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
29、[Off-Day](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zizicici/Off-Day)：休息日闹钟不响的 iOS 应用。这是一个专为 iOS 用户开发的节假日闹钟应用，内置多个公共假期模板，用户可以轻松标记假期，实现自动管理工作日和假期的闹钟设置，确保休息日不再被闹钟打扰。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/794390400.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
30、[krita-ai-diffusion](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Acly/krita-ai-diffusion)：Krita 的 AI 绘画助手插件。这是一个专为 Krita 绘画软件开发的 AIGC 插件，旨在提供更便捷和可控的图像生成体验。用户只需选择区域并输入文本提示，即可轻松实现图像填充、扩展、放大、添加和删除对象等操作，支持本地运行、Stable Diffusion、ControlNet、IP-Adapter 和自定义检查点等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/686161611.png' style="max-width:80%; max-height=80%;"></img></p>

31、[netron](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lutzroeder/netron)：跨平台的机器学习模型查看工具。这是一个神经网络、深度学习和机器学习模型的可视化工具，支持多种模型格式，包括 ONNX、TensorFlow Lite、Core ML、Keras、Caffe、Darknet 和 PyTorch 等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/1198539.png' style="max-width:80%; max-height=80%;"></img></p>

32、[Perplexica](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ItzCrazyKns/Perplexica)：AI 驱动的搜索引擎工具。这是一个开源的 AI 搜索引擎工具，灵感来源于 Perplexity AI。它结合了 SearxNG 和大语言模型（LLMs）等技术，能够理解你的问题并深入互联网查找答案，可作为传统搜索引擎的替代品。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/784181462.png' style="max-width:80%; max-height=80%;"></img></p>

33、[TensorRT-YOLO](https://hellogithub.com/periodical/statistics/click?target=https://github.com/laugh12321/TensorRT-YOLO)：灵活易用的 YOLO 部署工具。这是一款专为 NVIDIA 设备优化的 YOLO 部署工具。它通过集成 TensorRT 插件和 CUDA 技术，提供 C++ 和 Python API，显著提升了推理速度和易用性，支持多种 YOLO 版本，适用于目标检测、实例分割、姿态识别、旋转目标检测和视频分析等多种场景。来自 [@Laugh](https://hellogithub.com/user/2AGzE4dsO8ZUD9R) 的分享
```python
import cv2
from tensorrt_yolo.infer import DeployDet, generate_labels_with_colors, visualize

# 初始化模型
model = DeployDet("yolo11n-with-plugin.engine")
# 加载图片
im = cv2.imread("test_image.jpg")
# 模型预测
result = model.predict(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
print(f"==> detect result: {result}")
# 可视化
labels = generate_labels_with_colors("labels.txt")
vis_im = visualize(im, result, labels)
cv2.imwrite("vis_image.jpg", vis_im)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/749292767.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
34、[BewlyBewly](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BewlyBewly/BewlyBewly)：优化 bilibili 网站界面的浏览器插件。这是一个第三方的 B 站浏览器插件，通过优化 bilibili 网站的界面来提升用户体验，支持 Chrome、Edge 和 Firefox 浏览器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/473632745.png' style="max-width:80%; max-height=80%;"></img></p>

35、[frpc-desktop](https://hellogithub.com/periodical/statistics/click?target=https://github.com/luckjiawei/frpc-desktop)：跨平台的 frp 桌面客户端。该项目是内网穿透工具 frp 的桌面客户端，更方便地实现内网穿透。它开箱即用、界面清爽，支持开机启动、多用户、配置导入和导出等功能，适用于 Windows、Linux 和 macOS 平台。来自 [@蠢🐷](https://hellogithub.com/user/fRmIN16g9jXtYFe) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/723986046.png' style="max-width:80%; max-height=80%;"></img></p>

36、[keeptrack.space](https://hellogithub.com/periodical/statistics/click?target=https://github.com/thkruz/keeptrack.space)：卫星数据 3D 可视化工具。这是一个为非专业人士开发的开源天体力学工具，支持查看卫星数据、模拟卫星发射和解体等功能，适合用于教育和科普等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/77081817.png' style="max-width:80%; max-height=80%;"></img></p>

37、[openhaystack](https://hellogithub.com/periodical/statistics/click?target=https://github.com/seemoo-lab/openhaystack)：利用苹果网络实现物品追踪的框架。该项目是基于苹果的 Find My 网络，实现跨设备的定位与追踪。它通过将支持蓝牙的设备转化为类似 AirTag 的追踪器，轻松定位个人物品的位置，方便找回。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/341208122.jpg' style="max-width:80%; max-height=80%;"></img></p>

38、[ping-clock](https://hellogithub.com/periodical/statistics/click?target=https://github.com/turingbirds/ping-clock)：显示网络延迟的时钟。这是一个自制的时钟，用于显示 ping 指令的响应时间，整体造价约为 150 欧元。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/284364418.gif' style="max-width:80%; max-height=80%;"></img></p>

39、[spotube](https://hellogithub.com/periodical/statistics/click?target=https://github.com/KRTirtho/spotube)：开源的 Spotify 客户端。该项目是基于 Flutter 开发的 Spotify 客户端，完全免费且无广告。它使用 Spotify、JioSaavn 和 YouTube 作为音乐源，用户无需登录即可自由下载音乐，支持桌面和移动设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/104/338719962.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
40、[copenhagen](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pilcrowonpaper/copenhagen)：《Web 应用认证实现指南》。这是一本介绍如何在 Web 应用中实现认证（auth）的书籍，内容涵盖设计认证流程、存储用户凭据、保护用户数据等方面的指导与建议。

41、[php-the-right-way](https://hellogithub.com/periodical/statistics/click?target=https://github.com/codeguy/php-the-right-way)：《PHP: The Right Way》。这是一本适合初学者进阶的 PHP 书籍，介绍了 PHP 的最佳实践和编码规范，已被翻译成包括中文在内的多国语言。



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub103.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub105.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/104'>这里</a>。
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
