# 《HelloGitHub》第 68 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 目录

**Tips**：如果文中的图刷不出来，可以点击 [这里](https://hellogithub.com/periodical/volume/68/) 获取更好的阅读体验。

- [C 项目](#C-项目)
- [C# 项目](#C-项目-1)
- [C++ 项目](#C-项目-2)
- [CSS 项目](#CSS-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Python 项目](#Python-项目)
- [Rust 项目](#Rust-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [机器学习](#机器学习)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[toybox](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/landley/toybox)：该项目将 200 多个常用的 Linux 命令行工具，做成一个可执行文件。从而可以让 Android 这种原本不支持 Linux 命令的系统，也得以用上 ls、find、ps 等命令。还可以用于快速构建最小的 Linux 环境

2、[the_silver_searcher](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ggreer/the_silver_searcher)：比 ack 更快的命令行搜索工具。速度快、功能强大、使用简单，支持 Linux、Windows、macOS 操作系统，还能够整合到 Vim 和 Emacs 等编辑器
```
ack test_blah ~/code(8G)/  104.66s user 4.82s system 99% cpu 1:50.03 total
ag test_blah ~/code(8G)/  4.67s user 4.58s system 286% cpu 3.227 total
```

3、[WindTerm](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kingToolbox/WindTerm)：支持 SSH/Telnet/Serial/Shell/Sftp 的终端工具。虽然该软件完全免费，但部分代码尚未完全开源，对安全敏感的同学可以再观望下

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/WindTerm.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
4、[wavefunctioncollapse](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/marian42/wavefunctioncollapse)：基于波函数坍缩 (WFC) 算法，实现的无限城市示例。城市里有房子、楼梯、树木、连接房屋的通道，你可以在城市中自由移动、跳跃、飞行，但不论你怎么移动都找不到尽头，因为这座城市会无限延伸

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/wavefunctioncollapse.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[NETworkManager](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/BornToBeRoot/NETworkManager)：管理和解决网络问题的工具。它集成了 IP 和端口扫描、WiFi 分析器、跟踪路由、DNS 查询等工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/NETworkManager.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
6、[ppsspp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hrydgard/ppsspp)：能够运行在 Android 和 PC 上的开源 PSP 模拟器。[下载地址](https://ppsspp.org/index-cn.html)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/ppsspp.jpeg' style="max-width:80%; max-height=80%;"></img></p>

7、[leocad](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/leozide/leocad)：用来创建虚拟乐高模型的 CAD 工具。适用于 Windows、Linux 和 macOS 系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/leocad.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
8、[csshake](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/elrumordelaluz/csshake)：用 CSS 实现抖动效果

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/csshake.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
9、[FerretDB](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FerretDB/FerretDB)：真正开源的 MongoDB 替代品。它底层采用 PostgreSQL 作为存储引擎，用 Go 语言实现了 MongoDB 协议，所以几乎兼容所有的 MongoDB 库，迁移起来毫无负担。如果你用不到 MongoDB 的高级功能，还受限于它的开源协议，那么这个项目可作为 MongoDB 的开源替代方案。它才刚刚起步，建议观望一段时间或做足测试再用于生产环境

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/MangoDB.png' style="max-width:80%; max-height=80%;"></img></p>

10、[caddy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/caddyserver/caddy)：用 Go 编写的轻量级 Web 服务器。它相较于 Apache、Nginx 这些知名 Web 服务器，独特点在于提供了编译好的可执行文件，实现了真正的开箱即用。无需任何配置即可拥有免费的 HTTPS、自动把 Markdown 文件转化成 HTML 等人性化的功能。如果是搭建中小型的 Web 服务，它完全够用而且省时省心

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/caddy.png' style="max-width:80%; max-height=80%;"></img></p>

11、[croc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/schollz/croc)：可以让任意两台计算机，安全方便地传输文件和文件夹的工具。轻松实现端到端加密的跨平台文件传输，还支持多文件传输、传输中断和恢复等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/croc.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
12、[jnativehook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kwhat/jnativehook)：获取键盘和鼠标事件的 Java 库。轻松监听按键、鼠标移动、点击等事件
```java
import GlobalScreen;
import NativeHookException;
import NativeMouseWheelEvent;
import NativeMouseWheelListener;
// 鼠标移动
public class GlobalMouseWheelListenerExample implements NativeMouseWheelListener {
	public void nativeMouseWheelMoved(NativeMouseWheelEvent e) {
		System.out.println("Mosue Wheel Moved: " + e.getWheelRotation());
	}

	public static void main(String[] args) {
		try {
			GlobalScreen.registerNativeHook();
		}
		catch (NativeHookException ex) {
			System.err.println("There was a problem registering the native hook.");
			System.err.println(ex.getMessage());
			ex.printStackTrace();

			System.exit(1);
		}

		GlobalScreen.addNativeMouseWheelListener(new GlobalMouseWheelListenerExample());
	}
}
```

13、[spider-flow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ssssssss-team/spider-flow)：用流程图的方式编写爬虫的平台。无需写代码就可以快速完成一个简单的爬虫

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/spider-flow.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[greenDAO](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/greenrobot/greenDAO)：高性能的 Android ORM 库。拥有体积小、易于使用、支持数据库加密等特点，通过它 Android 开发者可以采用面向对象的方式操作数据库，不需要再手写和拼接 SQL 啦

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/greenDAO.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
15、[vue-color-avatar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Codennnn/vue-color-avatar)：纯前端实现的矢量风格头像生成网站。可以通过搭配不同的素材，生成个性化头像。该项目使用 Vite + Vue3 开发，能够帮助前端初学者熟悉 Vue3 语法并掌握项目搭建的相关知识

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/vue-color-avatar.png' style="max-width:80%; max-height=80%;"></img></p>

16、[colorfu](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pearmini/colorfu)：自动生成由文字/颜色/图片/纹理元素组成的壁纸。[在线尝试](https://colorfu.art/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/colorfu.png' style="max-width:80%; max-height=80%;"></img></p>

17、[pm2](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Unitech/pm2)：Node.js 的进程管理工具。它容易上手操作简单，可以有效地提高 Node.js 程序运行的稳定性，支持自动重启、负载均衡、不停服务重启、性能监控等功能，多用于生产环境中管理、监控 Node.js 进程

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/pm2.png' style="max-width:80%; max-height=80%;"></img></p>

18、[automa](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AutomaApp/automa)：通过图形化界面拖拽功能模块，实现浏览器自动操作的扩展工具。轻松实现自动填表、截图、定时执行等操作。让浏览器自动完成预设工作流的插件，从而减少重复性操作提高效率

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/automa.jpeg' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
19、[PyWebIO](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pywebio/PyWebIO)：快速构建 Web 应用的 Python 工具。通过该项目你可在不写 HTML、CSS、JS 代码的前提下，仅用 Python 快速完成一个包含数据展示、表单的小型 Web 应用页面

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/PyWebIO.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[pottery](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/brainix/pottery)：以 Python 的方式操作 Redis 的库。忘记那些 Redis 命令吧，只要你知道如何使用 Python 字典，那么你就会用这个库操作 Redis
```python
>>> from pottery import RedisList
>>> tel = RedisDict({'jack': 4098, 'sape': 4139}, redis=redis, key='tel')
>>> tel['guido'] = 4127
>>> tel
RedisDict{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> squares = RedisList([1, 4, 9, 16, 25], redis=redis, key='squares')
>>> squares
RedisList[1, 4, 9, 16, 25]
>>> squares[0]
1
```

21、[zulip](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zulip/zulip)：完全开源的企业级即时通讯项目。后端采用 Python 语言实现性能足够强大，功能齐全相当于开源、免费的 Slack，拥有拖拽上传文件、代码高亮、Markdown 语法、应用整合、容易接入的 API 等功能，还支持 Web、PC、iOS 和 Android 主流平台，众多知名企业都在用，能够有效地提高团队沟通和办公效率。同时该项目对新手用户友好，如果你想加入一个不错的 Python 开源项目，推荐你花时间研究下它一定会有所收获

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/zulip.png' style="max-width:80%; max-height=80%;"></img></p>

22、[webssh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/huashengdun/webssh)：简单的 SSH 连接服务器的 Python Web 应用。该项目后端采用 Tornado Web 框架和 Python SSH 库 paramiko，前端是 TypeScript 写的命令行前端组件 Xterm.js 实现。整个项目简单还具有实用价值，可作为 Python Web 的实战项目学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/webssh.png' style="max-width:80%; max-height=80%;"></img></p>

23、[django-debug-toolbar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jazzband/django-debug-toolbar)：Django 的调试工具栏。可显示当前请求和响应有关的各种调试信息，包括耗时、SQL、配置、性能等信息
```
1. 安装：pip install django-debug-toolbar
2. TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        # ...
    }
]
3. INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    "django.contrib.staticfiles",
    # ...
]
4. 增加 __debug__ URL
import debug_toolbar
from django.urls import include, path

urlpatterns = [
    # ...
    path('__debug__/', include(debug_toolbar.urls)),
]
5. MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
6. INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/django-debug-toolbar.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Rust 项目
24、[hyperfine](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sharkdp/hyperfine)：命令行基准测试工具。可用来查看和对比命令的耗时，支持多次运行的统计分析、结果导出等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/hyperfine.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
25、[xcode-dev-cleaner](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vashpan/xcode-dev-cleaner)：用于清理各种 Xcode 的缓存数据，释放存储空间。注意是清除 Xcode 缓存数据，不是卸载 Xcode 哈

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/xcode-dev-cleaner.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
26、[toml](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/toml-lang/toml)：更易读和易于维护的配置文件格式。如果你厌倦了 INI 的局限性、层层嵌套的 JSON 和 YAML 令人心惊胆战的缩进语法，不妨给 TOML 一个机会，它支持多种数据类型、抛弃了缩进和嵌套，而且众多流行编程语言都有对应的库。TOML 已经足够成熟，绝对值得一试。[查看文档](https://toml.io/cn/v1.0.0)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/toml.png' style="max-width:80%; max-height=80%;"></img></p>

27、[waka-readme-stats](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/anmol098/waka-readme-stats)：自动在 GitHub 个人首页展示编程时长的工具。该项目通过 WakaTime 记录用户在 IDE 的使用时间，统计编程时长和数据，然后采用 GitHub Action 自动获取并动态更新到 GitHub 个人首页。轻而易举地展示自己的编程时长

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/waka-readme-stats.png' style="max-width:80%; max-height=80%;"></img></p>

28、[PathPlanning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zhm-real/PathPlanning)：常见的路径规划算法集合。项目包含了 Python 代码实现、运行过程动画以及相关论文

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/PathPlanning.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[howdy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/boltgolt/howdy)：为 Linux 系统提供人脸识别解锁电脑的工具。通过电脑内置的摄像头和红外设备，实现了类似 Windows Hello™ 风格的身份认证，可用于登陆、锁屏、sudo 等任何需要输入密码的地方

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/howdy.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[The-Open-Book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/joeycastillo/The-Open-Book)：开源的电子水墨屏阅读设备。动手能力强的同学可跟着这个项目，从焊电路板开始亲手制作出一个类 Kindle 的 4.2 英寸阅读设备

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/The-Open-Book.jpeg' style="max-width:80%; max-height=80%;"></img></p>

31、[fl_chart](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/imaNNeoFighT/fl_chart)：Flutter 图表库。它支持折线图、条形图、饼图、散点图和雷达图

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/fl_chart.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
32、[ugo-compiler-book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wa-lang/ugo-compiler-book)：《从头开发一个迷你 Go 语言》该书教你从头实现迷你 Go 语言，内容包含了词法解析、语法树构建、函数闭包、接口、CGO 的实现等内容。[在线阅读](https://chai2010.cn/ugo-compiler-book/ch1-basic/index.html)

33、[archbase](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/foxsen/archbase)：教科书《计算机体系结构基础》第三版。[在线阅读](https://foxsen.github.io/archbase/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
34、[best_AI_papers_2021](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/louisfb01/best_AI_papers_2021)：2021 年必看的人工智能论文列表。该项目不是简单的罗列论文，它不仅包含相关论文的代码、效果展示，还有深入的文章和讲解视频。通过学习这些前沿的人工智能论文，提前了解 AI 在未来更多可能性

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/best_AI_papers_2021.png' style="max-width:80%; max-height=80%;"></img></p>

35、[AnimeGANv2](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TachibanaYoshino/AnimeGANv2)：可以将图片和视频转换成漫画风格的工具。采用的是神经风格迁移+生成对抗网络（GAN）的组合，转换速度快。[在线尝试](https://huggingface.co/spaces/akhaliq/AnimeGANv2)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/68/img/AnimeGANv2.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub67.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub69.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1xF2ECA89A2592'>云主机 4 元/月</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>推荐项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有各种回馈粉丝活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/68/'>这里</a> 获取更好的阅读体验。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
