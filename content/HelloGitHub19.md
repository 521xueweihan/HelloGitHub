# 《HelloGitHub》第 19 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/19) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### Go 项目
1、[ctop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bcicen/ctop)：实现了类 top 命令展示效果的 docker 容器监控工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/19/77419377.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
2、[HanLP](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hankcs/HanLP)：一系列模型与算法组成的 NLP 工具包，目标是普及自然语言处理在生产环境中的应用。具备功能完善、性能高效、架构清晰、语料时新、可自定义的特点，功能包括：中文分词、词性标注、命名实体识别、关键词提取等。示例代码：
```java
String[] testCase = new String[]{
    "北川景子参演了林诣彬导演的《速度与激情3》",
    "林志玲亮相网友:确定不是波多野结衣？",
};
Segment segment = HanLP.newSegment().enableJapaneseNameRecognize(true);
for (String sentence : testCase)
{
    List termList = segment.seg(sentence);
    System.out.println(termList);
}
```


3、[MVPArt](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/JessYanCoding/MVPArt)：一个新的 MVP 架构，此框架旨在解决传统 MVP 类和接口太多、并且 Presenter 和 View 通过接口通信过于繁琐、重用 Presenter 代价太大等问题。架构图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/19/83117984.png' style="max-width:80%; max-height=80%;"></img></p>

4、[p3c](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alibaba/p3c)：阿里云栖大会发布的 Java 代码规约扫描插件，支持多种 IDE。代码规范对于编程来说是非常重要的，随着代码量的增多会更加意识到其重要性。赶快拿去使用吧，[阿里巴巴 Java 开发手册](https://github.com/alibaba/p3c/blob/master/%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4Java%E5%BC%80%E5%8F%91%E6%89%8B%E5%86%8C%EF%BC%88%E7%BB%88%E6%9E%81%E7%89%88%EF%BC%89.pdf)


### JavaScript 项目
5、[emoji](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gee1k/emoji)：方便快速查找获取 emoji 表情、名称，并且可以复制到任何文本中，另外支持中文搜索 💯 [网站地址](http://emoji.svend.cc/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/19/104567903.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[H5](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/answershuto/H5)：这是作者的个人项目，功能是可视化编辑、生成手机 H5 页面的单页应用 WebApp。该项目是一个全栈项目，具有前后端完整服务。并且项目结构清晰。后端服务具有控制器，模型，路由，前端服务具有组件，并且使用 Vuex 做状态管理，麻雀虽小五脏俱全


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/19/76468697.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[project-guidelines](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/elsewhencode/project-guidelines)：JavaScript 项目规范，[中文](https://github.com/wearehive/project-guidelines/blob/master/README-zh.md)


8、[SelectMenu](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TerryZ/SelectMenu)：基于 jQuery 1.x 库的多样化的下拉菜单插件，源码具有中文注释，对于学习 jQuery 插件有帮助。示例代码如下：
```javascript
var data = [
    {id:1 ,name:'Chicago Bulls',desc:'芝加哥公牛'},
    {id:2 ,name:'Cleveland Cavaliers',desc:'克里夫兰骑士'},
    {id:3 ,name:'Detroit Pistons',desc:'底特律活塞'},
    {id:4 ,name:'Indiana Pacers',desc:'印第安纳步行者'}
];
//initialize selectmenu
$('#btnDemo').selectMenu({
    showField : 'desc',
    keyField : 'id',
    data : data
});
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/19/106082125.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
9、[kotlin-examples](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Kotlin/kotlin-examples)：JetBrains 开源的 Kotlin 语言 Web 示例项目


### PHP 项目
10、[Biny](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/Biny)：腾讯开源的一款高性能的超轻量级PHP框架，用于快速开发现代 Web 应用程序。代码简洁优雅，对应用层，数据层，模板渲染层的封装简单易懂，能够快速上手使用，[文档](http://www.billge.cc/)齐全。高性能，框架响应时间在 1ms 以内，单机 qps 轻松上3000。
- 支持跨库连表，条件复合筛选，查询PK缓存等
- 同步异步请求分离，类的自动化加载管理
- 支持Form表单验证，支持事件触发机制
- 支持浏览器端调试，快速定位程序问题和性能瓶颈
- 具有sql防注入，html自动防xss等特性


### Python 项目
11、[binlog2sql](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/danfengcao/binlog2sql)：从 MySQL binlog 解析出你要的 SQL。根据不同选项，提供如下功能
- 数据快速回滚，[闪回原理与实践](https://github.com/danfengcao/binlog2sql/blob/master/example/mysql-flashback-priciple-and-practice.md)
- 主从切换后新 master 丢数据的修复
- 从 binlog 生成标准SQL，带来的衍生功能


12、[pandas-tutorial](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hangsz/pandas-tutorial)：这套 pandas 教程包含从初级到进阶的内容，适合初学者和希望进阶建立知识体系的数据科学从业者阅读。作者还在持续更新高级内容，你值得拥有


13、[pysheeet](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/crazyguitar/pysheeet)：Python 速查表，[在线阅读](https://www.pythonsheets.com/)


14、[robobrowser](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jmcarp/robobrowser)：提供多种模拟操作网页的库，比如获得网页内容、访问链接、点击按钮、填充并提交表单、上传文件。使用简单、API 友好。适用于想要通过脚本流程化操作，某些未提供这些操作接口的场景，示例代码如下：
```python
# 上传文件
from robobrowser import RoboBrowser

# Browse to a page with an upload form
browser = RoboBrowser()
browser.open('http://cgi-lib.berkeley.edu/ex/fup.html')

# Find the form
upload_form = browser.get_form()
upload_form                     # <RoboForm upfile=, note=>

# Choose a file to upload
upload_form['upfile']           # <robobrowser.forms.fields.FileInput...>
upload_form['upfile'].value = open('path/to/file.txt', 'r')

# Submit
browser.submit(upload_form)
```


### 其它
15、[chinese-poetry](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/chinese-poetry/chinese-poetry)：中华古典文集数据集，包含 5.5 万首唐诗、26 万首宋诗和 2.1 万首宋词。唐宋两朝近 1.4 万古诗人和两宋时期1500 词人。以 json 文件、数据库方式存储，[爬取过程及分析](https://jackeygao.io/words/crawl-ci.html)


16、[ios-dev-flow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/leecade/ios-dev-flow)：iOS 开发流程，记录了 iOS 程序上架需要的方方面面


17、[remote-working](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/greatghoul/remote-working)：收集整理国内远程工作相关的项目


### 开源书籍
18、[kubernetes-handbook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rootsongjc/kubernetes-handbook)：Kubernetes 中文指南／实践手册，[在线阅读](https://jimmysong.io/kubernetes-handbook/)


19、[microservices](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/DocsHome/microservices)：《微服务：从设计到部署》中文版，[在线阅读](http://oopsguy.com/books/microservices/index.html)


20、[op_practice_book](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/meetbill/op_practice_book)：《运维实践指南》




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub18.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub20.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/19'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
