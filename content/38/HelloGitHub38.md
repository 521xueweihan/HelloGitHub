# 《HelloGitHub》第 38 期
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
- [Ruby 项目](#Ruby-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [教程](#教程)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C++ 项目
1、[terminal](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/terminal)：微软开源的一个全新、现代、功能丰富、高效的 Windows 终端应用程序。它支持 Windows 命令行社区最常用的许多命令，还支持选项卡、富文本、全球化、可配置性、主题和样式等功能。一直以来 Windows 不被开发者青睐的原因之一就是终端不好用，现在有了这个我都想买个 Windows 系统的电脑了（确定不是打游戏？）

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/Terminal.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
2、[golang-developer-roadmap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Alikhll/golang-developer-roadmap)：成为 Go 开发者的学习路线图，[中文版](https://github.com/Alikhll/golang-developer-roadmap/blob/master/i18n/ReadMe-zh-CN.md)

3、[scheduler](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/prprprus/scheduler)：Go 语言实现的作业调度工具包。适用于需要任务调度的场景，能够让初学者学到 time、reflect 等标准库的用法，[中文文档](https://github.com/prprprus/scheduler/blob/master/README-zh.md)

4、[nic](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/EddieIvan01/nic)：一个易用的 HTTP Request 包。它封装了 Go 的 HTTP 标准库，提供了简洁优雅的 API。可以更轻松的发送HTTP 请求，解决了 Go 标准库自定义 HTTP 请求，操作 headers、cookies 时繁琐的步骤。类似于 Python 的 Requests 和 urllib 的区别。示例代码：
```go
resp, err := nic.Get("http://example.com", nil)
if err != nil {
    log.Fatal(err.Error())
}
fmt.Println(resp.Text)
```

5、[redis-tui](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mylxsw/redis-tui)：炫酷的 redis 命令行图形界面工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/redis-tui.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[gameboy.live](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HFO4/gameboy.live)：Gameboy 模拟器，还可以通过 socket 远程玩
```
# 下载
git clone https://github.com/HFO4/gameboy.live.git
# 运行
cd gameboy.live
go build -o gbdotlive main.go

# 命令说明
Usage of gbdotlive:
  -G    Play specific game in Fyne GUI mode  # 用 Fyne GUI 模式玩游戏，会弹出一个窗口
  -c config # 配置文件路径
        Set the game option list config file path
  -d    Use Debugger in GUI mode # GUI 的 debug 模式
  -f FPS
        Set the FPS in GUI mode (default 60) # FPS 设定
  -g    Play specific game in GUI mode (default true) # 是否默认启动 GUI
  -h    This help # 显示帮助
  -m    Turn on sound in GUI mode (default true) # GUI 模式下是否有声音
  -p port
        Set the port for the cloud-gaming server (default 1989) # 默认监听端口，可以用 Telnet 玩
  -r ROM # 游戏 ROM 的路径
        Set ROM file path to be played in GUI mode
  -s    Start a cloud-gaming server # 启动服务器，用 Telnet 玩
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/gameboy.png' style="max-width:80%; max-height=80%;"></img></p>

7、[CovenantSQL](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CovenantSQL/CovenantSQL)：具有区块链特性的去中心化 SQL 关系型数据库。可以提供 DBaaS 服务，去中心化存储保证用户隐私。[中文文档](https://developers.covenantsql.io/docs/zh-CN/intro)，MacOS 系统可以通过 `brew install cql` 直接安装

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/CovenantSQL.png' style="max-width:80%; max-height=80%;"></img></p>

8、[diving](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vicanso/diving)：基于 [dive](https://github.com/wagoodman/dive) 分析 docker 镜像，界面化展示了镜像每层的变动（增加、修改、删除等）、用户层数据大小等信息。便捷获取镜像信息和每层镜像内容的文件树，可以方便地浏览镜像信息。对于需要优化镜像体积时非常方便

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/diving.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
9、[rhizobia_J](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/momosecurity/rhizobia_J)：陌陌开源的 Java 安全编码规范和 SDK

10、[generator-jhipster](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jhipster/generator-jhipster)：用于在几秒钟内创建 Spring Boot + Angular/React 项目的开源应用程序生成器（脚手架）。它可以自动化生成一个完整 Web 应用或微服务架构，加快项目的开发效率。特点和技术栈：
- 基于 Spring Boot 框架的服务端，具备高性能和高可用的 Java 技术栈
- 基于 Angular、React、Bootstrap 的时尚、现代、移动优先的前端
- 基于 JHipster Registry、Netflix OSS、ELK 堆栈和 Docker 的强大的微服务架构
- 使用 Yeoman、Webpack 和 Maven/Gradle 构建应用程序的强大工作流程

11、[Gloading](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/luckybilly/Gloading)：深度解耦的 Android 加载组件，特点：
- 深度解耦 App 中全局加载中、加载失败及空数据视图
- 分离全局加载状态视图的实现和使用
- 不需要在每个页面的布局文件中额外添加加载状态视图
- 可用于 Activity，也可用于为某个 View 显示加载状态等

```java
Gloading.initDefault(new GlobalAdapter());
Gloading.Holder holder = Gloading.getDefault().wrap(activity).withRetry(retryTask);
Gloading.Holder holder = Gloading.getDefault().wrap(view).withRetry(retryTask);

//显示加载中的UI状态
holder.showLoading() 

//显示加载成功的UI状态
holder.showLoadSuccess()

//显示加载失败的UI状态
holder.showFailed()

//显示加载成功，但数据未空的UI状态
holder.showEmpty()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/Gloading.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[Android-BLE](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/aicareles/Android-BLE)：Android 蓝牙框架，包括扫描、连接、设置通知、发送数据、读取、接收数据和 OTA 升级等。近乎一行代码植入项目，可扩展、配置蓝牙相关操作，适用于 Android-BLE4.0 蓝牙。即便是 BLE 方面的小白也可以在短短几分钟内接入并运用到项目中

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/Android-BLE.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
13、[practice](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mintsweet/practice)：使用当下流行的多种不同前端技术栈，实现不同项目的详细教程，教你如何快速上手这些技术。虽然项目名称叫做 `Practice` 但是内容为当前前端最火的框架实践，而且符合生产环境下的开发流程规范，推荐学习

14、[ieaseMusic](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/trazyn/ieaseMusic)：基于网易云音乐 API 开发的第三方客户端，支持 Linux、Mac OS 系统。成熟的 JS 桌面应用产品，颜值很高，音乐资源丰富

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/ieaseMusic.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[ts-utility-plugins](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ddzy/ts-utility-plugins)：使用原生 TS 构建特效、插件、业务的实践教程项目。脱离各种框架实现原生的特效以及插件

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
16、[PHP-Interview-QA](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/colinlet/PHP-Interview-QA)：《PHP 面试问答》结合实际 PHP 面试经验，系统地汇总面试中的各类的问题，并尝试提供简洁准确的答案，为你面试 PHP 相关岗位提供“秘籍”。包含：网络协议、数据结构与算法、PHP基础、Web、MySQL、Redis、自我介绍、离职原因、职业规划等部分

17、[wizard](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mylxsw/wizard)：一款基于 Laravel 开发框架的开源文档管理系统。目前已经在多家公司部署使用，支持：Markdown、Swagger 文档管理，公司内部的统一身份认证系统（LDAP）等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/wizard.jpeg' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
18、[PySnooper](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cool-RR/PySnooper)：Python 的第三方调试库。让你通过装饰器方法，方便的知道每一行程序运行后的结果，而不需要再手动增加 `print` 展示过程数据、调试程序。示例代码：
```python
import pysnooper

@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]

number_to_bits(6)
# 输出如下
Starting var:.. number = 6
15:29:11.327032 call         4 def number_to_bits(number):
15:29:11.327032 line         5     if number:
15:29:11.327032 line         6         bits = []
New var:....... bits = []
15:29:11.327032 line         7         while number:
15:29:11.327032 line         8             number, remainder = divmod(number, 2)
New var:....... remainder = 0
Modified var:.. number = 3
....
```

19、[Python-100-Days](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jackfrued/Python-100-Days)：《Python 100 天从新手到大师》—— Python 的入门学习资料，学习曲线低。非专业人士也能上手学习，适合新手入门

20、[Zvm](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/5A59/Zvm)：一款用 Python 实现的简易 JVM。实现功能如下：class 文件解析、类加载、运行时数据区、指令解释器、基本指令集、简易 GC、简易线程、简易 JDK 库，可以运行基本的 Java class 文件。代码量少，模块清晰，适合用来学习 JVM 的基本结构和实现

21、[city-vein](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/conv1d/city-vein)：用公交路线数据，还原城市结构。通过数据可视化手段，还原了 30 多个城市的城市结构。该项目中有数据获取和处理的脚本，而且该项目充分体现了数据可视化带来的便利和效果，易于激发学习编程的热情。[在线浏览](https://96486d9b.github.io/city-vein/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/city-vein.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
22、[huginn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/huginn/huginn)：基于 Ruby 开发的自动化处理任务工具。可以监控事物然后根据编写好的逻辑进行处理（IFTTT），比如：监控天气然后通过微信提醒你带伞、追的小说或者动漫更新通知、聚合信息发送等。它框架稳定、生态活跃，有了它从而让你的生活更加有效率，快去试试吧

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/huginn.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
23、[Brooklyn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pedrommcarrasco/Brooklyn)：炫酷的苹果电脑屏幕保护程序

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/Brooklyn.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[PopMenu](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CaliCastle/PopMenu)：一款简单、漂亮、方便、灵活自定义的弹出菜单组件。如果你的 App 需要一款灵活好看的弹出菜单的话，那么 PopMenu 值得你一试

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/PopMenu.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
25、[commit-messages-guide](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/RomuloOliveira/commit-messages-guide)：Git 提交描述（commit）的编写指南，[中文](https://github.com/RomuloOliveira/commit-messages-guide/blob/master/README_zh-CN.md)

26、[weekly](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/aliyunfe/weekly)：《阿里云前端技术周刊》

27、[algo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wangzheng0822/algo)：必知必会的数据结构和算法代码答案（多种编程语言）

28、[vim-bootstrap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/editor-bootstrap/vim-bootstrap)：一个简单、易用的 `.vimrc` 配置文件生成工具，也可通过[网站](https://vim-bootstrap.com/)点选生成。支持 Vim、NeoVim、NeoVim-Qt、MacVim 和 GVim。特点：
- 轻量：包含少且必要的插件
- 易用：适合在vim中成功存活的入门者
- 易于定制：只需选择使用的语言,即可获得对应配置
- 先进的插件管理器：使用 Vim-Plug 管理插件，简单易用、速度快
- 支持多种编程语言

29、[hacker-laws](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dwmkerr/hacker-laws)：程序员工作中可能使用到的定律、原则的讲解，这些原则多应用于我们的开发和设计中，开卷有益

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/hacker-laws.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 教程
30、[vscode-extension-samples](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/vscode-extension-samples)：官方 VS Code 开发扩展插件的代码实例集合

31、[3d-game-shaders-for-beginners](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lettier/3d-game-shaders-for-beginners)：有关如何为 3D 游戏实施 SSAO、景深、照明、法线贴图等效果的教程。包含示例代码（C++）与 Demo，更便于理解和学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/3d-game-shaders-for-beginners.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
32、[BentoML](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bentoml/BentoML)：一个机器学习工具用来打包和发布模型。帮助数据科学家用不到 5 分钟把在 ipython notebook 里的模型发布到生产环境
```python
%%writefile iris_classifier.py
from bentoml import BentoService, api, env, artifacts
from bentoml.artifact import PickleArtifact
from bentoml.handlers import DataframeHandler

# You can also import your own python module here and BentoML will automatically
# figure out the dependency chain and package all those python modules

@artifacts([PickleArtifact('model')])
@env(conda_pip_dependencies=["scikit-learn"])
class IrisClassifier(BentoService):

    @api(DataframeHandler)
    def predict(self, df):
        # arbitrary preprocessing or feature fetching code can be placed here 
        return self.artifacts.model.predict(df)
```

33、[stanford-cs-229-machine-learning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/afshinea/stanford-cs-229-machine-learning)：斯坦福 CS229 教程讲义文档，该文档内容细致、条理清晰，方便入门者作为读书笔记学习。[中文版](https://github.com/afshinea/stanford-cs-229-machine-learning/tree/master/zh)

34、[mlcourse.ai](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Yorko/mlcourse.ai)：一套机器学习课程。课程全面细致，同时带有 demo 以及进阶的 Kaggle 比赛的样例，非常适合初学者逐步的深入学习

35、[lihang-code](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fengdu78/lihang-code)：机器学习领域经典书籍《统计学习方法》的课件和代码。这个项目提供了课件、代码资源，叙述从具体问题或实例入手，由浅入深，阐明思路，给出必要的数学推导，便于读者掌握统计学习方法的实质，学会运用

36、[maskrcnn-benchmark](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/facebookresearch/maskrcnn-benchmark)：Facebook 开源的 PyTorch 版本的 Mask-RCNN。研究人员可以按照教程、示例代码逐步进行实现

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/38/img/maskrcnn-benchmark.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/37/HelloGitHub37.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/39/HelloGitHub39.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
