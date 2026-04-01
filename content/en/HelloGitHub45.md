# HelloGitHub Vol.45
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
1、[smartdns](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pymumu/smartdns)：一个运行在本地的 DNS 服务器。能够提高网络访问速度等诸多妙用，架构图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/130578889.png' style="max-width:80%; max-height=80%;"></img></p>

2、[xmake](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xmake-io/xmake)：一个基于 Lua 的轻量级跨平台自动构建工具。支持在各种主流平台上构建项目，主要用于解决 C/C++ 项目的跨平台构建，同时支持与其他语言的混合编译。工程配置语法简单易读，对初学者友好、上手方便
```bash
add_requires("libuv master", "ffmpeg", "zlib 1.20.*", "tbox >1.6.1")
target("test")
    set_kind("shared")
    add_files("src/*.c")
    add_packages("libuv", "ffmpeg", "tbox", "zlib")
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/34431834.png' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[Blog.Core](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/anjoy8/Blog.Core)：基于 ASP.NET Core 和 Vue 从零开始搭建前后端分离项目教程+实战项目。该项目从 .NET Core 基础讲起，内容完整、系统，对初学者和有一定基础的小伙伴都有借鉴和学习的价值


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/145101484.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Terminal.Gui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gui-cs/Terminal.Gui)：支持 Windows 和 Linux/Unix 的 .NET 终端 UI 工具库。方便实现终端 GUI 工具，并且可以实现终端中用鼠标啦


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/113807330.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
5、[pikiwidb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/OpenAtomFoundation/pikiwidb)：一个企业级开源的可持久化的大容量（百G）redis 存储服务。兼容 redis 的绝大部分接口，解决 redis 由于存储数据量巨大而导致内存不够用的容量瓶颈。并且可以像 redis 一样，通过 slaveof 命令进行主从备份，支持全同步和部分同步


6、[ThreadPool](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/progschj/ThreadPool)：一个简单的 C++11 线程池实现，代码加起来不到 100 行。示例代码：
```c++
// create thread pool with 4 worker threads
ThreadPool pool(4);

// enqueue and store future
auto result = pool.enqueue([](int answer) { return answer; }, 42);

// get result from future
std::cout << result.get() << std::endl;
```


7、[xournalpp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xournalpp/xournalpp)：一款支持 PDF 手写注释的笔记软件，支持 Linux、Windows、macOS 平台。看书的时候喜欢标注、做笔记，那这款工具肯定适合你。[下载地址](https://github.com/xournalpp/xournalpp/releases)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/11986447.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
8、[gf](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gogf/gf)：一款高性能、功能丰富的 Go Web 框架。特点：
- 模块化、松耦合设计
- 模块丰富，开箱即用
- 简便及可维护性为宗旨
- 详尽的开发文档及示例
- 完善的本地中文化支持
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/95761244.png' style="max-width:80%; max-height=80%;"></img></p>

9、[gods](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/emirpasic/gods)：简单易用的 Go 语言各种数据结构和算法，并封装成了一个库，开箱即食。示例代码：
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


10、[goproxy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/goproxyio/goproxy)：Go 模块安装代理工具。还在因为安装 Go 项目依赖失败而抓耳挠腮吗？快试试这个项目吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/146863879.png' style="max-width:80%; max-height=80%;"></img></p>

11、[gowp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xxjwxc/gowp)：Go 高性能异步并发线程池。接口调用简单、支持错误返回、无论排队多少任务，都不会阻止提交任务。可用于控制并发访问、并发执行。示例代码：
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


12、[pg_flame](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mgartner/pg_flame)：Postgres 数据库性能分析工具，把 `EXPLAIN ANALYZE` 结果通过火焰图展示


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/215655521.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
13、[SnowJena](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/onblog/SnowJena)：基于令牌桶算法实现的分布式无锁限流框架。简单易用的 API，开箱即用、支持熔断降级、动态配置规则、可视化监控等功能。示例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/181322928.jpeg' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
14、[formily](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alibaba/formily)：一款面向企业级复杂场景的高性能表单解决方案。特性：
- 🚀 高性能，字段分布式渲染，大大减轻 React 渲染压力
- 💡 支持 Ant Design/Fusion Next 组件体系
- 🎨 JSX 标签化写法/JSON Schema 数据驱动方案无缝迁移过渡
- 🏅 副作用逻辑独立管理，涵盖各种复杂联动校验逻辑
- 🌯 支持各种表单复杂布局方案


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/164768889.png' style="max-width:80%; max-height=80%;"></img></p>

15、[hoppscotch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hoppscotch/hoppscotch)：一款基于 Node.js 的免费开源、便捷美观的 API 调试工具。它是调试接口的利器，能够尽快的发现问题提高开发效率。相信体会过 Postman 的同学，看到这个项目的名字就已经跃跃欲试了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/203587744.png' style="max-width:80%; max-height=80%;"></img></p>

16、[rc-bullets](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zerosoul/rc-bullets)：基于 CSS3 Animation 使用 React 构建的弹幕组件。[演示地址](http://zerosoul.github.io/rc-bullets)，支持功能：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/223140010.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[react-loading](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Summer-andy/react-loading)：一款轻量、开箱即用并且支持按需加载的 React 动画组件库。示例代码：
```javascript
import React from 'react';
import { DisappearedLoading } from 'react-loadingg';
const Container = () => <DisappearedLoading ></DisappearedLoading>;
export default Container;  
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/219778203.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[react-text-loop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/braposo/react-text-loop)：实现文字循环展示的 React 组件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/85611345.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
19、[SketchyComponent](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/5A59/SketchyComponent)：一款 Android 上的手绘风格组件库。该库提供了一些基础图形和 icon，以及便捷的自定义能力。之前介绍过手绘风格的图表库大家很喜欢，这回是 Android 组件库不知道对不对大家的胃口。示例代码：
```java
// 1. 创建 Sketchy 图形
val skSquareDrawable = SkSquareDrawable().apply {
    // 2. 设置属性
    fillColor = resources.getColor(android.R.color.holo_orange_dark)
}
// 3. 给 View 设置背景
text.background = skSquareDrawable
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/227990983.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
20、[memory_profiler](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pythonprofilers/memory_profiler)：Python 程序内存占用分析工具。示例代码：
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


21、[mitmproxy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mitmproxy/mitmproxy)：基于 Python 语言开发的抓包工具。支持命令行、Web 平台的形式展示抓包结果，还能通过 Python 引用库来拦截、控制响应和请求。下图展示为命令行使用界面（类 vim 操作）


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/519832.png' style="max-width:80%; max-height=80%;"></img></p>

22、[PySimpleGUI](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PySimpleGUI/PySimpleGUI)：Python GUI 编程库，它是将 tkinter、Qt、Remi、WxPython 封装成更人性化的接口。示例代码和效果如下：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/140614233.png' style="max-width:80%; max-height=80%;"></img></p>

23、[PythonPlantsVsZombies](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/marblexu/PythonPlantsVsZombies)：Python 语言编写的植物大战僵尸。学习如何使用 Python 编写小游戏的极佳例子，运行步骤：
```
1. 需要 Python 3
2. 安装依赖库：pip install pygame
3. python main.py
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/204939699.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby
24、[pghero](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ankane/pghero)：Postgres 性能监控服务。让你对 pg 数据库的性能了如指掌


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/22059578.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
25、[AIDungeon](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/latitudegames/AIDungeon)：一个基于机器学习的地下城文字游戏。此项目介绍了如何使用机器学习构建一个游戏，代码简单清晰适合 AI 爱好者深入研究


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/179196443.png' style="max-width:80%; max-height=80%;"></img></p>

26、[face_recognition](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ageitgey/face_recognition)：上手快速、简单易用的人脸识别库。该库使用 dlib 顶尖的深度学习人脸识别技术构建，在户外脸部检测数据库基准（Labeled Faces in the Wild benchmark）上的准确率高达 99.38%。同时提供了一个简单的面部识别命令行工具，允许您对来自命令行的图像文件夹进行面部识别。完整的开发文档和应用案例，并且兼容树莓派系统（对配置要求低），对于初学者来说可以通过这个项目感受人脸识别或机器学习带来的乐趣。示例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/83844720.png' style="max-width:80%; max-height=80%;"></img></p>

27、[SSD-Pytorch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yatengLG/SSD-Pytorch)：完整的目标检测项目。结构简洁明了，中文注释。适宜新手入门、目标检测任务参考，甚至直接基于本项目实现目标检测任务。示例代码：
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


### Other
28、[clean-code-javascript](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ryanmcdermott/clean-code-javascript)：《Clean Code JavaScript》（JavaScript 代码整洁之道），这是根据《代码整洁之道》作者多年经验整理的 JS 代码优化建议，但也仅仅只是一份建议。[中文](https://github.com/alivebao/clean-code-js)


29、[pytest-chinese-doc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/luizyao/pytest-chinese-doc)：pytest 自动化测试框架的官方文档（5.1.3 版本）的中文翻译。但不仅仅是简单的翻译：
- 更多的示例：所有的示例代码都在 docs 目录下，以章节划分，尽量覆盖每个知识点
- 更多的拓展阅读：添加了学习时所查阅的资料、阅读的源码等，也是作者学习和思考的历程


30、[short_url](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/imfycc/short_url)：Elixir 语言开发的支持自定义短码的短链接服务。新手可以参考该项目源码和[原理解析](https://hufangyun.com/2017/short-url/)，理解、实现短链接服务的同时，体验用 Elixir 语言开发一个 Web 服务。[在线尝试](https://fearless-trustworthy-aidi.gigalixirapp.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/119340470.png' style="max-width:80%; max-height=80%;"></img></p>

31、[wenyan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wenyan-lang/wenyan)：文言文编程语言。文言文语法，可以编译成 JavaScript、Python 或者 Ruby，你见过用文言文编写程序吗？快来试试吧。[在线尝试](http://wenyan-lang.lingdong.works/ide.html)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/45/226726247.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
32、[front-end-handbook-2019](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/FrontendMasters/front-end-handbook-2019)：《Front-End Developer Handbook 2019》（前端开发者手册 2019 版）。该书适合任何阶段的人用来了解前端开发实践的指南，它概述和讨论了前端工程的实践：如何学习前端、在 2019 年进行前端实践时应该使用哪些工具。[在线阅读](https://frontendmasters.com/books/front-end-handbook/2019/)


33、[machine-learning-systems-design](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chiphuyen/machine-learning-systems-design)：一本关于机器学习系统设计的小册子附有练习题




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub44.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub46.md">『Next』</a>
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
