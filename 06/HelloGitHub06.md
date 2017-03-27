# 《HelloGitHub》第06期
>兴趣是最好的老师，[《HelloGitHub》](https://github.com/521xueweihan/HelloGitHub)就是帮你找到兴趣！

![](https://github.com/521xueweihan/HelloGitHub/blob/master/01/img/hello-github.jpg)

## 简介
最开始我只是想把自己在浏览 [GitHub](https://github.com/) 过程中，发现的有意思、高质量、容易上手的项目收集起来，这样便于以后查找和学习。后来一想，如果给这些 GitHub 项目都加上简单的效果图和一些通俗易懂的中文介绍。应该能够帮助到我这样的新手激发兴趣去参与、学习这些优秀、好玩的开源项目。

所以，我就做了一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 的人群的月刊，月刊的内容包括：**各种编程语言的项目**、**各种让生活变得更美好的工具**、**书籍、学习笔记、教程等**。这些项目都是非常容易上手，而且非常 Cool，主要是希望大家能动手用起来，加入到**开源社区**中。会编程的可以贡献代码，不会编程的可以反馈使用这些工具中的 Bug、帮着宣传你觉得优秀的项目、Star 项目⭐️。同时你将学习到更多编程知识、提高自己的编程技巧、发现自己的**兴趣**。

最后[《HelloGitHub》](https://github.com/521xueweihan/HelloGitHub)这个项目就诞生了！😁

---
>**以下为本期内容**｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub)｜每个月 28 号发布最新一期，首发在我的 [GitHub](https://github.com/521xueweihan) 上。

#### Python项目
1、[Young](https://github.com/shiyanhui/Young)：基于Tornado框架、MongoDB数据库，写的功能丰富的社区项目。详细的[安装步骤](https://github.com/shiyanhui/Young/blob/master/README_CN.md)，适合学习如何创建社区类web app。[在线预览](http://beyoung.io/)，项目运行效果图：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/young-show-min.png)

2、[textfilter](https://github.com/observerss/textfilter)：基于某1w词敏感词库，用Python实现几种不同的过滤方式。**用于过滤敏感词的实用模块**，示例代码：
```python
from filter import DFAFilter

gfw = DFAFilter()
gfw.parse("keywords")
print "待过滤：售假人民币 我操操操"
print "过滤后：", gfw.filter("售假人民币 我操操操", "*")

test_first_character()

# 运行结果
# 待过滤：售假人民币 我操操操
# 过滤后： 售假**币 ****
```

3、[qrcode](https://github.com/sylnsfar/qrcode)：Python写的生成动态、彩色、各式各样的二维码，详细的[中文文档](https://github.com/sylnsfar/qrcode/blob/master/README-cn.md)，通过`qrcode`生成的二维码样式如下：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/qrcode-show-min.png)

#### Go项目
4、[wukong](https://github.com/huichen/wukong)：悟空引擎，是一个高度可定制的全文搜索引擎，[为什么要有悟空引擎](https://github.com/huichen/wukong/blob/master/docs/why_wukong.md)，[入门教程](https://github.com/huichen/wukong/blob/master/docs/codelab.md)，这个项目的搜索引擎原理如下：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/wukong-show-min.png)

#### Java项目
5、[moco](https://github.com/dreamhead/moco)：开发过程中需要依赖一些接口，这些接口要么是搭建环境困难，要么是还没有实现，要么是交互比较复杂。这种情况下，使用mock server来mock（模拟）这些接口，以便开发和测试能够正常进行，*感谢推荐人：[QA_imp](https://home.cnblogs.com/u/bu1tcat/)*。快速上手步骤：
```
1. 下载 Moco：https://repo1.maven.org/maven2/com/github/dreamhead/moco-runner/0.11.0/moco-runner-0.11.0-standalone.jar

2. 写需要返回的reponse数据格式如下：
[
  {
    "response" :
      {
        "text" : "Hello, Moco"
      }
  }
]
(文件名：foo.json)

3.运行
java -jar moco-runner-<version>-standalone.jar http -p 12306 -c foo.json

4. 访问 http://localhost:12306，你将会看到 “Hello, Moco”
```

6、[disconf](https://github.com/knightliao/disconf)：**企业级开源项目disconf** 是一个分布式配置管理平台，专注于各种 *分布式系统配置管理* 的通用组件/通用平台, 提供统一的配置管理服务。核心目标：一个jar包，到处运行。[在线文档](http://disconf.readthedocs.io/zh_CN/latest/index.html)

#### C#项目
7、[Cowboy](https://github.com/gaochundong/Cowboy)：Cowboy.WebSockets 是一个基于 .NET/C# 实现的开源 WebSocket 网络库，[详细介绍](http://www.cnblogs.com/gaochundong/p/cowboy_websockets.html)

#### Javascript项目
8、[vue-sui-demo](https://github.com/eteplus/vue-sui-demo)：这是一个用vue 和 SUI-Mobile 写的移动端demo，可以用来学习vue.js库。[项目线上预览](http://eteplus.github.io/vue-sui-demo)，效果图如下：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/vue-sui-demo-show-min.png)

9、[nodePPT](https://github.com/ksky521/nodePPT)：这可能是迄今为止最好的网页版演示库，[在线演示](http://qdemo.sinaapp.com/)

#### Objective-C、Swift项目
10、[12306ForMac](https://github.com/fancymax/12306ForMac)：非官方的12306 mac os客户端

![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/12306ForMac-show-min.png)


#### 其它
11、[Apollo-11](https://github.com/chrislgarry/Apollo-11)：阿波罗11号代码，[中文介绍](https://github.com/chrislgarry/Apollo-11/blob/master/README.zh_cn.md)

12、[weapp-ide-crack](https://github.com/gavinkwoe/weapp-ide-crack)：【应用号】IDE + 破解 + Demo

13、[gvm](https://github.com/moovweb/gvm)：Go版本管理工具，可以通过命令，无痛切换不同的Go版本，示例指令：
```
1. 安装gvm：bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)

2. 根据提示，在shell配置中加入：source /PATH/.gvm/scripts/gvm

3. 以下为常用命令：
gvm install go1.4  ＃ 安装制定版本的GO
gvm use go1.4  ＃ 使用制定版本的GO

4. Mac下安装Go时如果出现错误，就安装依赖的库：
xcode-select --install
brew update
brew install mercurial

5. 我在使用中发现的问题：
安装Go时没有进度条
```

14、[hosts](https://github.com/racaljk/hosts)：最新可用的Google hosts文件。

15、[LearningNotes](https://github.com/GeniusVJR/LearningNotes)：很全面的学习笔记，偏向Android和Java

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
