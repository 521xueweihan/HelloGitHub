# HelloGitHub Vol.119
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### C
1、[voidImageViewer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/voidtools/voidImageViewer)：Tiny Free Image Viewer Smaller Than Images.This is a lightweight Windows image viewer written in C language, allowing you to hardly feel any waiting. It is small in size, quick to launch, has extremely fast image loading and switching speeds, and supports mainstream image formats such as JPG, PNG, WEBP, BMP, GIF, ICO, TIF, etc.Shared by [@刘睿华](https://hellogithub.com/en/user/TJ65FfbQU09PLHM)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/100767968.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[Zen-C](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/z-libs/Zen-C)：Writing C Code Like a High-Level Language.This is a modern systems programming language that allows you to write code like a high-level language but run it like C. It compiles to GNU C/C11 code, is compatible with the C ABI (Application Binary Interface), supports seamless integration into existing C language ecosystems, and enhances the development experience while maintaining the execution efficiency of C.
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

### C#
3、[ParquetViewer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mukunku/ParquetViewer)：Desktop Application for Quick Viewing of Parquet Files.This is a Parquet file viewing and querying tool designed specifically for Windows users, supporting browsing file metadata, performing simple SQL queries, and opening single files or multiple files within a folder.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/135630194.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Winhance](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/memstechtips/Winhance)：Out-of-the-Box Windows System Optimization Tool.This is a one-stop Windows 10/11 system optimization tool developed in C#, enabling customization and system streamlining without reinstalling the system. It integrates functions such as software management, system optimization, and interface customization, supports one-click uninstallation of pre-installed applications, performance tuning, and interface beautification, and is applicable to system reinstallation or new device initialization.Shared by [@只是肚子太寂寞](https://hellogithub.com/en/user/TXJgfoRNWa8vmF4)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/916105685.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
5、[MFCMouseEffect](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sqmw/MFCMouseEffect)：Windows Mouse Effect Enhancement Tool.This is a lightweight Windows desktop mouse/cursor effect tool that supports various mouse effects like click ripples, particle trails, hover glow, and floating text.Shared by [@sqmw](https://hellogithub.com/en/user/5Dle7yOkCgFSUVj)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1139933103.png' style="max-width:80%; max-height=80%;"></img></p>

6、[zvec](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alibaba/zvec)：Lightweight In-Process Vector Database.This open-source in-process vector database from Alibaba can be used directly without independent deployment. It is built on the Proxima engine, offering localized and low-latency vector data management and semantic retrieval capabilities, and supports functions like hybrid search, data persistence, and re-ranking.
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

### Go
7、[lazyssh](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Adembc/lazyssh)：Terminal Interactive SSH Management Tool.This is a terminal interactive SSH management tool written in Go, which performs secure and reliable connections based on OpenSSH. It provides an intuitive and easy-to-use terminal interface, supporting features such as fuzzy search, sorting, Ping checks, and one-click connection.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1037246832.png' style="max-width:80%; max-height=80%;"></img></p>

8、[sql-tap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mickamy/sql-tap)：Real-time SQL Traffic Monitoring Tool.This is a real-time SQL traffic monitoring tool developed in Go, which can be used without code modification. It is deployed as a proxy between the application and the database, captures all queries by parsing the database wire protocol, provides two usage methods: TUI and Web, and supports databases such as PostgreSQL, MySQL, and TiDB

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1157577714.png' style="max-width:80%; max-height=80%;"></img></p>

9、[Surge](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/surge-downloader/Surge)：High-Speed Download Tool for Terminal.This is a terminal download tool developed in Go language, which can automatically split downloaded files into multiple data chunks for parallel download, and supports features such as downloading from multiple mirror sources, automatic failover, and sequential download mode.Shared by [@Meet Mehta](https://hellogithub.com/en/user/AB7OfuhyiEqmkZv)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1085475816.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[task](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/go-task/task)：Build Tool to Say Goodbye to Complex Makefile Syntax.This is a modern build tool developed in Go, serving as a replacement for GNU Make. It uses a simpler YAML syntax and supports features like cross-platform compatibility, dependency management, parallel execution, and conditional triggering, making it suitable for project building, development environment management, and CI/CD integrationShared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

### Java
11、[jquick-curl](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/paohaijiao/jquick-curl)：Java Library for Directly Running curl Commands.This is a lightweight HTTP client Java library that can directly convert curl commands into executable HTTP request logic in Java without manual code rewriting. It is suitable for quickly integrating into Java projects after copying curl commands from Chrome browser developer tools, API documents, etc.Shared by [@paohaijiao](https://hellogithub.com/en/user/iIaNjn0mSdwx6gv)
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

12、[pokemon-tbje](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zachMahan64/pokemon-tbje)：Text-based Pokémon Game Written in Java.This is a terminal-based text Pokémon game built with the Java game development framework LibGDX, rendering the screen using Unicode Braille characters as pixels, and supporting battle mechanisms and a complete single-player storyline.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/968848455.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
13、[cloud-mail](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/maillab/cloud-mail)：Lightweight Email Service Based on Cloudflare.This is a lightweight and responsive email service based on Cloudflare. It enables you to quickly build an email service platform on Cloudflare Workers with just one domain at a low cost, supporting functions such as bulk email sending, attachment sending and receiving, and CAPTCHA verification.Shared by [@eoao](https://hellogithub.com/en/user/Yi9MEGzFwLfdPHb)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/971999086.png' style="max-width:80%; max-height=80%;"></img></p>

14、[folio-2025](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/brunosimon/folio-2025)：When Personal Homepage Transforms into a 3D Game.This project is an open-source new work by front-end guru Bruno Simon. He transforms his personal homepage into an immersive 3D open-world game where you can drive and explore, incorporating elements like physics simulation, weather systems, vegetation, and day-night cycles.Shared by [@卷卷卷](https://hellogithub.com/en/user/tDk0fh9eI4PxVwn)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/871518808.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[hanzi-writer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chanind/hanzi-writer)：Let Chinese Characters Come to Life on Web Pages.This is a JavaScript library for displaying Chinese character stroke order and interactive writing practice, supporting simplified/traditional Chinese characters, adjusting playback speed, loop modes, real-time stroke correctness checking, and other functions
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

16、[streamdown](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vercel/streamdown)：React Markdown Component Designed for Streaming Output.This project is a React Markdown component designed specifically for streaming scenarios, which can address issues like flickering, rendering errors, and security concerns when large language models output Markdown content word by word
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

17、[taoyuan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/setube/taoyuan)：Text-based Pastoral Management Simulation Game.This is a text-based pastoral management simulation game named 'Taoyuan Township', inspired by 'Stardew Valley'. It adopts a visual design that combines pixel art and Chinese style, and players can manage their farm as they wish, experiencing various gameplays like planting, fishing, cooking, animal husbandry, and cave exploration.Shared by [@谦君](https://hellogithub.com/en/user/OCYdts5lPczHag4)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1151925632.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
18、[Compass](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Kr0oked/Compass)：Minimalist Android Compass.This is an Android compass application developed in Kotlin, with a simple interface, small size, no ads, and supports real-time display of basic directions, sensor status, and vibration feedbackShared by [@ewiro](https://hellogithub.com/en/user/iItGgWoJjnLsr0Y)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/182394441.png' style="max-width:80%; max-height=80%;"></img></p>

19、[PixelPlayer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/theovilardo/PixelPlayer)：Highly Aesthetic and Multi-functional Android Music Player.This is a local-first, privacy-focused Android music player featuring a beautiful Material You dynamic theme that automatically adapts to album covers or phone wallpapers. It supports lyrics display, custom song transitions, home screen widgets, casting playback, and listening statistics, among other functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/987110251.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
20、[freemocap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/freemocap/freemocap)：Free and Open-Source Motion Capture System.This is a motion capture system developed based on Python, which requires no markers or GPUs and can collect full-body 3D motion data using ordinary cameras, and it is suitable for scenarios such as animation production, game development, and education

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/357362803.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[gh-space-shooter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/czl9707/gh-space-shooter)：Generating Space Shooter GIFs Based on GitHub Contributions.This project can generate space shooter game-style GIFs based on users' GitHub contribution graphs, supports customizing GIF frame rates, and can regularly generate via GitHub Actions and automatically update to personal homepages.Shared by [@Zane ChenPEc8I](https://hellogithub.com/en/user/wSHB9xmqPdsnu4C)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1126431904.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[great_expectations](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/great-expectations/great_expectations)：Verifying Data Quality Like Writing Unit Tests.This is a Python-based data quality verification framework that allows defining verification rules through concise code, just like writing unit tests for data, and supports multiple data access methods such as pandas, Spark, and SQLAlchemyShared by [@Ashraf Haress](https://hellogithub.com/en/user/6erlUGDQfB4qAPo)
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

23、[InvenTree](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/inventree/InvenTree)：Open-Source Inventory Management System.This is an inventory management platform developed with Python and Django, featuring a web management interface and REST API services, and supporting functions like barcode-based inventory entry, part tracking, bill of materials, and supplier management.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/85894461.png' style="max-width:80%; max-height=80%;"></img></p>

24、[pycparser](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/eliben/pycparser)：Pure Python Implemented C Parser.This is a pure Python-implemented C parser with no third-party dependencies. It can parse C code into an abstract syntax tree, enabling easy analysis and manipulation of C code using Python, and supports the full C99 standard and some C11 features.

### Rust
25、[FaceWinUnlock-Tauri](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zs1083339604/FaceWinUnlock-Tauri)：Open-Source Windows Face Recognition Unlock Tool.This is an enhanced Windows face recognition unlock tool developed based on the Tauri framework, which provides a Windows Hello-like face-unlocking experience for ordinary Windows computers without infrared cameras.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1126550681.png' style="max-width:80%; max-height=80%;"></img></p>

26、[monty](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pydantic/monty)：The Python Interpreter with Lightning-Fast Startup.This project is a Python interpreter developed by the Pydantic team using Rust, featuring rapid startup, secure isolation, state snapshots, etc., and is suitable for running Python code generated by large models in AI Agents.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/646426100.png' style="max-width:80%; max-height=80%;"></img></p>

27、[weathr](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Veirt/weathr)：Real-Time ASCII Weather Animation Written in Rust.This is a terminal-based weather tool written in Rust that uses ASCII animations to real-time display current weather conditions, supporting animations like rain, snow, lightning, and day-night transitions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1152969678.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift
28、[AppPorts](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wzh4869/AppPorts)：One-Click Migration of macOS Apps to External Hard Drives.This project migrates macOS applications to external storage devices (external hard drives, SD cards, or NAS) through symlinks via the Contents folder, retains the application entry point in the original location, enabling users to launch the application as before, and frees up precious macOS storage space without impacting usageShared by [@Zehua Wang](https://hellogithub.com/en/user/SjNchy8nMfGgUlx)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1099232644.png' style="max-width:80%; max-height=80%;"></img></p>

29、[DebugSwift](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/DebugSwift/DebugSwift)：Open-Source iOS Mobile Debugging Toolkit.This is an end-side debugging toolkit designed specifically for iOS app development. You can start the debugging panel in the app with just a few lines of code, and it supports functions like network traffic viewing, performance analysis, interface debugging, and file browsing.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/731804628.png' style="max-width:80%; max-height=80%;"></img></p>

30、[dorso](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tldev/dorso)：Posture-Correcting macOS Application.This is a Swift-developed macOS application for posture monitoring, which can detect postures in real time via the camera or AirPods. When it detects the user slouching or leaning forward, the application gradually blurs the screen to remind the user to correct their posture in time.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1141375692.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
31、[daily_stock_analysis](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ZhuLinsen/daily_stock_analysis)：Intelligent Stock Analysis System Based on LLM.This is an LLM-driven intelligent stock analysis tool that supports daily automatic analysis and push for A-shares, Hong Kong stocks, and US stocks. It obtains real-time market data from data sources like AkShare, Tushare, and YFinance, and uses large model API services such as DeepSeek to conduct multi-dimensional analysis (technical aspects, position distribution, public sentiment) on selected stocks, generating decision-making dashboards. It supports scheduled execution via GitHub Actions (no server required) or one-click deployment via Docker.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1131513930.png' style="max-width:80%; max-height=80%;"></img></p>

32、[learn-claude-code](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shareAI-lab/learn-claude-code)：Building an AI Agent from Scratch.This project demonstrates how to construct an AI Agent tool similar to Claude Code from the ground up, consisting of 12 lessons. Each lesson comes with a runnable Python file. The content progresses from the most fundamental Agent loop, incrementally incorporating functions like tool invocation, task planning, sub-agents, context compression, multi-agent collaboration, and autonomous execution, ultimately building a comprehensive AI Agent system.Shared by [@喜BFoCE](https://hellogithub.com/en/user/Fzr3vHc5AxqYUVj)
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

33、[no-magic](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Mathews-Tom/no-magic)：Implementing Modern Mainstream AI Algorithms in Zero-Dependency Single File.This is a teaching project designed specifically for learning AI algorithms, including 30 zero-dependency, single-file, directly runnable Python implementations covering from basic GPT to fine-tuning (LoRA, PPO) and inference optimization (Flash Attention), etc. Each algorithm is implemented with easy-to-understand code, accompanied by corresponding Manim animations for easy comprehension and learning.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1157073757.png' style="max-width:80%; max-height=80%;"></img></p>

34、[openclaw](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/openclaw/openclaw)：Out-of-the-Box Personal AI Assistant.This is an open-source personal AI assistant developed with TypeScript, which can be quickly deployed on macOS, Windows, and Linux systems, and supports interaction through instant messaging apps like WhatsApp, Telegram, and Slack. As long as your token quota is sufficient, it can work continuously 24/7 to serve youShared by [@喜BFoCE](https://hellogithub.com/en/user/Fzr3vHc5AxqYUVj)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1103012935.png' style="max-width:80%; max-height=80%;"></img></p>

35、[pi-mono](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/badlogic/pi-mono)：Minimalist AI Agent Toolkit.This is a TypeScript-based AI Agent toolkit. The popular OpenClaw is developed based on this project. It provides fundamental functions for AI Agent development, including unified multi-LLM service interfaces, Agent state management, tool invocation, interactive command-line interface, WebUI, and Slack bot integration, etc.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1035029907.png' style="max-width:80%; max-height=80%;"></img></p>

36、[qmd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tobi/qmd)：Intelligent Knowledge Base Search Tool for Local Operation.This is a fully locally-operated intelligent search engine that can be used to retrieve personal documents, knowledge bases, meeting minutes, and Markdown files. It integrates functions such as locally-run lightweight models, BM25 full-text search, vector semantic search, and re-ranking. It is ready to use out of the box, doesn't require internet access, supports the MCP protocol, and can be used as a knowledge search tool in AI assistant and Agent workflows.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1112365301.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Other
37、[fishes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/aldenhallak/fishes)：Online Virtual Aquarium for Hand-drawn Fish.This project enables users to create hand-drawn fish illustrations. Then, using AI technology, it assesses the similarity between the creations and actual fish. Fish that pass the review will be placed in a globally shared virtual aquarium.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1005290876.png' style="max-width:80%; max-height=80%;"></img></p>

38、[minichord](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/BenjaminPoilve/minichord)：Open-Source Handheld Electronic Instrument.This is a pocket-sized mini electronic instrument, equipped with 21 chord buttons to lower the playing threshold, featuring a harp touch area for playing different notes, and also supports being used as a MIDI controller via USB connection

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/848864434.jpg' style="max-width:80%; max-height=80%;"></img></p>

39、[pakku.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xmcp/pakku.js)：Browser Extension to Save Bilibili Danmaku Experience.This is a browser extension specifically designed to enhance the danmaku experience on the Bilibili website. It can automatically merge duplicate or similar danmaku content, bringing you a clear danmaku video experience.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/83450261.png' style="max-width:80%; max-height=80%;"></img></p>

40、[quickemu](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/quickemu-project/quickemu)：Tools for Novices to Play with Virtual Machines Easily.This is a tool for quickly creating and running QEMU virtual machines. It can automatically complete system image downloading, configuration file generation, and virtual machine startup through two commands, quickget and quickemu. It supports nearly a thousand operating system versions, but is only available on Linux and macOS hosts.Shared by [@c-hui](https://hellogithub.com/en/user/wB7zTCa05KkDhLY)

41、[skills](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/anthropics/skills)：Official Open-Source Claude Skills Tutorial.This project is the official open-source Agent Skills repository by Anthropic, introducing how to encapsulate prompts and tool invocations into plug-in forms through a standardized SKILL.md file structure, providing AI assistants with dynamically loadable skill packs to better accomplish specific tasks in a reusable manner

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/119/1061953414.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub118.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | 『Next』
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
        <a href="https://www.qiniu.com/products/ai-token-api?utm_source=hello">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/qiniu.jpg" width="60px"><br>
          <sub>七牛云</sub><br>
          <sub>百万 Token 免费体验</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
