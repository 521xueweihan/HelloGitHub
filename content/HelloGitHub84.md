# 《HelloGitHub》第 84 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/84) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[linked-list-good-taste](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mkirchner/linked-list-good-taste)：Linus Torvalds 解释编码品味的链表论证。在 2016 年的 TED 访谈中，Linus Torvalds 谈到了他认为好的编码品味，并举了一个例子：在单向链表中移除项目的两种实现。为了从链表中删除第一项，其中一个实现需要处理特殊情况，而另一个则不需要，Linus 更喜欢后者。

2、[rpi4-osdev](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sypstraw/rpi4-osdev)：为树莓派 4 编写操作系统的教程。这是一份 RealVNC 的 CTO 在树莓派 4 裸机上，编写操作系统的教程。内容分为 15 个章节，每章完成操作系统的一个部分，并提供了源码和讲解。来自 [@刘三非](https://hellogithub.com/user/VhrXCAs7cMxL08W) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/279028703.jpg' style="max-width:80%; max-height=80%;"></img></p>

3、[xdotool](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jordansissel/xdotool)：模拟键盘和鼠标操作的命令行工具。该项目可以通过命令的方式，模拟键盘输入、鼠标点击，以及移动、聚焦和调整窗口大小等操作，搭配上 shell 就是 DIY 的按键精灵，支持 Ubuntu、macOS、FreeBSD 等系统。
```
// 打字
xdotool type "HelloGitHub"
// 组合键
xdotool key ctrl+l
// 移动鼠标
xdotool mousemove x y
// 关闭窗口
xdotool selectwindow windowclose
```

### C# 项目
4、[DnsServer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TechnitiumSoftware/DnsServer)：一款适用于多平台的 DNS 服务。它开箱即用无需配置，并提供了友好的 Web 界面和监控，支持 Docker 部署以及 Windows、Linux、macOS 和树莓派操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/108726321.png' style="max-width:80%; max-height=80%;"></img></p>

5、[Flow.Launcher](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Flow-Launcher/Flow.Launcher)：Windows 的快速文件和程序启动器。这是一款可以让你的工作流程更加丝滑的工具，相当于 Mac 上的 Alfred。它能够快速启动应用，方便地搜索文件、书签等内容，支持扩展插件、预览文件、系统命令、游戏模式等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/257526212.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[Playnite](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JosefNemec/Playnite)：一款开源的电脑游戏管理工具。支持同步 Steam、Epic、GOG、Battle.net 等平台的游戏，导入后该工具会自动从 IGDB 获取游戏信息，为你的游戏提供一个统一的界面。它的代码完全开源保证了你的账号安全，而且支持包括中文在内的多种语言，适用于 Windows7 及以上的操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/86182490.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
7、[dragonfly](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dragonflydb/dragonfly)：一款为取代 Redis 而生的内存数据库。它与当下最流行的两款内存数据库 Redis 和 Memcached 的 API 完全兼容，所以无需修改代码即可完成迁移。性能上更是爆炸，官方表示单实例可支持数百万量级的 QPS，而且吞吐量是 Redis 的 25 倍，并可以应对 TB 级别的内存数据集。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/437245741.png' style="max-width:80%; max-height=80%;"></img></p>

8、[moonlight-qt](https://hellogithub.com/periodical/statistics/click?target=https://github.com/moonlight-stream/moonlight-qt)：让你可以在几乎任何设备上玩  PC 游戏的工具。该项目基于 NVIDIA GameStream 协议，通过串流的方式实现在 iOS、Android、电视等设备上玩电脑的 3A 大作。此过程手机无需下载和运行游戏，只需接收游戏画面、反馈操作指令。虽然安装过程有点复杂需要花些时间，但是为了躺着玩 PC 游戏一切都是值得的，感兴趣的小伙伴折腾起来吧！

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/131449222.jpg' style="max-width:80%; max-height=80%;"></img></p>

9、[oceanbase](https://hellogithub.com/periodical/statistics/click?target=https://github.com/oceanbase/oceanbase)：一款国产的原生分布式数据库。这是源自蚂蚁集团的一款基于 Paxos 协议和分布式架构的企业级分布式关系型数据库。它同时支持 OLTP 和 OLAP 的混合负载，具有高可用、高性能、水平扩展、兼容 SQL 语法等特点。来自 [@lijiayun123](https://hellogithub.com/user/licrT58f763QMR0) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/372536760.jpg' style="max-width:80%; max-height=80%;"></img></p>

10、[rr](https://hellogithub.com/periodical/statistics/click?target=https://github.com/rr-debugger/rr)：Linux 上的轻量级 C/C++ 调试工具。这是一款 Linux 上的轻量级调试 C/C++ 代码的工具，支持录制、重放和反向执行等操作，提供了一个可反复调试的环境，大大提升了调试效率。

### Go 项目
11、[gorss](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Lallassu/gorss)：一款用 Go 编写的命令行 RSS 阅读器。它简单易用隐蔽性强，支持预览内容、浏览器打开链接、自定义快捷键、主题、单词高亮等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/209380442.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[gosec](https://hellogithub.com/periodical/statistics/click?target=https://github.com/securego/gosec)：Go 语言源码安全检查工具。该项目通过扫描 Go 代码的 AST 检查源代码是否存在安全问题，能够发现源码中硬编码密码、XSS 和 SQL 注入等问题。

13、[skopeo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/containers/skopeo)：能够管理远程仓库的容器镜像的工具。它能够查看远程仓库的容器镜像信息，以及执行复制、同步、删除等操作，支持 docker.io、quay.io、私有仓库等。
```
$ skopeo inspect docker://registry.fedoraproject.org/fedora:latest
{
    ...
    "Architecture": "amd64",
    "Os": "linux",
    "Layers": [
        "sha256:2a0fc6bf62e155737f0ace6142ee686f3c471c1aab4241dc3128904db46288f0"
    ],
    "LayersData": [
        {
            "MIMEType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
            "Digest": "sha256:2a0fc6bf62e155737f0ace6142ee686f3c471c1aab4241dc3128904db46288f0",
            "Size": 71355009,
            "Annotations": null
        }
    ],
    "Env": [
        "DISTTAG=f37container",
        "FGC=f37",
        "container=oci"
    ]
}
```

14、[yaegi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/traefik/yaegi)：一款优雅的 Go 语言解释器。它是一个纯 Go、仅依赖标准库实现的 Go 解释器，拥有简单易用的 API，完全支持 Go 编程语言规范，以及 Go 1.18 和 1.19 版本。
```go
package main

import (
	"github.com/traefik/yaegi/interp"
	"github.com/traefik/yaegi/stdlib"
)

func main() {
	i := interp.New(interp.Options{})

	i.Use(stdlib.Symbols)

	_, err := i.Eval(`import "fmt"`)
	if err != nil {
		panic(err)
	}

	_, err = i.Eval(`fmt.Println("Hello Yaegi")`)
	if err != nil {
		panic(err)
	}
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/116938442.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
15、[AndroidBitmapMonitor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shixinzhang/AndroidBitmapMonitor)：Android 的图片内存分析工具。它可以帮助开发者快速发现应用内加载的图片是否合理，比如大小是否合适、缓存是否及时清理、是否加载了当前并不需要的图片等等，支持在线下和线上使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/595711802.jpg' style="max-width:80%; max-height=80%;"></img></p>

16、[frostmourne](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AutohomeCorp/frostmourne)：汽车之家开源的监控平台。采用 SpringBoot+MyBatis+XXL-JOB 构建的监控系统，支持接入 ES、HTTP、Prometheus、MySQL/TiDB 等多种数据源，以及钉钉、飞书、短信等多种报警消息发送方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/228294148.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
17、[koishi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/koishijs/koishi)：一款极易扩展的聊天机器人框架。它提供了便利的控制台和插件市场，让你无需编程基础也可以开箱即用，几分钟内搭建出自己的聊天机器人，支持 QQ、Telegram、Discord、飞书等聊天平台。来自 [@HBSpy](https://hellogithub.com/user/rIXCy0ZT2L49Ysj) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/225572038.jpg' style="max-width:80%; max-height=80%;"></img></p>

18、[nginx-proxy-manager](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NginxProxyManager/nginx-proxy-manager)：一款强大的 Nginx 可视化管理平台。它开箱即用支持 Docker 一键部署，可以让用户通过 Web 界面在线配置、管理 Nginx 服务，支持转发、重定向、SSL 证书、高级配置等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/114938943.png' style="max-width:80%; max-height=80%;"></img></p>

19、[qinglong](https://hellogithub.com/periodical/statistics/click?target=https://github.com/whyour/qinglong)：支持多种脚本语言的定时任务管理平台。这是一款定时执行脚本的平台，提供了在线管理脚本、环境变量、查看日志、秒级定时任务等功能，支持 Python3、JavaScript、shell 等脚本语言。来自 [@yanyuwangluo](https://hellogithub.com/user/LtSdACHwDTgO2ux) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/347404990.png' style="max-width:80%; max-height=80%;"></img></p>

20、[snk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Platane/snk)：“吃光”你所有的 GitHub 贡献。它可以根据 GitHub 上的贡献图，自动生成蛇的行走路径，一口气吃光所有“绿块”，支持生成 gif 或 svg 格式的动图。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/279995113.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[uptime-kuma](https://hellogithub.com/periodical/statistics/click?target=https://github.com/louislam/uptime-kuma)：一款极简的 uptime 监控工具。该项目可以用来监控服务正常运行时间，它界面美观、支持 Docker 一键部署，提供了中文界面、通知、多状态页面等实用功能。来自 [@浮生若夢](https://hellogithub.com/user/hKmH64UjOdwgCEi) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/382496361.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
22、[dujiaoka](https://hellogithub.com/periodical/statistics/click?target=https://github.com/assimon/dujiaoka)：PHP 写的开源自动售货系统。采用 Laravel+Bootstrap 实现的自动售卖虚拟产品的平台，比如兑换码、账号之类的数字商品，顾客付款后可以自动发货，已集成微信、支付宝、Paypal 等多种支付方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/129852395.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
23、[bar_chart_race](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dexplo/bar_chart_race)：基于 Python 的动态条形图。通过该项目可以用 Python 创建条形图比赛动画，显示数据排名的动态条形图，直观地展示数据变化过程。来自 [@databook](https://hellogithub.com/user/1qC4w2Ey6bu0fgR) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/259213243.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[dataset](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pudo/dataset)：为懒人准备的操作数据库的 Python 库。它基于 SQLAlchemy 构建了一个简单的数据层，可以让查询、写入、更新数据库中的数据，就像读写 JSON 文件一样简单，支持 SQLite、PostgreSQL 和 MySQL 数据库。
```python
import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='John Doe', age=37))
table.insert(dict(name='Jane Doe', age=34, gender='female'))

john = table.find_one(name='John Doe')
```

25、[GreaterWMS](https://hellogithub.com/periodical/statistics/click?target=https://github.com/GreaterWMS/GreaterWMS)：可商用的开源仓库管理系统。该项目是采用福特亚太区售后物流仓储供应链流程的仓库系统，它提供了客户管理、订单管理、库存管理、供应商管理、盘点等模块，支持手机、电脑等多种设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/266941405.png' style="max-width:80%; max-height=80%;"></img></p>

26、[secretflow](https://hellogithub.com/periodical/statistics/click?target=https://github.com/secretflow/secretflow)：蚂蚁开源的隐私计算框架。隐私计算即通过技术的手段实现数据在参与方可用不可见，让数据在安全和不泄露隐私的情况下流通、开放。该项目采用 Python 语言编写，支持包括 MPC、FL、TEE、HE、DP 在内的多种主流隐私计算技术。来自 [@vector](https://hellogithub.com/user/UBnaedx6ch7KzF4) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/481901631.jpg' style="max-width:80%; max-height=80%;"></img></p>

27、[shynet](https://hellogithub.com/periodical/statistics/click?target=https://github.com/milesmcc/shynet)：极简的网站分析平台。这是一个基于 Django 构建的网站分析平台，它很小、够用、界面友好、不追踪 cookie、支持多用户，追踪脚本不到 1KB。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/254441446.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust 项目
28、[carbonyl](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fathyb/carbonyl)：运行在终端里的浏览器。这是一款基于 Chromium 的命令行浏览器，可以在终端里用浏览器的方式访问网页，支持图片、动图、视频、音频等内容。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/591273534.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[lsd](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lsd-rs/lsd)：下一代 ls 命令。这个项目是用 Rust 重写的类似 ls 命令的查看目录清单的工具，同时增加了颜色、图标等新功能，更加赏心悦目。来自 [@pujianquan](https://hellogithub.com/user/pSBMNFK9ldZLgsa) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/158927812.png' style="max-width:80%; max-height=80%;"></img></p>

30、[typst](https://hellogithub.com/periodical/statistics/click?target=https://github.com/typst/typst)：比 LaTex 更好学的标记语言。这是一款新的基于标记语言的排版系统，它比知名的 LaTex 更加简洁、更容易上手，输出的公式也很漂亮，还可以更换各种字体。来自 [@databook](https://hellogithub.com/user/1qC4w2Ey6bu0fgR) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/210702427.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
31、[DevToysMac](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DevToys-app/DevToysMac)：macOS 上的程序员瑞士军刀。该项目是 DevToys 的 macOS 版本，无需安装下载解压后即可使用。它同样实现了程序员日常开发会用到的功能，比如时间戳转化、Base64 编/解码、JSON 格式化等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/453642201.png' style="max-width:80%; max-height=80%;"></img></p>

32、[wikipedia-ios](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wikimedia/wikipedia-ios)：维基百科官方开源的 iOS 客户端。维基百科是一本线上的百科全书，这是它的 iOS 客户端，支持搜索资料、热门文章、保存文章、多语言、夜间阅读等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/13863130.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
33、[Bringing-Old-Photos-Back-to-Life](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life)：通过深度学习修复老照片的工具。由微软开源的深度学习项目，可用于修复破损的老照片，修复效果显著。来自 [@lastone](https://hellogithub.com/user/y6WLMKXlxiH1b74) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/274594200.jpg' style="max-width:80%; max-height=80%;"></img></p>

34、[ChatGLM-6B](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zai-org/ChatGLM-6B)：清华 KEG 开源的双语对话语言模型。这是一个基于 GLM 架构、具有 62 亿参数的中英双语对话语言模型，支持在单张 2080Ti 上进行推理使用。
```python
>>> from transformers import AutoTokenizer, AutoModel
>>> tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
>>> model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
>>> model = model.eval()
>>> response, history = model.chat(tokenizer, "你好", history=[])
>>> print(response)
你好👋!我是人工智能助手 ChatGLM-6B,很高兴见到你,欢迎问我任何问题。
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/613349035.gif' style="max-width:80%; max-height=80%;"></img></p>

35、[DI-engine](https://hellogithub.com/periodical/statistics/click?target=https://github.com/opendilab/DI-engine)：OpenDILab 开源的决策 AI 平台。这是一个基于 PyTorch 的通用决策智能引擎，为开发者提供了 60+ 种算法、40+ 类型环境。支持各类定制化的训练和实际决策智能应用，比如游戏 AI、自动驾驶和生物序列预测等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/382787545.png' style="max-width:80%; max-height=80%;"></img></p>

36、[llama.cpp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ggml-org/llama.cpp)：在笔记本上运行 LLaMA 大模型。该项目实现了在 CPU 上流畅运行 LLaMA 模型，支持 macOS、Linux、Windows 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/612354784.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
37、[.tmux](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gpakosz/.tmux)：一份好看且通用的 tmux 配置文件。Tmux 是一个终端复用器，该项目包含了一份可以让 tmux 更漂亮、更好用的配置文件，以及详细的安装步骤。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/5526729.gif' style="max-width:80%; max-height=80%;"></img></p>

38、[ark-pixel-font](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TakWolf/ark-pixel-font)：开源的泛中日韩像素字体。为游戏开发提供了一套可用于正文的像素字体，目前完成了 1 万个左右的汉字(12px)。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/366474401.png' style="max-width:80%; max-height=80%;"></img></p>

39、[bpf-developer-tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eunomia-bpf/bpf-developer-tutorial)：从入门到进阶的 eBPF 开发者教程。这是一个基于 libbpf 和 CO-RE(一次编译，到处运行) 的 eBPF 教程，包括 eBPF 基本概念、代码实例、实际应用等内容，通过 20 个 eBPF 的小工具，来帮助开发者快速上手 eBPF。

40、[ENGAGE](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TUDSSL/ENGAGE)：自制无电池的 GameBoy。该项目实现了没有电池、仅通过太阳能和游戏操作供电的 GameBoy。它可正常运行俄罗斯方块游戏，遇到电量耗尽时能保存游戏的当前进度，即重新启动游戏后，下落的方块会处于同一位置。是不是听起来很酷？这里包含制作该设备所需的一切，感兴趣的同学可以试一试。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/281764334.png' style="max-width:80%; max-height=80%;"></img></p>

41、[GameDevMind](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gonglei007/GameDevMind)：全面的游戏开发技术图谱。该项目用思维导图的方式，展示了游戏开发需要具备的能力，包含技术栈、方法、工具、流程、管理、运营等方面。来自 [@gonglei007](https://hellogithub.com/user/dl593RYb28vQBki) 的分享

### 开源书籍
42、[PPHC](https://hellogithub.com/periodical/statistics/click?target=https://github.com/johnlui/PPHC)：《高并发的哲学原理》。这本书讨论的是 Web 服务高并发问题，内容由浅入深地介绍了 Apache、Nginx、epoll、交换机、k8s、数据库、分布式、微服务架构等解决高并发问题的技术和方案。来自 [@吕文翰](https://hellogithub.com/user/QkntmXFwR5yS7pr) 的分享

43、[py_regular_expressions](https://hellogithub.com/periodical/statistics/click?target=https://github.com/learnbyexample/py_regular_expressions)：《Python 正则表达式从入门到精通》。这本书包含数百个示例和练习，涵盖了 Python 正则表达式从初级到高级的用法。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/84/165224631.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub83.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub85.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/84'>这里</a>。
</p>

## 赞助


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


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
