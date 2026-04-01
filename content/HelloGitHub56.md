# 《HelloGitHub》第 56 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/56) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[ucore](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kiukotsu/ucore)：清华大学操作系统课程，配套实验项目。推荐给有计算机结构原理、C 和汇编、数据结构基础并对操作系统感兴趣的同学，项目中包含教学视频、练习题、实验指导书等


### C# 项目
2、[ContextMenuManager](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BluePointLilac/ContextMenuManager)：一个纯粹的 Windows 右键菜单管理程序。功能：
- 启用或禁用文件、文件夹、新建、发送到、打开方式等右键菜单项目
- 右键菜单项目进行修改名称、修改图标、导航注册表位置、永久删除等操作
- 右键菜单自定义添加项目，自定义菜单命令


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/304230333.png' style="max-width:80%; max-height=80%;"></img></p>

3、[RevokeMsgPatcher](https://hellogithub.com/periodical/statistics/click?target=https://github.com/huiyadanli/RevokeMsgPatcher)：适用于 Windows 系统下电脑版微信、QQ 的防撤回工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/198071756.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[spdlog](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gabime/spdlog)：快速、上手简单的 C++ 日志库。示例代码：
```C++
#include "spdlog/spdlog.h"

int main() 
{
    spdlog::info("Welcome to spdlog!");
    spdlog::error("Some error message with arg: {}", 1);
    
    spdlog::warn("Easy padding in numbers like {:08d}", 12);
    spdlog::critical("Support for int: {0:d};  hex: {0:x};  oct: {0:o}; bin: {0:b}", 42);
    spdlog::info("Support for floats {:03.2f}", 1.23456);
    spdlog::info("Positional args are {1} {0}..", "too", "supported");
    spdlog::info("{:<30}", "left aligned");
    
    spdlog::set_level(spdlog::level::debug); // Set global log level to debug
    spdlog::debug("This message should be displayed..");    
    
    // change log pattern
    spdlog::set_pattern("[%H:%M:%S %z] [%n] [%^---%L---%$] [thread %t] %v");
    
    // Compile time log levels
    // define SPDLOG_ACTIVE_LEVEL to desired level
    SPDLOG_TRACE("Some trace message with param {}", 42);
    SPDLOG_DEBUG("Some debug message");
}
```


5、[srpc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sogou/srpc)：搜狗基于 C++ Workflow 的高性能 RPC 框架。与 thrift/brpc 协议兼容，支持 protobuf/thrift IDL一键迁移，核心代码量仅 1w 行。示例代码：
```c++
class ExampleServiceImpl : public Example::Service
{
public:
    void Echo(EchoRequest *request, EchoResponse *response, RPCContext *ctx) override
    {
        response->set_message("Hi, " + request->name());
    }
};

int main()
{
    SRPCHttpServer server;
    ExampleServiceImpl impl;
    server.add_service(&impl);
    server.start(1412);
    pause();
    server.stop();
    return 0;
}
访问：
curl 127.0.0.1:1412/Example/Echo -H 'Content-Type: application/json' -d '{message:"from curl",name:"CURL"}'
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/295369297.png' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
6、[tailwindcss](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tailwindlabs/tailwindcss)：基于比组件更小、更灵活的工具类（utility-first）思想的 CSS 框架。这个思想简单来说就是用 class 保证灵活、便于自定义组件，而不是在组件基础上实现个性化。网上对这个框架褒贬不一，但我觉得挺好想学一下


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/106017343.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
7、[go-zero](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zeromicro/go-zero)：一个可靠的 Go 语言 Web 和 RPC 框架。就算是 Go 新手基于该框架，也可以快速写出高性能可扩展的微服务。示例代码：
```go
func main() {
  flag.Parse()

  var c config.Config
  conf.MustLoad(*configFile, &c)

  ctx := svc.NewServiceContext(c)
  server := rest.MustNewServer(c.RestConf)
  defer server.Stop()

  handler.RegisterHandlers(server, ctx)

  server.Start()
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/285864199.png' style="max-width:80%; max-height=80%;"></img></p>

8、[lazykube](https://hellogithub.com/periodical/statistics/click?target=https://github.com/TNK-Studio/lazykube)：支持鼠标操作和管理 K8s 的命令行工具。对比 k9s 命令行工具，可以不用去记那么多快捷键，直接用鼠标操作。解决公司不使用 rancher 和 dashboard 管理 K8s，只能通过堡垒机访问的场景。使用该工具只需要终端和鼠标，当然用到搜索功能时还是需要键盘的 😂


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/310469027.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[syncthing](https://hellogithub.com/periodical/statistics/click?target=https://github.com/syncthing/syncthing)：一个采用 Go 语言编写的免费、跨平台的文件同步工具。它不需要安装，只需要下载对应系统的压缩包解压后就可以直接运行和使用。拥有命令行、Web 和桌面程序多种操作模式，同时支持内网和互联网的文件同步，可以用来搭建私有网盘。又一个代替付费网盘的选择，如果考虑到昂贵的宽费用。可以把 syncthing 做为局域网下手机、电视和电脑共享文件的开源解决方案


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/14712850.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
10、[Mindustry](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Anuken/Mindustry)：一款 Java 编写的免费沙盒塔防游戏。支持多平台：Windows、Linux、macOS、Android 


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/89822531.png' style="max-width:80%; max-height=80%;"></img></p>

11、[novel](https://hellogithub.com/periodical/statistics/click?target=https://github.com/201206030/novel)：一个基于 SpringBoot 实现的小说和漫画在线阅读网站。网站功能齐全、资源丰富，同时支持 Web、安卓、微信小程序多平台。服务端分为网站和管理后台，采用 SpringBoot、MyBatis、MySQL、Redis 等技术实现，可当作 Java 新手实战项目学习


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/220875250.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
12、[AdminLTE](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ColorlibHQ/AdminLTE)：基于 Bootstrap 4.5 和 jQuery 的管理后台模板


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/15428480.png' style="max-width:80%; max-height=80%;"></img></p>

13、[blockly](https://hellogithub.com/periodical/statistics/click?target=https://github.com/RaspberryPiFoundation/blockly)：不会编程也可以写代码，通过拖拽模块自动生成代码的 Web 编辑器。谷歌开源的一个可视化编程的前端项目，支持自动生成：Python、JavaScript、PHP 等编程语言的代码，在线尝试的地址网络不好，可以通过 `npm install blockly` 安装后使用和学习


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/13872231.png' style="max-width:80%; max-height=80%;"></img></p>

14、[lucky-canvas](https://hellogithub.com/periodical/statistics/click?target=https://github.com/buuing/lucky-canvas)：一个基于 Vue 的大转盘/九宫格抽奖插件。[在线尝试](https://100px.net/demo/wheel/ymc.html)，特性：
- 可自由配置奖品、中奖概率等
- 支持同步、异步式抽奖
- 适配移动端
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/191120006.png' style="max-width:80%; max-height=80%;"></img></p>

15、[piano](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Wscats/piano)：基于 Omi 和 Omi Snippets 构建的钢琴应用。你不需要懂乐理知识，仅用键盘即可弹奏简单而熟悉的音乐，也借此项目感谢音乐和编程的陪伴！也致敬各位奋斗于 996 的代码家和打工人，音乐不曾辜负任何人，正如 Leehom Wang 歌曲中唱到：如果世界太危险，只有音乐最安全，带着我进梦里面，让歌词都实现！上面这段是作者写的推荐语，我本来想从项目的角度再夸下这个项目，但我放弃了。虽然我之前推荐过的那个钢琴项目弹的比这个要好听，但我更喜欢这个项目。因为我从他的项目中感受到满满敬意和“爱”，致敬每一位奋斗的“代码家”，HG 爱你们。[在线尝试](http://wscats.gitee.io/piano/build/)，示例代码：
```javascript
playSong(song) {
  this.setSong([...song])
  let offset = 0
  let time = 0
  let playSong = async () => {
    // 右边是从外部来中断递归
    if (offset < song.length && this.store.data.song.length > 0) {
      switch (typeof song[offset]) {
        // 简谱2演奏方法 根据 ++12345--6. 简单旋律情况
        case 'string':
          let letters = song[offset].match(/[0-9]/g)
          switch (letters.length) {
            case 1:
              time = this.handleString(song, offset)
              break
            default:
              time = this.handleStrings(song, offset)
              break
          }
          break
        // 简谱1演奏方法 根据 CDEFGAB，复杂旋律情况，比如有和弦
        case 'object':
          console.log(song[offset]['note'])
          time = song[offset]['time'];
          this.playNote(song[offset]['note'])
          break;
        case 'number':
          // 休止符
          switch (song[offset]) {
            case 0:
              time = 1000
              break
          }
          break
      }
      await new Promise((resolve) => {
        let timer = setTimeout(() => {
          clearInterval(timer)
          resolve()
        }, time)
      })
      offset++
      // 自定义事件，跟下面底部的音符自动跳动结合
      this.add()
      playSong()
    } else {
      // 暂停播放
      clearTimeout(this.timer)
      this.store.data.song = []
      this.store.data.count = 0
      return
    }
  }
  playSong()
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/84766582.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[screenity](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alyssaxuu/screenity)：一个强大的屏幕录制和标注的 Chrome 插件。特性：
- 🎥  可以录制任何应用的内容，包含“色相头”
- ✏️  在屏幕上的任何地方，添加文本和箭头等注释
- 👀  突出你的点击操作、光标
- 💾  支持导出为 mp4、gif 等常用格式
- ✂️  修剪或删除录像


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/309123651.gif' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C 项目
17、[Sloth](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sveinbjornt/Sloth)：一款 macOS 系统下显示进程打开的文件、socket、管道等信息的工具。就像桌面版的 lsof，快来试试吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/1535038.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
18、[flask-state](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yoobool/flask-state)：一款轻便的机器状态监控 Flask 插件。示例代码：
```
flask_state.init_app(app)
// npm
import 'echarts';
import 'flask-state/flask-state.min.css';
import {init} from 'flask-state';
// Create a DOM node with ID 'test'. After init() binds the node, click to open the listening window
init({dom:document.getElementById('test')});
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/290091588.png' style="max-width:80%; max-height=80%;"></img></p>

19、[gopup](https://hellogithub.com/periodical/statistics/click?target=https://github.com/justinzm/gopup)：采集各种权威公开数据的 Python 库。示例代码：
```python
# 安装：pip isntall gopup 

import gopup as gp
covid_baidu_df = gp.covid_baidu(indicator="热搜谣言粉碎")
print(covid_baidu_df)
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/248739733.png' style="max-width:80%; max-height=80%;"></img></p>

20、[python-cheatsheet](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gto76/python-cheatsheet)：全面且实用的 Python 备忘录。这个东西特别适合我这个上了年纪的人，比如：忘记怎么用 Python 写正则、要搞个进度条忘记库的名字和基本用法、用 pandas 处理数据忘记方法需要的参数等等。正当我觉得自己需要“回炉重学”的时候发现了这个项目，有了它上面的问题都可以找到拿来即用的代码片段。我又是那个快乐的 Pythoneer 了，示例代码：
```python
# $ pip3 install tqdm
>>> from tqdm import tqdm
>>> from time import sleep
>>> for el in tqdm([1, 2, 3], desc='Processing'):
...     sleep(1)
Processing: 100%|████████████████████| 3/3 [00:03<00:00,  1.00s/it]
```


21、[running_page](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yihong0618/running_page)：一个展示个人跑步主页的 Python 项目。特性：
- GitHub Actions 管理自动同步跑步进程及自动生成新的页面
- Gatsby 生成的静态网页，速度快
- Mapbox 进行地图展示
- 支持 Nike、Runtastic、佳明、Keep 的数据
- 自动备份 gpx 数据，方便备份及上传到其它软件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/296233312.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
22、[eul](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gao-sun/eul)：一款极简免费的 macOS 状态监控工具。我就在用，强烈推荐给你


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/275095333.jpg' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
23、[DeepLearningProject](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Spandan-Madan/DeepLearningProject)：哈佛大学开源的深度学习教程


24、[EasyOCR](https://hellogithub.com/periodical/statistics/click?target=https://github.com/JaidedAI/EasyOCR)：支持多种语言的即用型的 Python OCR 库，包括中文、日文、韩文等。示例代码：
```python
import easyocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
result = reader.readtext('chinese.jpg')
# 输出
[([[189, 75], [469, 75], [469, 165], [189, 165]], '愚园路', 0.3754989504814148),
 ([[86, 80], [134, 80], [134, 128], [86, 128]], '西', 0.40452659130096436),
 ([[517, 81], [565, 81], [565, 123], [517, 123]], '东', 0.9989598989486694),
 ([[78, 126], [136, 126], [136, 156], [78, 156]], '315', 0.8125889301300049),
 ([[514, 126], [574, 126], [574, 156], [514, 156]], '309', 0.4971577227115631),
 ([[226, 170], [414, 170], [414, 220], [226, 220]], 'Yuyuan Rd.', 0.8261902332305908),
 ([[79, 173], [125, 173], [125, 213], [79, 213]], 'W', 0.9848111271858215),
 ([[529, 173], [569, 173], [569, 213], [529, 213]], 'E', 0.8405593633651733)]
```


25、[examples](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pytorch/examples)：关于视觉、本文等方面的 PyTorch 的示例集合。包含：使用 Convnets 的图像分类（MNIST）、生成对抗网络（DCGAN）等


### 其它
26、[CopyTranslator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/CopyTranslator/CopyTranslator)：支持网页和 PDF 的划词翻译工具。有了它就可以解决阅读 PDF 文件时，要翻译大段内容情况下的乱码、换行、翻译不准的问题


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/134030857.gif' style="max-width:80%; max-height=80%;"></img></p>

27、[Front-End-Interview-Notebook](https://hellogithub.com/periodical/statistics/click?target=https://github.com/CavsZhouyou/Front-End-Interview-Notebook)：一份非拼凑、优秀的前端面试复习笔记。以提问方式发出问题，并给出了作者的答案，内容涵盖：HTML、CSS、JS、算法、计算机网络等方面。作者拿到了很多大厂 offer，然后把这些东西总结整理下来送给准备面试、换工作的前端小伙伴


28、[pi-hole](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pi-hole/pi-hole)：一个免费开源、部署简单的 DNS sinkhole 项目。没关系，我也不明白 DNS sinkhole 是个啥，就知道用它可实现路由器层屏蔽广告的功能。需要先在树莓派安装这个项目，然后配合支持自定义 DNS 的路由器，就可以实现该网络下的全设备广告自动屏蔽。[详细步骤](https://sspai.com/post/58183)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/20619036.png' style="max-width:80%; max-height=80%;"></img></p>

29、[styleguide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/google/styleguide)：谷歌的代码风格指南。每个大型项目都有自己的代码风格，当代码的风格统一时将更容易被理解。本项目是谷歌项目的代码风格说明，包含：C++、C#、Swift、Python、Java 等语言


30、[upptime](https://hellogithub.com/periodical/statistics/click?target=https://github.com/upptime/upptime)：一个免费开源的网站正常运行时间（uptime）监控服务。之所没有任何费用是因为实现方法都是完全基于 GitHub 提供的免费服务，比如：使用 GitHub 的 Action 每隔 5 分钟访问一次目标网站，获取网站最新的状态。然后通过 GitHub Issues 记录和报告异常，最后在 GitHub Pages 上可视化展示网站的运行状态。就很“绿色无公害”，我特别喜欢


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/286080143.png' style="max-width:80%; max-height=80%;"></img></p>

31、[winapps](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Fmstrat/winapps)：一个让你在 Linux (Ubuntu/Fedora) 系统里使用 Windows 办公软件的项目。支持 Microsoft Excel、Word、PowerPoint、Adobe Photoshop 等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/56/310933773.gif' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub55.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub57.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/56'>这里</a>。
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
