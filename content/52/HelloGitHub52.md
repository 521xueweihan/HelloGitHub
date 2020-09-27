# 《HelloGitHub》第 52 期
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
- [C 项目](#C-项目)
- [C# 项目](#C-项目-1)
- [C++ 项目](#C-项目-2)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [Python 项目](#Python-项目)
- [其它](#其它)
- [机器学习](#机器学习)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

**Tips**：如果文中的图刷不出来，可以向我们[反馈](https://github.com/521xueweihan/HelloGitHub/issues/899)。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C 项目
1、[SimpleKernel](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Simple-XX/SimpleKernel)：一个用来练手的简单内核项目。提供了各个阶段完成度不同的内核，可以选择从自己喜欢的地方开始

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/SimpleKernel.jpeg' style="max-width:80%; max-height=80%;"></img></p>

2、[raspberry-pi-os](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/s-matyukevich/raspberry-pi-os)：基于树莓派的操作系统开发教程（还未完结）。你的树莓派在吃灰吗？把它插上电用来学习开发操作系统吧

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
3、[perfview](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/perfview)：微软开源的性能分析工具。配套的教程[视频](https://channel9.msdn.com/Series/PerfView-Tutorial)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/perfview.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
4、[GuiLite](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/idea4good/GuiLite)：引用方便的 C++ 全平台 GUI 库。能够使用在 PC 端、移动设备、物联网设备甚至是没有操作系统的单片机，还支持多种开发语言和三方库

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/GuiLite.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[html-plus-plus](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/csb6/html-plus-plus)：这个库让你可以使用 C++ 模板编写 HTML。HTML 文档被表示为一个单一的、深层嵌套的类型，相当于 HTML 的模版引擎。代码简单可供新手学习和使用，示例代码：
```c++
#include <iostream>
#include "html++.h"

int main()
{
  html<
    head<
      title<"Help Me.">
    >,
    body<
      h1<"The horror!">,
      p<"Someone has probably done this before, but I can see why it didn't catch on.">,
      a<"href=https://github.com/csb6/html-plus-plus", "For science">
    >
  > page;

  std::cout << page.content;
  return 0;
}
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
6、[gotty](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yudai/gotty)：能够把终端执行的命令展示到网页上的工具。安装和运行命令如下：
```
安装：go get github.com/yudai/gotty
运行：gotty [options] <command> [<arguments...>]
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/gotty.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[algo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hoanhan101/algo)：Golang 程序员面试中的问题和解答集合。该项目目前完成了大部分的数据结构和算法部分，准备相关面试的小伙伴可以阅读学习起来了

8、[logrus](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sirupsen/logrus)：可能是 Go 目前最受欢迎的第三方日志库。日志首先要能让人看懂，其次是程序易于处理日志包含的内容，logrus 也许能让你轻松快速实现上述两点

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/logrus.png' style="max-width:80%; max-height=80%;"></img></p>

9、[websocket](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gorilla/websocket)：Go 的 websocket 三方库。看看它和标准库的对比，你就知道为什么它会出现在本期月刊中了

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/websocket.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
10、[FlappyBird](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kingyuluk/FlappyBird)：Java 标准库实现的 Flappy Bird。优化了游戏难度并加入移动型水管，增加可玩性。没有采用第三方库和游戏引擎、项目结构简单、代码注释完整，适合 Java 初学者做为编程入门实战项目

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/FlappyBird.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[metersphere](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/metersphere/metersphere)：一站式的开源企业级持续测试平台。适应场景包括：测试跟踪、接口测试、性能测试等，兼容 JMeter 等开源标准，能够帮助开发和测试团队充分利用云弹性进行高度可扩展的自动化测试。测试同学的福音

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/metersphere.png' style="max-width:80%; max-height=80%;"></img></p>

12、[incubator-iotdb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apache/incubator-iotdb)：清华大学软件学院自主研发并开源的时间序列数据管理引擎。能够有效应对工业物联网领域时间序列数量多、写入频率高、数据乱序到达、秒级聚合等场景。官方网站有系统设计文档和使用手册，作为初学者，可以系统的学习数据库系统的完整设计和实现。在 IoTDB 社区可以与国内用户直接交流、收集需求、设计功能、性能优化，每个改进点都可以看到直接效果。还可以体验 Apache 开源软件的工作模式，与世界各地的开发者交流想法，也有机会成为 Apache Committer、PMC 等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/incubator-iotdb.png' style="max-width:80%; max-height=80%;"></img></p>

13、[MyBookshelf](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gedoor/MyBookshelf)：免费开源的安卓小说阅读软件，能够自定义订阅小说数据源。支持：
- 全局状态栏沉浸
- 自定义多线程搜索、缓存
- 支持一键缓存
- 点击章节名跳转小说目录
- 自定义字体、阅读背景、文字颜色、背景颜色
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/MyBookshelf.png' style="max-width:80%; max-height=80%;"></img></p>

14、[QMUI_Android](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/QMUI_Android)：用于辅助快速搭建一个具备基本还原设计效果的 Android 项目。快速搭建一个 Demo App 的必备利器，[官网](https://qmuiteam.com/android)还提供示例 App 下载，感兴趣的小伙伴快去试试吧

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/QMUI_Android.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
15、[chrome-extensions-searchReplace](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Summer-andy/chrome-extensions-searchReplace)：一款搜索并且替换文本的谷歌插件。在做产品 PPT 的时候，需要对某些个页面中的一些名词进行统一替换，这个插件就是为了解决这个问题而诞生的。同时作者也是调研了其他类似功能的插件，它们都包含或多或少的问题，最终作者自己动手做了这个项目。可以说这款替换插件应该就是你最终的选择了

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/chrome-extensions-searchReplace.png' style="max-width:80%; max-height=80%;"></img></p>

16、[apidoc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apidoc/apidoc)：根据代码中的注释生成 RESTful 风格的 API 文档。注释示例：
```
/**
 * @api {get} /user/:id Request User information
 * @apiName GetUser
 * @apiGroup User
 *
 * @apiParam {Number} id User's unique ID.
 *
 * @apiSuccess {String} firstname Firstname of the User.
 * @apiSuccess {String} lastname  Lastname of the User.
 */
```

17、[mongo-express](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mongo-express/mongo-express)：使用 Node.js、Express 和 Bootstrap3 编写的 MongoDB 管理平台

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/mongo-express.png' style="max-width:80%; max-height=80%;"></img></p>

18、[Zettlr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Zettlr/Zettlr)：开源免费支持多种操作系统的 Markdown 编辑器。如果你想尝试一款新的 Markdown 编辑器，它或许能满足你对编辑器所有想法，如果还不够那就自己动手增加吧

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/Zettlr.png' style="max-width:80%; max-height=80%;"></img></p>

19、[leetcode-cli](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/skygragon/leetcode-cli)：LeetCode 的命令行工具。之前我们推荐过命令行斗地主、划水逛社区等，真正努力的人用命令行来刷算法题！我颤抖了

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/leetcode-cli.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
20、[Zebra](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zbrateam/Zebra)：用于越狱的 iOS 设备的软件包管理器

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/Zebra.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
21、[ar-cutpaste](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cyrildiagne/ar-cutpaste)：AR 拷贝实物照片到 PS 软件的工具。它可以通过 iPhone 或者 Android 手机将真实物品从周围环境中抠出来，并粘贴到 Photoshop 中，未来还会支持其它软件

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/ar-cutpaste.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[ncmdump](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nondanee/ncmdump)：网易云音乐下载的 NCM 文件转化工具

23、[nginx-ui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/schenkd/nginx-ui)：在线修改 Nginx 配置的服务。总的来说还是能减少修改配置出错的概率，而且不用面对漆黑枯燥的命令行了

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/nginx-ui.png' style="max-width:80%; max-height=80%;"></img></p>

24、[python-dotenv](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/theskumar/python-dotenv)：帮你更好的管理 Python 项目中敏感配置信息的开源三方库。在项目中会有一些数据库、账户、KEY 等敏感信息，这些信息最好不要写在源代码中。为了降低泄漏风险，一般会通过环境变量来设置，这个库可以很方便帮你在 Python 项目中管理这些信息。示例代码：
```python
# 安装：pip install -U python-dotenv
# 目录结构：
.
├── .env
└── settings.py
# 示例代码
# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("EMAIL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
25、[analytics](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/plausible/analytics)：一个开源的轻量级 Web 访问分析工具。如果你不想侵犯用户的隐私，只获取自己网站访问的基本数据，可以试试这个项目，用来代替谷歌分析

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/analytics.png' style="max-width:80%; max-height=80%;"></img></p>

26、[data-scientist-roadmap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MrMimic/data-scientist-roadmap)：数据科学技能路线图

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/data-scientist-roadmap.png' style="max-width:80%; max-height=80%;"></img></p>

27、[nvda](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nvaccess/nvda)：一个微软开源的免费 Windows 操作系统的无视觉桌面访问阅读器。通过合成器语音或者盲文点字的反馈，方便盲人和低视力人群使用运行在 Windows 操作系统下运作的电脑。也能够让开发者了解微软的常见的辅助功能接口，如微软 Active Accessibility、Java Access Bridge、IAccessible2 和 UI automation。希望有更多的人了解无障碍，[NVDA 中文站](https://www.nvdacn.com/)

28、[LeetcodeTop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/afatcoder/LeetcodeTop)：国内各大互联网公司常考的 LeetCode 题目

29、[git-history](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pomber/git-history)：在线查看 GitHub 开源项目中文件的改动历史的工具。使用方法：
```
1. 打开 GitHub 上任意一个项目的文件
2. 把地址中的 github.com 替换成 githistory.xyz
3. 访问替换后的地址
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/git-history.png' style="max-width:80%; max-height=80%;"></img></p>

30、[github-readme-stats](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/anuraghazra/github-readme-stats)：在你的 README 中展示动态生成的 GitHub 统计信息。使用简单、样式多样，使用方法：
```
[![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=521xueweihan)](https://github.com/anuraghazra/github-readme-stats)

替换“521xueweihan”为你的 GitHub 用户名
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/github-readme-stats.png' style="max-width:80%; max-height=80%;"></img></p>

31、[papirus-icon-theme](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)：适用于 Linux 系统的免费开源 SVG 图标主题

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/papirus-icon-theme.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
32、[3d-photo-inpainting](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vt-vl-lab/3d-photo-inpainting)：一个把单张静态照片转化成 3D 图片的项目。快来尝鲜啦，不要等朋友圈 3D 照片刷屏后才“后知后觉”

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/52/img/3d-photo-inpainting.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/51/HelloGitHub51.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/53/HelloGitHub53.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
