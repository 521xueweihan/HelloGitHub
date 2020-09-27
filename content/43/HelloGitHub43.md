# 《HelloGitHub》第 43 期
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
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [教程](#教程)
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
1、[tmux](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tmux/tmux)：一个终端复用工具，可极大的提高工作效率。
-  提供了强劲的、易于使用的命令行界面
-  可横向和纵向分割窗口
-  窗格可以自由移动和调整大小，或直接利用四个预设布局之一
-  可在多个缓冲区进行复制和粘贴
-  可通过交互式菜单来选择窗口、会话及客户端
-  等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/tmux.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
2、[BenchmarkDotNet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dotnet/BenchmarkDotNet)：功能强大的用于基准测试 .NET 库

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/BenchmarkDotNet.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
3、[CppNet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/caozhiyi/CppNet)：一个封装在 Tcp 协议上的 Proactor 模式 multi-thread 网络库。包含 OS 接口调用、回调处理、定时器、缓存管理等，这里有从操作系统到应用层的所有网络细节，便于初学者学习和实践。
- 简单：只导出了最少量的接口，其声明都类似系统 socket API。对客户端而言，只新增了一个 buffer 类型
- 快速：采用性能最优的 epoll 和 IOCP 做事件驱动，惊群处理交由内核。每个连接都独享一个内存池，从内存池中申请的内存都由智能指针管理
- 清晰：结构上分为事件驱动，会话管理，接口三层，通过回调向上通知。模块之间职责分工明确，最大的类不超过 500 行代码

4、[dbg-macro](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sharkdp/dbg-macro)：打日志是 C++ 开发中必不可少的一种 debug 方式，[dbg-macro](https://github.com/sharkdp/dbg-macro) 受 [rust-lang](https://www.rust-lang.org) 中 的 [dbg](https://doc.rust-lang.org/std/macro.dbg.html) 启发，提供比 printf 和 std::cout 更好的宏函数。主要有如下特点：
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

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/dbg-macro.png' style="max-width:80%; max-height=80%;"></img></p>

5、[CppCon2019](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/CppCon/CppCon2019)：C++ 2019 大会的幻灯片和相关材料集合

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
6、[RedisShake](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alibaba/RedisShake)：阿里开源的用于 redis 数据同步的工具。原理图如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/RedisShake.png' style="max-width:80%; max-height=80%;"></img></p>

7、[bigcache](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/allegro/bigcache)：基于 Go 语言的高性能大缓存库。在 Ubuntu 18.04 LTS，机器配置 i7-6700K CPU @ 4.00GHz with 32GB of RAM 上性能测试结果：
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

8、[pacgo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/danicat/pacgo)：基于 Go 实现的终端吃豆人游戏

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/pacgo.jpg' style="max-width:80%; max-height=80%;"></img></p>

9、[go-admin](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/GoAdminGroup/go-admin)：基于 Golang 语言的数据可视化与管理平台。特性如下：
- 🚀高生产效率：10 分钟内做一个好看的管理后台
- 🎨主题：默认为 adminlte，更多好看的主题正在制作中，欢迎给我们留言
- 🔢插件化：提供插件使用，真正实现一个插件解决不了问题，那就两个
- ✅认证：开箱即用的 rbac 认证系统
- ⚙️框架支持：支持大部分框架接入，让你更容易去上手和扩展

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/go-admin.png' style="max-width:80%; max-height=80%;"></img></p>

10、[zerolog](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rs/zerolog)：一个速度快、专门用于输出 JSON 格式日志的库。还在为解析不规则的日志而烦恼吗？有了 zerolog 你可以跳起来了！当然它还有低效但可在控制台输出漂亮日志的模式，快去试试吧。示例代码：
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

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/zerolog.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
11、[AutoUpdateProject](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MZCretin/AutoUpdateProject)：一个简单易用、接入方便、UI 多样的 Android 内实现在线更新的库。示例代码：
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

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/AutoUpdateProject.png' style="max-width:80%; max-height=80%;"></img></p>

12、[spring-analysis](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/seaswalker/spring-analysis)：Spring 框架源码讲解。包括：spring-core、spring-aop、spring-context、spring-taskspring-mvc 等部分

13、[eladmin](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/elunez/eladmin)：基于 Spring Boot 2.1.0、Vue 的前后端分离的后台管理系统，支持数据字典与数据权限管理、一键生成前后端代码、前端菜单动态路由等。基于 Spring Boot2.1.0 框架，涉及的技术栈：非关系数据库 redis、接口测试工具 swagger、druid 数据源驱动、邮件依赖（javax.mail）、三方支付和云存储 SDK、页面模板引擎 freemarker。技术栈丰富，初学者可以作为实战项目学习和使用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/eladmin.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
14、[nzh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cnwhy/nzh)：阿拉伯数字与中文数字相互转化的 JS 库。示例代码如下：
```javascript
var nzhcn = Nzh.cn;                 // 使用简体中文,  另外有 Nzh.hk -- 繁体中文
nzhcn.encodeS(100111);              // 转中文小写 >> 十万零一百一十一
nzhcn.encodeB(100111);              // 转中文大写 >> 壹拾万零壹佰壹拾壹
nzhcn.encodeS("1.23456789e+21");    // 科学记数法字符串 >> 十二万三千四百五十六万万七千八百九十万亿
nzhcn.toMoney("100111.11");         // 转中文金额 >> 人民币壹拾万零壹佰壹拾壹元壹角壹分
```

15、[request](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/request/request)： JavaScript 简单、易用的 HTTP 请求客户端。示例代码：
```javascript
const request = require('request');
request('https://hellogithub.com', function (error, response, body) {
  console.error('error:', error); // 如果请求发生错误将被打印
  console.log('statusCode:', response && response.statusCode); // 输出返回的状态码
  console.log('body:', body); // 输出返回的 HTML 
});
```

16、[SandDance](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/SandDance)：微软开源的数据可视化库。使用单元可视化，将数据库中的行一对一映射到屏幕中。在进行数据交互时，视图可无缝平滑过渡，展示效果炫酷

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/SandDance.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[chart-race-react](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bchao1/chart-race-react)：一个简单易用的 Bar Chart Race（长条图赛跑动画） React 组件。示例代码：
```javascript
import ReactDOM from 'react-dom';
import BarChart from 'chart-race-react';

ReactDOM.render(<BarChart />, document.getElementById('root'));
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/chart-race-react.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[fiora](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yinxin630/fiora)：一个功能丰富、支持多端的在线聊天室。它界面小清新，支持基本的聊天功能的同时还有好玩的消息朗读功能。项目上基于 TypeScript + React 16.9 代码逻辑清晰、注释较为完善，适合用来学习 node.js、 TypeScript、React 等技术

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/fiora.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
19、[RPA-Python](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tebelorg/RPA-Python)：一个 Python 自动化操作的库。比如：自动打开网页并截图，示例代码：
```python
t.init()
t.url('https://www.google.com')
t.type('q', 'decentralization[enter]')
t.snap('page', 'results.png')
t.close()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/TagUI-Python.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
20、[shift](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/square/shift)：一个 Ruby 语言写的在线 MySQL 数据库迁移工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/shift.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
21、[Percentage](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sindresorhus/Percentage)：让 Swift 语言支持百分比类型，消除精度缺失的烦恼。示例代码：
```swift
import Percent

10% + 5.5%
//=> 15.5%
-10% / 2
//=> -5%
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
22、[curlconverter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NickCarneiro/curlconverter)：把 curl 命令转化成各语言的代码的工具，支持 Python、JavaScript、PHP、R、Go 等语言。[在线体验](https://curl.trillworks.com/)

23、[hub](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/github/hub)：通过命令行的方式来操作 GitHub，支持绝大多数的操作。比如：创建远程仓库、删除远程仓库、提交 PR、管理 issue 等，常用操作：
- 创建远程仓库：hub create github-repository
- 删除远程仓库：hub delete github-repository
- fork 项目：hub fork

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/hub.png' style="max-width:80%; max-height=80%;"></img></p>

24、[cascadia-code](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/cascadia-code)：微软开源的一套等宽字体，有趣的是可以组合字符创建新的字形。组合效果如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/cascadia-code.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[Administrative-divisions-of-China](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/modood/Administrative-divisions-of-China)：中国行政区划（五级）：省级、地级、县级、乡级和村级的数据集和爬虫程序

26、[vim-airline](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vim-airline/vim-airline)：一个让每个 Vim 窗口的底部，都有一个漂亮状态行的插件。展示信息和效果如下图：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/vim-airline.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
27、[python_ebook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/shihyu/python_ebook)：Python 编程相关的电子书资源集合项目

28、[book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cosmicpython/book)：（英文）《Cosmic Python》讲述如何管理复杂性的 Pythonic 应用程序结构的书籍

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 教程
29、[BigData-Notes](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/heibaiying/BigData-Notes)：大数据入门教程，该教程介绍了大数据常用技术栈的基础和核心知识。内容涵盖：Hadoop、Spark、Storm、HBase、Hive、ZooKeeper、Kafka 等

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
30、[Ultra-Light-Fast-Generic-Face-Detector-1MB](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)：1MB 大小的轻量级人脸检测模型。该模型是针对边缘计算设备，基于 libfacedetection 替换压缩网络设计实现

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/Ultra-Light-Fast-Generic-Face-Detector-1MB.jpg' style="max-width:80%; max-height=80%;"></img></p>

31、[dimensionality_reduction_alo_codes](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/heucoder/dimensionality_reduction_alo_codes)：该项目使用 Python 实现了 11 种经典的数据抽取（数据降维）算法。同时附有相关资料、展示效果，适用于机器学习初学者和刚刚入坑数据挖掘的小伙伴

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/43/img/dimensionality_reduction_alo_codes.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/42/HelloGitHub42.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/44/HelloGitHub44.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
