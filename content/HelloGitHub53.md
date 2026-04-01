# 《HelloGitHub》第 53 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/53) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[baulk](https://hellogithub.com/periodical/statistics/click?target=https://github.com/baulk/baulk)：一个用 C 编写的极简 Windows 包管理器。易于使用、免安装、不修改系统环境变量，能够和 Windows Terminal 集成、添加到右键菜单。可以说是一个精简版的 Scoop


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/245962600.png' style="max-width:80%; max-height=80%;"></img></p>

2、[LCUI](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lc-soft/LCUI)：一个使用 C 开发的图形界面开发库。可借助 XML 和 CSS 构建简单的跨平台桌面应用，提供与网页类似的开发体验。因此，你可以使用它轻松做出十分漂亮的界面。与 Electron 不同，它只是一个应用了部分 Web 技术的传统 GUI 开发库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/5293802.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[Windows-Auto-Night-Mode](https://hellogithub.com/periodical/statistics/click?target=https://github.com/AutoDarkMode/Windows-Auto-Night-Mode)：设置定时自动切换 Windows 10 深色和浅色主题的工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/158025849.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
4、[flameshot](https://hellogithub.com/periodical/statistics/click?target=https://github.com/flameshot-org/flameshot)：操作简单、功能强大的截图工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/90902132.gif' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
5、[css-sweeper](https://hellogithub.com/periodical/statistics/click?target=https://github.com/propjockey/css-sweeper)：一个只用 HTML 和 CSS 实现的扫雷游戏。[在线试玩](https://propjockey.github.io/css-sweeper/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/281741508.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[papercss](https://hellogithub.com/periodical/statistics/click?target=https://github.com/papercss/papercss)：手绘风格的 CSS 库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/101221093.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
7、[ginrpc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xxjwxc/ginrpc)：简化 go-gin 框架注册路由方式，自动生成 Swagger/Markdown 文档。示例代码：
```go
type ReqTest struct {
	UserName    string `json:"user_name" binding:"required"` // 带校验方式
}

type Hello struct {
}

// Hello [grpc-go](https://github.com/grpc/grpc-go) 模式
// @Router /hello_ruter [post,get]
func (s *Hello) Hello(c *gin.Context, req ReqTest) (*ReqTest, error) {
	fmt.Println(req)
	return &req,nil
}

func main() {
	base := ginrpc.New(ginrpc.WithGroup("xxjwxc"))
	router := gin.Default()
	base.Register(router, new(Hello)) // 对象注册 like(go-micro)
	router.Run(":8080")
}
```


8、[go-internals](https://hellogithub.com/periodical/statistics/click?target=https://github.com/teh-cmc/go-internals)：关于 Go 程序设计语言内部实现原理的讲解。[中文翻译](https://github.com/go-internals-cn/go-internals)


9、[LeetCode-Go](https://hellogithub.com/periodical/statistics/click?target=https://github.com/halfrost/LeetCode-Go)：《LeetCode Cookbook》是帮助开发者在 LeetCode 上做题，提供解题思路和代码的项目。目前已经收录了 500+ 道题的题解和代码，代码都是 runtime beats 100%，代码全部都是用 Go 语言实现。[在线阅读](https://books.halfrost.com/leetcode)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/97533102.png' style="max-width:80%; max-height=80%;"></img></p>

10、[livego](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gwuhaolin/livego)：基于 Go 实现的直播服务项目


### Java 项目
11、[CalendarView](https://hellogithub.com/periodical/statistics/click?target=https://github.com/huanghaibin-dev/CalendarView)：一个优雅强大的 Android 日历控件，支持周视图、自定义周起始等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/84631679.png' style="max-width:80%; max-height=80%;"></img></p>

12、[D8gerAutoCode](https://hellogithub.com/periodical/statistics/click?target=https://github.com/caofanCPU/D8gerAutoCode)：IDEA Java 代码自动生成插件。支持自动生成单表增删改查、分页、注释等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/229872249.jpeg' style="max-width:80%; max-height=80%;"></img></p>

13、[java8-tutorial](https://hellogithub.com/periodical/statistics/click?target=https://github.com/winterbe/java8-tutorial)：手把手教你 Java8 的语言特性。项目中还更新了 Java11 的新特性


14、[tutorials](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eugenp/tutorials)：该项目是 Spring 框架下的小型、单一功能的教程和示例代码集合。主要是 Spring、Spring Boot、Spring Security 等方面


### JavaScript 项目
15、[genal-chat](https://hellogithub.com/periodical/statistics/click?target=https://github.com/genalhuang/genal-chat)：适合前端新手学习的‘星空’聊天室项目。采用 Vue + socket.io 结合 TypeScript 语法构建，界面炫酷、良好的代码规范、支持群聊和好友搜索等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/274610956.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[jizhi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/liminalpurr/jizhi)：中国风新标签页的 Chrome/Firefox 插件。它将在新标签页上展示中国传统色的层叠波浪动画效果，搭配经典诗词


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/173278813.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[MazeBattles.com](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HenryDavidZhu/MazeBattles.com)：使用 Node.js 和 Socket.io 实现的在线迷宫游戏。入口在左上角出口在右下角，通过 [a][w][s][d] 按键移动位置。支持多人和单人两种模式，点击 “Show Solution” 可展示迷宫的解（BFS 算法实现）。[在线试玩](http://www.mazebattles.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/152203485.png' style="max-width:80%; max-height=80%;"></img></p>

18、[remote-browser](https://hellogithub.com/periodical/statistics/click?target=https://github.com/intoli/remote-browser)：实现用 JavaScript 语言控制 Chrome 和 Firefox 浏览器的库。可轻松实现自动化测试、抓取数据等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/124411852.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[star-history](https://hellogithub.com/periodical/statistics/click?target=https://github.com/star-history/star-history)：展示 GitHub 项目 Star 历史的在线工具。支持多个项目展示在同一个图表上，效果如下图：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/42976210.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
20、[altair](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vega/altair)：强大的数据可视化 Python 库。支持多种数据展示方式、接口简单、效果炫酷，示例代码和效果如下：
```python
import altair as alt
from vega_datasets import data

source = data.cars()
brush = alt.selection(type='interval')
points = alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin',
    color='Origin',
    x='count(Origin)'
).transform_filter(
    brush
)

points & bars
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/42757577.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[handcalcs](https://hellogithub.com/periodical/statistics/click?target=https://github.com/connorferster/handcalcs)：通过简单的 Python 代码，生成复杂公式的工具。还记得写论文推算算法的时候，被一行行公式支配的恐惧吗？该库可以将 Python 写的公式，展示为 LaTeX 格式，效果如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/241504436.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[QuickCut](https://hellogithub.com/periodical/statistics/click?target=https://github.com/HaujetZhao/QuickCut)：一款轻量、好用的开源视频处理工具。它是基于 PyQt5 开发的桌面工具，用于满足非专业用户的视频处理需求：压缩视频、转码视频、倒放视频、合并片段、根据字幕裁切片段、自动配字幕、自动剪辑等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/282413176.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
23、[lottie-ios](https://hellogithub.com/periodical/statistics/click?target=https://github.com/airbnb/lottie-ios)：Airbnb 开源的快速实现 APP 动画的三方库。还有支持 [Android](https://github.com/airbnb/lottie-android)、[React Native](https://github.com/react-native-community/lottie-react-native)、[Web](https://github.com/airbnb/lottie-web)、[Windows](https://github.com/windows-toolkit/Lottie-Windows) 等平台，动画效果如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/70198664.gif' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
24、[cnn-convoluter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pwwang/cnn-convoluter)：一个支持交互的展示卷积过程的可视化工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/282327806.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[Never-Blink](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ByronHsu/Never-Blink)：谁先眨眼谁就输了的游戏。使用 React + Flask + Dlib 技术实现的“眨眼就输了”在线游戏，虽然是个 demo 级别的项目，但是很有意思可以在本地运行起来找朋友一起玩一下


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/190750590.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[waifu2x](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nagadomi/waifu2x)：基于机器学习把图片、照片变得高清。该项目使用卷积神经网络对图片进行 1-2 倍的无损放大操作，支持降噪保证图片质量。[在线尝试](http://waifu2x.udp.jp/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/35756351.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
27、[Algorithm-Guide](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Xunzhuo/Algorithm-Guide)：系统性学习算法与数据结构的资料集合


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/259780361.jpg' style="max-width:80%; max-height=80%;"></img></p>

28、[first-contributions](https://hellogithub.com/periodical/statistics/click?target=https://github.com/firstcontributions/first-contributions)：手把手教你如何在 GitHub 第一次贡献代码的教程。支持多种语言，[中文](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.chs.md)


29、[leek-fund](https://hellogithub.com/periodical/statistics/click?target=https://github.com/LeekHub/leek-fund)：在 VSCode 中看股票和基金实时数据的插件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/284397976.png' style="max-width:80%; max-height=80%;"></img></p>

30、[math-as-code](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Experience-Monks/math-as-code)：这是一份通过对比数学符号和 JavaScript 代码来帮助开发者更容易了解数学符号的项目


31、[PowerToys](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/PowerToys)：微软开源的 Windows 系统下强大的辅助工具。比如：窗口管理、批量图片处理、改键工具等，下图是屏幕颜色选择工具


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/184456251.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
32、[BuildYourOwnLisp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/orangeduck/BuildYourOwnLisp)：该书教你用 C 语言实现自己的 Lisp 语言。用 1000 多行实现一个小但功能齐全的 Lisp 语言，这里有份中文翻译版本，但是没有翻译完[点击阅读](https://ksco.gitbooks.io/build-your-own-lisp/content/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/53/18437816.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub52.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub54.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/53'>这里</a>。
</p>

## 赞助


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
        <a href="https://www.qiniu.com/products/ai-token-api?utm_source=hello">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/qiniu.jpg" width="60px"><br>
          <sub>七牛云</sub><br>
          <sub>百万 Token 免费体验</sub>
        </a>
      </th>
      <th align="center" style="width: 80px;">
        <a href="https://ofox.ai/zh?utm_source=github&utm_medium=hellogithub&utm_campaign=sponsor">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/0foxai.png" width="60px"><br>
          <sub>OfoxAI</sub><br>
          <sub>100+ 模型官方直连不掉线</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
