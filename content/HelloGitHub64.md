# 《HelloGitHub》第 64 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/64) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[X-TRACK](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/FASTSHIFT/X-TRACK)：开源的 GPS 自行车码表。功能齐全且拥有美观的界面，支持离线地图、显示轨迹等功能。[在线观看](https://www.bilibili.com/video/BV1GB4y1K7VV)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/349490770.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
2、[ToastFish](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Uahh/ToastFish)：利用 Windows 通知栏背单词的软件。能够选择单词集合，并在背完后进行测验


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/363866643.gif' style="max-width:80%; max-height=80%;"></img></p>

3、[XboxDownload](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/skydevil88/XboxDownload)：Xbox 下载助手。支持 Xbox 游戏加速下载、比价等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/376881436.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[Plants-vs.-Zombies-Online-Battle](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Zhuagenborn/Plants-vs.-Zombies-Online-Battle)：在没有游戏源代码的前提下，通过逆向工程和代码注入实现植物大战僵尸局域网对战模式。成功加载后解密模式的最后一关，会变为网络对战关卡。玩法为其中一个玩家放置植物进行防御，另一玩家放置僵尸进攻。项目结合逆向工程、C++和汇编相关技术，在无源代码的前提下为游戏增加功能。对逆向工程感兴趣的小伙可以看看源码


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/294864064.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[xpack](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xyz347/xpack)：实现 C++ 结构体和 JSON/XML/BSON 互转的库。C++ 初学者可以通过该项目学到高阶的宏技巧和初级的 SFINAE 写法
```c++
#include <iostream>
#include "xpack/json.h" // 包含该头文件

struct User {
    int id;
    std::string name;
    XPACK(O(id, name)); // 添加宏定义XPACK在结构体定义结尾
};

int main(int argc, char *argv[]) {
    User u;
    string data = "{\"id\":12345, \"name\":\"xpack\"}";

    xpack::json::decode(data, u);          // json转结构体
    cout<<u.id<<';'<<u.name<<endl;

    string json = xpack::json::encode(u);  // 结构体转json
    cout<<json<<endl;
    return 0;
}
```


### CSS 项目
6、[normalize.css](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/necolas/normalize.css)：用来消除浏览器默认样式的 CSS 库。不同浏览器对于同一个元素会有不一样的默认样式，比如：超链接线的颜色。相较于 reset（重制样式）解决办法，normalize.css 采用更加和平且高效地方式，解决了浏览器默认样式的问题，尽可能让同一个 CSS 文件在不同的浏览器上显示效果一样和正常


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/1700621.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
7、[dtm](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dtm-labs/dtm)：Go 语言实现的分布式事务管理器。优雅的解决了微服务架构下幂等、空补偿、悬挂等分布式事务难题，提供了简单易用、高性能、易水平扩展的分布式事务解决方案，除 Go 外还有 Python、PHP、Node.js 等语言的客户端
```go
  // 具体业务微服务地址
  const qsBusi = "http://localhost:8081/api/busi_saga"
	req := &gin.H{"amount": 30} // 微服务的载荷
	// DtmServer为DTM服务的地址，是一个url
	saga := dtmcli.NewSaga("http://localhost:8080/api/dtmsvr").
		// 添加一个TransOut的子事务，正向操作为url: qsBusi+"/TransOut"， 补偿操作为url: qsBusi+"/TransOutCompensate"
		Add(qsBusi+"/TransOut", qsBusi+"/TransOutCompensate", req).
		// 添加一个TransIn的子事务，正向操作为url: qsBusi+"/TransOut"， 补偿操作为url: qsBusi+"/TransInCompensate"
		Add(qsBusi+"/TransIn", qsBusi+"/TransInCompensate", req)
	// 提交saga事务，dtm会完成所有的子事务/回滚所有的子事务
  err := saga.Submit()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/367758176.png' style="max-width:80%; max-height=80%;"></img></p>

8、[erda](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/erda-project/erda)：企业级一站式 PaaS 平台。基于 Kubernetes 以应用为中心的 DevOps 且支持微服务治理的多云架构，可以让复杂业务的开发、运维、监控和问题诊断变得更简单、更高效。能减轻使用不同的工具混搭技术底座和云平台的运维难度，同时还有漂亮、简单易用的界面设计


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/344676663.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[goim](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Terry-Mao/goim)：轻量级、高性能、支持集群的 IM 和实时推送服务。纯 Golang 实现支持广播消息、房间推送、安全验证和多协议支持等功能，还有基于 Kafka 的异步消息推送


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/34854605.png' style="max-width:80%; max-height=80%;"></img></p>

10、[hugo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gohugoio/hugo)：Go 语言的静态网站生成器。静态网站生成器就是在本地把内容文件生成静态网页（HTML+CSS），然后把生成好的页面上传到服务器的工具。这种工具能够帮你轻松且快速地上线网站，而用户仅需选择喜欢的主题，便可以专注于内容创作。Hugo 作为最流行的静态网站生成器之一，拥有丰富的插件和主题，就算没有编程基础也能帮你快速制作出满意的博客或者网站


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/11180687.png' style="max-width:80%; max-height=80%;"></img></p>

11、[TopList](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tophubs/TopList)：各大网站热门头条的聚合网站。[在线预览](https://mo.fish/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/196937459.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
12、[dataease](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dataease/dataease)：开源的数据可视化和分析工具。采用 SpringBoot+Vue.js 技术栈实现，通过丰富的可视化图表让数据更加直观
- 数据连接：支持关系型数据库、Excel 等文件、Hadoop 等大数据平台、NoSQL 等各种数据源
- 图表展示：支持 PC 端、移动端及大屏
- 制作图表：支持丰富的图表类型、支持拖拉拽方式快速制作仪表板
- 数据引擎：支持直连模式、本地模式


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/335164964.gif' style="max-width:80%; max-height=80%;"></img></p>

13、[guava](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/guava)：Google 开源的 Java 三方类库。该库提供包括集合、I/O、缓存、并发等开箱即用的工具方法，任何的 Java 应用都可以通过依赖的方式引入该项目。作为 Google 的开源项目，本身的源码也是非常值得开发者学习


14、[Mybatis-PageHelper](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pagehelper/Mybatis-PageHelper)：MyBatis 通用分页插件，[使用方法](https://github.com/pagehelper/Mybatis-PageHelper/blob/master/wikis/zh/HowToUse.md)


### JavaScript 项目
15、[50projects50days](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bradtraversy/50projects50days)：50 个采用 HTML+CSS+JS 的前端小项目集合。项目包含网页源码和效果展示，标准入门级的前端开源项目。通过查看效果让新手感受前端的美妙，简单的源码降低了上手写代码门槛。或许其中某个网页的效果也会让工作多年的你大呼哇塞


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/313330998.png' style="max-width:80%; max-height=80%;"></img></p>

16、[etherpad-lite](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ether/etherpad-lite)：支持实时协作的富文本 WYSIWYG 编辑器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/1529160.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[gogocode](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thx/gogocode)：简化 JavaScript 抽象语法树（AST）处理的工具。借鉴了类似 jQuery 的预发和字符串构建 AST 的思想，大大简化了学习成本、降低了开发复杂度，官方团队在此基础上还开发出了 [Vue2 转 Vue3 的插件](https://gogocode.io/zh/docs/vue/vue2-to-vue3)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/344026346.png' style="max-width:80%; max-height=80%;"></img></p>

18、[rubick](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/rubickCenter/rubick)：基于 Electron 开发的开源插件化工具箱。起初项目作者是 uTools 的用户但 uTools 没有开源，他又想接入公司内部的工具，然后 Rubick（拉比克）就诞生了。它实现了 uTools 的大部分功能，可以适配 uTools 丰富的开源插件，享受用完即走的便利


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/375877482.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[sjcl](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bitwiseshiftleft/sjcl)：斯坦福大学开源的 JavaScript 加密库。用于 JS 的加密和解密，体积小且支持多种加密算法
```javascript
sjcl.encrypt("password", "data") //加密数据
sjcl.decrypt("password", "encrypted-data") //解密数据
```


### Kotlin 项目
20、[k-9](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thundernest/k-9)：开源的 Android 电子邮件客户端


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/1326671.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
21、[bigdata_analyse](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/TurboWay/bigdata_analyse)：大数据分析实战项目的集合。该项目包含了淘宝、租房、招聘等数据的分析实例，不仅有 Python、SQL、HQL 的实例代码，还附上了数据集下载地址。想学习大数据的同学们，万事俱备就差你来学了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/324295142.png' style="max-width:80%; max-height=80%;"></img></p>

22、[JDMemberCloseAccount](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yqchilde/JDMemberCloseAccount)：用 Python 操作 selenium 的实战项目。该项目以全自动退出京东加入的店铺会员为例，介绍了 Python 自动化的知识和方案


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/364211069.png' style="max-width:80%; max-height=80%;"></img></p>

23、[OnlineJudge](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/QingdaoU/OnlineJudge)：青岛大学开源的在线评测系统（OJ），采用 Django+Vue.js 实现。功能如下：
- 基于 Docker 的一键部署
- 支持 ACM/OI 两种比赛模式、实时/非实时评判
- 丰富的可视化图表，一图胜千言
- 支持多种编程语言：C/C++、Java、Python2/3
- 比赛用户 IP 限制 (CIDR ranges)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/40759452.png' style="max-width:80%; max-height=80%;"></img></p>

24、[Pillow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/python-pillow/Pillow)：最流行的 Python 图像处理库。它的诞生是由于 PIL 的年久失修，现已于 2011 年停止维护，所以开源爱好者们就在 PIL 的基础上创建了 Pillow。该库支持丰富的图像格式和强大的图像处理功能，如果你要用 Python 处理图像，它绝对是不二之选
```python
# 安装：pip install pillow
# 注意安装的版本，不同版本支持的 Python 版本也不同

from PIL import Image
# 打开 jpg 图像文件
im = Image.open('hellogithub.jpg')
# 转换成黑白图像
grayscale = tatras.convert('L')
# 展示图像
grayscale.show()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/5171600.png' style="max-width:80%; max-height=80%;"></img></p>

25、[tqsdk-python](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/shinnytech/tqsdk-python)：开源的 Python 量化交易框架。使用少量代码即可实现量化交易程序，还支持历史数据、实时数据、策略回测、实盘交易、图形化界面展示等功能。但免费版本仅提供全部的期货、商品/金融期权和上证50、沪深300 和中证500 的实时行情，付费版支持更多种类以及更加稳定的服务
```python
from tqsdk import TqApi, TqAuth, TqAccount, TargetPosTask

api = TqApi(TqAccount("H海通期货", "4003242", "123456"), auth=TqAuth("信易账户", "账户密码"))      # 创建 TqApi 实例, 指定交易账户
q_1910 = api.get_quote("SHFE.rb1910")                         # 订阅近月合约行情
t_1910 = TargetPosTask(api, "SHFE.rb1910")                    # 创建近月合约调仓工具
q_2001 = api.get_quote("SHFE.rb2001")                         # 订阅远月合约行情
t_2001 = TargetPosTask(api, "SHFE.rb2001")                    # 创建远月合约调仓工具

while True:
  api.wait_update()                                           # 等待数据更新
  spread = q_1910.last_price - q_2001.last_price        # 计算近月合约-远月合约价差
  print("当前价差:", spread)
  if spread > 250:
    print("价差过高: 空近月，多远月")
    t_1910.set_target_volume(-1)                              # 要求把1910合约调整为空头1手
    t_2001.set_target_volume(1)                               # 要求把2001合约调整为多头1手
  elif spread < 200:
    print("价差回复: 清空持仓")                               # 要求把 1910 和 2001合约都调整为不持仓
    t_1910.set_target_volume(0)
    t_2001.set_target_volume(0)
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/136556542.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
26、[firefox-ios](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mozilla-mobile/firefox-ios)：Firefox 浏览器 iOS 源码


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/26133979.jpeg' style="max-width:80%; max-height=80%;"></img></p>

27、[SwifterSwift](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SwifterSwift/SwifterSwift)：500合1 的原生 Swift 扩展库集合。集成了 500 多个原生 Swift 扩展的库，提供了更加方便的函数、语法糖、数据类型、UIKit 以及更高性能的 Cocoa 类，提高 Swift 的开发效率实现 1+1>2 的效果。适用于 iOS、macOS、tvOS 等系统
```swift
// 原来使用 UIAlertController 实现提醒的代码如下：
let alert = UIAlertController(title: "测试", message: "HelloGitHub", preferredStyle: .alert)
let okAction = UIAlertAction(title: "OK", style: .cancel, handler: nil)

alert.addAction(okAction)
present(alert, animated: true, completion: nil)

// 改成 SwifterSwift 后：
let alert = UIAlertController(title: "测试", message: "HelloGitHub")
alert.show()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/64705781.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
28、[adarkroom](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/doublespeakgames/adarkroom)：《小黑屋》是一款有趣的文字冒险类游戏。支持中文能够运行在浏览器、iOS 和 Android 设备，浏览器上默认会保存游戏进度到本地，另外还支持存档导入/导出防止丢失。友情提示：没玩过的同学刚开始容易摸不着头脑，因为事件触发需要时间，看滚动的文字+点击“添柴”耐心等 30 秒，就会触发新的事件了。如果你喜欢养成类游戏，那它一定会是你的菜。[在线试玩](http://adarkroom.doublespeakgames.com/?lang=zh_cn)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/11152831.png' style="max-width:80%; max-height=80%;"></img></p>

29、[developer-roadmap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kamranahmedse/developer-roadmap)：开发者学习路线图。这是一份包含后端、前端、运维部署等方向的学习路径图，帮你指明前进的方向。[中文](https://github.com/kamranahmedse/developer-roadmap/tree/master/translations/chinese)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/85077558.png' style="max-width:80%; max-height=80%;"></img></p>

30、[elasticsearch-dump](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/elasticsearch-dump/elasticsearch-dump)：Elasticsearch 数据导入/导出工具，可以用于 ES 的数据备份和迁移


31、[freeCodeCamp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/freeCodeCamp/freeCodeCamp)：免费学习编程的开源社区。它创立于 2014 年，期间帮助了无数编程爱好者学习编程，[中文站点](https://chinese.freecodecamp.org/)于 2021 年上线。freeCodeCamp 采用在线编程闯关的学习形式，遇到问题还可以通过活跃的社区答疑解惑。平台鼓励新手多动手写代码、运行代码，提倡 RSA 即：遇到问题先阅读文档资料，然后求助于搜索引擎，最后实在没招了再提问，这样有助于培养良好的提问习惯终身受益。同时作为非盈利组织，freeCodeCamp 不仅提供了免费学习的课程还开源了网站代码


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/28457823.png' style="max-width:80%; max-height=80%;"></img></p>

32、[git-split-diffs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/banga/git-split-diffs)：更加直观展示代码改动的命令行工具。在终端上使用 `git diff` 查看修改时，默认的展示效果并不直观，该项目将代码的改动以类似 GitHub 网站的风格展示方便查看，还有多种主题可供选择


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/356674026.png' style="max-width:80%; max-height=80%;"></img></p>

33、[hyper](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/vercel/hyper)：基于 Electron 的超高颜值终端工具。颜值即正义不仅在找对象时有用，挑工具时也同样奏效。它支持包括 Windows、Linux、macOS 等主流操作系统快下载试试，让你的终端漂亮得不像实力派


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/62367558.png' style="max-width:80%; max-height=80%;"></img></p>

34、[nocodb](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nocodb/nocodb)：开源的智能表格制作工具。我最初以为 nocodb 只是数据库桌面管理工具，后来我发现自己狭隘了。它不仅可以把数据库和图片等数据转化成表格的方式展现，还提供了团队协作、工作流接入以及更加开放 API 服务。让团队在数据上工作，数据就在手边“即视即用”。知名电子表格-数据库混合体 Airtable 产品的开源替代品


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/108761645.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
35、[CheatSheetSeries](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/OWASP/CheatSheetSeries)：OWASP（开放式 Web 应用程序安全项目）速查表。项目由 OWASP 社区的安全专家编写，列举了多种安全问题和解决方案，从而更好地保护你的 Web 应用。[在线阅读](https://cheatsheetseries.owasp.org/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/162723104.png' style="max-width:80%; max-height=80%;"></img></p>

36、[http-api-guide](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bolasblack/http-api-guide)：《HTTP 接口设计指北》内容为设计 Web API 的一些建议


37、[understand_linux_process](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tobegit3hub/understand_linux_process)：《理解 Linux 进程》


### 机器学习
38、[DouZero_For_HappyDouDiZhu](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tianqiraf/DouZero_For_HappyDouDiZhu)：基于快手开源的斗地主强化学习框架，实现的欢乐斗地主 AI 助手


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/384885506.png' style="max-width:80%; max-height=80%;"></img></p>

39、[HyperLPR](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/szad670401/HyperLPR)：中文车牌识别开源框架。支持 Python、Android、C++ 等编程语言调用，接入简单准确度较高。推荐给有车牌识别需求的小伙伴


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/104621881.png' style="max-width:80%; max-height=80%;"></img></p>

40、[insightface](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/deepinsight/insightface)：支持 2D&3D 人脸分析的 Python 库。基于 PyTorch 和 MXNet 实现，采用先进的 ArcFace 人脸识别方法，高效地实现了人脸检测、识别等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/64/102057483.png' style="max-width:80%; max-height=80%;"></img></p>

41、[Statistical-Learning-Method_Code](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Dod-o/Statistical-Learning-Method_Code)：用 Python 实现《统计学习方法》书中的算法




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub63.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub65.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/64'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
