# HelloGitHub Vol.40
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
1、[SuperWeChatPC](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/anhkgg/SuperWeChatPC)：这是一个超级微信电脑客户端。没错，是超级！因为它不仅是一个微信电脑客户端，还支持以下功能：
- 无限多开
- 消息防撤销
- 语音消息备份
- 等等

项目里还有相关技术内幕的文章链接，快前去学习吧


2、[TDengine](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/taosdata/TDengine)：一个专门针对物联网等行业以及应用监控进行设计优化的大数据平台。它的数据库插入、查询操作比其它的数据库快了 10 倍！消耗的成本也非常低，和其他典型的此类解决方案相比。TDengine 只需要不到 1/5 的计算资源，它还提供了 Java、C/C++、Python、Go、RESTful API 等用于开发的接口。还在为数据的写入、读取、计算的性能发愁吗？有了它相信你的头发存活率会大大提高


### C#
3、[Common.Utility](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/laochiangx/Common.Utility)：项目作者日常工作总结和网上收集、整理的 C# 各式各样的功能类库。类与类之间没有联系，可以单独引用至项目。代码中包含注释，便于使用和学习


### C++
4、[muduo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chenshuo/muduo)：一个依赖 Boost 的非阻塞 IO 和事件驱动 C++ 网络库。实现了对底层系统调用的封装、高性能异步日志的设计、Reactor 多线程并发模式设计、简单的 HTTP 协议的解析。适合开发 Linux 下的多线程服务端应用程序，通过阅读源码还可学习到 C++ 语言、Linux 网络编程等后端知识


### Go
5、[gocui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jroimartin/gocui)：命令行 UI 库。提供了类似 HTML canvas 的 API 用来在终端中绘制 UI，使得内容可以分块展示，甚至可以在某些终端中支持点击事件。如果你想做一个 redis-cli 或者其它炫酷、支持点击事件的命令行 UI 程序。但是又不想陷入手绘 UI 的困境，该库可以帮你解决这些烦恼


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/15625102.png' style="max-width:80%; max-height=80%;"></img></p>

6、[lazydocker](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jesseduffield/lazydocker)：带命令行 UI 的 docker 管理工具。可以通过点点点来管理 docker，却又不需要装 rancher 这样的企业级容器管理平台


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/187335810.png' style="max-width:80%; max-height=80%;"></img></p>

7、[mux](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gorilla/mux)：一个基于 Golang 语言的 HTTP 路由库。由于支持各种正则匹配路由，使得对应处理函数复用率大大提高。相比于 Gin、beego 等框架，这个项目基本上跟标准库的 `http.ServeMux` 和 `mux.Router` 保持一致，比标准库更强大的是它支持的正则匹配路由、自定义保留字段、嵌套路由等功能。示例代码：
```go
func main() {
    r := mux.NewRouter()
    r.HandleFunc("/", HomeHandler)
    r.HandleFunc("/products", ProductsHandler)
    r.HandleFunc("/articles", ArticlesHandler)
    http.Handle("/", r)
}
r := mux.NewRouter()
r.HandleFunc("/products/{key}", ProductHandler)
r.HandleFunc("/articles/{category}/", ArticlesCategoryHandler)
r.HandleFunc("/articles/{category}/{id:[0-9]+}", ArticleHandler)
```


8、[nps](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ehang-io/nps)：一款功能强大、轻量级的内网穿透代理服务器。支持 TCP 和 UDP 流量转发、支持内网 HTTP 代理、内网 socks5 代理、snappy 压缩、站点保护、加密传输、多路复用等功能。拥有 web 图形化管理，集成多用户模式。可以自搭建内网穿透代理服务，用来替代付费的内网穿透服务。又不像其他类似项目依赖命令行，它有图形页面。安装：
```
go get -u github.com/cnlh/nps
go build cmd/nps/nps.go # 服务端程序
go build cmd/nps/npc.go # 客户端程序
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/156084530.png' style="max-width:80%; max-height=80%;"></img></p>

9、[pan-light](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/peterq/pan-light)：基于 Golang + Qt5 的百度网盘不限速客户端。对比之前命令行版本的百度盘客户端，该项目拥有图形界面，更加友好、方便、易于使用，到 [release 页面](https://github.com/peterq/pan-light/releases)下载运行即可使用


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/176963109.png' style="max-width:80%; max-height=80%;"></img></p>

10、[scope](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/weaveworks/scope)：k8s 系列的容器间关系依赖可视化组件，通过图的方式解释微服务之间复杂的相互依赖关系。同类目前只有 scope 对于微服务之间的依赖的 debug 是非常有意义的。由于是用图的方式表示，意味着可以用图算法找最短路径、聚类、把耦合紧密的服务合并。通过计算图密度，还能揭示微服务之间的联系紧密。安装如下：
```
# 安装
sudo curl -L git.io/scope -o /usr/local/bin/scope
sudo chmod a+x /usr/local/bin/scope
scope launch
# 最后访问 http://localhost:4040
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/34659664.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
11、[arthas](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alibaba/arthas)：阿里开源的 Java 诊断工具。当线上出现了奇怪的异常时，无需发版就能截获运行时的数据，包括参数、返回值、异常、耗时等等。上手简单、文档完备、无代码侵入式的可以对正在运行的 jvm 进程进行监控，简单易用的命令行工具。线上出 bug 了，有了 arthas 先喝口咖啡压压惊，问题分分钟定位不是梦


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/146633589.png' style="max-width:80%; max-height=80%;"></img></p>

12、[mall](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/macrozheng/mall)：一套基于 SpringBoot+MyBatis 的电商系统，包括前台商城系统及后台管理系统。功能完备是学习和实践电商的好项目。项目结构：
```
mall
├── mall-common -- 工具类及通用代码
├── mall-mbg -- MyBatisGenerator 生成的数据库操作代码
├── mall-admin -- 后台商城管理系统接口
├── mall-search -- 基于 Elasticsearch 的商品搜索系统
├── mall-portal -- 前台商城系统接口
└── mall-demo -- 框架搭建时的测试代码
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/127988011.png' style="max-width:80%; max-height=80%;"></img></p>

13、[QuestionAnsweringSystem](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ysc/QuestionAnsweringSystem)：一个 Java 实现的人机问答系统，能够自动分析问题并给出候选答案。在 2011 年的美国热门电视智力问答节目《Jeopardy》中，由 IBM 开发的 AI 问答系统 Watson 战胜了人类选手，而 QuestionAnsweringSystem 则是 Watson 的 Java 实现。从今天的眼光去看，它可能已经不够那么智能，不过由于它的简便性和易于部署运行，因此非常适合新手把玩，赶紧去你的应用中集成一个炫酷的智能问答系统吧


14、[wormhole](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/deathearth/wormhole)：一个简单、易用的 API 管理平台。目的是为了降低后端服务开发与前端调用的耦合性，通过该框架使整个项目的开发、协作更加完善。客户端开发人员从管理平台查找需要的接口信息进行调用，服务端开发人员定义好接口后同步到管理平台中，管理平台可以统一对接口的访问设置等。一个让前端和后端能够成为“好朋友”的框架✌️


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/173974328.jpg' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
15、[cdfang-spider](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mengsixing/cdfang-spider)：成都房源统计的数据可视化项目。该项目统计了成都开盘以来所有的房源信息，帮助想在成都买房的同学提供一些可视化的数据分析，比房协网官方的数据更直观，分析更透彻。此项目包含了一套完整的源代码，以及详细的项目搭建文档，开发者可以根据搭建文档一步一步搭建这个项目。可以帮助开发者学习前端，后端，数据库端，单元测试，持续集成等全套知识。基于此项目，你可以做任何地区的房源信息可视化，让数据说话


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/125732193.png' style="max-width:80%; max-height=80%;"></img></p>

16、[javascript-questions](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lydiahallie/javascript-questions)：JavaScript 进阶问题列表，包含答案。[中文版阅读](https://github.com/lydiahallie/javascript-questions/blob/master/README-zh_CN.md)


17、[licia](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/liriliri/licia)：比较实用的 JS 工具库，内置了很多可能在工程中经常会用到的工具函数。该库提供 npm 安装，可以很好的融合到现代前端工程的开发中，从而提高开发效率。示例代码：
```javascript
const uuid = require("licia/uuid");
const dateFormat = require("licia/dateFormat");
const now = require("licia/now");
const randomBytes = require("licia/randomBytes");
console.log(randomBytes(5));
console.log(uuid());
console.log(dateFormat(now(), "yyyy-mm-dd"));
```


18、[styled-components](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/styled-components/styled-components)：如果你是写 react 的开发人员一定不要错过这个库，它使用 ES6 模板字符串完成在 react 中的 css-in-js 的实现，更顺畅地在 React 中写样式。css-in-js 是前端圈中很火的话题，css-in-js 认为样式应该在组件文件中，而不是单独的一个样式文件，这样只是物理上的区分，并不是实际上的组件封装


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/65794292.png' style="max-width:80%; max-height=80%;"></img></p>

19、[vue-unit-test-with-jest](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/holylovelqq/vue-unit-test-with-jest)：一个 Vue 的单元测试项目，列出了 Vue 开发时大多需要测试的环节，并附有测试代码及说明文档。现在前端开发的技术越来越多，但是我们只是注意到了开发阶段并没有做好对应的单元测试步骤，我们可以通过这个项目学习如何针对 Vue 项目做单元测试。示例代码：
```javascript
import { shallowMount, createLocalVue } from '@vue/test-utils'
import FilterTest from '@/components/FilterAddWatchTest.vue'
...
// 测试内容：filter ---- filter 不能通过 wrapper 或者 vm 获取，只能通过组件获取
// filter 需要测试函数的所有可能性
it('filter test', () => {
  // console.log(FilterTest.filters)
  expect(FilterTest.filters.formatText('12345678')).toBe('12...78')
  expect(FilterTest.filters.formatText('12345')).toBe('12345')
  expect(FilterTest.filters.formatText()).toBe('')
})
...
```


20、[x-build](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/codexu/x-build)：面向小型项目的脚手架工具，通过终端命令最快在几秒钟初始化项目目录。该库内部集成了 webpack、babel、eslint 等前端常用的工具。通过该项目可以了解脚手架的开发，并且可以熟悉如何在工具中集成 webpack 这对自定义脚手架开发很有帮助


21、[zdog](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/metafizzy/zdog)：想在你的 Web 应用上应用 3D 图形吗？想用你熟悉的技术实现炫酷的 3D 效果吗？没错 zdog 就是你的首选。这是一款用于用于 Canvas 和 svg 的 JS 3D 渲染引擎，你可以使用它轻松创建扁平化风格的 3D 模型。这个库只有 2800 行代码，并且最小体积为 28KB。并且它还提供了对开发者十分友好的声明式 API，并没有特别复杂的配置只要你会 JS 你就可以使用它。下图都是使用 zdog 完成的作品


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/174164624.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C
22、[GHDropMenuDemo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shabake/GHDropMenuDemo)：一款适用于多种场景、使用简单的筛选菜单组件。方便集成、快速选择出筛选项、对原有项目无污染


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/161890062.gif' style="max-width:80%; max-height=80%;"></img></p>

### PHP
23、[CRMEB](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/crmeb/CRMEB)：基于 ThinkPhp5.0 + Vue + EasyWeChat 开发的一套开源、免费新零售商城系统（集客户关系管理+营销电商系统）。能够帮助企业基于微信公众号、小程序、PC、APP 等，实现会员管理、数据分析、精准营销的电子商务管理系统。满足企业新零售、预约、O2O、多店等各种业务需求，反正就是功能强大、适用于多种场景的商城系统


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/154943413.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
24、[cufflinks](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/santosjorge/cufflinks)：基于 plotly 和 pandas 的绘图库。Pandas 是处理数据的常用库，cufflinks 可以让 pandas 处理后的数据更直观的展示。通过该库你可以用极少的代码，实现绚丽和多样的数据可视化图形


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/26881329.png' style="max-width:80%; max-height=80%;"></img></p>

25、[one-python-craftsman](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/piglei/one-python-craftsman)：如何编写优秀的 Python 代码？优秀的代码就是由无数优秀的细节组成的。这个项目就是详细讲解 Python 那些细节，比如何时使用异常、怎么给变量起名、怎么编写条件分支等等，看似简单的可能也是最难的地方。本项目作者是资深的 Python 开发，内容贴近实际工作和业务场景，相信认真学习完本项目，你的编码能力一定会得到很大提升，帮你在 Python 的开发道路上走的更高、更远


### Ruby
26、[rubocop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rubocop/rubocop)：一个 Ruby 静态代码分析器和代码格式化程序。开箱即用，强制执行社区 Ruby 样式指南中列出的许多指导原则。RuboCop 非常灵活，大多数行为都可以通过各种配置选项进行调整。除了报告代码中的问题外，还可以自动为您解决一些问题。使用最广、效率超高的 Ruby 静态代码检测工具。示例代码：
```
$ gem install rubocop
$ cd my/cool/ruby/project
$ rubocop
```


### Swift
27、[uPic](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gee1k/uPic)：一款 macOS 端的图床客户端，支持多种免费、付费的图床，让你方便快捷的上传图片，醉心于内容创作的工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/190874674.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
28、[DG-Net](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NVlabs/DG-Net)：深度学习模型训练时往往需要大量的标注数据，但收集和标注大量的数据往往比较困难。作者在行人重识别这个任务上探索了，利用生成数据来辅助训练的方法。通过生成高质量的行人图像（行人两两换衣），将其与行人重识别模型融合，同时提升行人生成的质量和行人重识别的精度
1. 不需要额外标注（如姿态 pose、属性 attribute、关键点 keypoints 等），就能生成高质量行人图像。通过交换提取出的特征，来实现两张行人图像的外表互换。这些外表都是训练集中真实存在的变化，而不是随机噪声。
2. 不需要部件匹配来提升行人重识别的结果。仅仅是让模型看更多训练样本就可以提升模型的效果。给定N张图像，我们首先生成了 NxN 的训练图像，用这些图像来训练行人重识别模型。(下图第一行和第一列为真实图像输入，其余都为生成图像)
3. 训练中存在一个循环。生成图像喂给行人重识别模型来学习好的行人特征，而行人重识别模型提取出来的特征也会再喂给生成模型来提升生成图像的质量。


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/194320424.jpg' style="max-width:80%; max-height=80%;"></img></p>

29、[hub](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pytorch/hub)：一个包含计算机视觉、自然语言处理领域的诸多经典模型的聚合中心。这年头有很多 Hub，什么 GitHub、SciHub、xxxxHub 等等，但是最近图灵奖得主 Yann LeCun 强推的 PyTorch-Hub。无论是 ResNet、BERT、GPT、VGG、PGAN 还是 MobileNet 等经典模型，只需输入一行代码，都能实现一键调用！妈妈再也不用担心你的模型啦！示例代码：
```
1、查询可用的模型

用户可以使用 torch.hub.list() 这个API列出 repo 中所有可用的入口点。
比如你想知道 PyTorch Hub 中有哪些可用的计算机视觉模型：

>>> torch.hub.list(‘pytorch/vision’)
>>>
[‘alexnet’,
‘deeplabv3_resnet101’,
‘densenet121’,
…
‘vgg16’,
‘vgg16_bn’,
‘vgg19’,
‘vgg19_bn’]

2、加载模型

在上一步中能看到所有可用的计算机视觉模型，如果想调用其中的一个，也不必安装，只需一句话就能加载模型。

model = torch.hub.load(‘pytorch/vision’, ‘deeplabv3_resnet101’, pretrained=True)

至于如何获得此模型的详细帮助信息，可以使用下面的 API：

print(torch.hub.help(‘pytorch/vision’, ‘deeplabv3_resnet101’))

如果模型的发布者后续加入错误修复和性能改进，用户也可以非常简单地获取更新，确保自己用到的是最新版本：

model = torch.hub.load(…, force_reload=True)

对于另外一部分用户来说，稳定性更加重要，他们有时候需要调用特定分支的代码。
例如 pytorch_GAN_zoo 的 hub 分支：

model = torch.hub.load(‘facebookresearch/pytorch_GAN_zoo:hub’, ‘DCGAN’, pretrained=True, useGPU=False)

3、查看模型可用方法

从 PyTorch Hub 加载模型后，你可以用 dir 查看模型的所有可用方法。以 bertForMaskedLM 模型为例：

>>> dir(model)
>>>
[‘forward’
…
‘to’
‘state_dict’,
]

如果你对forward方法感兴趣，使用 help 了解运行运行该方法所需的参数。

>>> help(model.forward)
>>>
Help on method forward in module pytorch_pretrained_bert.modeling:
forward(input_ids, token_type_ids=None, attention_mask=None, masked_lm_labels=None)
…
```


30、[LIS-YNP](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Eurus-Holmes/LIS-YNP)：一个包含基础教程、提高参考资料、有趣实践项目的 PyTorch 教程。人生苦短，我用 PyTorch


31、[TabNine](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/codota/TabNine)：基于 OpenAI 的语言模型的代码补全工具。支持 23 种编程语言、5 种编辑器（VS Code、Sublime Text、Atom、Emacs、Vim）、使用简单，效果惊艳


### Other
32、[from_coder_to_expert](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/0voice/from_coder_to_expert)：2019 年各互联网大厂最新内部技术分享的文档、PDF、PPT 集合。从程序员到 CTO，从专业走向卓越


33、[getAwayBSG](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Jinnrry/getAwayBSG)：项目名为“逃离北上广”，该项目通过爬取的招聘和房价数据。给准备逃离北上广等一线城市，却又找不到去处的 IT 人士提供了一些可视化数据作为建议


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/165990457.png' style="max-width:80%; max-height=80%;"></img></p>

34、[git-open](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/paulirish/git-open)：用 git 命令 push 完代码，想看仓库网页内容是否更新成功还需要再去打开网页查看。有了这个项目，直接输入 git open 命令浏览器就能自动打开对应的仓库的网页，支持 GitHub、GitLab、Bitbucket。是不是很方便？还等什么快去试试


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/40/29791986.gif' style="max-width:80%; max-height=80%;"></img></p>

35、[sqli-labs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Audi-1/sqli-labs)：非常详细的 SQL 注入教程。值得想要入门安全行业的同学阅读和学习（英文）


36、[Student-resources](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ivmm/Student-resources)：这个世界对学生总是非常友好，尤其是大学生。学生们总能获得各种各样的优惠，本文介绍的就是利用学生身份可以享受到的相关学生优惠权益，但也希望各位享受权利的同时不要忘记自己的义务，不要售卖、转手自己的学生优惠资格，使得其他同学无法受益。像 GitHub、Microsoft、AWS、JetBrains 以及最近开始的苹果学生优惠大促销，大学生（中学生也可以，小学生比较难）们都可以尽情享用啦！最后祝各位学生学业进步，让自己的生活更精彩


### Book
37、[flutter-in-action](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/flutterchina/flutter-in-action)：《Flutter 实战》，[在线阅读](https://book.flutterchina.club/)


38、[go101](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/go101/go101)：《Go语言101》是一本着重介绍 Go 语法和语义的编程指导书，[中文版在线阅读](https://gfw.go101.org/article/101.html)




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub39.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub41.md">『Next』</a>
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
        <a href="https://apifox.cn/a103hello">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/apifox.png" width="60px"><br>
          <sub>Apifox</sub><br>
          <sub>比 Postman 更强大</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
