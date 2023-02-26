# 《HelloGitHub》第 72 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/72) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[hashcat](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hashcat/hashcat)：一款强大的密码恢复工具。破解速度超快支持多种算法，适用于 Linux、macOS 和 Windows 操作系统
```
安装：brew install hashcat
常用参数：
-a  指定破解模式：“-a 0”字典攻击，“-a 1” 组合攻击；“-a 3”掩码攻击
-m  指定要破解的 hash 类型：默认为 MD5
--force 忽略破解过程中的警告

常用破解模式：
0：Straight（字典破解）
1：Combination（组合破解）
3：Brute-force（掩码暴力破解）
6：Hybrid Wordlist + Mask（字典+掩码破解）
7：Hybrid Mask + Wordlist（掩码+字典破解）

常用掩码设置：
l：纯小写字母 abcdefghijklmnopqrstuvwxyz
u：纯大写字母 ABCDEFGHIJKLMNOPQRSTUVWXYZ
d：纯数字 0123456789

举例：破解 8 位数字密码
hashcat -a 3 -m 0 --force 0D7002A70CCDE8BF4BA2A4A5572A85E9(密码md5字符串) ?l?l?l?l?l?l?l?l?l?l?l（11 位密码的掩码）
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/47409672.png' style="max-width:80%; max-height=80%;"></img></p>

2、[reptyr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nelhage/reptyr)：能够把旧终端运行中的程序，迁移到新终端窗口的实用工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/1252864.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[Monitorian](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/emoacht/Monitorian)：轻松调节多个显示器亮度的 Windows 桌面工具。操作界面支持中文，使用时显示器需要开启 DDC/CI


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/79386660.png' style="max-width:80%; max-height=80%;"></img></p>

4、[PluginCore](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yiyungent/PluginCore)：适用于 ASP.NET Core 的轻量级插件框架。开箱即用自带插件管理 Web 界面
```csharp
public void ConfigureServices(IServiceCollection services)
{
    // ...
    // 1. Add PluginCore
    services.AddPluginCore();
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...
    // 2. Use PluginCore
    app.UsePluginCore();
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/393686145.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[coost](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/idealvin/coost)：在 C++ 上实现类似 Go goroutine 的库。它实现了协程同步事件、协程锁、协程池、channel、waitgroup，内存占用少实测 1000 万协程占用 2.8G 内存
```c++
#include "co/co.h"

DEF_main(argc, argv) {
    co::Chan<int> ch;
    go([ch]() { /* capture by value, rather than reference */
        ch << 7;
    });

    int v = 0;
    ch >> v;
    LOG << "v: " << v;

    return 0;
}
```


### CSS 项目
6、[log](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/adamschwartz/log)：浏览器 console.log  风格的 CSS 库。[查看效果](https://adamschwartz.co/log/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/9401692.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
7、[gota](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/go-gota/gota)：Go 语言的数据处理库。该库提供了类似 Python 语言 Pandas 库的功能，以及 Series 和 DataFrames 的数据结构，支持用列的方式高效地处理数据
```go
type User struct {
    Name     string
    Age      int
    Accuracy float64
}
users := []User{
    {"Aram", 17, 0.2},
    {"Juan", 18, 0.8},
    {"Ana", 22, 0.5},
}
df := dataframe.LoadStructs(users)
fmt.Println(df)

// Output:
// [3x3] DataFrame
//
//     Name     Age   Accuracy
//  0: Aram     17    0.200000
//  1: Juan     18    0.800000
//  2: Ana      22    0.500000
//     <string> <int> <float>
```


8、[gse](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/go-ego/gse)：Go 的高性能多语言分词库。它是结巴分词的 Go 语言实现，支持中文和接入 ES 等功能
```go
text  = "《复仇者联盟3：无限战争》是全片使用IMAX摄影机拍摄制作的的科幻片."
// use DAG and HMM
hmm := seg.Cut(text, true)
fmt.Println("cut use hmm: ", hmm)
// cut use hmm:  [《复仇者联盟3：无限战争》 是 全片 使用 imax 摄影机 拍摄 制作 的 的 科幻片 .]
```


9、[hh-lol-prophet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/real-web-world/hh-lol-prophet)：英雄联盟对局先知工具。免费合法不封号，原理是基于 LOL 客户端接口获取用户数据，实现开局前对玩家信息分析和打分


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/460053762.png' style="max-width:80%; max-height=80%;"></img></p>

10、[illustrated-tls12](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/syncsynchalt/illustrated-tls12)：图解 TLS 连接。用在线交互的方式讲解 TLS 的全过程，从建立 TLS 1.2 客户端发送 ping 再到接收 pong，详细到每一个字节。[在线尝试](https://tls.ulfheim.net/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/151671321.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
11、[LSPosed](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/LSPosed/LSPosed)：运行于 Android 操作系统的钩子框架。支持 Android 8 以上，能够拦截几乎所有 Java 函数的调用，从而可被用来修改 Android 系统和软件的功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/320785435.png' style="max-width:80%; max-height=80%;"></img></p>

12、[supertokens-core](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/supertokens/supertokens-core)：开源的身份验证方案。为你的应用轻松增加登录、会话管理等功能，支持自行搭建服务。可用作 Auth0 的开源替代品


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/231921809.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
13、[chameleon](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/didi/chameleon)：一端所见即多端所见。适应不同环境的跨端整体解决方案，支持 Web、小程序、快应用 等平台


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/166419150.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[charts](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/frappe/charts)：简单、零依赖、响应式的 SVG 图表库
```javascript
const data = {
    labels: ["12am-3am", "3am-6pm", "6am-9am", "9am-12am",
        "12pm-3pm", "3pm-6pm", "6pm-9pm", "9am-12am"
    ],
    datasets: [
        {
            name: "Some Data", chartType: "bar",
            values: [25, 40, 30, 35, 8, 52, 17, -4]
        },
        ...
]}

const chart = new frappe.Chart("#chart", 
{   // or a DOM element,
    // new Chart() in case of ES6 module with above usage
    title: "My Awesome Chart",
    data: data,
    type: 'axis-mixed', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
    height: 250,
    colors: ['#7cd6fd', '#743ee2']
})
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/108395495.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[lax.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alexfoxy/lax.js)：用于滚动时创建平滑和好看动画的库。简单轻量仅 4KB 大小，但功能齐全且灵活
```html
<!-- JS -->
<script>
  window.onload = function () {
    lax.init()

    // Add a driver that we use to control our animations
    lax.addDriver('scrollY', function () {
      return window.scrollY
    })

    // Add animation bindings to elements
    lax.addElements('.selector', {
      scrollY: {
        translateX: [
          ["elInY", "elCenterY", "elOutY"],
          [0, 'screenWidth/2', 'screenWidth'],
        ]
      }
    })
  }
</script>

<!-- HTML -->
<div class="selector">Hello</div>
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/175176201.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[reveal.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hakimel/reveal.js)：一款 HTML 演示框架。让你摆脱传统死板的 PPT 制作方法，可以方便地使用 HTML、Markdown 语言制作 PPT


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/1861458.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[tinykeys](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jamiebuilds/tinykeys)：极小的键盘事件监听库
```javascript
import tinykeys from "tinykeys"

tinykeys(window, {
  "Shift+D": () => {
    alert("The 'Shift' and 'd' keys were pressed at the same time")
  },
  "y e e t": () => {
    alert("The keys 'y', 'e', 'e', and 't' were pressed in order")
  },
  "$mod+KeyD": () => {
    alert("Either 'Control+d' or 'Meta+d' were pressed")
  },
})
```


### Kotlin 项目
18、[compose-tetris](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vitaviva/compose-tetris)：基于 Jetpack Compose 的俄罗斯方块游戏


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/354306491.gif' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C 项目
19、[HBDNavigationBar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/listenzz/HBDNavigationBar)：自定义 UINavigationBar 的组件，用于各种状态之间平滑切换


### Python 项目
20、[pokete](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lxgr-linux/pokete)：运行在终端里的口袋妖怪类游戏。虽然游戏图像采用简单的 ASCII 码构建，但商店、小精灵、对战等功能一应俱全
```
运行方法：
# pip install scrap_engine
$ git clone https://github.com/lxgr-linux/pokete.git
$ ./pokete/pokete.py
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/331361562.png' style="max-width:80%; max-height=80%;"></img></p>

21、[rembg](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/danielgatis/rembg)：简单实用的删除图像背景/抠图工具
```python
from rembg import remove
from PIL import Image

input_path = 'input.png'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/286500101.png' style="max-width:80%; max-height=80%;"></img></p>

22、[saleor](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/saleor/saleor)：用 Python 开发的电商平台。采用 Django+GraphQL API+React 构建，功能丰富支持移动端、订单、商品、用户管理等。[在线体验](https://demo.saleor.io/dashboard)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/8162715.png' style="max-width:80%; max-height=80%;"></img></p>

23、[textdistance](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/life4/textdistance)：计算文本距离的常用算法库。包含计算文本相似度、多样性、编辑距离、压缩等多种算法，所有算法均采用 Python 实现，容易理解调用方便
```python
import textdistance
textdistance.hamming.normalized_similarity('test', 'text')
# 相似度为 0.75
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/90356012.png' style="max-width:80%; max-height=80%;"></img></p>

24、[tiptop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nschloe/tiptop)：炫酷的命令行系统监控工具
```
安装：pip install tiptop
运行：tiptop
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/409999750.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
25、[OnlySwitch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jacklandrin/OnlySwitch)：免费开源的 macOS 状态栏一键设置工具。可以轻松对系统功能进行设置，如隐藏桌面图标、清理 Xcode 缓存、一键隐藏刘海儿、进入夜览模式等数十种功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/433619938.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
26、[blog_os](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/phil-opp/blog_os)：用 Rust 从零开发一个操作系统的教程。保姆级教程！从空文件夹开始，一步步搭建开发环境，通过原理描述、代码示例讲解操作系统背后的原理。硬要说缺点的话就是教程是英文的，但是配上代码示例读起来不是很费劲。[中文](https://os.phil-opp.com/zh-CN/)


27、[design-patterns-for-humans](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kamranahmedse/design-patterns-for-humans)：人人都能看懂的设计模式教程。[中文](https://github.com/guanguans/design-patterns-for-humans-cn)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/82227585.png' style="max-width:80%; max-height=80%;"></img></p>

28、[electerm](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/electerm/electerm)：一款支持 SSH/SFTP 的终端工具。支持中文和 Windows、Linux、macOS 操作系统


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/106087444.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[ElectronBot](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/peng-zhihui/ElectronBot)：自制桌面级小机器人。它具备 USB 通信显示画面功能以及 6 个自由度，支持手势识别和人体关键点检测。这里有配套的全部开发资料和 SDK，让你也可以制作出一个这样有趣的机器人


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/468685658.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[english-words](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dwyl/english-words)：大型英语单词文本。它是基于 WordNet 英语词汇数据库整理的文本文件，可用于英语自动提示、自动搜索等功能


31、[Learn-Vim](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/iggredible/Learn-Vim)：学习 Vim 的指南。该教程不是“大而全的百科全书”，它着重介绍了 Vim 中最常用的功能，让你可以快速熟悉和使用 Vim。[中文](https://github.com/wsdjeg/Learn-Vim_zh_cn)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/279310322.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
32、[Deep-Learning-with-TensorFlow-book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dragen1860/Deep-Learning-with-TensorFlow-book)：《TensorFlow 深度学习》


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/192155460.png' style="max-width:80%; max-height=80%;"></img></p>

33、[microfrontends](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/phodal/microfrontends)：《微前端的那些事儿》 将 Web 应用由单一的单体应用，转变为多个小型前端应用聚合为一的应用


### 机器学习
34、[awesome-automl-papers](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hibayesian/awesome-automl-papers)：汇集了自动机器学习（AutoML）相关的论文、文章、教程等资源的项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/111381431.jpeg' style="max-width:80%; max-height=80%;"></img></p>

35、[deep-learning-for-image-processing](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/WZMIAOMIAO/deep-learning-for-image-processing)：深度学习在图像处理方面的教程。该项目配以视频的方式介绍知识点和搭建方法，对应的 PTT 在 course_ppt 目录下


36、[jina](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jina-ai/jina)：一款易用的神经搜索框架。神经搜索是指用非结构化数据，搜索非结构化数据。Jina 简化了神经搜索系统的搭建流程，使开发者可以快速构建以图搜图、以文字搜图、问答机器人、照片去重、海量标签分类等应用
```python
from docarray import Document, DocumentArray
from jina import Executor, Flow, requests
class PreprocImg(Executor):
    @requests
    async def foo(self, docs: DocumentArray, **kwargs):
        for d in docs:
            (
                d.load_uri_to_image_tensor(200, 200)  # load
                .set_image_tensor_normalization()  # normalize color
                .set_image_tensor_channel_axis(
                    -1, 0
                )  # switch color axis for the PyTorch model later
            )
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/72/240315046.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub71.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub73.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/72'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
