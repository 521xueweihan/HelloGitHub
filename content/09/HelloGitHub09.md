# 《HelloGitHub》第 09 期
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
- [C++ 项目](#C-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C++ 项目
1、[json](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nlohmann/json)：C++ 的 JSON 库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/img/json-show.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
2、[vim-go](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fatih/vim-go)：Go 的 vim 配置

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
3、[MSEC](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/MSEC)：腾讯开源的毫秒服务引擎（Mass Service Engine in Cluster）。它是一个开源框架，适用于在廉价机器组成的集群上开发和运营分布式后台服务。毫秒服务引擎集 RPC、名字发现服务、负载均衡、业务监控、灰度发布、容量管理、日志管理、key-value 存储于一体，[官网介绍](http://haomiao.qq.com/index.html#documents)

4、[android](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SmartisanTech/android)：锤子开源的 One Step 项目，一步（one step）是通过拖拽完成将信息发送至应用或联系人的动作，节省了在不同应用之间切换的诸多步骤，第一次打通了手持设备中应用间的边界，[One Step](http://www.smartisan.com/m1/#/os?section=onestep)

5、[android-open-project](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Trinea/android-open-project)：Android 开源项目分类汇总

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
6、[vue-hackernews-2.0](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vuejs/vue-hackernews-2.0)：这是一个 Vue2.0 示例，克隆 [Hacker News](https://news.ycombinator.com/) 网站（我感觉比原站好看多了😅）


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/img/vue-hackernews-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

7、[N-blog](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nswbmw/N-blog)：面向新手的 Node.js 教程，该教程讲述了 Node.js 基本知识点，同时结合搭建一个多人博客的实战，从零基础到实际开发，由浅到深帮助新手入门 Node.js 这门语言

8、[pomelo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NetEase/pomelo)：Pomelo 网易开源的一个 Node.js 游戏服务器框架，[Demo](http://pomelo.netease.com/demo.html)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
9、[VulApps](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Medicean/VulApps)：用于快速搭建各种漏洞环境，可用来学习、理解常见的漏洞，增强自己在开发过程的安全意识

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
10、[flask-limiter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alisaifee/flask-limiter)：一个 Flask 的扩展库，它可以根据访问者的 IP 限制其访问频率、次数等。示例代码如下：
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

11、[ngrok](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/inconshreveable/ngrok)：一个十分方便、好用的内网穿透工具，它可以把本地某个端口的服务，通过一个安全隧道，映射到公网的一个地址。同时它提供了一个 Web 页面，展示了每个请求、响应的所有信息，便于调试本地的程序。基本的使用方法如下：
```
ngrok 协议 本地服务监听的端口
ngrok http 8000

创建成功会返回公网地址，然后通过该地址就可以访问到本地的服务。
本地访问 http://localhost:4040，就可以查看关于每个请求、响应的相关数据
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/img/ngrok-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

12、[glances](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nicolargo/glances)：一个可以让你**一目了然**你的系统情况（类 (h)top）的工具，它界面友好，安装方便：`pip install glances`


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/09/img/glances-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
13、[Kingfisher](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/onevcat/Kingfisher)：Kingfisher 是一个异步下载和缓存图片的库，你可以把它看做 SDWebImage 的纯 Swift 实现和替代。它可以帮助简单地实现像是用户头像或者 table view 里面的图片的下载和缓存这样的工作，以提高 app 速度和帮助开发者节省时间，[作者的中文博客](http://project.onevcat.com/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
14、[freecodecamp.cn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FreeCodeCampChina/freecodecamp.cn)：freecodecamp 是一个自由的开源编程社区，[freecodecamp 中文社区](https://freecodecamp.cn)

15、[best-chinese-front-end-blogs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FrankFang/best-chinese-front-end-blogs)：该项目是收集优质的中文前端博客

16、[golang-open-source-projects](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hackstoic/golang-open-source-projects)：中文版 awesome-go

17、[Learn-Algorithms](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nonstriater/Learn-Algorithms)：算法数据结构学习，C 语言实现

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
18、[the-way-to-go_ZH_CN](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/unknwon/the-way-to-go_ZH_CN)：《The Way to Go》中文译本，中文正式名《Go 入门指南》

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
19、[machine-learning-for-software-engineers](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ZuzooVn/machine-learning-for-software-engineers)：自上而下的学习路线，软件工程师的机器学习，[中文版](https://github.com/ZuzooVn/machine-learning-for-software-engineers/blob/master/README-zh-CN.md)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/08/HelloGitHub08.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/10/HelloGitHub10.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
