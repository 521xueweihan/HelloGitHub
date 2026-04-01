# HelloGitHub Vol.43
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
1、[tmux](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tmux/tmux)：一个终端复用工具，可极大的提高工作效率。
-  提供了强劲的、易于使用的命令行界面
-  可横向和纵向分割窗口
-  窗格可以自由移动和调整大小，或直接利用四个预设布局之一
-  可在多个缓冲区进行复制和粘贴
-  可通过交互式菜单来选择窗口、会话及客户端
-  等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/36836475.png' style="max-width:80%; max-height=80%;"></img></p>

### C#
2、[BenchmarkDotNet](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dotnet/BenchmarkDotNet)：功能强大的用于基准测试 .NET 库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/12191244.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
3、[CppCon2019](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/CppCon/CppCon2019)：C++ 2019 大会的幻灯片和相关材料集合


4、[CppNet](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/caozhiyi/CppNet)：一个封装在 Tcp 协议上的 Proactor 模式 multi-thread 网络库。包含 OS 接口调用、回调处理、定时器、缓存管理等，这里有从操作系统到应用层的所有网络细节，便于初学者学习和实践。
- 简单：只导出了最少量的接口，其声明都类似系统 socket API。对客户端而言，只新增了一个 buffer 类型
- 快速：采用性能最优的 epoll 和 IOCP 做事件驱动，惊群处理交由内核。每个连接都独享一个内存池，从内存池中申请的内存都由智能指针管理
- 清晰：结构上分为事件驱动，会话管理，接口三层，通过回调向上通知。模块之间职责分工明确，最大的类不超过 500 行代码


5、[dbg-macro](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sharkdp/dbg-macro)：打日志是 C++ 开发中必不可少的一种 debug 方式，[dbg-macro](https://github.com/sharkdp/dbg-macro) 受 [rust-lang](https://www.rust-lang.org) 中 的 [dbg](https://doc.rust-lang.org/std/macro.dbg.html) 启发，提供比 printf 和 std::cout 更好的宏函数。主要有如下特点：
- 美观的彩色输出（当输出不是交互式终端时，颜色将自动禁用） 
- 兼容 C++11，并且是 header-only
- 支持基础类型和 STL 容器类型的输出
- 除了基本信息外，还输出变量名和类型
- 启用 DBG_MACRO_DISABLE 生成 release 版 

```c++
#include <vector>
#include <dbg.h>

// You can use "dbg(..)" in expressions:
int factorial(int n) {
  if (dbg(n <= 1)) {
    return dbg(1);
  } else {
    return dbg(n * factorial(n - 1));
  }
}

int main() {
  std::string message = "hello";
  dbg(message);  // [example.cpp:15 (main)] message = "hello" (std::string)
  const int a = 2;
  const int b = dbg(3 * a) + 1;  // [example.cpp:18 (main)] 3 * a = 6 (int)
  std::vector<int> numbers{b, 13, 42};
  dbg(numbers);  // [example.cpp:21 (main)] numbers = {7, 13, 42} (size: 3) (std::vector<int>)
  dbg("this line is executed");  // [example.cpp:23 (main)] this line is executed
  factorial(4);
  return 0;
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/192787774.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
6、[bigcache](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/allegro/bigcache)：基于 Go 语言的高性能大缓存库。在 Ubuntu 18.04 LTS，机器配置 i7-6700K CPU @ 4.00GHz with 32GB of RAM 上性能测试结果：
```
go version
go version go1.13 linux/amd64

cd caches_bench; go test -bench=. -benchmem -benchtime=4s ./... -timeout 30m
goos: linux
goarch: amd64
pkg: github.com/allegro/bigcache/v2/caches_bench
BenchmarkMapSet-8                     	12999889	       376 ns/op	     199 B/op	       3 allocs/op
BenchmarkConcurrentMapSet-8           	 4355726	      1275 ns/op	     337 B/op	       8 allocs/op
BenchmarkFreeCacheSet-8               	11068976	       703 ns/op	     328 B/op	       2 allocs/op
BenchmarkBigCacheSet-8                	10183717	       478 ns/op	     304 B/op	       2 allocs/op
BenchmarkMapGet-8                     	16536015	       324 ns/op	      23 B/op	       1 allocs/op
BenchmarkConcurrentMapGet-8           	13165708	       401 ns/op	      24 B/op	       2 allocs/op
BenchmarkFreeCacheGet-8               	10137682	       690 ns/op	     136 B/op	       2 allocs/op
BenchmarkBigCacheGet-8                	11423854	       450 ns/op	     152 B/op	       4 allocs/op
BenchmarkBigCacheSetParallel-8        	34233472	       148 ns/op	     317 B/op	       3 allocs/op
BenchmarkFreeCacheSetParallel-8       	34222654	       268 ns/op	     350 B/op	       3 allocs/op
BenchmarkConcurrentMapSetParallel-8   	19635688	       240 ns/op	     200 B/op	       6 allocs/op
BenchmarkBigCacheGetParallel-8        	60547064	        86.1 ns/op	     152 B/op	       4 allocs/op
BenchmarkFreeCacheGetParallel-8       	50701280	       147 ns/op	     136 B/op	       3 allocs/op
BenchmarkConcurrentMapGetParallel-8   	27353288	       175 ns/op	      24 B/op	       2 allocs/op
PASS
ok  	github.com/allegro/bigcache/v2/caches_bench	256.257s
```


7、[go-admin](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GoAdminGroup/go-admin)：基于 Golang 语言的数据可视化与管理平台。特性如下：
- 🚀高生产效率：10 分钟内做一个好看的管理后台
- 🎨主题：默认为 adminlte，更多好看的主题正在制作中，欢迎给我们留言
- 🔢插件化：提供插件使用，真正实现一个插件解决不了问题，那就两个
- ✅认证：开箱即用的 rbac 认证系统
- ⚙️框架支持：支持大部分框架接入，让你更容易去上手和扩展


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/137854081.png' style="max-width:80%; max-height=80%;"></img></p>

8、[pacgo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/danicat/pacgo)：基于 Go 实现的终端吃豆人游戏


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/148397397.jpg' style="max-width:80%; max-height=80%;"></img></p>

9、[RedisShake](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tair-opensource/RedisShake)：阿里开源的用于 redis 数据同步的工具。原理图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/173063554.png' style="max-width:80%; max-height=80%;"></img></p>

10、[zerolog](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rs/zerolog)：一个速度快、专门用于输出 JSON 格式日志的库。还在为解析不规则的日志而烦恼吗？有了 zerolog 你可以跳起来了！当然它还有低效但可在控制台输出漂亮日志的模式，快去试试吧。示例代码：
```go
package main

import (
    "github.com/rs/zerolog"
    "github.com/rs/zerolog/log"
)

func main() {
    zerolog.TimeFieldFormat = zerolog.TimeFormatUnix

    log.Info().Msg("hello world")
}

// Output: {"time":1516134303,"level":"info","message":"hello world"}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/91054480.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
11、[AutoUpdateProject](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/MZCretin/AutoUpdateProject)：一个简单易用、接入方便、UI 多样的 Android 内实现在线更新的库。示例代码：
```java
//更新库配置
UpdateConfig updateConfig = new UpdateConfig()
        .setDebug(true)//是否是Debug模式
        .setBaseUrl("http://www.cretinzp.com/system/versioninfo")//当 dataSourceType 为 DATA_SOURCE_TYPE_URL 时，配置此接口用于获取更新信息
        .setMethodType(TypeConfig.METHOD_GET)//当 dataSourceType 为 DATA_SOURCE_TYPE_URL 时，设置请求的方法
        .setDataSourceType(TypeConfig.DATA_SOURCE_TYPE_URL)//设置获取更新信息的方式
        .setShowNotification(true)//配置更新的过程中是否在通知栏显示进度
        .setNotificationIconRes(R.mipmap.download_icon)//配置通知栏显示的图标
        .setUiThemeType(TypeConfig.UI_THEME_AUTO)//配置 UI 的样式，一种有 12 种样式可供选择
        .setRequestHeaders(null)//当 dataSourceType 为 DATA_SOURCE_TYPE_URL 时，设置请求的请求头
        .setRequestParams(null)//当 dataSourceType 为 DATA_SOURCE_TYPE_URL 时，设置请求的请求参数
        .setCustomActivityClass(CustomActivity.class)//如果你选择的 UI 样式为 TypeConfig.UI_THEME_CUSTOM，那么你需要自定义一个 Activity 继承自 RootActivity 并参照 demo 实现功能，在此处填写自定义 Activity 的 class
        .setModelClass(new UpdateModel());
AppUpdateUtils.init(this, updateConfig);
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/84809523.png' style="max-width:80%; max-height=80%;"></img></p>

12、[eladmin](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/elunez/eladmin)：基于 Spring Boot 2.1.0、Vue 的前后端分离的后台管理系统，支持数据字典与数据权限管理、一键生成前后端代码、前端菜单动态路由等。基于 Spring Boot2.1.0 框架，涉及的技术栈：非关系数据库 redis、接口测试工具 swagger、druid 数据源驱动、邮件依赖（javax.mail）、三方支付和云存储 SDK、页面模板引擎 freemarker。技术栈丰富，初学者可以作为实战项目学习和使用


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/161757837.png' style="max-width:80%; max-height=80%;"></img></p>

13、[spring-analysis](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/seaswalker/spring-analysis)：Spring 框架源码讲解。包括：spring-core、spring-aop、spring-context、spring-taskspring-mvc 等部分


### JavaScript
14、[chart-race-react](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bchao1/chart-race-react)：一个简单易用的 Bar Chart Race（长条图赛跑动画） React 组件。示例代码：
```javascript
import ReactDOM from 'react-dom';
import BarChart from 'chart-race-react';

ReactDOM.render(<BarChart />, document.getElementById('root'));
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/216373471.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[fiora](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yinxin630/fiora)：一个功能丰富、支持多端的在线聊天室。它界面小清新，支持基本的聊天功能的同时还有好玩的消息朗读功能。项目上基于 TypeScript + React 16.9 代码逻辑清晰、注释较为完善，适合用来学习 node.js、 TypeScript、React 等技术


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/51762221.png' style="max-width:80%; max-height=80%;"></img></p>

16、[nzh](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cnwhy/nzh)：阿拉伯数字与中文数字相互转化的 JS 库。示例代码如下：
```javascript
var nzhcn = Nzh.cn;                 // 使用简体中文,  另外有 Nzh.hk -- 繁体中文
nzhcn.encodeS(100111);              // 转中文小写 >> 十万零一百一十一
nzhcn.encodeB(100111);              // 转中文大写 >> 壹拾万零壹佰壹拾壹
nzhcn.encodeS("1.23456789e+21");    // 科学记数法字符串 >> 十二万三千四百五十六万万七千八百九十万亿
nzhcn.toMoney("100111.11");         // 转中文金额 >> 人民币壹拾万零壹佰壹拾壹元壹角壹分
```


17、[request](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/request/request)： JavaScript 简单、易用的 HTTP 请求客户端。示例代码：
```javascript
const request = require('request');
request('https://hellogithub.com', function (error, response, body) {
  console.error('error:', error); // 如果请求发生错误将被打印
  console.log('statusCode:', response && response.statusCode); // 输出返回的状态码
  console.log('body:', body); // 输出返回的 HTML 
});
```


18、[SandDance](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/SandDance)：微软开源的数据可视化库。使用单元可视化，将数据库中的行一对一映射到屏幕中。在进行数据交互时，视图可无缝平滑过渡，展示效果炫酷


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/156293506.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python
19、[RPA-Python](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tebelorg/RPA-Python)：一个 Python 自动化操作的库。比如：自动打开网页并截图，示例代码：
```python
t.init()
t.url('https://www.google.com')
t.type('q', 'decentralization[enter]')
t.snap('page', 'results.png')
t.close()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/178592227.gif' style="max-width:80%; max-height=80%;"></img></p>

### Ruby
20、[shift](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/square/shift)：一个 Ruby 语言写的在线 MySQL 数据库迁移工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/49679370.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
21、[Percentage](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sindresorhus/Percentage)：让 Swift 语言支持百分比类型，消除精度缺失的烦恼。示例代码：
```swift
import Percent

10% + 5.5%
//=> 15.5%
-10% / 2
//=> -5%
```


### AI
22、[dimensionality_reduction_alo_codes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/heucoder/dimensionality_reduction_alo_codes)：该项目使用 Python 实现了 11 种经典的数据抽取（数据降维）算法。同时附有相关资料、展示效果，适用于机器学习初学者和刚刚入坑数据挖掘的小伙伴


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/191011404.png' style="max-width:80%; max-height=80%;"></img></p>

23、[Ultra-Light-Fast-Generic-Face-Detector-1MB](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)：1MB 大小的轻量级人脸检测模型。该模型是针对边缘计算设备，基于 libfacedetection 替换压缩网络设计实现


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/214118425.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Other
24、[Administrative-divisions-of-China](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/modood/Administrative-divisions-of-China)：中国行政区划（五级）：省级、地级、县级、乡级和村级的数据集和爬虫程序


25、[BigData-Notes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/heibaiying/BigData-Notes)：大数据入门教程，该教程介绍了大数据常用技术栈的基础和核心知识。内容涵盖：Hadoop、Spark、Storm、HBase、Hive、ZooKeeper、Kafka 等


26、[cascadia-code](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/cascadia-code)：微软开源的一套等宽字体，有趣的是可以组合字符创建新的字形。组合效果如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/196284711.gif' style="max-width:80%; max-height=80%;"></img></p>

27、[curlconverter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/curlconverter/curlconverter)：把 curl 命令转化成各语言的代码的工具，支持 Python、JavaScript、PHP、R、Go 等语言。[在线体验](https://curl.trillworks.com/)


28、[hub](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mislav/hub)：通过命令行的方式来操作 GitHub，支持绝大多数的操作。比如：创建远程仓库、删除远程仓库、提交 PR、管理 issue 等，常用操作：
- 创建远程仓库：hub create github-repository
- 删除远程仓库：hub delete github-repository
- fork 项目：hub fork


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/401025.png' style="max-width:80%; max-height=80%;"></img></p>

29、[vim-airline](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vim-airline/vim-airline)：一个让每个 Vim 窗口的底部，都有一个漂亮状态行的插件。展示信息和效果如下图：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/11075527.gif' style="max-width:80%; max-height=80%;"></img></p>

### Book
30、[book](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cosmicpython/book)：（英文）《Cosmic Python》讲述如何管理复杂性的 Pythonic 应用程序结构的书籍




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub42.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub44.md">『Next』</a>
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
