# 《HelloGitHub》第 06 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 目录

**Tips**：如果文中的图刷不出来，可以点击 [这里](https://hellogithub.com/periodical/volume/06/) 获取更好的阅读体验。

- [C# 项目](#C-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Python 项目](#Python-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C# 项目
1、[Cowboy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gaochundong/Cowboy)：一个基于 .NET/C# 实现的开源 WebSocket 网络库。[详细介绍](http://www.cnblogs.com/gaochundong/p/cowboy_websockets.html)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
2、[wukong](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/huichen/wukong)：悟空引擎是一个高度可定制的全文搜索引擎，[为什么要有悟空引擎](https://github.com/huichen/wukong/blob/master/docs/why_wukong.md)，[入门教程](https://github.com/huichen/wukong/blob/master/docs/codelab.md)，这个项目的搜索引擎原理如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/06/img/wukong-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
3、[moco](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dreamhead/moco)：开发过程中需要依赖一些接口，这些接口要么是搭建环境困难，要么是还没有实现，要么是交互比较复杂。这种情况下，使用 mock server 来 mock（模拟）这些接口，以便开发和测试能够正常进行。快速上手步骤：
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

4、[disconf](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/knightliao/disconf)：一个企业级的分布式配置管理平台，专注于各种分布式系统配置管理的通用平台，提供统一的配置管理服务。核心目标：一个 jar 包，到处运行。[在线文档](http://disconf.readthedocs.io/zh_CN/latest/index.html)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
5、[vue-sui-demo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/eteplus/vue-sui-demo)：这是一个用 Vue 和 SUI-Mobile 写的移动端 Demo，可以用来学习 Vue.js。[项目线上预览](https://eteplus.github.io/vue-sui-demo/)，效果图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/06/img/vue-sui-demo-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

6、[nodeppt](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ksky521/nodeppt)：这可能是迄今为止最好的网页版演示库，[在线演示](http://qdemo.sinaapp.com/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
7、[Young](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/shiyanhui/Young)：基于 Tornado 框架、MongoDB 数据库，写的功能丰富的社区项目。详细的[安装步骤](https://github.com/shiyanhui/Young/blob/master/README_CN.md)，适合学习如何创建社区类 Web App。[在线预览](http://beyoung.io/)，项目运行效果图：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/06/img/young-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

8、[textfilter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/observerss/textfilter)：基于某 1w 词敏感词库，用 Python 实现几种不同的过滤方式。**用于过滤敏感词的实用模块**，示例代码：
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

9、[amazing-qr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/x-hw/amazing-qr)：Python 写的生成动态、彩色、各式各样的二维码，详细的[中文文档](https://github.com/sylnsfar/qrcode/blob/master/README-cn.md)，通过 `qrcode` 生成的二维码样式如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/06/img/qrcode-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
10、[12306ForMac](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fancymax/12306ForMac)：非官方的 12306 购票，Mac OS 客户端


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/06/img/12306ForMac-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
11、[Apollo-11](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chrislgarry/Apollo-11)：阿波罗 11 号代码，[中文介绍](https://github.com/chrislgarry/Apollo-11/blob/master/README.zh_cn.md)

12、[weapp-ide-crack](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gavinkwoe/weapp-ide-crack)：【应用号】IDE + 破解 + Demo

13、[gvm](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/moovweb/gvm)：Go 版本管理工具，可以通过命令，无痛切换不同的 Go 版本，示例指令：
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

14、[LearningNotes](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/francistao/LearningNotes)：很全面的学习笔记，偏向 Android 和 Java

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub05.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub07.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1xF2ECA89A2592'>云主机 4 元/月</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>推荐项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有各种回馈粉丝活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/06/'>这里</a> 获取更好的阅读体验。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
