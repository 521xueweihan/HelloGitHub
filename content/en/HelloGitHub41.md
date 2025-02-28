# HelloGitHub Vol.41
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C#
1、[csredis](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/2881099/csredis)：Redis.io 官方推荐的 C# 语言 redis 客户端库，支持 redis 2.8-5.0 版本的所有命令，且包含哨兵、集群等功能。该项目从 2016 年开始持续迭代更新，实现了低门槛、高性能和分区等高级玩法。该项目作者：[2881099](https://github.com/2881099)，在 GitHub 上开源了很多有趣、实用的 C# 项目。欢迎大家关注他，同时参与到他的项目中，为开源社区贡献自己的一份力量。示例代码：
```csharp
var csredis = new CSRedis.CSRedisClient("127.0.0.1:6379,password=123");
RedisHelper.Initialization(csredis);

RedisHelper.Set("test1", "123123", 60);
RedisHelper.Get("test1");
//...函数名与 redis-cli 的命令相同

//普通订阅
RedisHelper.Subscribe(
  ("chan1", msg => Console.WriteLine(msg.Body)),
  ("chan2", msg => Console.WriteLine(msg.Body)));

//管道操作
RedisHelper.StartPipe().Set("a", "1").Get("a").EndPipe();
```


### C++
2、[awesome-modern-cpp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rigtorp/awesome-modern-cpp)：Wow Awesome！你想将 modern cpp 运用自如吗？那就来看 Awesome-modern-cpp 吧！这里列出了一些有关现代 C++ 的最佳实践、书籍、会议、谈话、播客、博客、网站、各种各样的库以及一些工具，让你不禁 Wow Awesome，这就是你独享的 moment


3、[fmt](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fmtlib/fmt)：这是一个开源的 C++ 格式库。它可以作为 (s)printf 和 iostreams 的安全和快速替代品，也是 C++ 20 中  std::format 的一个实现。它的格式化字符串语法类似于 Python 中的 `str.format`，支持用户自己定义的类型，还比 printf 和 iostreams 的常见标准库实现更快！而且 fmt 还非常安全，格式字符串中的错误可以在编译时报告，还可以防止缓冲区溢出错误。示例代码：
```c++
fmt::print("Hello, {}!", "world");  // 类 Python 的语法风格
fmt::printf("Hello, %s!", "world"); 
```


### Go
4、[go-github](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google/go-github)：谷歌出品的 GitHub API Go 语言版本。如果你需要做一个 GiHhub 相关的产品后端，这个可以省去很多功夫，而且还可以学习谷歌工程师写的  Go 项目、设计接口的思路。示例代码：
```go
import "github.com/google/go-github/v27/github" // 启用的 go module (GO111MODULE=on 或者不在 GOPATH 里)
import "github.com/google/go-github/github" // 没启用 go module 时

client := github.NewClient(nil)

// 获取用户 "willnorris" 所在的所有组织
orgs, _, err := client.Organizations.List(context.Background(), "willnorris", nil)
```


5、[gridstudio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ricklamers/gridstudio)：一个后端采用 Go 语言的电子表格 Web 应用程序，支持 Python 编程语言处理数据，结果运行即可见。它旨在提供一个集成的工作流程，用于加载、清理、操作和可视化数据。可在线使用，对于用 Python 等处理数据的数据工程师而言，就是一款神器。之前就很好奇石墨文档怎么做的，这下可以学习下了，电子表单是一个比较复杂的问题，该项目有很多可以学习的地方。安装：
```bash
git clone https://github.com/ricklamers/gridstudio # clone 项目
cd gridstudio && ./run.sh # 直接运行
# 然后访问 http://127.0.0.1:8080 用户名：admin 密码：admin
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/198441611.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[simple-computer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/djhworld/simple-computer)：一个用 Go 语言模拟简单计算机 CPU 的项目。只有 Go 语言的函数，没有硬件的模块，从与非门直到一台能做加减运算和显示的迷你虚拟计算机。这些是计算机最底层、基础的东西，虽然是使用 Go 语言模拟，而不是用硬件打造而。但是计算机的基本结构，运行的基本原理都显示的非常清楚。对于新手，既能了解 CPU 原理，也会发现编程语言除了能写软件之外的其他有趣用处。安装命令：
```bash
make # 构建项目
make test # 测试
./bin/simulator -bin _programs/brush.bin # 运行虚拟机
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/186473531.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
7、[SmartSwipe](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/luckybilly/SmartSwipe)：一个侧滑处理框架，而不是具体某种侧滑效果的实现。其内部封装十几种侧滑效果，包括侧滑返回、侧滑删除、百叶窗、开门等效果，总有那么几款能让你眼前一亮。示例代码：
```java
//为控件添加仿MIUI的弹性拉伸效果：
//	当纵向不能滚动（或滚动到顶/底）时，若继续拖动，则 UI 呈现弹性拉伸效果，释放后平滑恢复
SmartSwipe.wrap(view)
	.addConsumer(new StretchConsumer())
	.enableVertical();

SmartSwipe.wrap(view)
	.addConsumer(new StretchConsumer())
	.enableVertical() 	//仿 MIUI 拉伸效果的方向为：上下 2 个方向
	.addConsumer(new SpaceConsumer())
	.enableHorizontal()  //仿 iOS 弹性留白效果的方向为：左右 2 个方向
	;

SmartSwipeBack.activityBezierBack(application, null);	//仿小米 MIUI 系统的贝塞尔曲线返回效果
SmartSwipeBack.activityStayBack(application, null);		//仿手机 QQ 的手势滑动返回
SmartSwipeBack.activitySlidingBack(application, null);	//仿微信带联动效果的透明侧滑返回
SmartSwipeBack.activityDoorBack(application, null);		//侧滑开门样式关闭 activity
SmartSwipeBack.activityShuttersBack(application, null);	//侧滑百叶窗样式关闭 activity

//xxxMode 第二个参数为 false，表示工作方向为纵向：下拉刷新&上拉加载更多
//如果第二个参数设置为 true，则表示工作方向为横向：右拉刷新&左拉加载更多
SmartSwipeRefresh.drawerMode(view, false).setDataLoader(loader);
SmartSwipeRefresh.behindMode(view, false).setDataLoader(loader);
SmartSwipeRefresh.scaleMode(view, false).setDataLoader(loader);
SmartSwipeRefresh.translateMode(view, false).setDataLoader(loader);
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/196566030.gif' style="max-width:80%; max-height=80%;"></img></p>

8、[SoloPi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alipay/SoloPi)：一个不需要连接电脑、非侵入式的 Android 自动化工具。公测版拥有录制回放、性能测试、一机多控三项主要功能，能为测试开发人员节省宝贵时间。安卓版本多、终端型号多，一个成熟安卓应用的上线需要进行大量测试，而很多测试都是属于重复操作，通过此工具可以极大简化测试人员的工作量


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/175650201.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[vhr](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lenve/vhr)：一个前后端分离的人力资源管理系统。该项目采用 SpringBoot + Vue 架构，这两个都是近些年很流行的框架。该项目涉及的场景很多，可作为全栈工程师的入门实践


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/116237823.png' style="max-width:80%; max-height=80%;"></img></p>

10、[XUI](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xuexiangjys/XUI)：一个简洁而优雅的 Android 原生 UI 框架。让原生 Android 开发人员也能像 web 开发者一样，拥有方便的 UI 库。该项目适用于有一定 Android 开发经验的开发者


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/164397881.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
11、[chart.xkcd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/timqian/chart.xkcd)：手绘风格的 JS 图表库。手绘风格的设计给人一种很可爱的感觉，看了这些图表你会发现数据也可以以萌萌哒的形式展示


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/200573908.xkcd' style="max-width:80%; max-height=80%;"></img></p>

12、[fullPage.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alvarotrigo/fullPage.js)：通过调用 fullPage 可轻易创建全屏滚动网站（也称为单页网站）。 fullPage 可创建全屏滚动网站，同时也可在网站中添加横向滚动条。适合快速搭建全屏滚动或者拥有视觉差的站点，使得网站看上去更加高端、大气、上档次，示例代码：
```javascript
<div id="fullpage">
  <div class="section">Some section</div>
  <div class="section">Some section</div>
  <div class="section">Some section</div>
  <div class="section">Some section</div>
</div>
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/12972263.png' style="max-width:80%; max-height=80%;"></img></p>

13、[PicGo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Molunerfinn/PicGo)：基于 electron-vue 实现的桌面图床工具。该工具可以帮助你高效、非常方便地上传图片到网络图床，包括了微博图床、七牛图床、腾讯云 COS、又拍云、GitHub、SM.MS、阿里云OSS、Imgur 等。只要使用快捷键或拖动就可以上传，而且上传成功的图片链接会自动复制到你的剪贴板里，支持 macOS、Windows、Linux 三大系统


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/113965016.png' style="max-width:80%; max-height=80%;"></img></p>

14、[Valine](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xCss/Valine)：一款快速、简洁且高效的无后端的 JS 评论插件。该库使用 LeanCloud API 存储数据，且设计美观、体积小、支持 Markdown 和 Emoji。对于使用 Hexo、Hugo 等静态网页博客主来说，它简直就是福音。通过简单的几步就可以快速的给自己的博客增加评论功能，你还不快来试试


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/99242671.png' style="max-width:80%; max-height=80%;"></img></p>

15、[webtorrent](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/webtorrent/webtorrent)：基于 JS 的流媒体种子客户端。不需要等待种子中的内容下载完毕，就可以马上播放种子中的内容，且有 Windows、Mac 和 Linux 操作系统的桌面版客户端。还在为等待下载而苦恼吗？有了它即可复制种子链接观看对应的视频内容


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/13584262.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
16、[bullet](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bchao1/bullet)：一个支持终端输入和菜单选择的 Python 库。可以让使用者在终端上用方向键移动、单选、复选、密码输入等，而且支持定制化格式和颜色。看下面的效果图你就知道它是干什么


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/171899746.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[DaPy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/JacksonWuxs/DaPy)：一个易用的数据分析 Python 库。通过提供合理的数据结构和丰富的机器学习模型，它能帮你快速地实现数据分析思路。简单来说，DaPy 能帮助你完成数据挖掘任务中的每一步，导入导出数据、预处理数据、特征工程、模型训练和模型评估等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/124340246.png' style="max-width:80%; max-height=80%;"></img></p>

18、[PyUnit](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jtyoui/PyUnit)：帮助学习 Python 的代码集合包。包含 20 多个简单易用的常用方法和数学函数，大多数方法在 100 行左右，而且每一个类的使用都有对应的测试用例。非常方便初学者学习，也可以帮助有经验的开发者快速实现一些功能。示例代码：
```python
# 这是一个阳历转化农历的程序
from jtyoui.plunar import SC
if __name__ == '__main__':
    lun = SC(year=2018, month=1, day=2) #阳历转农历
    print(lun.y)  # 农历的年,中文字符 二零一九
    print(lun.year)  # 农历的年，阿拉伯数字 2019
    ...
    print(lun)  # 二零一九年 七月 十四 星期四 无
```


### Ruby
19、[overcommit](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sds/overcommit)：一款可配置的 git hook 管理工具。git hook 是 git 的强大功能，当触发某一个 git 的事件，例如：add、commit、push 等操作时，会触发执行对应事件的附加操作（hook）。可以用来检测代码质量、commit 描述风格、控制代码质量等。overcommit 就是能让你不写一行代码（配置不算代码），来自定义 hook 要执行的操作。它使用简单、文档详尽、例子众多、社区活跃，值得一试


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/1520275.png' style="max-width:80%; max-height=80%;"></img></p>

20、[rest-client](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rest-client/rest-client)：一个 Ruby 的 HTTP 客户端库。已经有累计 10 万人在使用，该库使用方便、API 设计优雅、支持常用的 HTTP 方法、文件下载、设置代理等。每个方法基本都有示例代码：
```ruby
require 'rest_client'

RestClient.get 'http://example.com/resource'

RestClient.get 'http://example.com/resource', {:params => {:id => 50, 'foo' => 'bar'}}

RestClient.get 'https://user:password@example.com/private/resource', {:accept => :json}

RestClient.post 'http://example.com/resource', :param1 => 'one', :nested => { :param2 => 'two' }

RestClient.post "http://example.com/resource", { 'x' => 1 }.to_json, :content_type => :json, :accept => :json

RestClient.delete 'http://example.com/resource'

response = RestClient.get 'http://example.com/resource'
response.code
➔ 200
response.cookies
➔ {"Foo"=>"BAR", "QUUX"=>"QUUUUX"}
response.headers
➔ {:content_type=>"text/html; charset=utf-8", :cache_control=>"private" ...
response.to_str
➔ \n<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\"\n   \"http://www.w3.org/TR/html4/strict.dtd\">\n\n<html ....

RestClient.post( url,
  {
    :transfer => {
      :path => '/foo/bar',
      :owner => 'that_guy',
      :group => 'those_guys'
    },
     :upload => {
      :file => File.new(path, 'rb')
    }
  })
```


### Swift
21、[AppearancesSwitcher](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/BoringApp/AppearancesSwitcher)：可以在 macOS 通知中心上快速切换“亮/暗”主题的小工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/201937396.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
22、[Awesome-Multimodal-Research](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Eurus-Holmes/Awesome-Multimodal-Research)：该项目是收录多模态相关研究的一个精选列表，正在持续更新中。现实世界中的信息通常以不同的模态出现。例如，图像通常与标签和文本解释联系在一起；文本包含图像以便更清楚地表达文章的主要思想。不同的模态由迥异的统计特性刻画。例如，图像通常表示为特征提取器的像素强度或输出，而文本则表示为离散的词向量。由于不同信息资源的统计特性不同，发现不同模态之间的关系是非常重要的


23、[Non-local_pytorch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AlexHex7/Non-local_pytorch)：今天推荐的这个项目是 Nonlocal Net 的第三方实现，实现框架为 PyTorch。项目简明易懂，但是还没有在大型公开数据集上测试过性能。但是附带了一个 MNIST 的样例，可以供读者参考。Nonlocal Net 是大神 Kaiming He 研究组在图像领域引入 Attention 机制的一篇[论文](https://arxiv.org/abs/1711.07971)。Nonlocal Net 的提出，引领了一波在图像领域运用注意力机制的浪潮，最近两年该方向论文层出不穷。Facebook 也开源了一个 Nonlocal Net 在视频分类中的[项目](https://github.com/facebookresearch/video-nonlocal-net)，但是框架基于他们维护的 caffe2，读者可以根据自身实际情况进行浏览阅读


24、[numpy-cn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/teadocs/numpy-cn)：这是 NumPy 中文翻译文档。适合任何想了解学习 NumPy 的人，还可以当作手册查阅。如果你是新手朋友，推荐阅读基础文章中的：理解 Numpy、NumPy 简单入门教程、创建 Numpy 数组的不同方式，参考文章里会不定期更新国内外优秀的 Numpy 相关的内容。如果你想徒手实现神经网络可以参看 NumPy 与 神经网络、 NumPy 实现 DNC、RNN 和 LSTM 神经网络算法


25、[rasa](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/RasaHQ/rasa)：一个专门为了多轮人机对话而生的框架。主要包含 Rasa Core、Rasa NLU 两大模块，提供了对话场景、意图理解、实体抽取等功能。用户只需按照平台的语料格式构建自己的语料，便可以方便的进行意图理解和实体抽取的训练。目前使用 Rasa 平台的用户也逐渐多了起来，除了官方文档网上也容易的找到相关的项目，便于学习和上手


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/41/70908208.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
26、[awesome-adb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mzlogin/awesome-adb)：ADB 用法集合（Android Debug Bridge）


27、[git-tips](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/521xueweihan/git-tips)：Git 常用命令集合


### Book
28、[OnJava8](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lingcoder/OnJava8)：《On Java 8》中文版又名《Java 编程思想》




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub40.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub42.md">『Next』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/en/periodical'>Submit open-source project!</a> 👈<br>
</p>

## Sponsor


<table>
  <thead>
    <tr>
      <th align="center" style="width: 80px;">
        <a href="https://www.compshare.cn/?utm_term=logo&utm_campaign=hellogithub&utm_source=otherdsp&utm_medium=display&ytag=logo_hellogithub_otherdsp_display">          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/ucloud.png" width="60px"><br>
          <sub>UCloud</sub><br>
          <sub>超值的GPU云服务</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://www.upyun.com/?from=hellogithub">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/upyun.png" width="60px"><br>
          <sub>CDN</sub><br>
          <sub>开启全网加速</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://github.com/OpenIMSDK/Open-IM-Server">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/im.png" width="60px"><br>
          <sub>OpenIM</sub><br>
          <sub>开源IM力争No.1</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://apifox.cn/a103hello">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/apifox.png" width="60px"><br>
          <sub>Apifox</sub><br>
          <sub>比 Postman 更强大</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
