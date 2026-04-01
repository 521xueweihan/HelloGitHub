# HelloGitHub Vol.31
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C
1、[C](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TheAlgorithms/C)：各种基础算法、数据结构的 C 语言实现。这个[TheAlgorithms](https://github.com/TheAlgorithms) 开源组织的项目包含基础算法的各种编程语言的示例代码


2、[obs-studio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/obsproject/obs-studio)：由 OBS 项目维护的免费开源流媒体和录制程序。该程序支持 Windows 7、macOS 10.10、Ubuntu 14.04 操作系统。可用于直播和屏幕录制，[下载地址](https://github.com/obsproject/obs-studio/releases)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/31/13233158.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C++
3、[CppCon2018](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/CppCon/CppCon2018)：CppCon 2018 幻灯片和资料


### Go
4、[gitea](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/go-gitea/gitea)：一个极易安装、运行快速、安装简单、使用体验良好的自建 Git 服务。采用 Go 作为后端语言，支持 Linux、 macOS、Windows 等，[在线Demo](https://try.gitea.io/)。安装步骤如下：
```
$ git clone https://github.com/go-gitea/gitea
$ cd gitea
$ TAGS="bindata" make generate all
$ ./gitea web 
```


5、[thunder](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/samsarahq/thunder)：Facebook GraphQL 协议的 Go 语言版本。相比之前的其它 GraphQL 库，通过反射结构体的 tag 可以自动生成 schema 给前端，更加便于开发。示例代码：
```go
// Friend is a small struct representing a person.
type Friend struct {
  FirstName string
  Last string `graphql:"lastName"` // use a custom name

  Added time.Date `graphql:"-"` // don't expose over graphql
}

// FullName builds a friend's full name.
func (f *Friend) FullName() string {
  return fmt.Sprintf("%s %s", f.FirstName, f.Last)
}

// registerFriend registers custom resolvers on the Friend type.
//
// Note: registerFriend wouldn't be necessary if the type only
// had the default struct field resolvers above.
func registerFriend(schema *schemabuilder.Schema) {
  object := schema.Object("Friend", Friend{})

  // fullName is a computed field on the Friend{} object.
  object.FieldFunc("fullName", Friend.FullName)
}
```


6、[wechat-go](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/songtianyi/wechat-go)：微信网页版 API 的 Go 实现。支持模拟微信网页版的登录、联系人、消息收发、机器人回复等功能。示例代码片段：
```go
func main() {
	// 创建session, 一个session对应一个机器人
	// 二维码显示在终端上
	session, err := wxweb.CreateSession(nil, nil, wxweb.TERMINAL_MODE)
	if err != nil {
		logs.Error(err)
		return
	}

	// 注册插件, 所有插件默认是开启的
	faceplusplus.Register(session)
	replier.Register(session)
	switcher.Register(session)
	gifer.Register(session)

	// 你也可以自己选择关闭插件里的handler(消息处理器)
	session.HandlerRegister.DisableByName("faceplusplus")

	// 登录并接收消息
	if err := session.LoginAndServe(false); err != nil {
		logs.Error("session exit, %s", err)
	}
}
```


7、[wxpay](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/objcoding/wxpay)：Go 的微信支付 SDK。微信系的 SDK，填补 Go 在微信支付开发界的空白。支持刷卡支付、统一下单、查询订单、撤销订单、关闭订单等。示例代码如下：
```go
// 创建支付账户
account1 := wxpay.NewAccount("appid", "mchid", "apiKey", false)
account2 := wxpay.NewAccount("appid", "mchid", "apiKey", false)
// 新建微信支付客户端
client := wxpay.NewClient(account1)
// 设置证书
account.SetCertData("证书地址")
// 设置支付账户
client.setAccount(account2)
// 设置http请求超时时间
client.SetHttpConnectTimeoutMs(2000)
// 设置http读取信息流超时时间
client.SetHttpReadTimeoutMs(1000)
// 更改签名类型
client.SetSignType(HMACSHA256)
```


### Java
8、[AndroidAutoSize](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/JessYanCoding/AndroidAutoSize)：学习成本极低的 Android 屏幕适配方案，已被知名 APP 用于线上产品


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/31/145098146.png' style="max-width:80%; max-height=80%;"></img></p>

9、[MyPerf4J](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LinShunKang/MyPerf4J)：一个针对高并发、低延迟应用设计的高性能 Java 性能监控和统计工具。特性：
- 高性能: 单线程支持每秒 1000 万次 响应时间的记录，每次记录只花费 73 纳秒
- 无侵入：采用 JavaAgent 方式，对应用程序完全无侵入，无需修改应用代码
- 低内存：采用内存复用的方式，整个生命周期只产生极少的临时对象，不影响应用程序的 GC
- 高精度：采用纳秒来计算响应时间
- 高实时：支持秒级监控，最低 1 秒


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/31/124743561.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[XChart](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/knowm/XChart)：用于绘制数据的轻量级 Java 库。示例代码：
```java
double[] xData = new double[] { 0.0, 1.0, 2.0 };
double[] yData = new double[] { 2.0, 1.0, 0.0 };
// Create Chart
XYChart chart = QuickChart.getChart("Sample Chart", "X", "Y", "y(x)", xData, yData);
// Show it
new SwingWrapper(chart).displayChart();
// Save it
BitmapEncoder.saveBitmap(chart, "./Sample_Chart", BitmapFormat.PNG);
// or save it in high-res
BitmapEncoder.saveBitmapWithDPI(chart, "./Sample_Chart_300_DPI", BitmapFormat.PNG, 300);
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/31/2078882.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
11、[33-js-concepts](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/leonardomso/33-js-concepts)：该项目介绍了每个 Javascript 开发者应该知道的 33 个概念。列举了 Javascript 中非常常见的 33 个概念，对于深入了解 Javascript 语言有很大的帮助。[中文阅读](https://github.com/stephentian/33-js-concepts)


12、[chrome-plugin-demo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sxei/chrome-plugin-demo)：Chrome 插件开发完整教程，可用来学习插件开发


13、[d3](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/d3/d3)：D3 的全称是（Data-Driven Documents），该库提供了各种简单易用的函数，大大简化了 JavaScript 操作数据的难度。该库的使用是数据可视化必须掌握的技术，[入门教程](http://wiki.jikexueyuan.com/project/d3wiki/introduction.html)，[示例 demo](https://github.com/d3/d3/wiki/Gallery)


14、[TypeScript-React-Starter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/TypeScript-React-Starter)：由 Microsoft 创建，该项目详细介绍了如何使用 TS 基于 create-react-app 创建 React 项目模版的步骤。TS 出现使得 JS 具有了强类型语言的严谨性，并且还保留了JS的灵活。React 是目前超火的前端框架，两者的结合非常值得学习


### Python
15、[awslogs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jorgebastida/awslogs)：一个简单的命令行工具，用于在本地查询 Amazon CloudWatch 日志，强大的支持多实例日志汇总查看。简单的查看命令：`awslogs get /var/logs/syslog ALL -s1d`


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/31/29613985.png' style="max-width:80%; max-height=80%;"></img></p>

16、[CUP](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/baidu/CUP)：CUP 基础库是百度开源的 Python 语言基础库，致力将 DEV 从涉及底层操作、Util 操作类解放出来，使其更关注构建 service 上层业务逻辑。
目前已涵盖了构建一个服务的各个方面，大家可以从基础库的代码结构、wiki、doc 中进行简单了解。
```
cup
    |-- cache.py                module              缓存相关模块 （ Memory cache related module ）
    |-- decorators.py           module              python 修饰符，比如 @Singleton 单例模式 (Decorators of python)
    |-- err.py                  module              异常 exception 类, Exception classes for CUP
    |-- __init__.py             module              默认__init__.py, Default __init__.py
    |-- log.py                  module              打印日志类，CUP 的打印日志比较简洁、规范，设置统一、简单(cup logging module)
    |-- mail.py                 module              发送邮件 （ CUP Email module (send emails)）
    |-- net                     package             网络相关操作（ Network operations, such as net handler parameter tuning ）
    |-- oper.py                 module              一些混杂操作(Mixin operations)
    |-- platforms.py            module              跨平台、平台相关操作函数(Cross-platform operations)
    |-- res                     package             资源获取、实时用量统计等，所有在 /prco 可获得的系统资源、进程、设备等信息 （ Resource usage queries (in /proc)、Prcoess query、etc ）
    |-- shell                   package             命令 Shell 操作 pakcage （ Shell Operations、cross-hosts execution ）
    |-- services                package             构建服务支持的类（比如心跳、线程池 based 执行器等等） Heartbeat、Threadpool based executors、file service、etc
    |-- thirdp                  package             第三方依赖纯 Py 模块（ Third-party modules：pexpect、httplib2 ）
    |-- timeplus.py             module              时间相关的模块(Time related module)
    |-- unittest.py             module              单元测试支持模块（ Unittest、assert、noseClass ）
    |-- util                    package             线程池、可打断线程、语义丰富的配置文件支持（ ThreadPool、Interruptable-Thread、Rich configuration、etc ）
    |-- version.py              module              内部版本文件，CUP Version
```


17、[supervisor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Supervisor/supervisor)：Python 开发的一个 C/S 服务，是 Linux/Unix 系统下的一个进程管理工具，不支持 Windows 系统。它可以很方便的监听、启动、停止、重启一个或多个进程。用 Supervisor 管理的进程，当一个进程意外被杀死，supervisort 监听到进程死后，会自动将它重新启动，很方便的做到进程自动恢复的功能，提高系统、服务的稳定性，多用于生产环境


### Swift
18、[Gifski](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sindresorhus/Gifski)：Gifski这个开源程序可以将一系列图片或一段视频转化为高质量的gif，高质量是这个程序最大的特色，下面我们将从使用与评价两个方面来介绍这个程序。Gifski实际上适用于windows，mac以及linux三个平台，唯一不同的是，mac平台上的gifski内置了视频分帧工具，因此可以直接把视频拖入程序窗口即可生成gif，而其它平台上则只能使用第三方程序分帧后才能处理，并且要在命令行中运行


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/31/119822304.jpg' style="max-width:80%; max-height=80%;"></img></p>

### AI
19、[nndl.github.io](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nndl/nndl.github.io)：《神经网络与深度学习》该课程主要介绍神经网络与深度学习中的基础知识、主要模型（卷积神经网络、递归神经网络等）以及在计算机视觉、自然语言处理等领域的应用。[在线阅读](https://nndl.github.io/)


20、[pwc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zziz/pwc)：深度学习、机器学习论文集合（英文）


### Other
21、[puppeteer-api-zh_CN](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zhaoqize/puppeteer-api-zh_CN)：Puppeteer 中文文档（与官方保持同步）


22、[quick-SQL-cheatsheet](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/enochtangg/quick-SQL-cheatsheet)：SQL 速查表，[中文查阅](https://github.com/enochtangg/quick-SQL-cheatsheet/blob/master/README_zh-hans.md)


23、[README](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/guodongxiaren/README)：该项目介绍了 GFM 的语法和示例展示。GitHub 的 Markdown 语法在标准的语法基础上做了扩充，称之为 GitHub Flavored Markdown，简称 GFM。友好的 README 是项目的第一印象，这点很重要


24、[zh-google-styleguide](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zh-google-styleguide/zh-google-styleguide)：Google 开源项目风格指南 (中文版)




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub30.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub32.md">『Next』</a>
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
