# 《HelloGitHub》第 55 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/55) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[htop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/htop-dev/htop)：交互式进程查看工具，可代替 top 命令。用了这库后，我基本不用 top 命令了


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/288082909.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
2、[ToolGood.Words](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/toolgood/ToolGood.Words)：一款高性能非法词、敏感词检测库。还支持繁体简体互换、获取拼音首字母、获取拼音字母、拼音模糊搜索等功能
```
string s = "中国|国人|zg人";
string test = "我是中国人";

StringSearch iwords = new StringSearch();
iwords.SetKeywords(s.Split('|'));

var b = iwords.ContainsAny(test);
Assert.AreEqual(true, b);

var f = iwords.FindFirst(test);
Assert.AreEqual("中国", f);

var all = iwords.FindAll(test);
Assert.AreEqual("中国", all[0]);
Assert.AreEqual("国人", all[1]);
Assert.AreEqual(2, all.Count);

var str = iwords.Replace(test, '*');
Assert.AreEqual("我是***", str);
```


### C++ 项目
3、[workflow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sogou/workflow)：搜狗开源的 C++ 服务器引擎。支撑搜狗几乎所有后端 C++ 在线服务，包括所有搜索服务、云输入法、广告等，每日处理超百亿请求。这是一个设计轻盈优雅的企业级程序引擎，可以满足大多数 C++ 后端开发需求


### CSS 项目
4、[flexboxfroggy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/thomaspark/flexboxfroggy)：一个帮助学习 CSS flexbox 知识的在线游戏。游戏一共 24 关，通俗易懂的解释了 flex 布局。适合初学者，并且支持中文，可以在 settings 中选择语言。[在线试玩](https://flexboxfroggy.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/46774900.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
5、[ali](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nakabonne/ali)：能够实时展示分析的压力测试工具。现在压测工具有很多，这款的亮点在于可以在终端实时展示压测过程的曲线。一条命令搞定启动：`ali 地址`


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/294836885.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[ferry](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/lanyulei/ferry)：基于 Gin + Vue + Element UI 前后端分离的工单系统。该系统是集工单统计、任务钩子、权限管理、灵活配置流程与模版等等功能， 帮助减少跨部门之间的沟通，提升工作效率与工作质量，减少不必要的工作量与人为出错率


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/279297541.png' style="max-width:80%; max-height=80%;"></img></p>

7、[go-diagrams](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/blushft/go-diagrams)：用 Go 语言画架构图的工具。想画架构图不知道用什么工具？会 Go 的小伙伴可以试试这个库，通过编写 Go 代码来绘制架构图，接口使用方便，但文档太简单了。示例代码：
```go
d, err := diagram.New(diagram.Filename("app"), diagram.Label("App"), diagram.Direction("LR"))
if err != nil {
    log.Fatal(err)
}

dns := gcp.Network.Dns(diagram.NodeLabel("DNS"))
lb := gcp.Network.LoadBalancing(diagram.NodeLabel("NLB"))
cache := gcp.Database.Memorystore(diagram.NodeLabel("Cache"))
db := gcp.Database.Sql(diagram.NodeLabel("Database"))

dc := diagram.NewGroup("GCP")
dc.NewGroup("services").
    Label("Service Layer").
    Add(
        gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 1")),
        gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 2")),
        gcp.Compute.ComputeEngine(diagram.NodeLabel("Server 3")),
    ).
    ConnectAllFrom(lb.ID(), diagram.Forward()).
    ConnectAllTo(cache.ID(), diagram.Forward())

dc.NewGroup("data").Label("Data Layer").Add(cache, db).Connect(cache, db)

d.Connect(dns, lb, diagram.Forward()).Group(dc)

if err := d.Render(); err != nil {
    log.Fatal(err)
}
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/295016801.png' style="max-width:80%; max-height=80%;"></img></p>

8、[gorched](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zladovan/gorched)：Go 语言写的终端游戏 Scorched Earth。它让我想起了“百战天虫”这款游戏，有同龄人吗？一起来回味下


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/263883501.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
9、[jmeter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/apache/jmeter)：Apache 开源的压力测试工具。提供 GUI 操作界面就是可以点点点操作，也可以写脚本提高测试的自动化，它还不局限于 Web 测试，支持更多压力测试场景。我身边 97% 从事测试相关工作的人都用过它，要不要来看看它的源码？纯 Java 实现


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/688352.png' style="max-width:80%; max-height=80%;"></img></p>

10、[mybatis-plus](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/baomidou/mybatis-plus)：一款好用的 Java 操作数据库框架。MyBatis 增强工具包，提供了一些高效、实用、快捷的功能，使用它可以有效地节省您的开发时间。比如切换数据源，只需修改配置文件
```java
List<User> userList = userMapper.selectList(
        new QueryWrapper<User>()
                .lambda()
                .ge(User::getAge, 18)
);
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/65987043.png' style="max-width:80%; max-height=80%;"></img></p>

11、[retrofit-spring-boot-starter](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/LianjiaTech/retrofit-spring-boot-starter)：一个适用于 Spring Boot 项目的轻量级 HTTP Web 框架。使用简单方便，支持接口化的方式发送 HTTP 请求。底层使用 Retrofit 实现，并支持了诸多功能特性增强，极大简化开发
```java
/**
* 定义接口
**/
@RetrofitClient(baseUrl = "${test.baseUrl}")
public interface HttpApi {

    @GET("person")
    Result<Person> getPerson(@Query("id") Long id);
}

/**
* 注入使用
**/
@Service
public class TestService {
    @Autowired
    private HttpApi httpApi;

    public void test() {
        // 通过httpApi发起http请求
    }
}
```


### JavaScript 项目
12、[AnotherRedisDesktopManager](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/qishibo/AnotherRedisDesktopManager)：一款支持多语言、多平台的 redis 桌面管理工具。对比目前其它同类型工具，它拥有更丰富的功能、更高的稳定性和性能，支持集群等功能


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/164574693.png' style="max-width:80%; max-height=80%;"></img></p>

13、[beeplay](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/watilde/beeplay)：让你可以用 JS 写一首“歌”的库。[在线尝试](http://watilde.github.io/beeplay/)，实例代码：
```javascript
var beeplay = require('beeplay')

beeplay()
  .play(null, 2)
  .play('D#5', 1/4).play('E5', 1/4).play('F#5', 1/2)
  .play('B5', 1/2).play('D#5', 1/4).play('E5', 1/4)
  .play('F#5', 1/4).play('B5', 1/4).play('C#6', 1/4).play('D#6', 1/4)
  .play('C#6', 1/4).play('A#5', 1/4).play('B5', 1/2)
  .play('F#5', 1/2).play('D#5', 1/4).play('E5', 1/4)
  .play('F#5', 1/2).play('B5', 1/2)
  .play('C#6', 1/4).play('A#5', 1/4).play('B5', 1/4).play('C#6', 1/4)
  .play('E6', 1/4).play('D#6', 1/4).play('E6', 1/4).play('C#6', 1/4);
```


14、[Bilibili-Evolved](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/the1812/Bilibili-Evolved)：哔哩哔哩增强浏览器插件。安装插件后可支持：下载视频、删除广告、夜间模式等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/141104618.png' style="max-width:80%; max-height=80%;"></img></p>

15、[vant](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/youzan/vant)：由有赞前端团队开源的移动端组件库。目前官方提供了 Vue 版本和微信小程序版本，并由社区团队维护 React 版本。有完善的中英文文档和示例，60+ 高质量组件，90%+ 单元测试覆盖率，持续维护 4 年以上


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/88717215.png' style="max-width:80%; max-height=80%;"></img></p>

16、[zooming](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/kingdido999/zooming)：纯 JS 实现支持移动端的图像缩放库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/72070328.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
17、[asciinema](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/asciinema/asciinema)：终端记录工具。忘记录屏软件吧，纯文本的录制终端操作的工具。安装简单、使用方便，且生成的记录文件极小，但需要配合 JS 文件播放


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/2823326.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[playwright-python](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/microsoft/playwright-python)：微软开源的浏览器自动化工具，可以用 Python 语言操作浏览器啦。支持 Linux、macOS、Windows 系统下的   Chromium、Firefox 和 WebKit 浏览器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/276414382.gif' style="max-width:80%; max-height=80%;"></img></p>

19、[practical-python](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/dabeaz-course/practical-python)：大佬 David Beazley 开源的 Python 免费入门级教程。他是《Python Cookbook 第三版》、《Python 参考手册》的作者，教程经过实际的教学实践、包含课后练习题。[在线学习](https://dabeaz-course.github.io/practical-python/Notes/Contents.html)，教程目录如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/266613704.png' style="max-width:80%; max-height=80%;"></img></p>

20、[redis-memory-analyzer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gamenet/redis-memory-analyzer)：Redis 实时内存分析工具。我比较好奇它是怎么实时获取 redis 中 key 的情况和信息，就看了下源码 `scanner.py` 文件。发现是采用 `scan_iter` 方法，控制扫描 key 返回的量。然后通过 `yield` 减少内存占用量，最后再加上 `register_script` 方法调用 Lua 脚本或` pipeline` 方法提高获取 key 信息的效率。分析后感觉这个工具可适用在数据量较大的情况，实时性要求在秒或者分钟级的场景下


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/50424582.png' style="max-width:80%; max-height=80%;"></img></p>

21、[wagtail](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wagtail/wagtail)：目前最强大的开源 Django CMS（内容管理系统）之一。我很少用“最”这个字眼，节省时间就聊聊它惊艳到我的点吧。首先该项目更新、迭代活跃，其次项目首页提到的功能都是免费的，没有付费解锁的骚操作。wagtail 专注于内容管理，不束缚前端实现。有趣的 StreamField 技术让你的内容变得灵活且不失结构，竟然还支持 A/B 测试，最后 Google、NASA 他们都在用这个项目


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/16479108.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
22、[stats](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/exelban/stats)：macOS 菜单栏上的监控工具。支持 CPU、GPU、内存、网络等监控和多语言


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/189285554.png' style="max-width:80%; max-height=80%;"></img></p>

### 其它
23、[keysim](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/crsnbrt/keysim)：键盘配色预览工具。“定制”这个操作一听就很贵，下单之前先这个工具先看看效果吧，避免浪费钱。[在线尝试](https://keyboardsimulator.xyz/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/294258257.png' style="max-width:80%; max-height=80%;"></img></p>

24、[socialify](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wei/socialify)：一键自动生成 GitHub 仓库头图。很多 GitHub 开源项目的作者不会用 PS，想要制作一张项目推广图就很困难，Socialify 就是帮你解决这个头疼的问题。[在线尝试](https://socialify.git.ci/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/297803332.png' style="max-width:80%; max-height=80%;"></img></p>

25、[tabler-icons](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tabler/tabler-icons)：一组免费开源的图标。目前共有 850+ 个图标，我觉得都挺好看的，您觉得呢？


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/243546335.png' style="max-width:80%; max-height=80%;"></img></p>

26、[ZY-Player](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Hunlongyu/ZY-Player)：免费无广告、高颜值+多平台的桌面视频资源播放器。功能如下：
- 全平台支持 Windows、Mac、Linux
- 视频源支持自定义, 支持导入/导出
- 播放历史, 自动跳转历史进度
- 支持精简模式, 摸鱼划水
- 显示豆瓣评分


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/224362151.png' style="max-width:80%; max-height=80%;"></img></p>

### 开源书籍
27、[Mastering_Go_ZH_CN](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hantmac/Mastering_Go_ZH_CN)：《Mastering Go》的中文翻译版《玩转 Go》。[在线阅读](https://wskdsgcf.gitbook.io/mastering-go-zh-cn/)


### 机器学习
28、[mlflow](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mlflow/mlflow)：一个简化机器学习开发的平台，支持跟踪实验、代码打包、部署模型等。它提供了一套轻量级的 API，可与目前主流机器学习 TensorFlow、PyTorch、XGBoost 等库轻松整合
```python
# 安装：$ pip install mlflow
# 启动：$ mlflow ui
# 示例代码
import mlflow
mlflow.keras.autolog()
# other keras code
...
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/136202695.png' style="max-width:80%; max-height=80%;"></img></p>

29、[snownlp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/isnowfy/snownlp)：一个 Python 写的自然语言处理库。使用简单、功能强大，支持中文分词、词性标注、情感分析等
```python
from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞')
s.words         # [u'这个', u'东西', u'真心',
                #  u'很', u'赞']
s.tags          # [(u'这个', u'r'), (u'东西', u'n'),
                #  (u'真心', u'd'), (u'很', u'd'),
                #  (u'赞', u'Vg')]
s.sentiments    # 0.9769663402895832 positive的概率
```


30、[video-object-removal](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zllrunning/video-object-removal)：通过 Pytorch 实现绘制一个边界框，即可删除视频中要删除的对象。下图是演示操作，框中红色是抹掉的部分，删除前后的效果对比图可进到项目首页查看


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/55/194876821.gif' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub54.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub56.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/55'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
