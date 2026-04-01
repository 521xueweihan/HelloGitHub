# 《HelloGitHub》第 21 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/21) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[kcp](https://hellogithub.com/periodical/statistics/click?target=https://github.com/skywind3000/kcp)：纯算法实现的快速可靠协议。能以比 TCP 浪费 10%-20% 的带宽为代价，换取平均延迟降低 30%-40%，且最大延迟降低 3 倍的传输效果


### C++ 项目
2、[OpenCC](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BYVoid/OpenCC)：中文简繁转化开源项目，[在线尝试](http://opencc.byvoid.com/)
- 严格区分 “一简对多繁” 和 “一简对多异”
- 完全兼容异体字，可以实现动态替换
- 严格审校一简对多繁词条，原则为 “能分则不合”
- 支持异体字和地区习惯用词转换，如 “裏” “裡”、“鼠標” “滑鼠”
- 词库和函数库完全分离，可以自由修改、导入、扩展
- 支持 C++、Python、PHP、Java、Ruby、Node.js 等
- 兼容 Windows、Linux、Mac 平台


### Go 项目
3、[mattermost](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mattermost/mattermost)：采用 Go 语言开发的团队通讯服务项目，可用于自行搭建服务。为团队带来跨 PC 和移动设备的消息收发、文件分享，搜索等功能的通讯服务平台


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/37448451.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
4、[android-material-design-icon-generator-plugin](https://hellogithub.com/periodical/statistics/click?target=https://github.com/konifar/android-material-design-icon-generator-plugin)：IntelliJ／Android Studio 生成、设计 icon 的插件，安装简单使用方便。如下图所示：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/28638448.gif' style="max-width:80%; max-height=80%;"></img></p>

5、[blade](https://hellogithub.com/periodical/statistics/click?target=https://github.com/lets-blade/blade)：轻量级、高效、简洁优雅的 Java Web 框架，致力于为个人开发者更快捷地开发 Web 应用提供便利。详尽的[中文文档](https://github.com/lets-blade/blade/blob/master/README_CN.md)及[入门视频](https://www.bilibili.com/video/av15572599/)。示例代码：
```java
public static void main(String[] args) {
    Blade.me().get("/", (req, res) -> {
        res.text("Hello Blade");
    }).start();
}
```


6、[canal](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alibaba/canal)：MySQL 数据库 binlog 的增量订阅、消费组件。模拟 MySQL salve 方式，实现 MySQL 的主从同步，同时加入了增量日志解析等功能。MySQL 原始主备机制，示意图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/7587038.jpeg' style="max-width:80%; max-height=80%;"></img></p>

7、[grain](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dianbaer/grain)：极简的、组件式的 RPC 框架，灵活且适合学习。包含系统通用多线程模型与消息通讯、多对多关系的分布式锁、基于系统通用多线程模型的 Websocket 框架、支持行级锁的多线程锁等组件


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/91581792.png' style="max-width:80%; max-height=80%;"></img></p>

8、[RxGalleryFinal](https://hellogithub.com/periodical/statistics/click?target=https://github.com/FinalTeam/RxGalleryFinal)：Android 图片、视频文件选择器，支持多选、单选、拍摄和裁剪等


### JavaScript 项目
9、[anyupload](https://hellogithub.com/periodical/statistics/click?target=https://github.com/dianbaer/anyupload)：该项目是一款上传插件，使用方便、简单。支持多文件上传、上传速率动态控制、真实进度监控 kb/s、分块生成 MD5、分块上传、MD5 校验、暂停、取消等功能。[在线体验](https://www.threecss.com/AnyUploadClient/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/107945228.png' style="max-width:80%; max-height=80%;"></img></p>

10、[git-point](https://hellogithub.com/periodical/statistics/click?target=https://github.com/gitpoint/git-point)：基于 React Native 开发的非官方开源 GitHub 客户端，功能丰富包含查看项目和用户信息、接收通知、管理
 Issues 和 PR。支持 Android、iOS，选择对应的客户端[下载使用](https://github.com/gitpoint/git-point/releases)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/86202845.png' style="max-width:80%; max-height=80%;"></img></p>

11、[numeric-keyboard](https://hellogithub.com/periodical/statistics/click?target=https://github.com/viclm/numeric-keyboard)：手机数字键盘，包含一个纯键盘 UI 和输入框套件。有纯 JavaScript、React、Vue 三个版本


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/106380954.png' style="max-width:80%; max-height=80%;"></img></p>

12、[webster](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zhuyingda/webster)：一款可以抓取网页中 AJAX 异步内容的分布式爬虫框架


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/109503867.png' style="max-width:80%; max-height=80%;"></img></p>

13、[wepy](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Tencent/wepy)：微信官方的开源项目，该项目是为了让小程序支持组件化开发的框架，特征如下：
- 类 Vue 开发风格
- 支持自定义组件开发
- 支持引入 NPM 包
- 等等


### Kotlin 项目
14、[profile-summary-for-github](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tipsy/profile-summary-for-github)：GitHub 账号数据可视化服务，很新颖地增加了 star 后可见（回复可见）😄


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/113752225.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
15、[jieba](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fxsjy/jieba)：强大的 Python 分词库，拿来直接用就好。示例代码如下：
```python
# encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

【全模式】: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学

【精确模式】: 我/ 来到/ 北京/ 清华大学

【新词识别】：他, 来到, 了, 网易, 杭研, 大厦    (此处，“杭研”并没有在词典中，但是也被Viterbi算法识别出来了)

【搜索引擎模式】： 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造
```


16、[pydu](https://hellogithub.com/periodical/statistics/click?target=https://github.com/flaggo/pydu)：该库将平时常用的数据结构和工具都收录其中，可供日常开发的使用，同时方便学习与借鉴，丰富的[文档](http://pydu.readthedocs.io/zh/latest/)能帮助新手更好的理解和使用它。这些实用的模块都是来自于开源项目和贡献者们的智慧，快来加入到这个项目中，让它变得更加实用和丰富


17、[thefuck](https://hellogithub.com/periodical/statistics/click?target=https://github.com/nvbn/thefuck)：在 Linux 命令行中，当你输入的命令有错误后，直接输入 `fuck` 就可以自动执行修复后的命令，效果图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/33614304.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[youtube-dl](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ytdl-org/youtube-dl)：强大的视频下载工具，支持几百个国内外主流视频网站。正如名字一样，最初是为了下载 youtube 上的视频而开发的。如果有国外服务器的朋友，可以充分利用这个工具，下载 youtube 上的视频，速度不要太爽。下面介绍安装、下载视频等命令：
```
# 1. 安装命令：sudo pip install youtube-dl
Installing collected packages: youtube-dl
Successfully installed youtube-dl-2017.12.14

# 2. 查看 URL 支持格式：youtube-dl --list-formats URL
format code  extension  resolution note
134          mp4        450x360    DASH video  449k , avc1.4d4015, 25fps, video only
17           3gp        176x144    small , mp4v.20.3, mp4a.40.2@ 24k
36           3gp        300x240    small , mp4v.20.3, mp4a.40.2
18           mp4        450x360    medium , avc1.42001E, mp4a.40.2@ 96k
43           webm       640x360    medium , vp8.0, vorbis@128k (best)

# 3. 选择格式下载视频：youtube-dl -f 18 URL （18为mp4 450x360格式）
[youtube:playlist] Downloading playlist PLF90USSyuoYzPhhFG7XFBRn63Zvs--lNP - add --no-playlist to just download video JyLducMVYVg
[youtube:playlist] PLF90USSyuoYzPhhFG7XFBRn63Zvs--lNP: Downloading webpage
[download] Downloading playlist: 情满四合院完整版
[youtube:playlist] playlist 情满四合院完整版: Downloading 42 videos
[download] Downloading video 1 of 42
...

# 4. 下载完成后，最后使用 https://github.com/houtianze/bypy 库把下载的视频同步到百度网盘上
```


### 其它
19、[android-training-course-in-chinese](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kesenhoo/android-training-course-in-chinese)：Android 官方培训课程中文版，[在线阅读](http://hukai.me/android-training-course-in-chinese/index.html)


20、[git-flight-rules](https://hellogithub.com/periodical/statistics/click?target=https://github.com/k88hudson/git-flight-rules)：Git 飞行规则，所谓飞行规则就是特定场景的非常详细的标准处理流程。该项目记录了使用 Git 过程中，如果遇到问题的解决办法和步骤，[中文](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)


21、[go-advice](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cristaloleg/go-advice)：Go 建议[中文版](https://github.com/cristaloleg/go-advices/blob/master/README_ZH.md)


22、[hello-comic](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pipiliang/hello-comic)：程序员有关的漫画的集合，希望有更多的人可以加入该项目分享有意思程序员漫画


23、[vscode](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/vscode)：Visual Studio Code 是微软出品的支持多平台的开源编辑器，体积小、功能丰富、性能强大、扩展性很强。我是用着挺爽，写些代码片段、文章、文档开箱即用。个人感觉编写中型项目、代码调试的话还是 IDE 更方便些，总之推荐下载和使用。[下载地址](https://code.visualstudio.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/21/41881900.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
24、[pydata-notebook](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BrambleXu/pydata-notebook)：《利用Python进行数据分析 2017 第二版》中文翻译笔记




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub20.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub22.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/21'>这里</a>。
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
