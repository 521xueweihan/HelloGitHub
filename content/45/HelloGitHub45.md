# 《HelloGitHub》第 45 期
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
- [Kotlin 项目](#Kotlin-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C 项目
1、[smartdns](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pymumu/smartdns)：一个运行在本地的 DNS 服务器。能够提高网络访问速度等诸多妙用，架构图如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/smartdns.png' style="max-width:80%; max-height=80%;"></img></p>

2、[xmake](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xmake-io/xmake)：一个基于 Lua 的轻量级跨平台自动构建工具。支持在各种主流平台上构建项目，主要用于解决 C/C++ 项目的跨平台构建，同时支持与其他语言的混合编译。工程配置语法简单易读，对初学者友好、上手方便
```bash
add_requires("libuv master", "ffmpeg", "zlib 1.20.*", "tbox >1.6.1")
target("test")
    set_kind("shared")
    add_files("src/*.c")
    add_packages("libuv", "ffmpeg", "tbox", "zlib")
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/xmake.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
3、[gui.cs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/migueldeicaza/gui.cs)：支持 Windows 和 Linux/Unix 的 .NET 终端 UI 工具库。方便实现终端 GUI 工具，并且可以实现终端中用鼠标啦

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/gui_cs.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Blog.Core](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/anjoy8/Blog.Core)：基于 ASP.NET Core 和 Vue 从零开始搭建前后端分离项目教程+实战项目。该项目从 .NET Core 基础讲起，内容完整、系统，对初学者和有一定基础的小伙伴都有借鉴和学习的价值

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/Blog_Core.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
5、[ThreadPool](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/progschj/ThreadPool)：一个简单的 C++11 线程池实现，代码加起来不到 100 行。示例代码：
```c++
// create thread pool with 4 worker threads
ThreadPool pool(4);

// enqueue and store future
auto result = pool.enqueue([](int answer) { return answer; }, 42);

// get result from future
std::cout << result.get() << std::endl;
```

6、[xournalpp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xournalpp/xournalpp)：一款支持 PDF 手写注释的笔记软件，支持 Linux、Windows、macOS 平台。看书的时候喜欢标注、做笔记，那这款工具肯定适合你。[下载地址](https://github.com/xournalpp/xournalpp/releases)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/xournalpp.png' style="max-width:80%; max-height=80%;"></img></p>

7、[pika](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Qihoo360/pika)：一个企业级开源的可持久化的大容量（百G）redis 存储服务。兼容 redis 的绝大部分接口，解决 redis 由于存储数据量巨大而导致内存不够用的容量瓶颈。并且可以像 redis 一样，通过 slaveof 命令进行主从备份，支持全同步和部分同步

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
8、[pg_flame](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mgartner/pg_flame)：Postgres 数据库性能分析工具，把 `EXPLAIN ANALYZE` 结果通过火焰图展示

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/pg_flame.png' style="max-width:80%; max-height=80%;"></img></p>

9、[goproxy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/goproxyio/goproxy)：Go 模块安装代理工具。还在因为安装 Go 项目依赖失败而抓耳挠腮吗？快试试这个项目吧

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/goproxy.png' style="max-width:80%; max-height=80%;"></img></p>

10、[gods](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/emirpasic/gods)：简单易用的 Go 语言各种数据结构和算法，并封装成了一个库，开箱即食。示例代码：
```go
type Stack interface {
	Push(value interface{})
	Pop() (value interface{}, ok bool)
	Peek() (value interface{}, ok bool)

	containers.Container
	// Empty() bool
	// Size() int
	// Clear()
	// Values() []interface{}
}
```

11、[gowp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xxjwxc/gowp)：Go 高性能异步并发线程池。接口调用简单、支持错误返回、无论排队多少任务，都不会阻止提交任务。可用于控制并发访问、并发执行。示例代码：
```go
package main

import (
	"fmt"
	"time"

	"github.com/xxjwxc/gowp/workpool"
)

func main() {
	wp := workpool.New(10)             //设置最大线程数
	for i := 0; i < 20; i++ { //开启20个请求
		ii := i
		wp.Do(func() error {
			for j := 0; j < 10; j++ { //每次打印0-10的值
				time.Sleep(1 * time.Second)
			}
			return nil
		})
	}

	wp.Wait()
	fmt.Println("down")
}
```

12、[gf](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gogf/gf)：一款高性能、功能丰富的 Go Web 框架。特点：
- 模块化、松耦合设计
- 模块丰富，开箱即用
- 简便及可维护性为宗旨
- 详尽的开发文档及示例
- 完善的本地中文化支持
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/gf.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
13、[SnowJena](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ystcode/SnowJena)：基于令牌桶算法实现的分布式无锁限流框架。简单易用的 API，开箱即用、支持熔断降级、动态配置规则、可视化监控等功能。示例代码：
```java
public class AppTest {
    Logger logger = LoggerFactory.getLogger(getClass());
    /**
     * 本地限流
     */
    @Test
    public void test1() {
        // 1.配置规则
        RateLimiterRule rateLimiterRule = new RateLimiterRuleBuilder()
                .setLimit(1)
                .setPeriod(1)
                .setUnit(TimeUnit.SECONDS) //每秒令牌数为1
                .build();
        // 2.工厂模式生产限流器
        RateLimiter limiter = RateLimiterFactory.of(rateLimiterRule);
        // 3.使用
        while (true) {
            if (limiter.tryAcquire()) {
                logger.info("ok");
            }
        }
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/SnowJena.jpeg' style="max-width:80%; max-height=80%;"></img></p>

14、[holer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wisdom-projects/holer)：一个将局域网中的应用映射到公网访问的端口映射软件，支持转发基于 TCP 协议的报文。内网穿透工具，包含 Web 后台管理系统。用到的技术如下：
- 服务端采用 SpringBoot 和 Netty 实现
- 客户端采用 Java Netty 和 Go 语言实现

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/holer.png' style="max-width:80%; max-height=80%;"></img></p>

15、[miaosha](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/qiurunze123/miaosha)：一款秒杀系统设计与实现。高并发大流量的秒杀是面试常见问题，该项目不仅有具体问题的解决思路，还有具体代码实现和示例 demo，全部理解、学习后相信秒杀问题再也拦不住你啦

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/miaosha.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
16、[postwoman](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/liyasthomas/postwoman)：一款基于 Node.js 的免费开源、便捷美观的 API 调试工具。它是调试接口的利器，能够尽快的发现问题提高开发效率。相信体会过 Postman 的同学，看到这个项目的名字就已经跃跃欲试了

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/postwoman.png' style="max-width:80%; max-height=80%;"></img></p>

17、[react-text-loop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/braposo/react-text-loop)：实现文字循环展示的 React 组件

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/react-text-loop.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[formily](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alibaba/formily)：一款面向企业级复杂场景的高性能表单解决方案。特性：
- 🚀 高性能，字段分布式渲染，大大减轻 React 渲染压力
- 💡 支持 Ant Design/Fusion Next 组件体系
- 🎨 JSX 标签化写法/JSON Schema 数据驱动方案无缝迁移过渡
- 🏅 副作用逻辑独立管理，涵盖各种复杂联动校验逻辑
- 🌯 支持各种表单复杂布局方案

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/uform.png' style="max-width:80%; max-height=80%;"></img></p>

19、[rc-bullets](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zerosoul/rc-bullets)：基于 CSS3 Animation 使用 React 构建的弹幕组件。[演示地址](http://zerosoul.github.io/rc-bullets)，支持功能：
- 管理弹幕：暂停、隐藏、清屏等
- 设置弹幕：速度、循环次数、延迟播放、自定义动画类型等

```javascript
import React, { useEffect, useState } from 'react';
import BulletScreen, { StyledBullet } from 'rc-bullets';

const headUrl='https://zerosoul.github.io/rc-bullets/assets/img/heads/girl.jpg';
export default function Demo() {
  // 弹幕屏幕
  const [screen, setScreen] = useState(null);
  // 弹幕内容
  const [bullet, setBullet] = useState('');
  useEffect(() => {
    // 给页面中某个元素初始化弹幕屏幕，一般为一个大区块
    let s = new BulletScreen('.screen');
    // or
    // let s=new BulletScreen(document.querySelector('.screen));
    setScreen(s);
  }, []);
  // 弹幕内容输入事件处理
  const handleChange = ({ target: { value } }) => {
    setBullet(value);
  };
  // 发送弹幕
  const handleSend = () => {
    if (bullet) {
      // push 纯文本
      screen.push(bullet);
      // or 使用 StyledBullet

      screen.push(
        <StyledBullet
          head={headUrl}
          msg={bullet}
        />
      );
      // or 还可以这样使用，效果等同使用 StyledBullet 组件
      screen.push({msg:bullet,head:headUrl,color:"#eee" bgColor:"rgba(2,2,2,.3)"})
    }
  };
  return (
    <main>
      <div className="screen" style={{ width: '100vw', height: '80vh' }}></div>
      <input value={bullet} onChange={handleChange} />
      <button onClick={handleSend}>发送</button>
    </main>
  );
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/rc-bullets.gif' style="max-width:80%; max-height=80%;"></img></p>

20、[react-loading](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sixiaodong123/react-loading)：一款轻量、开箱即用并且支持按需加载的 React 动画组件库。示例代码：
```javascript
import React from 'react';
import { DisappearedLoading } from 'react-loadingg';
const Container = () => <DisappearedLoading ></DisappearedLoading>;
export default Container;  
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/react-loading.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Kotlin 项目
21、[SketchyComponent](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/m-zylab/SketchyComponent)：一款 Android 上的手绘风格组件库。该库提供了一些基础图形和 icon，以及便捷的自定义能力。之前介绍过手绘风格的图表库大家很喜欢，这回是 Android 组件库不知道对不对大家的胃口。示例代码：
```java
// 1. 创建 Sketchy 图形
val skSquareDrawable = SkSquareDrawable().apply {
    // 2. 设置属性
    fillColor = resources.getColor(android.R.color.holo_orange_dark)
}
// 3. 给 View 设置背景
text.background = skSquareDrawable
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/SketchyComponent.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
22、[memory_profiler](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pythonprofilers/memory_profiler)：Python 程序内存占用分析工具。示例代码：
```python
# 采用装饰器的方式引用，不影响现有代码
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()

# 运行命令：python -m memory_profiler example.py
# 输出：
Line #    Mem usage  Increment   Line Contents
==============================================
     3                           @profile
     4      5.97 MB    0.00 MB   def my_func():
     5     13.61 MB    7.64 MB       a = [1] * (10 ** 6)
     6    166.20 MB  152.59 MB       b = [2] * (2 * 10 ** 7)
     7     13.61 MB -152.59 MB       del b
     8     13.61 MB    0.00 MB       return a
```

23、[PySimpleGUI](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/PySimpleGUI/PySimpleGUI)：Python GUI 编程库，它是将 tkinter、Qt、Remi、WxPython 封装成更人性化的接口。示例代码和效果如下：
```python
import PySimpleGUI as sg

sg.theme('DarkAmber')	# 设置主题颜色
# 界面内包含的东西
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# 创建窗口
window = sg.Window('Window Title', layout)
# 监听事件
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# 用户点击取消按钮事件
        break
    print('You entered ', values[0])

window.close()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/PySimpleGUI.png' style="max-width:80%; max-height=80%;"></img></p>

24、[mitmproxy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mitmproxy/mitmproxy)：基于 Python 语言开发的抓包工具。支持命令行、Web 平台的形式展示抓包结果，还能通过 Python 引用库来拦截、控制响应和请求。下图展示为命令行使用界面（类 vim 操作）

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/mitmproxy.png' style="max-width:80%; max-height=80%;"></img></p>

25、[PythonPlantsVsZombies](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/marblexu/PythonPlantsVsZombies)：Python 语言编写的植物大战僵尸。学习如何使用 Python 编写小游戏的极佳例子，运行步骤：
```
1. 需要 Python 3
2. 安装依赖库：pip install pygame
3. python main.py
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/PythonPlantsVsZombies.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
26、[pghero](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ankane/pghero)：Postgres 性能监控服务。让你对 pg 数据库的性能了如指掌

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/pghero.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
27、[clean-code-javascript](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ryanmcdermott/clean-code-javascript)：《Clean Code JavaScript》（JavaScript 代码整洁之道），这是根据《代码整洁之道》作者多年经验整理的 JS 代码优化建议，但也仅仅只是一份建议。[中文](https://github.com/alivebao/clean-code-js)

28、[wenyan](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wenyan-lang/wenyan)：文言文编程语言。文言文语法，可以编译成 JavaScript、Python 或者 Ruby，你见过用文言文编写程序吗？快来试试吧。[在线尝试](http://wenyan-lang.lingdong.works/ide.html)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/wenyan-lang.png' style="max-width:80%; max-height=80%;"></img></p>

29、[short_url](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Youthink/short_url)：Elixir 语言开发的支持自定义短码的短链接服务。新手可以参考该项目源码和[原理解析](https://hufangyun.com/2017/short-url/)，理解、实现短链接服务的同时，体验用 Elixir 语言开发一个 Web 服务。[在线尝试](https://fearless-trustworthy-aidi.gigalixirapp.com/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/short_url.png' style="max-width:80%; max-height=80%;"></img></p>

30、[pytest-chinese-doc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/luizyao/pytest-chinese-doc)：pytest 自动化测试框架的官方文档（5.1.3 版本）的中文翻译。但不仅仅是简单的翻译：
- 更多的示例：所有的示例代码都在 docs 目录下，以章节划分，尽量覆盖每个知识点
- 更多的拓展阅读：添加了学习时所查阅的资料、阅读的源码等，也是作者学习和思考的历程

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
31、[machine-learning-systems-design](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chiphuyen/machine-learning-systems-design)：一本关于机器学习系统设计的小册子附有练习题

32、[front-end-handbook-2019](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FrontendMasters/front-end-handbook-2019)：《Front-End Developer Handbook 2019》（前端开发者手册 2019 版）。该书适合任何阶段的人用来了解前端开发实践的指南，它概述和讨论了前端工程的实践：如何学习前端、在 2019 年进行前端实践时应该使用哪些工具。[在线阅读](https://frontendmasters.com/books/front-end-handbook/2019/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
33、[SSD-Pytorch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yatengLG/SSD-Pytorch)：完整的目标检测项目。结构简洁明了，中文注释。适宜新手入门、目标检测任务参考，甚至直接基于本项目实现目标检测任务。示例代码：
```python
# 实例化模型：模型的具体各种参数在 Config 文件中进行配置
net = SSD(cfg)
# 将模型移动到 GPU 上，cfg.DEVICE.MAINDEVICE 定义了模型所使用的主 GPU
# 模型的参数更新会在主 GPU 上进行
net.to(cfg.DEVICE.MAINDEVICE)

# 初始化训练器：训练器参数已通过 cfg 进行配置；也可传入参数进行配置（但不建议）
trainer = Trainer(cfg, max_iter=None, batch_size=None, 
                  train_devices=None, model_save_step=None, 
                  model_save_root=None, vis = None, vis_step=None)
# 训练器开始：在数据集上训练模型
trainer(net, train_dataset)
```

34、[AIDungeon](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AIDungeon/AIDungeon)：一个基于机器学习的地下城文字游戏。此项目介绍了如何使用机器学习构建一个游戏，代码简单清晰适合 AI 爱好者深入研究

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/AIDungeon.png' style="max-width:80%; max-height=80%;"></img></p>

35、[face_recognition](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ageitgey/face_recognition)：上手快速、简单易用的人脸识别库。该库使用 dlib 顶尖的深度学习人脸识别技术构建，在户外脸部检测数据库基准（Labeled Faces in the Wild benchmark）上的准确率高达 99.38%。同时提供了一个简单的面部识别命令行工具，允许您对来自命令行的图像文件夹进行面部识别。完整的开发文档和应用案例，并且兼容树莓派系统（对配置要求低），对于初学者来说可以通过这个项目感受人脸识别或机器学习带来的乐趣。示例代码：
```python
# 定位图片中的所有人脸：
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)

# 识别人脸关键点，包括眼睛、鼻子、嘴和下巴
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/img/face_recognition.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/44/HelloGitHub44.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/46/HelloGitHub46.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
