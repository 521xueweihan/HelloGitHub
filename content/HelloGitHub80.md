# 《HelloGitHub》第 80 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/80) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[cockpit](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cockpit-project/cockpit)：基于 Web 的服务器图形界面。这是一款开源的服务器管理工具，让你可以通过 Web 界面轻松管理 Linux 服务器，支持配置防火墙、Web 终端、容器管理、查看系统日志等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/14049216.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
2、[Malware-Patch](https://hellogithub.com/periodical/statistics/click?target=https://github.com/the1812/Malware-Patch)：阻止 Windows 流氓软件授权的工具。它轻巧、无需后台运行，可用于阻止指定软件的管理员授权。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/133600987.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
3、[Magisk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/topjohnwu/Magisk)：Android 获取 Root 权限的工具。它可以快速、无痛地获得 Android 的超级用户权限，支持 Android 5.0 以上的设备。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/67702184.png' style="max-width:80%; max-height=80%;"></img></p>

4、[osquery](https://hellogithub.com/periodical/statistics/click?target=https://github.com/osquery/osquery)：像数据库一样查询设备的工具。它将操作系统抽象成一个数据库，让用户可以通过 SQL 查询操作系统的运行情况，比如运行中的进程、网络连接、文件和用户。攻击者一般会在运行恶意程序后删掉程序，通过 osquery 可以轻松找到没有源文件的进程。
```shell
osquery> SELECT name, path, pid FROM processes WHERE on_disk = 0;
name = Drop_Agent
path = /Users/jim/bin/dropage
pid = 561
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/22394357.png' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
5、[css-only-chat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kkuchta/css-only-chat)：仅用 CSS 实现网络聊天。前端不用 JavaScript 只用 CSS 实现网络聊天的功能，秘诀是伪选择器加载的背景图像和永远加载的索引页。
```css
.some-button:active {
  background-image: url('some_image.jpg')
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/185419470.gif' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
6、[cadvisor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google/cadvisor)：一款由 Google 开源的容器监控工具。它可以实时统计容器运行时占用的资源，包括 CPU 利用率、内存使用量、网络传输等信息。提供了 Web 可视化页面，能方便用户分析和监控容器运行状态，支持包括 Docker 在内的几乎所有类型的容器。
```
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  --privileged \
  --device=/dev/kmsg \
  gcr.io/cadvisor/cadvisor:$VERSION
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/20653934.png' style="max-width:80%; max-height=80%;"></img></p>

7、[dsq](https://hellogithub.com/periodical/statistics/click?target=https://github.com/multiprocessio/dsq)：可直接用 SQL 查询数据文件的命令行工具。通过该项目无需将数据导入数据库，就能用 SQL 查询文件内的数据，可执行模糊查询、计数、排序等命令，支持 JSON、CSV、Excel、Parquet、YAML 等类型的文件。还可以搭配其它命令行工具(jq)，实现更丰富的功能。来自 [@总钻风](https://hellogithub.com/user/PDzxTYajWgimyF9) 的分享
```shell
$ dsq testdata/userdata.parquet 'select count(*) from {}' | jq
[
  {
    "count(*)": 1000
  }
]
```

8、[json-to-go](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mholt/json-to-go)：立刻将 JSON 转化为 Go 类型定义的工具。这是一个用 JavaScript 写的在线小工具，可以直接将输入的 JSON 转成对应的 Go 类型定义。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/16112842.png' style="max-width:80%; max-height=80%;"></img></p>

9、[pocketbase](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pocketbase/pocketbase)：仅一个文件的开源后端。将 SQLite 数据库、接口服务、登录认证、管理后台等服务器端的功能，做成一个开箱即用的可执行文件。让原本不懂后端开发的用户，也可以通过用户界面快速构建起接口服务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/510607652.png' style="max-width:80%; max-height=80%;"></img></p>

10、[supervisord](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ochinchina/supervisord)：用 Go 重新实现的 supervisord 。开源项目 supervisord 作为 Python 项目中常用的进程管理工具，深受广大开发爱好者的喜欢。但如果在非 Python 环境的情况下，用起来就不是那么顺手啦，所以作者用 Go 重写了 supervisord，编译后可以方便地运行在任何环境下。
```
$ cat supervisor.conf
[program:test]
command = /your/program args
$ supervisord -c supervisor.conf
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/69154291.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
11、[Aegis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/beemdevelopment/Aegis)：一款免费、安全、开源的 2FA 安卓应用。双重认证(2FA) 就是使用两种不同的元素来确认用户身份，比如用户名和密码是一种元素，手机号和短信验证码也是一种元素，两种元素结合就是双重认证。除了短信之外还有一种 APP 可生成和验证码功能类似的一次性密码(TOTP)，Aegis 就是一款支持 HOTP 和 TOTP 算法的开源 2FA 应用，使用时要先将手机和账号绑定，绑定后 APP 就会定时刷新一组随机数字，需要双重认证时输入这串数字即可。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/65757761.png' style="max-width:80%; max-height=80%;"></img></p>

12、[jenkins](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jenkinsci/jenkins)：一款由 Java 编写的开源持续集成工具。做为开源 CI/CD 软件的王者，它专注于自动化你的开发工作流程，具有安装简单、友好的操作页面、易于扩展、分布式的特点，常用来优化项目开发流程或自动化各种任务。
```shell
1. 下载 jar 包
2. 运行：java -jar jenkins.war --httpPort=8080
3. 打开浏览器访问：http://localhost:8080
4. 根据提示完成安装
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/1103607.jpg' style="max-width:80%; max-height=80%;"></img></p>

13、[wvp-GB28181-pro](https://hellogithub.com/periodical/statistics/click?target=https://github.com/648540858/wvp-GB28181-pro)：开箱即用的网络视频平台。基于 GB28181 标准实现的网络视频平台，能够接入摄像机、平台、NVR 等设备、支持视频预览、云台控制、录像查询和回放、无人观看自动断流等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/312830970.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
14、[cypress](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cypress-io/cypress)：基于 JavaScript 的下一代前端测试工具。主要用于浏览器端到端测试的自动化工具，端到端(E2E)测试就是站在用户的角度，模拟实际使用场景的测试方式。Cypress 目前已成主流浏览器端到端测试工具，它运行速度快、上手简单，支持图形化界面可实时观察执行情况，以及截屏和视频记录测试结果。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/31629751.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[Dashboard](https://hellogithub.com/periodical/statistics/click?target=https://github.com/leon-kfd/Dashboard)：一款完全自定义配置的浏览器起始页。基于 Vite+Vue3+TypeScript 构建的浏览器起始页，预设了多款简洁清爽的主题开箱即用，能够随心所欲地添加组件，编辑模式下可拖拽组件更改大小和位置，支持浏览器插件和网页两种使用方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/353963704.png' style="max-width:80%; max-height=80%;"></img></p>

16、[Rocket.Chat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/RocketChat/Rocket.Chat)：一款可自由定制的企业级开源通信平台。功能丰富的通信平台，可自托管做为 Slack 的开源替代品。支持创建频道、团队和讨论等多种不同功能的群聊，消息支持图片、文件、视频和语音，拥有包括 Windows、Linux、macOS、Android 和 iOS 在内的多种客户端。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/35866694.jpg' style="max-width:80%; max-height=80%;"></img></p>

17、[slidev](https://hellogithub.com/periodical/statistics/click?target=https://github.com/slidevjs/slidev)：专为程序员打造的演示文稿工具。该项目是基于 Web 的幻灯片制作和演示工具，让用户可以使用 纯文本+Markdown 语法制作幻灯片，支持导出为 PDF 或 PNG 格式的文件，或以单页面展示幻灯片。对于大多数不擅长做 PPT 的程序员，基于提供的现成主题也可以制作出看起来不错的演示文稿。来自 [@总钻风](https://hellogithub.com/user/PDzxTYajWgimyF9) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/361044034.png' style="max-width:80%; max-height=80%;"></img></p>

18、[the-super-tiny-compiler](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jamiebuilds/the-super-tiny-compiler)：可能是最小的编译器。仅用 1000 行 JavaScript 代码实现的迷你编译器，其中注释还占了一大半，实际代码只有 200 行左右。它虽然代码量不多，但完整地实现了编译器基本功能，可以用来学习编译器原理。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/53639099.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP 项目
19、[YOURLS](https://hellogithub.com/periodical/statistics/click?target=https://github.com/YOURLS/YOURLS)：完全免费的短网址服务。采用 PHP 编写的短网址服务，它完全开源可自行搭建服务，支持数据统计、地理位置、可视化等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/5508585.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
20、[calibre](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kovidgoyal/calibre)：一款功能强大的电子书管理工具。它是集下载、格式转化、制作、管理于一体的电子书工具，比如可以将 txt 文本，转化成包含作者信息和书籍封面的 mobi 文件，制作完成后还可以直接发送到 Kindle 设备上。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/10332822.png' style="max-width:80%; max-height=80%;"></img></p>

21、[changedetection.io](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dgtlmoon/changedetection.io)：简单好用的网站变更检测、监控和通知服务。基于 Flask+Selenium 构建的 Web 服务，可以在目标网站发生变化时发出通知，可用于监控商品降价、工作机会、版本发布、最新内容等，支持 Docker 的安装方式。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/333483116.png' style="max-width:80%; max-height=80%;"></img></p>

22、[Macast](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xfangfang/Macast)：一款轻巧的投屏接收器。该项目可以让电脑接收来自手机的视频、图片和音乐投屏，支持手机上的主流视频和音乐软件，以及其它符合 DLNA 协议的软件。无打扰地运行在状态栏和菜单栏，适用于 Windows、macOS、Linux 操作系统。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/373037895.png' style="max-width:80%; max-height=80%;"></img></p>

23、[reloadium](https://hellogithub.com/periodical/statistics/click?target=https://github.com/reloadware/reloadium)：Python 热重载调试工具。在不重启程序的前提下，通过这个项目可以查看改动后、最新的 Python 代码运行效果，以及每行代码的耗时。有了它可以更高效地调试 Python 代码，强烈推荐在 PyCharm 和 VSCode 上使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/448167075.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[rocketry](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Miksus/rocketry)：更加人性化的 Python 调度库。可通过 Python 装饰器语法，进行任务调度的 Python 库。它简单、优雅、高效，支持定时、并发（异步、多线程、多进程）、条件触发等功能。
```python
from rocketry import Rocketry
from rocketry.conds import daily

app = Rocketry()

@app.task(daily)
def do_daily():
    ...

@app.task(daily & file_exists("data.csv"))
def do_things():
    ...

if __name__ == '__main__':
    app.run()
```

### Rust 项目
25、[difftastic](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Wilfred/difftastic)：命令行文件对比工具。一种可根据文件的语法，进行结构化比较的工具，支持 30 多种编程语言。来自 [@SHOWTA](https://hellogithub.com/user/GAeFLr6oWyYcnbp) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/162276894.png' style="max-width:80%; max-height=80%;"></img></p>

26、[sniffnet](https://hellogithub.com/periodical/statistics/click?target=https://github.com/GyulyVGC/sniffnet)：可轻松监控网络流量的工具。这是一个简单、可靠、炫酷的网络监控应用，可以让你一目了然地了解设备的网络流量。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/519895363.gif' style="max-width:80%; max-height=80%;"></img></p>

27、[websocat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vi/websocat)：WebSockets 的命令行客户端。一条命令连接或建立 WebSockets 服务，适用于 Windows、macOS、Linux。
```shell
A$ websocat -s 1234
Listening on ws://127.0.0.1:1234/
ABC
123

B$ websocat ws://127.0.0.1:1234/
ABC
123
```

### Swift 项目
28、[CotEditor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/coteditor/CotEditor)：一款适用于 macOS 的轻量级纯文本编辑器。它免费、整洁、启动速度快，拥有看起来十分舒服的界面。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/9243402.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
29、[AiLearning-Theory-Applying](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ben1234560/AiLearning-Theory-Applying)：快速上手 AI 理论及应用实战。该教程包含学习 AI 必备的数学基础，机器学习实战小项目、深度学习入门、自然语言通用框架 BERT 实战，以及大量数据集。

30、[vmaf](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Netflix/vmaf)：Netflix 开源的视频质量评估算法。一种将人类视觉模型与机器学习结合的评估视频质量的方法，目的是改善观众们的观看体验。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/51317975.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
31、[fonteditor](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ecomfe/fonteditor)：在线字体编辑器。在线编辑、转换、预览字体文件，支持多种字体格式。来自 [@奈何人间](https://hellogithub.com/user/6oGlnBYh9y4XFDC) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/28329935.jpg' style="max-width:80%; max-height=80%;"></img></p>

32、[free-for-dev](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ripienaar/free-for-dev)：专为程序员准备的免费服务清单。现在虽然有大量免费的服务，但大多数开发者很难找到它们，这是一份免费服务(SaaS、PaaS、IaaS 等)和产品的列表。来自 [@westinyang](https://hellogithub.com/user/jTPCSG8Q2MashYf) 的分享

33、[GameShell](https://hellogithub.com/periodical/statistics/click?target=https://github.com/phyver/GameShell)：玩游戏学习 Shell。这是一款帮助入门 shell 命令的文字游戏。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/94422621.gif' style="max-width:80%; max-height=80%;"></img></p>

34、[hackingtool](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Z4nzu/hackingtool)：黑客工具全家桶。该项目收录了各种黑客工具，包括破解密码、SQL 注入、钓鱼攻击、XSS、DDos 等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/254832799.png' style="max-width:80%; max-height=80%;"></img></p>

35、[platformio-core](https://hellogithub.com/periodical/statistics/click?target=https://github.com/platformio/platformio-core)：专业的嵌入式开发平台。做嵌入式开发时往往会遇到诸多不便，比如硬件厂商的 IDE 绑定和复杂的配置过程。这款 IDE 能让你轻松突破这些限制，PlatformIO IDE 兼容  Arduino、树莓派和 ESP32 在内的 40 多种平台，以及超过 20+ 的框架。它不仅支持 Debug、代码自动补全、单元测试、串口调试等实用的功能，还提供了 VSCode、Vim 等编辑器的插件，把开发工具的选择权彻底地还给开发者。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/19606299.png' style="max-width:80%; max-height=80%;"></img></p>

36、[sms_forwarding](https://hellogithub.com/periodical/statistics/click?target=https://github.com/chenxuuu/sms_forwarding)：超低成本的短信转发器。通过该项目仅需 50 元就可以制作出一个短信转发器，实现不用手机接收验证码。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/558275471.jpg' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
37、[Book3_Elements-of-Mathematics](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Visualize-ML/Book3_Elements-of-Mathematics)：《数学要素》从加减乘除到机器学习。全彩多图的一本科普书，内容以图解+数学+编程为主。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/497668360.png' style="max-width:80%; max-height=80%;"></img></p>

38、[parsing-techniques](https://hellogithub.com/periodical/statistics/click?target=https://github.com/duguying/parsing-techniques)：《Parsing Techniques》解析技术。该书是编译器前端的经典书籍。

39、[py4e](https://hellogithub.com/periodical/statistics/click?target=https://github.com/csev/py4e)：《Python for Everybody》适合所有人的 Python。不管你有没有编程基础，只要对编程感兴趣，都可以通过这本书学会 Python，进入有趣的编程世界。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/80/34169414.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub79.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub81.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/80'>这里</a>。
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
