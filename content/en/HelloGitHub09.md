# HelloGitHub Vol.09
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C++
1、[json](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nlohmann/json)：C++ 的 JSON 库



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/11171548.gif' style="max-width:80%; max-height=80%;"></img></p>

### Go
2、[vim-go](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fatih/vim-go)：Go 的 vim 配置


### Java
3、[android](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SmartisanTech/android)：锤子开源的 One Step 项目，一步（one step）是通过拖拽完成将信息发送至应用或联系人的动作，节省了在不同应用之间切换的诸多步骤，第一次打通了手持设备中应用间的边界，[One Step](http://www.smartisan.com/m1/#/os?section=onestep)


4、[android-open-project](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Trinea/android-open-project)：Android 开源项目分类汇总


5、[MSEC](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Tencent/MSEC)：腾讯开源的毫秒服务引擎（Mass Service Engine in Cluster）。它是一个开源框架，适用于在廉价机器组成的集群上开发和运营分布式后台服务。毫秒服务引擎集 RPC、名字发现服务、负载均衡、业务监控、灰度发布、容量管理、日志管理、key-value 存储于一体，[官网介绍](http://haomiao.qq.com/index.html#documents)


### JavaScript
6、[N-blog](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nswbmw/N-blog)：面向新手的 Node.js 教程，该教程讲述了 Node.js 基本知识点，同时结合搭建一个多人博客的实战，从零基础到实际开发，由浅到深帮助新手入门 Node.js 这门语言


7、[pomelo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NetEase/pomelo)：Pomelo 网易开源的一个 Node.js 游戏服务器框架，[Demo](http://pomelo.netease.com/demo.html)


8、[vue-hackernews-2.0](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vuejs/vue-hackernews-2.0)：这是一个 Vue2.0 示例，克隆 [Hacker News](https://news.ycombinator.com/) 网站（我感觉比原站好看多了😅）



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/65052980.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP
9、[VulApps](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Medicean/VulApps)：用于快速搭建各种漏洞环境，可用来学习、理解常见的漏洞，增强自己在开发过程的安全意识


### Python
10、[flask-limiter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alisaifee/flask-limiter)：一个 Flask 的扩展库，它可以根据访问者的 IP 限制其访问频率、次数等。示例代码如下：
```python
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    global_limits=["2 per minute", "1 per second"],
)

@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return "24"

@app.route("/fast")
def fast():
    return "42"

@app.route("/ping")
@limiter.exempt
def ping():
    return 'PONG'

app.run()
```


11、[glances](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nicolargo/glances)：一个可以让你**一目了然**你的系统情况（类 (h)top）的工具，它界面友好，安装方便：`pip install glances`



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/2909429.png' style="max-width:80%; max-height=80%;"></img></p>

12、[ngrok](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/inconshreveable/ngrok)：一个十分方便、好用的内网穿透工具，它可以把本地某个端口的服务，通过一个安全隧道，映射到公网的一个地址。同时它提供了一个 Web 页面，展示了每个请求、响应的所有信息，便于调试本地的程序。基本的使用方法如下：
```
ngrok 协议 本地服务监听的端口
ngrok http 8000

创建成功会返回公网地址，然后通过该地址就可以访问到本地的服务。
本地访问 http://localhost:4040，就可以查看关于每个请求、响应的相关数据
```



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/8900723.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
13、[Kingfisher](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/onevcat/Kingfisher)：Kingfisher 是一个异步下载和缓存图片的库，你可以把它看做 SDWebImage 的纯 Swift 实现和替代。它可以帮助简单地实现像是用户头像或者 table view 里面的图片的下载和缓存这样的工作，以提高 app 速度和帮助开发者节省时间，[作者的中文博客](http://project.onevcat.com/)


### AI
14、[machine-learning-for-software-engineers](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ZuzooVn/machine-learning-for-software-engineers)：自上而下的学习路线，软件工程师的机器学习，[中文版](https://github.com/ZuzooVn/machine-learning-for-software-engineers/blob/master/README-zh-CN.md)


### Other
15、[best-chinese-front-end-blogs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/FrankFang/best-chinese-front-end-blogs)：该项目是收集优质的中文前端博客


16、[freecodecamp.cn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/FreeCodeCampChina/freecodecamp.cn)：freecodecamp 是一个自由的开源编程社区，[freecodecamp 中文社区](https://freecodecamp.cn)


17、[golang-open-source-projects](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hackstoic/golang-open-source-projects)：中文版 awesome-go


18、[Learn-Algorithms](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nonstriater/Learn-Algorithms)：算法数据结构学习，C 语言实现


### Book
19、[the-way-to-go_ZH_CN](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/unknwon/the-way-to-go_ZH_CN)：《The Way to Go》中文译本，中文正式名《Go 入门指南》




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub08.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub10.md">『Next』</a>
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
