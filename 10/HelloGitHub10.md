#《HelloGitHub》第10期
>兴趣是最好的老师，[《HelloGitHub》](https://github.com/521xueweihan/HelloGitHub)就是帮你找到兴趣！

![](https://github.com/521xueweihan/HelloGitHub/blob/master/01/img/hello-github.jpg)

## 简介
最开始我只是想把自己在浏览 [GitHub](https://github.com/) 过程中，发现的有意思、高质量、容易上手的项目收集起来，这样便于以后查找和学习。后来一想，如果给这些 GitHub 项目都加上简单的效果图和一些通俗易懂的中文介绍。应该能够帮助到我这样的新手激发兴趣去参与、学习这些优秀、好玩的开源项目。

所以，我就做了一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 的人群的月刊，月刊的内容包括：**各种编程语言的项目**、**各种让生活变得更美好的工具**、**书籍、学习笔记、教程等**。这些项目都是非常容易上手，而且非常 Cool，主要是希望大家能动手用起来，加入到**开源社区**中。会编程的可以贡献代码，不会编程的可以反馈使用这些工具中的 Bug、帮着宣传你觉得优秀的项目、Star 项目⭐️。同时你将学习到更多编程知识、提高自己的编程技巧、发现自己的**兴趣**。

最后[《HelloGitHub》](https://github.com/521xueweihan/HelloGitHub)这个项目就诞生了！😁

---
>**以下为本期内容**｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub)｜每个月 28 号发布最新一期，首发在我的 [GitHub](https://github.com/521xueweihan) 上。

#### Python项目
1、[saythanks.io](https://github.com/kennethreitz/saythanks.io)：Kennethreitz 写的一个简单的网站（基于Flask），用于向开源项目作者发送感谢邮件的 Web App。该项目结构简单，可以用来学习大神是如何快速开发 Web 项目、方法、代码风格、开发常用库。而且该项目的意义也特别好：**感谢开源项目的作者**，愿开源社区越来越好，[网站地址](https://saythanks.io)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/10/img/thanks-show-min.png)

2、[locust](https://github.com/locustio/locust)：模拟用户行为的[负载测试](http://blog.csdn.net/kerryzhu/article/details/3515714)工具，包含友好的 Web 页面，如下图：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/10/img/locust-show-min.png)

3、[jumpserver](https://github.com/jumpserver/jumpserver)：Jumpserver 是一款由 python 编写开源的跳板机(是一类可作为跳板批量操作远程设备的网络设备)系统，实现了跳板机应有的功能。基于 ssh 协议来管理，客户端无需安装 agent 。支持常见 Linux 系统，效果如下：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/10/img/jumpserver-min.gif)

#### Go项目
4、[kingshard](https://github.com/flike/kingshard)：Kingshard 是一个由 Go 开发高性能 MySQL Proxy 项目，kingshard 在满足基本的读写分离的功能上，致力于简化 MySQL 分库分表操作；能够让 DBA 通过 kingshard 轻松平滑地实现 MySQL 数据库扩容。

5、[v2ray-core](https://github.com/v2ray/v2ray-core)：提供常用的代理软件模块，简化网络代理软件的开发。[什么是 V2Ray？](https://toutyrater.github.io/v2ray-guide-pages/)

#### PHP项目
6、[typecho](https://github.com/typecho/typecho)：PHP的一款博客程序，[官网](http://typecho.org/)，[文档](http://docs.typecho.org/doku.php)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/10/img/typecho-show-min.png)

#### Javascript项目
7、[iview](https://github.com/iview/iview)：iView 是一套基于 Vue.js 的开源 UI 组件库，主要服务于 PC 界面的中后台产品。特性：
- 高质量、功能丰富
- 友好的 API ，自由灵活地使用空间
- 事无巨细的文档
- 细致、漂亮的 UI
- 使用单文件的 Vue 组件化开发模式
- 基于 npm + webpack + babel 开发，支持 ES2015

8、[flv.js](https://github.com/Bilibili/flv.js)：使用纯 JavaScript 写的 HTML5 Flash 视频（flv）播放器，示例代码如下：
```javascript
<script src="flv.min.js"></script>
<video id="videoElement"></video>
<script>
    if (flvjs.isSupported()) {
        var videoElement = document.getElementById('videoElement');
        var flvPlayer = flvjs.createPlayer({
            type: 'flv',
            url: 'http://example.com/flv/video.flv'
        });
        flvPlayer.attachMediaElement(videoElement);
        flvPlayer.load();
        flvPlayer.play();
    }
</script>
```

9、[RAP](https://github.com/thx/RAP)：阿里妈妈MUX团队出品，企业级 Web 接口管理工具。RAP 通过 GUI 工具帮助 WEB 工程师更高效的管理接口文档，同时通过分析接口结构自动生成 Mock 数据、校验真实接口的正确性，使得接口开发更加规范、自动化。

![](https://github.com/521xueweihan/HelloGitHub/blob/master/10/img/rap-show-min.jpeg)

#### C#项目
10、[Wox](https://github.com/Wox-launcher/Wox)：Windows 上的 Alfred、Launchy，使用演示：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/10/img/wox-min.gif)

#### 机器学习
11、[MLAlgorithms](https://github.com/rushter/MLAlgorithms)：常见的机器学习算法，Python实现：
- [Deep learning (MLP, CNN, RNN, LSTM)](https://github.com/rushter/MLAlgorithms/tree/master/mla/neuralnet)
- [Linear regression, logistic regression](https://github.com/rushter/MLAlgorithms/blob/master/mla/linear_models.py)
- [Random Forests](https://github.com/rushter/MLAlgorithms/blob/master/mla/ensemble/random_forest.py)
- [Support vector machine (SVM) with kernels (Linear, Poly, RBF)](https://github.com/rushter/MLAlgorithms/tree/master/mla/svm)
- [K-Means](https://github.com/rushter/MLAlgorithms/blob/master/mla/kmeans.py)
- ...

#### Java项目
12、[RocketMQ](https://github.com/alibaba/RocketMQ)：RocketMQ 是阿里巴巴在 2012 年开源的第三代分布式消息中间件。
历年双 11，RocketMQ 都承担了阿里巴巴生产系统百分之百的消息流转，在核心交易链路有着稳定和出色的表现，今年双十一，更是创造了万亿级消息精准低延迟投递。

#### C++项目
13、[simhash](https://github.com/yanyiwu/simhash)：此项目用来对中文文档计算出对应的 simhash 值。 simhash 是谷歌用来进行文本去重的算法（[详见simhash算法原理及实现](http://yanyiwu.com/work/2014/01/30/simhash-shi-xian-xiang-jie.html)），现在广泛应用在文本处理中。特征：
- 使用 CppJieba 作为分词器和关键词抽取器
- 使用 jenkins 作为 hash 函数
- hpp 风格，所有源码都是 .hpp 文件里面，方便使用。 没有链接，就没有伤害。
- 本项目的副产品项目：simhash_server 提供了简单的 simhash HTTP 服务。

#### Objective-C项目
14、[sequelpro](https://github.com/sequelpro/sequelpro)：这是我到目前为止在 Mac 上发现最好用的 MySQL 管理工具。本人一直在使用，并且推荐给了我的小伙伴们，用过都说好😈～

![](https://github.com/521xueweihan/HelloGitHub/blob/master/10/img/sequelpro-show-min.png)

#### 其它
15、[IntelliJ-IDEA-Tutorial](https://github.com/judasn/IntelliJ-IDEA-Tutorial)：IntelliJ IDEA 简体中文专题教程

16、[redisbook](https://github.com/huangz1990/redisbook)：Redis 设计与实现（网络版）

17、[algorithm](https://github.com/qiwsir/algorithm)：老齐的算法教程

18、[Awesome_API](https://github.com/marktony/Awesome_API/blob/master/Chinese.md)：该页收集中国国内可用API

19、[Lee-VR-Source](https://github.com/GeekLiB/Lee-VR-Source)：VR 开发者必备资源汇总

20、[500 Lines or Less](https://github.com/aosabook/500lines)：（英文）用少于 500 行的 Python 代码，你可以写出什么东西？相信你看完这个项目，会学到很多（每个项目的作者都是业内大神写的）。[中文翻译版（未翻译完）](https://github.com/HT524/500LineorLess_CN)

---


## 声明
如果你发现了好玩、有意义的开源项目，[点击这里](https://github.com/521xueweihan/HelloGitHub/issues/new) 分享你觉得有意思的项目。

- 分享项目格式：项目名称——项目地址：项目描述(中文)，追求完美👉项目上手 Demo、有图有真相～

或许你分享的项目会让别人由衷的感慨：“原来还有这么有意思的项目！编程可以这么酷！”

**欢迎转载，请注明出处和作者，同时保留声明和联系方式。**

## 联系方式
- [削微寒](https://github.com/521xueweihan)

- [博客园](http://www.cnblogs.com/xueweihan/)

- [知乎专栏](https://zhuanlan.zhihu.com/hellogithub)
