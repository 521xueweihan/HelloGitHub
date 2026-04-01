# 《HelloGitHub》第 94 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/94) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[genann](https://hellogithub.com/periodical/statistics/click?target=https://github.com/codeplea/genann)：C 语言写的极简神经网络库。这是一个轻量、无依赖、单文件的 C 语言神经网络库，内含丰富的示例和测试。代码简洁易读，适合作为初学者学习神经网络的入门项目。来自 [@ziming012](https://hellogithub.com/user/t7lxvuwPRDamU8p) 的分享
```c
#include "genann.h"

/* Not shown, loading your training and test data. */
double **training_data_input, **training_data_output, **test_data_input;

/* New network with 2 inputs,
 * 1 hidden layer of 3 neurons each,
 * and 2 outputs. */
genann *ann = genann_init(2, 1, 3, 2);

/* Learn on the training set. */
for (i = 0; i < 300; ++i) {
    for (j = 0; j < 100; ++j)
        genann_train(ann, training_data_input[j], training_data_output[j], 0.1);
}

/* Run the network and see what it predicts. */
double const *prediction = genann_run(ann, test_data_input[0]);
printf("Output for the first test data point is: %f, %f\n", prediction[0], prediction[1]);

genann_free(ann);
```

### C# 项目
2、[FancyScrollView](https://hellogithub.com/periodical/statistics/click?target=https://github.com/setchi/FancyScrollView)：Unity 滑动列表插件。该项目采用 Unity 引擎动画系统来定制列表滑动效果，具备非常高的灵活性，除了用作滑动列表，还可以用作导航栏。项目代码结构和风格规范，接入成本低、易于使用和定制。来自 [@Wu Zheng](https://hellogithub.com/user/zwC03jng8kKhql6) 的分享
```csharp
using UnityEngine;
using UnityEngine.UI;
using FancyScrollView;

class MyCell : FancyCell<ItemData>
{
    [SerializeField] Text message = default;

    public override void UpdateContent(ItemData itemData)
    {
        // 更新内容
        message.text = itemData.Message;
    }

    public override void UpdatePosition(float position)
    {
        // position 是一个介于 0.0 到 1.0 之间的值
        // 可以根据 position 自由控制滚动的外观
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/83178374.gif' style="max-width:80%; max-height=80%;"></img></p>

3、[MarkovJunior](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mxgmn/MarkovJunior)：基于马尔可夫链的图像生成器。马尔可夫链是一种数学模型，具有“无记忆”的性质，即未来状态的概率分布只依赖于当前状态，而不依赖于过去的状态。该项目利用马尔可夫链原理，通过模拟图像的状态转移来生成独特的图像，包括建筑、迷宫等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/498726567.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[abseil-cpp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/abseil/abseil-cpp)：谷歌开源的 C++ 基础库。这是一个在 Google 内部被广泛应用的 C++ 公共库，它提供了一系列高质量、可靠、高效的基础模块，其中包括字符串处理、并发、时间、STL 容器、测试、日志等实用函数。来自 [@张程林](https://hellogithub.com/user/PU5imApS4WqLeHZ) 的分享

5、[gpupixel](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pixpark/gpupixel)：高性能跨平台实时美颜滤镜库。这是一个用 C++11 编写的高性能图像和视频处理库，内置基于 GPU 的美颜特效滤镜，效果可以达到商业级别水平。支持磨皮、美白、瘦脸、大眼等特效，适用于 iOS、macOS 和 Android 平台。来自 [@Zhaoyou Ge](https://hellogithub.com/user/s3GSnjBQb6X9zwh) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/508234417.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[qtrvsim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cvut/qtrvsim)：面向教育的 RISC-V CPU 模拟器。这是一个采用 Qt 实现的 RISC-V CPU 模拟器，由捷克理工大学计算学院开发。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/318563203.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
7、[goploy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zhenorzz/goploy)：容易上手的代码发布平台。这是一个采用 Go + Vue.js 构建的 Web 部署平台，可一键部署、发布和回滚项目。支持基于角色的访问控制、监控、秒级定时任务、Xterm、LDAP 等功能，提供了完整的安装引导，即使是初学者也能轻松上手。来自 [@zhenorzz](https://hellogithub.com/user/QASc7j3pUxHqgbC) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/161898203.gif' style="max-width:80%; max-height=80%;"></img></p>

8、[listmonk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/knadh/listmonk)：开源的邮件列表和营销平台。这是一个开箱即用的邮件营销平台，可以帮助你管理邮件订阅者、创建和发送邮件、分析营销数据。可查看邮件阅读率、链接点击率等，支持自托管适用于个人和企业。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/193833307.png' style="max-width:80%; max-height=80%;"></img></p>

9、[restic](https://hellogithub.com/periodical/statistics/click?target=https://github.com/restic/restic)：一款强大的开源备份工具。该项目提供了简单、快速、安全的开源备份解决方案。它无需繁琐的配置，即可轻松完成备份和恢复操作。采用增量备份策略，备份数据经过加密和压缩处理，保障数据安全且节省空间，支持灵活的存储选择，包括本地磁盘和云存储。可设置自动备份时间，确保数据得到定期的备份保护。
```
$ restic --repo /tmp/backup backup ~/work
enter password for repository:
scan [/home/user/work]
scanned 764 directories, 1816 files in 0:00
[0:29] 100.00%  54.732 MiB/s  1.582 GiB / 1.582 GiB  2580 / 2580 items  0 errors  ETA 0:00
duration: 0:29, 54.47MiB/s
snapshot 40dc1520 saved
```

10、[vfox](https://hellogithub.com/periodical/statistics/click?target=https://github.com/version-fox/vfox)：无忧应对多编程语言不同版本的工具。这是一款跨平台的通用版本管理工具，通过命令行快速安装、切换编程语言的不同版本，并支持自定义源地址。相比于针对每种语言的独立版本管理工具（如 nvm、fvm、gvm 等），这个项目让开发者摆脱繁琐的学习和记忆过程，只需一个工具、一条命令，轻松搞定多编程语言版本管理。来自 [@Han Li](https://hellogithub.com/user/TV6tBSMzmZUWQqk) 的分享
```
$ vfox c
node -> v20.10.0
java -> v11.0.12
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/729446906.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
11、[1brc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gunnarmorling/1brc)：探索 Java 处理 10 亿行文本的最快速度。这是一个有趣的 Java 编程挑战，要求开发者编写一个 Java 程序，读取包含多个气象站温度值的文件（10 亿行），然后计算每个气象站的最小、平均和最大值，最后按照站点名称排序后输出，现在最快速度为 2 秒。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/736572328.png' style="max-width:80%; max-height=80%;"></img></p>

12、[automq](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AutoMQ/automq)：一款真正的云原生 Kafka 解决方案。该项目是基于云原生重新设计的新一代 Kafka 发行版。在保持和 Apache Kafka 100%兼容前提下，AutoMQ 可以为用户提供高达 10 倍的成本优势以及百倍的弹性优势，同时支持秒级分区迁移和流量自动重平衡，解决运维痛点。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/679601811.jpg' style="max-width:80%; max-height=80%;"></img></p>

13、[spring-startup-analyzer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/linyimin0812/spring-startup-analyzer)：优化 Spring 应用启动性能的工具。该项目利用采集 Spring 应用启动过程数据，生成交互式分析报告，为开发者提供了分析 Spring 应用启动性能的工具。其主要功能包括分析启动卡点、处理 Spring Bean 异步初始化，以及显示应用未加载的 jar 包、方法调用次数和耗时统计等详细信息。来自 [@linyimin](https://hellogithub.com/user/jfau31oBX46pr8O) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/634983681.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
14、[awesome-hands-control](https://hellogithub.com/periodical/statistics/click?target=https://github.com/RylanBot/awesome-hands-control)：用手势操控电脑程序的工具。该项目基于手势识别进行自定义操控电脑程序，采用纯前端技术栈实现。它通过训练好的模型（MediaPipe）来识别手势，然后将特定手势与电脑操控绑定，最后，用户可以指定操作的进程，从而实现手势操控电脑程序。来自 [@Rylan](https://hellogithub.com/user/c3A7yEZFnvKMulI) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/719241997.png' style="max-width:80%; max-height=80%;"></img></p>

15、[bpmn-js](https://hellogithub.com/periodical/statistics/click?target=https://github.com/bpmn-io/bpmn-js)：专注于流程图的可视化和编辑组件。该项目提供了直观的拖拽式创建和编辑流程图的功能，可用于构建业务流程管理、决策流可视化和低代码平台。来自 [@塔咖](https://hellogithub.com/user/bzJpGyu0IanC6L7) 的分享
```javascript
const xml = '...'; // my BPMN 2.0 xml
const viewer = new BpmnJS({
  container: 'body'
});

try {
  const { warnings } = await viewer.importXML(xml);

  console.log('rendered');
} catch (err) {
  console.log('error rendering', err);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/17592572.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[dockge](https://hellogithub.com/periodical/statistics/click?target=https://github.com/louislam/dockge)：一个美观、易用的 Docker Compose 管理平台。该项目提供了一个 Web 界面，用于管理 docker-compose.yaml 文件。它开箱即用、界面设计精美，支持交互式编辑 compose.yaml 文件、更新 docker 镜像，以及启动、停止、重启、删除 docker 等操作。来自 [@猎隼丶止戈reNo7](https://hellogithub.com/user/Ew59HqRWjPe0zZO) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/708775091.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[theatre](https://hellogithub.com/periodical/statistics/click?target=https://github.com/theatre-js/theatre)：一个用于创建 Web 动画的 JavaScript 库。该项目是带图形用户界面的 Web 动画编辑器，能对任何 JavaScript 变量进行动画处理。它不仅支持处理 three.js 或其他 3D 库对象的动画功能，还能利用 React 等库对 HTML/SVG 进行动画处理。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/15393566.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[tiny-rdm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tiny-craft/tiny-rdm)：一款轻量级的跨平台 Redis 桌面客户端。该项目是基于 WebView2 的 Redis 桌面客户端，拥有小巧的体积和精美的界面，同时支持中文。它提供了多种连接方式、分段加载、慢日志、转码显示等功能，可以在 Windows、Linux 和 macOS 系统上使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/659115218.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
19、[jingmo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hefengbao/jingmo)：一款古诗词文和成语应用。它叫「京墨」是一个免费的 Android 阅读应用，内含丰富的中国传统文化内容，包括古诗、歇后语、成语故事、中国传统节日、绕口令等。安装应用第一次进入无内容，需要在设置里手动同步数据。来自 [@贺丰宝](https://hellogithub.com/user/2K7jqBdMvyUrOEs) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/682370127.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C 项目
20、[Itsycal](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sfsam/Itsycal)：可爱的 Mac 菜单栏日历。这是一个迷你的菜单栏日历工具，拥有可爱的界面和实用的功能。支持显示/添加系统日历的事件、深色模式、周数、快捷键等功能，适用于 macOS 11+ 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/50525082.png' style="max-width:80%; max-height=80%;"></img></p>

21、[KeepingYouAwake](https://hellogithub.com/periodical/statistics/click?target=https://github.com/newmarcel/KeepingYouAwake)：防止 Mac 进入睡眠状态的工具。这一个小型的菜单栏实用工具，可以让 Mac 电脑在预设的时间内或永久不进入睡眠模式，适用于 macOS 10.13 或更高版本。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/25431634.jpg' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
22、[akaunting](https://hellogithub.com/periodical/statistics/click?target=https://github.com/akaunting/akaunting)：专为小型企业和个人设计的在线会计软件。该项目是基于 Laravel+Vue.js+Tailwind CSS+MySQL 构建的会计平台，为用户提供全面的会计和财务功能。其中包括费用跟踪、现金流、报告等，并且支持移动端适配和多语言。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/95011974.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
23、[DouyinLiveRecorder](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ihmily/DouyinLiveRecorder)：一款支持多平台的直播录制工具。该项目是基于 FFmpeg 实现的多平台直播源录制工具，支持循环执行直播录制任务（循环值守）、直播状态推送、多人录制、去水印、选择画质等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/667354736.png' style="max-width:80%; max-height=80%;"></img></p>

24、[harlequin](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tconbeer/harlequin)：一个简单、快速、美观的终端数据库客户端。这是一个带界面的命令行数据库客户端，提供了数据库和表目录、查询编辑器、显示结果、导出数据的功能，支持 DuckDB、SQLite、Postgres、MySQL 等数据库。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/635393461.png' style="max-width:80%; max-height=80%;"></img></p>

25、[khal](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pimutils/khal)：一款简单、美观的终端日历。该项目是用 Python 写的命令行日历工具，支持快速便捷地浏览、添加和编辑事件，以及同步日历数据。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/12357974.png' style="max-width:80%; max-height=80%;"></img></p>

26、[pyupgrade](https://hellogithub.com/periodical/statistics/click?target=https://github.com/asottile/pyupgrade)：一键升级 Python 代码的工具。这是一个用于自动升级 Python 代码，以适应新版本语法的工具。支持升级到不同的 Python 版本、提供预览模式即查看改动变化等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/83462592.png' style="max-width:80%; max-height=80%;"></img></p>

27、[text_blind_watermark](https://hellogithub.com/periodical/statistics/click?target=https://github.com/guofei9987/text_blind_watermark)：给文本加盲水印的 Python 库。通过该项目可以将一段隐秘信息嵌入到明文中，嵌入前后的明文无变化。简单说就是给文本打上隐藏水印，适合在版权保护、数据泄露溯源、数据安全等场景使用，支持 macOS 的 Chrome 浏览器、苹果备忘录、macOS/iPhone 的微信和钉钉等应用。
```python
from text_blind_watermark import TextBlindWatermark2

password = 'HelloGitHub'
text = '这句话中有盲水印，你能提取出来吗？'
watermark = 'HelloGitHub'

text_blind_wm = TextBlindWatermark2(password=password)

text_with_wm = text_blind_wm.embed(text=text, watermark=watermark)
print(text_with_wm)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/437797089.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
28、[cmd-wrapped](https://hellogithub.com/periodical/statistics/click?target=https://github.com/YiNNx/cmd-wrapped)：一个 Rust 编写的命令行历史记录分析工具。这是一款命令行工具，它可以读取你的命令行操作历史记录，并生成详细的分析报告。报告包括过去任意一年的命令行活跃时段、常用命令等信息，支持 Zsh、Bash、fish 等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/737071068.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
29、[AnimateDiff](https://hellogithub.com/periodical/statistics/click?target=https://github.com/guoyww/AnimateDiff)：让 AI 生成的图动起来。这是一款可以在 Stable Diffusion 中制作动图的库，支持将大多数开源模型转换为动画生成器。让原本通过文字生成的图片，变成 gif 图片动起来。来自 [@adoin](https://hellogithub.com/user/HJZMx5VeRfNDQ8z) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/654930782.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[AnyText](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tyxsspa/AnyText)：轻松 DIY 图片文字，定制你的创意设计。该项目提供了文字生成和文字编辑两种模式，它能够根据提示词生成图文融合的图片，并确保文字的准确性，还支持对上传图片中的文字进行编辑后，重新生成图片。支持中文、英语、日语、韩语等多语言，适用于海报设计、Logo 设计、创意涂鸦、表情包等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/692934702.jpg' style="max-width:80%; max-height=80%;"></img></p>

31、[pyvideotrans](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jianchang512/pyvideotrans)：开源的视频翻译和配音工具。该项目可以将视频从一种语言翻译成指定语言的视频，并自动生成和添加对应语言的字幕和配音。来自 [@okaymyworld](https://hellogithub.com/user/Gf8J0xolgYIMUT9) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/699432836.png' style="max-width:80%; max-height=80%;"></img></p>

32、[StreamDiffusion](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cumulo-autumn/StreamDiffusion)：实时交互式 AIGC 图片。该项目能以惊人的速度生成 AIGC 图像，单张 RTX4090 显卡可达 100 张/秒。它通过流批处理简化数据处理，采用残差无分类器（RCFG）减少计算冗余，随机相似性过滤器提高 GPU 利用率，并通过优化 IO 队列实现并行处理。同时，利用多种模型加速工具，实现爆炸式地提升 AIGC 图像速度。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/724635656.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
33、[gdb-dashboard](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cyrus-and/gdb-dashboard)：GDB 可视化调试界面。这是专为 GNU 调试器（GDB）设计的文本界面，支持模块化显示调试的程序相关信息，更直观和方便地调试代码。该界面采用 Python 编写，具备轻松自定义和扩展的特性。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/42191943.png' style="max-width:80%; max-height=80%;"></img></p>

34、[kubernetes-network-policy-recipes](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ahmetb/kubernetes-network-policy-recipes)：只需复制粘贴即可解决 K8s 网络问题的配方。该项目包含了 Kubernetes 网络策略的各种用例和示例 YAML 文件，可直接复制使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/98780162.gif' style="max-width:80%; max-height=80%;"></img></p>

35、[particle-life](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hunar4321/particle-life)：粒子生命演化游戏。该项目通过定义粒子之间的相互作用力，从而生成复杂的自组织图案。源码十分简单，用户可以在线试玩，创造出各种有趣的图案。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/523244338.jpg' style="max-width:80%; max-height=80%;"></img></p>

36、[proxypin](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wanghongenpin/proxypin)：支持手机端的免费抓包工具。该项目是采用 Flutter 开发的抓包工具，可用于拦截、检查和重写 HTTP(S) 流量。它支持扫码连接、域名过滤、请求重写等功能，适用于 Windows、macOS、Linux、Android 和 iOS 平台。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/649662864.png' style="max-width:80%; max-height=80%;"></img></p>

37、[vimwiki](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vimwiki/vimwiki)：Vim 中的个人 wiki。这是一个 Vim 插件，通过以 wiki 的方式连接文本，提供更好的组织笔记和想法的功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/6698053.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
38、[game-programming-patterns](https://hellogithub.com/periodical/statistics/click?target=https://github.com/munificent/game-programming-patterns)：《游戏编程模式》。该书收集了经过验证、已发布的 3A 级游戏中的经验和模式，来解决你在游戏开发中遇到的问题。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/94/11390832.jpg' style="max-width:80%; max-height=80%;"></img></p>

39、[PDF-Explained](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zxyle/PDF-Explained)：《PDF 解析》。该项目是《PDF Explained》一书的非官方中文翻译版，内容由浅入深介绍了如何构建简单的 PDF 文件，以及 PDF 运算符、书签、超链接、注释、加密等高级特性。



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub93.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub95.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/94'>这里</a>。
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
