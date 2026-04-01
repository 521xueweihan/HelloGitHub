# HelloGitHub Vol.35
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
1、[IdentityServer4.Admin](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/skoruba/IdentityServer4.Admin)：免费开源的 IdentityServer4 与 Asp.Net Core Identity 管理器。IdentityServer4 官方的管理器是收费的，该项目很好的替代了官方管理器，可以方便的管理使用 IdentityServer4 所搭建的认证服务器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/121049045.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
2、[FLIF](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/FLIF-hub/FLIF)：免费、新颖的无损图像格式。压缩比方面优于 PNG、lossless WebP、lossless BPG、lossless JPEG2000 等格式


### Go
3、[1m-go-websockets](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/eranyanay/1m-go-websockets)：该项目演示了如何用 Go 编写一个可以提供超过一百万个 websockets 连接、运行内存小于 1GB 的服务器。`setup.sh` 是用来创建 websocket 客户端的，`destroy.sh` 则用来销毁客户端


4、[cds](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ovh/cds)：企业级开源持续集成系统。支持横向扩展、自带 UI、常用的持续集成构建等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/70572539.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[docui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/skanehira/docui)：终端 Docker 管理工具，自带一个终端界面。使用该工具可以方便的通过界面管理 docker 不用再记那些命令。安装命令：
```
# Homebrew
$ brew tap skanehira/docui
$ brew install docui

# go get
$ go get -d github.com/skanehira/docui
$ cd $GOPATH/src/github.com/skanehira/docui
$ GO111MODULE=on go install
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/147890536.png' style="max-width:80%; max-height=80%;"></img></p>

6、[go-echarts](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/go-echarts/go-echarts)：Golang 代码生成对应的 echarts 可视化图表。实例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/165092572.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java
7、[APIJSON](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Tencent/APIJSON)：快速开发 API 服务的框架。为简单的增删改查、复杂的查询、简单的事务操作提供了完全自动化的 API。大部分 HTTP 请求后端再也不用写接口了，也不用写文档了，适合中小型前后端分离的项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/74359442.jpg' style="max-width:80%; max-height=80%;"></img></p>

8、[halo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/halo-dev/halo)：Java 博客系统。在层出不穷的博客系统中，很难看到使用 Java 编写的简洁优雅的博客系统。该项目还具备着轻快且功能强大的特点，这些特性使它从众多 Java 博客系统脱颖而出。安装命令：
```
# 安装 Halo
$ yum install -y wget && wget -O halo-cli.sh https://git.io/fxHqp && bash halo-cli.sh -i
# 更新 Halo
$ bash halo-cli.sh -u
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/126178683.png' style="max-width:80%; max-height=80%;"></img></p>

9、[IQL](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/teeyog/IQL)：基于 SparkSQL 实现了一套即席查询服务，具有如下特性：
- 优雅的交互方式，支持多种 datasource/sink、多数据源混算
- Spark 常驻服务，基于 zookeeper 的引擎自动发现
- 多 session 模式实现并行查询
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/127410260.png' style="max-width:80%; max-height=80%;"></img></p>

10、[SpringBoot-Learning](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dyc87112/SpringBoot-Learning)：Spring Boot 教程


### JavaScript
11、[ant-design-vue](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vueComponent/ant-design-vue)：Ant Design 的 Vue 实现，该项目已经得到 [Ant Design 官方](https://vue.ant.design/docs/vue/introduce-cn/)认可


12、[Chart.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chartjs/Chart.js)：基于 canvas 的可视化库。可用于构建简单的 H5 图表，满足基本的日常可视化需求


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/8843683.png' style="max-width:80%; max-height=80%;"></img></p>

13、[Gitter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nslogx/Gitter)：GitHub 的小程序客户端。UI 设计漂亮，可作为小程序和 GitHub 结合的实战项目学习


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/164824151.png' style="max-width:80%; max-height=80%;"></img></p>

14、[Motrix](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/agalwood/Motrix)：免费开源功能齐全的下载工具。技术展采用 Vue + VueX + Element，不仅界面简洁大方而且支持下载 BT、磁力链等资源。如果你受够了下载限速、弹框广告等，就快来 Motrix 享受“纯”下载的平静吧！技术栈适合学习桌面应用开发
- 支持 Windows、Linux、macOS
- 最高支持 10 个任务同时下载
- 单任务最高支持 64 线程下载
- 设置上传/下载限速
- 移除任务时可同时删除相关文件
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/162279822.png' style="max-width:80%; max-height=80%;"></img></p>

15、[rainbow](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ccampbell/rainbow)：体积小、易于使用、支持各种编程语言的语法高亮插件。该项目原理是通过正则过滤关键字，然后进行高亮。代码：
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


### Objective-C
16、[iWeChat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lefex/iWeChat)：还原、探索微信 APP 的项目。通过该项目借鉴、学习微信客户端开发的相关设计与技术，也可以学到如何分析一个第三方 APP 的方法


### Python
17、[ruia](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/howie6879/ruia)：基于 asyncio 和 aiohttp 的 Python3 异步爬虫框架。它具有容易上手、非阻塞、扩展性强等特点，实例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/140359487.png' style="max-width:80%; max-height=80%;"></img></p>

18、[spug](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/openspug/spug)：使用 Python+Vue 实现的开源运维平台，前后端分离方便二次开发。该项目基于 Docker 镜像发布部署，方便安装和升级。支持运维常见功能：主机管理、任务计划管理、发布部署、监控告警等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/119708446.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
19、[deep-learning-drizzle](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kmario23/deep-learning-drizzle)：世界计算机名校的深度学习、强化学习、机器学习、计算机视觉、自然语言处理等方面的公开课


20、[gpt-2](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/openai/gpt-2)：OpenAI 发布的 15 亿参数量通用语言模型 GPT-2，迄今最大模型！展示了一种构建语言处理系统的潜在方式，即根据自然发生的演示学习执行任务。实例代码：
```python
export PYTHONIOENCODING=UTF-8
python3 src/generate_unconditional_samples.py | tee samples
python3 src/generate_unconditional_samples.py --top_k 40 --temperature 0.7 | tee samples
python3 src/interactive_conditional_samples.py --top_k 40
```


21、[stanza](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/stanfordnlp/stanza)：适用于多种人类语言的 Stanford NLP 官方 Python 库。包含用于运行 CoNLL 2018 共享任务的最新完全神经管道以及访问 Java Stanford CoreNLP 服务器的软件包。实例代码：
```python
import stanfordnlp
stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc.sentences[0].print_dependencies()
```


22、[Tensorflow-Cookbook](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/taki0112/Tensorflow-Cookbook)：易学易用的 Tensorflow 教程


### Other
23、[devhub](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/devhubapp/devhub)：支持 Android、iOS、Web、Desktop 的 GitHub 管理通知客户端。能够帮你方便地接收、查看、管理 GitHub 消息、动态等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/75236196.jpg' style="max-width:80%; max-height=80%;"></img></p>

24、[Micro8](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Micropoor/Micro8)：浸淫渗透攻击的老鸟所写，内容一线深入浅出，主要是 Windows 系统场景。对于初中级安全从业人员、乙方安全测试、甲方安全自检、网络安全爱好者等提高都有很大的帮助


25、[neovim](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/neovim/neovim)：致力于改善 Vim 的维护、可扩展性等方面的编辑器。它功能强大、项目开发活跃、社区活跃，“新一代”的 Vim


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/16408992.png' style="max-width:80%; max-height=80%;"></img></p>

26、[OI-wiki](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/OI-wiki/OI-wiki)：免费、开放、持续更新的编程竞赛相关知识教程。包含竞赛的基础知识、常见题型、解题思路以及常用工具等内容，帮助大家更快速、深入地学习编程竞赛相关知识


27、[USTC-Course](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/USTC-Resource/USTC-Course)：该仓库收录中国科学技术大学众多课程资源。包括电子版教材、参考书、讲义、试卷、学习心得、习题解答等。以计算机学院课程为主，也包含公选课、自由选修等其他课程。


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/35/164782828.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
28、[cppwasm-book](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/3dgen/cppwasm-book)：《C/C++ 面向 WebAssembly 编程》，[在线阅读](https://3dgen.cn/cppwasm-book/)


29、[d2l-zh](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/d2l-ai/d2l-zh)：《Dive into Deep Learning 》翻译版，即《动手学深度学习》。[在线阅读](http://zh.d2l.ai/)


30、[You-Dont-Know-JS](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/getify/You-Dont-Know-JS)：（英文）深入探讨 JavaScript 语言核心机制的书籍，适用于深入学习 JS。该书已出版，但在线阅读免费




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub34.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub36.md">『Next』</a>
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
