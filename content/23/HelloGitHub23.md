# 《HelloGitHub》第 23 期
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
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
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
1、[ffmpeg-libav-tutorial](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/leandromoreira/ffmpeg-libav-tutorial)：《笨方法学 FFmpeg libav》（英文）

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
2、[NiceHashMiner](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nicehash/NiceHashMiner)：一款可以自动帮你挖比特币的免费 App。[中文官网地址](https://miner.nicehash.com/)，经典版截图如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/23/img/NiceHashMinerLegacy-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
3、[WxJava](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Wechat-Group/WxJava)：开源、非官方、功能全面的微信开发 Java SDK，支持包括微信支付、开放平台、小程序、企业号和公众号等功能的开发。[示例 Demo 索引](https://github.com/Wechat-Group/weixin-java-tools/blob/master/demo.md)，以及详细的[开发文档](https://github.com/wechat-group/weixin-java-tools/wiki)

4、[CC](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/luckybilly/CC)：使用简单、功能丰富的 Android 组件化框架。适用于几乎所有的组件化开发需求，可进行组件层面的 AOP 编程。[项目 wiki](https://github.com/luckybilly/CC/wiki)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/23/img/cc.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[Geisha](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/RitterHou/Geisha)：用 Java 语言写的 Web MVC 框架。包含诸多语言特性并实现了 IOC 、通过注解设置 URL 映射的功能。入门实践项目，适合新手熟悉 Java 语法和了解 Web 框架的实现。示例代码如下：
```java
@Component
@RequestMapping("/person")
public class Hello {

    @RequestMapping("/info")
    public String hello(@Param("name") String name, @Param("age") String age) {
        return "hello " + name + ", your age is " + Integer.valueOf(age);
    }

}
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
6、[wiki](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Requarks/wiki)：NodeJS+Git+Markdown 实现轻松搭建 wiki。对于团队内部的知识分享是一个不错的选择。[在线预览](https://docs.requarks.io/wiki)

7、[prettier](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/prettier/prettier)：十分方便的代码格式化库。支持如：JavaScript、Flow、TypeScript、CSS、SCSS等编程语言。同时提供了编辑插件，在使用 vscode 开发 Vue 项目时候，使用此插件可以让代码更具有可读性
```javascript
/**
 * 格式化之前
 */
foo(reallyLongArg(), omgSoManyParameters(), IShouldRefactorThis(), isThereSeriouslyAnotherOne());

/**
 * 格式化之后
 */
foo(
  reallyLongArg(),
  omgSoManyParameters(),
  IShouldRefactorThis(),
  isThereSeriouslyAnotherOne()
);
```

8、[node-fetch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/node-fetch/node-fetch)：将 fetch 引入了 node 环境，配合了 node 强大的 http 模块。做到了在不同的 JS 环境中使用一致的API。fetch API 是代替 XMLHttpRequest 的一种全新的解决方案，其简化了 XHR 的复杂步骤，采用了 Promise。示例代码如下：
```javascript
fetch('/url').then(res => {}).catch(err => {})
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
9、[iOS-Performance-Optimization](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/skyming/iOS-Performance-Optimization)：关于 iOS 性能优化梳理。包含基本工具、业务优化、内存优化、卡顿优化、布局优化、电量优化、 安装包瘦身、启动优化、网络优化等

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
10、[arithmetic-php](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pushaowei/arithmetic-php)：PHP 语言实现的各类算法合集 

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
11、[rq](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rq/rq)：基于 redis 的简单、轻量级任务队列库。可以帮助理解简单的任务队列模式和设计。使用简单、文档健全，适用于小型项目或简单的场景。
```shell
# Tip：job 需要通过模块引用加入到任务队列中
23:46:59 Cleaning registries for queue: default
23:47:47 default: snap1.count_words_at_url('https://hellogithub.com') (c4f96606-c833-4057-8ac4-b35bc60dfec9)
23:47:47 default: Job OK (c4f96606-c833-4057-8ac4-b35bc60dfec9)
23:47:47 Result is kept for 500 seconds
```

12、[python-console-snake](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tancredi/python-console-snake)：命令行贪吃蛇

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/23/img/python-console-snake-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

13、[toapi](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gaojiuli/toapi)：该项目做的事儿是通过简单的配置把目标网页的内容爬下来，缓存结果后提供成 API 的一条龙服务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/23/img/toapi-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

14、[redash](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/getredash/redash)：开源的数据可视化 Web 项目，提供了数据库查询和数据可视化功能。只提供的数据可视化最要的功能，使得简单易用且容易上手。可以直观地将一个 SQL 查询的结果可视化出来。同时提供 SQL 代码片段存储，减少重复编写 SQL 的问题

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/23/img/redash.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
15、[LyricsX](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ddddxxx/LyricsX)：一个为 iTunes、Spotify、Vox 播放器提供自动下载歌词，并在桌面和任务栏显示的插件

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/23/img/LyricsX-show-min.jpg' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
16、[vim-galore](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mhinz/vim-galore)：Vim 从入门到精通，[中文](https://github.com/wsdjeg/vim-galore-zh_cn)

17、[awesome-blockchain-cn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chaozh/awesome-blockchain-cn)：区块链技术开发相关资料

18、[hangzhou_house_knowledge](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/houshanren/hangzhou_house_knowledge)：《杭州房产知识扫盲》，作者 2017 年总结出来的买房购房知识，希望可以帮助到要在杭州买房的朋友

19、[Back-End-Developer-Interview-Questions](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/monklof/Back-End-Developer-Interview-Questions)：后端面试问题集合

20、[http-api-design](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/interagent/http-api-design)：HTTP API 设计指南。这篇指南介绍描述了 HTTP+JSON API 的一种设计模式，最初摘录整理自 Heroku 平台的 API 设计指南。[中文翻译版](https://github.com/ZhangBohan/http-api-design-ZH_CN)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
21、[yast-cn](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/DeathKing/yast-cn)：《Scheme入门教程》中译版，[在线阅读](http://deathking.github.io/yast-cn/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
22、[captcha_break](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ypwhs/captcha_break)：使用深度学习来破解 captcha（python 生成验证码的库）验证码。该项目会通过 Keras 搭建一个深度卷积神经网络来识别 captcha 生成的图片验证码，建议使用显卡来运行该项目。可视化代码都是在 jupyter notebook 中完成的，如果你希望写成 python 脚本，稍加修改即可正常运行

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/22/HelloGitHub22.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/24/HelloGitHub24.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
