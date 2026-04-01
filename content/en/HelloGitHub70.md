# HelloGitHub Vol.70
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
1、[daytripper](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dekuNukem/daytripper)：上班摸鱼神器之激光绊脚器。它分为发射器和接收器两部分，设置好后会在有人路过绊脚器时，自动触发隐藏桌面、切换应用等操作


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/144575169.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[tinyssh](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/janmojzis/tinyssh)：极简 SSH 服务器。为了便于学习仅保留了基础功能，而且抛弃了较旧的加密算法。该项目的学习价值大于实用价值，适合对 SSH 和加密知识感兴趣的小伙伴


### C#
3、[.NET-Backend-Developer-Roadmap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Elfocrash/.NET-Backend-Developer-Roadmap)： .NET 后端学习路线图


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/447406555.png' style="max-width:80%; max-height=80%;"></img></p>

4、[LiveCharts2](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Live-Charts/LiveCharts2)：简单、灵活、强大的 .Net 图表库。支持 WPF、WinForms、WinUI、UWP 等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/337897094.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[PDFPatcher](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wmjordan/PDFPatcher)：多功能的 PDF 工具箱，可用于修改 PDF 文件信息。支持：
- 修改、合并 PDF 文档
- 自动生成书签
- 书签编辑器
- 高速无损地导出文件中的图片
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/441460974.png' style="max-width:80%; max-height=80%;"></img></p>

6、[PowerRemoteDesktop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PhrozenIO/PowerRemoteDesktop)：仅用 PowerShell 实现的远程桌面工具。它易于安装和使用、功能齐全，未依赖现有的协议和工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/445545738.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
7、[CGraph](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ChunelFeng/CGraph)：无第三方依赖的 DAG 调度框架。实现了依赖节点依次执行、无依赖节点并发执行的逻辑。项目结构清晰、文档齐全，不仅代码中包含关键注释，还有示例代码和讲解文章。初学者可以通过该项目学到图调度方式、模块开发、模板编程、多线程编程、设计模式和通用算法的知识
```c++
void tutorial_simple() {
    /* 创建一个流水线，用于设定和执行流图信息 */
    GPipelinePtr pipeline = GPipelineFactory::create();
    GElementPtr a, b, c, d = nullptr;

    /**
     * 其中，MyNode1算子的执行内容为sleep(1s)
     * MyNode2算子的执行内容为sleep(2s)
     * 以下几行代码，相当于是设定了一个[b/c]依赖[a]，[d]依赖[b/c]的dag流图
     */
    pipeline->registerGElement<MyNode1>(&a, {}, "nodeA");
    pipeline->registerGElement<MyNode2>(&b, {a}, "nodeB");
    pipeline->registerGElement<MyNode1>(&c, {a}, "nodeC");
    pipeline->registerGElement<MyNode2>(&d, {b, c}, "nodeD");

    /* 执行流图框架 */
    pipeline->process();
    GPipelineFactory::destroy(pipeline);
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/361735570.jpeg' style="max-width:80%; max-height=80%;"></img></p>

8、[oclint](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/oclint/oclint)：强大的静态代码分析工具。可以用来检查 C、C++ 和 Objective-C 代码，发现潜在的 Bug 提高代码质量


9、[timg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hzeller/timg)：在终端查看图片、动图、视频的命令行工具
```
timg some-image.jpg # 展示图片
timg --loops=3 some-animated.gif # 循环展示三次动图
timg some-video.mp4 # 播放视频
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/61416223.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
10、[go-pry](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/d4l3k/go-pry)：Go 语言的交互式 REPL 命令行工具
```
# 安装
go get github.com/d4l3k/go-pry
go install -i github.com/d4l3k/go-pry
# 运行
go-pry -i="fmt,math,strconv"
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/31686893.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[gotests](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cweill/gotests)：自动生成 Go 语言测试代码的工具。该项目基于表驱动测试法（TableDrivenTests）自动生成测试代码，表驱动测试法是创建一张数据表格，每一行为输入和预期输出值，然后用这张表格的数据测试代码


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/49927767.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[gotop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xxxserxxx/gotop)：用 Go 写的系统监控命令行工具。重点是带实时折线图，看起来比较炫酷


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/240037957.gif' style="max-width:80%; max-height=80%;"></img></p>

13、[minio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/minio/minio)：采用 Go 编写的开源对象存储服务。支持存储图片、视频、日志等文件，还拥有方便操作的 Web 管理后台。虽然轻量却有着不错的性能，同时采用 RS code 编码算法实现即使丢失一半的硬盘，依旧可以找回数据。适用于大数据、机器学习等场景
- 高性能：单个文件最大支持 5T，读写速率最高可以达到 55Gb/s 和 35Gb/s
- 可扩展：不同集群可以组合，支持跨越多个数据中心
- 云原生：支持容器化、基于 K8S 的编排、多租户
- 对接多种后端存储：支持 S3、DAS、 NAS、Google 等云存储


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/29261473.png' style="max-width:80%; max-height=80%;"></img></p>

14、[octosql](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cube2222/octosql)：用 SQL 的方式查询多个数据源的命令行工具。支持用 SQL 查询 CSV、JSON 文件和多种数据库中的数据，甚至可以在它们之间自由 JOIN
```
octosql "SELECT * FROM ./myfile.json"
octosql "SELECT * FROM ./myfile.json" --describe  # Show the schema of the file.
octosql "SELECT invoices.id, address, amount
         FROM invoices.csv JOIN db.customers ON invoices.customer_id = customers.id
         ORDER BY amount DESC"
octosql "SELECT customer_id, SUM(amount)
         FROM invoices.csv
         GROUP BY customer_id"
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/173582015.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java
15、[agrona](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/aeron-io/agrona)：提供了用于创建高性能应用的数据结构和实用方法的库。它将 Java 标准库中的数据结构进行包装，避免了 Java 自动装箱。比如提供的队列使用了填充字节的方式，避免头尾结点进入同一缓冲行，来提高队列出队入队的性能。整个项目代码量不多注释完善、代码风格清晰，抛开使用来讲也是一个值得学习的项目


16、[maven-mvnd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/apache/maven-mvnd)：Apache Maven 团队开源的更快的构建工具。因为内嵌了 Maven 所以可以丝滑地从 Maven 切换为 mvnd，而且它相较于 Maven 启动速度更快、使用的内存更少、编译花费的时间更少


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/210029529.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[momo-code-sec-inspector-java](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/momosecurity/momo-code-sec-inspector-java)：Java 静态代码安全审计工具。它能够在编码过程中发现潜在的安全风险，并提供一键修复的功能，可在 IDEA 的插件市场安装


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/302571472.png' style="max-width:80%; max-height=80%;"></img></p>

18、[thumbnailator](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/coobird/thumbnailator)：Java 的缩略图生成库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/39673913.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
19、[js-sdsl](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/js-sdsl/js-sdsl)：实用的 JavaScript 数据结构库。实现了 LinkList、Queue、Set、Map 等数据结构，严格的单元测试提供了正确性和性能的保证，可用于各种需要用到高级数据结构的场景
```html
<script src="https://zly201.github.io/js-sdsl/js-sdsl.min.js"></script>
<script>
    const { Vector } = sdsl;
    const myVector = new Vector();
    // you code here...
</script>
```


20、[lottery](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/moshang-ax/lottery)：年会抽奖程序。基于 Express + Three.js 的 3D 球体抽奖项目，能够自定义文字、图片和抽奖规则，还支持一键导入抽奖人员和导出抽奖结果


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/168259404.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[mometa](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/imcuttle/mometa)：前端代码可视化编辑器。一款低代码辅助开发的工具，可通过拖拽的方式构建和编辑页面。特性：
- 🛠 直接作用于源码，支持移动端布局
- 🍒 开放物料生态，可定制团队内物料库
- 🌟 无缝兼容接入，不破坏已有项目开发模式


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/430673290.png' style="max-width:80%; max-height=80%;"></img></p>

22、[resume](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/visiky/resume)：在线简历生成器。轻松实现在线简历，支持在线预览、编辑和下载 PDF 简历。[在线尝试](https://visiky.github.io/resume/?mode=edit)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/85487142.png' style="max-width:80%; max-height=80%;"></img></p>

23、[shepherd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shipshapecode/shepherd)：用来引导用户浏览网站的 JavaScript 库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/15246993.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C
24、[Stay](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shenruisi/Stay)：移动端 Safari 浏览器插件管理器。提供了丰富的脚本管理能力，还支持运行油猴插件。内置的脚本库提供了 App 防跳转、广告拦截、自动展开文本等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/420680322.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP
25、[dootask](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kuaifan/dootask)：在线项目管理平台。功能包括任务分配、文档协作、即时 IM、文档协作、文件管理等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/400984450.png' style="max-width:80%; max-height=80%;"></img></p>

26、[esupdater](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/WGrape/esupdater)：基于 Canal 的 ES 增量更新框架。适用于把 MySQL 的增量数据，实时更新到 ES 实现同步更新搜索数据


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/437779131.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
27、[django-grappelli](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sehmaschine/django-grappelli)：美化 Django 默认管理后台界面的库
```
# 安装
pip install django-grappelli
# 设置 settings.py 文件
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
)
# 增加路径
urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls), # admin site
]
# 增加请求处理器
TEMPLATES = [
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.request',
                ...
]
# 最后
python manage.py collectstatic
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/580566.png' style="max-width:80%; max-height=80%;"></img></p>

28、[Hitomi-Downloader](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/KurtBestor/Hitomi-Downloader)：Python 写的桌面下载工具。界面简单使用方便，拥有下载限速、BT 种子、自动提取网页视频等功能，支持下载国内多个视频网站的内容


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/112070198.png' style="max-width:80%; max-height=80%;"></img></p>

29、[trzsz](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/trzsz/trzsz)：简单实用的文件传输工具。支持 tmux 和 iTerm2 一起使用，并且有显示上传/下载进度的进度条


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/436126869.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby
30、[fastlane](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fastlane/fastlane)：一款专为 iOS 和 Android 开发者提供自动化构建的工具。它上手简单使用方便，能够帮助开发者自动完成 App 打包、签名、测试、发布、提交到 App Store、Google Play 等工作，实现一条命令发布应用
```
lane :beta do
  increment_build_number
  build_app
  upload_to_testflight
end
lane :release do
  capture_screenshots
  build_app
  upload_to_app_store       # 上传截图和应用到应用商店
  slack                     # 发布完成回调通知
end
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/27442967.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
31、[iGlance](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/iglance/iGlance)：macOS 状态栏系统监视器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/135611480.png' style="max-width:80%; max-height=80%;"></img></p>

32、[SwiftPamphletApp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ming1016/SwiftPamphletApp)：一款免费开源的 Swift 手册工具。能够帮助开发者方便地查看 Swift 语法和常用库的使用指南，除此之外还可以接收 Swift 开源库的动态


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/427532379.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
33、[JetBrainsMono](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/JetBrains/JetBrainsMono)：JetBrains 为开发者开源的免费字体。该字体形状简单没有不必要的细节，从而阅读起来十分轻松而且小尺寸时显示更加清晰


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/173314762.png' style="max-width:80%; max-height=80%;"></img></p>

34、[m-cli](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rgcr/m-cli)：macOS 命令行工具。实现在终端用简短命令的方式操作 macOS 系统，比如管理蓝牙、打开 Wi-Fi、清空废纸篓、操作 iTunes 等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/62925253.png' style="max-width:80%; max-height=80%;"></img></p>

35、[one-html-page-challenge](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Metroxe/one-html-page-challenge)：单个 HTML 页面的挑战。该项目汇集了满足仅有一个 HTML 文件、小于 1MB、不可接入 API、不能引用库条件下实现的创意网页。[在线查看](https://onehtmlpagechallenge.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/194445383.png' style="max-width:80%; max-height=80%;"></img></p>

36、[realworld](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/realworld-apps/realworld)：该项目汇集了不同技术栈的实战项目。这里有采用不同编程语言框架，实现相同功能内容网站的项目代码。例如用 Vue.js+Django 开发包含注册、登录、发布文章、标签、评论等功能的网站，让你通过简单但完整的实战项目，快速上手新的技术栈，消除刚接触某个技术时的手足无措。[点击查看](https://codebase.show/projects/realworld)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/52631841.gif' style="max-width:80%; max-height=80%;"></img></p>

37、[WhiteSur-gtk-theme](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vinceliuice/WhiteSur-gtk-theme)：仿苹果 Big Sur 风格的 GTK 主题


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/70/279638102.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
38、[rust-course](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sunface/rust-course)：《Rust 语言圣经》涵盖了 Rust 语言从入门到精通的全部知识。该书目前还未完成，正处于积极更新的状态。[在线阅读](https://book.rust.team)


39、[safe-rules](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Qihoo360/safe-rules)：由 360 质量工程部开源的《代码安全规则集合》。一份全面详细的 C/C++ 编程规范指南，适用于桌面、服务端以及嵌入式等软件开发




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub69.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub71.md">『Next』</a>
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
