# 《HelloGitHub》第 57 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/57) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[ngx_waf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ADD-SP/ngx_waf)：一个 Nginx 防火墙模块。我差点就错过了的宝藏项目，它使用简单不需要复杂的配置，支持的功能直戳我的痛点。你看：
- 支持 IPV4、IPV6 和 IP 段黑白名单
- CC 防御即自动拉黑 IP 一段时间
- 支持 GET、POST、URL、Cookie 等黑名单（正则）


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/286048802.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
2、[fast-cpp-csv-parser](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ben-strasser/fast-cpp-csv-parser)：读取 CSV 文件的 C++ 库（仅头文件）。示例代码：
```c++
# include "csv.h"

int main(){
  io::CSVReader<3> in("ram.csv");
  in.read_header(io::ignore_extra_column, "vendor", "size", "speed");
  std::string vendor; int size; double speed;
  while(in.read_row(vendor, size, speed)){
    // 对 ram.csv 文件中的数据，做你想做的事情吧！
  }
}
```


3、[godot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/godotengine/godot)：一款功能丰富的开源游戏引擎。最初它只是一款 2D 引擎，近期拓展了 3D 部分的能力。相较于 UE4 或者 Unity 这样的成熟商业引擎来说，Godot 还很年轻不够成熟，尤其 3D 方面的能力。但它拥有简易的开发方式，上手简单。而且社区活跃、文档覆盖全面、有较为丰富的示例代码，对于刚入门的游戏开发者友好。同时开源引擎底层代码完全开源，开发者可以阅读和贡献代码，而不是只停留在游戏逻辑开发层面。总而言之 Godot 是一个极有潜力的游戏引擎，推荐给想学习游戏开发的同学


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/15634981.jpg' style="max-width:80%; max-height=80%;"></img></p>

4、[UNO](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Gusabary/UNO)：使用 C++ 编写的命令行 UNO 纸牌游戏。操作方便支持人机或联机对战，游戏基于 Asio 网络库和现代 C++ 开发，也有对 C++17 的尝试。分别实现了服务端、客户端，代码简单对 C++ 新手友好，UNO 的爱好者快来玩一玩吧！


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/297546772.gif' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
5、[water.css](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kognise/water.css)：一个专门为简单页面和示例网页准备的 CSS 框架


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/179574410.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
6、[fyne](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fyne-io/fyne)：一款 Go 语言跨平台 UI 库。想用 Go 写图形界面应用的小伙伴，快速上手：
```
安装
$ go get fyne.io/fyne
运行一个 demo
$ go get fyne.io/fyne/cmd/fyne_demo/
$ fyne_demo
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/120227732.png' style="max-width:80%; max-height=80%;"></img></p>

7、[golearn](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sjwhitworth/golearn)：Go 写的机器学习框架。来，跑个模型试试吧：
```
cd $GOPATH/src/github.com/sjwhitworth/golearn/examples/knnclassifier
go run knnclassifier_iris.go
```


### Java 项目
8、[keepass2android](https://hellogithub.com/periodical/statistics/click?target=https://github.com/PhilippC/keepass2android)：一个开源的 Android 密码管理器。[下载地址](https://github.com/PhilippC/keepass2android/releases)，功能：
- 仅需输入一次安全性很强的密码（很长或随机的密码）
- 支持几乎可与所有的 Android 的浏览器
- 支持 .kdbx 文件的读写
- 能够编辑条目包括附加字符串字段、文件附件、标签等
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/104254445.png' style="max-width:80%; max-height=80%;"></img></p>

9、[PrettyZoo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vran-dev/PrettyZoo)：一款 Java 写的高颜值 ZooKeeper 客户端桌面应用。该项目使用了 JDK11 以及 JavaFX 编写的 GUI 客户端，代码量适中适合想学习 JavaFX 编写应用的朋友。需要连接 ZK 服务端查看数据的话，手边有这么个工具还是挺方便的。实用和颜值集一身的项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/211431657.jpg' style="max-width:80%; max-height=80%;"></img></p>

10、[vueblog](https://hellogithub.com/periodical/statistics/click?target=https://github.com/MarkerHub/vueblog)：一款轻量级 Java 博客项目。基于 SpringBoot+Vue 实现并附有详细开发文档和讲解视频，让刚学会 Java 的同学也能搞定。每个体面的技术人员可能都有一个自己说了算的博客吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/263788932.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
11、[Ant-Forest](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SuperMonster003/Ant-Forest)：基于 Auto.js 的蚂蚁森林能量自动收获脚本。它是个“绿色环保”的项目，我能从中感受到满满的爱和想把它做好的决心！来看看作者开发 Ant-Forest 时解决了哪些难题：
1. 能量球识别无法使用控件信息（使用基于霍夫变换的图像识别）
2. 脚本执行逻辑易被打断（使用事件监听及扩展模块增强鲁棒性）
3. 每次只能运行一次（完善的复查及定时循环功能）
4. 不同设备分辨率及屏幕比例不同（使用等比缩放/定宽缩放等进行适配）


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/176399479.png' style="max-width:80%; max-height=80%;"></img></p>

12、[h5-Dooring](https://hellogithub.com/periodical/statistics/click?target=https://github.com/MrXujiang/h5-Dooring)：一款功能齐全的 H5 页面可视化配置平台。让你通过可视化的方式制作出 H5 页面，技术栈以 React 为主，后台采用 Node.js 实现。虽然网上有很多这种工具，但本项目免费开源、功能齐全值得一试


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/289417971.png' style="max-width:80%; max-height=80%;"></img></p>

13、[tui.image-editor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nhn/tui.image-editor)：功能齐全的图片编辑器。支持图片剪裁、旋转、涂鸦等功能，实现了 Vue 和 React 封装的组件，便于整合进你的项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/57261731.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[windows95](https://hellogithub.com/periodical/statistics/click?target=https://github.com/felixrieseberg/windows95)：基于 Electron 实现的 Windows 95 操作系统。它实现了该操作系统下的所有东西，对！所有！想体验下 Windows 95 版的扫雷吗？下载安装即可


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/145803079.png' style="max-width:80%; max-height=80%;"></img></p>

15、[x-spreadsheet](https://hellogithub.com/periodical/statistics/click?target=https://github.com/myliang/x-spreadsheet)：基于 JavaScript 实现的轻量级 Web 电子表格库。它功能齐全，包含表格的基本操作和函数等，还有详细的中文文档，[在线尝试](https://myliang.github.io/x-spreadsheet/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/147656990.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C 项目
16、[LuLu](https://hellogithub.com/periodical/statistics/click?target=https://github.com/objective-see/LuLu)：免费开源的 macOS 防火墙软件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/103010090.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
17、[humhub](https://hellogithub.com/periodical/statistics/click?target=https://github.com/humhub/humhub)：用 PHP 写的开源社交平台。看过《社交网络》的小伙伴，都知道大名鼎鼎的 Facebook 最早就是扎克伯格用 PHP 语言写出来的，humhub 能够让不会编程的小伙伴也可以用创建出一个社交平台啦。跟着提示一步步操作，不到 1 分钟我的社交平台就建好了，[点击访问](https://hellogithub.humhub.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/16685462.png' style="max-width:80%; max-height=80%;"></img></p>

18、[phpbrew](https://hellogithub.com/periodical/statistics/click?target=https://github.com/phpbrew/phpbrew)：一个编译、安装、管理多版本 PHP 的工具。有了它就可以方便地在不同 PHP 版本之间自由切换啦，特性：
- 配置选项简化为 Variants 无需担心路径问题
- 集成至 bash/zsh 等，易于切换版本
- 易于安装、启用 PHP 扩展


### Python 项目
19、[pgcli](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dbcli/pgcli)：支持语法高亮和自动补全的 Postgres 数据库客户端命令行工具。它安装简单上手快速，如果你用过 Postgres 数据库自带的命令行工具，就一定能感受到 pgcli 的迷人之处


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/25126616.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[python-patterns](https://hellogithub.com/periodical/statistics/click?target=https://github.com/faif/python-patterns)：Python 设计模式和使用场景的集合


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/4578002.png' style="max-width:80%; max-height=80%;"></img></p>

21、[pythonguis-examples](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pythonguis/pythonguis-examples)：基于 PyQt 框架写的小型桌面应用程序的集合。想用 Python 写桌面应用的小伙伴，这个项目应该可以帮到你。比如写个扫雷游戏：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/120960730.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
22、[bat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sharkdp/bat)：替代 cat 的命令行工具。你还在命令行用 cat 查看文件吗？那你就 out 啦！今天推荐的 bat 它不仅支持语法高亮，还能展示 Git 的改动。macOS 下安装命令：`brew install bat` 相信你用过 bat 后就不会再想用回 cat 了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/130464961.png' style="max-width:80%; max-height=80%;"></img></p>

23、[jpeg_tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/MROS/jpeg_tutorial)：教你编写 JPEG 解码器的教程，示例为 Rust 代码


### Swift 项目
24、[Pine](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lukakerr/Pine)：一个免费、轻量、简洁的 macOS Markdown 编辑器。功能：
- 主题
- LaTex 公式
- 自动保存
- 自定义字体
- 字数统计等写作分析
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/131082361.png' style="max-width:80%; max-height=80%;"></img></p>

25、[Publish](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JohnSundell/Publish)：专为 Swift 开发人员准备的静态网站生成器。让你实现整个网站都是用 Swift 构建的工具，支持多种主题、插件以及更多强大的自定义选项。[示例网站](https://swiftbysundell.com/)，安装和快速开始：
```
$ git clone https://github.com/JohnSundell/Publish.git
$ cd Publish
$ make
$ mkdir MyWebsite
$ cd MyWebsite
$ publish new
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/230532062.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
26、[pulse](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alex-damian/pulse)：根据包含马赛克的人脸图像，生成一张相似容貌的结果。注意不是复原哦，仅可用于人脸


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/265645902.gif' style="max-width:80%; max-height=80%;"></img></p>

27、[Surface-Defect-Detection](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Charmve/Surface-Defect-Detection)：该项目整理了目前大量靠谱的表面缺陷检测数据集，还有最新的顶会论文以及作者的解读笔记。从事视觉方向的小伙伴，心动了吗？


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/298980599.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
28、[neofetch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dylanaraps/neofetch)：展示操作系统信息的命令行工具，支持将近 150 种操作系统


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/48795298.png' style="max-width:80%; max-height=80%;"></img></p>

29、[open-source-rover](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nasa-jpl/open-source-rover)：NASA 面向科技爱好者开源的火星漫游车设计方案和代码。通过该项目你可以使用便宜的树莓派做出自己的火星漫游车，所需的零件很容易就可以买到，遥控部分是使用现成的 Xbox 手柄或者手机，减少花销。喜欢动手和硬件的小伙伴们，这个东西够酷吗？


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/139205847.jpg' style="max-width:80%; max-height=80%;"></img></p>

30、[sql-style-guide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mattm/sql-style-guide)：一份 SQL 语句编写风格建议。比如：
```
-- Good
select *
from users
where email = 'example@domain.com'

-- Bad
select *
from users
where email = "example@domain.com"
```


31、[Web-Dev-For-Beginners](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/Web-Dev-For-Beginners)：微软开源的 Web 开发教程。该教程共有 24 节课，但目前只有英文版


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/311525798.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
32、[pure-bash-bible](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dylanaraps/pure-bash-bible)：该书有好多复制就能用的 bash 函数，我愿称其为 bash 的“奇技淫巧”。比如把字母转为大写的函数：
```
upper() {
    # Usage: upper "string"
    printf '%s\n' "${1^^}"
}

$ upper "hello"
HELLO
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/57/137147386.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub56.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub58.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/57'>这里</a>。
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
