# 《HelloGitHub》第 39 期
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

🎉 最后 [HelloGitHub](https://hellogithub.com) 这个项目就诞生了 🎉

---
> **以下为本期内容**｜每个月 **28** 号发布最新一期｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub#内容)

#### C# 项目
1、[FreeSql](https://github.com/2881099/FreeSql)：一个功能强大的 C# 对象关系映射程序（ORM），支持 .NETCore 2.1+、.NETFramework 4.5+ 开发模式下，开箱即用，可繁可简的使用方式。支持 CodeFirst 迁移、丰富的表达式函数、支持多种数据库、大量采用 ExpressionTree 技术提升性能等功能。示例代码：
```csharp
var t0 = fsql.Select<Tag>()
    .Where(a => a.Parent.Parent.Name == "粤语")
    .IncludeMany(a => a.Tags, then => then.Where(sub => sub.Name == "xxx"))
    .ToList();

var t3 = fsql.Select<Xxx>()
    .Where(a => a.IsDelete == 0)
    .WhereIf(keyword != null, a => a.UserName.Contains(keyword))
    .WhereIf(role_id > 0, a => a.RoleId == role_id)
    .Where(a => a.Nodes.AsSelect().Any(t => t.Parent.Id == t.UserId))
    .Count(out var total)
    .Page(page, size)
    .OrderByDescending(a => a.Id)
    .ToList()
```

#### C++ 项目
2、[pprint](https://github.com/p-ranav/pprint)：一个让输出变得更漂亮的 C++ 库。就像 python 语言的 pprint 库，它对基本类型、字符串、复数、enum 类型、STL 容器等做了输出格式优化，有了缩紧和分行才更容易发现这个世界的美好。示例代码如下：
```c++
#include <pprint.hpp>
printer.print(std::map<std::string, std::set<int>>{{"foo", {1, 2, 3, 3, 2, 1}}, {"bar", {7, 6, 5, 4}}});

// 输出结果如下
{
  "bar" : {4, 5, 6, 7}, 
  "foo" : {1, 2, 3}
}
```

3、[marksencent](https://github.com/Gltina/marksencent)：这是一个在托福听力中标记句子的工具（即精听工具）。在听力时可文本对照，并且对听力音频中没听懂片段进行标记，并选择标记理由，方便日后的反复复习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/marksencent.gif' style="max-width:80%; max-height=80%;"></img></p>

#### CSS 项目
4、[RemixIcon](https://github.com/Remix-Design/RemixIcon)：一套免费、可商用、设计精美、细致的图标库。看到它第一眼后，我感觉自己之前用的图标简直就是枯草🙈。这个项目可以让开发者、设计师在一个图标库中快速找到适合的图标，用于自己的网站或 APP 开发。不同于混搭收集的图标库，RemixIcon 的每一枚图标都是由设计师精心设计而成，并且每一枚图标都包含填充和描边两种风格，便于切换使用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/RemixIcon.png' style="max-width:80%; max-height=80%;"></img></p>

#### Go 项目
5、[olivia](https://github.com/olivia-ai/olivia)：一个类似 Siri 的开源语音助手，目前只支持英文。开源的语音助手并不多，而且涉及的问题很复杂，现在有了它就可以基于这个项目做一些有趣的小应用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/olivia.png' style="max-width:80%; max-height=80%;"></img></p>

6、[goalert](https://github.com/target/goalert)：一个基于 Go 语言实现的报警和处理报警系统。它以发请求或者手动添加方式进行告警，支持短信、电话、发邮件等通知方式。集成了一个看板，基本上算是开箱即用。安装命令如下：
```
docker run -it --rm -p 8081:8081 goalert/all-in-one
访问本地 8081 端口，用户名 admin，密码 admin123
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/goalert.png' style="max-width:80%; max-height=80%;"></img></p>

7、[geziyor](https://github.com/geziyor/geziyor)：Go 的分布式爬虫框架。示例代码：
```go
func main() {
    geziyor.NewGeziyor(&geziyor.Options{
        StartURLs: []string{"http://quotes.toscrape.com/"},
        ParseFunc: quotesParse,
// exporter 可以用来把最终结果存成各种格式，例如 json
        Exporters: []geziyor.Exporter{exporter.JSONExporter{}},
    }).Start()
}

// 请求的结果直接进了一个管道处理函数，这样的函数可以串联起来，爬虫和清洗二合一
// 这样拆分爬虫逻辑，某些逻辑也可以重用
func quotesParse(g *geziyor.Geziyor, r *geziyor.Response) {
    r.HTMLDoc.Find("div.quote").Each(func(i int, s *goquery.Selection) {
        g.Exports <- map[string]interface{}{
            "text":   s.Find("span.text").Text(),
            "author": s.Find("small.author").Text(),
        }
    })
    if href, ok := r.HTMLDoc.Find("li.next > a").Attr("href"); ok {
        g.Get(r.JoinURL(href), quotesParse)
    }
}
```

8、[script](https://github.com/bitfield/script)：一个封装好的 OS 三方库，解决了 Go 使用 OS 标准库错误处理的麻烦。如果没有它，打开一个文件查找一个关键字再统计下数量，你至少会需要 2-3 个异常处理的逻辑。有了它，只需要：
```go
numErrors, err := script.File("test.txt").Match("Error").CountLines()
// 等同于 grep Error test.txt | wc -l
```

9、[unioffice](https://github.com/unidoc/unioffice)：一个让 Go 可以创建、操作 Office Word、Excel、Powerpoint 三件套的库。示例代码：
```go
dox := document.New()
doc.X().Background = wordprocessingml.NewCT_Background()
doc.X().Background.ColorAttr = &wordprocessingml.ST_HexColor{}
doc.X().Background.ColorAttr.ST_HexColorRGB = color.RGB(50, 50, 50).AsRGBString()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/unioffice.png' style="max-width:80%; max-height=80%;"></img></p>

#### Java 项目
10、[Java](https://github.com/TheAlgorithms/Java)：一份算法清单，详细演示了 Java 中内置的算法实现。如果你想要知道平时使用 Java 时，Java 的内置算法如何帮你处理任务，那么这个项目值得一读。此外，这份清单中还用到了配图来帮助你理解

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/Java.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[Linkage-RecyclerView](https://github.com/KunMinX/Linkage-RecyclerView)：一款基于 MVP 架构开发的二级联动列表控件，高度解耦、轻松配置、使用方便。依托于 MVP 的 “配置解耦” 特性，使用者无需知道内部的实现细节，仅通过实现配置类即可完成功能的定制和扩展。此外，在不设置自定义配置的情况下，最少只需一行代码即可运行起来

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/Linkage-RecyclerView.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[SmoothRefreshLayout](https://github.com/dkzwm/SmoothRefreshLayout)：一个高效、强大的 Android 刷新库。支持越界回弹、二级刷新、横向刷新、拉伸回弹、类QQ下拉回弹效果等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/SmoothRefreshLayout.gif' style="max-width:80%; max-height=80%;"></img></p>

#### JavaScript 项目
13、[wechat-format](https://github.com/lyricat/wechat-format)：公众号文章的排版真是让人头大，还好有这个微信公众号排版编辑器。便捷地把 Markdown 内容转换成微信特定的 HTML 内容，然后粘贴到公众号的编辑后台就完活了。虽然不是特别美观，但是节省了很多时间，[在线尝试](https://lab.lyric.im/wxformat/)

14、[fe-interview](https://github.com/haizlin/fe-interview)：每天早上 4 个基础前端面试题，助你在前端面试中‘所向披靡’，无人能挡

15、[AutoPiano](https://github.com/WarpPrism/AutoPiano)：自由钢琴（AutoPiano）是利用 HTML5 技术开发的在线钢琴应用。在学习工作之余可以享受钢琴、音乐的美好，支持钢琴曲的自动播放功能、按键提示。让学习钢琴变得简单，谁都可以练成‘钢琴手’，[在线体验](http://www.autopiano.cn/)

16、[HitUP](https://github.com/wonderbeyond/HitUP)：一款发现 Top 系列的 Chrome 扩展。它会替换掉浏览器默认的 New Tab 空白页面，助你保持对流行技术趋势的跟进。核心功能是展示 GitHub 上近期最流行的项目，并会围绕 “Find top things” 的主题谨慎添加新特性，让你对新技术和新事物‘了如指掌’

17、[filepond](https://github.com/pqina/filepond)：一个 JavaScript 文件上传库。可以上传拖入的任何内容，具有体积小、上传快、方便的文件管理等特点，从而让用户享受‘丝滑’般的文件上传体验

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/filepond.gif' style="max-width:80%; max-height=80%;"></img></p>

#### Objective-C 项目
18、[OpenEmu](https://github.com/OpenEmu/OpenEmu)：在 macOS 系统上回味下童年时的游戏，一个可以玩各种复古游戏的游戏机

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/OpenEmu.png' style="max-width:80%; max-height=80%;"></img></p>

#### PHP 项目
19、[FreshRSS](https://github.com/FreshRSS/FreshRSS)：一个 PHP 写的免费自托管 RSS 阅读器（free and free），据说上万条订阅都不带卡顿。可分配多账户、支持第三方安卓、iOS 客户端、支持 FEVER API 协议，与 Rsshub 搭配使用，完美解决 RSS 重度用户的痛点。是 RSS 爱好者的福音和神器

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/FreshRSS.png' style="max-width:80%; max-height=80%;"></img></p>

#### Python 项目
20、[psutil](https://github.com/giampaolo/psutil)：一个跨平台库的进程和系统资源监控、管理库。用于查看有关正在运行的进程和系统利用率，如 CPU、内存、磁盘、网络等信息。 实现了 UNIX 命令行工具提供的许多功能，例如：ps、top、lsof、netstat、ifconfig 等，支持 Linux、Windows、macOS 等系统。学会了这个库，就可以通过 Python 脚本做更多有趣的事情了。查看内存的代码：
```
>>> psutil.virtual_memory()
svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304)
>>> psutil.swap_memory()
sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
```

21、[manim](https://github.com/3b1b/manim)：一个生成数学教学视频的动画引擎。它用编程的方式创建精美的数学动画，让数学更加易懂。效果如 
 3Blue1Brown 的视频中所展示的那样，效果炫酷。但要学会和用好这个工具需要花些精力

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/manim.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[you-get](https://github.com/soimort/you-get)：一个 Python 写的视频下载工具，下载工具千万个但我仅仅推荐了这个工具。是因为正常情况下载不了视频的网站，用它你就可以方便地下载下来。剩下的要自己去看介绍，不能再多说了🙊
```
(env) ➜  ~ you-get 'https://v.ifeng.com/c/7msWmwppMPC'
Site:       ifeng.com
Title:      完整版第五期：陈晓卿 中国有俩行当门槛极低——美食圈和摄影圈
Type:       MPEG-4 video (video/mp4)
Size:       0.01 MiB (8578 Bytes)

Downloading 完整版第五期：陈晓卿 中国有俩行当门槛极低——美食圈和摄影圈.mp4
 100% (  0.0/  0.0MB) ├████████████████████┤[1/1]   71 kB/s

```

23、[arrow](https://github.com/crsmithdev/arrow)：还在为处理时间、时区、转化、夏令时等问题而头疼吗？这个 Python 的第三方时间库。提供了更便捷的方式来创建、操作和格式化时间和日期，用更少的代码来处理时间和日期。示例代码：
```
>>> import arrow
>>> utc = arrow.utcnow()
>>> utc
<Arrow [2013-05-11T21:23:58.970460+00:00]>

>>> utc = utc.replace(hours=-1)
>>> utc
<Arrow [2013-05-11T20:23:58.970460+00:00]>

>>> local = utc.to('US/Pacific')
>>> local
<Arrow [2013-05-11T13:23:58.970460-07:00]>

>>> arrow.get('2013-05-11T21:23:58.970460+00:00')
<Arrow [2013-05-11T21:23:58.970460+00:00]>

>>> local.timestamp
1368303838
```

24、[GithubMonitor](https://github.com/Macr0phag3/GithubMonitor)：由于很多猪队友的存在，公司敏感信息通过 GitHub 泄露出去是很常见的。这个项目主要根据关键字与 hosts 生成的关键词，利用 GitHub 提供的 API 监控 Git 泄漏，并在检测到信息泄露的时候发送邮件通知

#### Ruby 项目
25、[pagy](https://github.com/ddnexus/pagy)：特别快的 Ruby 分页库。具有效率高、易用、自定义等特性，只需要少量代码就可实现分页。还有丰富文档可够参考，如果你要在 Ruby 程序中实现分页又不想自己费神，那就快试试这个吧

#### Swift 项目
26、[timer-app](https://github.com/michaelvillar/timer-app)：一个 macOS 上简单的计时器软件。拖动蓝色箭头设置时间，当时间到了会显示通知，并发出一个很好的声音

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/timer-app.png' style="max-width:80%; max-height=80%;"></img></p>

#### 其它
27、[ChineseBQB](https://github.com/zhaoolee/ChineseBQB)：表情包资源库，我悄悄的下了好几张，终于可以在群里挺起腰板了

28、[papers-notebook](https://github.com/dyweb/papers-notebook)：论文阅读笔记，包含：分布式、虚拟化、容器、机器学习等方面。可以作为学习计算机部分专业论文的入门资料

29、[most-frequent-technology-english-words](https://github.com/Wei-Xia/most-frequent-technology-english-words)：程序员工作中常见、应知应会的英语词汇列表。该列表中的单词是英语类计算机书籍、文档、文章中高频常见的技术词汇。最终目的是希望程序员结合自身的英语基础，在掌握列表中的词汇后，可以无障碍阅读英语技术文章和文档

30、[fe-necessary-book](https://github.com/ddzy/fe-necessary-book)：该项目主要是分享一些技术书籍，也会不定期分享一些开发者必备的软件、工具包、社区、相亲等程序员相关的资源。放松的时候来看看挺不错的✌️

#### 开源书籍
31、[The-Hacker-Playbook-3-Translation](https://github.com/Snowming04/The-Hacker-Playbook-3-Translation)：《The Hacker Playbook 3》中文翻译版（渗透测试实战红队第三版）

#### 机器学习
32、[awesome-bert](https://github.com/Jiakui/awesome-bert)：与 bert 相关的 nlp 论文、应用、资源集合。紧跟自然语言处理发展前沿，便于加速开展相关研究工作

33、[ImageMiniLab](https://github.com/itisyang/ImageMiniLab)：图像迷你实验室，可进行图像实验、处理、分析。使用 PyQt5 结合 opencv-python 实现代码简洁易读，通过该工具可以快速演示图像算法效果，便于 cv 入门学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/39/img/ImageMiniLab.jpg' style="max-width:80%; max-height=80%;"></img></p>

34、[PyTorch-NLP](https://github.com/PetrochukM/PyTorch-NLP)：简称 torchnlp 是一个支持快速原型设计（包括数据集和神经网络层）的 PyTorch-NLP 工具包。该库封装好了神经网络层、文本处理模块和数据集库，有利于加速自然语言处理研究和实践。示例代码：
```python
# Load a Dataset
from torchnlp.datasets import imdb_dataset

# Load the imdb training dataset
train = imdb_dataset(train=True)
train[0]  # RETURNS: {'text': 'For a movie that gets..', 'sentiment': 'pos'}

# Apply Neural Networks Layers
import torch
from torchnlp.nn import LockedDropout

input_ = torch.randn(6, 3, 10)
dropout = LockedDropout(0.5)

# Apply a LockedDropout to `input_`
dropout(input_) # RETURNS: torch.FloatTensor (6x3x10)
```

35、[xlnet](https://github.com/zihangdai/xlnet)：CMU 全新 XLNet 预训练模型。BERT 带来的影响还未平复，CMU 与谷歌大脑提出的 XLNet 在 20 个任务上的表现超过了 BERT，并在 18 个任务上取得了当前最佳效果。令人激动的是目前 XLNet 已经开放了训练代码和大型预训练模型，这回又有的玩了

36、[deeplearning-models](https://github.com/rasbt/deeplearning-models)：各种深度学习架构、模型和技巧的集合。TensorFlow 和 PyTorch 的各种深度学习架构、模型和技巧的 Jupyter 集合，非常适合学习



---
<p align="center">
    “看完了，还不够？<a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a> | 还不过瘾，那就看看每天更新的前端日报吧 <a href='https://daily.fairyever.com/'><今日前端></a>”<br>
    如果你发现了好玩、有意义的开源项目 <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击这里</a> 分享你觉得有趣的项目。
</p>

## 公众号
最近开了公众号，后续公众号会针对月刊推荐过的内容精选、梳理，做成系列的文章发布。月刊也会同时发布在公众号，便于第一时间阅读。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:70%;"></img><br>
欢迎关注 HelloGitHub 公众号，获取更多开源项目的资料和内容。
</p>

## 声明
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">知识共享署名-相同方式共享 4.0 国际许可协议</a>进行许可。

**欢迎转载，请注明出处和作者，同时保留声明。**
