# 《HelloGitHub》第 116 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/116) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[sj.h](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rxi/sj.h)：极简的 C 语言 JSON 解析库。这是一个轻量级的 C 语言 JSON 解析库，提供可靠的 JSON 遍历和基础解析功能。它仅 150 行代码、无外部依赖，采用零内存分配策略，直接在原数据上进行解析，速度快且无内存泄漏风险，适用于嵌入式、物联网和游戏开发等场景。
```c
char *json_text = "{ \"x\": 10, \"y\": 20, \"w\": 30, \"h\": 40 }";

typedef struct { int x, y, w, h; } Rect;

bool eq(sj_Value val, char *s) {
    size_t len = val.end - val.start;
    return strlen(s) == len && !memcmp(s, val.start, len);
}

int main(void) {
    Rect rect = {0};

    sj_Reader r = sj_reader(json_text, strlen(json_text));
    sj_Value obj = sj_read(&r);

    sj_Value key, val;
    while (sj_iter_object(&r, obj, &key, &val)) {
        if (eq(key, "x")) { rect.x = atoi(val.start); }
        if (eq(key, "y")) { rect.y = atoi(val.start); }
        if (eq(key, "w")) { rect.w = atoi(val.start); }
        if (eq(key, "h")) { rect.h = atoi(val.start); }
    }

    printf("rect: { %d, %d, %d, %d }\n", rect.x, rect.y, rect.w, rect.h);
    return 0;
}
```

### C# 项目
2、[CPUSetSetter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SimonvBez/CPUSetSetter)：手动指定运行游戏用的 CPU 核。该项目是专为 Windows 11 设计的性能优化工具，利用 CPU Sets 技术，让用户可以自由控制游戏和应用程序运行时使用的 CPU 核，全程无需重启程序。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1029765448.png' style="max-width:80%; max-height=80%;"></img></p>

3、[PicView](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Ruben2776/PicView)：比系统自带更好用的看图工具。这是一款快速、免费的图片查看工具，适用于 Windows 和 macOS 平台。它采用 .NET NativeAOT 编译技术，体积小、启动速度快，支持浏览长图、编辑图片、格式转换、批量处理等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/79786795.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[crossdesk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kunkundi/crossdesk)：支持 Web 端的远程桌面工具。这是一款开源、轻量级的跨平台远程桌面工具，支持不同设备间（Windows、Linux 和 macOS）的远程桌面控制和音视频传输，特点是可直接通过浏览器控制远程设备，无需额外安装任何应用。来自 [@Junkun Di](https://hellogithub.com/user/cb0OpZRrBuGVAfL) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/720999514.png' style="max-width:80%; max-height=80%;"></img></p>

5、[MouseClick](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SeaEpoch/MouseClick)：开源的鼠标连点工具。这是一款基于 Qt6 构建的鼠标连点器，仅适用于 Windows 系统。它开箱即用、操作简单，支持自定义鼠标点击间隔和快捷键功能。来自 [@SeaYJ](https://hellogithub.com/user/6aHSOczLEVNxDF7) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/383007660.png' style="max-width:80%; max-height=80%;"></img></p>

6、[objcurses](https://hellogithub.com/periodical/statistics/click?target=https://github.com/admtrv/objcurses)：命令行查看 3D 模型的工具。这是一款极简的 3D 模型查看器，能够将 3D 模型文件以 ASCII 字符方式渲染展示在终端里，支持 3D 对象的实时预览、旋转和交互操作。来自 [@CN1998Ft](https://hellogithub.com/user/QwmfN9cuvYja4b3) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/887103582.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[seekdb](https://hellogithub.com/periodical/statistics/click?target=https://github.com/oceanbase/seekdb)：开箱即用的轻量级向量数据库。该项目是 OceanBase 团队开源的一款轻量级 AI 原生搜索数据库，支持关系型、向量和文本数据的统一存储与检索。它提供嵌入式和服务器两种模式，最低仅需 1C1G 即可运行，并兼容 MySQL 协议。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1080442728.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[filebrowser](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gtsteffaniak/filebrowser)：完全开源可自托管的私有云盘。该项目是基于 Go+Vue.js 构建的在线文件管理工具，功能比原版 FileBrowser 更丰富，支持多文件源（本地或云）、目录级访问控制、设置共享过期时间、文件搜索和缩略图等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/652319769.png' style="max-width:80%; max-height=80%;"></img></p>

9、[kite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kite-org/kite)：开源的轻量级 K8s 管理面板。这是一款轻量级、现代化的 Kubernetes 可视化管理平台，适用于管理和监控 K8s 集群。它拥有直观易用的界面，支持查看 Pod 日志、执行容器命令、编辑 YAML 配置、管理用户权限等功能。来自 [@Zzde](https://hellogithub.com/user/w5uk718RFhDzdCX) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1003614809.png' style="max-width:80%; max-height=80%;"></img></p>

10、[term.everything](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mmulet/term.everything)：终端里运行任意 GUI 应用。该项目突破了传统终端只能运行命令行程序的限制，让用户能够在终端（Terminal）中运行任意 GUI 应用程序，将图形界面的操作体验带入终端环境。它通过自研的 Wayland 合成器，将原本输出到显示器的 GUI 窗口实时渲染为终端可显示的字符或图片，实现了在终端内运行图形应用的能力，兼容 iTerm2、Alacritty、Kitty 等主流终端模拟器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1051928239.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[tuios](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Gaurav-Gosain/tuios)：终端内实现桌面级窗口管理。这是一个 Go 编写的终端多窗口管理工具，支持浮动窗口、鼠标拖拽、自动平铺、多工作区切换等功能。窗口可以自由重叠和移动，像桌面操作系统一样，适合觉得 tmux 快捷键难记的开发者。来自 [@天涯孤雁](https://hellogithub.com/user/gf67BzSc528eYP9) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1051789550.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[CordysCRM](https://hellogithub.com/periodical/statistics/click?target=https://github.com/1Panel-dev/CordysCRM)：新一代客户关系管理系统。这是一款基于 Spring Boot 和 Vue.js 构建的 CRM（客户关系管理）平台，支持线索获取、商机跟进、合同签约等功能，并可通过集成 SQLBot 和 MaxKB 实现 AI 加持。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1043515641.png' style="max-width:80%; max-height=80%;"></img></p>

13、[reitti](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dedicatedcode/reitti)：Java 开发的个人足迹分析平台。这是一款基于 Spring Boot 和 PostGIS 构建的个人位置追踪与分析平台，适用于记录自己的行动轨迹和地理位置信息。支持自动识别停留地点、分析出行路线、判断交通方式，并以时间轴+地图的方式展示。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/989939173.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
14、[cesium](https://hellogithub.com/periodical/statistics/click?target=https://github.com/CesiumGS/cesium)：3D 地理空间的 JavaScript 库。该项目是用于在 Web 网页中创建交互式 3D 地球和 2D 地图的 JavaScript 库，它利用了 WebGL 技术来加速图形处理，具备较好的渲染速度，可处理海量数据和动态数据可视化，支持地形和三维瓦片（3D Tiles）等多种数据格式，适用于构建地理信息系统（GIS）等 Web 应用。
```javascript
import { Viewer } from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";

const viewer = new Viewer("cesiumContainer");
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/3606738.png' style="max-width:80%; max-height=80%;"></img></p>

15、[jsonrepair](https://hellogithub.com/periodical/statistics/click?target=https://github.com/josdejong/jsonrepair)：自动兼容错误 JSON 格式的 JavaScript 库。这是一个用于修复/解析多种错误 JSON 格式的 JavaScript 库，与 JSON.parse() 遇到格式错误直接抛出异常不同。它可以自动处理常见的 JSON 格式问题，如键名缺失引号、单引号代替双引号、尾部多余逗号、缺失逗号和换行符不规范等。
```javascript
import { jsonrepair } from 'jsonrepair'

try {
  // The following is invalid JSON: is consists of JSON contents copied from 
  // a JavaScript code base, where the keys are missing double quotes, 
  // and strings are using single quotes:
  const json = "{name: 'John'}"
  
  const repaired = jsonrepair(json)
  
  console.log(repaired) // '{"name": "John"}'
} catch (err) {
  console.error(err)
}
```

16、[log-lottery](https://hellogithub.com/periodical/statistics/click?target=https://github.com/LOG1997/log-lottery)：炫酷 3D 球体年会抽奖应用。这是一个基于 Three.js 和 Vue.js 构建的年会抽奖工具，支持导入人员名单、设置奖品/奖项、播放背景音乐、临时抽奖等功能。来自 [@1：](https://hellogithub.com/user/EQPvVCA9NTGfnoR) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/738128540.png' style="max-width:80%; max-height=80%;"></img></p>

17、[openscreen](https://hellogithub.com/periodical/statistics/click?target=https://github.com/siddharthvaddem/openscreen)：免费开源的屏幕录制工具。这是一款免费且开源的屏幕录制工具，可作为 Screen Studio 的轻量级替代品，支持应用录制、修改背景、自定义缩放时长等功能，适用于 Windows 和 macOS 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1073433866.png' style="max-width:80%; max-height=80%;"></img></p>

18、[stylex](https://hellogithub.com/periodical/statistics/click?target=https://github.com/facebook/stylex)：易扩展的 CSS-in-JS 解决方案。该项目是 Meta 开源的 CSS-in-JS 库，支持在 JavaScript 中定义样式，并在编译时自动优化和提取为独立的 CSS 文件，不仅消除运行时的性能开销，还能彻底避免样式冲突。来自 [@IZRINO](https://hellogithub.com/user/eK0Bv1dmJPxnrwy) 的分享
```javascript
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  root: {
    padding: 10,
  },
  element: {
    backgroundColor: 'red',
  },
});

const styleProps = stylex.props(styles.root, styles.element);
```

### Kotlin 项目
19、[librepods](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kavishdevar/librepods)：让 AirPods 在安卓设备满血复活。该项目能够让用户在 Android 设备上使用 AirPods Pro/Max 的高级功能，包括主动降噪切换、入耳检测、头部姿势控制、对话感知等，但需要 Root 权限并配合 Xposed 使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/863717537.png' style="max-width:80%; max-height=80%;"></img></p>

20、[XMSLEEP](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Tosencen/XMSLEEP)：开源的 Android 白噪音应用。这是一个专注于白噪音播放的 Android 应用，提供雨声、篝火、雷声、猫咪呼噜、鸟鸣、夜虫等多种自然声音，帮助你放松、冥想和入睡。来自 [@Tosencen](https://hellogithub.com/user/Gxvd2eIyHm54S9p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1089198514.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
21、[Wallos](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ellite/Wallos)：开源的个人订阅管理平台。这是一款 PHP 开发的自托管个人订阅管理平台，可直观展示所有订阅的服务名称、价格、支付周期（月/年/周等）和距离下次付款的剩余天数，支持多种通知方式和统计分析。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/701017456.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
22、[fastapi-best-practices](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zhanymkanov/fastapi-best-practices)：FastAPI 最佳实践指南。这是一份作者在初创公司多年使用 FastAPI 开发应用的实战经验总结，内容涵盖项目结构、异步、Pydantic、Depends、数据迁移等方面。

23、[FindMy.py](https://hellogithub.com/periodical/statistics/click?target=https://github.com/malmeloo/FindMy.py)：玩转 Find My 网络的 Python 库。这是一个用于查询 Apple Find My 网络的 Python 库，让开发者使用 Python 代码获取 AirTag、iPhone、iPad 等官方设备以及自制 AirTag 的实时位置信息。

24、[localstack](https://hellogithub.com/periodical/statistics/click?target=https://github.com/localstack/localstack)：本地模拟 AWS 云服务。这是一个功能齐全的本地 AWS 云服务模拟框架，支持 Lambda、S3、DynamoDB、Kinesis、SQS、SNS、API Gateway 等服务。只需一条命令，即可在本地启动完整的 AWS 服务环境，解决了开发和调试过程中依赖 AWS 账户和服务的痛点。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/71948498.png' style="max-width:80%; max-height=80%;"></img></p>

25、[PythonRobotics](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AtsushiSakai/PythonRobotics)：机器人算法 Python 实现集合。该项目汇集了机器人领域算法的 Python 实现，涵盖定位、SLAM、路径规划、空中导航、机械臂、双足机器人等技术，并提供示例代码和可视化演示。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/54376220.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[tiny8](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sql-hkr/tiny8)：纯 Python 实现的 CPU 模拟器。该项目是 Python 写的轻量级 8 位 CPU 模拟器，能够将抽象的汇编语言执行过程转化为可视化、可交互的学习体验，并支持将代码执行过程导出为 GIF 或 MP4，适用于《计算机组成原理》或《汇编语言》课程的教学与学习。
```python
from tiny8 import CPU, assemble_file

asm = assemble_file("fibonacci.asm")
cpu = CPU()
cpu.load_program(asm)
cpu.run(max_steps=1000)

print(f"Result: R17 = {cpu.read_reg(17)}")  # Final Fibonacci number
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1079950805.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
27、[gitlogue](https://hellogithub.com/periodical/statistics/click?target=https://github.com/unhappychoice/gitlogue)：回放你的 Git 提交历史。这是一个能够将 Git 提交历史转化为动画的命令行工具，通过打字动画和代码高亮，在终端里生动展示每一次变更。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1092562478.gif' style="max-width:80%; max-height=80%;"></img></p>

28、[xan](https://hellogithub.com/periodical/statistics/click?target=https://github.com/medialab/xan)：终端里的 CSV 数据魔术师。这是一个能够处理 GB 级超大 CSV 文件的命令行工具，支持预览、过滤、切片、聚合、排序等操作，并可在终端里通过直方图、热力图等方式进行数据可视化。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/140488417.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
29、[Petrichor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kushalpandya/Petrichor)：优雅的 macOS 本地音乐播放器。这是一款用 Swift 精心设计的 macOS 本地音乐播放器，支持 MP3、FLAC、DSD 等主流及无损音频格式。它专注于离线场景、界面清爽，为你带来纯粹的音乐播放体验。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/969355437.png' style="max-width:80%; max-height=80%;"></img></p>

30、[ScrollSnap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Brkgng/ScrollSnap)：Mac 滚动截图工具。这是一款用于解决 macOS 原生截图功能，不支持滚动截图的工具。只需要框选指定区域，然后滚动页面，即可轻松得到完整的长截图。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/983779325.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
31、[char](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fastrepl/char)：本地优先的 AI 笔记和会议助手。这是一款可离线运行的 AI 智能笔记和会议记录应用，通过接入 Ollama 可实现语音转录到摘要生成全程在本地完成，支持会议录音、实时转录、笔记整理和智能摘要等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/900550981.png' style="max-width:80%; max-height=80%;"></img></p>

32、[cognee](https://hellogithub.com/periodical/statistics/click?target=https://github.com/topoteretes/cognee)：开箱即用的智能体记忆引擎。这是一个专为 AI 智能体（Agents）提供记忆功能的 Python 项目，集成了图数据库、知识图谱及向量数据库等技术。它仅需 5 行代码，即可轻松为 AI 智能体提供持久化、多模态记忆，支持连接和检索过去的对话、文档、图像和音频转录等内容。
```python
import cognee
import asyncio


async def main():
    # Add text to cognee
    await cognee.add("Natural language processing (NLP) is an interdisciplinary subfield of computer science and information retrieval.")

    # Generate the knowledge graph
    await cognee.cognify()

    # Query the knowledge graph
    results = await cognee.search("Tell me about NLP")

    # Display the results
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/679343504.png' style="max-width:80%; max-height=80%;"></img></p>

33、[droidrun](https://hellogithub.com/periodical/statistics/click?target=https://github.com/droidrun/droidrun)：用自然语言操控你的手机。这是一个基于 LLM Agents 的手机自动化框架，可通过自然语言操控 Android 设备或模拟器，支持 DeepSeek、OpenAI、Gemini 等主流大模型。使用时需要在手机上安装 DroidRun Portal，用来收集 UI 信息并执行操作命令，然后通过 ADB 将信息传给电脑上的 DroidRun 框架，由它与 LLM 交互并给出执行指令。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/965313467.gif' style="max-width:80%; max-height=80%;"></img></p>

34、[Everywhere](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DearVa/Everywhere)：随手可用的 AI 桌面助手。这是一款基于上下文感知的桌面 AI 助手，能够自动获取并理解当前屏幕上的内容，无需截图、复制内容或切换应用。只需一键即可召唤出 AI，进行问答、翻译、答疑等任务。来自 [@Dear.Va](https://hellogithub.com/user/LNYEf6O9Qv5JeR2) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/971243074.png' style="max-width:80%; max-height=80%;"></img></p>

35、[next-ai-draw-io](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DayuanJiang/next-ai-draw-io)：让 AI 替你画架构图。这是一个基于 Next.js 构建的 Web 应用，融合了 AI 与 draw.io 图表绘制能力。现在你可以通过对话直接生成、编辑、优化流程图和架构图，支持流动效果连线、截图复刻、历史版本等功能。来自 [@喜BFoCE](https://hellogithub.com/user/Fzr3vHc5AxqYUVj) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/953521037.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
36、[bash-screensavers](https://hellogithub.com/periodical/statistics/click?target=https://github.com/attogram/bash-screensavers)：黑客风格终端屏保合集。该项目提供 12 个有趣的命令行 ASCII 动画，包括经典矩阵代码雨、无限管道迷宫、烟花等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1036073889.gif' style="max-width:80%; max-height=80%;"></img></p>

37、[espectre](https://hellogithub.com/periodical/statistics/click?target=https://github.com/francescopace/espectre)：基于 Wi-Fi 信号的运动监测系统。这是一个基于 Wi-Fi 频谱分析（CSI）的运动检测系统，采用 ESP32-S3 开发板，成本约 10 欧元。它通过分析人体对 Wi-Fi 信号的干扰变化，实现无需摄像头、麦克风的运动检测，支持 Home Assistant 集成，适用于智能家居自动化，如人来开灯、家庭安防等场景。来自 [@LaoZ](https://hellogithub.com/user/LT1VF8UXAHRoheE) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1083590674.png' style="max-width:80%; max-height=80%;"></img></p>

38、[GreenWall](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zmrlft/GreenWall)：像画画一样自定义 GitHub 绿格子。这是一个自定义 GitHub 贡献墙（绿墙）的工具，可通过直观的拖拽界面，轻松创作文字、Logo 或任意图案。来自 [@ShiYi](https://hellogithub.com/user/ucwD1E5BxrhWt4J) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1080902977.png' style="max-width:80%; max-height=80%;"></img></p>

39、[SO-ARM100](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TheRobotStudio/SO-ARM100)：开源低成本的机械臂。该项目是由 TheRobotStudio 与 Hugging Face 联合开源的低成本机械臂，内含自制 SO-100 和 SO-101 两款机械臂的所有资料。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/798981945.png' style="max-width:80%; max-height=80%;"></img></p>

40、[vscode-pets](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tonybaloney/vscode-pets)：在 VSCode 里养只宠物。该项目能够让你在 VSCode 编辑器里养一只或多只可互动的电子宠物，内置可爱的猫、狗、橡皮鸭等多种宠物。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/341041243.gif' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub115.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub117.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/116'>这里</a>。
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
