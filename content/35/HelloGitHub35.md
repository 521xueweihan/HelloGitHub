# 《HelloGitHub》第 35 期
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
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [Python 项目](#Python-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [教程](#教程)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C# 项目
1、[IdentityServer4.Admin](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/skoruba/IdentityServer4.Admin)：免费开源的 IdentityServer4 与 Asp.Net Core Identity 管理器。IdentityServer4 官方的管理器是收费的，该项目很好的替代了官方管理器，可以方便的管理使用 IdentityServer4 所搭建的认证服务器

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/IdentityServer4.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
2、[FLIF](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FLIF-hub/FLIF)：免费、新颖的无损图像格式。压缩比方面优于 PNG、lossless WebP、lossless BPG、lossless JPEG2000 等格式

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
3、[cds](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ovh/cds)：企业级开源持续集成系统。支持横向扩展、自带 UI、常用的持续集成构建等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/cds.gif' style="max-width:80%; max-height=80%;"></img></p>

4、[docui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/skanehira/docui)：终端 Docker 管理工具，自带一个终端界面。使用该工具可以方便的通过界面管理 docker 不用再记那些命令。安装命令：
```
# Homebrew
$ brew tap skanehira/docui
$ brew install docui

# go get
$ go get -d github.com/skanehira/docui
$ cd $GOPATH/src/github.com/skanehira/docui
$ GO111MODULE=on go install
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/docui.png' style="max-width:80%; max-height=80%;"></img></p>

5、[go-echarts](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/go-echarts/go-echarts)：Golang 代码生成对应的 echarts 可视化图表。实例代码：
```go
// example.go
package main

import (
    "log"
    "math/rand"
    "os"
    "time"

    "github.com/chenjiandongx/go-echarts/charts"
)

var nameItems = []string{"衬衫", "牛仔裤", "运动裤", "袜子", "冲锋衣", "羊毛衫"}
var seed = rand.NewSource(time.Now().UnixNano())

func randInt() []int {
    cnt := len(nameItems)
    r := make([]int, 0)
    for i := 0; i < cnt; i++ {
        r = append(r, int(seed.Int63()) % 50)
    }
    return r
}

func main() {
    bar := charts.NewBar()
    bar.SetGlobalOptions(charts.TitleOpts{Title: "Bar-示例图"}, charts.ToolboxOpts{Show: true})
    bar.AddXAxis(nameItems).
        AddYAxis("商家A", randInt()).
        AddYAxis("商家B", randInt())
    f, err := os.Create("bar.html")
    if err != nil {
        log.Println(err)
    }
    bar.Render(f)
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/go-echarts.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[1m-go-websockets](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/eranyanay/1m-go-websockets)：该项目演示了如何用 Go 编写一个可以提供超过一百万个 websockets 连接、运行内存小于 1GB 的服务器。`setup.sh` 是用来创建 websocket 客户端的，`destroy.sh` 则用来销毁客户端

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
7、[SpringBoot-Learning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dyc87112/SpringBoot-Learning)：Spring Boot 教程

8、[halo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/halo-dev/halo)：Java 博客系统。在层出不穷的博客系统中，很难看到使用 Java 编写的简洁优雅的博客系统。该项目还具备着轻快且功能强大的特点，这些特性使它从众多 Java 博客系统脱颖而出。安装命令：
```
# 安装 Halo
$ yum install -y wget && wget -O halo-cli.sh https://git.io/fxHqp && bash halo-cli.sh -i
# 更新 Halo
$ bash halo-cli.sh -u
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/halo.png' style="max-width:80%; max-height=80%;"></img></p>

9、[APIJSON](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/APIJSON/APIJSON)：快速开发 API 服务的框架。为简单的增删改查、复杂的查询、简单的事务操作提供了完全自动化的 API。大部分 HTTP 请求后端再也不用写接口了，也不用写文档了，适合中小型前后端分离的项目

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/APIJSON.jpg' style="max-width:80%; max-height=80%;"></img></p>

10、[IQL](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/teeyog/IQL)：基于 SparkSQL 实现了一套即席查询服务，具有如下特性：
- 优雅的交互方式，支持多种 datasource/sink、多数据源混算
- Spark 常驻服务，基于 zookeeper 的引擎自动发现
- 多 session 模式实现并行查询
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/IQL.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
11、[Gitter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/huangjianke/Gitter)：GitHub 的小程序客户端。UI 设计漂亮，可作为小程序和 GitHub 结合的实战项目学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/Gitter.png' style="max-width:80%; max-height=80%;"></img></p>

12、[Motrix](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/agalwood/Motrix)：桌面下载工具，支持下载 HTTP、FTP、BT、磁力链、百度网盘等资源。界面简洁易用，采用 Vue + VueX + Element 的技术架构适合学习桌面应用开发

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/Motrix.png' style="max-width:80%; max-height=80%;"></img></p>

13、[rainbow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ccampbell/rainbow)：体积小、易于使用、支持各种编程语言的语法高亮插件。该项目原理是通过正则过滤关键字，然后进行高亮。代码：
```javascript
// JS关键字判断
Rainbow.extend('javascript', [

    /**
     * matches $. or $(
     */
    {
        name: 'selector',
        pattern: /\$(?=\.|\()/g
    },
    {
        name: 'support',
        pattern: /\b(window|document)\b/g
    }
...
```

14、[Chart.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chartjs/Chart.js)：基于 canvas 的可视化库。可用于构建简单的 H5 图表，满足基本的日常可视化需求

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/Chart.png' style="max-width:80%; max-height=80%;"></img></p>

15、[ant-design-vue](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vueComponent/ant-design-vue)：Ant Design 的 Vue 实现，该项目已经得到 [Ant Design 官方](https://vue.ant.design/docs/vue/introduce-cn/)认可

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
16、[iWeChat](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lefex/iWeChat)：还原、探索微信 APP 的项目。通过该项目借鉴、学习微信客户端开发的相关设计与技术，也可以学到如何分析一个第三方 APP 的方法

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
17、[spug](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/openspug/spug)：使用 Python+Vue 实现的开源运维平台，前后端分离方便二次开发。该项目基于 Docker 镜像发布部署，方便安装和升级。支持运维常见功能：主机管理、任务计划管理、发布部署、监控告警等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/spug.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[ruia](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/howie6879/ruia)：基于 asyncio 和 aiohttp 的 Python3 异步爬虫框架。它具有容易上手、非阻塞、扩展性强等特点，实例代码：
```python
from ruia import TextField, Item, Spider

class HackerNewsItem(Item):
    target_item = TextField(css_select='tr.athing')
    title = TextField(css_select='a.storylink')


class HackerNewsSpider(Spider):
    start_urls = ['https://news.ycombinator.com/news?p=1']

    async def parse(self, response):
        async for item in HackerNewsItem.get_items(html=response.html):
            yield item

if __name__ == '__main__':
    HackerNewsSpider.start()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/ruia.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
19、[devhub](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/devhubapp/devhub)：支持 Android、iOS、Web、Desktop 的 GitHub 管理通知客户端。能够帮你方便地接收、查看、管理 GitHub 消息、动态等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/devhub.jpg' style="max-width:80%; max-height=80%;"></img></p>

20、[neovim](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/neovim/neovim)：致力于改善 Vim 的维护、可扩展性等方面的编辑器。它功能强大、项目开发活跃、社区活跃，“新一代”的 Vim

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/neovim.png' style="max-width:80%; max-height=80%;"></img></p>

21、[Micro8](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Micropoor/Micro8)：浸淫渗透攻击的老鸟所写，内容一线深入浅出，主要是 Windows 系统场景。对于初中级安全从业人员、乙方安全测试、甲方安全自检、网络安全爱好者等提高都有很大的帮助

22、[OI-wiki](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/OI-wiki/OI-wiki)：免费、开放、持续更新的编程竞赛相关知识教程。包含竞赛的基础知识、常见题型、解题思路以及常用工具等内容，帮助大家更快速、深入地学习编程竞赛相关知识

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
23、[You-Dont-Know-JS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/getify/You-Dont-Know-JS)：（英文）深入探讨 JavaScript 语言核心机制的书籍，适用于深入学习 JS。该书已出版，但在线阅读免费

24、[d2l-zh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/d2l-ai/d2l-zh)：《Dive into Deep Learning 》翻译版，即《动手学深度学习》。[在线阅读](http://zh.d2l.ai/)

25、[cppwasm-book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/3dgen/cppwasm-book)：《C/C++ 面向 WebAssembly 编程》，[在线阅读](https://3dgen.cn/cppwasm-book/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 教程
26、[USTC-Course](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/USTC-Resource/USTC-Course)：该仓库收录中国科学技术大学众多课程资源。包括电子版教材、参考书、讲义、试卷、学习心得、习题解答等。以计算机学院课程为主，也包含公选课、自由选修等其他课程。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/img/USTC-CS-Courses-Resource.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
27、[gpt-2](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/openai/gpt-2)：OpenAI 发布的 15 亿参数量通用语言模型 GPT-2，迄今最大模型！展示了一种构建语言处理系统的潜在方式，即根据自然发生的演示学习执行任务。实例代码：
```python
export PYTHONIOENCODING=UTF-8
python3 src/generate_unconditional_samples.py | tee samples
python3 src/generate_unconditional_samples.py --top_k 40 --temperature 0.7 | tee samples
python3 src/interactive_conditional_samples.py --top_k 40
```

28、[deep-learning-drizzle](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kmario23/deep-learning-drizzle)：世界计算机名校的深度学习、强化学习、机器学习、计算机视觉、自然语言处理等方面的公开课

29、[stanza](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/stanfordnlp/stanza)：适用于多种人类语言的 Stanford NLP 官方 Python 库。包含用于运行 CoNLL 2018 共享任务的最新完全神经管道以及访问 Java Stanford CoreNLP 服务器的软件包。实例代码：
```python
import stanfordnlp
stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc.sentences[0].print_dependencies()
```

30、[Tensorflow-Cookbook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/taki0112/Tensorflow-Cookbook)：易学易用的 Tensorflow 教程

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/34/HelloGitHub34.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/36/HelloGitHub36.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
