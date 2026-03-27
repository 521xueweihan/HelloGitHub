# HelloGitHub Vol.28
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C#
1、[choco](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chocolatey/choco)：类似 yum、apt-get、brew 的 Windows 包、软件管理、自动安装工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/28647218.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++
2、[cpp-cheat-sheet](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gibsjose/cpp-cheat-sheet)：能够帮你通过 Google 和 NASA 面试的 C++ 数据结构和算法的 cheat sheet（英文）


3、[taskflow](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/taskflow/taskflow)：一个 C++ 头文件库，让你以简单的几行代码就可以实现高效的并发。示例代码如下：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/130068982.gif' style="max-width:80%; max-height=80%;"></img></p>

### CSS
4、[pure](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pure-css/pure)：雅虎公司出品的一组轻量级、响应式纯 CSS 模块，适用于任何 Web 项目。本网站就是采用 Pure.css 模版构建，[中文文档](https://www.purecss.cn/)


### Go
5、[go-cloud](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google/go-cloud)：还在为兼容不同的云平台 SDK 而烦恼吗？go-cloud 通过封装不同云平台的接口，向用户提供统一的 API。例如：阿里云和腾讯云的存储桶 API 不一样，但是通过 go-cloud 的封装，可以使用统一的 API 调用


6、[go-fundamental-programming](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/unknwon/go-fundamental-programming)：无闻出品的《Go 编程基础》教程


7、[go-mysql](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/go-mysql-org/go-mysql)：监听 MySQL binlog 的库，可以用来把主库 MySQL 的变化同步到 Redis、elasticsearch 等。同时提供了一个类似阿里 canal 的工具库，监听并解析 binlog 变化。让管理数据和了解数据状态变得更加轻松


8、[night](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/talkgo/night)：Go 夜读，该项目每周四晚上更新 Go 源码阅读以及线下技术讨论。难得的中文 Golang 源码解析，包含文档和YouTube 视频，干货满满


9、[xinge-api-Golang](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xingePush/xinge-api-Golang)：腾讯信鸽 push v3 版的 Golang SDK。支持函数式配置项、标签推送、全平台推送、批量推送等


### Java
10、[Auto.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/clearw5/Auto.js)：不需要 ROOT 权限的类似按键精灵的自动操作软件，可以实现自动点击、滑动、输入文字、打开应用等。Auto.js 的大部分用户用它来点赞、签到、刷游戏


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/80171078.png' style="max-width:80%; max-height=80%;"></img></p>

11、[MTransition](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/HJ-Money/MTransition)：一个 Android 的 Activity 切换动画库。该库可以用少量代码实现一些复杂的、自定义的 Activity 切换动画


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/138117119.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[vjtools](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vipshop/vjtools)：唯品会的 Java 技术干货分享


### JavaScript
13、[DesktopNaotu](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NaoTu/DesktopNaotu)：桌面版脑图是基于百度脑图的本地化版本，帮助你在没有互联网环境的情况下，依然可以使用脑图工具。开箱即用，跨平台支持 Windows/Linux/Mac OS。桌面版思维工具，目前 Xmind 使用很多，但是需要收费，对于不常用，要求没有严格可以考虑此项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/73137241.png' style="max-width:80%; max-height=80%;"></img></p>

14、[G6](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/antvis/G6)：蚂蚁金服出品的关系数据可视化引擎，开发者可以基于 G6 拓展出属于自己的图分析应用或者图编辑器应用。[官方文档](https://antv.alipay.com/zh-cn/index.html)，示例代码：
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


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/81810486.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[taro](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NervJS/taro)：一套 React 语法规范的多端开发解决方案。我们可以只书写一套代码，再通过 Taro 的编译工具，将源代码分别编译出可以在不同端（微信小程序、H5、React-Native 等）运行的代码。已经投入到了京东生产环境使用，示例代码如下：
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


16、[Web-Notes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wx-chevalier/Web-Notes)：现代 Web 开发导论，内容大纲如下： 
- 基础篇
- 进阶篇
- 架构优化篇
- React 篇
- Vue 篇


### Kotlin
17、[kotlin-in-chinese](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/huanglizhuo/kotlin-in-chinese)：Kotlin 官方文档翻译项目


### Python
18、[scylla](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/MikeChongCan/scylla)：一款高质量的免费代理 IP 池工具，仅支持 Python 3.6。[中文文档](https://scylla.wildcat.io/zh/latest/)，特性如下：
- 自动化的代理 IP 爬取与验证
- 易用的 JSON API
- 简单但美观的 web 用户界面，基于 TypeScript 和 React（例如，代理的地理分布）
- 最少仅用一行代码即可与 Scrapy 和 requests 进行集成
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/128911431.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
19、[Best-App](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hzlzh/Best-App)：苹果系统下的优秀软件、硬件、技巧、周边设备的集合


20、[CS-Interview-Knowledge-Map](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/InterviewMap/CS-Interview-Knowledge-Map)：这是一份制作精良、系统的面试图谱。内容包括：前端、计算机网络、算法、数据结构等方面。相信认真学习完这份资料，你会找到自己心仪的工作。[在线阅读](https://yuchengkai.cn/docs/zh/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/125791597.png' style="max-width:80%; max-height=80%;"></img></p>

21、[follow-me-install-kubernetes-cluster](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/opsnull/follow-me-install-kubernetes-cluster)：部署 kubernetes 集群教程。该教程介绍使用二进制部署最新 kubernetes 集群的所有步骤，而不是使用 kubeadm 等自动化方式来部署集群。这样有助于理解系统各组件的交互原理，进而能够快速定位、解决实际中遇到的问题


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/87710748.png' style="max-width:80%; max-height=80%;"></img></p>

22、[spark_study](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shijinkui/spark_study)：Spark 源码阅读笔记


### Book
23、[progit2](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/progit/progit2)：《Pro Git 第二版》[在线中文阅读](https://git-scm.com/book/zh/v2)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/28/15400220.png' style="max-width:80%; max-height=80%;"></img></p>

24、[The-Flask-Mega-Tutorial-zh](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh)：2017 年新版《The Flask Mega-Tutorial 教程》（狗书）中文翻译版




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub27.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub29.md">『Next』</a>
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
    </tr>
  </thead>
</table>


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
