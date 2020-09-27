# 《HelloGitHub》第 42 期
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
- [CSS 项目](#CSS-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [教程](#教程)
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
1、[linq4c](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/haifenghuang/linq4c)：如果你想在 C 中使用隔壁 C# 的 linq 方法，那么不妨来使用这个项目！这是它的 C 语言版。实现了 linq 的大部分方法（60+）。现在它还在不断完善中，欢迎更多的小伙伴加入共同维护
```c
bool WhereCallback(void *item) {
    char *str= (char *)item;
    return str[0] == 'h';
}

void *SelectCallback(void *item) {
    return newStr("%s_1", (char *)item);
}

char *str1 = "huang", *str2 = "hai", *str3 = "feng";

ArrayList array = arrlist_new();
arrlist_append(array, str1);
arrlist_append(array, str2);
arrlist_append(array, str3);

Linq *lq = From(array);
ArrayList result = 
    lq
    ->Where(lq, WhereCallback)
    ->Select(lq, SelectCallback)
    ->ToArray(lq);

for(int i = 0; i < arrlist_size(result); i++) {
    printf("%s\n", arrlist_get(result, i));
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/linq4c.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
2、[nebula](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vesoft-inc/nebula)：Nebula Graph 是一款开源图数据库，目标是为超大规模的图数据提供高并发、低延时的读、写及计算服务。目前是世界上唯一能够容纳千亿个顶点和万亿条边、并提供毫秒级查询延时的图数据库解决方案。特点：
- 全对称分布式架构
- 可扩展
- 高可用
- 数据强一致
- 类 SQL 查询语言

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/nebula.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
3、[iCSS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chokcoco/iCSS)：该项目围绕 CSS 话题，讲述了 CSS 相关的技巧、动画实现

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/iCSS.jpg' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
4、[kubesphere](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kubesphere/kubesphere)：一款在主流容器调度平台 Kubernetes 之上构建的企业级分布式多租户容器管理平台。提供简单易用的操作界面以及向导式操作方式，在降低用户使用容器调度平台学习成本的同时，极大降低开发、测试、运维的日常工作的复杂度。[中文文档](https://kubesphere.io/docs/zh-CN/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/kubesphere.png' style="max-width:80%; max-height=80%;"></img></p>

5、[starcharts](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/caarlos0/starcharts)：生成 GitHub 星图的项目

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/starcharts.png' style="max-width:80%; max-height=80%;"></img></p>

6、[ultimate-go](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hoanhan101/ultimate-go)：该项目是作者在学习 Go 过程中，对 Go 源码以及涉及到的相关的计算机基础知识的心得与总结。适合 Go 学习者阅读与学习。快来和作者一起深入了解 Go 源码，了解背后的计算机理论和 Go 的设计思想

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
7、[easyexcel](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alibaba/easyexcel)：使用简单、上手快速、占用内存小且避免内存溢出的 Java 处理 Excel 工具。示例代码：
```java
/**
* 最简单的读
* <p>1. 创建excel对应的实体对象 参照{@link DemoData}
* <p>2. 由于默认异步读取excel，所以需要创建excel一行一行的回调监听器，参照{@link DemoDataListener}
* <p>3. 直接读即可
*/
@Test
public void simpleRead() {
    String fileName = TestFileUtil.getPath() + "demo" + File.separator + "demo.xlsx";
    // 这里 需要指定读用哪个class去读，然后读取第一个sheet 文件流会自动关闭
    EasyExcel.read(fileName, DemoData.class, new DemoDataListener()).sheet().doRead();
}
```

8、[lila](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ornicar/lila)：一款基于 Scala 语言，完全免费、开源、没有广告、支持多语言的在线国际象棋游戏。[在线试玩](https://lichess.org/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/lila.png' style="max-width:80%; max-height=80%;"></img></p>

9、[tablesaw](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jtablesaw/tablesaw)：一款包括数据框和可视化库，可用于加载、转换、过滤和汇总数据的 Java 实用程序。用 Tablesaw 处理数据会节省您的时间和精力，它还支持描述性统计，并且能够与 Smile 机器学习库完美集成。最近两年数据分析师职业大火，做好数据分析，就离不开数据可视化框架。Java 工程师掌握一种数据可视化库势在必行，示例代码：
```java
public class BoxExample {

  public static void main(String[] args) throws Exception {
    Table table = Table.read().csv("../data/tornadoes_1950-2014.csv");

    Layout layout = Layout.builder().title("Tornado Injuries by Scale").build();

    BoxTrace trace =
        BoxTrace.builder(table.categoricalColumn("scale"), table.nCol("injuries")).build();
    Plot.show(new Figure(layout, trace));
  }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/tablesaw.png' style="max-width:80%; max-height=80%;"></img></p>

10、[simple-java-mail](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bbottema/simple-java-mail)：一个轻量级 Java 邮件框架，支持复杂、自定义的发送电子邮件业务。包括经过身份验证的代理、附件、嵌入式图像、自定义标头和属性、强大的地址验证等，亮点是支持身份代理等功能，防止其他其他邮件服务拦截邮件

11、[XUpdate](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xuexiangjys/XUpdate)：一套基于 Android 的全量版本更新整体解决方案。它除了提供 Android SDK 外，还附带了 Spring Boot 搭建的后台服务以及 Vue.js 编写的后台管理界面。主要解决中小企业 Android 版本管理混乱的问题，提供可定制化的解决方案。该框架提供了完全可插拔的版本更新，同时为了让使用者使用方便，还提供了后台服务和管理界面，使用的都是现下最流行的技术。完全做到灵活、方便，并提供了大量丰富的文档供大家参阅
```java
XUpdate.newBuild(getActivity())
.updateUrl(mUpdateUrl)
.isAutoMode(true) // 如果需要完全无人干预、自动更新，需要 root 权限【静默安装需要】
.update();
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/XUpdate.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
12、[star-battle](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gd4Ark/star-battle)：一个使用 JavaScript ES6、Canvas 开发的飞船射击类游戏。[在线试玩](https://4ark.me/star-battle/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/star-battle.jpeg' style="max-width:80%; max-height=80%;"></img></p>

13、[markdown-nice](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mdnice/markdown-nice)：能够自定义样式的 Markdown 编辑器。支持内容和自定义样式浏览器中实时保存、上传图片、脚注、公式等，输出的内容可一件复制到微信公众号、知乎、掘金、博客园和 CSDN 等一系列平台。极大的减轻了微信公众号文章的排版和编辑工作

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/markdown-nice.jpg' style="max-width:80%; max-height=80%;"></img></p>

14、[marktext](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/marktext/marktext)：一个简单且优雅的开源 Markdown 编辑器，支持 Linux、macOS 和 Windows [下载地址](https://github.com/marktext/marktext#download-and-install)。功能：
- 实时预览（所见即所得）和简洁明了的界面
- Markdown 扩展，例如数学表达式和 emoji 表情
- 输出 HTML 和 PDF 文件
- 各种编辑模式：源代码模式、打字机模式、专注模式
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/marktext.png' style="max-width:80%; max-height=80%;"></img></p>

15、[leonsans](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cmiscm/leonsans)：这是一个用 JS 编写的 Sans Serif 半衬线字体。Leon Sans 允许动态更改字体粗细并在 HTML 5 的 Canvas 元素中创建自定义动画、效果或形状，[点击](https://leon-kim.com/)查看动画效果。PS：这个字体是作者来庆祝他刚出生的婴儿 Leon 的哦

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/leonsans.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[taro-music](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lsqy/taro-music)：基于 Taro 与网易云音乐 API 开发的网易云音乐小程序。技术栈为 typescript+taro+taro-ui+redux 目前主要是着重小程序端的展示，可以通过项目学习上述几个技术栈的使用和实战，从而能够快速使用 Taro 开发一个属于你自己的小程序，目前已实现的主要功能点如下：
- 用户登陆
- 我的关注列表
- 最近播放列表
- 歌曲播放页面
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/taro-music.jpeg' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
17、[JHBlog](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SunshineBrother/JHBlog)：该项目整理了作者从初级 iOS 开发到中级的晋级之路的相关知识集合

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
18、[healthchecks](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/healthchecks/healthchecks)：基于 Python3 和 Django2 的 Cron 定时任务监控工具，同时支持多种定时任务失败时的告警方式

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/healthchecks.png' style="max-width:80%; max-height=80%;"></img></p>

19、[GeneralNewsExtractor](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kingname/GeneralNewsExtractor)：基于《基于文本及符号密度的网页正文提取方法》论文用 Python 实现的正文抽取器，可以用来提取 HTML 中正文的内容、作者、标题。之前我看到这篇论文也想实现该抽取工具，但是我因为懒癌晚期躺下了，感谢[kingname](https://github.com/kingname) ‘带趟’ ✌️

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/GeneralNewsExtractor.png' style="max-width:80%; max-height=80%;"></img></p>

20、[bokeh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bokeh/bokeh)：一个交互式的数据可视化 Python 库，专注于在 Web 浏览器中实现美观、直接的数据可视化功能。使用它可以让你快速和轻松地创建交互式图表、仪表板和数据可视化程序。流式数据集的可视化效果如下图：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/bokeh.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
21、[ruby-pinyin](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/janx/ruby-pinyin)：可以把汉字转化为对应的拼音的库，同时能够较好的处理多音字的情况。正确处理多音字，示例代码如下：
```ruby
PinYin.of_string('南京市长江大桥', :unicode)
return ["nán", "jīng", "shì", "cháng", "jiāng", "dà", "qiáo"]

能够正确的将“长”转为“chang2”，而不是“zhang3”
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
22、[EFQRCode](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/EFPrefix/EFQRCode)：一个轻量级的、用来生成和识别二维码的纯 Swift 库，可根据输入的水印图和图标产生艺术二维码

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/EFQRCode.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
23、[reverse-interview](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/viraptor/reverse-interview)：如果当面试官问“你还有什么要问我的吗？”的时候你毫无头绪，那这个项目正是你所需要的。[中文](https://github.com/yifeikong/reverse-interview-zh)

24、[pull](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wei/pull)：一个 GitHub App，它可以让 fork 的仓库自动同步，保持和原仓库同步的神器。很多同学参与开源时会 fork 项目，但无法取得原项目的最新更新。此 Github App 可以很好的解决这个问题，截至目前已有几万仓库使用，截至目前已经自动生成了 70 万个 PR，该数字还在持续增加。注意：如果 master 有更改需要备份后使用，具体见[英文文档](https://github.com/wei/pull#readme)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/pull.png' style="max-width:80%; max-height=80%;"></img></p>

25、[chinese-colors](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zerosoul/chinese-colors)：中国传统颜色在线手册，[在线体验](https://colors.ichuantong.cn/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/chinese-colors.png' style="max-width:80%; max-height=80%;"></img></p>

26、[navi](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/denisidoro/navi)：命令行辅助工具，有了它再也不用担心找不到历史输入过的命令、忘记命令等诸多烦恼

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/navi.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 教程
27、[advanced-java](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/doocs/advanced-java)：一份 Java 工程师进阶知识点集合，内容涵盖：高并发、分布式、高可用、微服务等领域知识。这些知识点不局限于 Java 语言，后端的同学也可以从中收获很多，[在线阅读](https://doocs.github.io/advanced-java)

28、[Nodejs-Roadmap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/qufei1993/Nodejs-Roadmap)：Node.js 技术栈学习指南。内容侧重于 Node.js 服务端，包含：Node.js 基础知识、Node.js 核心模块、主流框架实践、缓存、数据库、消息中间件、DevOps、HTTP 协议以及 Node.js 在微服务等，[在线阅读](https://www.nodejs.red/)

29、[c9-python-getting-started](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/c9-python-getting-started)：微软出品的零基础 Python 入门教程，内容浅显易懂。包含示例代码、演示的 PPT、[配套的 Youtube 视频](https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
30、[ChineseNLPCorpus](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/InsaneLife/ChineseNLPCorpus)：中文自然语言处理数据集

31、[albert_zh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/brightmart/albert_zh)：海量中文预训练 ALBERT 模型

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/42/img/albert_zh.jpeg' style="max-width:80%; max-height=80%;"></img></p>

32、[cherry](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Windsooon/cherry)：简单易用的文本分类器。适用多种语言，自带两个预训练模型，使用预训练模型进行分类只需一行代码。使用自己的数据集进行定制训练也只需要十行代码。轻松达到高精确率，召回率。同时该库支持自定义分词算法、分类算法等。示例代码：
```bash
>>> res = cherry.classify(model='harmful', text=['她们对计算机很有热情，也希望学习到数据分析，网络爬虫，人工智能等方面的知识，从而运用在她们工作上'])
>>> res.word_list
[(2, '她们'), (1, '网络'), (1, '热情'), (1, '方面'), (1, '数据分析'), (1, '希望'), (1, '工作'), (1, '学习'), (1, '从而')]
>>> res.probability
# 返回结果分别对应 赌博，正常，政治，色情 4个 类别的概率
array([[4.43336608e-03, 9.95215198e-01, 3.51419231e-04, 1.68657851e-08]])
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/41/HelloGitHub41.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/43/HelloGitHub43.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
