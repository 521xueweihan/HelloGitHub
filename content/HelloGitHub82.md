# 《HelloGitHub》第 82 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/82) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[bare-metal-programming-guide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cpq/bare-metal-programming-guide)：裸机编程指南。这是一份教你如何在不依赖 IDE 的情况下，进行单片机开发的教程。内容先是介绍了寄存器、向量表、启动代码、链接脚本等知识点，最后实现了一个带设备仪表盘的 Web 服务器。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/537042935.png' style="max-width:80%; max-height=80%;"></img></p>

2、[sumatrapdf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sumatrapdfreader/sumatrapdf)：免费小巧的开源 PDF 阅读器。这是一款体积小、占用内存少、启动速度快的 Windows PDF 阅读工具，拥有日常所需的所有功能和简约大方的界面，这一切不多不少刚刚好。来自 [@Tianchi Gao](https://hellogithub.com/user/8rWP9fXUuvRdwSz) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/6041301.png' style="max-width:80%; max-height=80%;"></img></p>

3、[ZSWatch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ZSWatch/ZSWatch)：自制开源智能手表。该项目是基于开源 Zephyr 的智能手表，设备包含了一个分辨率为 240x240 的 IPS TFT 圆形屏幕和 3 个按钮(上一页/下一页/进入)，支持计步、血氧仪、心率仪、蓝牙等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/529594820.gif' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
4、[carnac](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Code52/carnac)：用于展示键盘按键操作的工具。这是一款能够在桌面实时显示键盘操作记录的工具，多用于演示应用、录制教程等场景，适用于 Windows 7 及以上的操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/3429434.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[downkyi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/leiurayer/downkyi)：一款多功能的 B 站视频下载工具。这是一款简单易用的哔哩哔哩视频下载工具，它拥有简洁的操作界面，使用起来十分方便。支持批量下载、音视频提取、去水印等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/324473895.png' style="max-width:80%; max-height=80%;"></img></p>

6、[SeeSharpSnake](https://hellogithub.com/periodical/statistics/click?target=https://github.com/MichalStrehovsky/SeeSharpSnake)：用 C# 写一个小于 8KB 的贪吃蛇。这个项目的重点不是教你如何用 C# 写出一个贪吃蛇游戏，而是讲解怎么将编译后的 C# 贪吃蛇程序，从最初的 65MB 精简成 8KB 大小、可以独立运行的应用。
```shell
# To build the 4.7 MB version of the game
dotnet publish -r win-x64 -c Release /p:Mode=CoreRT
# To build the 4.3 MB version of the game
dotnet publish -r win-x64 -c Release /p:Mode=CoreRT-Moderate
# To build the 3.0 MB version of the game
dotnet publish -r win-x64 -c Release /p:Mode=CoreRT-High
# To build the 1.2 MB version of the game
dotnet publish -r win-x64 -c Release /p:Mode=CoreRT-ReflectionFree
# To build the 10 kB version of the game
dotnet publish -r win-x64 -c Release /p:Mode=CoreRT-NoRuntime
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/231551119.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
7、[cpp-httplib](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yhirose/cpp-httplib)：一个文件的 C++ HTTP/HTTPS 库。这是一个用 C++11 写的仅头文件、跨平台的 HTTP/HTTPS 服务器端和客户端库，使用时十分方便，只需在代码中引入 `httplib.h` 文件。
```c++
#define CPPHTTPLIB_OPENSSL_SUPPORT
#include "path/to/httplib.h"

// HTTPS
httplib::Client cli("https://hellogithub.com");

auto res = cli.Get("/periodical");
res->status;
res->body;
```

8、[Ripes](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mortbopet/Ripes)：RISC-V 的模拟器和汇编编辑器。该项目可以通过图形化的方式，展示机器代码在各种微架构上运行的过程，可用于探索不同的高速缓存设计对性能的影响等问题。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/108505982.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[SFML](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SFML/SFML)：简单高效的 C++ 多媒体库。这是一个可用来简化游戏和多媒体应用开发的 C++ 库，因其上手门槛低和良好的生态，成为了众多 C++ 新手入门图形化开发的首选。来自 [@1024](https://hellogithub.com/user/yKq0Tx2oCRSzLcH) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/1524684.png' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
10、[css](https://hellogithub.com/periodical/statistics/click?target=https://github.com/primer/css)：GitHub 开源的设计系统。由 GitHub 设计团队开源和维护的项目，包含了 GitHub 的界面设计原则、使用指南和开箱即用的 UI 组件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/32551735.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
11、[d2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/terrastruct/d2)：一种可将文本转换为图表的脚本语言。该项目是一种图表脚本语言，可将文本转换为图表。你只需描述想要的图表，它就会生成对应的图像。
```shell
echo 'x -> y' > input.d2
d2 -w input.d2 out.svg
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/533087958.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[grpcurl](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fullstorydev/grpcurl)：类似 cURL 但用于 gRPC 的工具。一款实现与 gRPC 服务器交互的命令行工具，可以轻松请求 gRPC 服务，就像 gRPC 版的 cURL 一样好用。
```
# 安装
brew install grpcurl
# 使用
grpcurl grpc.server.com:443 my.custom.server.Service/Method
```

13、[shifu](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Edgenesis/shifu)：一款云原生物联网开发框架。这是一个生产级别的物联网平台，它可以将物联网(IoT)设备，封装成 K8s 的最小的可部署的计算单元(pod)，直接将设备的能力和数据通过 API 开放出来，让物联网应用的开发变得更加简单。
```shell
cd shifu
# 在集群中安装 Shifu
kubectl apply -f pkg/k8s/crd/install/shifu_install.yml
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/394207324.png' style="max-width:80%; max-height=80%;"></img></p>

14、[writefreely](https://hellogithub.com/periodical/statistics/click?target=https://github.com/writefreely/writefreely)：一起写作并建立一个社区。这是一个 Go 写的博客平台，除了能够创建基于 Markdown、极简的独立博客之外，还可以建立类似博客园的博客社区。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/86956808.png' style="max-width:80%; max-height=80%;"></img></p>

15、[yao](https://hellogithub.com/periodical/statistics/click?target=https://github.com/YaoApp/yao)：一款 Go 写的应用引擎。通过该项目最快几分钟，就能从零构建出一套系统，适合用于开发接口服务、管理后台、数据可视化平台、自建低代码平台等系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/403559729.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
16、[HummerRisk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HummerRisk/HummerRisk)：云原生安全检测平台。该项目用非侵入的方式，解决云原生环境的安全和治理问题。支持主流公/私有云资源的安全检测、漏洞扫描、一键获取报告等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/499359479.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[HydraLab](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/HydraLab)：开源的智能移动云测平台。这是一个基于 Spring Boot+React 构建的云测服务，它部署简单开箱即用，支持在线管理测试设备、执行测试用例、测试结果可视化等功能。来自 [@Nathan Bu](https://hellogithub.com/user/hsaTiud2BzvNP6g) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/486525050.png' style="max-width:80%; max-height=80%;"></img></p>

18、[neo4j](https://hellogithub.com/periodical/statistics/click?target=https://github.com/neo4j/neo4j)：目前最流行的图数据库。它是一款采用 Java 和 Scala 语言开发的原生图数据库，专属的查询语言 Cypher，能够直观且高效地查询和处理数据之间的关系。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/6650539.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
19、[html2canvas](https://hellogithub.com/periodical/statistics/click?target=https://github.com/niklasvh/html2canvas)：实现浏览器内截屏的 JavaScript 库。该项目可以让你在浏览器内对整个网页或部分内容进行截图，原理是通过读取 DOM 和样式，将当前页面渲染成一个画布图像。
```javascript
html2canvas(document.querySelector("#capture")).then(canvas => {
    document.body.appendChild(canvas)
});
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/2056312.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[JavaScript-Algorithms](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sisterAn/JavaScript-Algorithms)：教你从零构建前端算法体系。学习算法不仅是为了面试，也是每个前端进阶必备的技能之一。该项目包含了前端的进阶算法、常见面试题、手写源码等，帮你构建完整的数据结构和算法的知识体系。

21、[pomotroid](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Splode/pomotroid)：视觉上令人愉悦的番茄时钟。这是一款 Vue 写的拥有超高颜值的番茄计时器，支持自定义时间、回合数、提示音、桌面通知等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/119006816.png' style="max-width:80%; max-height=80%;"></img></p>

22、[satori](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vercel/satori)：能够将 HTML 和 CSS 转换为 SVG 的库。由 Vercel 团队开源的可根据 HTML 和 CSS 代码生成 SVG 图像的库。支持 JSX 语法，使用起来十分方便和顺手。
```typescript
import satori from 'satori'

const svg = await satori(
  <div style={{ color: 'black' }}>hello, world</div>,
  {
    width: 600,
    height: 400,
    fonts: [
      {
        name: 'Roboto',
        data: robotoArrayBuffer,
        weight: 400,
        style: 'normal',
      },
    ],
  },
)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/452769633.png' style="max-width:80%; max-height=80%;"></img></p>

23、[underscore](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jashkenas/underscore)：强大的 JavaScript 函数库。该库提供了 100 多个实用的函数，包括常用的 map、filter、reduce、invoke 以及更专业的辅助函数，比如函数绑定、JavaScript 模板功能、创建快速索引等，让我们可以更加方便地在 JavaScript 中实现函数式编程。来自 [@Y. S](https://hellogithub.com/user/nSRYiOjq19vby5B) 的分享
```javascript
// countBy
_.countBy([1, 2, 3, 4, 5], function(num) {
  return num % 2 == 0 ? 'even': 'odd';
});
// 输出：{odd: 3, even: 2}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/349241.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
24、[bandit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PyCQA/bandit)：查找 Python 代码中常见安全问题的工具。该项目是 PyCQA 出品的 Python 代码检测工具，知名的 isort 和 flake8 就是他们开源的。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/131129792.png' style="max-width:80%; max-height=80%;"></img></p>

25、[devguide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/python/devguide)：CPython 开发人员指南。这份指南来自 Python 官方，介绍了如何为 CPython 做贡献，适用于任何阶段的贡献者。

26、[Django-Styleguide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HackSoftware/Django-Styleguide)：Django 使用姿势指南。这是一份 Django 编码风格指南，它来自于一线团队的多年经验总结，希望能够帮助你构建出更好的 Django 应用程序。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/142351241.png' style="max-width:80%; max-height=80%;"></img></p>

27、[numpy-100](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rougier/numpy-100)：Numpy 的练习册。该项目包含了 100 个关于 Python 常用的数据处理库 Numpy 的练习和解决方案。
```python
# How to sum a small array faster than np.sum? (★★☆)

Z = np.arange(10)
np.add.reduce(Z)
```

28、[prefect](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PrefectHQ/prefect)：Python 的数据流编排平台。如果将获取、清洗、处理数据的程序当作一个个分散的任务，该项目可以将这些任务整合到工作流中，实现在一个 Web 平台部署、安排和监控它们的执行。
```python
from prefect import flow, task

@task
def say_hello():
	print("Hello, World! I'm HelloGitHub!")

@flow("Prefect Flow"):
def h_flow():
	say_hello()

# run the flow!
h_flow() # "Hello, World! I'm HelloGitHub!"
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/139199684.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby 项目
29、[YouPlot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/red-data-tools/YouPlot)：Ruby 写的命令行数据可视化工具。该项目能够在终端里将数据转化成彩色的图表，支持条形图、直方图、箱型图等类型的图表。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/283230219.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
30、[ChatGPT](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lencx/ChatGPT)：第三方的 ChatGPT 桌面应用。把 ChatGPT 放到你的桌面，支持快捷键、斜杠命令、划词搜索、导出记录等实用的功能，适用于 macOS、Windows、Linux 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/575340621.png' style="max-width:80%; max-height=80%;"></img></p>

31、[gitui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gitui-org/gitui)：带界面的 Git 命令行工具。该项目为 git 提供了终端界面，让用户可以更加顺畅地使用 git。交互式的操作提示，让你无需再记忆大量的 git 命令。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/247725846.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
32、[vimac](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nchudleigh/vimac)：用键盘代替鼠标的 macOS 应用。它可以让用户实现仅通过键盘操作苹果电脑，支持两种操作模式。
- 激活模式：将屏幕上可点击的位置，映射成键盘按键
- 滚动模式：使用 HJKL 按键，可完成区域滚动

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/206583780.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
33、[annotated_deep_learning_paper_implementations](https://hellogithub.com/periodical/statistics/click?target=https://github.com/labmlai/annotated_deep_learning_paper_implementations)：深度学习论文的实现集合。这是一个关于神经网络和相关算法 PyTorch 实现的集合，代码里还包含逐行的注释。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/290091948.png' style="max-width:80%; max-height=80%;"></img></p>

34、[Chinese-CLIP](https://hellogithub.com/periodical/statistics/click?target=https://github.com/OFA-Sys/Chinese-CLIP)：OpenAI CLIP 模型中文预训练版本。该项目使用了大规模的中文数据进行训练（~2亿图文数据），提供了多个规模的预训练模型和技术报告，让使用者仅通过几行代码就能完成中文图文特征提取和图文检索。
```python
import torch 
from PIL import Image

import cn_clip.clip as clip
from cn_clip.clip import load_from_name, available_models
print("Available models:", available_models())  
# Available models: ['ViT-B-16', 'ViT-L-14', 'ViT-L-14-336', 'ViT-H-14', 'RN50']

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = load_from_name("ViT-B-16", device=device, download_root='./')
model.eval()
image = preprocess(Image.open("examples/pokemon.jpeg")).unsqueeze(0).to(device)
text = clip.tokenize(["杰尼龟", "妙蛙种子", "小火龙", "皮卡丘"]).to(device)

with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    # 对特征进行归一化，请使用归一化后的图文特征用于下游任务
    image_features /= image_features.norm(dim=-1, keepdim=True) 
    text_features /= text_features.norm(dim=-1, keepdim=True)    

    logits_per_image, logits_per_text = model.get_similarity(image, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

print("Label probs:", probs)  # 图文匹配概率 [[1.268734e-03 5.436878e-02 6.795761e-04 9.436829e-01]]
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/511745849.png' style="max-width:80%; max-height=80%;"></img></p>

35、[KuiperInfer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zjhellofss/KuiperInfer)：从零编写深度学习推理框架的教程。手把手教你用 C++ 写出一个深度学习推理框架，项目整体风格和结构借鉴了Caffe。初学者通过该教程不仅可以了解深度学习框架背后的知识，还能够学会如何上手一个中等规模的 C++ 项目。来自 [@炸排骨](https://hellogithub.com/user/vIKAZxSG1s2iyDE) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/568649213.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
36、[cdn-up-and-running](https://hellogithub.com/periodical/statistics/click?target=https://github.com/leandromoreira/cdn-up-and-running)：从零开始构建 CDN 的教程。为了让你在实战中学习 CDN 的工作原理，这里会从创建一个单一的后端服务开始，逐渐扩展到多个节点、模拟延迟、可视化、可测试的 CDN 服务。因为设计 CDN 会涉及 Nginx、Lua、Docker、Grafana 等知识点，所以学习该教程需要有一定的编程基础。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/441214263.png' style="max-width:80%; max-height=80%;"></img></p>

37、[fluentui-emoji](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/fluentui-emoji)：一套可爱的 emoji 表情。该项目是微软开源的一套精致、可爱的 emoji 表情包。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/390896426.png' style="max-width:80%; max-height=80%;"></img></p>

38、[k8s_PaaS](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ben1234560/k8s_PaaS)：教你用 K8s 部署一套完整服务的教程。通过该教程你可以学习到如何部署 Kubernetes 集群，以及在此基础上搭建由 Apollo、Jenkins、Prometheus 等服务组成的完整的软件研发和部署平台。来自 [@郭学威](https://hellogithub.com/user/YRakbLESMsm7c9l) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/294880855.png' style="max-width:80%; max-height=80%;"></img></p>

39、[pi-apps](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Botspot/pi-apps)：最受欢迎的树莓派应用商店。这是一款完全免费、开源的树莓派应用商店，它安装简单使用方便，内置了 200 多个应用程序，支持 32 位和 64 位的 Raspberry Pi OS。
```shell
# 下载
git clone https://github.com/Botspot/pi-apps
# 安装
~/pi-apps/install
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/297820951.png' style="max-width:80%; max-height=80%;"></img></p>

40、[smiley-sans](https://hellogithub.com/periodical/statistics/click?target=https://github.com/atelier-anchor/smiley-sans)：一款完全开源、精雕细琢的中文黑体。这款字体名为「得意黑」，整体字身窄而斜，细节融入了取法手绘美术字的特殊造型。支持简体中文常用字、拉丁字母、阿拉伯数字和各种标点符号。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/564785929.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
41、[essential-netty-in-action](https://hellogithub.com/periodical/statistics/click?target=https://github.com/waylau/essential-netty-in-action)：《Netty 实战》精简版。该书是《Netty in Action》的中文精简版，带你快速掌握 Netty。

42、[time-as-a-friend](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xiaolai/time-as-a-friend)：《把时间当作朋友》。做事不一定要图快，马跑起来比骆驼快，但骆驼一生走过的路却是马的两倍。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/82/175853072.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub81.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub83.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/82'>这里</a>。
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
