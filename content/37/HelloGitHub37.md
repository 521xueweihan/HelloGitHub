# 《HelloGitHub》第 37 期
>兴趣是最好的老师，**HelloGitHub** 就是帮你找到兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 简介
分享 GitHub 上有趣、入门级的开源项目。

这是一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 人群的月刊，月刊的内容包括：**各种编程语言的项目**、**让生活变得更美好的工具**、**书籍、学习笔记、教程等**，这些开源项目大多都是非常容易上手，而且非常 Cool。主要是希望大家能动手用起来，加入到**开源社区**中。
- 会编程的可以贡献代码
- 不会编程的可以反馈使用这些工具中的 Bug
- 帮着宣传你觉得优秀的项目
- Star 项目⭐️

在浏览、参与这些项目的过程中，你将学习到**更多编程知识**、**提高编程技巧**、**找到编程的乐趣**。

🎉 最后 HelloGitHub 这个项目就诞生了 🎉

## 目录
- [C# 项目](#C-项目)
- [C++ 项目](#C-项目-1)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [教程](#教程)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C# 项目
1、[RemoteDesktopManage](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xunki/RemoteDesktopManage)：基于 MSTSC 连接 Windows 远程桌面，并对其进行封装实现管理多个远程桌面配置的小工具。更加方便地管理多个远程桌面，实现同时远程、互相切换。相当于把多个 MSTSC 集合在一个软件里，并进行分组打标试用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/RemoteDesktopManage.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
2、[tinytetris](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/taylorconor/tinytetris)：一个用 C++ 编写的终端版俄罗斯方块游戏。提供了两个版本的源码，分为注释版和库版，注释较多易于理解和学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/tinytetris.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
3、[overlord](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bilibili/overlord)：基于 Go 语言编写的 memcache 和 redis&cluster 的代理及集群管理平台。致力于提供自动化高可用的缓存服务解决方案。自带图形界面的缓存集群管理程序，[安装步骤](https://github.com/bilibili/overlord/blob/master/doc/wiki-cn/platform-deploy.md)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/overlord.png' style="max-width:80%; max-height=80%;"></img></p>

4、[kratos](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/go-kratos/kratos)：哔哩哔哩开源的一套 Go 微服务框架，包含大量微服务相关框架及工具。解决了 gin 在微服务场景下的一些适配和微服务本身的一系列生态，[快速开始](https://github.com/bilibili/kratos/blob/master/doc/wiki-cn/quickstart.md)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/kratos.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[docker-slim](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/docker-slim/docker-slim)：自动缩减 docker 镜像的体积的工具。大幅度缩减 docker 镜像的体积，方便分发，使用命令 `docker-slim build --http-probe your-name/your-app`。比如 Node.js 镜像缩减后的对比：
```
from ubuntu:14.04 - 432MB => 14MB (缩减了 30.85 倍)

from debian:jessie - 406MB => 25.1MB (缩减了 16.21 倍)

from node:alpine - 66.7MB => 34.7MB (缩减了 1.92 倍)
```

6、[akutan](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/eBay/akutan)：eBay 开源的分布式图数据库，少数依然支持 SparQL 的图数据库

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
7、[giffun](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/guolindev/giffun)：Android 端开源的 GIF 浏览和分享 App。该应用界面基于 Material Design 标准设计，围绕 GIF 为主题，建立了一个小型的社交系统。支持：
- 查看热门搞笑的 GIF 图
- 关注你喜欢的人，他的有趣分享尽收眼底
- 一键发布你自己的 GIF 趣图
- 对你感兴趣的内容点赞、点评
- 喜欢的内容轻松转发至主流社交软件，传递你的快乐

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/giffun.gif' style="max-width:80%; max-height=80%;"></img></p>

8、[cim](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/crossoverJie/cim)：一款面向开发者的 IM 即时通讯系统。命令行通讯工具，对开发者友好。提供了一些组件让开发者易于扩展和定制功能。架构图如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/cim.jpeg' style="max-width:80%; max-height=80%;"></img></p>

9、[SpringAll](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wuyouzhuguli/SpringAll)：Spring 系列源码教程，包含 Spring Boot、Spring Boot、Spring Cloud 等。Spring 是 Java 目前生命力最强的框架之一，通过资料与源码的配合，容易学习和上手

10、[seata](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/seata/seata)：一套一站式分布式事务解决方案。让分布式事务的使用像本地事务的使用一样，简单和高效，并逐步解决开发者们遇到的分布式事务方面的所有难题。分布式事务提出了很多年，但是一直没有很好的解决方案，要不就收费很贵。蚂蚁金服开源的 seata，将让分布式事务不在束之高阁，任何需要的人都可以使用它，推荐学习和使用。工作流程图如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/seata.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
11、[xgplayer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bytedance/xgplayer)：由字节跳动西瓜视频开源的带解析器、能节省流量的 HTML5 视频播放器。可以作为 H5 组件、Vue、React 组件单独使用。它根据组件化的原则设计了一个独立的、可分离的 UI 组件。更重要的是，它不仅在 UI 层具有灵活性，而且在功能上也很大胆：它摆脱了视频加载、缓冲和格式支持。在播放器端加载视频、解析视频、转换格式，让不支持分段播放的 MP4 动态支持，这样就无须转换源视频的格式，服务器端也无其他开销。[官网](http://h5player.bytedance.com/)，示例代码：
```javascript
//  安装：$ npm install xgplayer
// 第一步：<div id="vs"></div>
// 第二步：
import Player from 'xgplayer';

const player = new Player({
    id: 'vs',
    url: 'http://s2.pstatp.com/cdn/expire-1-M/byted-player-videos/1.0.0/xgplayer-demo.mp4'
})
```

12、[zhui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zhui-team/zhui)：这是一款国风的组件库。好用的组件库千千万，有趣的创意万里挑一

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/zhui.png' style="max-width:80%; max-height=80%;"></img></p>

13、[emoji-minesweeper](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/muan/emoji-minesweeper)：Emoji 符号的扫雷游戏。代码很简短，游戏创意很酷。寥寥 300+ 行代码实现该游戏，简短易于初学者学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/emoji-minesweeper.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[squoosh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/GoogleChromeLabs/squoosh)：谷歌开源的图片压缩工具。在保证图片质量的情况下快速压缩图片，支持多种图片格式。6.63M 的图片压缩后为 2.92M，使用起来简单方便

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/squoosh.png' style="max-width:80%; max-height=80%;"></img></p>

15、[leetcode](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/azl397985856/leetcode)：更加贴近前端的数据结构与算法的库。以 leetcode 作为切入点，详细讲解关于数据结构的方方面面， 并以JavaScript 语言作为解题语言。 后期会加入更多关于前端贴合的内容， 比如：`react fiber` 的实现和链表、`react hooks` 的实现和数组等等
- 第一部分：leetcode 经典题目的解析，包括思路、关键点和具体的代码实现
- 第二部分：对于数据结构与算法的总结
- 第三部分：anki 卡片， 将 leetcode 题目按照一定的方式记录在 anki 中，方便大家记忆

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
16、[ffmpeg-python](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kkroening/ffmpeg-python)：FFmpeg 是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。这个是其 Python 的库，可以用该库操作、处理视频和音频。示例代码：
```python
# 水平翻转视频
import ffmpeg
stream = ffmpeg.input('input.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/ffmpeg-python.png' style="max-width:80%; max-height=80%;"></img></p>

17、[pyright](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/pyright)：微软出品的 Python 静态类型检查工具。执行速度快，适合大型 Python 项目，引用一句话：动态语言一时爽，重构火葬场

18、[pyxel](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kitao/pyxel)：基于 Python 编程程语言实现的复古游戏引擎。示例代码：
```python
# 代码中导入 Pyxel 模块后
import pyxel
# 首先使用 init 函数指定窗口大小
pyxel.init(160, 120)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)
# 最后然后使用 run 函数启动 Pyxel 应用程序
pyxel.run(update, draw)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/pyxel.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
19、[githubchart-api](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/2016rshah/githubchart-api)：根据 GitHub 账号的贡献记录生成对应图像。一行代码，可以在任何网站展示自己在 GitHub 上的贡献活跃图标。示例代码：
```
<img src="http://ghchart.rshah.org/用户名" alt="Github commit chart" />
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/githubchart-api.png' style="max-width:80%; max-height=80%;"></img></p>

20、[guides](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thoughtbot/guides)：Ruby 编程风格指南。统一的格式风格有利于代码的维护和迭代，对于 Ruby 使用者而言帮助极大

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
21、[GodEye](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zixun/GodEye)：一行代码自动显示日志、崩溃、网络、ANR、泄漏、CPU、文件夹等信息，就像上帝睁开眼睛一样

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/GodEye.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
22、[zju-icicles](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/QSCTech/zju-icicles)：浙江大学各种课程相关资源集合。包含：课程、作业、答案、复习资料、选课攻略等，是浙大在校生的必备资源，对于有考研想法的小伙伴而言也是很好的资源

23、[awesome-scalability](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/binhnguyennus/awesome-scalability)：一个系统的阅读列表，描述了可扩展、高可用、高性能的大型系统背后的东西。每部分都是基于真实案例，讲述了如何搭建一个可扩展、高可用、高性能的大型系统，案例都是来自于经过数百万甚至数十亿用户实战检验的系统。对于所有工程师而言都是一个很好的学习资料，开卷有益

24、[awesome-wechat-weapp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/justjavac/awesome-wechat-weapp)：该项目收集了微信小程序开发过程中会使用到的资料、问题以及第三方组件库。随着微信小程序的市场越来越大，很多公司也专门以制作小程序为业，不论对感兴趣的人还是想自己动手做小程序的人而言，这份合集省去了不少查找资料的时间

25、[REKCARC-TSC-UHT](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/PKUanonym/REKCARC-TSC-UHT)：清华大学计算机系课程相关资源集合。内容丰富，包含从大一到大四，跟着清华学子一起学习传说中高校的课程吧

26、[SJTU-Courses](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CoolPhilChen/SJTU-Courses)：上海交通大学课程资料分享

27、[libpku](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lib-pku/libpku)：由第三方整理的北京大学课程资料，涵盖了专业课、公选课、通选课等

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
28、[prometheus-book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yunlzheng/prometheus-book)：《Prometheus 操作指南》，[在线阅读](https://yunlzheng.gitbook.io/prometheus-book/parti-prometheus-ji-chu/quickstart/why-monitor)

29、[the-craft-of-selfteaching](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/selfteaching/the-craft-of-selfteaching)：《自学是门手艺》一个编程入门者的自学心得。如今学习资源很多，对于初学者入门而言，最难的是如何自学，阅读本书打开编程自学大门吧

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 教程
30、[nginx-admins-handbook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/trimstray/nginx-admins-handbook)：该项目描述了如何提高 Nginx 的性能、安全性等方面的步骤，让你的网站在 SSL Labs 的评级到达 A+

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
31、[openpose](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CMU-Perceptual-Computing-Lab/openpose)：基于卷积神经网络和监督学习的开源库，可以实现人的面部、躯干和四肢甚至手指的跟踪。适用于多人，且标记准确，同时具有较好的鲁棒性

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/openpose.png' style="max-width:80%; max-height=80%;"></img></p>

32、[FaceDetection-DSFD](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TencentYoutuResearch/FaceDetection-DSFD)：腾讯优图的双分支人脸检测器全新算法，该算法已经被计算机视觉顶级会议 CVPR 2019 接收。优图此次提出的 DSFD 人脸检测算法，主要有 3 点创新：
1. 新的特征增强模块（FEM：Feature Enhance Module）
2. 分层锚点渐进式的代价函数监督（PLA：Progressive Anchor Loss）
3. 改进的锚点匹配策略（Improved Anchor Matching Strategy）

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/FaceDetection-DSFD.png' style="max-width:80%; max-height=80%;"></img></p>

33、[SPADE](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NVlabs/SPADE)：英伟达（NVIDIA）新开源的绘图工具。利用生成对抗网络，根据几根简单的线条就能生成栩栩如生的图像

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/SPADE.gif' style="max-width:80%; max-height=80%;"></img></p>

34、[ICCV2019-LearningToPaint](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hzwer/ICCV2019-LearningToPaint)：一个深度强化学习项目，研究如何让机器用画笔画画。也可体验制作自己的绘画或根据一张图片生成一整个绘画过程

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/37/img/LearningToPaint.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/36/HelloGitHub36.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/38/HelloGitHub38.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
