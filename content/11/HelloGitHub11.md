# 《HelloGitHub》第 11 期
>兴趣是最好的老师，**HelloGitHub** 就是帮你找到兴趣！

![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg)

## 简介
分享 GitHub 上有趣、入门级的开源项目。

这是一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 人群的月刊，月刊的内容包括：**各种编程语言的项目**、**让生活变得更美好的工具**、**书籍、学习笔记、教程等**，这些开源项目大多都是非常容易上手，而且非常 Cool。主要是希望大家能动手用起来，加入到**开源社区**中。
- 会编程的可以贡献代码
- 不会编程的可以反馈使用这些工具中的 Bug
- 帮着宣传你觉得优秀的项目
- Star 项目⭐️

在浏览、参与这些项目的过程中，你将学习到**更多编程知识**、**提高编程技巧**、**找到编程的乐趣**。

🎉 最后 [HelloGitHub](https://hellogithub.com) 这个项目就诞生了 🎉

---
> **以下为本期内容**｜每个月 **28** 号发布最新一期｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub#往期回顾)

#### C 项目
1、[wrk](https://github.com/wg/wrk)：现代 HTTP 基准测试（实现对一类测试对象的某项性能指标进行定量的和可对比的测试）工具，使用示例：
```sh
# 输入命令
wrk -t12 -c400 -d30s http://127.0.0.1:8080/index.html

# 输出
Running 30s test @ http://127.0.0.1:8080/index.html
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   635.91us    0.89ms  12.92ms   93.69%
    Req/Sec    56.20k     8.07k   62.00k    86.54%
  22464657 requests in 30.00s, 17.76GB read
Requests/sec: 748868.53
Transfer/sec:    606.33MB
```

#### Go 项目
2、[negroni](https://github.com/urfave/negroni)：Negroni 是一个很地道的 Web 中间件，它不是一个框架，是为了方便使用 net/http 而设计的一个库而已。[中文介绍](https://github.com/urfave/negroni/blob/master/translations/README_zh_cn.md)

#### Java 项目
3、[WechatLuckyMoney](https://github.com/veryyoung/WechatLuckyMoney)：微信抢红包插件，基于 Xposed 框架，速度快得冷人发指。为避免过度拉仇恨，请谨慎使用（哈哈哈😄）。


![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/11/img/wechatluckymoney.gif)

4、[GitClub](https://github.com/TellH/GitClub)：GitClub 不仅仅是一个 GitHub 客户端，还是一个发现优秀 GitHub 开源项目的 App

5、[tale](https://github.com/otale/tale)：简洁、漂亮、轻量级、Java 博客，[在线预览](https://tale.biezhi.me/)。特性：
- 设计简洁，界面美观
- Markdown 文章发布
- 自定义文章链接
- 支持多主题
- 支持 Emoji 表情
- 支持网易云音乐播放
- 支持附件和数据库备份
- 部署简单，不依赖 Tomcat


![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/11/img/tale-show-min.png)

6、[jvm-mon](https://github.com/ajermakovics/jvm-mon)：命令行模式的 JVM 监控


![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/11/img/jvm-show-min.png)

#### JavaScript 项目
7、[react-tetris](https://github.com/chvin/react-tetris)：逼真的俄罗斯方块（非常逼真、强大！），详细的技术介绍，[在线试玩](https://chvin.github.io/react-tetris/?lan=zh)


![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/11/img/tetris.gif)

#### Python 项目
8、[sh](https://github.com/amoffat/sh)：sh 是一个成熟，用于替代 subprocess，它允许你调用任何程序，就像它是一个函数，支持 Python2.6 - 3.5

```python
from sh import ifconfig
print ifconfig("eth0")
```

9、[fastText.py](https://github.com/salestock/fastText.py)：fastText 简而言之，就是把文档中所有词通过 lookup table 变成向量，取平均后直接用线性分类器得到分类结果。[fastText 的实现](https://www.zybuluo.com/Wayne-Z/note/460881)

10、[mongoaudit](https://github.com/stampery/mongoaudit)：强大的 MongoDB 渗透测试工具，用于发掘 MongoDB 漏洞、并提出改善方法。
- 安装：`pip install mongoaudit`
- 运行：`python mongoaudit`

#### Swift 项目
11、[Swift30Projects](https://github.com/soapyigu/Swift30Projects)：30 个小型 Swift Apps，可以用来上手学习、练习移动开发。


![](https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/11/img/swift30projects-show-min.jpg)

#### 其它
12、[linux-command](https://github.com/jaywcjlove/linux-command)：Linux 命令大全搜索工具，内容包含 Linux 命令手册、详解、学习、搜集

13、[chinese-programmer-wrong-pronunciation](https://github.com/shimohq/chinese-programmer-wrong-pronunciation)：中国程序员容易发音错误的单词

14、[go-lang-cheat-sheet](https://github.com/a8m/go-lang-cheat-sheet)：（英文）Go 语法特性集合

#### 开源书籍
15、[book](https://github.com/qyuhen/book)：雨痕大神写的学习笔记

16、[nginx-book](https://github.com/taobao/nginx-book)：Nginx 开发从入门到精通——本书的作者为淘宝核心系统服务器平台组的成员

17、[real-world-haskell-cn](https://github.com/huangz1990/real-world-haskell-cn)：《Real World Haskell》中文翻译项目

18、[open-shell-book](https://github.com/tinyclub/open-shell-book)：《Shell 编程范例》，面向操作对象学 Shell！

19、[python-data-structure-cn](https://github.com/facert/python-data-structure-cn)：《Problem Solving with Algorithms and Data Structures using Python》中文版

20、[docker_practice](https://github.com/yeasy/docker_practice)：Dokcer 从入门到实践

21、[explore-flask](https://github.com/spacewander/explore-flask-zh)：[《explore flask》中文翻译](https://spacewander.github.io/explore-flask-zh/index.html)

22、[react-cookbook](https://github.com/shimohq/react-cookbook)：编写简洁漂亮，可维护的 React 应用

23、[rust-book-chinese](https://github.com/KaiserY/rust-book-chinese)：Rust 程序设计语言 中文版



---

## 换种方式阅读
- **网站：** https://hellogithub.com
- **GitBook：** https://gitbook.hellogithub.com

## 声明
如果你发现了好玩、有意义的开源项目 [点击这里](https://github.com/521xueweihan/HelloGitHub/issues/new) 分享你觉得有意思的项目。

**欢迎转载，请注明出处和作者，同时保留声明。**
