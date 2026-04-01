# 《HelloGitHub》第 98 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/98) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[cmus](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cmus/cmus)：小巧的命令行音乐播放器。这是一个专为类 Unix 系统设计的轻量级命令行音乐播放器，可以播放本地的音乐文件。它简单易用、占用资源少、启动速度快，支持多种音频格式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/7365136.png' style="max-width:80%; max-height=80%;"></img></p>

2、[Remotery](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Celtoys/Remotery)：轻量级的远程实时 CPU/GPU 分析器。该项目是用于监控 CPU 和 GPU 上多线程活动的工具。它提供了一个 C 文件，可轻松集成到项目中，并配备了一个实时监控 Web 界面，可通过浏览器远程观察和分析程序的性能。适用于监控游戏的实时运行性能和分析移动端应用的性能等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/17664381.gif' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[RunCat365](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Kyome22/RunCat365)：在 Windows 任务栏飞奔的“小猫”。这是一个用 C# 写的小工具，它会在 Windows 任务栏显示一只奔跑的小猫动画，CPU 使用率越高它跑得越快。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/285618804.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[caesium-image-compressor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Lymphatus/caesium-image-compressor)：免费的图片压缩软件。这是一款用 C++ 编写的图片压缩工具，它拥有简洁的中文界面，支持 JPG、PNG 和 WebP 格式的无损压缩，同时配备了实时预览和批量处理的功能。此外，还提供了 Windows、Linux 和 macOS 客户端，以及无需安装的 Web 版本。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/48986680.png' style="max-width:80%; max-height=80%;"></img></p>

5、[concurrentqueue](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cameron314/concurrentqueue)：C++ 的高性能无锁并发队列。该项目是用 C++11 编写的快速、无锁、并发队列，支持多个线程同时进行生产者和消费者操作。它具有无需使用锁和单头文件的特点，适用于需要高性能并发处理的各种场景。
```c++
#include "concurrentqueue.h"

moodycamel::ConcurrentQueue<int> q;
q.enqueue(25);

int item;
bool found = q.try_dequeue(item);
assert(found && item == 25);
```

6、[input-overlay](https://hellogithub.com/periodical/statistics/click?target=https://github.com/univrsal/input-overlay)：显示用户操作输入的 OBS 直播插件。该项目是用来在直播中显示键盘按键、鼠标移动和游戏手柄按钮的插件，适用于 Windows 和 Linux 上的 OBS 直播软件，可用于游戏直播和教学演示等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/99977220.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
7、[fscan](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shadow1ng/fscan)：开源的内网安全扫描工具。该项目是用 Go 语言开发的内网扫描工具，提供了一键自动化全方位的漏洞扫描。它使用方便、功能全面，支持端口扫描、常见的服务器爆破、Web 应用漏洞扫描、NetBIOS 嗅探等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/312629343.png' style="max-width:80%; max-height=80%;"></img></p>

8、[go-humanize](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dustin/go-humanize)：让数字和时间更容易理解的 Go 语言库。这是一个提供人性化数字和时间的 Go 语言库，它通过提供格式化函数，帮助开发者将大小和时间等数字转化为更易于人类理解的形式，比如文件大小、相对时间、逗号分隔的数字、序数词等。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享
```go
fmt.Printf("That file is %s.", humanize.Bytes(82854982)) // That file is 83 MB.
fmt.Printf("This was touched %s.", humanize.Time(someTimeInstance)) // This was touched 7 hours ago.
```

9、[mactop](https://hellogithub.com/periodical/statistics/click?target=https://github.com/context-labs/mactop)：专为苹果芯片打造的 Mac 性能监控工具。该项目用不到 1k 行的 Go 代码，实现了一个类似 top 命令的工具。它可以实时显示 Apple M 系列芯片的性能指标，包括 CPU、GPU 使用率、内存、网络和硬盘等信息。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/789247155.png' style="max-width:80%; max-height=80%;"></img></p>

10、[micro](https://hellogithub.com/periodical/statistics/click?target=https://github.com/micro-editor/micro)：现代化的终端文本编辑器。这个项目是用 Go 写的基于终端的文本编辑器，可作为 Nano 的替代品。它下载即用、无需配置、跨平台，支持多光标编辑、语法高亮、鼠标、插件扩展等功能，特别适合在 SSH 远程连接服务器时进行文本编辑工作。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/53632140.png' style="max-width:80%; max-height=80%;"></img></p>

11、[superfile](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yorukot/superfile)：非常漂亮的终端文件管理器。这是一个现代终端文件管理器，为命令行文件操作提供了一个直观且漂亮的界面。它默认采用 Vim 风格的快捷键操作，还支持插件和主题自定义。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/774468912.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[Acode](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Acode-Foundation/Acode)：Android 手机上的代码编辑器。这是一款专为 Android 设备设计的代码编辑工具，它是轻量级的 Web IDE，具有即时预览、控制台和丰富的插件等特点，支持 HTML、Python、Java、JavaScript 等多种编程语言。来自 [@虾华](https://hellogithub.com/user/ckl6eKxwCuRyVJI) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/217150613.png' style="max-width:80%; max-height=80%;"></img></p>

13、[blossom](https://hellogithub.com/periodical/statistics/click?target=https://github.com/blossom-editor/blossom)：私有部署的云端双链笔记软件。这是一个支持私有部署的云端存储双链笔记软件，可以将你的所有笔记、图片、个人计划安排保存在私有服务器上，并实现跨设备的实时同步。它提供 Markdown 编辑、双链笔记、全量备份、网页转换、多账号权限和统计等功能，兼容 Windows、macOS 和网页客户端。来自 [@猎隼丶止戈reNo7](https://hellogithub.com/user/Ew59HqRWjPe0zZO) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/675481198.png' style="max-width:80%; max-height=80%;"></img></p>

14、[JSqlParser](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JSQLParser/JSqlParser)：解析 SQL 语句的 Java 库。该项目可以读取 SQL 语句，并分解成结构化的 Java 对象，实现用 Java 代码解析或动态生成 SQL 语句，支持 SQL 标准和主流的关系型数据库。
```java
String sqlStr = "select 1 from dual where a=b";

PlainSelect select = (PlainSelect) CCJSqlParserUtil.parse(sqlStr);

SelectItem selectItem =
        select.getSelectItems().get(0);
Assertions.assertEquals(
        new LongValue(1)
        , selectItem.getExpression());

Table table = (Table) select.getFromItem();
Assertions.assertEquals("dual", table.getName());

EqualsTo equalsTo = (EqualsTo) select.getWhere();
Column a = (Column) equalsTo.getLeftExpression();
Column b = (Column) equalsTo.getRightExpression();
Assertions.assertEquals("a", a.getColumnName());
Assertions.assertEquals("b", b.getColumnName());
```

15、[odc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/oceanbase/odc)：企业级数据库协同开发平台。该项目是提供数据库协同开发和数据管理的平台，专为提升 SQL 开发效率而设计。它基于 Spring Boot 和 Electron 构建，提供了 Web 和桌面客户端，支持 SQL 规范检查、变更回滚、数据生命周期管理、数据脱敏和操作审计等功能，兼容 OceanBase、Oracle、MySQL 和 Doris 等多种数据源。来自 [@XiaoYangGzeyP](https://hellogithub.com/user/QfYG9d5Kt2nqWPJ) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/675901913.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
16、[papermark](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mfts/papermark)：开源的文件分享平台。该项目作为 DocSend 服务的开源替代方案，提供了自托管、简单易用的文档分享功能。它采用 Next.js+Tailwind CSS 构建，用户仅需上传文档，就能获得一个可在线访问文件内容的地址，并支持自定义域名和访问数据追踪等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/646985602.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[plane](https://hellogithub.com/periodical/statistics/click?target=https://github.com/makeplane/plane)：开源的项目管理和问题跟踪平台。该项目是开源的项目管理系统，旨在简化团队的项目管理流程。它易于使用、可自托管，支持问题跟踪、周期管理、项目分解和分析统计等功能，可作为 JIRA 的替代品。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/568098118.png' style="max-width:80%; max-height=80%;"></img></p>

18、[swr](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vercel/swr)：用于数据请求的 React Hooks 库。该项目是帮助开发者简化数据请求逻辑的 React 库，支持自动处理数据的缓存、重验证、错误重试等多种功能，比如当用户重新点击/回到页面时，自动请求接口获取最新数据。
```javascript
import useSWR from 'swr'
 
function Profile() {
  const { data, error, isLoading } = useSWR('/api/user', fetcher)
 
  if (error) return <div>failed to load</div>
  if (isLoading) return <div>loading...</div>
  return <div>hello {data.name}!</div>
}
```

19、[undraw-ui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/readpage/undraw-ui)：基于 Vue 3 的评论组件。这是一个基于 Vue 3 的 UI 组件，提供了评论、内容折叠、回复、表情等功能，以及目录、搜索等组件。来自 [@Mr.King](https://hellogithub.com/user/fUDKIpV5ohlc3qb) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/479253212.png' style="max-width:80%; max-height=80%;"></img></p>

20、[uppy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/transloadit/uppy)：易于集成的 JavaScript 文件上传组件。这是一个轻量级的 JavaScript 文件上传组件，它提供了一个美观的用户界面，支持从多个源导入文件、断点续传、国际化，以及预览、编辑和多文件上传的功能。
```javascript
import React, { useEffect } from 'react'
import Uppy from '@uppy/core'
import Webcam from '@uppy/webcam'
import { Dashboard } from '@uppy/react'

const uppy = new Uppy().use(Webcam)

function Component () {
  return <Dashboard uppy={uppy} plugins={['Webcam']} />
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/46273445.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
21、[Lemuroid](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Swordfish90/Lemuroid)：Android 设备上的全能游戏模拟器。这款基于 Libretro 的多合一游戏模拟器，能够让你在 Android 设备上玩各种怀旧游戏。它提供了即时存档、本地多人游戏和自定义按键等功能，支持模拟 NES、GBA、3DS、PSP 等多种游戏机。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/226883777.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
22、[buku](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jarun/buku)：强大的浏览器书签管理工具。这是一款开源的书签命令行管理工具，它轻量、隐私安全且易于使用，支持从主流浏览器导入书签、自动获取书签信息、跨平台同步和强大的搜索功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/45355064.png' style="max-width:80%; max-height=80%;"></img></p>

23、[flagsmith](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Flagsmith/flagsmith)：轻松管理功能开关和配置的平台。这是一个开源、功能齐全的特征标志（Feature flag）和远程配置平台，专为中小型团队设计。它是基于 Django REST framework 构建的 Web 应用，用于管理应用功能的开关和远程配置，支持 A/B 测试、多变量测试和组织管理等功能，适用于逐步推出新功能、进行市场测试、环境管理等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/136163130.png' style="max-width:80%; max-height=80%;"></img></p>

24、[marimo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/marimo-team/marimo)：创新的响应式 Python 笔记本。该项目是专为 Python 设计的响应式笔记本(notebook)，即在与 UI 交互时自动执行并更新所依赖的代码单元格，从而保证代码和输出的一致性。它以纯 Python 文件的形式存储，便于管理和运行，支持作为脚本执行或部署为可交互的 Web 应用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/678526156.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[umap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lmcinnes/umap)：高维数据降维的 Python 库。该项目是用于将高维数据映射到低维空间的 Python 库，帮助研究人员理解复杂数据集。与 t-SNE 相比，它在保持数据全局结构方面更加出色，能够高效地执行高维到低维的映射，适用于数据可视化、特征提取和聚类分析等多种场景。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享
```python
import umap
from sklearn.datasets import load_digits

digits = load_digits()

mapper = umap.UMAP().fit(digits.data)
umap.plot(mapper, labels=digits.target)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/95995403.png' style="max-width:80%; max-height=80%;"></img></p>

26、[Windrecorder](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yuka-friends/Windrecorder)：你的个人屏幕记忆搜索工具。该项目是专为 Windows 设计的屏幕记录工具，并提供搜索和回放功能。它会持续录制屏幕内容，同时保证数据安全（不上传、不联网），利用 OCR 和图片识别技术，让用户可以轻松搜索和回看屏幕活动历史。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/672537073.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
27、[bacon](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Canop/bacon)：后台运行的 Rust 代码检查工具。这是一个专为 Rust 语言设计的后台代码检查工具，它可以在后台运行，并即时地向开发者提供关于 Rust 代码的警告、错误和测试失败的反馈，让开发者专注于编写代码，而不是频繁地手动运行检查命令。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/308327979.png' style="max-width:80%; max-height=80%;"></img></p>

28、[bandwhich](https://hellogithub.com/periodical/statistics/click?target=https://github.com/imsnif/bandwhich)：查看带宽使用情况的命令行工具。这是一个开源的命令行网络带宽监控工具，它可以实时显示网络使用情况，包括进程、连接和远程地址等信息。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/206874323.png' style="max-width:80%; max-height=80%;"></img></p>

29、[rust-by-practice](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sunface/rust-by-practice)：Rust 语言实战。该项目提供了大量的 Rust 实战练习，来帮助 Rust 新手学习和上手 Rust 语言。这里除了有大量的练习题和答案，还支持在线编辑和运行 Rust 代码。

### Swift 项目
30、[MacSymbolicator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/inket/MacSymbolicator)：符号化 macOS/iOS 崩溃报告的工具。这是一个简单的 Mac 应用，它能够将 macOS/iOS 崩溃报告中的十六进制地址，转换为源码中的函数和行号，帮助开发者分析应用的崩溃原因，支持 crash 和 ips 格式的崩溃报告。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/31854735.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
31、[facefusion](https://hellogithub.com/periodical/statistics/click?target=https://github.com/facefusion/facefusion)：开源的 AI 换脸和增强工具。这是一款功能强大的人脸交换和增强工具，支持将图片/视频中的人脸替换成另一个人的脸、改善人脸和背景清晰度等功能，还提供了友好的 Web 界面（WebUI）和低门槛的 CPU 处理选项。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/679869950.png' style="max-width:80%; max-height=80%;"></img></p>

32、[litellm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BerriAI/litellm)：简化大模型 API 调用的工具。该项目能够将各种 AI 大模型和服务的接口，统一转换成 OpenAI 的格式，简化了在不同 AI 服务/大模型切换和管理的工作。此外，它还支持设置预算、限制请求频率、管理 API Key 和配置 OpenAI 代理服务器等功能。
```python
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["COHERE_API_KEY"] = "your-cohere-key"

messages = [{ "content": "Hello, how are you?","role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion(model="command-nightly", messages=messages)
print(response)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/671269505.gif' style="max-width:80%; max-height=80%;"></img></p>

33、[llama3-from-scratch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/naklecha/llama3-from-scratch)：从头开始实现 Llama 3 的教程。该项目通过逐层构建 Llama 3 的方式，帮助人们深入理解 LLM 是如何工作的。作者使用 PyTorch 框架，实现了加载模型权重、文本的分词处理、模型配置以及逐层实现 Transformer 模型中的关键组件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/802916901.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
34、[cloudflare_temp_email](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dreamhunter2333/cloudflare_temp_email)：免费搭建临时邮箱服务。该项目通过 CloudFlare 的免费服务，提供一个功能完备的临时邮箱服务，支持收发邮件、访问密码、自动回复、查看附件等功能。来自 [@Dream Hunter](https://hellogithub.com/user/FxNypXK7UQ9OECT) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/678900558.png' style="max-width:80%; max-height=80%;"></img></p>

35、[docs-linux-kernel-labs-zh-cn](https://hellogithub.com/periodical/statistics/click?target=https://github.com/linux-kernel-labs-zh/docs-linux-kernel-labs-zh-cn)：Linux 内核实验。该项目是布加勒斯特理工大学的《Linux 内核教学》课程的中文翻译版，适合对 Linux 内核感兴趣的程序员学习。课程内容分为课程和实验两部分，其中实验是在基于 QEMU 的虚拟机中进行，亲身体验 Linux 内核的开发、构建、部署及执行过程。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/720977650.png' style="max-width:80%; max-height=80%;"></img></p>

36、[LapisCV](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BingyanStudio/LapisCV)：开箱即用的简历模板。该项目提供了适用于 Obsidian 和 Typora 的简历模板，它基于 Markdown 格式、编辑方便、所见即所得，设计简洁且正式，借助编辑器可直接导出 PDF 格式的简历。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/767730706.png' style="max-width:80%; max-height=80%;"></img></p>

37、[OV-Watch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/No-Chicken/OV-Watch)：低成本的开源智能手表。这是一个制作成本仅需 80 元的智能手表项目，它不仅提供了基本的手表功能，还支持睡眠模式、蓝牙、计步、卡包、指南针和心率测量等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/637258361.jpg' style="max-width:80%; max-height=80%;"></img></p>

38、[phonedata](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xluohome/phonedata)：手机号码归属地信息库。该项目整理了超过 40 多万条中国手机号段和归属地信息，数据均来自网上的公开数据。

### 开源书籍
39、[LLMBook-zh.github.io](https://hellogithub.com/periodical/statistics/click?target=https://github.com/LLMBook-zh/LLMBook-zh.github.io)：《大语言模型》。这是一本为想入门大模型技术的程序员/学生准备的开源书籍，内容不仅涵盖了大模型的基础原理和关键技术，还提供了配套的代码工具库和大模型，帮助读者快速入门并实践。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/786642156.jpg' style="max-width:80%; max-height=80%;"></img></p>

40、[raytracing.github.io](https://hellogithub.com/periodical/statistics/click?target=https://github.com/RayTracing/raytracing.github.io)：《Ray Tracing in One Weekend》系列书籍。这是一套光线追踪技术的入门书籍，教你用 C++ 实现一个光线追踪器。光线追踪（Ray Tracing）是一种计算机图形学中的渲染技术，能够通过模拟光线在虚拟场景中的传播，生成出栩栩如生的真实感图像。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/197663980.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub97.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub99.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/98'>这里</a>。
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
