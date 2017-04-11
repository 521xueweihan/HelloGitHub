# 《HelloGitHub》第 06 期
>兴趣是最好的老师，HelloGitHub 就是帮你找到兴趣！

![](https://github.com/521xueweihan/HelloGitHub/blob/master/01/img/hello-github.jpg)

## 简介
**分享、推荐 GitHub 上好玩、容易上手的项目，帮你找到编程的乐趣。**

🎉 然后 [HelloGitHub](http://hellogithub.com/) 这个项目就诞生了 🎉

---
｜**以下为本期内容**｜每个月 **28** 号发布最新一期｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub#往期回顾)｜

#### C# 项目

<details>

1、[Cowboy](https://github.com/gaochundong/Cowboy)：Cowboy.WebSockets 是一个基于 .NET/C# 实现的开源 WebSocket 网络库，[详细介绍](http://www.cnblogs.com/gaochundong/p/cowboy_websockets.html)

</details>

#### Go 项目

<details>

2、[wukong](https://github.com/huichen/wukong)：悟空引擎，是一个高度可定制的全文搜索引擎，[为什么要有悟空引擎](https://github.com/huichen/wukong/blob/master/docs/why_wukong.md)，[入门教程](https://github.com/huichen/wukong/blob/master/docs/codelab.md)，这个项目的搜索引擎原理如下：


![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/wukong-show-min.png)

</details>

#### Java 项目

<details>

3、[moco](https://github.com/dreamhead/moco)：开发过程中需要依赖一些接口，这些接口要么是搭建环境困难，要么是还没有实现，要么是交互比较复杂。这种情况下，使用 mock server 来 mock（模拟）这些接口，以便开发和测试能够正常进行，*感谢推荐人：[QA_imp](https://home.cnblogs.com/u/bu1tcat/)*。快速上手步骤：
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

4、[disconf](https://github.com/knightliao/disconf)：**企业级开源项目 Disconf** 是一个分布式配置管理平台，专注于各种 *分布式系统配置管理* 的通用组件／通用平台，提供统一的配置管理服务。核心目标：一个 jar 包，到处运行。[在线文档](http://disconf.readthedocs.io/zh_CN/latest/index.html)

</details>

#### JavaScript 项目

<details>

5、[vue-sui-demo](https://github.com/eteplus/vue-sui-demo)：这是一个用 Vue 和 SUI-Mobile 写的移动端 Demo，可以用来学习 Vue.js。[项目线上预览](http://blog.coderfun.com/vue-sui-demo/)，效果图如下：


![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/vue-sui-demo-show-min.png)

6、[nodePPT](https://github.com/ksky521/nodePPT)：这可能是迄今为止最好的网页版演示库，[在线演示](http://qdemo.sinaapp.com/)

</details>

#### Python 项目

<details>

7、[Young](https://github.com/shiyanhui/Young)：基于 Tornado 框架、MongoDB 数据库，写的功能丰富的社区项目。详细的[安装步骤](https://github.com/shiyanhui/Young/blob/master/README_CN.md)，适合学习如何创建社区类 Web App。[在线预览](http://beyoung.io/)，项目运行效果图：


![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/young-show-min.png)

8、[textfilter](https://github.com/observerss/textfilter)：基于某 1w 词敏感词库，用 Python 实现几种不同的过滤方式。**用于过滤敏感词的实用模块**，示例代码：
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

9、[qrcode](https://github.com/sylnsfar/qrcode)：Python 写的生成动态、彩色、各式各样的二维码，详细的[中文文档](https://github.com/sylnsfar/qrcode/blob/master/README-cn.md)，通过 `qrcode` 生成的二维码样式如下：


![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/qrcode-show-min.png)

</details>

#### Swift 项目

<details>

10、[12306ForMac](https://github.com/fancymax/12306ForMac)：非官方的 12306 购票，Mac OS 客户端


![](https://github.com/521xueweihan/HelloGitHub/blob/master/06/img/12306ForMac-show-min.png)

</details>

#### 其它

<details>

11、[Apollo-11](https://github.com/chrislgarry/Apollo-11)：阿波罗 11 号代码，[中文介绍](https://github.com/chrislgarry/Apollo-11/blob/master/README.zh_cn.md)

12、[weapp-ide-crack](https://github.com/gavinkwoe/weapp-ide-crack)：【应用号】IDE + 破解 + Demo

13、[gvm](https://github.com/moovweb/gvm)：Go 版本管理工具，可以通过命令，无痛切换不同的 Go 版本，示例指令：
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

14、[hosts](https://github.com/racaljk/hosts)：最新可用的 Google hosts 文件。

15、[LearningNotes](https://github.com/GeniusVJR/LearningNotes)：很全面的学习笔记，偏向 Android 和 Java

</details>



---

## 声明
如果你发现了好玩、有意义的开源项目，[点击这里](https://github.com/521xueweihan/HelloGitHub/issues/new) 分享你觉得有意思的项目。

- 分享项目格式：`项目名称——项目地址：项目描述(中文)，追求完美👉项目上手 demo、截图`

或许你分享的项目会让别人由衷的感慨：“原来还有这么有意思的项目！编程可以这么酷！”

**欢迎转载，请注明出处和作者，同时保留声明和联系方式。**

## 联系方式
- [GitHub](https://github.com/521xueweihan)

- [GitBook](https://gitbook.hellogithub.com/)

- [博客园](http://www.cnblogs.com/xueweihan/)

- [简书](http://www.jianshu.com/u/f04b57b6f433)

- [掘金](https://juejin.im/user/5677785f60b2298f122fe889)

- [知乎专栏](https://zhuanlan.zhihu.com/hellogithub)
