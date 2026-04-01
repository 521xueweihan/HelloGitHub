# HelloGitHub Vol.36
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C#
1、[koral](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kulics/koral)：一个专注于简单的开源跨平台编程语言。这门语言的设计目标是改进阅读与编写效率，降低语法负担。让使用者能够把真正的注意力放在解决问题上，只需极少的代码就能优雅地表达逻辑。[中文手册](https://github.com/kulics/xs/blob/master/book-zh/introduction.md)，示例代码如下：
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


### C++
2、[calculator](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/calculator)：微软 Windows 系统预装的计算器工具开源了。该工具提供标准、科学、程序员计算器的功能，以及各种度量单位和货币之间的转换功能。实现语言为 C++ 代码并不复杂，快来看看微软工程师编写的代码吧！运行效果如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/168008797.png' style="max-width:80%; max-height=80%;"></img></p>

### CSS
3、[bootstrap-table](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wenzhixin/bootstrap-table)：基于 Bootstrap 的 jQuery 表格插件，通过简单的设置就可以拥有强大的单选、多选、排序、分页、编辑、导出、过滤（扩展）等功能。示例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/12246785.png' style="max-width:80%; max-height=80%;"></img></p>

4、[CSS-Inspiration](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chokcoco/CSS-Inspiration)：这里汇集了 CSS 的使用和学习的示例代码，展示不同 CSS 属性或者不同的课题使用 CSS 来解决的各种方法。[在线阅读地址](https://chokcoco.github.io/CSS-Inspiration/#/)包含代码实际展示样式


### Go
5、[auxpi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/0xDkd/auxpi)：基于 API 的简单图床应用。整合了主流图床的 API，并且做了一个 GUI 用来管理，[安装](https://github.com/aimerforreimu/AUXPI/wiki/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC)简单


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/156077183.jpeg' style="max-width:80%; max-height=80%;"></img></p>

6、[etcd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/etcd-io/etcd)：一个高可用的分布式键值数据库，k8s 全家桶标配的注册与发现服务。它采用 raft 一致性算法，基于 Go 语言实现。可以通过该项目了解、学习 raft 的实际应用场景
```
# 使用 etcd 的客户端存取键值对
$ etcdctl put mykey "this is awesome"
$ etcdctl get mykey
```


7、[harness](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/harness/harness)：一个基于 Docker 的持续集成平台，使用 Go 语言编写


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/16607898.png' style="max-width:80%; max-height=80%;"></img></p>

8、[learn-go-with-tests](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/quii/learn-go-with-tests)：通过单元测试学习 Go 语言。下载仓库源码后，进入对应目录。每一个小文件夹就是一个对应的 Go 项目，在里面`go test`即可运行单元测试。由于是测试驱动开发，所以需要在你改动代码之后跑通单元测试才算学会通过。每一个对应的文件夹都有相应 Markdown 文字教程，比较浅显易懂。而且还有[中文版](https://studygolang.gitbook.io/learn-go-with-tests)


9、[pprof](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google/pprof)：Go 语言的性能分析工具，可以用来调试 Go 程序的内存泄露、goroutine 泄露之类的问题。使用方法：
```
# 安装
$ go get -u github.com/google/pprof
# 生成一个profile文件
$ pprof -top [你的golang程序二进制文件] profile.pb.gz
# 生成火焰图
$ pprof -web [你的golang程序二进制文件] profile.pb.gz
```


### Java
10、[Luban](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Curzibn/Luban)：图片压缩是常见的问题，那么微信是如何处理图像的压缩？Luban（鲁班）就是通过在微信朋友圈发送近 100 张不同分辨率的图片，对比原图与微信压缩后的图片逆向推算出来的压缩算法。示例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/64054478.png' style="max-width:80%; max-height=80%;"></img></p>

11、[yacy_search_server](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yacy/yacy_search_server)：一款采用了新的搜索方法的搜索引擎软件。 它不需要中央服务器，但它搜索的结果来自于独立的分布式网络。在这样的分布式网络中，没有任何一个实体可以决定列出的内容或结果出现的顺序。启动和关闭的方法：
- GNU/Linux 系统，启动：`./startYACY.sh`、关闭：`./stopYACY.sh`
- Windows 系统，启动：双击`startYACY.bat`、 关闭：双击`stopYACY.bat`
- Mac OS X 系统，请使用 Mac 应用程序，并像其他 Mac 应用程序那样启动或停止它（双击）


### JavaScript
12、[griffith](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zhihu/griffith)：让流式播放变得简单。无论你视频格式是 `mp4` 还是 `hls`，Griffith 都能使用媒体源拓展（MSE）来实现分段加载等功能，提供在线视频播放。示例代码：
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


13、[makegirlsmoe_web](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/makegirlsmoe/makegirlsmoe_web)：动漫角色图片生成工具。支持：选择发色、发型、眼睛、皮肤、微笑、风格等等特征生成二次元图片。自定义生成可爱的二次元头像，二次元界福音。[在线尝试](https://make.girls.moe/#/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/97284537.png' style="max-width:80%; max-height=80%;"></img></p>

14、[ncform](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ncform/ncform)：只需要配置相关参数，便可方便生成表单的UI组件，自带校验规则满足日常 90% 的要求。表单是 Web 应用中常见的组件，但是开发表单是一个重体力活，ncform 通过配置便可生成表单，极大的提高了开发效率


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/140506352.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[vscode-leetcode](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LeetCode-OpenSource/vscode-leetcode)：这是一个可以让用户在 VS Code 编辑器中，练习 LeetCode 习题的插件。支持：查看高票解答、提交答案、测试答案等。提高了刷题效率，助你在校招、社招中杀出重围。上班摸鱼刷题利器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/121125679.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[Web](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/qianguyihao/Web)：前端入门的图文教程，从 0-1 的过程。内容详细，对于新入行前端的同学有很多的帮助


### Objective-C
17、[BackgroundMusic](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kyleneideck/BackgroundMusic)：macOS 音频工具，包含功能：自动暂停音乐、设置各个应用程序的音量、录制系统音频


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/52422583.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP
18、[PasteMe](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LucienShui/PasteMe)：快速分享文本、代码的网站项目。支持加密、一键复制、永久保存、阅后即焚等功能。[在线示例](https://pasteme.cn/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/144435465.png' style="max-width:80%; max-height=80%;"></img></p>

19、[php-console](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/inhere/php-console)：使用简单，功能全面的 PHP 命令行应用库。提供控制台参数解析、命令运行、颜色风格输出、 用户信息交互等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/84031519.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
20、[awesome-python-login-model](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Kr1s77/awesome-python-login-model)：该项目收集了各大网站登陆方式和部分网站的爬虫程序。登陆方式实现包含 selenium 登录、通过抓包直接模拟登录等。有助于新手研究、编写爬虫


21、[better-exceptions](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Qix-/better-exceptions)：更加友好、实用、漂亮的输出 Python 异常


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/84720080.png' style="max-width:80%; max-height=80%;"></img></p>

22、[dash](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/plotly/dash)：一款只用几百行 Python 代码就可以轻易实现数据分析可视化的利器，是目前 Python 社区数据可视化主要的工具之一。具有：使用简单、易于扩展、开发团队活跃等特点


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/33702544.gif' style="max-width:80%; max-height=80%;"></img></p>

23、[ds-cheatsheets](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/FavioVazquez/ds-cheatsheets)：Python 在数据科学方面使用库的速查表，包含了 Pandas、Jupyter、SQL、Dask 等。虽然都是些基本的 API 调用，但是用来备忘和速查足以


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/162608338.png' style="max-width:80%; max-height=80%;"></img></p>

24、[gita](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nosarthur/gita)：基于 Python 开发的管理 git 工具，使用后可在任何目录下代理执行 git 指令。同时支持同时显示多个 repo 的状态信息、本地分支与远程分支的关系等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/119705647.png' style="max-width:80%; max-height=80%;"></img></p>

25、[pylane](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NtesEyes/pylane)：一个基于 gdb 的 Python 进程注入和调试工具。通过 gdb trace Python 进程，然后在该进程的 Python vm 中动态地注入一段 Python 代码， 从而对一个运行中的 Python 进程执行一段任意的逻辑。更多 Python 调试经验，可阅读这篇[文章](https://mp.weixin.qq.com/s/Mlhrp2E390EMD0ZfSaNFKw)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/127239283.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[scrapydweb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/my8100/scrapydweb)：Scrapy 爬虫管理平台，支持：Scrapyd 集群管理、日志可视化、定时任务、邮件通知、移动端 UI


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/150997854.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby
27、[jekyll](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jekyll/jekyll)：强大的静态博客网站生成工具。无需数据库，可以通过 Markdown 和 Config 轻松生成一个静态博客。该项目十分成熟、社区活跃、拥有多种主题可供选择。最后可以通过 [GitHub Page](https://pages.github.com/) 把生成的博客免费部署上线。快速开始：
```
1. 安装 jekll：gem install bundler jekyll
2. 创建项目：jekyll new my-awesome-site
3. 进入新创建的项目：cd my-awesome-site
4. 本地运行：bundle exec jekyll serve
5. 本地访问地址：http://localhost:4000
```


### Swift
28、[Bagel](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yagiz/Bagel)：一个小型、原生的 iOS 网络调试工具。使用过程不需要配置证书、代理之类的东西。只需要 iOS 设备和 Mac 处于同一网络，就可以查看、监控 App 的网络流量等信息


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/91084289.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
29、[BigGAN-PyTorch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ajbrock/BigGAN-PyTorch)：“Bye Bye TPU”，4 个 GPU 就能训练“史上最强” BigGAN！只需 4-8 个 GPU 即可训练，摆脱了算力束缚


30、[faceswap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/deepfakes/faceswap)：这个工具可以对图片和视频进行换脸。可以很方便地处理图片和视频，搞些有意思的事情


31、[GNNPapers](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/thunlp/GNNPapers)：自从卷积神级网络面世以来，大部分人将其应用在规则的空间结构数据当中，比如图像。但是现实中存在更多的并不具备规则的空间结构的数据，因此研究人员提出了处理这部分数据的网络模型-GNN。该项目列举了 GNN 方面的论文，较为全面，适合有一定基础的人阅读


32、[QuickDraw](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vietnh1009/QuickDraw)：谷歌开发的一个流行的在线游戏，神经网络会猜测你在画什么。神经网络从每幅图画中学习，提高正确猜测涂鸦内容的能力。现在你可以基于这个仓库，用 Python 构建自己的 Quick Draw 游戏


33、[Virgilio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/virgili0/Virgilio)：本资源库旨在为以下领域提供三种有机完整的学习路径：机器学习、商业智能、云计算。在此你将能够了解相关原理并且在项目实践中予以运用。如果仔细遵循这些学习路径，则可以从零开始构建完整的认识和获得始终可用的技能。事实上，这些学习路径不需要之前有相关知识，但基础编程和简单数学是理解和实践大多数相关概念的必要条件


### Other
34、[ChinaMobilePhoneNumberRegex](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/VincentSit/ChinaMobilePhoneNumberRegex)：一组匹配中国大陆手机号码的正则表达式


35、[ChromeAppHeroes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zhaoolee/ChromeAppHeroes)：优秀、实用的 Chrome 插件集合。该项目还包含插件的中文的使用介绍，为的是让好的插件被更多人发现和使用


36、[FiraCode](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tonsky/FiraCode)：Free Open Source Font to Enhance Code Aesthetics. This is an open-source monospaced font specifically designed for programmers. Its core charm lies in the unique 'programming ligatures' feature. It can intelligently automatically combine multiple common symbols in code (such as!= or =>) into a single, easy-to-read symbol, making your code look more tidy and elegant visually.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/26500787.png' style="max-width:80%; max-height=80%;"></img></p>

37、[howto-make-more-money](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/easychen/howto-make-more-money)：该项目介绍了程序员如何挣零花钱的姿势


38、[translations](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/oldratlee/translations)：一些不错的英文资料、文章翻译项目


39、[web-frameworks](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/the-benchmarker/web-frameworks)：该项目展示了不同编程语言的 Web 框架性能对比，持续更新。可以作为挑选 Web 框架的参照信息


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/36/86350964.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
40、[Go42](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ffhelicopter/Go42)：《Go语言四十二章经》Golang 入门书籍。书中作者总结了自己踩坑的经验总结和思考，[在线阅读](https://github.com/ffhelicopter/Go42/blob/master/SUMMARY.md)


41、[PythonDataScienceHandbook](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jakevdp/PythonDataScienceHandbook)：英文原版《Python Data Science Handbook》，该书对于希望或已经从事数据科学相关工作的 Python 工程师而言是重要的学习手册。[在线阅读](https://jakevdp.github.io/PythonDataScienceHandbook/)




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub35.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub37.md">『Next』</a>
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
