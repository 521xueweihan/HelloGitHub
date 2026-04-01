# HelloGitHub Vol.54
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C
1、[libevent](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/libevent/libevent)：C 语言实现的轻量级、高性能事件通知库。基于事件驱动，支持多种 I/O 多路复用技术：epoll、poll、select、kqueue 等。libevent 就是这些系统基础库的统一封装，提供更高级的 API 并解决跨平台的问题


### C#
2、[dotnet-docker](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dotnet/dotnet-docker)：.NET Core 和 Tools 的 Docker 镜像


3、[machinelearning](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dotnet/machinelearning)：微软开源的 C# 机器学习框架。支持的机器学习类任务：分类、回归、聚类等，[教程和视频](https://dotnet.microsoft.com/learn/ml-dotnet)。示例代码：
```C
var dataPath = "sentiment.csv";
var mlContext = new MLContext();
var loader = mlContext.Data.CreateTextLoader(new[]
    {
        new TextLoader.Column("SentimentText", DataKind.String, 1),
        new TextLoader.Column("Label", DataKind.Boolean, 0),
    },
    hasHeader: true,
    separatorChar: ',');
var data = loader.Load(dataPath);
var learningPipeline = mlContext.Transforms.Text.FeaturizeText("Features", "SentimentText")
        .Append(mlContext.BinaryClassification.Trainers.FastTree());
var model = learningPipeline.Fit(data);

var predictionEngine = mlContext.Model.CreatePredictionEngine<SentimentData, SentimentPrediction>(model);
var prediction = predictionEngine.Predict(new SentimentData
{
    SentimentText = "Today is a great day!"
});
Console.WriteLine("prediction: " + prediction.Prediction);
```


### C++
4、[drogon](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/drogonframework/drogon)：一款 C++ 的异步非阻塞高性能 Web 框架。功能强大、上手容易，使得用 C++ 语言构建各种类型的高性能 Web 应用，变得更加方便。示例代码：
```C++
#include <drogon/drogon.h>
using namespace drogon;
int main()
{
    app().setLogPath("./")
         .setLogLevel(trantor::Logger::kWarn)
         .addListener("0.0.0.0", 80)
         .setThreadNum(16)
         .enableRunAsDaemon()
         .run();
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/131236938.png' style="max-width:80%; max-height=80%;"></img></p>

### CSS
5、[css-diner](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/flukeout/css-diner)：通过游戏方式在线学习 CSS 选择器知识。初学者可以通过简单的动画界面，学习 CSS 多种选择器语法是如何筛选出页面的元素，虽然是英文网站但还算通俗易懂。[在线尝试](https://flukeout.github.io/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/16636908.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
6、[go-admin](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/go-admin-team/go-admin)：基于 Gin+Vue+Element UI 的前后端分离权限管理系统。文档齐全、还有视频教程适合新手学习，特点：
- 遵循 RESTful API 设计规范
- 基于 Gin Web API 框架，提供了丰富的中间件支持（用户认证、跨域、访问日志、追踪 ID 等）
- 支持 Swagger 文档
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/247032621.png' style="max-width:80%; max-height=80%;"></img></p>

7、[go-micro](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/micro/go-micro)：一款 Go 插件化的基础框架。我只知道它是个 Go 微服务框架，基于它可以快速构建微服务。示例代码如图所示：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/29217054.png' style="max-width:80%; max-height=80%;"></img></p>

8、[now](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jinzhu/now)：Go 语言的时间工具库。项目简单、代码易懂，示例代码丰富：
```go
import "github.com/jinzhu/now"

time.Now() // 2013-11-18 17:51:49.123456789 Mon

now.BeginningOfMinute()        // 2013-11-18 17:51:00 Mon
now.BeginningOfHour()          // 2013-11-18 17:00:00 Mon
now.BeginningOfDay()           // 2013-11-18 00:00:00 Mon
now.BeginningOfWeek()          // 2013-11-17 00:00:00 Sun
now.BeginningOfMonth()         // 2013-11-01 00:00:00 Fri
now.BeginningOfQuarter()       // 2013-10-01 00:00:00 Tue
now.BeginningOfYear()          // 2013-01-01 00:00:00 Tue

now.WeekStartDay = time.Monday // Set Monday as first day, default is Sunday
now.BeginningOfWeek()          // 2013-11-18 00:00:00 Mon

now.EndOfMinute()              // 2013-11-18 17:51:59.999999999 Mon
now.EndOfHour()                // 2013-11-18 17:59:59.999999999 Mon
now.EndOfDay()                 // 2013-11-18 23:59:59.999999999 Mon
now.EndOfWeek()                // 2013-11-23 23:59:59.999999999 Sat
now.EndOfMonth()               // 2013-11-30 23:59:59.999999999 Sat
now.EndOfQuarter()             // 2013-12-31 23:59:59.999999999 Tue
now.EndOfYear()                // 2013-12-31 23:59:59.999999999 Tue

now.WeekStartDay = time.Monday // Set Monday as first day, default is Sunday
now.EndOfWeek()                // 2013-11-24 23:59:59.999999999 Sun
```


9、[pgweb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sosedoff/pgweb)：基于 Go 实现的跨平台 PostgreSQL 数据库管理工具。通过本地起服务+浏览器的方式解决了跨平台的问题，启动命令：
```
三种方式：

参数：pgweb --host localhost --user myuser --db mydb
URL：pgweb --url postgres://user:password@host:port/database?sslmode=[mode]
Socket：pgweb --url "postgres:///database?host=/absolute/path/to/unix/socket/dir"
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/24968828.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
10、[roncoo-pay](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/roncoo/roncoo-pay)：开源的 Java 互联网业务支付系统。拥有独立的账户体系、用户体系、支付接入体系、支付交易体系、对账清结算体系等，想学习支付相关技术的同学可以看看这个项目。项目结构如下：
```
roncoo-pay
|
├── roncoo-pay-app-notify //商户通知模块
|
├── roncoo-pay-app-order-polling //订单轮询模块
|
├── roncoo-pay-app-reconciliation //交易对账模块
|
├── roncoo-pay-app-settlement //交易结算模块
|
├── roncoo-pay-common-core //公共基础模块，不需要单独部署
|
├── roncoo-pay-service //核心业务模块，不需要单独部署
|
├── roncoo-pay-web-boss //运营后台模块
|
├── roncoo-pay-web-gateway //支付网关模块
|
├── roncoo-pay-web-merchant //商户后台模块
|
├── roncoo-pay-web-sample-shop //模拟商城模块
```


11、[screw](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pingfangushi/screw)：简单好用的数据库表结构文档生成工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/273891882.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
12、[IconPark](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bytedance/IconPark)：该开源库提供了 1200+ 高质量图标，还有一个界面便于定制图标。强大之处是可以通过改变一个 SVG 文件的属性来变换出多种主题，支持导出 SVG、PNG、Vue 和 React 图标组件等。极大的方便了设计师和开发者，让他们有更多时间逛 HG 了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/282828123.png' style="max-width:80%; max-height=80%;"></img></p>

13、[mind-elixir-core](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SSShooter/mind-elixir-core)：一款免费开源的思维导图 JS 库。[在线尝试](https://mindelixir.ink/#/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/199951138.jpg' style="max-width:80%; max-height=80%;"></img></p>

14、[next](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alibaba-fusion/next)：一套企业级中后台 UI 解决方案，致力于解决设计师与前端在工作协同、产品体验一致性、开发效率方面的问题。就是设计师修改颜色之类的，可以生成一个 NPM 主题包，前端拿到这个包就可以直接还原设计师的设计


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/138132664.png' style="max-width:80%; max-height=80%;"></img></p>

15、[tesseract.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/naptha/tesseract.js)：支持多种语言的文字识别的 JS 库，能够方便、准确的把图片中的文字解析提取出来（就能复制了）。基于 Tesseract OCR 引擎实现的 JS 版本，方便前端实现文字识别功能和在浏览器中直接使用。[在线尝试](https://tesseract.projectnaptha.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/37958358.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
16、[DateTimePicker](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/loper7/DateTimePicker)：一个简约、漂亮的日期时间选择器。支持 100% 自定义 UI，内置日期时间选择弹窗基于 Google BottomSheetDialog


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/245125241.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
17、[Computer-Networking-A-Top-Down-Approach-NOTES](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES)：《计算机网络－自顶向下方法》编程作业。包含问题和 Python 代码解答，Wireshark 实验部分为官方文档的翻译


18、[learn-python3](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jerry-git/learn-python3)：一份 Python3 的教程，请查收。该教程采用 Jupyter notebooks 形式，便于运行和阅读。并且还包含了练习题，对新手友好。缺点的话就是英文的教程，但是我都能看懂你肯定也可以


19、[livebox](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/parzulpan/livebox)：一个网络直播聚合平台，能够观看视频直播、高清电视和收听广播电台等。目前支持 30+ 个视频直播、50+ 个高清电视频道和 70+ 个广播电台，比较全面的 Web 项目，用到的技术栈：
- 前端/客户端：Qt、Vue、Flutter 等
- 后端：MySQL、Redis、Kafka/RabbitMQ、Elasticsearch 等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/272427828.png' style="max-width:80%; max-height=80%;"></img></p>

20、[readthedocs.org](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/readthedocs/readthedocs.org)：知名文档社区网站（readthedocs.org）的开源源码。该网站上托管了：Scrapy、requests、bootstrap-datepicker 等知名库的文档，我看了下项目是基于 Django 开发的，文件有些多看起来需要点耐心


21、[taichi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/taichi-dev/taichi)：一个高性能图形学编程框架。它可以将你编写的 Python 代码转换成高效的汇编代码，在多 CPU 和 GPU 上运行，相当于是在用 Python 的语法写着色器。Taichi 解决了图形学配环境难，代码移植性差等问题，只需 `pip install taichi` 即可安装，编写的程序在 Windows、Linux、OSX 上均可运行，降低了新手学习图形学的门槛。示例代码：
```python
import taichi as ti

ti.init(arch=ti.gpu)  # 指定编译后的函数在 GPU 上执行

n = 320
pixels = ti.field(dtype=float, shape=(n * 2, n))  # 提前声明数组存储类型，大小


@ti.func  # 该函数将是被调用的过程函数
def complex_sqr(z):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])


@ti.kernel  # 该函数将被 Taichi 编译
def paint(t: float):
    for i, j in pixels:  # 最外层循环会自动并行化
        c = ti.Vector([-0.8, ti.cos(t) * 0.2])
        z = ti.Vector([i / n - 1, j / n - 0.5]) * 2
        iterations = 0
        while z.norm() < 20 and iterations < 50:  # 其他语法和原生 Python 基本一致
            z = complex_sqr(z) + c
            iterations += 1
        pixels[i, j] = 1 - iterations * 0.02


gui = ti.GUI("Julia Set", res=(n * 2, n))

for i in range(1000000):
    paint(i * 0.03)
    gui.set_image(pixels)
    gui.show()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/74660642.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust
22、[rustlings](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rust-lang/rustlings)：该项目通过一个个简单练习小 demo，让初学者学习 Rust 的语法。通过简单的命令即可安装本项目，然后修改每个小练习，达到编译通过或者目标输出，通过后会进入下一关，有种闯关的成就感。运行方法：
```
安装：
git clone https://github.com/rust-lang/rustlings
cd rustlings
git checkout tags/4.0.0 # or whatever the latest version is (find out at https://github.com/rust-lang/rustlings/releases/latest)
cargo install --force --path .

安装完后，运行：
rustlings watch
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/42489829.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
23、[ZLPhotoBrowser](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/longitachi/ZLPhotoBrowser)：轻量级照片选择框架。它使用简单、功能丰富，支持预览/相册内拍照及录视频、拖拽/滑动选择、编辑裁剪图片/视频等功能。示例代码：
```swift
// 使用起来非常简单
let ac = ZLPhotoPreviewSheet()
ac.selectImageBlock = { [weak self] (images, assets, isOriginal) in
    // your code
}
// 快速选择方法
ac.showPreview(animate: true, sender: self)
// 进入相册选择方法
ac.showPhotoLibrary(sender: self)
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/47162528.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
24、[computervision-recipes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/computervision-recipes)：计算机视觉系统最佳实践，包含各种 CV 示例项目。示例使用 PytTorch 深度学习库+ Jupyter 文件，涵盖：图像分类、相似、识别、追踪等方面，适合对图像方面感兴趣的小伙伴阅读和学习


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/170161374.jpg' style="max-width:80%; max-height=80%;"></img></p>

25、[nsfw-filter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nsfw-filter/nsfw-filter)：基于 tensefow.js 实现的过滤 NSFW（裸露、暴力等）图片的浏览器插件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/278011746.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[seq2seq-couplet](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wb14123/seq2seq-couplet)：基于深度学习的对对联项目，你出上联它自动生成下联。我尝试了下，对得三观很正，还挺有意思。[在线尝试](https://ai.binwang.me/couplet/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/122696125.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
27、[Halfrost-Field](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/halfrost/Halfrost-Field)：前阿里巴巴资深后端工程师“霜神”的技术博客，分享前、后端的技术干货。作者日常工作语言是 Go，在进入阿里巴巴之前，做了几年前端工作。文章内容包含：机器学习、Go、JS、iOS、网络协议等系列


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/86981606.png' style="max-width:80%; max-height=80%;"></img></p>

28、[hexo-theme-matery](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/blinkfox/hexo-theme-matery)：一款采用 Material Design 和响应式设计的 Hexo 博客主题。特点：
- 响应式设计，博客在桌面端、平板、手机等设备上均能很好的展现
- 首页轮播文章及每天动态切换 Banner 图片
- 时间轴式的归档页
- 词云的标签页和雷达图的分类页
- 丰富的关于我页面（包括关于我、文章统计图、我的项目、我的技能、相册等）
- 支持文章置顶和文章打赏
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/146325535.png' style="max-width:80%; max-height=80%;"></img></p>

29、[highlight.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/highlightjs/highlight.js)：让网页上的代码实现高亮的 JS 库，给代码点颜色瞧瞧。支持多种编程语言和样式，使用简单。示例代码：
```html
<link rel="stylesheet" href="/path/to/styles/default.css">
<script src="/path/to/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
<pre><code>...</code></pre>
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/1213225.png' style="max-width:80%; max-height=80%;"></img></p>

30、[L-ink_Card](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/peng-zhihui/L-ink_Card)：该项目包含了制作一个迷你 NFC 智能卡的代码和教程。野生钢铁侠稚晖出品的[演示视频](https://www.bilibili.com/video/BV1Cf4y1y7KT/)，他还制作了很多别的有趣的东西，大家可以去看看很有意思


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/273689548.jpg' style="max-width:80%; max-height=80%;"></img></p>

31、[lite](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rxi/lite)：一款用 Lua 编写的超级轻量级的文本编辑器。在 Windows 下的 exe 文件虽然只有 300KB 左右，但颜值、功能和速度却一点都不差，甚至还支持使用自定义插件、配色主题等功能。小而美的文本编辑器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/230599151.png' style="max-width:80%; max-height=80%;"></img></p>

32、[ntfstool](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ntfstool/ntfstool)：一款为苹果电脑提供 NTFS 读写支持的免费工具。有了它就可以很方便的在苹果电脑上读写，从 Windows 系统拷贝数据的 U 盘和移动硬盘等。[安装说明](https://github.com/ntfstool/ntfstool/blob/master/README-CN.md)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/242364937.jpeg' style="max-width:80%; max-height=80%;"></img></p>

### Book
33、[jshistory-cn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/doodlewind/jshistory-cn)：《JavaScript 20 年》中文版。[在线阅读](https://cn.history.js.org/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/255242703.png' style="max-width:80%; max-height=80%;"></img></p>

34、[trpl-zh-cn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/KaiserY/trpl-zh-cn)：《Rust 程序设计语言（第二版）》中文翻译。[在线阅读](https://kaisery.github.io/trpl-zh-cn/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/54/80980931.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub53.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub55.md">『Next』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/en/periodical'>Submit open-source project!</a> 👈<br>
</p>

## Sponsor


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


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
