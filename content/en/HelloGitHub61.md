# HelloGitHub Vol.61
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
1、[acwj](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/DoctorWkt/acwj)：教你写 C 语言编译器的实战教程。教程注重实战循序渐进，一步步教你如何用 C 语言写一个可以自己编译自己（自举）、能够在真正的硬件上运行的 C 语言编译器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/215973962.png' style="max-width:80%; max-height=80%;"></img></p>

2、[zstd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/facebook/zstd)：快速、无损的数据压缩算法 Zstandard 的实现。Zstd 的压缩比接近 lzma、lzham 和 ppmx，并且比 lza 或 bzip2 性能更好。在相似的压缩比情况下，它解压缩的速度比其他的算法都要快。很多知名项目和游戏都有这个算法的身影，示例代码：
```c
static void compress_orDie(const char* fname, const char* oname)
{
    size_t fSize;
    void* const fBuff = mallocAndLoadFile_orDie(fname, &fSize);
    size_t const cBuffSize = ZSTD_compressBound(fSize);
    void* const cBuff = malloc_orDie(cBuffSize);

    /* Compress.
     * If you are doing many compressions, you may want to reuse the context.
     * See the multiple_simple_compression.c example.
     */
    size_t const cSize = ZSTD_compress(cBuff, cBuffSize, fBuff, fSize, 1);
    CHECK_ZSTD(cSize);

    saveFile_orDie(oname, cBuff, cSize);

    /* success */
    printf("%25s : %6u -> %7u - %s \n", fname, (unsigned)fSize, (unsigned)cSize, oname);

    free(fBuff);
    free(cBuff);
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/29759715.jpeg' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[Files](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/files-community/Files)：一个全新的文件管理器。采用 Fluent Design 和 Windows 平台最新的 API 实现，简约但不简单


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/164140756.png' style="max-width:80%; max-height=80%;"></img></p>

4、[ravendb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ravendb/ravendb)：一款快速、可靠的开源 NoSQL 数据库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/542714.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
5、[algorithm-pattern](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/greyireland/algorithm-pattern)：LeetCode 刷题集合项目。项目从 Go 语言入门讲起，总结了一套刷题模板和解题套路，示例代码为 Go 语言


6、[chanify](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chanify/chanify)：基于 Go 实现的向 iOS 设备推送消息的服务。手机上安装好配套的 iOS 应用，然后以 Docker 的方式部署完服务，就可以通过一条命令推送指定消息到 APP 上，是不是很方便吖
```
# 发送文本消息
$ curl --form-string "text=hello" "http://<address>:<port>/v1/sender/<token>"

# 发送文本文件
$ cat message.txt | curl -H "Content-Type: text/plain" --data-binary @- "http://<address>:<port>/v1/sender/<token>"
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/342322079.png' style="max-width:80%; max-height=80%;"></img></p>

7、[ebiten](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hajimehoshi/ebiten)：Go 语言的 2D 游戏引擎库。通过它可以轻松地用 Go 语言制作出支持多平台的 2D 游戏，项目中还包含很多示例代码，帮助你快速上手


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/10721619.png' style="max-width:80%; max-height=80%;"></img></p>

8、[imaging](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/disintegration/imaging)：Go 语言的图像处理库。支持：调整大小、旋转、剪切、亮度调整等功能，示例代码：
```go
// 调整
dstImage128 := imaging.Resize(srcImage, 128, 128, imaging.Lanczos)
// 锐化
dstImage := imaging.Sharpen(srcImage, 0.5)
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/7042338.png' style="max-width:80%; max-height=80%;"></img></p>

9、[jql](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cube2222/jql)：用 Go 写的 JSON 数据查询工具。该工具安装方便，语法简单容易上手，实用示例代码很多比如：
```
# 查询 test.json 文件中，所有国家的名称
cat test.json | jql '(elem "countries" (elem (keys) (elem "name")))'
[
  "Poland",
  "United States",
  "Germany"
]
```


### Java
10、[flink-recommandSystem-demo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/water8394/flink-recommandSystem-demo)：一个基于 Flink 实现的商品实时推荐系统。可以通过这个项目了解和学习推荐系统的设计和流程，该系统是通过 Flink 处理日志和统计商品热度，将处理好的数据放入 Redis 缓存。然后再将画像标签和实时记录放入 HBase。在用户请求获取推荐时，根据用户画像生成商品热度榜，并结合协同过滤和标签两个推荐模块，返回最终生成的商品推荐列表


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/186777581.png' style="max-width:80%; max-height=80%;"></img></p>

11、[jacoco](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jacoco/jacoco)：Java 代码测试覆盖率库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/4950187.png' style="max-width:80%; max-height=80%;"></img></p>

12、[kooder](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/oschina/kooder)：一个开源的代码搜索服务。为包括 GitLab、Gitea 的代码托管系统提供源码、仓库、Issue 的搜索服务


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/345917142.png' style="max-width:80%; max-height=80%;"></img></p>

13、[OpenRefine](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/OpenRefine/OpenRefine)：一款用于清理数据的桌面工具。通过可视化的方式分析、整理数据，支持 Windows、Linux、Mac 操作系统。拥有查询、过滤、去重、分析等功能，可以把杂乱的数据变成“整洁”的电子表格，还能够将结果导出成多种格式的文件。不会编程和 SQL 的小伙伴们，也可以轻松分析海量数据啦！


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/6220644.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
14、[drawio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jgraph/drawio)：一款简洁强大的绘图工具。免费开源可以自行部署也可以[在线使用](https://app.diagrams.net/)，功能上直追 Microsoft Visio。支持流程图、序列图、网络拓扑图、甘特图、思维导图、模型图等，还能导出多种格式类型比如 png、svg、PDF、HTML 和 VSDX 格式（Microsoft Visio 图形格式）


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/67508428.png' style="max-width:80%; max-height=80%;"></img></p>

15、[kutt](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/thedevs-network/kutt)：免费开源的短链接服务。服务基于 Node.js+Express+React 实现，支持管理链接、自定义短链接、设置链接密码、访问统计等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/121380371.png' style="max-width:80%; max-height=80%;"></img></p>

16、[nav](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xjh22222228/nav)：一个支持 SEO 的静态导航网站。不依赖后端的纯前端项目开箱即用，简单清爽


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/131143048.png' style="max-width:80%; max-height=80%;"></img></p>

17、[npkill](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/voidcosmos/npkill)：快速查找和轻松删除 node_modules 文件夹的工具。还在为 node_modules 占了很多磁盘空间而烦恼吗？还在手动找用不到的 node_modules 目录吗？快来试试 npkill 吧！轻松地删除 node_modules 目录


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/194513266.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[taro](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cloud9c/taro)：一款 Web 轻量级的 3D 游戏引擎。底层基于 three.js 和 cannon-es 支持 3D 刚体物理引擎


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/270208710.gif' style="max-width:80%; max-height=80%;"></img></p>

### PHP
19、[question2answer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/q2a/question2answer)：采用 PHP+MySQL 实现的免费开源的问答平台。基本上问答平台该有的功能它都有，那么问题来了是做个知乎还是 Stack Overflow 呢？
- 支持回答投票、评论、最佳回答、关注和关闭问题
- 完备的用户和权限管理
- 多语言支持
- 搜索时的相似问题匹配
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/2916562.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
20、[apkleaks](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dwisiswant0/apkleaks)：扫描 APK 文件是否包含敏感信息的命令行工具
```
// custom-rules.json
{
  "Amazon AWS Access Key ID": "AKIA[0-9A-Z]{16}",
  ...
}
$ apkleaks -f /path/to/file.apk -p rules.json -o ~/Documents/apkleaks-results.txt
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/267958226.jpeg' style="max-width:80%; max-height=80%;"></img></p>

21、[graphene-django](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/graphql-python/graphene-django)：让你轻松地将 GraphQL 整合到 Django 项目的库


22、[tomato-clock](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/coolcode/tomato-clock)：Python 写的命令行番茄工作法定时器。代码仅有 100 多行，不依赖其它第三方库
```
🍅 tomato 25 minutes. Ctrl+C to exit
 🍅🍅---------------------------------------------- [8%] 23:4 ⏰ 
```


23、[vardbg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/CCExtractor/vardbg)：一款能够把 Python 程序执行过程，导出成视频或动图的代码调试工具。可用于动画学算法、制作代码讲解视频等场景


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/233500493.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust
24、[fselect](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jhspetersson/fselect)：用类 SQL 的命令查找文件的命令行工具
```
fselect size, path from /home/user where name = '*.cfg' or name = '*.tmp'
fselect size, abspath from ./tmp where size gt 2g
fselect hsize, abspath from ./tmp where size lt 8k
```


### Swift
25、[awesome-ios](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vsouza/awesome-ios)：超棒的 iOS 开源项目集合。它非常全面包含 Objective-C、Swift 语言的项目，拥有网络、UI、JSON、数据库、音视频等分类，iOS 初学者寻找开源项目的好地方


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/21700699.png' style="max-width:80%; max-height=80%;"></img></p>

26、[Knot](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Lojii/Knot)：一款 iOS 抓包工具。实现了 HTTP(S) 解析、流量解析、多格式导出、证书管理以及过程分析等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/239665453.png' style="max-width:80%; max-height=80%;"></img></p>

27、[SwiftUITodo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/devxoul/SwiftUITodo)：用 SwiftUI 做的 Todo 工具。这是一个示例项目帮助新手掌握 SwiftUI 


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/190091793.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
28、[AI-Expert-Roadmap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AMAI-GmbH/AI-Expert-Roadmap)：人工智能学习路线图


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/306977633.png' style="max-width:80%; max-height=80%;"></img></p>

29、[Real-Time-Person-Removal](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jasonmayes/Real-Time-Person-Removal)：在 Web 浏览器中实时移除人像。该项目采用 JavaScript+TensorFlow.js 实现“凭空消失”


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/241217584.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
30、[cloudmusic-vscode](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/YXL76/cloudmusic-vscode)：网易云音乐 VS Code 插件。基于网易云网页 API 实现，支持：
- 歌曲播放、收藏、喜欢
- 心动模式、私人 FM
- 评论（单曲、歌单...）
- 歌词显示
- 搜索（热搜/单曲/专辑/歌手...）
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/275492724.png' style="max-width:80%; max-height=80%;"></img></p>

31、[LIII](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/aliakseis/LIII)：免费开源的 BT 下载工具。如果你厌倦了广告、购买 VIP 才能提速，只想要一个简单好用的下载工具，那你可以试试这个开源项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/97960048.png' style="max-width:80%; max-height=80%;"></img></p>

32、[shapez.io](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tobspr-games/shapez.io)：一款 Steam 上的模拟建造游戏《异形工厂》的源码。游戏是在无边的地图上开采资源、放置设施、组合图形、相互搭配，扩建自己的异形工厂。游戏轻松但也很有挑战性，快去试一试吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/255365829.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
33、[Probabilistic-Programming-and-Bayesian-Methods-for-Hackers](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)：《黑客的贝叶斯方法：以 Python 为例》


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/61/7607075.png' style="max-width:80%; max-height=80%;"></img></p>

34、[tensorflow-handbook](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/snowkylin/tensorflow-handbook)：《简明的 TensorFlow 2》，[在线阅读](https://tf.wiki/zh_hans/)


35、[The-design-and-implementation-of-a-64-bit-os](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yifengyou/The-design-and-implementation-of-a-64-bit-os)：《一个 64 位操作系统的设计与实现》




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub60.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub62.md">『Next』</a>
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
