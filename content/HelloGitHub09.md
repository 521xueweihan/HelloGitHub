# 《HelloGitHub》第 09 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/09) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C++ 项目
1、[json](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nlohmann/json)：C++ 的 JSON 库



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/11171548.gif' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
2、[vim-go](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fatih/vim-go)：Go 的 vim 配置


### Java 项目
3、[android](https://hellogithub.com/periodical/statistics/click?target=https://github.com/SmartisanTech/android)：锤子开源的 One Step 项目，一步（one step）是通过拖拽完成将信息发送至应用或联系人的动作，节省了在不同应用之间切换的诸多步骤，第一次打通了手持设备中应用间的边界，[One Step](http://www.smartisan.com/m1/#/os?section=onestep)


4、[android-open-project](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Trinea/android-open-project)：Android 开源项目分类汇总


5、[MSEC](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Tencent/MSEC)：腾讯开源的毫秒服务引擎（Mass Service Engine in Cluster）。它是一个开源框架，适用于在廉价机器组成的集群上开发和运营分布式后台服务。毫秒服务引擎集 RPC、名字发现服务、负载均衡、业务监控、灰度发布、容量管理、日志管理、key-value 存储于一体，[官网介绍](http://haomiao.qq.com/index.html#documents)


### JavaScript 项目
6、[N-blog](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nswbmw/N-blog)：面向新手的 Node.js 教程，该教程讲述了 Node.js 基本知识点，同时结合搭建一个多人博客的实战，从零基础到实际开发，由浅到深帮助新手入门 Node.js 这门语言


7、[pomelo](https://hellogithub.com/periodical/statistics/click?target=https://github.com/NetEase/pomelo)：Pomelo 网易开源的一个 Node.js 游戏服务器框架，[Demo](http://pomelo.netease.com/demo.html)


8、[vue-hackernews-2.0](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vuejs/vue-hackernews-2.0)：这是一个 Vue2.0 示例，克隆 [Hacker News](https://news.ycombinator.com/) 网站（我感觉比原站好看多了😅）



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/65052980.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
9、[VulApps](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Medicean/VulApps)：用于快速搭建各种漏洞环境，可用来学习、理解常见的漏洞，增强自己在开发过程的安全意识


### Python 项目
10、[flask-limiter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alisaifee/flask-limiter)：一个 Flask 的扩展库，它可以根据访问者的 IP 限制其访问频率、次数等。示例代码如下：
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


11、[glances](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nicolargo/glances)：一个可以让你**一目了然**你的系统情况（类 (h)top）的工具，它界面友好，安装方便：`pip install glances`



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/2909429.png' style="max-width:80%; max-height=80%;"></img></p>

12、[ngrok](https://hellogithub.com/periodical/statistics/click?target=https://github.com/inconshreveable/ngrok)：一个十分方便、好用的内网穿透工具，它可以把本地某个端口的服务，通过一个安全隧道，映射到公网的一个地址。同时它提供了一个 Web 页面，展示了每个请求、响应的所有信息，便于调试本地的程序。基本的使用方法如下：
```
ngrok 协议 本地服务监听的端口
ngrok http 8000

创建成功会返回公网地址，然后通过该地址就可以访问到本地的服务。
本地访问 http://localhost:4040，就可以查看关于每个请求、响应的相关数据
```



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/8900723.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
13、[Kingfisher](https://hellogithub.com/periodical/statistics/click?target=https://github.com/onevcat/Kingfisher)：Kingfisher 是一个异步下载和缓存图片的库，你可以把它看做 SDWebImage 的纯 Swift 实现和替代。它可以帮助简单地实现像是用户头像或者 table view 里面的图片的下载和缓存这样的工作，以提高 app 速度和帮助开发者节省时间，[作者的中文博客](http://project.onevcat.com/)


### 人工智能
14、[machine-learning-for-software-engineers](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ZuzooVn/machine-learning-for-software-engineers)：自上而下的学习路线，软件工程师的机器学习，[中文版](https://github.com/ZuzooVn/machine-learning-for-software-engineers/blob/master/README-zh-CN.md)


### 其它
15、[best-chinese-front-end-blogs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/FrankFang/best-chinese-front-end-blogs)：该项目是收集优质的中文前端博客


16、[freecodecamp.cn](https://hellogithub.com/periodical/statistics/click?target=https://github.com/FreeCodeCampChina/freecodecamp.cn)：freecodecamp 是一个自由的开源编程社区，[freecodecamp 中文社区](https://freecodecamp.cn)


17、[golang-open-source-projects](https://hellogithub.com/periodical/statistics/click?target=https://github.com/hackstoic/golang-open-source-projects)：中文版 awesome-go


18、[Learn-Algorithms](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nonstriater/Learn-Algorithms)：算法数据结构学习，C 语言实现


### 开源书籍
19、[the-way-to-go_ZH_CN](https://hellogithub.com/periodical/statistics/click?target=https://github.com/unknwon/the-way-to-go_ZH_CN)：《The Way to Go》中文译本，中文正式名《Go 入门指南》




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub08.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub10.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/09'>这里</a>。
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
