# 《HelloGitHub》第 36 期
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
- [CSS 项目](#CSS-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [机器学习](#机器学习)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

**Tips**：如果文中的图刷不出来，可以向我们[反馈](https://github.com/521xueweihan/HelloGitHub/issues/899)。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C# 项目
1、[feel](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kulics-works/feel)：一个专注于简单的开源跨平台编程语言。这门语言的设计目标是改进阅读与编写效率，降低语法负担。让使用者能够把真正的注意力放在解决问题上，只需极少的代码就能优雅地表达逻辑。[中文手册](https://github.com/kulics/xs/blob/master/book-zh/introduction.md)，示例代码如下：
```
# export namespace
\HelloWorld {
    System # import namespace
}
# package
program -> {
    # main function
    Main() -> () {
        # list
        greetings := {"Hello", "Hola", "Bonjour",
                    "Ciao", "こんにちは", "안녕하세요",
                    "Cześć", "Olá", "Здравствуйте",
                    "Chào bạn", "您好"}
        # for-each  
        @ item <- greetings {
            # switch
            ? item -> [ 0 <= 8 ] {
                prt(item) # call function
            } _ {
                # lambda
                prt( greetings.filter( {it -> it.len> 4} ) )
                <- @
            }
        }
    }
}
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
2、[calculator](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/calculator)：微软 Windows 系统预装的计算器工具开源了。该工具提供标准、科学、程序员计算器的功能，以及各种度量单位和货币之间的转换功能。实现语言为 C++ 代码并不复杂，快来看看微软工程师编写的代码吧！运行效果如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/calculator.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
3、[CSS-Inspiration](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chokcoco/CSS-Inspiration)：这里汇集了 CSS 的使用和学习的示例代码，展示不同 CSS 属性或者不同的课题使用 CSS 来解决的各种方法。[在线阅读地址](https://chokcoco.github.io/CSS-Inspiration/#/)包含代码实际展示样式

4、[bootstrap-table](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wenzhixin/bootstrap-table)：基于 Bootstrap 的 jQuery 表格插件，通过简单的设置就可以拥有强大的单选、多选、排序、分页、编辑、导出、过滤（扩展）等功能。示例代码：
```
<table data-toggle="table">
  <thead>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Item 1</td>
      <td>$1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Item 2</td>
      <td>$2</td>
    </tr>
  </tbody>
</table>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/bootstrap-table.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
5、[drone](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/drone/drone)：一个基于 Docker 的持续集成平台，使用 Go 语言编写

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/drone.png' style="max-width:80%; max-height=80%;"></img></p>

6、[etcd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/etcd-io/etcd)：一个高可用的分布式键值数据库，k8s 全家桶标配的注册与发现服务。它采用 raft 一致性算法，基于 Go 语言实现。可以通过该项目了解、学习 raft 的实际应用场景
```
# 使用 etcd 的客户端存取键值对
$ etcdctl put mykey "this is awesome"
$ etcdctl get mykey
```

7、[pprof](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/pprof)：Go 语言的性能分析工具，可以用来调试 Go 程序的内存泄露、goroutine 泄露之类的问题。使用方法：
```
# 安装
$ go get -u github.com/google/pprof
# 生成一个profile文件
$ pprof -top [你的golang程序二进制文件] profile.pb.gz
# 生成火焰图
$ pprof -web [你的golang程序二进制文件] profile.pb.gz
```

8、[learn-go-with-tests](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/quii/learn-go-with-tests)：通过单元测试学习 Go 语言。下载仓库源码后，进入对应目录。每一个小文件夹就是一个对应的 Go 项目，在里面`go test`即可运行单元测试。由于是测试驱动开发，所以需要在你改动代码之后跑通单元测试才算学会通过。每一个对应的文件夹都有相应 Markdown 文字教程，比较浅显易懂。而且还有[中文版](https://studygolang.gitbook.io/learn-go-with-tests)

9、[auxpi](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/0xDkd/auxpi)：基于 API 的简单图床应用。整合了主流图床的 API，并且做了一个 GUI 用来管理，[安装](https://github.com/aimerforreimu/AUXPI/wiki/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC)简单

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/AUXPI.jpeg' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
10、[Luban](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Curzibn/Luban)：图片压缩是常见的问题，那么微信是如何处理图像的压缩？Luban（鲁班）就是通过在微信朋友圈发送近 100 张不同分辨率的图片，对比原图与微信压缩后的图片逆向推算出来的压缩算法。示例代码：
```java
// 同步调用
Flowable.just(photos)
    .observeOn(Schedulers.io())
    .map(new Function<List<String>, List<File>>() {
      @Override public List<File> apply(@NonNull List<String> list) throws Exception {
        // 同步方法直接返回压缩后的文件
        return Luban.with(MainActivity.this).load(list).get();
      }
    })
    .observeOn(AndroidSchedulers.mainThread())
    .subscribe();
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/Luban.png' style="max-width:80%; max-height=80%;"></img></p>

11、[yacy_search_server](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yacy/yacy_search_server)：一款采用了新的搜索方法的搜索引擎软件。 它不需要中央服务器，但它搜索的结果来自于独立的分布式网络。在这样的分布式网络中，没有任何一个实体可以决定列出的内容或结果出现的顺序。启动和关闭的方法：
- GNU/Linux 系统，启动：`./startYACY.sh`、关闭：`./stopYACY.sh`
- Windows 系统，启动：双击`startYACY.bat`、 关闭：双击`stopYACY.bat`
- Mac OS X 系统，请使用 Mac 应用程序，并像其他 Mac 应用程序那样启动或停止它（双击）

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
12、[Web](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/qianguyihao/Web)：前端入门的图文教程，从 0-1 的过程。内容详细，对于新入行前端的同学有很多的帮助

13、[ncform](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ncform/ncform)：只需要配置相关参数，便可方便生成表单的UI组件，自带校验规则满足日常 90% 的要求。表单是 Web 应用中常见的组件，但是开发表单是一个重体力活，ncform 通过配置便可生成表单，极大的提高了开发效率

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/ncform.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[vscode-leetcode](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/LeetCode-OpenSource/vscode-leetcode)：这是一个可以让用户在 VS Code 编辑器中，练习 LeetCode 习题的插件。支持：查看高票解答、提交答案、测试答案等。提高了刷题效率，助你在校招、社招中杀出重围。上班摸鱼刷题利器

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/vscode-leetcode.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[griffith](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zhihu/griffith)：让流式播放变得简单。无论你视频格式是 `mp4` 还是 `hls`，Griffith 都能使用媒体源拓展（MSE）来实现分段加载等功能，提供在线视频播放。示例代码：
```javascript
// yarn add griffith

import Player from 'griffith'

const sources = {
  hd: {
    play_url: 'https://zhstatic.zhihu.com/cfe/griffith/zhihu2018_hd.mp4',
  },
  sd: {
    play_url: 'https://zhstatic.zhihu.com/cfe/griffith/zhihu2018_sd.mp4',
  },
}

render(<Player sources={sources} />)
```

16、[makegirlsmoe_web](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/makegirlsmoe/makegirlsmoe_web)：动漫角色图片生成工具。支持：选择发色、发型、眼睛、皮肤、微笑、风格等等特征生成二次元图片。自定义生成可爱的二次元头像，二次元界福音。[在线尝试](https://make.girls.moe/#/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/makegirlsmoe_web.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
17、[BackgroundMusic](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kyleneideck/BackgroundMusic)：macOS 音频工具，包含功能：自动暂停音乐、设置各个应用程序的音量、录制系统音频

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/BackgroundMusic.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
18、[php-console](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/inhere/php-console)：使用简单，功能全面的 PHP 命令行应用库。提供控制台参数解析、命令运行、颜色风格输出、 用户信息交互等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/php-console.png' style="max-width:80%; max-height=80%;"></img></p>

19、[PasteMe](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/LucienShui/PasteMe)：快速分享文本、代码的网站项目。支持加密、一键复制、永久保存、阅后即焚等功能。[在线示例](https://pasteme.cn/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/PasteMe.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
20、[ds-cheatsheets](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FavioVazquez/ds-cheatsheets)：Python 在数据科学方面使用库的速查表，包含了 Pandas、Jupyter、SQL、Dask 等。虽然都是些基本的 API 调用，但是用来备忘和速查足以

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/ds-cheatsheets.png' style="max-width:80%; max-height=80%;"></img></p>

21、[better-exceptions](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Qix-/better-exceptions)：更加友好、实用、漂亮的输出 Python 异常

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/better-exceptions.png' style="max-width:80%; max-height=80%;"></img></p>

22、[scrapydweb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/my8100/scrapydweb)：Scrapy 爬虫管理平台，支持：Scrapyd 集群管理、日志可视化、定时任务、邮件通知、移动端 UI

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/scrapydweb.png' style="max-width:80%; max-height=80%;"></img></p>

23、[awesome-python-login-model](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Kr1s77/awesome-python-login-model)：该项目收集了各大网站登陆方式和部分网站的爬虫程序。登陆方式实现包含 selenium 登录、通过抓包直接模拟登录等。有助于新手研究、编写爬虫

24、[gita](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nosarthur/gita)：基于 Python 开发的管理 git 工具，使用后可在任何目录下代理执行 git 指令。同时支持同时显示多个 repo 的状态信息、本地分支与远程分支的关系等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/gita.png' style="max-width:80%; max-height=80%;"></img></p>

25、[dash](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/plotly/dash)：一款只用几百行 Python 代码就可以轻易实现数据分析可视化的利器，是目前 Python 社区数据可视化主要的工具之一。具有：使用简单、易于扩展、开发团队活跃等特点

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/dash.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[pylane](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NtesEyes/pylane)：一个基于 gdb 的 Python 进程注入和调试工具。通过 gdb trace Python 进程，然后在该进程的 Python vm 中动态地注入一段 Python 代码， 从而对一个运行中的 Python 进程执行一段任意的逻辑。更多 Python 调试经验，可阅读这篇[文章](https://mp.weixin.qq.com/s/Mlhrp2E390EMD0ZfSaNFKw)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/pylane.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
27、[jekyll](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jekyll/jekyll)：强大的静态博客网站生成工具。无需数据库，可以通过 Markdown 和 Config 轻松生成一个静态博客。该项目十分成熟、社区活跃、拥有多种主题可供选择。最后可以通过 [GitHub Page](https://pages.github.com/) 把生成的博客免费部署上线。快速开始：
```
1. 安装 jekll：gem install bundler jekyll
2. 创建项目：jekyll new my-awesome-site
3. 进入新创建的项目：cd my-awesome-site
4. 本地运行：bundle exec jekyll serve
5. 本地访问地址：http://localhost:4000
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
28、[Bagel](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yagiz/Bagel)：一个小型、原生的 iOS 网络调试工具。使用过程不需要配置证书、代理之类的东西。只需要 iOS 设备和 Mac 处于同一网络，就可以查看、监控 App 的网络流量等信息

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/Bagel.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
29、[howto-make-more-money](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/easychen/howto-make-more-money)：该项目介绍了程序员如何挣零花钱的姿势

30、[translations](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/oldratlee/translations)：一些不错的英文资料、文章翻译项目

31、[ChinaMobilePhoneNumberRegex](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/VincentSit/ChinaMobilePhoneNumberRegex)：一组匹配中国大陆手机号码的正则表达式

32、[web-frameworks](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/the-benchmarker/web-frameworks)：该项目展示了不同编程语言的 Web 框架性能对比，持续更新。可以作为挑选 Web 框架的参照信息

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/web-frameworks.png' style="max-width:80%; max-height=80%;"></img></p>

33、[FiraCode](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tonsky/FiraCode)：高逼格的具有编程连字的等宽字体，最适合在编程编辑器、IDE、终端中使用。十分酷的字体，可以增加写代码的欲望

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/img/FiraCode.png' style="max-width:80%; max-height=80%;"></img></p>

34、[ChromeAppHeroes](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zhaoolee/ChromeAppHeroes)：优秀、实用的 Chrome 插件集合。该项目还包含插件的中文的使用介绍，为的是让好的插件被更多人发现和使用

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
35、[PythonDataScienceHandbook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jakevdp/PythonDataScienceHandbook)：英文原版《Python Data Science Handbook》，该书对于希望或已经从事数据科学相关工作的 Python 工程师而言是重要的学习手册。[在线阅读](https://jakevdp.github.io/PythonDataScienceHandbook/)

36、[Go42](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ffhelicopter/Go42)：《Go语言四十二章经》Golang 入门书籍。书中作者总结了自己踩坑的经验总结和思考，[在线阅读](https://github.com/ffhelicopter/Go42/blob/master/SUMMARY.md)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
37、[BigGAN-PyTorch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ajbrock/BigGAN-PyTorch)：“Bye Bye TPU”，4 个 GPU 就能训练“史上最强” BigGAN！只需 4-8 个 GPU 即可训练，摆脱了算力束缚

38、[Virgilio](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/virgili0/Virgilio)：本资源库旨在为以下领域提供三种有机完整的学习路径：机器学习、商业智能、云计算。在此你将能够了解相关原理并且在项目实践中予以运用。如果仔细遵循这些学习路径，则可以从零开始构建完整的认识和获得始终可用的技能。事实上，这些学习路径不需要之前有相关知识，但基础编程和简单数学是理解和实践大多数相关概念的必要条件

39、[QuickDraw](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/uvipen/QuickDraw)：谷歌开发的一个流行的在线游戏，神经网络会猜测你在画什么。神经网络从每幅图画中学习，提高正确猜测涂鸦内容的能力。现在你可以基于这个仓库，用 Python 构建自己的 Quick Draw 游戏

40、[GNNPapers](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thunlp/GNNPapers)：自从卷积神级网络面世以来，大部分人将其应用在规则的空间结构数据当中，比如图像。但是现实中存在更多的并不具备规则的空间结构的数据，因此研究人员提出了处理这部分数据的网络模型-GNN。该项目列举了 GNN 方面的论文，较为全面，适合有一定基础的人阅读

41、[faceswap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/deepfakes/faceswap)：这个工具可以对图片和视频进行换脸。可以很方便地处理图片和视频，搞些有意思的事情

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/35/HelloGitHub35.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/37/HelloGitHub37.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
