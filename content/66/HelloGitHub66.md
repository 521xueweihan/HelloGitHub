# 《HelloGitHub》第 66 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 目录

**Tips**：如果文中的图刷不出来，可以点击 [这里](https://hellogithub.com/periodical/volume/66/) 获取更好的阅读体验。

- [C 项目](#C-项目)
- [C# 项目](#C-项目-1)
- [C++ 项目](#C-项目-2)
- [CSS 项目](#CSS-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Kotlin 项目](#Kotlin-项目)
- [Objective-C 项目](#Objective-C-项目)
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
1、[HEX-LINK](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/JingYang1124/HEX-LINK)：自制电脑游戏的体感设备。该项目包含制作时需要的硬件设计和全部源码
```
.
├─firmware # 软件（根据自己使用的工具选择如下一种工程即可）
│  ├─ArduinoIDE_Proj # Arduino IDE版工程 
│  │  ├─Additional_Libraries # 里面的文件夹需要复制到Arduino IDE安装目录下的libraries文件夹
│  │  ├─Hex_Link_Leonardo # 需要下载至接收端的程序
│  │  └─Hex_Link_Nano # 需要下载至发送端的程序
│  ├─Bootloaders # 需要下载至芯片的arduino bootloader 
│  └─Vscode_PlatformIO_Proj # VScode PlatformIO版工程 
│      ├─Hex_Link_Leonardo # 需要下载至接收端的程序
│      └─Hex_Link_Nano # 需要下载至发送端的程序
├─hardware # 硬件（PCB工程）
│  ├─BOM   # PCB的物料清单，包含参考的购买链接（链接仅作参考，在其他任何店铺购买相同型号即可）
│  ├─Hex_Link_Rec # 接收端PCB工程
│  ├─Hex_Link_Trans # 发送端PCB工程
│  └─Nano_Jtag_Pin # 转接板：用来烧录Nano bootloader的Jtag口转接板
├─model # 接收端外壳3维模型
│  ├─Solidworks_Project # 2018版本Solidworks工程
│  └─STL_TAP # STL文件，可直接用于3D打印.TAP文件是顶层亚克力板的CNC加工文件
├─references # 参考文档
└─tools # 额外的脚本工具
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/HEX-LINK.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
2、[SteamTools](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SteamTools-Team/SteamTools)：集合多种 Steam 客户端工具的工具箱。该工具支持 Window、Linux、macOS、Android 操作系统，包括游戏库存管理、解锁成就、史低价格、出售库存物品等功能，还有丰富的插件等待你发掘

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/SteamTools.png' style="max-width:80%; max-height=80%;"></img></p>

3、[xLua](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/xLua)：为 C#、Unity、.Net 等环境增添 Lua 脚本编程的能力，使得 Lua 代码方便地与 C# 相互调用
```
XLua.LuaEnv luaenv = new XLua.LuaEnv();
luaenv.DoString("CS.UnityEngine.Debug.Log('hello world')");
luaenv.Dispose();
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/xLua.png' style="max-width:80%; max-height=80%;"></img></p>

4、[BBDown](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nilaoda/BBDown)：命令行哔哩哔哩视频下载工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/BBDown.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
5、[libqalculate](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Qalculate/libqalculate)：使用 C++ 编写的多功能计算器桌面应用、库和 CLI 程序。它易于使用功能强大，支持大型可定制函数库、单位计算和转换、符号计算（包括积分和方程）。作为用户你可以直接在命令行中使用，作为开发者你也可以在自己的项目中使用这个库。官方还制作了 [Qt](https://github.com/Qalculate/qalculate-qt) 和 [GTK](https://github.com/Qalculate/qalculate-gtk) 两个版本的 GUI 计算器应用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/libqalculate.png' style="max-width:80%; max-height=80%;"></img></p>

6、[btop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/aristocratos/btop)：界面酷炫的命令行资源监视器。可以显示处理器、内存、磁盘、网络和进程的使用情况和统计信息，还支持鼠标操作

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/btop.png' style="max-width:80%; max-height=80%;"></img></p>

7、[TinyWebServer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/qinguoyi/TinyWebServer)：Linux 下的 C++ 轻量级 Web 服务器。该项目不仅可以用来搭建 Web 服务，也适合 C++ 初学者作为网络编程实战项目。作者还写了文章讲解相关代码和原理，帮助初学者更好的掌握网络编程相关知识

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
8、[css_tricks](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/QiShaoXuan/css_tricks)：常用 CSS 样式示例集合

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/css_tricks.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
9、[video-srt-windows](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wxbool/video-srt-windows)：自动识别视频语音生成字幕文件的工具。采用 Go+walk 开发所以仅支持 Windows 系统，原理是请求在线语音转文字的服务，超出免费额度需付费。另外还加入了导出字幕文件和翻译功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/video-srt-windows.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[go-daily-lib](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/darjun/go-daily-lib)：每天学习一个 Go 语言库。内容包含标准库和三方库，每个库对应一篇介绍和上手的文章

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/go-daily-lib.png' style="max-width:80%; max-height=80%;"></img></p>

11、[Open-IM-Server](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/OpenIMSDK/Open-IM-Server)：基于 Go 实现的轻量级即时通讯（IM）项目。具有高性能、易扩展、安装简单、私有化部署等特性，同时包含多种客户端 SDK。从服务器到客户端一体的开源即时通讯（IM）解决方案

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/Open-IM-Server.png' style="max-width:80%; max-height=80%;"></img></p>

12、[go-fly](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/taoshihan1991/go-fly)：基于 Go 语言实现的在线客服系统，采用 Gin+MySQL+JWT+WebSocket 等技术栈实现

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/go-fly.jpeg' style="max-width:80%; max-height=80%;"></img></p>

13、[viper](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/spf13/viper)：用来搞定 Go 应用中配置的库。支持多种配置文件类型、监控并重新加载配置文件、远程读取配置系统等
```go
viper.SetConfigName("config") // 配置文件名，不包括后缀
viper.SetConfigType("yaml") // 配置文件的后缀
viper.AddConfigPath("/etc/appname/")   // 查找配置文件的目录
viper.AddConfigPath("$HOME/.appname")  // 支持查找多个目录
// 异常处理
if err := viper.ReadInConfig(); err != nil {
	if _, ok := err.(viper.ConfigFileNotFoundError); ok {
		// 如果没有找到配置文件
	} else {
		// 找到了配置文件，但出现了其他错误
	}
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/viper.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
14、[o2oa](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/o2oa/o2oa)：国产的 OA 系统。功能齐全支持考勤、会议管理、云盘等，适用于企业 OA、协同办公

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/o2oa.png' style="max-width:80%; max-height=80%;"></img></p>

15、[IJPay](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Javen205/IJPay)：Java 支付工具库，轻松完成支付模块开发。封装了常用的微信、QQ、支付宝、银联、PayPal 支付等支付方式的各种常用接口。不依赖任何 MVC 框架，轻松接入到 Java 项目

16、[VirtualApp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/asLody/VirtualApp)：Android 系统的沙盒程序，App 虚拟化引擎。它创建了一个虚拟空间，在那里可以任意安装、启动、控制、卸载应用。虚拟空间与外部隔离相当于沙盒环境，可在安卓上实现应用多开、静默安装等黑科技

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/VirtualApp.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
17、[sharedb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/share/sharedb)：基于 JSON 数据 OT 算法的实时数据库。简单来说就是实时协同数据框架，可用来实现当页面因用户操作发生数据变化时，实时把数据同步展示到其它用户页面上，其中 OT 算法就是解决此协同过程中问题的通用算法。常见的场景比如：多用户之间的状态同步、在线协作文档、离线后数据改动同步等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/sharedb.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[30-Days-Of-JavaScript](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Asabeneh/30-Days-Of-JavaScript)：30 天 JavaScript 编程挑战。该教程虽然是英文教程但是图文并茂通俗易通，内容循序渐进包含练习题，适合零基础想要学习 JavaScript 的同学

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/30-Days-Of-JavaScript.png' style="max-width:80%; max-height=80%;"></img></p>

19、[YesPlayMusic](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/qier222/YesPlayMusic)：高颜值的第三方网易云播放器。它不仅拥有简洁美观的外观，还有丰富的功能
- 支持 Windows/macOS/Linux
- 私人 FM/每日推荐歌曲
- 网易云账号登录
- 歌词显示
- 自定义快捷键和全局快捷键
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/YesPlayMusic.png' style="max-width:80%; max-height=80%;"></img></p>

20、[javascript](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/airbnb/javascript)：Airbnb 开源的 JavaScript 风格指南。[中文](https://github.com/lin-123/javascript)
```javascript
// 采用数组解构
const arr = [1, 2, 3, 4];

// bad
const first = arr[0];
const second = arr[1];

// good
const [first, second] = arr;
```

21、[spy-debugger](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wuchangming/spy-debugger)：远程调试手机页面和抓包的工具。操作简单仅需手机和电脑在同一个 WIFI 下，即可在实现真机调试页面

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/spy-debugger.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Kotlin 项目
22、[Component](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xiaojinzi123/Component)：Android 的组件化框架，帮助开发者在实现项目组件化。它的强大在于功能齐全、更新及时，支持 Kotlin、AndroidX、RxJava、协程等

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
23、[iOSInterviewQuestions](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ChenYilong/iOSInterviewQuestions)：iOS 面试题集合（附答案）

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
24、[Pokemon-Terminal](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/LazoCoder/Pokemon-Terminal)：适用于多种终端的口袋妖怪主题工具。支持 iTerm2、ConEmu、Terminology、Windows 的终端，已经收集了 719 个小精灵

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/Pokemon-Terminal.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[mypy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/python/mypy)：Python 静态类型检查库。既然 Python 是一门动态类型语言，为啥还要检查类型呢？有了静态类型检测则无需运行代码，就可以发现程序中潜在的错误。还可以加入到 `git hook` 中，实现在提交代码前自动检查。详情查看[这篇文章](https://mp.weixin.qq.com/s/K4RGr5NqMFAUKtB0KFPV5g)

26、[CPython-Internals](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zpoint/CPython-Internals)：图文并茂的 Python 源码阅读笔记项目。阅读的是比较新的 CPython 3.8 版本，重点是项目一直在更新维护
```c++
static void take_gil(PyThreadState *tstate)
{
    /* 忽略 */
    while (_Py_atomic_load_relaxed(&_PyRuntime.ceval.gil.locked)) {
    	/* 只要 gil 是锁住的状态, 进入这个循环 */
        int timed_out = 0;
        unsigned long saved_switchnum;

        saved_switchnum = _PyRuntime.ceval.gil.switch_number;
        /* 释放 gil.mutex, 并在以下两种条件下唤醒
           1. 等待 INTERVAL 微秒(默认 5000) 
           2. 还没有等待到 5000 微秒但是收到了 gil.cond 的信号
        */
        COND_TIMED_WAIT(_PyRuntime.ceval.gil.cond, _PyRuntime.ceval.gil.mutex,
                        INTERVAL, timed_out);
        /* 当前持有 gil.mutex 这把互斥锁 */
        if (timed_out &&
            _Py_atomic_load_relaxed(&_PyRuntime.ceval.gil.locked) &&
            _PyRuntime.ceval.gil.switch_number == saved_switchnum) {
            /* 如果超过了等待时间, 并且这段等待时间里 gil 的持有者没有变更过, 则尝试让当前持有 gil 的线程进行释放gil
            把 gil_drop_request 值设为 1, 持有锁的线程看到这个值的时候, 会尝试放弃 gil */
            SET_GIL_DROP_REQUEST();
        }
        /* 继续回到 while 循环, 检查 gil 是否为锁住状态 */
    }
    /* 忽略 */
}
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Rust 项目
27、[nushell](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nushell/nushell)：一种更加人性化的新型 shell

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/nushell.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
28、[Clipy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Clipy/Clipy)：macOS 的剪贴板扩展应用。支持展示剪贴板历史记录、内容模版等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/Clipy.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
29、[QWidgetDemo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/feiyangqingyun/QWidgetDemo)：Qt 编写的示例集合。每个示例都可独立运行、代码简洁易懂，适合初学者学习

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/QWidgetDemo.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[xemu](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mborgerson/xemu)：免费开源的 Xbox 模拟器，支持 Windows、Linux、macOS 系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/xemu.png' style="max-width:80%; max-height=80%;"></img></p>

31、[yabai](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/koekeishiya/yabai)：适用于 macOS 的平铺式窗口管理器。该工具可以轻松实现窗口平铺不重叠，不用鼠标仅通过键盘移动、调整、切换、全屏、自动布局等管理窗口的操作
- `Control+Option+A/D`：激活 平铺/浮动 模式
- `Option+h/j/k/l`：使 左/下/上/右 侧窗口成为活动窗口
- `Shift+Option+h/j/k/l`：向 左/下/上/右 移动当前活动窗口
- `Command+Option+n`：创建新桌面，并将当前活动窗口移动至新桌面

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/yabai.png' style="max-width:80%; max-height=80%;"></img></p>

32、[awesome-for-beginners](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MunGell/awesome-for-beginners)：对初学者友好的开源项目集合。如果你想参与到开源项目的建设，可以在这个集合中寻找项目，祝你早日完成第一个贡献（PR）

33、[lifeRestart](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/VickScarlet/lifeRestart)：在线文字游戏《人生重开模拟器》。纯文字游戏只需开局选天赋分配初始属性，后面就是看岁月如白驹过隙，转眼就过完了这一生，不满意的话可以轻松重开新的人生。游戏凭借诙谐幽默的文案和出乎意料的结尾，广受好评。[在线试玩](https://liferestart.syaro.io/view/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/lifeRestart.png' style="max-width:80%; max-height=80%;"></img></p>

34、[chinese-dos-games](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rwv/chinese-dos-games)：中文 DOS 游戏集合。[在线试玩](https://dos.zczc.cz/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/chinese-dos-games.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
35、[introduction-to-front-end-engineering](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/woai3c/introduction-to-front-end-engineering)：一本小书《带你入门前端工程》。该书是作者对过去两年前端工程化实践的经验和心得总结，[在线阅读](https://woai3c.github.io/introduction-to-front-end-engineering/)

36、[pumpkin-book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/datawhalechina/pumpkin-book)：《机器学习公式详解》西瓜书公式推导解析。[在线阅读](https://datawhalechina.github.io/pumpkin-book/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/pumpkin-book.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
37、[invoice](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/guanshuicheng/invoice)：增值税发票 OCR 识别项目。包含训练好的模型和微服务，启动后可直接通过接口调用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/invoice.png' style="max-width:80%; max-height=80%;"></img></p>

38、[GameAISDK](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/GameAISDK)：基于图像识别的 AI 自动化框架，支持吃鸡类、射击类、MOBA 类等游戏类型。内置多种图像识别算法和 AI 算法，不用抠图完全基于图像识别的 AI 训练和框架

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/66/img/GameAISDK.png' style="max-width:80%; max-height=80%;"></img></p>

39、[genshin_auto_fish](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/7eu7d7/genshin_auto_fish)：基于深度学习的原神手游自动钓鱼工具。其中用 YOLOX 搞定鱼的定位和类型的识别以及鱼竿落点的定位，用 DQN 搞定自适应控制钓鱼过程的点击，让力度落在最佳区域内

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/65/HelloGitHub65.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/67/HelloGitHub67.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1xF2ECA89A2592'>云主机 4 元/月</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>推荐项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有各种回馈粉丝活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/66/'>这里</a> 获取更好的阅读体验。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
