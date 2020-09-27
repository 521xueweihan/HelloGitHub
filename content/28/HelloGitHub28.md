# 《HelloGitHub》第 28 期
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
- [C# 项目](#C-项目)
- [C++ 项目](#C-项目-1)
- [CSS 项目](#CSS-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Kotlin 项目](#Kotlin-项目)
- [Python 项目](#Python-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

**Tips**：如果文中的图刷不出来，可以向我们[反馈](https://github.com/521xueweihan/HelloGitHub/issues/899)。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C# 项目
1、[choco](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chocolatey/choco)：类似 yum、apt-get、brew 的 Windows 包、软件管理、自动安装工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/choco.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
2、[cpp-cheat-sheet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gibsjose/cpp-cheat-sheet)：能够帮你通过 Google 和 NASA 面试的 C++ 数据结构和算法的 cheat sheet（英文）

3、[taskflow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/taskflow/taskflow)：一个 C++ 头文件库，让你以简单的几行代码就可以实现高效的并发。示例代码如下：
```c++
#include "taskflow.hpp"  // the only include you need

int main(){
  
  tf::Taskflow tf(std::thread::hardware_concurrency());

  auto [A, B, C, D] = tf.silent_emplace(
    [] () { std::cout << "TaskA\n"; },               //  the taskflow graph
    [] () { std::cout << "TaskB\n"; },               // 
    [] () { std::cout << "TaskC\n"; },               //          +---+          
    [] () { std::cout << "TaskD\n"; }                //    +---->| B |-----+   
  );                                                 //    |     +---+     |
                                                     //  +---+           +-v-+ 
  A.precede(B);  // B runs after A                   //  | A |           | D | 
  A.precede(C);  // C runs after A                   //  +---+           +-^-+ 
  B.precede(D);  // D runs after B                   //    |     +---+     |    
  C.precede(D);  // D runs after C                   //    +---->| C |-----+    
                                                     //          +---+          
  tf.wait_for_all();  // block until finished

  return 0;
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/cpp-taskflow.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
4、[pure](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pure-css/pure)：雅虎公司出品的一组轻量级、响应式纯 CSS 模块，适用于任何 Web 项目。本网站就是采用 Pure.css 模版构建，[中文文档](https://www.purecss.cn/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
5、[go-fundamental-programming](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/unknwon/go-fundamental-programming)：无闻出品的《Go 编程基础》教程

6、[go-cloud](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/go-cloud)：还在为兼容不同的云平台 SDK 而烦恼吗？go-cloud 通过封装不同云平台的接口，向用户提供统一的 API。例如：阿里云和腾讯云的存储桶 API 不一样，但是通过 go-cloud 的封装，可以使用统一的 API 调用

7、[night](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/talkgo/night)：Go 夜读，该项目每周四晚上更新 Go 源码阅读以及线下技术讨论。难得的中文 Golang 源码解析，包含文档和YouTube 视频，干货满满

8、[xinge-api-Golang](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xingePush/xinge-api-Golang)：腾讯信鸽 push v3 版的 Golang SDK。支持函数式配置项、标签推送、全平台推送、批量推送等

9、[go-mysql](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/siddontang/go-mysql)：监听 MySQL binlog 的库，可以用来把主库 MySQL 的变化同步到 Redis、elasticsearch 等。同时提供了一个类似阿里 canal 的工具库，监听并解析 binlog 变化。让管理数据和了解数据状态变得更加轻松

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
10、[vjtools](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vipshop/vjtools)：唯品会的 Java 技术干货分享

11、[Auto.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hyb1996/Auto.js)：不需要 ROOT 权限的类似按键精灵的自动操作软件，可以实现自动点击、滑动、输入文字、打开应用等。Auto.js 的大部分用户用它来点赞、签到、刷游戏

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/Auto-js-min.png' style="max-width:80%; max-height=80%;"></img></p>

12、[MTransition](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HJ-Money/MTransition)：一个 Android 的 Activity 切换动画库。该库可以用少量代码实现一些复杂的、自定义的 Activity 切换动画

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/MTransition.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
13、[Web-Series](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wx-chevalier/Web-Series)：现代 Web 开发导论，内容大纲如下： 
- 基础篇
- 进阶篇
- 架构优化篇
- React 篇
- Vue 篇

14、[taro](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NervJS/taro)：一套 React 语法规范的多端开发解决方案。我们可以只书写一套代码，再通过 Taro 的编译工具，将源代码分别编译出可以在不同端（微信小程序、H5、React-Native 等）运行的代码。已经投入到了京东生产环境使用，示例代码如下：
```javascript
import Taro, { Component } from '@tarojs/taro'
import { View, Button } from '@tarojs/components'

export default class Index extends Component {
    constructor () {
        super(...arguments)
        this.state = {
            title: '首页',
            list: [1, 2, 3]
        }
    }
    ....   // 代码来源官网示例
}
```

15、[G6](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/antvis/G6)：蚂蚁金服出品的关系数据可视化引擎，开发者可以基于 G6 拓展出属于自己的图分析应用或者图编辑器应用。[官方文档](https://antv.alipay.com/zh-cn/index.html)，示例代码：
```javascript
import G6 from '@antv/g6';

const data = {
  nodes: [{
    id: 'node1',
    x: 100,
    y: 200
  },{
    id: 'node2',
    x: 300,
    y: 200
  }],
  edges: [{
    target: 'node2',
    source: 'node1'
  }]
};
const graph = new G6.Graph({
  container: 'mountNode',
  width: 500,
  height: 500
});
graph.read(data);
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/g6.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[DesktopNaotu](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/NaoTu/DesktopNaotu)：桌面版脑图是基于百度脑图的本地化版本，帮助你在没有互联网环境的情况下，依然可以使用脑图工具。开箱即用，跨平台支持 Windows/Linux/Mac OS。桌面版思维工具，目前 Xmind 使用很多，但是需要收费，对于不常用，要求没有严格可以考虑此项目

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/DesktopNaotu-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Kotlin 项目
17、[kotlin-in-chinese](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/huanglizhuo/kotlin-in-chinese)：Kotlin 官方文档翻译项目

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
18、[scylla](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/imWildCat/scylla)：一款高质量的免费代理 IP 池工具，仅支持 Python 3.6。[中文文档](https://scylla.wildcat.io/zh/latest/)，特性如下：
- 自动化的代理 IP 爬取与验证
- 易用的 JSON API
- 简单但美观的 web 用户界面，基于 TypeScript 和 React（例如，代理的地理分布）
- 最少仅用一行代码即可与 Scrapy 和 requests 进行集成
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/scylla-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
19、[spark_study](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/shijinkui/spark_study)：Spark 源码阅读笔记

20、[CS-Interview-Knowledge-Map](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/InterviewMap/CS-Interview-Knowledge-Map)：这是一份制作精良、系统的面试图谱。内容包括：前端、计算机网络、算法、数据结构等方面。相信认真学习完这份资料，你会找到自己心仪的工作。[在线阅读](https://yuchengkai.cn/docs/zh/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/InterviewMap-min.png' style="max-width:80%; max-height=80%;"></img></p>

21、[Best-App](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hzlzh/Best-App)：苹果系统下的优秀软件、硬件、技巧、周边设备的集合

22、[follow-me-install-kubernetes-cluster](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/opsnull/follow-me-install-kubernetes-cluster)：部署 kubernetes 集群教程。该教程介绍使用二进制部署最新 kubernetes 集群的所有步骤，而不是使用 kubeadm 等自动化方式来部署集群。这样有助于理解系统各组件的交互原理，进而能够快速定位、解决实际中遇到的问题

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/follow-me-install-kubernetes-cluster-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
23、[The-Flask-Mega-Tutorial-zh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh)：2017 年新版《The Flask Mega-Tutorial 教程》（狗书）中文翻译版

24、[progit2](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/progit/progit2)：《Pro Git 第二版》[在线中文阅读](https://git-scm.com/book/zh/v2)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/img/progit2-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/27/HelloGitHub27.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/29/HelloGitHub29.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
