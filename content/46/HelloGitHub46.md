# 《HelloGitHub》第 46 期
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
- [C 项目](#C-项目)
- [C++ 项目](#C-项目-1)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [其它](#其它)
- [机器学习](#机器学习)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

**Tips**：如果文中的图刷不出来，可以向我们[反馈](https://github.com/521xueweihan/HelloGitHub/issues/899)。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C 项目
1、[freebsd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/freebsd/freebsd)：FreeBSD 操作系统源码仓库。快拉住我，我有点飘了竟然敢点开操作系统看源码 😅

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
2、[design-patterns-cpp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/JakubVojvoda/design-patterns-cpp)：常见设计模式 C++ 语言实现版

3、[sudoku](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mayerui/sudoku)：C++ 实现的命令行数独游戏。600 余行代码，初学者也可以轻松学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/sudoku.png' style="max-width:80%; max-height=80%;"></img></p>

4、[indicators](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/p-ranav/indicators)：一个使用 C++ 编写的进度条库，你可以用它在命令行中实现美观的进度条。它使用方便、线程安全、支持多种进度条样式

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/indicators.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
5、[statping](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/statping/statping)：一个 Go 编写的服务状态展示页项目。通过该项目可以快速搭建起一个展示服务可用状态、服务质量的页面

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/statping.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[gormt](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xxjwxc/gormt)：一款 MySQL 数据库转 Go struct 的工具。支持：
- 命令行、界面方式生成
- YML 文件灵活配置
- 自动生成快捷操作函数
- 支持索引、外键等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/gormt.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[gojsonq](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thedevsaddam/gojsonq)：一款支持解析、查询 JSON/YAML/XML/CSV 数据的 Go 三方开源库。示例代码：
```go
package main

import "github.com/thedevsaddam/gojsonq"

func main() {
	const json = `{"name":{"first":"Tom","last":"Hanks"},"age":61}`
	name := gojsonq.New().FromString(json).Find("name.first")
	println(name.(string)) // Tom
}
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
8、[gradle](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gradle/gradle)：一个基于 Apache Ant 和 Maven 概念的项目自动化建构工具（干了这两个工具的活）。它使用一种基于 Groovy 的特定领域语言来声明项目设置，而不是传统的 XML（更灵活）。当前其支持的语言限于 Java、Groovy 和 Scala，计划未来将支持更多的语言

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/gradle.png' style="max-width:80%; max-height=80%;"></img></p>

9、[zxing](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zxing/zxing)：一款用于解析、生成多种格式的 1D/2D 条形码（UPC-A、QR Code、UPC-E、Data Matrix 等）的开源 Java 库。提供了多种的客户端支持包括：J2ME、J2SE 和 Android 等

10、[jodd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/oblac/jodd)：一组以极简为原则的 Java 服务框架和实用工具的项目。这不是一个介绍 Java 项目的集合，而是把经常会用到的功能，用尽可能少的代码实现并封装成库，供开发人员选择使用。当你要用 Java 快速实现一些功能的时候，从而不需要引入繁重的库就可以快速实现功能。一个功能一个库，灵活使用、极简实用，便于学习和理解
```
Jodd = tools + ioc + mvc + db + aop + tx + json + html < 1.7 Mb
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
11、[Learn-Vue-Source-Code](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NLRX-WJC/Learn-Vue-Source-Code)：该项目是作者学习 Vue 源码的笔记。[在线阅读](https://nlrx-wjc.github.io/Learn-Vue-Source-Code/)

12、[p5.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/processing/p5.js)：一个 JavaScript 创意编程程式库，可以用来绘图、实现艺术创意等。使用该库只需要会 JS 代码就可以用它画出许多有趣的东西，文档齐全能够快速上手，还有在线编辑器。[官网](https://p5js.org/zh-Hans/)，示例代码：
```javascript
function setup() {
  createCanvas(640, 480);
}

function draw() {
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/p5.png' style="max-width:80%; max-height=80%;"></img></p>

13、[concent](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/concentjs/concent)：一个兼容 Redux 生态的渐进式和高性能状态管理方案。基于依赖标记、引用收集和状态分发原理工作，通过独有的实例上下文机制增强组件能力，抹平类组件和函数组件的生命周期函数写法差异。内置 computed、watch、setup、event 等高级特性，让逻辑复用更优雅、组件表现形式更丰富、应用架构更稳健

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/concent.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[vue-monoplasty-slide-verify](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/monoplasty/vue-monoplasty-slide-verify)：基于 Vue2.0+ 的验证码插件。可用于网页注册等需要验证码的地方，滑动式的验证码免于字母验证码的繁琐输入。[在线演示](https://monoplasty.github.io/vue-monoplasty-slide-verify/)，示例代码：
```javascript
import Vue from 'vue';
import SlideVerify from 'vue-monoplasty-slide-verify';

Vue.use(SlideVerify);

export default {
      name: 'App',
      data(){
          return {
              msg: '',
          }
      },
      methods: {
          onSuccess(){
              this.msg = 'login success'
          },
          onFail(){
              this.msg = ''
          },
          onRefresh(){
              this.msg = ''
          }
      }
  }
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/vue-monoplasty-slide-verify.png' style="max-width:80%; max-height=80%;"></img></p>

15、[gods-pen](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ymm-tech/gods-pen)：一个在线生成 H5 页面的平台。用户无需掌握复杂的编程技术，通过简单拖拽、少量配置即可快速制作精美的页面，可用于营销场景下的页面制作。同时，也为开发者提供了完备的编程接入能力，通过脚本和组件的形式获得强大的组件行为和交互控制能力

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/gods-pen.png' style="max-width:80%; max-height=80%;"></img></p>

16、[fe-interview](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/azl397985856/fe-interview)：项目作者总结关于准备前端面试的复习汇总项目，项目不定时更新。这不仅仅是一份用于求职面试的攻略，也是一份前端小伙伴用来检视自己，实现突破的宝典。希望通过这个指南，大家可以打通自己的任督二脉，在前端的路上更进一步

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
17、[Bob](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ripperhe/Bob)：一款支持划词翻译和截图翻译 Mac 端翻译软件。系统默认划词工具有些不支持的 PDF 文件，通过这个软件截图翻译功能，可以舒服的解决阅读这些文件时需要翻译的问题

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/Bob.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[textmate](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/textmate/textmate)：一款 macOS 上著名的开源代码编辑器。它界面简洁，功能强大。支持高效的 Snippets 功能、主流版本控制系统、自定义主题、实时 HTML/Markdown 预览等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/textmate.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
19、[php-curl-class](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/php-curl-class/php-curl-class)：该开源项目封装了 PHP 的 cURL 库，使得发送 HTTP 请求变得简单。适用于需要 PHP 爬虫或者其它模拟 HTTP 访问的情况，示例代码：
```php
<?php
// 获取豆瓣电影示例
require '../vendor/autoload.php';
use Curl\Curl;

$curl = new Curl();
$url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=time&page_limit=20&page_start=1";
$curl->get($url);
$curl->setOpt(CURLOPT_SSL_VERIFYPEER, false);
$curl->close();
var_dump($curl->getResponse());exit;
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/php-curl-class.png' style="max-width:80%; max-height=80%;"></img></p>

20、[parsedown](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/erusev/parsedown)：一个小而美的 PHP 的 Markdown 解析库。该库提供了标准 Markdown 文本转化成 HTML 字符串功能，并拥有良好的文档。它的主文件只有一个，除了 PHP 版本限制必须高于 5.3 外几乎无依赖，可通过 composer 引入，也可以直接使用 Parsedown.php 文件。该项目中使用大量正则表达式，可作为学习正则表达式的示例，并且有完整的单元测试。示例代码：
```php
$Parsedown = new Parsedown();
echo $Parsedown->text('Hello _Parsedown_!'); # prints: <p>Hello <em>Parsedown</em>!</p>
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
21、[sentry](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/getsentry/sentry)：一款免费开源的 Python 实时异常监控平台。采用 C/S 模式，服务器端通过 Python 实现，同时提供 web 管理页面，支持从任何语言、任何应用程序发送事件。一个成熟的服务必要的一环就是异常告警，Sentry 可以帮你及时知道服务非预期的异常

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/sentry.png' style="max-width:80%; max-height=80%;"></img></p>

22、[vaex](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vaexio/vaex)：类似 Pandas 的 Python 数据处理库，在处理大型数据集的时候表现极大的优于 Pandas。Vaex 通过懒加载、延迟计算和零内存复制策略，极大的降低了内存的使用率、提高了计算的效率。从而能够每秒处理 10 亿行的数据，并且支持以直方图、密度图等形式展示数据。有大数据集处理需求的小伙伴赶快试试吧

23、[word_cloud](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/amueller/word_cloud)：Python 的词云生成工具。示例代码：
```python
# 加载内容
text = open(path.join(d, 'constitution.txt')).read()
# 生成词云图片
wordcloud = WordCloud().generate(text)
# 展示生成的图片
image = wordcloud.to_image()
image.show()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/word_cloud.png' style="max-width:80%; max-height=80%;"></img></p>

24、[KeymouseGo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/taojy123/KeymouseGo)：Python 实现的精简绿色版按键精灵。记录用户的鼠标、键盘操作，自动执行之前记录的操作，可设定执行的次数。在进行某些简单、单调重复的操作时，使用该软件可以十分省事儿。只需要录制一遍，剩下的交给 KeymouseGo 来做就可以了

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/KeymouseGo.jpg' style="max-width:80%; max-height=80%;"></img></p>

25、[ZeroNet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HelloZeroNet/ZeroNet)：一个使用 Bitcoin 加密和 BitTorrent 网络的去中心化网络。将传统巨头垄断的互联网变得平民化，不需要租用服务器不需要公网 IP，每个人都可以轻松创建分布式博客、分布式论坛、分布式微博、分布式视频网站、分布式直播网站等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/ZeroNet.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
26、[astuto](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/riggraz/astuto)：一个免费、开源的 Ruby 自托管客户反馈平台。它可以帮助您收集、管理用户的反馈并设置其优先级。客户反馈是大部分网站不可或缺的功能，使用 astuto 能够十分快速的给你的网站加上此功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/astuto.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
27、[valval](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/taojy123/valval)：一个基于 V 语言的 web 框架。V 语言是一门还在开发和完善过程中的语言，还不怎么成熟但却十分适合用于 web 开发，不仅官方的标准库中提供了 vweb 以及 orm 的支持，不少开发者也都推出了各自的 web 开发框架，valval 就是其中之一。示例代码如下：
```v
// demo.v
import valval

fn hello(req valval.Request) valval.Response {
    return valval.response_ok('hello world')
}

fn main() {
    mut app := valval.new_app(true)
    app.register('/', hello)
    valval.runserver(app, 8012)
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/valval.png' style="max-width:80%; max-height=80%;"></img></p>

28、[powerlevel9k](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Powerlevel9k/powerlevel9k)：一款 ZSH 系的 Powerline 主题。效果如下图：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/powerlevel9k.png' style="max-width:80%; max-height=80%;"></img></p>

29、[zotero](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zotero/zotero)：一款开源文献管理工具。可以方便的管理、收集、组织、引用和共享文献的工具，经常进行学术研究和文献阅读的小伙伴请收好

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/zotero.png' style="max-width:80%; max-height=80%;"></img></p>

30、[Hippy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/Hippy)：一个新生的跨端开发框架，目标是使开发者可以只写一套代码就直接运行于三个平台（iOS、Android 和 Web）。Hippy 的设计是面向传统 Web 开发者的，特别是之前有过 React Native 和 Vue 的开发者用起来会更为顺手，Hippy 致力于让前端开发跨端 App 更加容易。鹅厂提供的跨端开发框架，内部多款 APP 在用，还不快来试试！项目目录说明如下：
```
Hippy
├── examples                          # 前终端范例代码。
│   ├── hippy-react-demo              # hippy-react 前端范例代码。
│   ├── hippy-vue-demo                # hippy-vue 前端范例代码。
│   ├── ios-demo                      # iOS 终端范例代码。
│   └── android-demo                  # Android 终端范例代码。
├── packages                          # 前端 npm 包。
│   ├── hippy-debug-server            # Hippy 的前终端调试服务。
│   ├── hippy-react                   # Hippy 的 React 语法绑定。
│   ├── hippy-react-web               # hippy-react 转 Web 的库。
│   ├── hippy-vue                     # Hippy 的 Vue 语法绑定。
│   ├── hippy-vue-css-loader          # 用来将 CSS 文本转换为 JS 语法树以供解析的 Webpack loader。
│   ├── hippy-vue-native-components   # hippy-vue 中浏览器中所没有的，额外的，终端定制组件。
│   └── hippy-vue-router              # 在 hippy-vue 中运行的 vue-router。
├── ios
│   └── sdk                           # iOS SDK。
├── android
│   ├── support_ui                    # Android 终端实现的组件。
│   └── sdk                           # Android SDK。
├── core                              # C++ 实现的 JS 模块，通过 Binding 方式运行在 JS 引擎中。
├── layout                            # Hippy 布局引擎。
├── scripts                           # 项目编译脚本。
└── types                             # 全局 Typescript 类型定义。
```

31、[iptv](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/iptv-org/iptv)：全球各地 8 千多个公开、可用的网络电视频道集合。随着网络的日益发展，电视节目离我们越来越远。不用电视盒子，不用下载电视软件，直接使用流媒体软件看网络电视是一个不错的选择。操作步骤:
- 打开任何支持流媒体协议的播放器
- 然后粘贴流媒体地址：https://iptv-org.github.io/iptv/index.m3u
- 播放器推荐：IINA（Mac）、VLC（Linux）、Potplayer（Windows）

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/iptv.png' style="max-width:80%; max-height=80%;"></img></p>

32、[wuhan2020](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wuhan2020/wuhan2020)：武汉新型冠状病毒防疫信息收集平台。[在线浏览](https://wuhan2020.github.io/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
33、[faceai](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vipstone/faceai)：一款优秀入门级 AI 项目以及教程，内容涵盖：人脸、视频、文字的检测和识别。他不仅包含最基本的人脸检测、识别（图片、视频）、轮廓标识、头像合成（给人戴帽子），还有表情识别（生气、厌恶、恐惧等）、视频对象提取、图片修复（可用于水印去除）、图片自动上色等等。推荐这个开源项目不是因为它的内容强大，而是它的教程写的实在太好了，真 · 入门级。手把手教你如何使用这个项目，做出上述功能来。在每篇功能文章的教程里，不仅仅写了每个功能的技术实现方案，还有具体重点关键代码的注释和解释以及具体实现，让你非常轻松的能够看懂、学习和使用。对于想要入门或者了解机器学习的初学者不能再友好了。示例代码：
```python
# Tesseract Ocr文字识别
from PIL import Image
import pytesseract

path = "img\\text-img.png"
text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/46/img/faceai.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/45/HelloGitHub45.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/47/HelloGitHub47.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
