# 《HelloGitHub》第 89 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/89) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[barco](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lucavallin/barco)：用 C 语言从头写一个 Linux 容器。该项目仅依赖底层的 Linux 功能，用 C 语言实现的一个 Linux 容器，可用来了解更多关于 Linux 容器和内核的技术细节。
```
$ sudo ./bin/barco -u 0 -m / -c /bin/sh -a . [-v]

22:08:41 INFO  ./src/barco.c:96: initializing socket pair...
22:08:41 INFO  ./src/barco.c:103: setting socket flags...
22:08:41 INFO  ./src/barco.c:112: initializing container stack...
22:08:41 INFO  ./src/barco.c:120: initializing container...
22:08:41 INFO  ./src/barco.c:131: initializing cgroups...
22:08:41 INFO  ./src/cgroups.c:73: setting memory.max to 1G...
22:08:41 INFO  ./src/cgroups.c:73: setting cpu.weight to 256...
22:08:41 INFO  ./src/cgroups.c:73: setting pids.max to 64...
22:08:41 INFO  ./src/cgroups.c:73: setting cgroup.procs to 1458...
22:08:41 INFO  ./src/barco.c:139: configuring user namespace...
22:08:41 INFO  ./src/barco.c:147: waiting for container to exit...
22:08:41 INFO  ./src/container.c:43: ### BARCONTAINER STARTING - type 'exit' to quit ###

# ls
bin         home                lib32       media       root        sys         vmlinuz
boot        initrd.img          lib64       mnt         run         tmp         vmlinuz.old
dev         initrd.img.old      libx32      opt         sbin        usr
etc         lib                 lost+found  proc        srv         var
# echo "i am a container"
i am a container
```

2、[quake2-rerelease-dll](https://hellogithub.com/periodical/statistics/click?target=https://github.com/id-Software/quake2-rerelease-dll)：《雷神之锤 2》官方重制版源码。《雷神之锤 2》是 id Software 在 1997 年发布的一款第一人称射击游戏，被许多玩家视为经典。该项目是官方 2023 年重新发布的 《雷神之锤 2》游戏源码。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/675738701.jpg' style="max-width:80%; max-height=80%;"></img></p>

3、[trurl](https://hellogithub.com/periodical/statistics/click?target=https://github.com/curl/trurl)：解析和操作 URL 的命令行工具。该项目是 cURL 作者的新作，可用来解析 URL、替换/提取/设置 URL 中的参数。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/621725724.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
4、[GeekDesk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BookerLiu/GeekDesk)：小巧的 Windows 桌面启动工具。这款名为极客桌面的免费工具，拥有极简的界面，支持搜索全盘文件、一键呼出、自定义壁纸、定时提醒等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/357072316.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[Starward](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Scighost/Starward)：一款开源的 miHoYo 游戏启动器。这是一款支持米哈游旗下所有桌面端游戏的启动器，支持下载游戏、记录游戏时间、切换账号、保存抽卡记录、米游社工具箱等功能，可运行在 Windows 10 及以上的操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/636565625.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
6、[implot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/epezent/implot)：实时绘图的 GUI 库。该项目可根据用户交互和数据更新，实时更新图像的 Dear ImGui 绘图库，支持 GPU 加速、多种绘图类型、混合绘图等功能。仅需少量的代码，就能集成实时数据可视化的功能。
```
int   bar_data[11] = ...;
float x_data[1000] = ...;
float y_data[1000] = ...;

ImGui::Begin("My Window");
if (ImPlot::BeginPlot("My Plot")) {
    ImPlot::PlotBars("My Bar Plot", bar_data, 11);
    ImPlot::PlotLine("My Line Plot", x_data, y_data, 1000);
    ...
    ImPlot::EndPlot();
}
ImGui::End();
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/257596449.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[wslg](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/wslg)：在 Windows 上运行 Linux 图形化应用的工具。该项目是微软开源的支持在 Windows 操作系统上，运行 Linux GUI 应用的工具。提供了原生和自然的 Linux GUI 应用使用体验，比如跨 Windows 和 Linux 应用的剪切粘贴等功能。WSLg 已内置在 Windows 10 及以上的系统中，可直接通过 wsl 命令启动。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/346871538.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
8、[etree](https://hellogithub.com/periodical/statistics/click?target=https://github.com/beevik/etree)：更好用的轻量级 Go 语言 XML 库。虽然 Go 语言内置了处理 XML 的库，但在使用时必须按照嵌套层级定义结构体非常繁琐。这个项目的设计灵感来源于 Python 语言的  ElementTree 库，可以在无需定义结构体的情况下灵活的读取、生成 XML 文档。来自 [@两双筷子sqldc](https://hellogithub.com/user/5dGtvaZ6H3L4QMY) 的分享
```go
doc := etree.NewDocument()
doc.CreateProcInst("xml", `version="1.0" encoding="UTF-8"`)
doc.CreateProcInst("xml-stylesheet", `type="text/xsl" href="style.xsl"`)

people := doc.CreateElement("People")
people.CreateComment("These are all known people")

jon := people.CreateElement("Person")
jon.CreateAttr("name", "Jon")

sally := people.CreateElement("Person")
sally.CreateAttr("name", "Sally")

doc.Indent(2)
doc.WriteTo(os.Stdout)
```

9、[golang-design-pattern](https://hellogithub.com/periodical/statistics/click?target=https://github.com/senghoo/golang-design-pattern)：Go 语言设计模式的实例代码。该项目是作者阅读《研磨设计模式》一书的读书笔记，并用 Go 语言实现了书中涉及的 23 个设计模式。

10、[ls-lint](https://hellogithub.com/periodical/statistics/click?target=https://github.com/loeffel-io/ls-lint)：检查目录和文件命名风格的工具。这是一款 Go 编写的目录和文件名 Lint 工具，它依赖少、速度快，可通过 yml 配置文件自定义检测规则和忽略目录，适用于 Git Hooks、GitHub Action、Docker Image 等多种场景。
```
ls:
  .js: snake_case
  .ts: snake_case | camelCase
  .d.ts: PascalCase
  .html: regex:[a-z0-9]+

ignore:
  - node_modules
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/240896563.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[webp_server_go](https://hellogithub.com/periodical/statistics/click?target=https://github.com/webp-sh/webp_server_go)：一款开箱即用的 WebP 服务器。WebP 是谷歌开发的一种为了提升图像加载速度的图片格式，该项目是用 Go 写的 WebP 服务，无需二次开发就能实现将 JPG、PNG、BMP、SVG 等格式的图片，转化成 WebP 格式的服务，能够有效地减小图片体积、节省带宽、提升图片加载速度。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/239239351.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[Jailer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Wisser/Jailer)：一款强大的数据库提取数据工具。用于数据库子集和关系数据浏览的工具，支持按照表之间关系浏览数据库、生成 DML 拓扑关系等功能。可用来从生产数据库中提取出，支持测试一条完整业务线所需的数据库表和数据。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/1923665.png' style="max-width:80%; max-height=80%;"></img></p>

13、[OneAccount](https://hellogithub.com/periodical/statistics/click?target=https://github.com/LouBii/OneAccount)：一款简约的 Android 记账应用。这是一款支持自定义支出/收入分类、定时提醒、预算设置、花费统计等功能的记账 APP。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/148282280.jpg' style="max-width:80%; max-height=80%;"></img></p>

14、[triplea](https://hellogithub.com/periodical/statistics/click?target=https://github.com/triplea-game/triplea)：一款 Java 的回合制战争游戏。这是一款免费、开源的战争棋盘类游戏，玩家可以在游戏中模拟第二次世界大战、拿破仑战争等经典战役，支持 Windows、Linux 和 macOS 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/39766308.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
15、[biomes-game](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ill-inc/biomes-game)：一款开源沙盒 MMORPG 游戏。这是由已被 OpenAI 收购的 Global Illumination 公司，采用 React+Next.js+TypeScript 和 WebAssembly 等技术，构建的大型多人在线角色扮演游戏。玩家可以在游戏里探索世界、建造房子、交易、社交等，无需下载打开浏览器就可以玩。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/677467268.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[docsify](https://hellogithub.com/periodical/statistics/click?target=https://github.com/docsifyjs/docsify)：开箱即用的文档网站生成器。该项目可以帮你快速生成文档网站，开箱即用无需构建，写完文档即可发布。支持全文搜索、自定义主题、丰富的 API、Emoji 等实用功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/74260508.png' style="max-width:80%; max-height=80%;"></img></p>

17、[poster-design](https://hellogithub.com/periodical/statistics/click?target=https://github.com/palxiao/poster-design)：一款强大的在线设计图片工具。采用 Vue3+Vite2+Vuex+ElementPlus 技术实现的在线海报图片设计工具，可用于生成电商分享图、文章长图、视频/公众号封面等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/454264265.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[warriorjs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/olistic/warriorjs)：一个有趣的 JavaScript 编程 RPG 游戏。在游戏中你将通过 JavaScript 语法指挥战士与敌人战斗、营救俘虏，一步步走向塔顶，获得传说中的 JavaScript 之剑。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/34798315.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[WeHalo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sav7ng/WeHalo)：清爽的微信小程序版博客。该项目是基于 Halo 博客后端的微信小程序，可以轻松地将博客内容搬到微信小程序上，支持个人名片、博文展示、评论、搜索文章、自定义导航栏等功能。来自 [@umail.com](https://hellogithub.com/user/a0L3Omilqk8zNQY) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/158522838.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
20、[DrissionPage](https://hellogithub.com/periodical/statistics/click?target=https://github.com/g1879/DrissionPage)：类似 selenuium 的网页自动化工具。这是一个基于 Python 的网页自动化工具，支持 Chromium 内核浏览器。它将控制浏览器和收发请求两大功能合二为一，并提供了统一、简洁的接口。来自 [@马小六](https://hellogithub.com/user/MdXgAyzJSFbTeHh) 的分享
```python
# 下载星巴克产品图
from DrissionPage import SessionPage
from re import search

# 以s模式创建页面对象
page = SessionPage()
# 访问目标网页
page.get('https://www.starbucks.com.cn/menu/')

# 获取所有class属性为preview circle的元素
divs = page.eles('.preview circle')
# 遍历这些元素
for div in divs:
    # 用相对定位获取当前div元素后一个兄弟元素，并获取其文本
    name = div.next().text

    # 在div元素的style属性中提取图片网址并进行拼接
    img_url = div.attr('style')
    img_url = search(r'"(.*)"', img_url).group(1)
    img_url = f'https://www.starbucks.com.cn{img_url}'

    # 执行下载
    page.download(img_url, r'.\imgs', rename=name)
```

21、[learndb-py](https://hellogithub.com/periodical/statistics/click?target=https://github.com/spandanb/learndb-py)：从头用 Python 写一个数据库。该项目是用 Python 从零实现一个关系型数据库，从而更好地了解数据的内部构造，此数据库仅可作为学习和练手项目，无法应用在生产环境。

22、[nvitop](https://hellogithub.com/periodical/statistics/click?target=https://github.com/XuehaiPan/nvitop)：用 top 命令的方式查看 NVIDIA GPU 和进程状态。这是一款 NVIDIA 设备和进程监控工具，拥有多彩高亮的界面，实时更新的进程和设备信息，支持过滤进程、鼠标控制、发送信号等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/332736941.png' style="max-width:80%; max-height=80%;"></img></p>

23、[upiano](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eliasdorneles/upiano)：运行在命令行里的电子琴。这是一个小型的电子琴命令行应用，它安装简单、运行方便，支持鼠标和键盘两种操作方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/98796916.png' style="max-width:80%; max-height=80%;"></img></p>

24、[watchgha](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nedbat/watchgha)：在本地查看 GitHub Action 运行状态的工具。仅需一条命令就可以实时显示当前分支，在 GitHub Action 上运行状态的命令行工具。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/613355435.gif' style="max-width:80%; max-height=80%;"></img></p>

### Ruby 项目
25、[OpenFarm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/openfarmcc/OpenFarm)：一个教你如何种植农作物的网站。这是一个关于种植农作物的知识库，你可以在里面找到如何种植西红柿、土豆、草莓等植物的步骤，这一切都是免费的。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/13895958.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
26、[rjvm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/andreabergia/rjvm)：用 Rust 写一个迷你 JVM 的学习项目。这是一个用 Rust 写 JVM7 的练手项目，已实现 Java 基础类型、异常处理、堆栈跟踪、垃圾回收、解析 .class 文件等功能。

27、[starship](https://hellogithub.com/periodical/statistics/click?target=https://github.com/starship/starship)：轻量、速度超快的高颜值终端。这是一个 Rust 写的高颜值、适用于各种 Shell 的终端，它开箱即用，可定制各式各样的提示符，适用于 Windows、Linux、Android 和 macOS 系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/178991158.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
28、[Mist](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ninxsoft/Mist)：自动下载 macOS 系统固件的工具。这款工具可以列出所有可供下载的 macOS 固件/安装程序的信息，包括名称、版本号、发布日期和大小。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/509050256.png' style="max-width:80%; max-height=80%;"></img></p>

29、[SkeletonView](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Juanpe/SkeletonView)：一款优雅的 Swift 骨架屏库。骨架屏是在页面展示所需的数据还未加载完成时，先展示出页面大致结构的一项技术。这个 Swift 骨架屏库容易上手、接口友好，支持所有 UIView、自定义动画等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/109878485.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
30、[audiocraft](https://hellogithub.com/periodical/statistics/click?target=https://github.com/facebookresearch/audiocraft)：Meta 开源的文本生成音乐的库。该项目可根据文本提示词生成高质量、高保真的音频和音乐，比如吹着风吹口哨、一段适合海滩场景的流行舞曲，生成效果十分惊艳。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/650945129.png' style="max-width:80%; max-height=80%;"></img></p>

31、[Fooocus](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lllyasviel/Fooocus)：一款开箱即用的图片生成软件。该项目在设计时吸收了 Stable Diffusion 和 Midjourney 的优点，它安装简单、操作方便，省去了复杂的参数调节步骤。用户只需要输入提示词，就可以生成与 Midjourney 水平相当的图片。支持本地部署、离线使用，最低配置要求 8GB 内存和 4GB 的 Nvidia 显卡。来自 [@刘三非](https://hellogithub.com/user/VhrXCAs7cMxL08W) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/676676006.png' style="max-width:80%; max-height=80%;"></img></p>

32、[machine-learning-notes](https://hellogithub.com/periodical/statistics/click?target=https://github.com/roboticcam/machine-learning-notes)：徐亦达的机器学习课程。该项目是香港浸会大学（HKBU）徐亦达教授开源的关于机器学习、概率模型、深度学习的讲义和视频课程链接。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/121647248.jpg' style="max-width:80%; max-height=80%;"></img></p>

### 其它
33、[beepy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/beeper/beepy)：一款全键盘便携式的 Linux 计算机。这是一个结合了黑莓键盘、400*200 LCD 显示屏、2000mAh 电池的板子，售价 79 美元。插上树莓派 Zero W，立马变成了一个黑莓版的 Linux 游乐场。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/532730834.jpg' style="max-width:80%; max-height=80%;"></img></p>

34、[cloc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AlDanial/cloc)：计算代码行数的工具。这是一款可以统计源码中空白行、注释、不同编程语言代码行数的工具。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/42029482.png' style="max-width:80%; max-height=80%;"></img></p>

35、[How-To-Secure-A-Linux-Server](https://hellogithub.com/periodical/statistics/click?target=https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)：一份 Linux 服务器安全指南。这是一份专注于保护非企业场景下的 Linux 服务器安全的操作指南，它虽然不够专业但对于个人来说足够了。

36、[linux-tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dunwu/linux-tutorial)：一份实用的 Linux 教程。不同于大而全的 Linux 教程，该项目的内容主要侧重于实用性，内容包括 Linux 常用命令、Linux 系统运维、软件运维、常用 shell 脚本等。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

37、[weekly](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ljinkai/weekly)：独立开发产品变现周刊。关于独立开发者、产品变现相关内容的周刊。

### 开源书籍
38、[lean-side-bussiness](https://hellogithub.com/periodical/statistics/click?target=https://github.com/easychen/lean-side-bussiness)：《精益副业：程序员如何优雅地做副业》。该书扩展了《程序员如何优雅地挣零花钱》的内容，引入了精益创业流程，将其优化为副业专用精益副业流程，并增添了独立开发变现和网课变现实践的内容。

39、[putting-the-you-in-cpu](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hackclub/putting-the-you-in-cpu)：当你运行程序时发生了什么？这是一份关于程序是如何跑起来的迷你书，内容涉及计算机基础、操作系统、Linux 如何加载可执行文件等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/648351143.png' style="max-width:80%; max-height=80%;"></img></p>

40、[theByteBook](https://hellogithub.com/periodical/statistics/click?target=https://github.com/isno/theByteBook)：《深入架构原理与实践》。随着云计算的兴起，技术架构的关注点也从集群可用性治理，发展到云原生和 FinOps 成本管理。该书涵盖了网络、容器、网关、微服务与分布式、云原生、质量监测和成本管理方面的内容，帮助读者快速理清云时代下的技术架构体系。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/89/547677901.jpg' style="max-width:80%; max-height=80%;"></img></p>

41、[typescript-tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wangdoc/typescript-tutorial)：阮一峰的 TypeScript 教程。这是一份面向初学者的 TypeScript 开源教程，内容涵盖 TypeScript 的基本概念和用法。



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub88.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub90.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/89'>这里</a>。
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
