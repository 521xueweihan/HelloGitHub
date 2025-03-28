# 《HelloGitHub》第 106 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/106) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[sshfs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/libfuse/sshfs)：通过 SSH 挂载远程文件系统的工具。这是一个基于 SFTP 协议的文件系统工具，可通过 SSH 协议将远程文件系统挂载到本地。它操作简单，仅需一条命令，即可像访问本地文件系统一样管理远程文件和目录，兼容 Linux、BSD 和 macOS 系统。
```
挂载文件系统
sshfs [user@]hostname:[directory] mountpoint
卸载文件系统
fusermount -u mountpoint
```

### C# 项目
2、[mRemoteNG](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mRemoteNG/mRemoteNG)：集成多协议的远程连接管理工具。这是一款功能强大的远程连接管理工具，支持 RDP、VNC、SSH 等多种主流协议。它提供了标签式界面，用户可同时管理和切换多个远程连接，支持 Windows 11、10 等系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/460848.png' style="max-width:80%; max-height=80%;"></img></p>

3、[msstyleEditor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nptr/msstyleEditor)：开箱即用的 Windows 视觉样式编辑器。这是一款用于编辑 Windows 视觉样式（.msstyles 文件）的工具，兼容 Windows 7、8、10 和 11 系统。它无需安装、开箱即用，支持快速查看所有组件并修改其属性，轻松自定义主题样式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/93086337.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[Memento](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ripose-jp/Memento)：边看视频边学日语的视频播放器。这是一款基于 mpv 的开源视频播放器，专为学习日语而设计。它能够帮助用户在观看视频时学习日语，支持弹出式词典、字幕浏览、生成和同步生词卡等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/302477133.png' style="max-width:80%; max-height=80%;"></img></p>

5、[mixxx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mixxxdj/mixxx)：免费开源的 DJ 混音软件。该项目是一款用 C++ 开发的专业级 DJ 软件，完全免费。它提供了丰富的功能和硬件兼容性，支持自动 BPM 检测、实时效果处理、录音和直播等功能，适用于 Windows、macOS 和 Linux 平台。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/10126031.png' style="max-width:80%; max-height=80%;"></img></p>

6、[parallel-hashmap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/greg7mdp/parallel-hashmap)：高性能的 HashMap 库。该项目提供了多种高性能、内存友好、线程安全的哈希表和 B 树容器实现。它基于 Google 的 Abseil 库进行开发和优化，支持 C++11 标准和头文件形式，无需编译即可直接使用。
```c++
#include <iostream>
#include <string>
#include <parallel_hashmap/phmap.h>

using phmap::flat_hash_map;

int main()
{
    flat_hash_map<std::string, std::string> nickname =
    {
        { "tom",  "tomcat"},
        { "jim",  "jimoby"}
    };

    for (const auto& n : nickname)
        std::cout << n.first << "'s nickname is: " << n.second << "\n";

    email["bill"] = "hellogithub";
    std::cout << "bill's nickname is: " << nickname["bill"] << "\n";

    return 0;
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/173454206.png' style="max-width:80%; max-height=80%;"></img></p>

7、[upx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/upx/upx)：压缩可执行文件的工具。这是一款开源的可执行文件压缩工具，支持多种可执行文件格式（Windows、Linux、macOS）。它拥有出色的压缩比（50-70%），压缩后的文件可直接运行，适用于程序分发和大规模存储的场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/67031040.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[bunster](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yassinebenaid/bunster)：一键“编译” shell 脚本的工具。该项目是一个 Shell-to-Go 转译器（Transpiler），原理是先把 shell 脚本转换为 Go 代码，然后利用 Go 工具链将其编译为二进制可执行文件，弥补了传统 shell 脚本在性能、可移植性和安全性方面的不足。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/831420946.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[daytona](https://hellogithub.com/periodical/statistics/click?target=https://github.com/daytonaio/daytona)：简化开发环境搭建的工具。该项目可以通过一条命令，快速创建一个配置好的开发环境，支持与主流 IDE 无缝集成，以及本地机器、远程服务器、云平台等多种基础设施。来自 [@IZRINO](https://hellogithub.com/user/eK0Bv1dmJPxnrwy) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/753490180.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[gopher-lua](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yuin/gopher-lua)：将 Lua 脚本嵌入 Go 程序。这是一个 Go 语言实现的 Lua 虚拟机和编译器，完全兼容 Lua5.1 语法。开发者可以通过简单的代码，将 Lua 脚本嵌入到 Go 应用中，适用于游戏开发、自动化工具和插件系统等需要脚本化支持的场景。来自 [@两双筷子sqldc](https://hellogithub.com/user/5dGtvaZ6H3L4QMY) 的分享
```go
L := lua.NewState()
defer L.Close()
if err := L.DoString(`print("hello")`); err != nil {
    panic(err)
}
```

11、[SamWaf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/samwafgo/SamWaf)：开源的轻量级 Web 应用防火墙。这是一款完全开源的轻量级 Web 应用防火墙，支持私有化部署，提供 Bot 检测、URL 白名单、CC 防护、自定义防护规则等功能，适用于小型企业、工作室和个人网站。来自 [@猎隼丶止戈reNo7](https://hellogithub.com/user/Ew59HqRWjPe0zZO) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/737285725.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[mzt-biz-log](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mouzt/mzt-biz-log)：开箱即用的 Spring Boot 操作日志组件。这是一个为 Spring Boot 项目设计的操作日志组件，支持通过注解的方式，轻松记录业务操作日志，包括操作人、操作时间、操作内容等。来自 [@FangPengbo](https://hellogithub.com/user/WtxAwC6DlVhTEJO) 的分享
```java
@LogRecord(
        fail = "创建订单失败，失败原因：「{{#_errorMsg}}」",
        success = "{{#order.purchaseName}}下了一个订单,购买商品「{{#order.productName}}」,测试变量「{{#innerOrder.productName}}」,下单结果:{{#_ret}}",
        type = LogRecordType.ORDER,
        bizNo = "{{#order.orderNo}}")
public boolean createOrder(Order order) {
    log.info("【创建订单】orderNo={}", order.getOrderNo());

    // db insert order
    Order order1 = new Order();
    order1.setProductName("内部变量测试");

    LogRecordContext.putVariable("innerOrder", order1);

    return true;
}
```

13、[poi-tl](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Sayi/poi-tl)：Java 的 Word 模板引擎。该项目是基于 Apache POI 的 Word 模板引擎，可以动态生成 Word 文档。它提供了友好的 API，支持文本、图片、表格、条件渲染、图表等多种内容的渲染，适用于批量生成合同、报告、通知、证书等场景。
```java
XWPFTemplate template = XWPFTemplate.compile("template.docx").render(
  new HashMap<String, Object>(){{
    put("title", "HelloGitHub");
}});  
template.writeAndClose(new FileOutputStream("output.docx")); 
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/32567673.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
14、[openmtp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ganeshrvel/openmtp)：Mac 上的 Android 文件传输工具。这是一个专为 macOS 设计的开源 Android 文件传输工具。通过 USB 连接，实现 macOS 与 Android 设备之间快速稳定的文件传输，支持 macOS 11.0 及以上版本。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/161636751.png' style="max-width:80%; max-height=80%;"></img></p>

15、[readest](https://hellogithub.com/periodical/statistics/click?target=https://github.com/readest/readest)：沉浸式的电子书阅读器。这是一款为热爱阅读的用户量身打造的阅读软件，将极简设计与强大功能融合，为你带来专注、沉浸的阅读体验。它基于 Next.js 和 Tauri 开发，支持跨平台运行，现已支持 macOS、Windows、Linux 和 Web 平台，未来还将推出 iOS 和 Android 版本，实现真正的全平台覆盖。来自 [@Huang Xin](https://hellogithub.com/user/eRLUbPOy2qZtDgw) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/871781831.png' style="max-width:80%; max-height=80%;"></img></p>

16、[sharp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lovell/sharp)：高性能的 Node.js 图像处理库。这是一个基于 libvips 的高性能 Node.js 图像处理库，支持对 JPEG、PNG、WebP、GIF 和 SVG 等格式的图像进行调整大小、格式转换、裁剪和旋转等操作。
```javascript
const semiTransparentRedPng = await sharp({
  create: {
    width: 48,
    height: 48,
    channels: 4,
    background: { r: 255, g: 0, b: 0, alpha: 0.5 }
  }
})
  .png()
  .toBuffer();
```

17、[stretchly](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hovancik/stretchly)：跨平台的休息提醒助手。这是一款跨平台的 Electron 应用，旨在通过定时休息提醒，帮助用户养成健康的工作习惯，支持包括中文在内的多种语言，并提供自定义休息间隔、时长、提示音效等个性化设置。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/63014033.png' style="max-width:80%; max-height=80%;"></img></p>

18、[svgl](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pheralb/svgl)：精美的 Logo 资源库。该项目是基于 SvelteKit 和 Tailwind CSS 构建的在线 Logo 库，收录了 400 多种标志和文字商标，覆盖技术、编程语言、框架、公司等分类，支持一键下载和复制代码。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/448688478.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
19、[AndroidEasterEggs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hushenghao/AndroidEasterEggs)：Android 系统彩蛋大全。该项目收集了各种 Android 系统彩蛋，包含完整的代码和体验等功能。来自 [@p0ssword](https://hellogithub.com/user/GxAPw47k9KVOyhM) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/306645388.png' style="max-width:80%; max-height=80%;"></img></p>

20、[Maestro](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mobile-dev-inc/Maestro)：移动端 UI 自动化测试框架。这是一款开源的移动端和 Web 应用 UI 自动化测试工具，它采用简单易懂的 YAML 语法编写测试脚本，内置容错机制和操作延迟容忍功能，支持 Android、iOS、Flutter 和桌面浏览器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/476427476.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
21、[chonkie](https://hellogithub.com/periodical/statistics/click?target=https://github.com/chonkie-ai/chonkie)：轻量级的文本分块 Python 库。这是一个专为 RAG 应用设计的轻量级文本分块库，它简单易用、速度快，能够按固定大小分割文本，支持多种分词器、向量模型和灵活的分块策略，适用于长文本处理、构建 RAG 应用等场景。
```python
from chonkie import TokenChunker
from tokenizers import Tokenizer

tokenizer = Tokenizer.from_pretrained("gpt2")
chunker = TokenChunker(tokenizer)

chunks = chunker("HelloGitHub! Chonkie, the chunking library is so cool! I love the tiny hippo hehe.")

for chunk in chunks:
    print(f"Chunk: {chunk.text}")
    print(f"Tokens: {chunk.token_count}")
```

22、[fonttools](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fonttools/fonttools)：操作字体文件的 Python 库。这是一个用于编辑和转换字体文件的 Python 库，支持 TrueType 和 OpenType 字体与 XML 格式（TTX）之间的相互转换，兼容多种字体格式，适用于编辑、调试和优化字体等场景。
```python
from fontTools.afmLib import AFM

f = AFM("Tests/afmLib/data/TestAFM.afm")
print(f["A"])
# (65, 668, (8, -25, 660, 666))

f.FontName = "TestFont HelloGitHub"
f.write("testfont-hellogithub.afm")
```

23、[httpdbg](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cle-b/httpdbg)：轻松捕获 Python 程序中 HTTP(S) 请求的工具。该项目是用于帮助开发者调试 Python 程序中的 HTTP(S) 请求的工具。通过 pyhttpdbg 命令运行程序，即可在浏览器中查看发出的 HTTP 请求，支持脚本运行、交互式控制台、单元测试多种运行模式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/273906263.png' style="max-width:80%; max-height=80%;"></img></p>

24、[pwndbg](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pwndbg/pwndbg)：专为逆向工程设计的 GDB/LLDB 插件。这是一个专为 GDB 和 LLDB 调试器设计的插件，支持寄存器状态显示、内存搜索、内存泄漏查找等功能，适用于底层软件开发、硬件调试和逆向工程等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/31181767.png' style="max-width:80%; max-height=80%;"></img></p>

25、[PyPSA](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PyPSA/PyPSA)：电力系统分析 Python 库。这是一个用于电力系统分析的 Python 库，专注于电力和多能源系统的建模与优化。它基于 Pandas、NumPy、GLPK、Cbc 等库，能够高效计算最优潮流优化（OPF）、线性和非线性电力流，并支持模拟各种电力和能源系统组件的功能。
```python
import pypsa

# create a new network
n = pypsa.Network()
n.add("Bus", "mybus")
n.add("Load", "myload", bus="mybus", p_set=100)
n.add("Generator", "mygen", bus="mybus", p_nom=100, marginal_cost=20)

# load an example network
n = pypsa.examples.ac_dc_meshed()

# run the optimisation
n.optimize()

# plot results
n.generators_t.p.plot()
n.plot()

# get statistics
n.statistics()
n.statistics.energy_balance()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/49414256.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
26、[aquascope](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cognitive-engineering-lab/aquascope)：可视化 Rust 代码执行过程的工具。这是一个 Rust 代码可视化的工具，直观展示代码的编译和运行细节，帮助开发者理解 Rust 语言的运行机制。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/537217688.png' style="max-width:80%; max-height=80%;"></img></p>

27、[code2prompt](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mufeedvh/code2prompt)：将代码库转换为 LLM 提示的工具。这是一个 Rust 写的命令行工具，能够将代码库快速转换为适用于 LLM 的提示词（Markdown 文件）。它会自动遍历目录，生成代码结构树并整合到提示词中，同时支持提示词模板、Token 计算、生成 Git 提交信息、文件筛选等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/769564277.png' style="max-width:80%; max-height=80%;"></img></p>

28、[rpg-cli](https://hellogithub.com/periodical/statistics/click?target=https://github.com/facundoolano/rpg-cli)：将你的文件系统变成一个地牢游戏。这是一款用 Rust 编写的命令行 RPG 游戏，每次执行 cd 命令时，都可能遭遇敌人并触发回合制战斗（自动），游戏支持角色升级、物品、职业和宝箱等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/361019889.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
29、[boring.notch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TheBoredTeam/boring.notch)：将 MacBook 的刘海变成音乐控制中心。这是一款专为 macOS 设计的应用，可将原本单调的刘海区域变成一个炫酷的音乐控制中心，支持日历、AirDrop 和音乐控制等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/837073921.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[SwiftUI-Shimmer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/markiv/SwiftUI-Shimmer)：SwiftUI 闪烁效果动效库。这是一个轻量级的 SwiftUI 动效库，可以轻松为任意 SwiftUI 视图添加闪烁效果，支持自定义动画、渐变样式、闪烁速度等，适用于加载状态、占位符、骨架屏等场景。
```swift
Text("Custom Gradient Mode").bold()
    .font(.largeTitle)
    .shimmering(
        gradient: Gradient(colors: [.clear, .orange, .white, .green, .clear]),
        bandSize: 0.5,
        mode: .overlay()
    )
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/350812836.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
31、[AI-on-the-edge-device](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jomjol/AI-on-the-edge-device)：将“旧”设备接入数字世界。该项目基于 ESP32 等便宜的硬件（不到 10 欧）和 TensorFlow Lite 框架，实现对仪表数字的自动识别和数据传输，轻松将传统设备（水表、燃气表、电表）改造成智能设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/283280154.jpg' style="max-width:80%; max-height=80%;"></img></p>

32、[instructor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/instructor-ai/instructor)：让 LLM 输出结构化数据的 Python 库。该项目是用于处理大语言模型（LLMs）结构化输出的 Python 库。它基于 Pydantic 实现了数据验证和类型注释，能够将 LLM 的结果（自然语言）转换为结构化数据，支持多种大语言模型服务，以及自动重试、流式响应等功能。
```python
import instructor
from pydantic import BaseModel
from openai import OpenAI


# Define your desired output structure
class UserInfo(BaseModel):
    name: str
    age: int


# Patch the OpenAI client
client = instructor.from_openai(OpenAI())

# Extract structured data from natural language
user_info = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=UserInfo,
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(user_info.name)
#> John Doe
print(user_info.age)
#> 30
```

33、[lite.ai.toolkit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xlite-dev/lite.ai.toolkit)：轻量级的 C++ AI 工具包。这是一个用 C++ 编写的 AI 工具包，内置超过 100 种 AI 模型，包括对象检测、人脸识别、分割、抠图等领域。它支持 ONNXRuntime、MNN、NCNN、TNN 和 TensorRT 等主流推理引擎，帮助开发者快速部署和使用 AI 模型。来自 [@wangzijian](https://hellogithub.com/user/1NZpMjQFDvCfaEK) 的分享
```c++
#include "lite/lite.h"

int main(int argc, char *argv[]) {
  std::string onnx_path = "yolov5s.onnx";
  std::string test_img_path = "test_yolov5.jpg";
  std::string save_img_path = "test_results.jpg";

  auto *yolov5 = new lite::cv::detection::YoloV5(onnx_path); 
  std::vector<lite::types::Boxf> detected_boxes;
  cv::Mat img_bgr = cv::imread(test_img_path);
  yolov5->detect(img_bgr, detected_boxes);
  
  lite::utils::draw_boxes_inplace(img_bgr, detected_boxes);
  cv::imwrite(save_img_path, img_bgr);  
  delete yolov5;
  return 0;
}
```

34、[minimind](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jingyaogong/minimind)：从零开始训练小型语言模型。这不仅是一个微型语言模型的实现，更是一份入门 LLM 的教程，旨在降低学习和上手 LLM 的门槛。它提供了从数据预处理到模型训练、微调和推理的全流程代码和教程。最小模型仅 0.02B 参数，可在普通 GPU 上轻松运行。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/834369920.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
35、[flutter_slidable](https://hellogithub.com/periodical/statistics/click?target=https://github.com/letsar/flutter_slidable)：Flutter 的滑动操作组件。这是一个 Flutter 的开源库，可用于快速实现列表项的滑动操作，支持多方向、滑动动画、自动关闭等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/141008724.gif' style="max-width:80%; max-height=80%;"></img></p>

36、[inky-dashboard](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jaeheonshim/inky-dashboard)：电子墨水屏的待办事项和日历管理工具。这是一款低功耗的电子墨水屏待办事项和日历管理工具，硬件采用 Raspberry Pi Pico W 和 Inky Frame 7.3 英寸七色电子墨水屏，同时使用 LVGL 实现界面布局，支持多种颜色显示、待办事项、日历同步等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/900200373.jpg' style="max-width:80%; max-height=80%;"></img></p>

37、[nginx-proxy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nginx-proxy/nginx-proxy)：为 Docker 容器自动配置 Nginx 反向代理。该项目可以自动为 Docker 容器提供 Nginx 反向代理服务。它能够实时监听 Docker 容器的启动和停止事件，自动为每个 Docker 容器配置 Nginx 反向代理，无需手动干预，极大简化了容器环境下的 Nginx 配置流程。
```
# 第一步启动 nginx-proxy
docker run --detach \
    --name nginx-proxy \
    --publish 80:80 \
    --volume /var/run/docker.sock:/tmp/docker.sock:ro \
    nginxproxy/nginx-proxy:1.6

# 第二步启动应用
docker run --detach \
    --name your-proxied-app \
    --env VIRTUAL_HOST=hellogithub.com \
    nginx
```

38、[reference](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Fechin/reference)：为开发者准备的速查表。这是一份专为开发者准备的快速参考手册（cheat sheet）集合，旨在为开发者提供简洁、直观的速查表，内容涵盖多种编程语言、框架、Linux 命令和数据库等。来自 [@databook](https://hellogithub.com/user/1qC4w2Ey6bu0fgR) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/322855089.png' style="max-width:80%; max-height=80%;"></img></p>

39、[VoxelSpace](https://hellogithub.com/periodical/statistics/click?target=https://github.com/s-macke/VoxelSpace)：不到 20 行的地形渲染算法。这是一个用于地形渲染的算法，核心代码不到 20 行。它复现了经典游戏 Comanche 所采用的渲染技术（Voxel Space），为开发者提供了一个学习和参考的示例。
```python
def Render(p, height, horizon, scale_height, distance, screen_width, screen_height):
    # Draw from back to the front (high z coordinate to low z coordinate)
    for z in range(distance, 1, -1):
        # Find line on map. This calculation corresponds to a field of view of 90°
        pleft  = Point(-z + p.x, -z + p.y)
        pright = Point( z + p.x, -z + p.y)
        # segment the line
        dx = (pright.x - pleft.x) / screen_width
        # Raster line and draw a vertical line for each segment
        for i in range(0, screen_width):
            height_on_screen = (height - heightmap[pleft.x, pleft.y]) / z * scale_height. + horizon
            DrawVerticalLine(i, height_on_screen, screen_height, colormap[pleft.x, pleft.y])
            pleft.x += dx

# Call the render function with the camera parameters:
# position, height, horizon line position,
# scaling factor for the height, the largest distance, 
# screen width and the screen height parameter
Render( Point(0, 0), 50, 120, 120, 300, 800, 600 )
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/104589662.gif' style="max-width:80%; max-height=80%;"></img></p>

40、[zh-style-guide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yikeke/zh-style-guide)：中文技术文档写作风格指南。这是一个开源的中文技术文档写作规范指南，旨在为中文技术文档的语言风格、结构样式、内容元素、标点符号、格式排版等方面提供参考规范。

### 开源书籍
41、[Foundations-of-LLMs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ZJU-LLMs/Foundations-of-LLMs)：《大模型基础》。该书是由浙江大学 DAILY 实验室开源的大语言模型教材，内容涵盖传统语言模型、大语言模型架构演化、Prompt 工程、参数高效微调、模型编辑、检索增强生成等方面。来自 [@无间之钟](https://hellogithub.com/user/rnlYFdQcyhRm50p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/822044840.png' style="max-width:80%; max-height=80%;"></img></p>

42、[pytorch-deep-learning](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mrdbourke/pytorch-deep-learning)：《学习 PyTorch 进行深度学习：从零到精通》。该项目提供了丰富的图文教程、代码示例、视频讲解和实战项目，旨在通过实践的方式帮助初学者掌握 PyTorch 框架和深度学习技术。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/418718534.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub105.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub107.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/106'>这里</a>。
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
