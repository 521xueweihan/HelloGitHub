# 《HelloGitHub》第 119 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/119) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C 项目
1、[voidImageViewer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/voidtools/voidImageViewer)：比图片还小的免费看图工具。这是一款用 C 语言编写的 Windows 轻量级图片查看工具，让你几乎感受不到等待。它体积小、启动快，拥有极快的图片加载和切换速度，支持 JPG、PNG、WEBP、BMP、GIF、ICO、TIF 等主流图片格式。来自 [@刘睿华](https://hellogithub.com/user/TJ65FfbQU09PLHM) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/100767968.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[Zen-C](https://hellogithub.com/periodical/statistics/click?target=https://github.com/z-libs/Zen-C)：像高级语言一样写 C 代码。这是一个现代系统编程语言，写起来像高级语言又能像 C 语言一样运行。它通过编译生成 GNU C/C11 代码，兼容 C ABI（应用程序二进制接口），支持无缝集成到现有的 C 语言生态，在保持 C 语言运行效率的基础上，提升开发体验。
```
import "std/net/tcp.zc"

fn main() {
    "Echo Server listening on :8080";
    let listener = TcpListener::bind("127.0.0.1", 8080).unwrap();

    loop {
        // Accept new connections
        let stream = listener.accept().unwrap();
        let buf: char[1024];
        
        while true {
            let n = stream.read(&buf[0], 1024).unwrap();
            if n == 0 { break; }
            stream.write(&buf[0], n);
        }
    }
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1132223692.png' style="max-width:80%; max-height=80%;"></img></p>

### C# 项目
3、[ParquetViewer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mukunku/ParquetViewer)：快速查看 Parquet 文件的桌面应用。这是一款专为 Windows 用户设计的 Parquet 文件查看与查询工具，支持浏览文件元数据、执行简单的 SQL 查询、打开单个文件或文件夹内的多个文件。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/135630194.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Winhance](https://hellogithub.com/periodical/statistics/click?target=https://github.com/memstechtips/Winhance)：开箱即用的 Windows 系统优化工具。这是一款基于 C# 开发的 Windows 10/11 一站式系统优化工具，无需重装系统即可定制、精简系统。它集成了软件管理、系统优化、界面定制等功能，支持一键卸载预装应用、性能调优和界面美化，适用于重装系统或新机初始化。来自 [@只是肚子太寂寞](https://hellogithub.com/user/TXJgfoRNWa8vmF4) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/916105685.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
5、[MFCMouseEffect](https://hellogithub.com/periodical/statistics/click?target=https://github.com/sqmw/MFCMouseEffect)：Windows 鼠标特效增强工具。这是一款轻量级的 Windows 桌面鼠标/光标特效工具，支持点击波纹、粒子拖尾、悬停发光、漂浮文字等多种鼠标特效。来自 [@sqmw](https://hellogithub.com/user/5Dle7yOkCgFSUVj) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1139933103.png' style="max-width:80%; max-height=80%;"></img></p>

6、[zvec](https://hellogithub.com/periodical/statistics/click?target=https://github.com/alibaba/zvec)：轻量级进程内向量数据库。该项目是阿里开源的进程内向量数据库，无需独立部署即可直接使用。它基于 Proxima 引擎构建，提供本地化、低延迟的向量数据管理和语义检索能力，支持混合搜索、数据持久化、重排序等功能。
```python
import zvec

# Define collection schema
schema = zvec.CollectionSchema(
    name="example",
    vectors=zvec.VectorSchema("embedding", zvec.DataType.VECTOR_FP32, 4),
)

# Create collection
collection = zvec.create_and_open(path="./zvec_example", schema=schema)

# Insert documents
collection.insert([
    zvec.Doc(id="doc_1", vectors={"embedding": [0.1, 0.2, 0.3, 0.4]}),
    zvec.Doc(id="doc_2", vectors={"embedding": [0.2, 0.3, 0.4, 0.1]}),
])

# Search by vector similarity
results = collection.query(
    zvec.VectorQuery("embedding", vector=[0.4, 0.3, 0.3, 0.1]),
    topk=10
)

# Results: list of {'id': str, 'score': float, ...}, sorted by relevance
print(results)
```

### Go 项目
7、[lazyssh](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Adembc/lazyssh)：终端交互式 SSH 管理工具。这是一款 Go 写的终端交互式 SSH 管理工具，基于 OpenSSH 执行连接安全可靠。它提供直观易用的终端界面，支持模糊搜索、排序、Ping 检查和一键连接等功能。来自 [@孤胆枪手](https://hellogithub.com/user/i1wAIyo6P3NXkxm) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1037246832.png' style="max-width:80%; max-height=80%;"></img></p>

8、[sql-tap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mickamy/sql-tap)：实时监控 SQL 流量的工具。这是一款基于 Go 开发的实时 SQL 流量监控工具，无需修改代码即可使用。它作为代理部署在应用与数据库之间，通过解析数据库 wire 协议捕获所有查询，提供 TUI 和 Web 两种使用方式，支持 PostgreSQL、MySQL 和 TiDB 数据库。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1157577714.png' style="max-width:80%; max-height=80%;"></img></p>

9、[Surge](https://hellogithub.com/periodical/statistics/click?target=https://github.com/surge-downloader/Surge)：终端里的高速下载工具。这是一款采用 Go 语言开发的终端下载工具，可将下载文件自动切分为多个数据块并行下载，支持从多个镜像源下载、自动故障转移、顺序下载模式等功能。来自 [@Meet Mehta](https://hellogithub.com/user/AB7OfuhyiEqmkZv) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1085475816.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[task](https://hellogithub.com/periodical/statistics/click?target=https://github.com/go-task/task)：告别 Makefile 复杂语法的构建工具。这是一款基于 Go 语言开发的现代化构建工具，可作为 GNU Make 的替代品。它采用更简单的 YAML 语法，支持跨平台、依赖管理、并行执行和条件触发等功能，适用于项目构建、开发环境管理和 CI/CD 集成。来自 [@DeShuiYu](https://hellogithub.com/user/ZWJkOqsvYbPgD8p) 的分享

### Java 项目
11、[jquick-curl](https://hellogithub.com/periodical/statistics/click?target=https://github.com/paohaijiao/jquick-curl)：直接运行 curl 命令的 Java 库。这是一款轻量级 HTTP 客户端 Java 库，可直接将 curl 命令转换为 Java 中可执行的 HTTP 请求逻辑，无需手动改写代码。适用于从 Chrome 浏览器开发者工具、API 文档等复制 curl 命令后，快速集成到 Java 项目中。来自 [@paohaijiao](https://hellogithub.com/user/iIaNjn0mSdwx6gv) 的分享
```java
import java.util.List;
// 示例UserService接口定义
public interface UserService {

    /**
     * 获取所有用户
     * @param req 请求参数载体
     * @return 所有用户列表
     */
    @JCurlCommand("curl -X GET --location 'http://localhost:8080/api/users/all'")
    List<JUser> all(JQuickCurlReq req);

    /**
     * 根据ID获取单个用户
     * @param req 请求参数载体
     * @return 单个用户信息
     */
    @JCurlCommand("curl -X GET http://localhost:8080/api/users/1")
    JUser getUserById(JQuickCurlReq req);

    /**
     * 创建新用户（POST请求）
     * @param req 请求参数载体
     * @return 创建后的用户信息
     */
    @JCurlCommand("curl -X POST http://localhost:8080/api/users/createUser \\\n" +
            "-H \"Content-Type: application/json\" \\\n" +
            "-d '{\"name\":\"John Doe\",\"email\":\"john@example.com\"}'")
    JUser users(JQuickCurlReq req);
}
```

12、[pokemon-tbje](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zachMahan64/pokemon-tbje)：Java 写的文字版宠物小精灵游戏。这是一款基于 Java 游戏开发框架 LibGDX 构建的终端文字版宠物小精灵游戏，通过 Unicode 盲文字符作为像素点渲染画面，支持对战机制和完整的单人剧情。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/968848455.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
13、[cloud-mail](https://hellogithub.com/periodical/statistics/click?target=https://github.com/maillab/cloud-mail)：基于 Cloudflare 的轻量级邮箱服务。这是一款基于 Cloudflare 的轻量级、响应式邮箱服务，只需一个域名即可在 Cloudflare Workers 上低成本快速搭建邮件服务平台，支持群发、收发附件和人机验证等功能。来自 [@eoao](https://hellogithub.com/user/Yi9MEGzFwLfdPHb) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/971999086.png' style="max-width:80%; max-height=80%;"></img></p>

14、[folio-2025](https://hellogithub.com/periodical/statistics/click?target=https://github.com/brunosimon/folio-2025)：当个人主页变成 3D 游戏。该项目是前端大神 Bruno Simon 的开源新作，他将个人主页打造成一个可以驾车探索的沉浸式 3D 开放世界游戏，融入了物理模拟、天气系统、植被、昼夜交替等元素。来自 [@卷卷卷](https://hellogithub.com/user/tDk0fh9eI4PxVwn) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/871518808.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[hanzi-writer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/chanind/hanzi-writer)：让汉字在网页上动起来。这是一款用于展示汉字笔画顺序和交互式书写练习的 JavaScript 库，支持简/繁体字、调节播放速度、循环方式、实时检查笔画正确性等功能。
```javascript
var writer = HanziWriter.create('character-target-div', '你好', {
  width: 100,
  height: 100,
  padding: 5,
  showOutline: true
});
document.getElementById('animate-button').addEventListener('click', function() {
  writer.animateCharacter();
});
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/24015646.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[streamdown](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vercel/streamdown)：专为流式输出而生的 Markdown 渲染组件。该项目是专为流式传输场景设计的 React Markdown 组件，可用于解决大语言模型逐字输出 Markdown 内容时出现的闪烁、渲染错误和安全等问题。
```typescript
export default function Chat() {
  const { messages, status } = useChat();

  return (
    <div>
      {messages.map(message => (
        <div key={message.id}>
          {message.role === 'user' ? 'User: ' : 'AI: '}
          {message.parts.map((part, index) =>
            part.type === 'text' ? (
              <Streamdown
                key={index}
                animated
                plugins={{ code, mermaid, math, cjk }}
                isAnimating={status === 'streaming'}
              >
                {part.text}
              </Streamdown>
            ) : null,
          )}
        </div>
      ))}
    </div>
  );
}
```

17、[taoyuan](https://hellogithub.com/periodical/statistics/click?target=https://github.com/setube/taoyuan)：文字版田园模拟经营游戏。这是一款名为《桃源乡》的纯前端文字版田园模拟经营游戏，灵感来自《星露谷物语》。它采用像素与中国风相结合的视觉设计，玩家可以按照自己的想法经营农场，体验种植、钓鱼、烹饪、畜牧养殖和矿洞探险等多种玩法。来自 [@谦君](https://hellogithub.com/user/OCYdts5lPczHag4) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1151925632.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin 项目
18、[Compass](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Kr0oked/Compass)：极简的 Android 指南针。这是一款基于 Kotlin 开发的 Android 指南针应用，界面简洁、体积小、无广告，支持实时显示基本方位、传感器状态和震动反馈。来自 [@ewiro](https://hellogithub.com/user/iItGgWoJjnLsr0Y) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/182394441.png' style="max-width:80%; max-height=80%;"></img></p>

19、[PixelPlayer](https://hellogithub.com/periodical/statistics/click?target=https://github.com/theovilardo/PixelPlayer)：高颜值多功能的 Android 音乐播放器。这是一款本地优先、注重隐私的 Android 音乐播放器，拥有美观的 Material You 动态主题 ，界面可随专辑封面或手机壁纸自动变化，支持歌词显示、自定义歌曲过渡、桌面小部件、投屏播放、听歌统计等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/987110251.png' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
20、[freemocap](https://hellogithub.com/periodical/statistics/click?target=https://github.com/freemocap/freemocap)：免费开源的动作捕捉系统。这是一款基于 Python 开发的动作捕捉系统，无需标记点和 GPU，仅用普通摄像头即可实现全身 3D 动作数据采集，适用于动画制作、游戏开发和教育等场景。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/357362803.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[gh-space-shooter](https://hellogithub.com/periodical/statistics/click?target=https://github.com/czl9707/gh-space-shooter)：基于 GitHub 贡献生成太空射击动图。该项目能够根据用户的 GitHub 贡献图生成太空射击游戏风格的动图，支持自定义动图帧率以及通过 GitHub Actions 定时生成并自动更新到个人主页。来自 [@Zane ChenPEc8I](https://hellogithub.com/user/wSHB9xmqPdsnu4C) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1126431904.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[great_expectations](https://hellogithub.com/periodical/statistics/click?target=https://github.com/great-expectations/great_expectations)：像写单元测试一样验证数据质量。这是一个基于 Python 的数据质量验证框架，可通过简洁的代码定义验证规则，就像为数据编写单元测试，支持 pandas、Spark 和 SQLAlchemy 等多种数据接入方式。来自 [@Ashraf Haress](https://hellogithub.com/user/6erlUGDQfB4qAPo) 的分享
```python
import great_expectations as gx

context = gx.get_context()

file_path = "./data/folder_with_data/yellow_tripdata_sample_2019-01.csv"
batch = context.data_sources.pandas_default.read_csv(file_path)

expectation = gx.expectations.ExpectColumnMaxToBeBetween(
    column="passenger_count", min_value=1, max_value=6
)
validation_results = batch.validate(expectation)
print(validation_results)
```

23、[InvenTree](https://hellogithub.com/periodical/statistics/click?target=https://github.com/inventree/InvenTree)：开源的库存管理系统。这是一款基于 Python 和 Django 开发的库存管理平台，内置 Web 管理界面和 REST API 服务，支持扫码入库、零件追踪、物料清单和供应商管理等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/85894461.png' style="max-width:80%; max-height=80%;"></img></p>

24、[pycparser](https://hellogithub.com/periodical/statistics/click?target=https://github.com/eliben/pycparser)：纯 Python 实现的 C 语言解析器。这是一个纯 Python 实现、无第三方依赖的 C 语言解析器，可将 C 代码解析为抽象语法树，从而实现用 Python 轻松分析与操作 C 语言代码，支持完整的 C99 标准和部分 C11 特性。

### Rust 项目
25、[FaceWinUnlock-Tauri](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zs1083339604/FaceWinUnlock-Tauri)：开源的 Windows 人脸识别解锁工具。这是一款基于 Tauri 框架开发的 Windows 面容识别解锁增强工具，为没有红外摄像头的普通 Windows 电脑提供类似 Windows Hello 的刷脸解锁体验。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1126550681.png' style="max-width:80%; max-height=80%;"></img></p>

26、[monty](https://hellogithub.com/periodical/statistics/click?target=https://github.com/pydantic/monty)：启动速度极快的 Python 解释器。该项目是 Pydantic 团队用 Rust 开发的 Python 解释器，具有启动快、安全隔离、状态快照等特点，适合在 AI Agent 中运行大模型生成的 Python 代码。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/646426100.png' style="max-width:80%; max-height=80%;"></img></p>

27、[weathr](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Veirt/weathr)：Rust 写的实时 ASCII 天气动画。这是一款用 Rust 编写的终端查看天气工具，可通过 ASCII 动画实时展示当前天气情况，支持下雨、下雪、闪电和昼夜变化等动画效果。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1152969678.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
28、[AppPorts](https://hellogithub.com/periodical/statistics/click?target=https://github.com/wzh4869/AppPorts)：一键将 macOS 应用迁移到外部硬盘。该项目通过 Contents 链接的方式，将 macOS 应用迁移到外部存储设备（移动硬盘、SD 卡或 NAS），并在原位置保留应用入口，让用户能够像之前一样启动应用，在不影响使用的前提下释放宝贵的 macOS 存储空间。来自 [@Zehua Wang](https://hellogithub.com/user/SjNchy8nMfGgUlx) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1099232644.png' style="max-width:80%; max-height=80%;"></img></p>

29、[DebugSwift](https://hellogithub.com/periodical/statistics/click?target=https://github.com/DebugSwift/DebugSwift)：开源的 iOS 移动端调试工具箱。这是一款专为 iOS 应用开发设计的端侧调试工具包，仅需几行代码即可在应用中启动调试面板，支持查看网络流量、性能分析、界面调试和文件浏览等功能。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/731804628.png' style="max-width:80%; max-height=80%;"></img></p>

30、[dorso](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tldev/dorso)：矫正坐姿的 macOS 应用。这是一款用 Swift 开发的 macOS 坐姿监测应用，可通过摄像头或 AirPods 实时检测坐姿。当发现用户驼背或前倾时，应用会逐渐模糊屏幕，从而提醒用户及时纠正坐姿。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1141375692.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
31、[daily_stock_analysis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ZhuLinsen/daily_stock_analysis)：基于 LLM 的智能股票分析系统。这是一个由 LLM 驱动的智能股票分析工具，支持 A 股、港股和美股的每日自动分析与推送。它通过 AkShare、Tushare、YFinance 等数据源获取实时行情，并借助 DeepSeek 等大模型 API 服务，对自选股票进行多维度分析（技术面、筹码分布、舆情），生成决策仪表盘，支持 GitHub Actions 定时执行（无需服务器）或 Docker 一键部署。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1131513930.png' style="max-width:80%; max-height=80%;"></img></p>

32、[learn-claude-code](https://hellogithub.com/periodical/statistics/click?target=https://github.com/shareAI-lab/learn-claude-code)：从零开始动手实现 AI Agent。该项目是讲解如何从零构建类似 Claude Code 的 AI Agent 工具，共计 12 节课，每节课都有一个可运行的 Python 文件。内容从最基础的 Agent 循环，逐步叠加工具调用、任务规划、子智能体、上下文压缩、多智能体协作和自主执行等功能，最终构建出一个完整的 AI Agent 系统。来自 [@喜BFoCE](https://hellogithub.com/user/Fzr3vHc5AxqYUVj) 的分享
```python
def agent_loop(messages):
    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM,
            messages=messages, tools=TOOLS,
        )
        messages.append({"role": "assistant",
                         "content": response.content})

        if response.stop_reason != "tool_use":
            return

        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = TOOL_HANDLERS[block.name](**block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })
        messages.append({"role": "user", "content": results})
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1010681419.png' style="max-width:80%; max-height=80%;"></img></p>

33、[no-magic](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Mathews-Tom/no-magic)：零依赖单文件实现现代 AI 主流算法。这是一个专为学习 AI 算法设计的教学项目，包含 30 个零依赖、单文件、可直接运行的 Python 实现，涵盖从基础的 GPT 到微调（LoRA、PPO）以及推理优化（Flash Attention）等内容。通过简单易懂的代码实现每个算法，并配有对应的 Manim 动画，方便理解和学习。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1157073757.png' style="max-width:80%; max-height=80%;"></img></p>

34、[openclaw](https://hellogithub.com/periodical/statistics/click?target=https://github.com/openclaw/openclaw)：开箱即用的个人 AI 助手。这是一款用 TypeScript 开发的开源个人 AI 助手，可快速部署在 macOS、Windows 和 Linux 系统，并支持通过 WhatsApp、Telegram、Slack 等即时通讯应用进行交互。只要你的 token 额度充足，它就能 7*24 不停歇地执行任务，持续为你“打工”。来自 [@喜BFoCE](https://hellogithub.com/user/Fzr3vHc5AxqYUVj) 的分享

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1103012935.png' style="max-width:80%; max-height=80%;"></img></p>

35、[pi-mono](https://hellogithub.com/periodical/statistics/click?target=https://github.com/badlogic/pi-mono)：极简的 AI Agent 工具箱。这是一款基于 TypeScript 开发的 AI Agent 工具箱，爆火的 OpenClaw 就是基于该项目开发出来的。它提供开发 AI Agent 所需的基础功能，包括统一多 LLM 服务接口、Agent 状态管理、工具调用、交互式命令行界面、WebUI 和 Slack 机器人集成等。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1035029907.png' style="max-width:80%; max-height=80%;"></img></p>

36、[qmd](https://hellogithub.com/periodical/statistics/click?target=https://github.com/tobi/qmd)：本地运行的智能知识库搜索工具。这是一款完全本地运行的智能搜索引擎，可用于检索个人文档、知识库、会议记录和 Markdown 文件。它集成了本地运行轻量化模型、BM25 全文检索、向量语义搜索和重排序等功能，开箱即用、无需联网、支持 MCP 协议，可作为 AI 助手和 Agent 工作流中的知识搜索工具。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1112365301.jpg' style="max-width:80%; max-height=80%;"></img></p>

### 其它
37、[fishes](https://hellogithub.com/periodical/statistics/click?target=https://github.com/aldenhallak/fishes)：手绘鱼类的在线虚拟水族馆。该项目是让用户通过手绘创作鱼类涂鸦，并通过 AI 技术判定作品与鱼的相似度，通过审核的鱼会被放入一个全球共享的虚拟水族箱中。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1005290876.png' style="max-width:80%; max-height=80%;"></img></p>

38、[minichord](https://hellogithub.com/periodical/statistics/click?target=https://github.com/BenjaminPoilve/minichord)：开源的掌上电子乐器。这是一个口袋大小的迷你电子乐器，配备 21 个和弦按钮降低演奏门槛，并设有竖琴触控区用于弹奏不同音符，还支持通过 USB 连接作为 MIDI 控制器使用。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/848864434.jpg' style="max-width:80%; max-height=80%;"></img></p>

39、[pakku.js](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xmcp/pakku.js)：拯救 B 站弹幕体验的浏览器插件。这是一款专为提升哔哩哔哩网站弹幕体验的浏览器插件，能够自动合并重复或相似的弹幕内容，还你清爽的弹幕视频体验。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/83450261.png' style="max-width:80%; max-height=80%;"></img></p>

40、[quickemu](https://hellogithub.com/periodical/statistics/click?target=https://github.com/quickemu-project/quickemu)：让小白也能玩转虚拟机的工具。这是一个用于快速创建和运行 QEMU 虚拟机的工具，通过 quickget 和 quickemu 两个命令，能够自动完成系统镜像下载、配置文件生成和启动虚拟机，支持近千种操作系统版本，但仅限于在 Linux 和 macOS 宿主机上使用。来自 [@c-hui](https://hellogithub.com/user/wB7zTCa05KkDhLY) 的分享

41、[skills](https://hellogithub.com/periodical/statistics/click?target=https://github.com/anthropics/skills)：Claude 官方开源的 Skills 教程。该项目是 Anthropic 官方开源的 Agent Skills 仓库，介绍如何通过标准化的 SKILL.md 文件结构，将提示词和工具调用封装为插件形式，为 AI 助手提供可动态加载的技能包，以可复用的方式更好地完成特定任务。

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1061953414.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub118.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | 『下一期』
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/119'>这里</a>。
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
    </tr>
  </thead>
</table>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
