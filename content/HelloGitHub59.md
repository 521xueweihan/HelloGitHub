# 《HelloGitHub》第 59 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/59) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[TIC-80](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nesbox/TIC-80)：复古游戏引擎模拟器。TIC-80 支持 Windows、Linux、Mac 等主流平台，通过它你可以运行多种复古小游戏，觉得没意思？它不仅可以玩游戏还可以制作游戏，支持多种编程语言，还有地图、声音编辑器等，就是一个回到过去的“神奇迷你电脑”


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/77920383.gif' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
2、[tilt-brush](https://hellogithub.com/periodical/statistics/click?target=https://github.com/googlevr/tilt-brush)：Google 开源的 VR 绘图工具。用它可以在虚拟三维空间中创作各种作品，支持主流的 VR 设备


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/255415824.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
3、[winmerge](https://hellogithub.com/periodical/statistics/click?target=https://github.com/WinMerge/winmerge)：一个用 C++ 编写的 Windows 比较和合并工具。它可以比较文件和文件夹，以直观的可视化格式来显示两者甚至三者之间的差异，操作简单


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/26494018.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
4、[bild](https://hellogithub.com/periodical/statistics/click?target=https://github.com/anthonynsimon/bild)：纯 Go 实现的多种图像处理算法库。示例代码：
```go
package main

import (
    "github.com/anthonynsimon/bild/effect"
    "github.com/anthonynsimon/bild/imgio"
    "github.com/anthonynsimon/bild/transform"
)

func main() {
    img, err := imgio.Open("input.jpg")
    if err != nil {
        fmt.Println(err)
        return
    }

    inverted := effect.Invert(img)
    resized := transform.Resize(inverted, 800, 800, transform.Linear)
    rotated := transform.Rotate(resized, 45, nil)

    if err := imgio.Save("output.png", rotated, imgio.PNGEncoder()); err != nil {
        fmt.Println(err)
        return
    }
}
```


5、[darwinkit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/progrium/darwinkit)：封装 Apple/Mac 接口的 Go 库。用它仅在 80 行代码内就能写出个 macOS 菜单栏「番茄时钟」应用，[查看源码](https://github.com/progrium/macdriver/blob/main/examples/pomodoro/main.go#L1)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/309781884.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[gin-vue-admin](https://hellogithub.com/periodical/statistics/click?target=https://github.com/flipped-aurora/gin-vue-admin)：一个基于 Gin+Vue 实现的后台管理系统。看项目名字就知道它为什么而生！该项目的作者还做了配套的免费教学视频，找 Go 实战项目的同学可以学起来了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/205679232.png' style="max-width:80%; max-height=80%;"></img></p>

7、[pyroscope](https://hellogithub.com/periodical/statistics/click?target=https://github.com/grafana/pyroscope)：基于 Go 的开源实时性能分析平台。仅需在源码中添加几行代码，pyroscope 就能帮你找出代码的性能问题、CPU 使用过高的原因，还有丰富的图表和调用树展示。支持 Go、Python、Ruby 编程语言，[中文说明](https://github.com/pyroscope-io/pyroscope/blob/main/translations/README.ch.md)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/325724738.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
8、[dbeaver](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dbeaver/dbeaver)：支持主流数据库的桌面管理工具。一款用 Java 写的数据库管理工具，只要是 JDBC 支持的数据库它都支持。虽然分免费社区版和付费企业版，但是免费的功能其实已经够用啦


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/44662669.png' style="max-width:80%; max-height=80%;"></img></p>

9、[fizz-gateway-node](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fizzgate/fizz-gateway-node)：一个 Java 微服务网关。支持热服务编排、自动授权选择、在线测试、监控、管理后台等功能，帮助企业治理 API 服务降低重复代码投入，提高服务稳定性


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/291666391.png' style="max-width:80%; max-height=80%;"></img></p>

10、[jsoup](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jhy/jsoup)：抓取和解析 HTML 的 Java 库。可能很多人都知道这个库，我就不多说什么了。想知道上手有多快？看完示例代码你就算会用了
```java
Document doc = Jsoup.connect("https://en.wikipedia.org/").get();
log(doc.title());
Elements newsHeadlines = doc.select("#mp-itn b a");
for (Element headline : newsHeadlines) {
  log("%s\n\t%s", 
    headline.attr("title"), headline.absUrl("href"));
}
```


11、[Recaf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Col-E/Recaf)：Java 字节码编辑器。让你像写普通代码的一样编写 Java 字节码，如果不懂这方面的知识，先不要轻举妄动，可以去看看字节码的资料再回来把玩这个项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/98499283.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[Sa-Token](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dromara/Sa-Token)：一个轻量级 Java 权限认证框架。它上手简单易于扩展，可以快速解决：登录认证、权限认证、Session 会话等一系列权限相关问题。示例代码：
```java
// 在登录时写入当前会话的账号 ID 
StpUtil.setLoginId(10001);	

// 然后在任意需要校验登录处调用以下 API：如果当前会话未登录
// 这句代码会抛出 `NotLoginException` 异常
StpUtil.checkLogin();	

// 还有以下功能
StpUtil.logoutByLoginId(10001);     // 让账号为 10001 的会话注销登录（踢人下线）
StpUtil.hasRole("super-admin");     // 查询当前账号是否含有指定角色标识, 返回 true 或 false
StpUtil.setLoginId(10001, "PC");        // 指定设备标识登录
StpUtil.logoutByLoginId(10001, "PC");   // 指定设备标识进行强制注销 (不同端不受影响)
StpUtil.switchTo(10044);                // 将当前会话身份临时切换为其它账号
```


### JavaScript 项目
13、[folio-2019](https://hellogithub.com/periodical/statistics/click?target=https://github.com/brunosimon/folio-2019)：一个开源的 3D 博客项目。这个博客我点进去后就惊呆了，用户可通过操控一辆小汽车选择要阅读的文章，过程中还有汽车的声音和砖块碰撞的效果等，特别炫酷！快去体验下吧！[点击尝试](https://bruno-simon.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/196761128.png' style="max-width:80%; max-height=80%;"></img></p>

14、[instant.page](https://hellogithub.com/periodical/statistics/click?target=https://github.com/instantpage/instant.page)：通过预加载，提高网页加载速度的 JavaScript 库。它支持移动端和 PC 端，在 PC 端时当鼠标悬浮在链接上和在移动端时链接可见后立即预加载，从而降低点击后网页的加载时间。复制 HTML 代码片段加到网页上即可生效
```html
<script src="//instant.page/5.1.0" type="module" integrity="sha384-by67kQnR+pyfy8yWP4kPO12fHKRLHZPfEsiSXR8u2IKcTdxD805MGUXBzVPnkLHw"></script>
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/169606323.png' style="max-width:80%; max-height=80%;"></img></p>

15、[majestic](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Raathigesh/majestic)：美观且便捷的 JavaScript 测试框架 Jest 的图形界面工具。遵循“不写测试的项目，不是好项目”的原则，测试是一定要写的。如果有一个赏心悦目的测试运行界面，应该能略微减轻写单元测试时，痛苦的心情吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/112321084.png' style="max-width:80%; max-height=80%;"></img></p>

16、[monitor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/clouDr-f2e/monitor)：收集页面上的用户行为和报错信息的轻量级前端库。我问了下项目维护者，信息展示平台和后端服务还未开源，还需要等公司定开源协议。那就先看下前端的功能吧：
- 请求错误和代码报错上传
- 收集用户点击、跳转行为
- 支持 React、Vue、微信小程序


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/281088983.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[node-jvm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/YaroslavGaponov/node-jvm)：用 Node.js 实现 JVM 的项目。代码简洁易懂，而且 examples 目录下有运行 Java 代码的例子和所需文件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/13502197.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
18、[actionview](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lxerxa/actionview)：一个类 Jira 的开源问题需求跟踪平台。前端基于 React＋Redux 后端采用 PHP 的 Laravel 框架实现


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/64629613.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
19、[alive-progress](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rsalmei/alive-progress)：新！Python 炫酷进度条项目。支持 Python2.7-3.8 示例代码：
```python
# 安装：pip install alive-progress
from alive_progress import alive_bar

with alive_bar(total) as bar:  # declare your expected total
    for item in items:         # iterate as usual over your items
        ...                    # process each item
        bar()                  # call after consuming one item
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/200590949.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[blind_watermark](https://hellogithub.com/periodical/statistics/click?target=https://github.com/guofei9987/blind_watermark)：给图片加盲水印的 Python 库。盲水印就是图片有水印但人眼看不出来，需要通过程序才能提取水印，相当于隐形“盖章”，可以用在数据泄露溯源、版权保护等场景。该库出自阿里巴巴安全团队，强大之处：
- 解析水印图时无需原图
- 水印图剪裁、旋转都不会破坏图中的盲水印
- 支持密码加密
```python
from blind_watermark import WaterMark

bwm_obj = WaterMark(password_wm=1, password_img=1)
# 原图
bwm_obj.read_img('pic/原图.jpg')
# 水印图
bwm_obj.read_wm('pic/水印.png')
# 打水印后的图
bwm_obj.embed('output/结果.png')
# 注意需要设定水印的长宽 wm_shape
bwm_objextract(filename='output/结果.png', wm_shape=(120, 120), out_wm_name='output/解出的水印.png', )
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/197206410.png' style="max-width:80%; max-height=80%;"></img></p>

21、[PyG2Plot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hustcc/PyG2Plot)：基于 G2Plot 封装的 Python3 可视化库。G2Plot 是蚂蚁集团开源的一个基于图表分类学的可视分析图表库，内置 25+ 常见图表类型。该库是 Python 对 G2Plot 的封装，体验良好，开箱即用
```python
from pyg2plot import Plot

line = Plot("Line")

line.set_options({
  "height": 400, # set a default height in jupyter preview
  "data": [
    { "year": "1991", "value": 3 },
    { "year": "1992", "value": 4 },
    { "year": "1993", "value": 3.5 },
    { "year": "1994", "value": 5 },
    { "year": "1995", "value": 4.9 },
    { "year": "1996", "value": 6 },
    { "year": "1997", "value": 7 },
    { "year": "1998", "value": 9 },
    { "year": "1999", "value": 13 },
  ],
  "xField": "year",
  "yField": "value",
})

line.render_notebook()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/329159574.png' style="max-width:80%; max-height=80%;"></img></p>

22、[requests-html](https://hellogithub.com/periodical/statistics/click?target=https://github.com/psf/requests-html)：好用的 Python 解析 HTML 库。写爬虫的小伙伴都感受过解析 HTML 的痛苦，常用工具 BeautifulSoup、lxml、Scrapy 的 selector 等。今天你有了新的选择 requests-html，支持 XPath、CSS 选择器、动态页面、过滤指定内容等。上手特别简单和迅速，我的爬虫项目 [Hydra](https://github.com/HelloGitHub-Team/Hydra) 中就用了它，解析 HTML 变得轻松了许多。下面是我觉得好用的函数示例：
```python
# 找出元素下的所有链接
about.absolute_links
{'http://brochure.getpython.info/', 'https://www.python.org/about/quotes/', 'https://www.python.org/about/help/'}
# 匹配内容
>>> r.html.search('Python is a {} language')[0]
programming
# 直接提取属性的值
>>> about.attrs
{'id': 'about', 'class': ('tier-1', 'element-1'), 'aria-haspopup': 'true'}
# 呈现加载 JS 后的动态内容
r.html.render()
```


23、[vcrpy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kevin1024/vcrpy)：把 HTTP 的请求拦截下来，返回本地准备好的数据的库。就像“插卡”一样，使用装饰器方式修饰的函数会被拦截下来，直接返回指定本地路径的文件中的数据，从而提高测试执行速度和确定性
```python
@vcr.use_cassette('fixtures/vcr_cassettes/synopsis.yaml')
def test_iana():
    response = urllib2.urlopen('http://www.iana.org/domains/reserved').read()
    assert 'Example domains' in response
```


### Swift 项目
24、[Maccy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/p0deje/Maccy)：适用于 macOS 的轻量级剪贴板管理工具。支持复制内容的历史记录、快速搜索、快捷键选择等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/119637215.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[SQLite.swift](https://hellogithub.com/periodical/statistics/click?target=https://github.com/stephencelis/SQLite.swift)：纯 Swift 实现的轻量级 SQLite3 数据库框架。采用链式编程的写法，让数据库的管理变得优雅。代码容易理解，即使你不会 SQL 语句，也可以轻松查询数据库
```swift
import SQLite

let db = try Connection("path/to/db.sqlite3")

let users = Table("users")
let id = Expression<Int64>("id")
let name = Expression<String?>("name")
let email = Expression<String>("email")

try db.run(users.create { t in
    t.column(id, primaryKey: true)
    t.column(name)
    t.column(email, unique: true)
})

// CREATE TABLE "users" (
//     "id" INTEGER PRIMARY KEY NOT NULL,
//     "name" TEXT,
//     "email" TEXT NOT NULL UNIQUE
// )
```


### 人工智能
26、[avatarify-python](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alievk/avatarify-python)：视频会议实时换脸工具。利用机器学习训练的模型，通过捕捉人脸动作并与图片相结合进行实时渲染的方式，达到实时换脸的效果。支持 OBS、Zoom、Skype、Teams、Slack 等直播和会议软件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/253601257.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
27、[AndroidSDK](https://hellogithub.com/periodical/statistics/click?target=https://github.com/thyrlian/AndroidSDK)：包含完整 Android SDK 运行环境的 Docker 镜像。适用于各种 Android 持续集成场景，甚至包括模拟器运行应用、界面自动化测试，也可以连接云端进行自动化测试。Android 构建的容器镜像解决方案之一（不违法许可协议的方案），并在 Docker 官方的 DockerCon EU 2017 进行过宣讲


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/64508433.jpeg' style="max-width:80%; max-height=80%;"></img></p>

28、[awesome-macos-command-line](https://hellogithub.com/periodical/statistics/click?target=https://github.com/herrbischoff/awesome-macos-command-line)：针对 macOS 系统做一些“酷”事情的 shell 命令集合。有些一条命令能解决的问题，就不需要点来点去，找来找去了


29、[coding-fonts](https://hellogithub.com/periodical/statistics/click?target=https://github.com/CSS-Tricks/coding-fonts)：极简的编程字体介绍和展示网站。[在线尝试](https://coding-fonts.css-tricks.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/298681464.png' style="max-width:80%; max-height=80%;"></img></p>

30、[computer-science](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ossu/computer-science)：开源社区大学，计算机科学自学的免费材料集合仓库。该项目不仅包含了学习的视频，还有学习计划和时间安排，同时这些课程大多来自国际知名大学。唯一不足的点是材料都是英文的，我想了想还是决定推荐给大家，毕竟学好英语也是编程路上必经之路


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/19415064.png' style="max-width:80%; max-height=80%;"></img></p>

31、[data-engineer-roadmap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/datastacktv/data-engineer-roadmap)：数据工程师学习路径图


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/292293462.png' style="max-width:80%; max-height=80%;"></img></p>

32、[docker-curriculum](https://hellogithub.com/periodical/statistics/click?target=https://github.com/prakhar1989/docker-curriculum)：专为新手准备的 Docker 教程。[在线阅读](https://docker-curriculum.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/47304932.png' style="max-width:80%; max-height=80%;"></img></p>

33、[github1s](https://hellogithub.com/periodical/statistics/click?target=https://github.com/conwnet/github1s)：通过 VS Code 在线快速阅读 GitHub 项目代码的工具。你是否烦心过 GitHub 的访问速度和项目 clone 速度，在项目地址 github 后面加上 1s，即可在线阅读代码无需等待


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/192175095.gif' style="max-width:80%; max-height=80%;"></img></p>

34、[qwerty-learner](https://hellogithub.com/periodical/statistics/click?target=https://github.com/RealKai42/qwerty-learner)：好用有趣的打字记单词的在线网站。很多人直观地觉得能扣篮的人打球好，打字快的人编程厉害。如此说来，多用这个项目不仅可以背单词，还有助于提高编程能力呢


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/59/331603334.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub58.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub60.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/59'>这里</a>。
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
