# 《HelloGitHub》第 73 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 目录

**Tips**：如果文中的图刷不出来，可以点击 [这里](https://hellogithub.com/periodical/volume/73/) 获取更好的阅读体验。

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
- [Ruby 项目](#Ruby-项目)
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
1、[lvgl](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lvgl/lvgl)：美观易用的轻量级嵌入式系统图形库
- 拥有丰富的图形组件：按键、图表、图片等
- 支持多种输入设备：触摸屏、键盘、按键等
- 最低资源占用：64 kB ROM、16 kB RAM
- 不依赖特定的硬件平台，可在多种显示屏上运行
- 支持多语种：中文、韩文、阿拉伯文等
- 丰富详细的示例

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/lvgl.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[uthash](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/troydhanson/uthash)：为 C 语言提供哈希表的库。由于 C 语言中没有类似字典的数据结构，该库提供了哈希表常见的查询、插入、删除、排序等函数。使用方法简单，仅需引入一个头文件
```c
#include "uthash.h"

struct my_struct {
    int id;            /* we'll use this field as the key */
    char name[10];
    UT_hash_handle hh; /* makes this structure hashable */
};

struct my_struct *users = NULL;

void add_user(struct my_struct *s) {
    HASH_ADD_INT( users, id, s );
}
```

3、[warpd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rvaiya/warpd)：用键盘代替鼠标的工具。拥有多种操作模式比如方向键移动鼠标和区域选择，但仅支持 Linux 和 macOS 系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/warpd.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
4、[TradingSystem](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/oybab/TradingSystem)：开源的交易管理系统。包含了服务器端、PC 客户端、手机客户端的源码，支持中文界面、交易管理、打印小票、会员管理、统计报表等功能，适用于餐厅、超市、酒店等领域。使用和二次开发前请认真阅读开源协议

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/TradingSystem.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
5、[Cytopia](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CytopiaTeam/Cytopia)：免费开源的像素风模拟城市建设游戏

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/Cytopia.png' style="max-width:80%; max-height=80%;"></img></p>

6、[FileCentipede](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/filecxx/FileCentipede)：一个用 C++ 和 Qt 编写的跨平台文件下载器。它界面简洁、下载速度快、支持多协议，还有浏览器插件可用来下载网页中的视频和音频

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/FileCentipede.png' style="max-width:80%; max-height=80%;"></img></p>

7、[ydb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ydb-platform/ydb)：Yandex 开源的企业级分布式 SQL 数据库。具有高可用、易扩展、事务、强一致性、灾后自动恢复等特点，提供 Web 平台方便查询以及 Go、Java、Python、JavaScript  等多种编程语言 SDK

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/ydb.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
8、[simple.css](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kevquirk/simple.css)：超轻量级的 CSS 框架。不引入新的样式类，仅把 HTML 元素设为合理值，从而实现仅用 HTML 元素就可以构建美观、响应式的网页

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/simple.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
9、[monitoror](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/monitoror/monitoror)：平铺的监控工具。安装简单配置方便的“监控墙”，所有监控指标以平铺的方式展示，美观且一目了然。支持 Linux、macOS 和 Windows 主流操作系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/monitoror.png' style="max-width:80%; max-height=80%;"></img></p>

10、[yomo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yomorun/yomo)：低延时流式边缘计算框架。它基于 QUIC（快速 UDP 互联网连接）协议实现，有效地提高了数据传输率和稳定性，实现在复杂网络环境下数据依然可以超低时延传输和处理。原生支持多地域分布式的部署模式，使得终端用户可就近访问节点，保证数据传输的低延时。适用于开发实时交互的应用，比如在线协作 SaaS、元宇宙、AR/VR、云游戏、物联网 IoT 等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/yomo.png' style="max-width:80%; max-height=80%;"></img></p>

11、[gorse](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gorse-io/gorse)：由 Go 语言实现的推荐系统引擎。无需具备推荐系统相关知识，就能轻而易举地搭建推荐系统。开发者只需将用户信息、物料信息和互动数据（例如点赞、收藏等）导入系统，Gorse 就会自动训练模型为每个用户生成推荐

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/gorse.png' style="max-width:80%; max-height=80%;"></img></p>

12、[lal](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/q191201771/lal)：纯 Go 开发的流媒体服务器。完备的直播服务器，支持多种常见编码格式和 RTMP、RTSP、HLS 等协议

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/lal.png' style="max-width:80%; max-height=80%;"></img></p>

13、[casdoor](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/casdoor/casdoor)：提供登陆界面的身份访问管理平台。提供中文界面的用户管理后台，支持多种第三方登录、单点登录以及手机/邮箱验证码、找回密码等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/casdoor.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
14、[javamelody](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/javamelody/javamelody)：监控 Java、Java Web 应用程序的工具。监控包含 HTTP 请求、SQL 耗时、方法执行次数、错误百分比、Java 内存等指标，支持自定义时间维度和导出报告

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/javamelody.png' style="max-width:80%; max-height=80%;"></img></p>

15、[guice](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/guice)：轻量级 Java 依赖注入框架。不需要大量的模版代码，即可编写依赖注入的代码。使开发和调试更容易、更快速，适合个人开发者在小项目中使用
```java
import javax.inject.Inject;
import com.google.inject.Guice;
import com.google.inject.Injector;
import com.google.inject.Module;

public class Main {
    @Inject
    private HelloWorldService service;//hello service
    
    public static void main(String[] args) {
        Main main = new Main();
        Module module = new HelloWorldModule();
        Injector injector = Guice.createInjector(module);
        injector.injectMembers(main);//injects the implementation of the service
        
        main.testGuice();
    }

    public void testGuice()
    {
        service.sayHello();//usage of the service
    }
}
```

16、[databasir](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vran-dev/databasir)：一款数据库模型文档管理平台。支持自动同步数据库元数据并生成文档，解决数据模型文档管理中的内容更新不及时等问题

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/databasir.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[streamx](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/streamxhub/streamx)：Flink/Spark 极速开发框架，一站式流数据处理平台。提供开箱即用的流式大数据开发体验，可在平台上统一管理配置、开发、测试、部署、监控、运维的整个过程

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/streamx.jpg' style="max-width:80%; max-height=80%;"></img></p>

18、[stendhal](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/arianne/stendhal)：一款免费、开源的多人在线冒险（MMORPG）游戏。项目采用 Java 语言编写，虽然游戏画面复古还是 2D 但拥有数百种物品、怪物、NPC、任务和自由交易组成的丰富世界。玩家可以通过完成任务得到经验和金钱，更新装备逐渐变强探索更多新的地图。该游戏从 2005 年开源持续维护至今，[在线试玩](https://stendhalgame.org/client/stendhal.html)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/stendhal.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
19、[nanoid](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ai/nanoid)：用于生成随机 ID 的 JS 库
- 小巧：无依赖，仅 130 字节
- 快速：比 UUID 快 60%
- 安全：加密的强随机 API，可在集群中使用
- 紧凑：它使用比 UUID 更大的字母表
- 易用：已移植到 20 多种编程语言
```javascript
const { nanoid } = require('nanoid');
nanoid(); //=> "U9HDHNW3BkWMEd6GV_QPa"
```

20、[rubiks-cube](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pengfeiw/rubiks-cube)：使用 Three.js 制作的 3D 魔方。支持自定义魔方阶数，[在线尝试](https://pengfeiw.github.io/minicode/threejs-rubik)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/rubiks-cube.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[nexe](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nexe/nexe)：可将 Node.js 应用程序，打包成一个可执行文件的命令行工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/nexe.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[cnchar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/theajack/cnchar)：小巧的汉字处理 JS 库。支持简体字拼音、多音字、笔画数等功能
```javascript
let spell = cnchar.spell('你好');
let stroke = cnchar.stroke('你好');
console.log(spell, stroke);
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/cnchar.png' style="max-width:80%; max-height=80%;"></img></p>

23、[rough](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rough-stuff/rough)：手绘风格的图形库。可以让你用素描、类似手绘的风格来绘制图形
```javascript
const rc = rough.canvas(document.getElementById('canvas'));
rc.rectangle(10, 10, 200, 200); // x, y, width, height
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/rough.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Kotlin 项目
24、[architecture-samples](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/android/architecture-samples)：Android 架构蓝图。该项目是官方给出的 Android 应用设计建议，展示并讨论了如何设计 Android 应用架构，以及保证项目的可测试和可维护性。还有一个简单的 to-do 应用作为示例，方便开发人员和初学者学习和理解

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/architecture-samples.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
25、[hammerspoon](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Hammerspoon/hammerspoon)：强大的 macOS 自动化工具。通过该项目可以方便地用 Lua 脚本与 macOS 系统 API 进行交互，实现操作窗口、鼠标、文件系统、屏幕等功能。可用于打造各种 macOS 便捷工具
```lua
hs.hotkey.bind({"cmd", "alt", "ctrl"}, "W", function()
  hs.notify.new({title="Hammerspoon", informativeText="Hello World"}):send()
end)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/hammerspoon.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
26、[pikepdf](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pikepdf/pikepdf)：用于读取和写入 PDF 文件的 Python 库
```python
import pikepdf

with pikepdf.open('input.pdf') as pdf:
    num_pages = len(pdf.pages)
    del pdf.pages[-1]
    pdf.save('output.pdf')
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/pikepdf.png' style="max-width:80%; max-height=80%;"></img></p>

27、[docker-py](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/docker/docker-py)：用 Python 操作 Docker 的库。Docker 官方出品的 Python 库，可以用来批量、自动管理镜像
```python
import docker
client = docker.from_env()
client.images.pull('nginx')
# <Image 'nginx'>
client.containers.run("ubuntu:latest", "echo hello world")
# 'hello world\n'
client.containers.list()
# [<Container '45e6d2de7c54'>, <Container 'db18e4f20eaa'>, ...]
```

28、[memray](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bloomberg/memray)：Python 的内存分析器。帮你分析 Python 应用的内存使用情况，找到内存泄漏的原因、占用内存多的代码、内存使用率高的原因。支持生成内存报告（火焰图、表格、树状图）和实时报告等模式，以及统计结果等功能
- 表格报告：memray table [options] <results>
- 实时报告：memray run --live application.py
- 统计结果：memray stats [options] <results>

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/memray.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[pinry](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pinry/pinry)：分享图片的开源网站。该项目前后端分离采用 Vue.js + Django 等技术栈，网站以平铺的方式展示图片，支持浏览、上传和搜索图片以及管理后台、个人页、增加标签等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/pinry.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[modin](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/modin-project/modin)：更快、类似 pandas 的数据处理和分析库。底层通过 Ray 或 Dask 加速计算，上层兼容大部分 pandas API。所以使用起来十分简单，仅需更改一行代码即可从 pandas 无缝切换到 Modin，同时获得更快的数据处理速度
```python
# import pandas as pd
import modin.pandas as pd
import numpy as np

frame_data = np.random.randint(0, 100, size=(2**10, 2**8))
df = pd.DataFrame(frame_data)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/modin.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
31、[lobsters](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lobsters/lobsters)：lobste.rs 网站的源码。采用 Rails 开发的网站，类似 Hacker News 以分享链接和讨论为核心。可用来二次开发类似的网站

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/lobsters.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Rust 项目
32、[gitv](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chenjiandongx/gitv)：由 Rust 编写的 Git 仓库分析和数据可视化的命令行工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/gitv.png' style="max-width:80%; max-height=80%;"></img></p>

33、[dnsguide](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/EmilHernvall/dnsguide)：用 Rust 从头写一个 DNS 服务的教程

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
34、[WordPress-iOS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wordpress-mobile/WordPress-iOS)：官方开源的 WordPress iOS 客户端

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/WordPress-iOS.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
35、[iRedMail](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/iredmail/iRedMail)：开箱即用的免费邮件服务器。通过该项目可以快速在 Linux/BSD 上部署邮件服务，除此之外还拥有 Web 管理平台，数据均存储在服务器上，即保证了数据隐私还易于迁移和备份

36、[WechatMomentScreenshot](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TransparentLC/WechatMomentScreenshot)：朋友圈截图生成工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/WechatMomentScreenshot.png' style="max-width:80%; max-height=80%;"></img></p>

37、[RedisInsight](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/RedisInsight/RedisInsight)：官方开源的 Redis 桌面管理工具。提供了可视化操作界面、监控、内存分析、管理 Redis 集群等功能

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/RedisInsight.png' style="max-width:80%; max-height=80%;"></img></p>

38、[getwidget](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ionicfirebaseapp/getwidget)：免费开源的 Flutter UI 库。包含 1000 多种常用组件，帮你快速、轻松地构建 Flutter 应用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/getwidget.png' style="max-width:80%; max-height=80%;"></img></p>

39、[SmartIDE](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SmartIDE/SmartIDE)：快速搭建云开发环境的工具。不需要手动安装任何工具、SDK、编辑器和设置环境变量等繁琐操作，一条命令即可获得所需的开发环境和 IDE，轻松实现云端开发

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/SmartIDE.png' style="max-width:80%; max-height=80%;"></img></p>

40、[vcard-personal-portfolio](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/codewithsadee/vcard-personal-portfolio)：用来展示个人信息的网站

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/vcard-personal-portfolio.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
41、[awk](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wuzhouhui/awk)：《AWK 程序设计语言》中文翻译

42、[tensorflow-internals](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/horance-liu/tensorflow-internals)：《TensorFlow 内核剖析》通过剖析 TF 源码的方式，介绍它的架构、领域模型、工作原理等知识。虽然讲解的 1.2 版本已经过时，但仍然可以用来了解知名机器学习框架的内部原理

43、[rCore-Tutorial-Book-v3](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rcore-os/rCore-Tutorial-Book-v3)：用 Rust 语言从零开始写一个基于 RISC-V 架构的类 Unix 内核。清华大学开源的中文教程，从计算机发展历史开始科普，一步步说到为何操作系统会诞生，以及现代操作系统必须具备的特性。实践方面也是从空文件夹开始，像搭乐高积木一样，慢慢将操作系统的核心开发出来，教程读起来简直像看小说一样让人欲罢不能。[在线阅读](https://rcore-os.github.io/rCore-Tutorial-Book-v3/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/rCore-Tutorial-Book-v3.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
44、[instant-ngp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NVlabs/instant-ngp)：加速训练 NeRF 模型的项目。英伟达开源的最快只需 5 秒，训练出一只狐狸 NeRF 模型的技术。即根据静态的 2D 图片通过神经网络建模，快速训练出可以放大且从任何角度观察都清晰的图片

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/73/img/instant-ngp.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub72.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub74.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1xF2ECA89A2592'>云主机 4 元/月</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>推荐项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有各种回馈粉丝活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/73/'>这里</a> 获取更好的阅读体验。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
