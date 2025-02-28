# 《HelloGitHub》第 103 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/103) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[rawdrawandroid](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cnlohr/rawdrawandroid)：仅用 C 语言开发 Android 应用。这是一个 Android 应用开发框架，可以让开发者不用 Java，仅用 C 和 Make 开发 Android 应用。它轻量且跨平台，支持 OpenGL ES、陀螺仪、多点触控及 Android 键盘，并能直接访问 USB 设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/212012440.png' style="max-width:80%; max-height=80%;"></img></p>

2、[taisei](https://hellogithub.com/periodical/statistics/click?target=https://github.com/taisei-project/taisei)：免费开源的东方 Project 系列的射击游戏。该项目是基于东方 Project 世界观的弹幕射击类游戏，拥有独立原创的故事情节、音乐和游戏机制。这款名为“泰西”的游戏，采用 C11、SDL2 和 OpenGL 开发，完全免费且开源，支持在 Windows、Linux、macOS 和 Chrome 等浏览器上运行。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/977986.gif' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[Bulk-Crap-Uninstaller](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Klocman/Bulk-Crap-Uninstaller)：免费的 Windows 应用卸载神器。这是一个用 C# 开发的 Windows 软件卸载工具，能够快速删除大量不需要的应用程序。它完全免费、开箱即用，支持批量和强制卸载、清理残留文件、检测隐藏或受保护的已注册应用等功能。虽然面向 IT 专业人员设计，但其简单的默认设置，让任何人都能轻松上手。来自 [@猎隼丶止戈reNo7](https://hellogithub.com/user/Ew59HqRWjPe0zZO) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/64677873.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Macro-Deck](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Macro-Deck-App/Macro-Deck)：将手机变成 Stream Deck 的工具。该项目可以将手机、平板等带浏览器的设备变成类似 Stream Deck 的远程自定义按键板，实现一键执行单步或多步操作，适用于直播和简化日常任务等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/166713531.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[aria2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/aria2/aria2)：超快的命令行下载工具。这个跨平台命令行下载工具由 C++ 开发，支持 HTTP(S)、FTP、SFTP、BitTorrent 等多种协议。它操作简单、体积小、下载速度快，并提供后台运行、速度限制、分段下载和 BitTorrent 扩展等功能。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享

6、[fast_float](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fastfloat/fast_float)：速度与精准兼具的 C++ 数字解析库。该项目是用于快速解析数字字符串的 C++ 库，实现了类似 from_charts 函数的功能。它是一个速度极快、仅头文件的库，比标准库快数倍。支持解析 float、double 和整数类型的字符串，已被广泛应用在 Chromium、Redis 和 LLVM 等知名项目中。
```c++
#include "fast_float/fast_float.h"
#include <iostream>

int main() {
    const std::string input =  "3.1416 xyz ";
    double result;
    auto answer = fast_float::from_chars(input.data(), input.data()+input.size(), result);
    if(answer.ec != std::errc()) { std::cerr << "parsing failure\n"; return EXIT_FAILURE; }
    std::cout << "parsed the number " << result << std::endl;
    return EXIT_SUCCESS;
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/305438763.png' style="max-width:80%; max-height=80%;"></img></p>

7、[mame](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mamedev/mame)：开源的街机模拟器。这是一款支持海量街机游戏的模拟器。它通过模拟多种硬件平台，实现了在电脑上运行各种复古软件的功能。不仅支持街机，还有老式电脑和游戏机。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/14303048.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[beszel](https://hellogithub.com/periodical/statistics/click?target=https://github.com/henrygd/beszel)：轻量级高颜值的 Docker 监控平台。这是一个轻量级的服务器监控平台，包括 Docker 统计、历史数据和警报功能。它拥有友好的 Web 界面，配置简单、开箱即用，支持自动备份、多用户、OAuth 认证和 API 访问等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/825470378.png' style="max-width:80%; max-height=80%;"></img></p>

9、[envd](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tensorchord/envd)：高效的 AI 开发环境搭建工具。这是一个为 AI/ML 项目提供可复现开发环境的命令行工具。只需简单的配置语言和命令，即可快速创建基于容器的开发环境，支持远程构建、依赖缓存和导入远程仓库等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/480303698.png' style="max-width:80%; max-height=80%;"></img></p>

10、[gophish](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gophish/gophish)：开源的网络钓鱼平台。该项目提供了一个开箱即用的网络钓鱼平台，可用于模拟钓鱼攻击。它拥有友好的 Web 管理后台，支持邮件模板、批量发送邮件、网站克隆和数据可视化，适用于企业安全培训和渗透测试等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/14508450.png' style="max-width:80%; max-height=80%;"></img></p>

11、[opentofu](https://hellogithub.com/periodical/statistics/click?target=https://github.com/opentofu/opentofu)：实现基础设施即代码的开源方案。该项目是一个开源的基础设施即代码工具，专注于自动化地创建、管理和部署本地和云服务基础设施。作为 Terraform 的一个分支，它由社区驱动，支持使用高级配置语法描述基础设施、生成执行计划和构建资源依赖图，从而减少人为操作失误，实现复杂变更的自动化。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/679421146.png' style="max-width:80%; max-height=80%;"></img></p>

12、[photoview](https://hellogithub.com/periodical/statistics/click?target=https://github.com/photoview/photoview)：极简的照片管理平台。这是一款用于自建云相册的 Web 应用，它拥有直观的用户界面和丰富的功能，支持自动整理照片、生成缩略图、共享相册、EXIF 解析和多用户管理。还提供了 iOS 应用，方便用户在手机上访问。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/195657294.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
13、[GoGoGo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ZCShou/GoGoGo)：开源的 Android 虚拟定位应用。该项目是一个基于 Android 调试 API 和百度地图实现的虚拟定位工具，无需 ROOT 权限即可修改地理位置。它支持位置搜索和手动输入坐标，并提供了一个可自由移动的摇杆来模拟位移。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/434497397.jpg' style="max-width:80%; max-height=80%;"></img></p>

14、[karate](https://hellogithub.com/periodical/statistics/click?target=https://github.com/karatelabs/karate)：开源的 API 自动测试框架。这是一款基于 Java 的 API 测试框架，可与 Spring Boot、Maven 等 Java 生态系统无缝集成。它整合了 API 测试自动化、模拟、性能测试和 UI 自动化等功能，支持使用类似 Cucumber 的语法编写测试用例，并提供了一个跨平台的可执行文件，即使对 Java 不熟悉也能轻松上手。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/81226206.jpg' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
15、[icones](https://hellogithub.com/periodical/statistics/click?target=https://github.com/antfu-collective/icones)：极简的图标搜索网站。这是一个用于快速查找各种图标的网站，支持分类过滤和多选模式。用户可将选择的图标打包为字体或直接下载 SVG 格式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/278862095.png' style="max-width:80%; max-height=80%;"></img></p>

16、[media-chrome](https://hellogithub.com/periodical/statistics/click?target=https://github.com/muxinc/media-chrome)：打造现代化网页播放器界面的组件库。这是一个用于定制网页音频和视频播放器界面的库，兼容各种 JavaScript 框架。它高度可定制，开发者可以轻松调整组件的外观和功能，支持字幕、投屏、快捷键、倍速、预览缩略图、移动端和静音按钮等功能。
```html
<media-controller audio>
  <audio
    slot="media"
    src="xxxxxx"
  ></audio>
  <media-control-bar>
    <media-play-button></media-play-button>
    <media-time-display showduration></media-time-display>
    <media-time-range></media-time-range>
    <media-playback-rate-button></media-playback-rate-button>
    <media-mute-button></media-mute-button>
    <media-volume-range></media-volume-range>
  </media-control-bar>
</media-controller>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/208394975.jpg' style="max-width:80%; max-height=80%;"></img></p>

17、[Moe-Counter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/journey-ad/Moe-Counter)：可爱的网站计数器。该项目是一个用于统计页面访问人数的计数器。它不仅简单易用，还提供多种可爱风格的主题，用户可根据个人喜好进行选择。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/284698414.png' style="max-width:80%; max-height=80%;"></img></p>

18、[piscina](https://hellogithub.com/periodical/statistics/click?target=https://github.com/piscinajs/piscina)：灵活高效的 Node.js 线程池。该项目是用 TypeScript 编写的高性能 Node Worker 线程池，旨在简化 Node.js 多线程编程。它提供简单易用的 API，支持线程间通信、动态调整线程池大小、取消任务、设置内存限制和异步任务跟踪等功能。
```javascript
const path = require('path');
const Piscina = require('piscina');

const piscina = new Piscina({
  filename: path.resolve(__dirname, 'worker.js')
});

(async function() {
  const result = await piscina.run({ a: 4, b: 6 });
  console.log(result);  // Prints 10
})();
```

19、[swapy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TahaSh/swapy)：轻松实现拖动交换布局的库。该项目可以将任意布局转换为可拖动交换的形式，仅需几行代码即可实现。它支持设置交互动画，可以在 React、Vue、Svelte 等框架中使用，适用于各种需要交互式布局的场景。
```typescript
import { createSwapy } from 'swapy'

const container = document.querySelector('.container')

const swapy = createSwapy(container, {
  animation: 'dynamic' // or spring or none
})

// You can disable and enable it anytime you want
swapy.enable(true)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/829042475.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
20、[etchdroid](https://hellogithub.com/periodical/statistics/click?target=https://github.com/etchdroid/etchdroid)：在手机上制作 USB 启动盘的工具。这是一个开源的 Android 应用，专为在手机上制作操作系统 USB 启动盘而设计。它无需 ROOT 权限，即可将操作系统镜像写入 USB 设备，支持 Ubuntu、树莓派等多个系统，适用在无法使用电脑时制作启动 U 盘。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/147043230.png' style="max-width:80%; max-height=80%;"></img></p>

21、[KeyMapper](https://hellogithub.com/periodical/statistics/click?target=https://github.com/keymapperorg/KeyMapper)：Android 按键重映射应用。这是一个免费开源的 Android 应用，可以自定义 Android 设备的按键、指纹和手势操作。无需 ROOT 权限，支持蓝牙和有线键盘，提供灵活的按键重映射体验。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/141129812.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
22、[backtrader](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mementum/backtrader)：Python 量化交易回测框架。该项目是用 Python 编写的回测库，专为开发和测试交易策略而设计。它可以从 CSV 文件、在线数据源和 pandas 中提取数据，支持多策略同步运行、生成交易策略的可视化图表等功能。内置 100 多种指标，包括趋势、成交量和波动性等指标。
```python
from datetime import datetime
import backtrader as bt

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

data0 = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime(2011, 1, 1),
                                  todate=datetime(2012, 12, 31))
cerebro.adddata(data0)

cerebro.run()
cerebro.plot()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/29050338.png' style="max-width:80%; max-height=80%;"></img></p>

23、[core](https://hellogithub.com/periodical/statistics/click?target=https://github.com/home-assistant/core)：开源的智能家居平台。这是一个用 Python 编写的智能家居平台，旨在整合不同品牌的智能设备，提供个性化的家庭自动化体验。它解决了传统系统互操作性（Interoperability）差的问题，允许用户在同一平台上自由控制和联动 Apple HomeKit、米家、Aqara、涂鸦等设备，极大提升了智能家居的灵活性和便捷性。适合希望打破单一平台限制的用户，尤其是追求高性价比的 DIY 智能家居爱好者。来自 [@无间之钟](https://hellogithub.com/user/rnlYFdQcyhRm50p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/12888993.png' style="max-width:80%; max-height=80%;"></img></p>

24、[paperless-ngx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/paperless-ngx/paperless-ngx)：纸质文档数字化存档工具。这是一个基于 Django 的文档管理系统，可将纸质文档转换成可搜索的在线存档。不同于普通的扫描仪将实体书变为难以检索的图片或 PDF 格式，它通过文档扫描器实现电子化，转化为易于检索的格式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/458648791.png' style="max-width:80%; max-height=80%;"></img></p>

25、[pipreqs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/bndr/pipreqs)：快速生成 Python 项目依赖文件的工具。该项目可以根据 Python 项目中的导入语句，生成 requirements.txt 文件。它能够自动识别项目中使用的库，无需安装即可生成依赖库列表。

26、[pokeapi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PokeAPI/pokeapi)：宝可梦数据的 API 服务。这是一个基于 Django 构建的宝可梦数据 RESTful API 服务，为开发者提供全面的宝可梦数据库，包括小精灵的动作、属性、技能和进化信息等详细资料。

### Rust 项目
27、[insta](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mitsuhiko/insta)：Rust 的快照测试库。这是一个用于 Rust 项目的快照测试库，特别适用于参考值非常大或经常变化的场景。它提供了 VSCode 插件和命令行工具，当测试因参考值变动而失败时，可以通过 review 命令查看问题，并一键更新快照（参考值），从而快速通过单元测试。
```rust
fn split_words(s: &str) -> Vec<&str> {
    s.split_whitespace().collect()
}

#[test]
fn test_split_words() {
    let words = split_words("hello from the other side");
    insta::assert_yaml_snapshot!(words);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/165561258.gif' style="max-width:80%; max-height=80%;"></img></p>

28、[oha](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hatoo/oha)：Rust 驱动的 HTTP 压测工具。这是一个用 Rust 开发的 HTTP 请求压测工具，它操作简单、带 TUI 动画界面，支持生成请求延迟、吞吐量等指标的报告，以及动态 URL 和更灵活的请求间隔（burst-delay）等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/244377430.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[steel](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mattwparas/steel)：基于 Rust 的嵌入式 Scheme 解释器。这是一个用 Rust 编写的嵌入式 Scheme 解释器，旨在提供轻量级且快速的脚本语言支持。它解决了在嵌入式环境或小型应用中对高效、灵活脚本引擎的需求。来自 [@无间之钟](https://hellogithub.com/user/rnlYFdQcyhRm50p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/241949362.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
30、[aural-player](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kartik-venugopal/aural-player)：灵感来自 Winamp 的 macOS 音乐播放器。该项目是受经典的 Winamp 播放器启发，用 Swift 编程语言开发的适用于 macOS 的音乐播放器。它内置音效和均衡器，支持多种音频格式、回放、歌词显示、自定义界面等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/96710143.gif' style="max-width:80%; max-height=80%;"></img></p>

31、[DockDoor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ejbills/DockDoor)：适用于 macOS 的窗口预览工具。该项目是用 Swift 和 SwiftUI 开发的 Dock 窗口预览工具。只需将鼠标悬停在 Dock 上的应用图标，即可预览其打开的窗口，还支持类似 Windows 的 Alt+Tab 切换和自定义快捷键的功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/809906907.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
32、[moondream](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vikhyat/moondream)：小型的视觉语言模型。这是一个可在资源受限的设备上运行的小型视觉语言模型，它能够理解并生成与图像相关的自然语言描述，支持图像识别、生成描述和问答等功能。
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

image = Image.open('<IMAGE_PATH>')
enc_image = model.encode_image(image)
print(model.answer_question(enc_image, "Describe this image.", tokenizer))
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/736812439.png' style="max-width:80%; max-height=80%;"></img></p>

33、[Prompt_Engineering](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NirDiamant/Prompt_Engineering)：全面的提示工程实战指南。这份教程致力于帮助用户掌握与大型语言模型（LLM）沟通的技巧。内容涵盖从基础到高级的提示工程技术，附有详细的实现指南和示例代码。

34、[spaCy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/explosion/spaCy)：强大的自然语言处理 Python 库。这是一个工业级的自然语言处理（NLP）库，支持 70 多种语言的分词和训练。它采用 Python 编写，可实现标注、解析和文本分类等功能，并支持模型打包与部署。
```python
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
```

35、[ultralytics](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ultralytics/ultralytics)：先进的对象检测和跟踪模型。该项目是基于之前的 YOLO 版本，增加了新功能并改进了模型，在对象检测、跟踪、实例分割和图像分类等任务中表现出色。
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data="coco8.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("path/to/image.jpg")
results[0].show()

# Export the model to ONNX format
path = model.export(format="onnx")  # return path to exported model
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/535360445.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
36、[BilibiliSponsorBlock](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hanydd/BilibiliSponsorBlock)：B 站视频空降助手。这是一款能够自动跳过 B 站视频中恰饭片段和开场、结尾动画的浏览器插件，所有标注数据均由网友贡献，支持 Chrome、Edge 和 FireFox 浏览器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/744617272.png' style="max-width:80%; max-height=80%;"></img></p>

37、[cognitive-load](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zakirullin/cognitive-load)：降低开发者认知负荷的建议。这是一篇关于如何在软件开发过程中，降低认知负荷的文章。即简化代码、提高代码的可读性，减轻开发者在阅读和理解代码时的负担。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/642858415.png' style="max-width:80%; max-height=80%;"></img></p>

38、[dockerc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NilsIrl/dockerc)：将 Docker 镜像编译为独立可执行文件的工具。该项目能将 Docker 镜像转化为二进制可执行文件，无需配置 Docker 环境或安装依赖，简化了软件的分发和运行流程。来自 [@kero990](https://hellogithub.com/user/c3Y4NR1rq6neVoD) 的分享

39、[kubernetes-goat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/madhuakula/kubernetes-goat)：Kubernetes 安全攻防演练平台。该项目是用于构建漏洞百出、易受攻击的集群环境，让开发者可以在真实场景中学习 K8s 攻击和防御技巧。

40、[pilipala](https://hellogithub.com/periodical/statistics/click?target=https://github.com/guozhigq/pilipala)：开源的 bilibili 第三方客户端。该项目是用 Flutter 开发的 B 站第三方客户端，支持 Android 和 iOS 平台。它提供了推荐视频列表、热门直播、番剧、离线缓存、回复评论、弹幕和搜索等功能。来自 [@Micro·J](https://hellogithub.com/user/L2Xx0OfvPzpYt4u) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/629282922.png' style="max-width:80%; max-height=80%;"></img></p>

41、[Sensor-Watch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/joeycastillo/Sensor-Watch)：卡西欧 F-91W 手表的开源电路板。该项目是为经典 Casio F-91W 手表自制电路板，采用 ARM Cortex-M0+ 微控制器（SAM L22）。配备十位数段液晶显示屏、五个指示段、LED 背光和三个按钮，支持用户通过 USB 编程，在手表上运行自定义程序。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/356689400.jpg' style="max-width:80%; max-height=80%;"></img></p>

42、[themostdangerouswritingapp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/maebert/themostdangerouswritingapp)：挑战写作效率极限的工具。这是一个帮助用户进入写作“心流”状态的 Web 应用。如果你停止输入超过 5 秒，屏幕上的文字就会逐渐变得模糊，最终会彻底消失。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/52758523.gif' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
43、[udlbook](https://hellogithub.com/periodical/statistics/click?target=https://github.com/udlbook/udlbook)：《Understanding Deep Learning》理解深度学习。该书是由 Simon J.D. Prince 编写的一本关于深度学习的专业书籍，内容涵盖深度学习的理论基础、性能评估、卷积网络、Transformers、图神经网络、生成对抗网络（GANs）、扩散模型（Diffusion Models）、强化学习等主题，并附有大量练习题。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/520128820.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub102.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub104.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/103'>这里</a>。
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
