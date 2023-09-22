# 《HelloGitHub》第 76 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/76) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[gb-studio](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chrismaltby/gb-studio)：简单好玩的 Game Boy 游戏制作工具。这是一款可视化游戏构建工具。无需编程基础即可通过拖拽的方式，快速制作出复古风格的 Game Boy 游戏。不仅支持导出游戏 ROM，还可以直接构建成在线游戏。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/181894913.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[jq](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jqlang/jq)：轻快的命令行 JSON 处理器。JSON 作为最常见的序列化格式，日常开发中经常会遇到。这个项目可以通过简单的命令对 JSON 数据进行格式化、过滤等操作，还支持直接解析接口的 JSON 数据，十分灵活和方便。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/5101141.png' style="max-width:80%; max-height=80%;"></img></p>

3、[libvips](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/libvips/libvips)：极快的多线程图像处理库。具有占用内存小、处理速度快等特点的图像处理底层库。它能够处理多种图像和像素格式，为了使用方便不仅支持命令行调用，官方还提供了 Ruby、Python 等多种编程语言的 SDK。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/1291410.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
4、[CrazyCar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TastSong/CrazyCar)：一款用 Unity 制作的联机赛车游戏。这是一套完整的网络联机游戏解决方案，项目包含游戏端、服务器端、网络传输和管理后台。游戏支持计时赛、多人比赛、个人成就、资源热更等特性，可以运行在 iOS/Android/Windows 设备上。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/416555156.png' style="max-width:80%; max-height=80%;"></img></p>

5、[Masuit.Tools](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ldqk/Masuit.Tools)：C# 开发工具箱。该库包含了 C# 日常开发常用的操作类，比如字符串处理、进制转换、日期处理、加密/解密、文件压缩、图像裁剪、断点续传、分布式 ID 等。
```csharp
double milliseconds = DateTime.Now.GetTotalMilliseconds();// 获取毫秒级时间戳
double microseconds = DateTime.Now.GetTotalMicroseconds();// 获取微秒级时间戳
double nanoseconds = DateTime.Now.GetTotalNanoseconds();// 获取纳秒级时间戳
double seconds = DateTime.Now.GetTotalSeconds();// 获取秒级时间戳
double minutes = DateTime.Now.GetTotalMinutes();// 获取分钟级时间戳
```

### C++ 项目
6、[CppCoreGuidelines](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/isocpp/CppCoreGuidelines)：C++ 核心指南。一份由 C++ 之父 Bjarne Stroustrup 领导的 C++ 编码指南，目的是为了帮助大家更好地使用现代 C++。这个项目主要讨论的是关于 C++ 编写接口、内存管理、并发等方面的问题，适合有一定 C++ 基础想要进阶的小伙伴。

7、[flatbuffers](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/flatbuffers)：谷歌开源的高性能序列化库。类似 Protocol Buffers 的序列化格式，但解析速度更快、占用内存更少，多用于对解析耗时敏感的 Android 应用和游戏。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/19953044.png' style="max-width:80%; max-height=80%;"></img></p>

8、[imgui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ocornut/imgui)：游戏行业内流行的轻量级 C++ 图形界面库。这是个即时模式的 GUI 框架，控件都需要手绘。优点是更加灵活和轻量，可以快速构建功能简单、体积小的 GUI 程序，但不适合用来实现复杂动画的 GUI 应用，多用于开发游戏内的 GUI 工具。
```C++
ImGui::Text("Hello, world %d", 123);
if (ImGui::Button("Save"))
    MySaveFunction();
ImGui::InputText("string", buf, IM_ARRAYSIZE(buf));
ImGui::SliderFloat("float", &f, 0.0f, 1.0f);
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/22067521.jpg' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
9、[css-protips](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AllThingsSmitty/css-protips)：CSS 专业技巧。一个帮你提升 CSS 技巧的收藏集。

10、[ui-buttons](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/eludadev/ui-buttons)：CSS 按钮样式集合。该项目实现了 100 种不同样式的按钮。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/492267422.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
11、[gitleaks](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gitleaks/gitleaks)：一款静态应用程序安全测试(SAST)工具。它可以检测项目中是否包含密码、API Key、token 等信息，还能够轻松整合到 Git Hook 和 GitHub Action，实现提交代码时自动检测，通过告警和阻止 push 等方式，有效地防止敏感信息泄漏。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/119190187.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[mercure](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dunglas/mercure)：一种用于实时通信的开放式协议。该项目是基于 HTTP 和 SSE 的一种协议，然后用 Go 语言实现的实时推送服务。相较于 WebSocket 协议它使用起来更加简单，客户端发起订阅就和请求普通的 HTTP 接口一样，而且在 HTTP/2 下还可以双向通信。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/140949512.png' style="max-width:80%; max-height=80%;"></img></p>

13、[ptg](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/crossoverJie/ptg)：用 Go 写的 GUI gRPC 客户端。作者在调试 gPRC 接口时，发现没有类似 postman 趁手的 gPRC 客户端，所以就自己动手写了一个然后开源了。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/415986304.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[wechat-backup](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/greycodee/wechat-backup)：本地备份微信聊天记录的工具。它能够将手机上的微信聊天记录，解密后保存在电脑上，支持查看、搜索、恢复微信聊天记录。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/503408858.png' style="max-width:80%; max-height=80%;"></img></p>

15、[wild-workouts-go-ddd-example](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example)：Go DDD 示例项目。该项目通过一个预约系统的示例，展示了如何在 Go 项目中实现领域驱动设计(DDD)和读写分离架构(CQRS)。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/261871717.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
16、[forest](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dromara/forest)：极简的声明式 Java HTTP 客户端。一个开源的 Java HTTP 客户端框架，采用声明式的开发方式，分分钟即可完成 HTTP 请求的定义、发送、接收、解析、错误处理、日志打印等操作。
```java
public interface AmapClient {
    /**
     * @Get注解代表该方法专做GET请求
     * 在url中的{0}代表引用第一个参数，{1}引用第二个参数
     */
    @Get("http://ditu.amap.com/service/regeo?longitude={0}&latitude={1}")
    Map getLocation(String longitude, String latitude);
}

// 注入接口实例
@Autowired
private AmapClient amapClient;
...
// 调用接口
Map result = amapClient.getLocation("121.475078", "31.223577");
System.out.println(result);
```

17、[liteflow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dromara/liteflow)：轻快、稳定可编排的规则引擎。规则引擎能够帮助系统解耦，实现通过修改规则就可以适应复杂多变的业务逻辑。这是一个功能强大的 Java 规则引擎，支持同步异步混编、平滑热刷新，无需重启应用即可让新规则生效，规则语法简单、文档通俗易懂，学习门槛低容易上手。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/250036571.png' style="max-width:80%; max-height=80%;"></img></p>

18、[picocli](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/remkop/picocli)：构建 Java 命令行应用的框架。简单易用寥寥几行代码，就可以完成一个 Java 命令行应用程序。虽然由 Java 编写但可以在 Groovy、Kotlin、Scala 中使用，支持命令自动补全、颜色、子命令、帮助信息等功能。
```java
import picocli.CommandLine;
import picocli.CommandLine.Option;
import picocli.CommandLine.Parameters;
import java.io.File;

@Command(name = "example", mixinStandardHelpOptions = true, version = "Picocli example 4.0")
public class Example implements Runnable {

    @Option(names = { "-v", "--verbose" },
      description = "Verbose mode. Helpful for troubleshooting. Multiple -v options increase the verbosity.")
    private boolean[] verbose = new boolean[0];

    @Parameters(arity = "1..*", paramLabel = "FILE", description = "File(s) to process.")
    private File[] inputFiles;

    public void run() {
        if (verbose.length > 0) {
            System.out.println(inputFiles.length + " files to process...");
        }
        if (verbose.length > 1) {
            for (File f : inputFiles) {
                System.out.println(f.getAbsolutePath());
            }
        }
    }

    public static void main(String[] args) {
        // By implementing Runnable or Callable, parsing, error handling and handling user
        // requests for usage help or version help can be done with one line of code.

        int exitCode = new CommandLine(new Example()).execute(args);
        System.exit(exitCode);
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/80640282.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
19、[mjml](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mjmlio/mjml)：能够快速制作出响应式邮件的框架。邮件样式是一个让人头疼的问题，而通过这个项目制作的邮件，可以正常地显示在不同的邮件客户端。它还提供了在线编辑器，以及多种邮件模版和丰富的组件，能够帮你快速制作出精美、移动端优先、响应式的邮件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/50586840.png' style="max-width:80%; max-height=80%;"></img></p>

20、[naive-ui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tusen-ai/naive-ui)：仅支持 Vue3 的组件库。拥有完善的 TypeScript 类型推导的 Vue3 组件库，拥有 80 多种组件、中文文档，如果你想换换“口味”可以试试它。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/373855820.png' style="max-width:80%; max-height=80%;"></img></p>

21、[regex-vis](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Bowen7/regex-vis)：在线可视化正则编辑器。该项目可将输入的正则表达式，自动生成对应的可视化图形，支持通过编辑图形节点修改正则表达式，以及对正则表达式进行测试等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/295656398.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[vxe-table](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/x-extends/vxe-table)：好用的 Vue 表格组件。支持增删改查、虚拟列表、大数据懒加载、数据校验、分页、弹窗等功能的 Vue 表格组件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/182395618.png' style="max-width:80%; max-height=80%;"></img></p>

23、[wangEditor](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wangeditor-team/wangEditor)：一款开源的 Web 富文本编辑器。基于 slate.js 和 snabbdom.js 实现的富文本编辑器，支持 JS、Vue 和 React 框架。开箱即用仅需几行代码，就能实现一个功能齐全的富文本编辑器。
```javascript
import '@wangeditor/editor/dist/css/style.css'
import { createEditor, createToolbar } from '@wangeditor/editor'

// 创建编辑器
const editor = createEditor({
  selector: '#editor-container'
})
// 创建工具栏
const toolbar = createToolbar({
  editor,
  selector: '#toolbar-container'
})
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/26262860.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
24、[typing-learner](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tangshimin/typing-learner)：可通过视频生成单词本的背单词应用。该项目可将 MKV 格式的英文视频制作成单词库，在记忆单词时可通过台词和播放视频片段，让每个单词都有语境，帮助理解和记忆英文单词。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/479222482.gif' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C 项目
25、[lemon-cleaner](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/lemon-cleaner)：苹果电脑专属的清理工具。腾讯开源的免费 macOS 设备空间清理工具「柠檬清理」，支持深度清理、删除重复文件、卸载应用、状态栏显示等功能，能够一键轻松清理垃圾释放空间。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/513077635.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
26、[course-tencent-cloud](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xiaochong0302/course-tencent-cloud)：PHP 写的网课平台。依托腾讯云基础服务架构，采用 Phalcon 框架开发的网课系统，支持付费、点播、直播、专栏、问答、会员、秒杀等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/296000242.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
27、[diagrams](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mingrammer/diagrams)：用 Python 代码图解系统架构。程序员在做技术方案的时候，系统架构图是必不可少的。该项目将绘制架构图时所需的图标，封装成了对应的类极易调用，文档还提供了丰富的示例，让你分分钟就能上手，轻松用 Python 快速绘制出一份精美且清晰的架构图，这样不仅能省去拖拽调整连线的步骤，而且代码还可以复用，以便应对不断迭代升级的架构。
```python
with Diagram("Advanced Web Service with On-Premise", show=False):
    ingress = Nginx("ingress")

    metrics = Prometheus("metric")
    metrics << Grafana("monitoring")

    with Cluster("Service Cluster"):
        grpcsvc = [
            Server("grpc1"),
            Server("grpc2"),
            Server("grpc3")]

    with Cluster("Sessions HA"):
        primary = Redis("session")
        primary - Redis("replica") << metrics
        grpcsvc >> primary

    with Cluster("Database HA"):
        primary = PostgreSQL("users")
        primary - PostgreSQL("replica") << metrics
        grpcsvc >> primary

    aggregator = Fluentd("logging")
    aggregator >> Kafka("stream") >> Spark("analytics")

    ingress >> grpcsvc >> aggregator
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/237791077.png' style="max-width:80%; max-height=80%;"></img></p>

28、[labelImg](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HumanSignal/labelImg)：图形化界面的图像标注工具。用 Python 和 Qt 编写的图像标注桌面应用，简单方便下载就能用，适用于 Windows、Linux、macOS。标注数据支持 PASCAL VOC 格式的 XML 文件和 YOLO 的 txt 文件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/42625970.jpg' style="max-width:80%; max-height=80%;"></img></p>

29、[MechanicalSoup](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MechanicalSoup/MechanicalSoup)：自动与网站交互的轻量级 Python 库。我们写爬虫一般是请求+解析两步走，该项目将 Requests(请求) 和 BeautifulSoup(解析) 两大 Python 爬虫常用库，封装成一个浏览器对象(StatefulBrowser)，将上面说的两步并成一步。后面仅需一个浏览器对象，就可以完成请求页面、过滤内容、提交表单、跳转地址等操作，使得代码更加简单、操作更加方便。又因为它不依赖浏览器进程，所以相较于 Selenium 它更加轻巧，但缺点是不支持 JS 动态渲染的页面。
```python
import re
import mechanicalsoup

# Connect to Google
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com/")

# Fill-in the form
browser.select_form('form[action="/search"]')
browser["q"] = "MechanicalSoup"
# Note: the button name is btnK in the content served to actual
# browsers, but btnG for bots.
browser.submit_selected(btnName="btnG")

# Display links
for link in browser.links():
    target = link.attrs['href']
    # Filter-out unrelated links and extract actual URL from Google's
    # click-tracking.
    if (target.startswith('/url?') and not
            target.startswith("/url?q=http://webcache.googleusercontent.com")):
        target = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", target)
        print(target)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/20180433.png' style="max-width:80%; max-height=80%;"></img></p>

30、[orange3](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/biolab/orange3)：互动式数据分析桌面工具。一款面向不会编程人群的数据挖掘和数据可视化工具箱。内置多种图表类型、支持可视化编程，无需写代码即可做出简单、实用的数据分析软件，多用于教学和实验室等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/8357227.png' style="max-width:80%; max-height=80%;"></img></p>

31、[ydata-profiling](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ydataai/ydata-profiling)：能够自动生成 pandas DataFrame 分析报告的库。虽然 pandas 自带的 df.describe 函数可以方便地生成统计报告，但是信息较少。该项目能够自动生成一份 df 多维度的 HTML 分析报告，包含列的类型、缺失情况、数值分布、行重复率、占用内存大小等信息，有助于更好地了解数据情况。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/49346299.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
32、[pueue](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Nukesor/pueue)：命令行任务管理工具。一个处理 shell 命令队列的工具，支持后台执行、定时执行、任务并行、暂停任务、任务崩溃恢复等功能。但它只是一个命令行工具，不能当作任务队列来用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/41925963.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
33、[MiaoYan](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tw93/MiaoYan)：一款 macOS 上的 Markdown 编辑器。采用 Swift5 原生开发，适用于 macOS 的 Markdown 编辑器「妙言」。界面清爽好看，支持 PPT 模式、语法高亮、黑暗模式等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/253461233.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
34、[functional-programming-jargon](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hemanth/functional-programming-jargon)：函数式编程世界的行话。该项目希望通过介绍函数编程中的术语，让学习函数式编程变得容易些，示例代码均采用 JavaScript 编写。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/31168578.png' style="max-width:80%; max-height=80%;"></img></p>

35、[LxgwWenKai](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lxgw/LxgwWenKai)：适合正文阅读的开源中文字体。它是基于 FONTWORKS 出品的 Klee One 字体衍生品，并且针对简体中文做了增补和优化，字体效果惊艳、完全免费且支持商用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/334448316.png' style="max-width:80%; max-height=80%;"></img></p>

36、[MaaAssistantArknights](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MaaAssistantArknights/MaaAssistantArknights)：明日方舟游戏助手。基于图像识别技术，实现一键完成明日方舟游戏的全部日常任务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/384520418.png' style="max-width:80%; max-height=80%;"></img></p>

37、[opensnitch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/evilsocket/opensnitch)：一个 Linux 应用防火墙。它能够监视和控制应用的网络活动，相当于 Linux 版的 Little Snitch。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/88417028.png' style="max-width:80%; max-height=80%;"></img></p>

38、[Publii](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/GetPublii/Publii)：带 GUI 的静态网站生成工具。一款本地的静态网站 CMS 工具，有了它无需编程基础，即可通过图形化界面，轻松地创建个人博客、企业官网等，还支持一键发布到 GitHub Page、GitLab、Netlify 等网站。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/137733266.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
39、[dive-into-webpack](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gwuhaolin/dive-into-webpack)：《深入浅出 Webpack》。一本系统讲解 Webpack 的书，内容涵盖了 Webpack 的入门、配置、实战、优化以及原理。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/110203554.png' style="max-width:80%; max-height=80%;"></img></p>

40、[interviews.ai](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/BoltzmannEntropy/interviews.ai)：《深度学习面试》。书中包含了数百个人工智能领域面试时会遇到的问题(PRB)和解答(SOL)，作者希望可以借此帮助研究生/求职者，通过机器学习方面的面试。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/412151953.png' style="max-width:80%; max-height=80%;"></img></p>

### 机器学习
41、[flair](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/flairNLP/flair)：简单易用的 NLP 框架。基于 PyTorch 的 NLP 框架，支持文本命名实体识别(NER)、词性标注(PoS)、词义消歧和分类。项目中包含详细的使用教程，介绍了如何标记文本、训练语言模型等。
```python
from flair.data import Sentence
from flair.models import SequenceTagger

# make a sentence
sentence = Sentence('I love Berlin .')

# load the NER tagger
tagger = SequenceTagger.load('ner')

# run NER over sentence
tagger.predict(sentence)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/136914524.png' style="max-width:80%; max-height=80%;"></img></p>

42、[paper-reading](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mli/paper-reading)：深度学习论文精读集合。李沐发起的深度学习领域经典、最新论文精读视频集合。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/419991646.png' style="max-width:80%; max-height=80%;"></img></p>

43、[paper2gui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Baiyuetribe/paper2gui)：面向非编程人员的 AI 应用工具箱。该项目提供了多款免安装下载即用的 AI 工具，功能涵盖语音合成、视频补帧、图像风格转化、目标检测、OCR 识别等方面，让编程小白也能轻松拥有 AI “魔法”。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/76/415489170.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub75.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub77.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/76'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
