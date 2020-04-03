# 《HelloGitHub》第 27 期
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
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [Python 项目](#Python-项目)
- [Ruby 项目](#Ruby-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C# 项目
1、[Rosin](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/AlloyTeam/Rosin)：一个 Fiddler 插件，用于协助开发者进行移动端页面开发、调试

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/Rosin-min.jpeg' style="max-width:80%; max-height=80%;"></img></p>

2、[cms](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/siteserver/cms)：开源、免费、企业级内容管理平台。基于该工具可以快速、方便地搭建搭建一个性能优异、颇具规模、易于维护的网站平台

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/SiteServer-CMS-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
3、[MyTinySTL](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Alinshans/MyTinySTL)：用 C++11 实现的小型 STL（容器库＋算法库）。代码结构清晰规范、包含中文文档与注释，并且自带一个简单的测试框架，适合新手学习与参考。示例代码如下：
```c++
// 在尾部插入元素
template <class T>
void vector<T>::push_back(const value_type& value)
{
  if (end_ != cap_)
  {
    data_allocator::construct(mystl::address_of(*end_), value);
    ++end_;
  }
  else
  {
    reallocate_insert(end_, value);
  }
}
```

4、[apollo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ApolloAuto/apollo)：百度自主研发、开源的全面开放自动驾驶平台。它将帮助汽车行业及自动驾驶领域的合作伙伴结合车辆和硬件系统，快速搭建一套属于自己的自动驾驶系统

5、[incubator-brpc](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apache/incubator-brpc)：百度开源的 RPC 框架，拥有超过 100 万个实例和 500 多种服务

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
6、[appify](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/machinebox/appify)：该项目能够方便的把 Golang 项目包装成 MacOS 可以直接运行的软件。可以用来把自己写的小工具包装成一个其他人可以直接下载并双击使用的软件。提供自定义 logo、名字，分分钟发布自己的 Golang 软件。使用步骤如下：
```shell
# 1.安装命令
$ go get github.com/machinebox/appify

# 2.封装命令
$ appify -name "My Go Application" -icon ./icon.png /path/to/bin
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/appify-min.png' style="max-width:80%; max-height=80%;"></img></p>

7、[usql](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xo/usql)：通用SQL命令行客户端。支持以下所有数据库和协议：

| 数据库 (scheme/driver)        | 协议别名 [real driver]                 |
|------------------------------|---------------------------------------|
| Microsoft SQL Server (mssql) | ms, sqlserver                         |
| MySQL (mysql)                | my, mariadb, maria, percona, aurora   |
| Oracle (ora)                 | or, oracle, oci8, oci                 |
| PostgreSQL (postgres)        | pg, postgresql, pgsql                 |
| SQLite3 (sqlite3)            | sq, sqlite, file                      |

```
安装方法
1. 根据你的系统下载最新的 binary
2. 解压缩出 `usql` 或者 `usql.exe`
3. 把binary放到你的 `$PATH` (Linux/macOS) 或 `%PATH%` (Windows)路径下
4. 然后就可以用`usql`链接到你喜欢的SQL数据库啦~
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
8、[RetrofitUrlManager](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/JessYanCoding/RetrofitUrlManager)：以简洁的 API 让 Retrofit 同时支持多个 BaseUrl，动态改变 BaseUrl

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/RetrofitUrlManager.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
9、[v-region](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TerryZ/v-region)：使用 Vue 创建的中国省市区选择组件，组件复用程度高、可直接引入项目中使用。使用场景适用于需要用户选择地址，采用该组件可以提高交互程度。[文档](https://terryz.github.io/vue/#/region/demo)，示例代码：
```js
<v-region :city="false" :area="false" class="form-control"></v-region> // 只显示省份
<v-region :area="false" class="form-control"></v-region> // 显示省市
<v-region class="form-control"></v-region> // 显示省市区
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/v-region-min.png' style="max-width:80%; max-height=80%;"></img></p>

10、[whistle](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/avwo/whistle)：基于 Node.js 实现的跨平台 web 调试代理工具，类似于 Windows 平台上的 Fiddler。主要用于查看、修改HTTP、HTTPS、Websocket的请求、响应，也可以作为 HTTP 代理服务器使用。不同于 Fiddler 通过断点修改请求响应的方式，whistle 采用的是类似配置系统 hosts 的方式，一切操作都可以通过配置实现。通过该工具，可以现实复杂的前端环境、生产、开发、bugFix 一键切换。

11、[simpread](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Kenshin/simpread)：让你瞬间进入沉浸式阅读的扩展，还原阅读的本质，提升你的阅读体验。使用它可以为你剔除页面上无关的干扰信息，让用户专注于阅读主要的内容。通过这个项目，还可以学习如何开发 Chrome 扩展

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/simpread-min.png' style="max-width:80%; max-height=80%;"></img></p>

12、[incubator-echarts](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apache/incubator-echarts)：使用 JavaScript 实现的开源、流行、强大的可视化库。可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器。提供直观、交互丰富、可实现高度个性定制化的数据可视化图表，也可将其封装为任何 MVVM 框架的组件方便适用。[官网](http://echarts.baidu.com/)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/incubator-echarts-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
13、[KafkaRefresh](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/HsiaohuiHsiang/KafkaRefresh)：内置多种动画、可自定义和灵活的 iOS 下拉刷新框架。[中文文档](https://github.com/OpenFeyn/KafkaRefresh/blob/master/CREADME.md)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/KafkaRefresh.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
14、[tenacity](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jd/tenacity)：使用该库可以优雅地实现各种需求的重试。示例代码如下：
```python
from tenacity import retry, stop_after_attempt

# 通过装饰器，实现遇到异常重试3次
@retry(stop=stop_after_attempt(3)) 
def get_data(url):
    response = requests.get(url)
    response_json = response.json()
```

15、[unimatrix](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/will8211/unimatrix)：模拟“黑客帝国”影片中的终端动画脚本

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/unimatrix-min.png' style="max-width:80%; max-height=80%;"></img></p>

16、[pudb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/inducer/pudb)：基于控制台的全屏 Python 可视化调试器。比 pdb 好用太多了，特性：
- 源码语法高亮，栈、断点、变量可见并且一直动态更新。变量展示还有很多可以定制化的功能。
- 基于键盘，简单高效。支持 VI 的鼠标移动。还支持 PDB 的某些命令
- 支持查找源代码，可以使用 m 代用 module browser 查看载入的模块
- 断点设置。鼠标移到某行代码，按 b，然后可以在断点窗口编辑断点

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/pudb-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Ruby 项目
17、[hacker101](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Hacker0x01/hacker101)：（英文）一个免费的 Web安全课程。无论你是一个程序员、对 bug 悬赏感兴趣，或是一个经验丰富的安全专业人员，在 HACKE101 课程中都可以学到东西。包涵大量示例代码和在线 Demo，示例代码为 Ruby。

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
18、[IBAnimatable](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/IBAnimatable/IBAnimatable)：一个帮助我们在 Interface Builder 和 Swift Playground 里面设计 UI、交互、导航模式,、换场和动画的开源库。下图的整个 App 都是通过 IBAnimatable 在 Interface Builder 设计完成，没有任何一行代码。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/IBAnimatable.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[TuringCalendar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zhihaozhang/TuringCalendar)：图灵教育推出的限量款[编程日历 2018](http://www.ituring.com.cn/book/download/43507086-33c3-40e9-9115-d610e1333bca)，因为简约大气的设计和每周一个编程语言的介绍，在程序员中广受欢迎。现在日历 PDF 的源文件已经开源，于是就有了这个项目。一个 macOS 桌面上的日历 widget，效果图如下：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/TuringCalendar-min.jpeg' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
20、[Android_Data](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Freelander/Android_Data)：这个集合主要能够帮助初学者在初学 Android 开发的时候，能够快速、方便地找到适合自己的学习资料

21、[Front-End-Checklist](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thedaviddias/Front-End-Checklist)：一份在网站发布到生产环境之前，前端部分需要测试、检查的详尽清单。[中文版](https://github.com/JohnsenZhou/Front-End-Checklist)

22、[build-your-own-x](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/danistefanovic/build-your-own-x)：（英文）费曼：“我不能创造的東西，我就不了解。”该项目收集了不同编程语言造轮子的教程

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
23、[simplified-deeplearning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/exacity/simplified-deeplearning)：《DeepLearningBook》读书笔记

24、[elasticsearch-spark-recommender](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/IBM/elasticsearch-spark-recommender)：使用 Apache Spark 的机器学习库 (MLlib) 来训练一个协同过滤推荐系统模型 和 Elasticsearch 构建一个推荐系统教程，[中文版阅读](https://github.com/IBM/elasticsearch-spark-recommender/blob/master/README-cn.md)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/27/img/elasticsearch-spark-recommender-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/26/HelloGitHub26.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/28/HelloGitHub28.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
