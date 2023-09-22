# 《HelloGitHub》第 58 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/58) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C# 项目
1、[EverythingToolbar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/srwi/EverythingToolbar)：把搜索和启动应用等功能整合到 Windows taskbar 的工具。效果如下图：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/295200728.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
2、[ChordNova](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Chen-and-Sim/ChordNova)：一款开源免费的和弦生成工具。我不懂乐理，但单从这个软件的界面就感受到了专业，因为有很多乐理的名词😅


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/283499368.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
3、[containers-the-hard-way](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/shuveb/containers-the-hard-way)：用 Go 实现迷你 Docker，包含 Docker 核心功能的开源项目。该项目仅用 Linux 系统接口实现了类似容器的功能，这些能够帮助你更好地了解容器的工作方式。如果你想更深入地理解容器，就参考本项目写一个迷你 Docker 吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/266515261.png' style="max-width:80%; max-height=80%;"></img></p>

4、[delve](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/go-delve/delve)：一款 Go 语言的调试工具。如果你还在像我一样用 `fmt.Println` 调试 go 的代码，就试试这个工具吧。万星的开源项目可不是开玩笑的，它上手简单并且支持多种方式调用，助你快速找到 Bug


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/19994257.png' style="max-width:80%; max-height=80%;"></img></p>

5、[rqlite](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rqlite/rqlite)：用 Go 实现的基于 SQLite 轻量级、分布式关系数据库。如果你对分布式数据库的原理及实现感兴趣的话，这个项目真的是你入门这方面的不二之选，这个项目用 SQLite 作为存储引擎，让你可以把更多的精力放在理解分布式的知识上，尝试阅读下这个项目的文档，相信你会对它感兴趣的。设计图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/23247808.png' style="max-width:80%; max-height=80%;"></img></p>

6、[vegeta](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tsenart/vegeta)：基于 Go 语言的 HTTP 压测工具。目前市面上的压测工具已经很多了，但是今天推荐的这款惊艳到我点是下面这条命令执行后的效果（vegeta+jaggr+jplot），让我们一起来感受下吧
```bash
echo 'GET http://localhost:8080' | \
    vegeta attack -rate 5000 -duration 10m | vegeta encode | \
    jaggr @count=rps \
          hist\[100,200,300,400,500\]:code \
          p25,p50,p95:latency \
          sum:bytes_in \
          sum:bytes_out | \
    jplot rps+code.hist.100+code.hist.200+code.hist.300+code.hist.400+code.hist.500 \
          latency.p95+latency.p50+latency.p25 \
          bytes_in.sum+bytes_out.sum
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/12080551.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
7、[Anki-Android](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ankidroid/Anki-Android)：高效学习神器 Anki 安卓客户端。Anki 是一个帮助学习的记忆卡片软件，卡片正面是问题背面是答案，然后根据记忆公式帮你复习和记牢。[下载地址](https://github.com/ankidroid/Anki-Android/releases/tag/v2.14.3) 如果下载后不会用的话，本文点赞过 100 我出一份小白教程给大家上手这个神器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/7716883.png' style="max-width:80%; max-height=80%;"></img></p>

8、[apollo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apolloconfig/apollo)：携程开源的分布式配置中心。开箱即用理念发挥到极致，比如：服务器部分基于 Spring Boot 和 Spring Cloud 开发，运行方便无需额外的 Tomcat 应用容器。并且具备配置修改后即时生效、规范的权限、流程治理等特性，适用于微服务配置管理场景


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/53127403.jpg' style="max-width:80%; max-height=80%;"></img></p>

9、[java-design-patterns](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/iluwatar/java-design-patterns)：设计模式 Java 的最佳实践，出自开源社区大佬们之手。作为有梦想和追求的 Java 程序员，当然需要会一些设计模式啦。这个项目虽然是英文的但是先看代码和图，尝试理解含义那么英文描述也就能猜得八九不离十了。不要让英语作为你不努力的借口，努力变强吧！[在线阅读](https://java-design-patterns.com/)


10、[JustAuth](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/justauth/JustAuth)：帮你搞定第三方登陆的 Java 开源组件。使用简单、接入方便，帮你随心所欲地接入第三方登陆，让登陆变得简单。目前已经支持十多个平台，还在持续扩充中


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/168500397.png' style="max-width:80%; max-height=80%;"></img></p>

11、[KnowStreaming](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/didi/KnowStreaming)：功能强大的 Kafka 集群监控和运维管理平台。强大到我一度以为它是付费的，如果你的公司用 Kafka 的话，可以试试主导把这个项目在公司内部用起来，那你离升职和加薪就不远了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/248416273.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
12、[cloudbase-framework](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/cloudbase-framework)：腾讯开源的云原生一体化部署工具。一键将项目部署上云，不限制框架和语言


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/256659361.png' style="max-width:80%; max-height=80%;"></img></p>

13、[hearthstone-battlegrounds-tools](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chenyueban/hearthstone-battlegrounds-tools)：暴雪炉石传说游戏的记牌插件。不懂编程的小伙伴拿去用就好了，支持 Windows 和 macOS 系统。开发者的话，这是一整套完整的 Electronjs 开发流程，从多个渲染进程的管理、不同平台的差异化处理、版本的控制与发布等方面都做了细致的封装，学起来吧。功能上她还具有以下特性：
- 🌴 当天战绩统计，历史战绩查询
- 🎉 统计你所使用过的英雄，自动计算每个英雄的平均排名、选择率
- 🙈 选择英雄时展示可选英雄的大数据选择率、平均排名等
- 🃏 对局信息记录，记录对局过的对手阵容
- ✈️ 一键拔线（可怕）
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/309671292.jpg' style="max-width:80%; max-height=80%;"></img></p>

14、[Multiavatar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/multiavatar/Multiavatar)：生成人物头像的 JS 库。支持随机生成一个好看、独特、多文化的头像


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/313732427.png' style="max-width:80%; max-height=80%;"></img></p>

15、[newbee-mall-vue3-app](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/newbee-ltd/newbee-mall-vue3-app)：基于 Vue 3.0 技术栈的电商网站前端开源项目。它麻雀虽小五脏俱全，包含模块：首页、类型分类、搜索、地址管理、登录注册等等，该有的基本上都有涉及到。对新手友好，在熟悉 Vue 3.x 的朋友也可以来看看


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/305132874.png' style="max-width:80%; max-height=80%;"></img></p>

16、[X6](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/antvis/X6)：AntV 旗下的图编辑引擎。提供了开箱即用的交互组件和简单易用的节点定制能力，从而能够快速完成流程图、DAG 图、ER 图等图应用。示例代码：
```javascript
import { Graph } from '@antv/x6';

const graph = new Graph({
  container: document.getElementById('container'),
  width: 800,
  height: 600,
  background: {
    color: '#fffbe6', // 设置画布背景颜色
  },
  grid: {
    size: 10,      // 网格大小 10px
    visible: true, // 渲染网格背景
  },
});
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/221622743.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
17、[easy-sms](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/overtrue/easy-sms)：短信发送 PHP 组件。特点：
- 支持目前市面多家服务商
- 一套写法兼容所有平台
- 简单配置即可灵活增减服务商
- 内置多种服务商轮询策略、支持自定义轮询策略
- 等等
```php
use Overtrue\EasySms\EasySms;

$config = [
    // HTTP 请求的超时时间（秒）
    'timeout' => 5.0,

    // 默认发送配置
    'default' => [
        // 网关调用策略，默认：顺序调用
        'strategy' => \Overtrue\EasySms\Strategies\OrderStrategy::class,

        // 默认可用的发送网关
        'gateways' => [
            'yunpian', 'aliyun',
        ],
    ],
    // 可用的网关配置
    'gateways' => [
        'errorlog' => [
            'file' => '/tmp/easy-sms.log',
        ],
        'yunpian' => [
            'api_key' => '824f0ff2f71cab52936axxxxxxxxxx',
        ],
        'aliyun' => [
            'access_key_id' => '',
            'access_key_secret' => '',
            'sign_name' => '',
        ],
        //...
    ],
];

$easySms = new EasySms($config);

$easySms->send(13188888888, [
    'content'  => '您的验证码为: 6379',
    'template' => 'SMS_001',
    'data' => [
        'code' => 6379
    ],
]);
```


18、[mochat](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mochat-cloud/mochat)：一套开源的企业微信开发框架和管理系统。基于 PHP 开发的前后端分离、功能强大的企业微信管理平台


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/330622402.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
19、[lastversion](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dvershinin/lastversion)：帮你找到库或者软件最新版本的 Python 工具。它可以避开不同项目作者使用的不同风格的版本号，获取一个项目的最新版本号，下载或安装它们。本项目可用于 build system，比如自动更新脚本。支持从这些网站搜索：GitHub、GitLab、PyPI 等，确保版本最新和稳定
```
# 获取最新的 Linux 版本号和最新的 Wordpress 版本号
lastversion linux
# 作者的版本标签：v5.10
# 本项目提供的版本标签：5.10
lastversion wordpress
# 作者的版本标签：5.6
# 本项目提供的版本标签：5.6
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/187117077.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[streamlit](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/streamlit/streamlit)：能够快速地把数据制作成可视化、交互页面的 Python 框架。分分钟让你的数据变成图表，并且该项目提供免费的共享服务平台帮你的项目上线，方便数据的共享和讨论


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/204086862.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[xonsh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xonsh/xonsh)：支持 Python 赋能的 shell。如果你不会编写 shell 脚本，但是会 Python。那通过这个项目可以让你混用 shell 命令和 Python 语法，高效快速地完成你想要的功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/29620400.png' style="max-width:80%; max-height=80%;"></img></p>

22、[Zappa](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zappa/Zappa)：Python 无服务框架(serverless)。用这个项目开发完功能，只需几个命令就能打包上传到云服务平台，瞬间完成服务发布。不仅程序员喜欢它，老板也喜欢因为能够降低服务器成本省钱。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/279672524.gif' style="max-width:80%; max-height=80%;"></img></p>

### Ruby 项目
23、[spree](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/spree/spree)：基于 Ruby on Rails 实现的大而全的电子商城开源项目。功能齐全项目结构清晰：
- spree_api：REST API 接口
- spree_frontend：移动优先，可自定义的店面
- spree_backend：功能丰富的管理面板
- spree_cmd：开发人员的命令行工具
- spree_core：数据层、服务和邮件、基本组件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/3314.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
24、[mas](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mas-cli/mas)：Mac App Store 命令行版


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/40092232.png' style="max-width:80%; max-height=80%;"></img></p>

25、[Moya](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Moya/Moya)：基于 Alamofire 的轻量级 Swift 网络层框架。它提供了网络抽象层，使用起来足够简单，能够方便地与 RXSwift、PromiseKit、ObjectMapper 结合，轻松地应对常见的开发任务。同时也非常全面，应对复杂任务也同样容易。最后 Moya 有一个很棒的社区，贡献者们提供了很多实用的扩展
```swift
provider = MoyaProvider<GitHub>()
provider.request(.zen) { result in
    switch result {
    case let .success(moyaResponse):
        let data = moyaResponse.data
        let statusCode = moyaResponse.statusCode
        // do something with the response data or statusCode
    case let .failure(error):
        // this means there was a network failure - either the request
        // wasn't sent (connectivity), or no response was received (server
        // timed out).  If the server responds with a 4xx or 5xx error, that
        // will be sent as a ".success"-ful response.
    }
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/23013268.png' style="max-width:80%; max-height=80%;"></img></p>

26、[MTMR](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Toxblh/MTMR)：自定义 TouchBar 的应用。你问我体验如何？我没钱买带 TouchBar 的电脑啊，你装上我看看就行了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/125547624.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
27、[Ad-papers](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wzhe06/Ad-papers)：计算广告相关论文、学习资料和业界分享集合


28、[awesome-seo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/madawei2699/awesome-seo)：有关 Google SEO 和流量变现资料的项目。该项目是作者学习 SEO 过程中整理的权威资料，推荐给有个人网站的小伙伴们


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/327323917.png' style="max-width:80%; max-height=80%;"></img></p>

29、[free-font](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wordshub/free-font)：免费可商用的字体集合。这个项目收录的都是免费可商用的字体，并且仔细地标记出了商用时是否需要获取授权等细节


30、[game-programmer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/miloyip/game-programmer)：游戏程序员的学习路径图。一位游戏开发大神开源的项目，希望能够帮助向往游戏开发的你 or 你的孩子，走上游戏开发这条“不归路”。[中文](https://miloyip.github.io/game-programmer/game-programmer-zh-cn.svg)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/75701562.png' style="max-width:80%; max-height=80%;"></img></p>

31、[luarocks](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/luarocks/luarocks)：Lua 包管理工具。支持三大平台，安装和使用如下：
```
$ wget https://luarocks.org/releases/luarocks-3.5.0.tar.gz
$ tar zxpf luarocks-3.5.0.tar.gz
$ cd luarocks-3.5.0
$ ./configure && make && sudo make install
$ sudo luarocks install luasocket
$ lua
Lua 5.3.5 Copyright (C) 1994-2018 Lua.org, PUC-Rio
> require "socket"
```


32、[makeaplan_public](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/DuanJiaNing/makeaplan_public)：使用 Flutter 和 Go 开发的「制定计划 APP」。帮助用户记录和追踪自己的计划，辅助用户完成自己的目标。手机端用的是 Flutter 后端用 Go 实现，服务器和客户端通过 ProtoBuffer+grpc 进行通信。可作为学习 Flutter 和 Go 的实战项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/316890509.png' style="max-width:80%; max-height=80%;"></img></p>

33、[theia](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/eclipse-theia/theia)：Eclipse 开源的 IDE 工具。我岁数大了，用惯了一个 IDE 就不想换了，喜欢尝鲜的小伙伴可以去把玩一下。看介绍像是一个拥抱开源，与 VS Code 功能相近的开发工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/83050680.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
34、[DeepLearning-500-questions](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/scutan90/DeepLearning-500-questions)：《深度学习 500 问》AI 工程师面试知识点的书籍。内容涵盖深度学习的知识点及各大公司常见的笔试题


### 机器学习
35、[DeepMoji](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bfelbo/DeepMoji)：通过深度学习把自然语言转化成 emoji 表情的项目。用机器学习来了解文字表达的情感，最后返回几个感情相近的 emoji 表情。该项目有趣且易于学习，包含机器学习项目该有的所有内容：示例、模型、数据、测试、源码等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/97591379.png' style="max-width:80%; max-height=80%;"></img></p>

36、[nanodet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/RangiLyu/nanodet)：移动端的轻量级 Anchor-Free 目标检测模型。具有体积小（1.8 MB）、速度快（10.23 ms）、便于训练（硬件要求低）、部署简单（安卓示例）等优点


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/58/305316768.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub57.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub59.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/58'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
