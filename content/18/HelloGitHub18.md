# 《HelloGitHub》第 18 期
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
- [CSS 项目](#CSS-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [其它](#其它)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C 项目
1、[db_tutorial](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cstack/db_tutorial)：用 C 从零创建一个简单的数据库

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### CSS 项目
2、[materialize](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Dogfalo/materialize)：基于 Material Design 的现代响应式前端框架，简化了前端的开发，文档丰富。[官网](http://materializecss.com/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
3、[tidb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pingcap/tidb)：开源分布式 NewSQL 数据库，能优雅的替换传统的数据库中间件、数据库分库分表等 Sharding 方案。具备如下核心特性：
- SQL支持 （TiDB 是 MySQL 兼容的）
- 水平线性弹性扩展
- 分布式事务
- 跨数据中心数据强一致性保证
- 故障自恢复的高可用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/tidb-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

4、[echo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/labstack/echo)：Go 语言最受欢迎的 Web 框架之一，具有：高性能、便于扩展、轻量的特点，示例代码：
```go
package main

import "github.com/labstack/echo"

func main() {
	e := echo.New()
	e.GET("/", callback)
	e.Logger.Fatal(e.Start(":3000"))
}

func callback(ctx echo.Context) error {
	return ctx.HTML(200, "<h1>你好 echo</h1>")
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/echo-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
5、[AndroidTVLauncher](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/JackyAndroid/AndroidTVLauncher)：一个 TV Leanback 风格桌面，基于 Leanback 库开发，符合 Android TV 官方交互规范

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/AndroidTVLauncher-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

6、[spring-data-jpa-datatables](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/darrachequesne/spring-data-jpa-datatables)：spring-data-jpa 和 jQuery [datatables](https://www.datatables.net/) 集成工具。极大简化基于 datatables 数据表格的开发，示例代码：
```
// 前端代码
$(document).ready(function() {
	var table = $('table#sample').DataTable({
		'ajax': {
			'contentType': 'application/json',
			'url': '/data/users',
			'type': 'POST',
			'data': function(d) {
				return JSON.stringify(d);
			}
		},

// java 代码 server-side becomes
@JsonView(DataTablesOutput.View.class)
@RequestMapping(value = "/data/users", method = RequestMethod.POST)
public DataTablesOutput<User> getUsers(@Valid @RequestBody DataTablesInput input) {
	return userRepository.findAll(input);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/spring-data-jpa-datatables-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

7、[xxl-job](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xuxueli/xxl-job)：轻量级分布式任务调度框架，其核心设计目标是：开发迅速、学习简单、轻量级、易扩展，文档齐全。[官网](http://www.xuxueli.com/xxl-job/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
8、[flatpickr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/flatpickr/flatpickr)：扁平化的日期选择组件，项目源码使用 TypeScript 编写，可以学习使用 Typescript 编写 JS 插件，Typescript 语言的好处是：可以在多人协作中避免一些变量类型错误的问题，从而提高效率。使用示例代码：
```javascript
// ConnonJS 方式引入
const flatpickr = require("flatpickr");
flatpickr("#myID", {});
flatpickr(".myClass", {}); 

// jQuery 方式引入
$(".selector").flatpickr(optional_config);
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/flatpickr-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

9、[vue-3d-model](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hujiulong/vue-3d-model)：展示三维模型的 Vue 组件，支持模型操作和模型点击事件，能自动缩放模型到合适大小并校正偏移，目前支持 obj、stl、dae 和 json 格式的模型，示例代码：
```vue
<template>
    <model-obj src="example/models/obj/LeePerrySmith.obj"></model-obj>
</template>
<script>
    import { ModelObj } from 'vue-3d-model'

    export default {
        components: { ModelObj }
    }
</script>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/vue-3d-model.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[weweChat](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/trazyn/weweChat)：微信的第三方客户端。在完整实现 Web 微信功能的基础上，新增并优化部分功能，重设计整体 UI，提供更好的体验。Mac 安装命令：`brew cask install wewechat`

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/weweChat-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

11、[puppeteer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/puppeteer/puppeteer)：Google Chrome 团队开源的面向 Node.js 的，基于 DevTools 协议的远程 Headless Chrome 控制库，它可以生成网页截图、PDF、抓取单页应用与网页内容、进行自动化表单提交、界面测试与模拟键盘输入等功能。示例代码如下：
```javascript
// 访问 https://example.com 并将截图保存为 example.png
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();
```

12、[SelectPage](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TerryZ/SelectPage)：简洁优雅而功能强大的选择器，使用简单，适应各种UI环境，功能强大，丰富的参数和回调函数
。它包含了 autocomplete、ajax 数据源、多选择 Tag、i18n 国际化，结果列表分页展示，键盘快捷操作等
```javascript
//defined a array, the data returned at the server side is also used that format：
//Array[{Object},{...}]
var data = [
    {id:1 ,name:'Chicago Bulls',desc:'芝加哥公牛'},
    {id:2 ,name:'Cleveland Cavaliers',desc:'克里夫兰骑士'},
    {id:3 ,name:'Detroit Pistons',desc:'底特律活塞'},
    {id:4 ,name:'Indiana Pacers',desc:'印第安纳步行者'}
];
//init SelectPage
$('#selectpage').selectPage({
    showField : 'desc',
    keyField : 'id',
    data : data
});
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/SelectPage-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
13、[wooyun_public](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hanc00l/wooyun_public)：乌云公开漏洞、知识库爬虫和搜索

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/18/img/wooyun-show-min.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
14、[pygorithm](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/OmkarPathak/pygorithm)：一个帮助学习主要算法的库，可以通过理解这些算法的实现，提高自己的算法水平。冒泡排序示例：
```python
>>> from pygorithm.sorting import bubble_sort
>>> my_list = [12, 4, 3, 5, 13, 1, 17, 19, 15]
>>> sorted_list = bubble_sort.sort(my_list)
>>> print(sorted_list)
>>> [1, 3, 4, 5, 12, 13, 15, 17, 19]
```

15、[newspaper](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/codelucas/newspaper)：强大的提取 Web 的内容、文章的库，支持多种语言，安装命令 `pip3 install newspaper3k`。示例代码：
```python
>>> from newspaper import Article

>>> url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
>>> article = Article(url)

>>> article.download()

>>> article.html
'<!DOCTYPE HTML><html itemscope itemtype="http://...'

>>> article.parse()

>>> article.authors
['Leigh Ann Caldwell', 'John Honway']

>>> article.publish_date
datetime.datetime(2013, 12, 30, 0, 0)

>>> article.text
'Washington (CNN) -- Not everyone subscribes to a New Year's resolution...'

>>> article.top_image
'http://someCDN.com/blah/blah/blah/file.png'

>>> article.movies
['http://youtube.com/path/to/link.com', ...]

>>> from newspaper import Article
>>> url = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'

>>> a = Article(url, language='zh') # Chinese

>>> a.download()
>>> a.parse()

>>> print(a.text[:150])
香港行政长官梁振英在各方压力下就其大宅的违章建
筑（僭建）问题到立法会接受质询，并向香港民众道歉。
梁振英在星期二（12月10日）的答问大会开始之际
在其演说中道歉，但强调他在违章建筑问题上没有隐瞒的
意图和动机。 一些亲北京阵营议员欢迎梁振英道歉，
且认为应能获得香港民众接受，但这些议员也质问梁振英有

>>> print(a.title)
港特首梁振英就住宅违建事件道歉
```

16、[faker](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/joke2k/faker)：用于生成假数据的库，支持多种语言，你值得拥有。示例代码：
```python
fake.address()
# '辽宁省雪市静安廉街b座 998259'

fake.street_address()
# '巢湖街U座'

fake.building_number()
# 'x座'

fake.city_suffix()
# '市'

fake.latitude()
# Decimal('-0.295126')

fake.province()
# '湖北省'
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
17、[ctf-wiki](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ctf-wiki/ctf-wiki)：一个自由的站点，主要包含了 CTF 的基础知识 、常见题型、解题思路以及常用工具等，希望可以帮助你更快地了解 CTF 竞赛以及网络安全相关知识

18、[china_area_mysql](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kakuilan/china_area_mysql)：中国 5 级行政区域 MySQL 库

19、[open_source_team](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/niezhiyang/open_source_team)：国内顶尖团队的开源地址

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
20、[deeplearningbook-chinese](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/exacity/deeplearningbook-chinese)：Deep Learning 中文版

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/17/HelloGitHub17.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/19/HelloGitHub19.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
