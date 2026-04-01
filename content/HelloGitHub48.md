# 《HelloGitHub》第 48 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/48) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[DungeonRush](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yujqiao/DungeonRush)：元气贪吃蛇游戏。作者受到元气骑士的启发，基于贪吃蛇进行一些玩法上的创新。该项目适用于 C 语言初学者、第一次尝试使用跨平台图形库的同学，参考本项目就可以写出一个可玩性高的游戏，收获满满成就感


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/242162049.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[libhv](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ithewei/libhv)：一个跨平台、简单易用的非阻塞 IO 事件循环库。用它可以快速的编写 HTTP 客户端/服务端，可提供高性能的 httpd 服务。项目模块划分清晰，代码可读性高，快去看下源代码吧。示例代码：
```c++
#include "HttpServer.h"

int http_api_echo(HttpRequest* req, HttpResponse* res) {
    res->body = req->body;
    return 0;
}

int main() {
    HttpService service;
    service.base_url = "/v1/api";
    service.AddApi("/echo", HTTP_POST, http_api_echo);

    http_server_t server;
    server.port = 8080;
    server.service = &service;
    http_server_run(&server);
    return 0;
}
```


3、[myscan](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nobackdoor/myscan)：开源的多线程 socket 扫描 IP 端口的程序。目前仅支持 Windows 系统，代码简单可作为初学者学习项目
```
命令：
myscan -p Port1[,Port2,Port3...] [-t Thread](default 10) [-d] (DEBUG) StartIp EndIp
例子：
myscan -p 80 192.168.1.1 192.168.1.254
myscan -p 21,22,23,80,443,8080 -t 256 192.168.1.1 192.168.1.254
```


### C++ 项目
4、[contour](https://hellogithub.com/periodical/statistics/click?target=https://github.com/contour-terminal/contour)：一个使用 C++ 17 开发的终端模拟器。可在 Windows、Linux 和 MacOS 三大平台使用，支持字体连字 Font Ligatures（例如 Fira Code 字体）、GPU 加速渲染、背景模糊（Win10、KDE）、256 色、True Color 和配色主题


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/202277409.png' style="max-width:80%; max-height=80%;"></img></p>

5、[milvus](https://hellogithub.com/periodical/statistics/click?target=https://github.com/milvus-io/milvus)：一款开源的、针对海量特征向量的相似性搜索引擎。相比 Faiss 和 SPTAG 这样的算子库，Milvus 提供完整的向量数据更新，索引与查询框架。Milvus 利用 GPU 进行索引加速与查询加速，能大幅提高单机性能。部署使用简单，降低了 AI 应用落地的难度


### CSS 项目
6、[cssgridgenerator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sdras/cssgridgenerator)：在线通过点击动态生成基本的 CSS Grid 代码。[在线尝试](https://cssgrid-generator.netlify.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/188726142.jpeg' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
7、[awesome-golang-algorithm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/6boris/awesome-golang-algorithm)：Go 语言刷 LeetCode。[在线阅读](https://leetcode.gin.sh/)


8、[gops](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google/gops)：展示当前系统运行了哪些 Go 程序的工具，同时支持深入分析的参数
```
# 展示当前运行的所有 Go 程序
$ gops
983   980    uplink-soecks  go1.9   /usr/local/bin/uplink-soecks
52697 52695  gops           go1.10  /Users/jbd/bin/gops
4132  4130   foops        * go1.9   /Users/jbd/bin/foops
51130 51128  gocode         go1.9.2 /Users/jbd/bin/gocode

# 某一个 Go 程序的详细信息
$ gops <pid>
parent PID:	5985
threads:	27
memory usage:	0.199%
cpu usage:	0.139%
username:	jbd
cmd+args:	/Applications/Splice.app/Contents/Resources/Splice Helper.app/Contents/MacOS/Splice Helper -pid 5985
local/remote:	127.0.0.1:56765 <-> :0 (LISTEN)
local/remote:	127.0.0.1:56765 <-> 127.0.0.1:50955 (ESTABLISHED)
local/remote:	100.76.175.164:52353 <-> 54.241.191.232:443 (ESTABLISHED)
```


9、[wtf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wtfutil/wtf)：瞥一眼你的“私人管家”，终端个人信息面板。安装简单，还可通过配置文件设置你想看到的信息。设置可能需要花一些时间，但最终效果还是很可以的


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/127227141.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
10、[dolphinscheduler](https://hellogithub.com/periodical/statistics/click?target=https://github.com/apache/dolphinscheduler)：分布式易扩展的可视化 DAG 工作流任务调度系统。致力于解决数据处理流程中错综复杂的依赖关系，使调度系统在数据处理流程中开箱即用


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/173335706.jpg' style="max-width:80%; max-height=80%;"></img></p>

11、[KCenter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xaecbd/KCenter)：Kafka 集群管理维护、生产消费监控平台


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/248890809.png' style="max-width:80%; max-height=80%;"></img></p>

12、[MusicPlayer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Mpmart08/MusicPlayer)：一款开源的 Java 桌面版音乐播放器，使用 JavaFX/Java 8 技术开发的项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/44499483.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
13、[G2](https://hellogithub.com/periodical/statistics/click?target=https://github.com/antvis/G2)：一套面向常规统计图表，以数据驱动的高交互可视化图形语法，具有高度的易用性和扩展性。使用 G2，你可以无需关注图表各种繁琐的实现细节，一条语句即可使用 Canvas 或 SVG 构建出各种各样的可交互的统计图表。G2 是整个蚂蚁金服 AntV 可视化解决方案中的一个环节，主要针对在高交互、高扩展的二维统计图表


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/59737212.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[gitmoji-cli](https://hellogithub.com/periodical/statistics/click?target=https://github.com/carloscuesta/gitmoji-cli)：Git 交互式客户端，方便在提交信息中增加 emoji 表情。终于知道别人的提交信息为什么会有表情了，效果如下图：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/74069926.png' style="max-width:80%; max-height=80%;"></img></p>

15、[honeyed-words-generator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zerosoul/honeyed-words-generator)：一个“土味情话”在线生成项目。支持生成图片、分享二维码，[在线访问](https://works.yangerxiao.com/honeyed-words-generator/)。你们先看，我看完被撩到了我先去静静


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/240414393.png' style="max-width:80%; max-height=80%;"></img></p>

16、[panolens.js](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pchen66/panolens.js)：基于 WebGL 的全景查看库。效果如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/46604802.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
17、[httpx](https://hellogithub.com/periodical/statistics/click?target=https://github.com/encode/httpx)：使用简单方便，轻松实现异步请求的 HTTP 客户端（Python 3.8+)。示例代码：
```python
>>> import httpx
# 同步
>>> r = httpx.get('https://www.example.org/')
>>> r
<Response [200 OK]>
>>> r.status_code
# 异步
>>> async with httpx.AsyncClient() as client:
>>>     r = await client.get('https://www.example.org/')
>>> r
<Response [200 OK]>
```


18、[iredis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/laixintao/iredis)：Python 语言写的支持自动补全、语法高亮、命令提示等的 Redis 命令行客户端。超好用，真是相见很晚啊


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/166371259.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[python-small-examples](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jackzhenguo/python-small-examples)：Python 有趣、实用的代码示例集合。包含：Python 基础、小技巧、坑、文件操作、机器学习、绘图等，代码如下：
```python
# pyecharts 绘制水球图示例
from pyecharts import options as opts
from pyecharts.charts import Liquid, Page
from pyecharts.globals import SymbolType

def liquid() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.67, 0.30, 0.15])
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid"))
    )
    return c

liquid().render('./img/liquid.html')
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/222183074.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[rssant](https://hellogithub.com/periodical/statistics/click?target=https://github.com/anyant/rssant)：免费开源的 RSS 订阅项目，服务端是 Django 写的。你可以自己部署也可以直接使用[在线版](https://rss.anyant.com/)，远离嘈杂的推荐、广告，专注你订阅的内容


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/229764065.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby 项目
21、[homeland](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ruby-china/homeland)：开源免费、不限制商业使用的社区网站系统


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/3842593.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
22、[autokeras](https://hellogithub.com/periodical/statistics/click?target=https://github.com/keras-team/autokeras)：Keras 官方出品基于 Keras 的 AutoML 系统。支持 CPU 和 GPU 训练，傻瓜式 API，3 行代码就能训练一个模型。目前支持的任务：图像分类、图像回归、文本分类、结构化数据分类等。将人从手工选择超参数中解放出来，快速开发原型，官方口号“所有人都能使用机器学习”，[官网](https://autokeras.com/)
```python
# 安装命令 pip install autokeras
import autokeras as ak

clf = ak.ImageClassifier()
clf.fit(x_train, y_train)
results = clf.predict(x_test)
```


### 其它
23、[browser-2020](https://hellogithub.com/periodical/statistics/click?target=https://github.com/luruke/browser-2020)：该项目汇集了浏览器鲜为人知的一些功能


24、[fucking-algorithm](https://hellogithub.com/periodical/statistics/click?target=https://github.com/labuladong/fucking-algorithm)：解 LeetCode 题目集合。号称“手撕 LeetCode 题目”，虽然之前推荐过不少解题集合，但是这次我还是没忍住。该项目讲究思路指南，解题思路描述清晰，真香啊


25、[learnGitBranching](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pcottle/learnGitBranching)：一个 Git 命令可视化学习项目。能够生动形象的帮助开发人员理解、学习 Git 命令，通过一系列刺激的关卡挑战，逐步深入的学习 Git 的强大功能。[在线尝试](https://learngitbranching.js.org/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/48/5405654.png' style="max-width:80%; max-height=80%;"></img></p>

26、[Waking-Up](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wolverinn/Waking-Up)：采用追问形式的后端面试问题总结。提问然后追问是面试常见模式，更加贴近真实面试




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub47.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub49.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/48'>这里</a>。
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
