# HelloGitHub Vol.114
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
1、[fastfetch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fastfetch-cli/fastfetch)：Faster System Information Viewer.This is a command-line tool similar to neofetch, which provides an overview of system information in the terminal. It is written in C language and is faster than neofetch, which is written in bash. The information displayed includes the operating system, shell, kernel, CPU, GPU, memory, etc., and currently supports Linux, Android, FreeBSD, macOS, and Windows 7+ operating systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/340181518.png' style="max-width:80%; max-height=80%;"></img></p>

2、[miniaudio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mackron/miniaudio)：Extremely Easy-to-Use C Language Audio Library.This is a single-file, zero-dependency, cross-platform C language audio library. It encapsulates the underlying audio APIs of various mainstream operating systems into simple and easy-to-use interfaces, allowing you to easily implement functions such as audio playback, recording and processing. It is suitable for game engines, real-time communication, embedded, offline batch processing and other scenarios.
```c
#include "miniaudio/miniaudio.h"

#include <stdio.h>

int main()
{
    ma_result result;
    ma_engine engine;

    result = ma_engine_init(NULL, &engine);
    if (result != MA_SUCCESS) {
        return -1;
    }

    ma_engine_play_sound(&engine, "sound.wav", NULL);

    printf("Press Enter to quit...");
    getchar();

    ma_engine_uninit(&engine);

    return 0;
}
```

### C#
3、[ClassIsland](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ClassIsland/ClassIsland)：The Open Source Timetable Tool at a Glance.This is a desktop timetable application specifically designed for large-screen devices. It can place the timetable in the form of simple components on the desktop all the time, replacing the traditional blackboard timetable. It supports functions such as class dismissal reminders, weather information, countdown, password protection, and timetable import. It is suitable for classrooms equipped with classroom multimedia large screens, projectors or smart blackboards.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/663887125.png' style="max-width:80%; max-height=80%;"></img></p>

4、[CrossPlatformDiskTest](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/maxim-saplin/CrossPlatformDiskTest)：Multi-platform Hard Disk Performance Testing Tool.This is an open-source storage and memory performance testing tool suitable for solid-state drives, mechanical hard drives, USB drives and other storage devices. It supports sequential and random read/write tests, provides performance indicators such as IOPS and MB/s, and is compatible with Windows, macOS, Linux and Android systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/150983217.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
5、[Crow](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/CrowCpp/Crow)：Lightweight C++ Web Framework Similar to Flask.This is a lightweight web framework designed specifically for C++ developers. It can be easily integrated by simply including header files. It has a simple and easy-to-use routing API similar to Python Flask. With only a small amount of code, a web service can be quickly built, greatly reducing the threshold of C++ web development.
```cpp
#include "crow.h"

int main()
{
    crow::SimpleApp app;

    CROW_ROUTE(app, "/")([](){
        return "Hello world";
    });

    app.port(18080).multithreaded().run();
}
```

6、[ShaderGlass](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mausimus/ShaderGlass)：Adding Cool Special Effects to Windows Desktop in Real Time.This is a shader tool suitable for Windows systems that can achieve various overlay effects such as image special effects, retro display, and visual enhancement. It can add a 'special effect filter' in real time to your screen or application window. It comes with classic shaders such as CRT, image enlargement, pixelation, and color correction.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/308317827.jpg' style="max-width:80%; max-height=80%;"></img></p>

7、[vicinae](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vicinaehq/vicinae)：Blazing Fast Native Desktop Launcher.This is a desktop launcher developed based on C++. It does not rely on Electron or browsers. It is fast, easy to expand, and has a simple interface. It focuses on improving desktop operation efficiency and supports features such as file search, clipboard history, and inline calculator.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1027461827.gif' style="max-width:80%; max-height=80%;"></img></p>

### Go
8、[fuck-u-code](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Done-0/fuck-u-code)：Tool for Automatically Detecting Code 'Shit Mountain' Level.This is a tool used to evaluate the 'shit mountain' level of code, supporting multiple programming languages such as Python, Java, and Go. It can automatically scan the specified directory, deeply analyze the chaos degree of project code, and tell you the result in a sharp and funny way.Shared by [@wei-guang](https://hellogithub.com/en/user/JtGB5xfIQaqE1re)

9、[git-who](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sinclairtarget/git-who)：Git Directory-level Contribution Analysis Tool.This is a command-line tool developed with Go and Ruby languages, used to quickly count and visualize the number of commits, lines of code modified, and active time of each contributor by directory in a Git repository.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/899941526.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[gonzo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/control-theory/gonzo)：Terminal User Interface Log Analysis Tool.This is a terminal (TUI) log analysis tool developed with Go language, inspired by k9s. It supports real-time analysis, filtering and visualizing logs in the terminal interface, and combines AI to enhance log insight ability. It is suitable for daily development, operation and maintenance, and fault troubleshooting scenarios.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1040280323.png' style="max-width:80%; max-height=80%;"></img></p>

11、[ntfy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/binwiederhier/ntfy)：Out-of-the-box Cross-Device Push Notification Service.This project is an open-source push notification service based on the HTTP protocol, supporting cross-device message pushing via PUT/POST requests. Developed in Go language, users can easily send notifications through command-line tools or simple APIs without registration. It supports custom notification content and self-hosted deployment, and provides corresponding Android and iOS clients.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/420503947.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[kroki](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yuzutech/kroki)：Lightweight Chart Generation Service Supporting Multiple Syntaxes.This is a service that supports generating charts from various text descriptions. It provides a unified API interface and supports dozens of mainstream chart syntaxes and formats, including PlantUML, Mermaid, Graphviz, C4, BlockDiag, BPMN, Excalidraw, etc.Shared by [@塔咖](https://hellogithub.com/en/user/bzJpGyu0IanC6L7)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/165063056.png' style="max-width:80%; max-height=80%;"></img></p>

13、[PeerBanHelper](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PBH-BTN/PeerBanHelper)：BT Anti-sucking Tool to Improve Download Experience.This is an anti-sucking tool specifically designed for BT (BitTorrent) users. It can automatically identify and block peers that only download and do not upload, as well as unpopular or abnormal nodes. It supports mainstream BT clients such as qBittorrent, Deluge, BiglyBT, and BitComet.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/754169590.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
14、[CubeCity](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hexianWeb/CubeCity)：Cartoon-style City-building Simulation Game.This is a lightweight, cartoon-style 2.5D city simulation game built based on Three.js and Vue3. Players can build, relocate and demolish buildings in real-time through clicking and dragging in the browser. Buildings will automatically generate gold coins that can be used to build or upgrade facilities. The game integrates the concepts of Environmental, Social and Governance (ESG). City planning needs to balance multiple needs in order to create an ideal sustainable city.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1013487627.png' style="max-width:80%; max-height=80%;"></img></p>

15、[lazy-brush](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dulnan/lazy-brush)：JavaScript Library for Smooth Handwriting and Signatures.This is a JavaScript library for smooth drawing that supports smoothly drawing brush trajectories with a mouse or finger. It adopts the 'lazy brush' algorithm to effectively reduce problems such as hand tremors and sawtooth, making lines more natural and smooth. It is suitable for various scenarios such as drawing boards, signatures, and handwriting.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/145379450.png' style="max-width:80%; max-height=80%;"></img></p>

16、[mammoth.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mwilliamson/mammoth.js)：Library for Converting Word Documents to HTML.This is a JavaScript library for converting the content of Word documents (.docx) into HTML. It can extract structural information in the document, such as headings, lists, tables, footnotes, etc., and map them to corresponding HTML tags. At the same time, it ignores most styles (such as font color, font size, margins, etc.), making the generated HTML code more concise and clean.
```javascript
var mammoth = require("mammoth");

mammoth.convertToHtml({path: "path/to/document.docx"})
    .then(function(result){
        var html = result.value; // The generated HTML
        var messages = result.messages; // Any messages, such as warnings during conversion
    })
    .catch(function(error) {
        console.error(error);
    });
```

17、[Termix](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Termix-SSH/Termix)：Good-looking One-stop Server Management Platform.This is a web-based server management platform that integrates SSH terminal, SSH tunnel, server monitoring and file management functions. It is completely open source and free, and can be self-hosted. It supports automatic reconnection, file upload, split-screen display and syntax highlighting features.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/893684207.png' style="max-width:80%; max-height=80%;"></img></p>

18、[websocket-devtools](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/law-chain-hot/websocket-devtools)：Plug-and-Play WebSocket Debugging Tool.This is a professional WebSocket debugging and traffic control browser plugin. After installation, it will add a new tab in the Chrome DevTools panel. It is easy to operate and supports real-time monitoring, message simulation and traffic interception of WebSocket traffic and other functions.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1013230576.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
19、[goodtime](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/adrcotfas/goodtime)：Minimal and Power-saving Tomato Clock Tool.This is an open-source Android time management tool that helps users manage time and improve concentration based on the Pomodoro Technique. It is ad-free, trackless, and completely offline, supporting features such as history records, colored labels, heatmap statistics, focus/break ratio, and custom styles.Shared by [@ewiro](https://hellogithub.com/en/user/iItGgWoJjnLsr0Y)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/61319303.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
20、[lutris](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lutris/lutris)：Open-Source Linux Gaming Platform.This is a game management platform designed specifically for Linux users, written in Python. It offers a user-friendly interface that greatly simplifies the process of game installation and configuration on Linux, allowing users to easily install and manage a variety of games. It supports connections to multiple gaming platforms such as Steam, GOG, Humble Bundle, and also has the capability to run Windows games.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/13419223.jpg' style="max-width:80%; max-height=80%;"></img></p>

21、[pdfplumber](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jsvine/pdfplumber)：Python Library for Easily Extracting PDF Text and Tables.This project is a Python-based PDF parsing and data extraction library that can easily extract text and tables. It is able to accurately obtain detailed positions, sizes and font information of each character, line, rectangle and other elements in the PDF document, and supports one-click generation of page snapshots for convenient debugging.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/41279279.png' style="max-width:80%; max-height=80%;"></img></p>

22、[pydoll](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/autoscrape-labs/pydoll)：WebDriver-Free Browser Automation Python Library.This is a Python library for automating Chromium-based browsers. It controls browsers directly through the native DevTools Protocol (CDP) without relying on WebDriver. It supports bypassing captchas and simulating human interactions.
```python
import asyncio

from pydoll.browser import Chrome
from pydoll.constants import Key

async def baidu_search(query: str):
    async with Chrome() as browser:
        tab = await browser.start()
        await tab.go_to('https://www.baidu.com')
        search_box = await tab.find(tag_name='textarea', id='chat-textarea')
        await search_box.insert_text(query)
        await search_box.press_keyboard_key(Key.ENTER)
        await asyncio.sleep(5)

asyncio.run(baidu_search('HelloGitHub'))
```

23、[pyscript](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pyscript/pyscript)：Create Applications Directly in the Browser Using Python.This project allows developers to directly use the Python programming language within HTML files, similar to how JavaScript files are included and executed. It supports MicroPython, common third-party libraries, and manipulation of page elements, making it suitable for quickly creating interactive data visualizations, website prototypes, and web applications for online education.Shared by [@Veeja Liu](https://hellogithub.com/en/user/70zTMbIqVf9dvZp)
```html
<head>
    <link rel="stylesheet" href="./core.css"/>
    <script type="module" src="./core.js"></script>
</head>
<body>
    <script type="py" terminal>
        from pyscript import display
        display("HelloGitHub!") # this goes to the DOM
        print("Hello terminal") # this goes to the terminal
    </script>
</body>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/461710233.png' style="max-width:80%; max-height=80%;"></img></p>

24、[tinyio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/patrick-kidger/tinyio)：Extremely Easy-to-Use Python Event Loop Library.This is a lightweight Python event loop library with approximately 300 lines of code, providing developers with a more concise and easy-to-use asynchronous programming experience than asyncio.
```python
import tinyio

def slow_add_one(x: int):
    yield tinyio.sleep(1)
    return x + 1

def foo():
    four, five = yield [slow_add_one(3), slow_add_one(4)]
    return four, five

loop = tinyio.Loop()
out = loop.run(foo())
assert out == (4, 5)
```

### Rust
25、[rust-tutorial](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/InkSha/rust-tutorial)：Beginner-Friendly Rust Practical Tutorial.This is a quick start tutorial designed specifically for Rust beginners, guiding you to implement a usable command-line Todo application step by step.

26、[Seelen-UI](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/eythaann/Seelen-UI)：Highly Customizable Windows Desktop Decoration Tool.This is a free and open-source Windows desktop enhancement tool focusing on high customization and efficiency improvement. It is developed with Rust language and combines Tauri framework with web technologies, supporting window tiling management, application launcher, Dock, taskbar, dynamic wallpaper, plugin extension and other functions.Shared by [@Rainux He](https://hellogithub.com/en/user/EDis5NBzXAIb4qF)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/758623687.png' style="max-width:80%; max-height=80%;"></img></p>

27、[xh](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ducaale/xh)：More Friendly Command-line HTTP Client.This is a command-line HTTP client written in Rust, supporting syntax highlighting, JSON formatting, download progress bars, session cookie persistence, etc. It can perfectly replace cURL.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/294521053.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift
28、[AirBattery](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lihaoyun6/AirBattery)：Mac Tool for Remotely Viewing Apple Device Battery.This is a battery monitoring tool specifically designed for macOS, which can display the battery level of iPhone, iPad, AirPods and Apple Watch and other devices in real time in the Mac menu bar. Without installing any App on the iOS side, you can view the current battery level and charging status of the device on the computer side and support low battery reminder.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/755969344.png' style="max-width:80%; max-height=80%;"></img></p>

29、[Ice](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jordanbaird/Ice)：Powerful macOS Menu Bar Management Tool.This project is a menu bar management tool designed for macOS systems. It is ready to use out of the box and is easy to operate, with main features including hiding and displaying menu bar content, support for hover display, click display, auto-hide, setting menu bar shadows, shortcuts, startup at boot, and auto-update capabilities.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/674832198.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
30、[how-to-build-a-coding-agent](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ghuntley/how-to-build-a-coding-agent)：Practical Tutorial on Implementing an AI Programming Assistant from Scratch.This is a project that teaches you how to develop a local AI programming assistant from scratch using Go language combined with the Claude API. It starts with a simple chatbot and gradually implements functions such as file operations, command execution, code editing, and search.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1025300166.png' style="max-width:80%; max-height=80%;"></img></p>

31、[parlant](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/emcie-co/parlant)：Intelligent Agent Development Framework for Regulating Large Models.This is an LLM intelligent agent development framework specifically designed for real-world scenario control. Its purpose is to solve the problem that traditional LLM dialogue systems are difficult to accurately control in complex businesses. It defines intelligent agent behavior rules through natural language and flexibly controls the dialogue behavior of AI to avoid 'hallucinations' or deviating from business goals.
```python
import asyncio
import parlant.sdk as p

async def main():
  async with p.Server() as server:
    agent = await server.create_agent(
        name="Otto Carmen",
        description="You work at a car dealership",
    )

    await agent.create_guideline(
        # This is when the guideline will be triggered
        condition="the customer greets you",
        # This is what the guideline instructs the agent to do
        action="offer a refreshing drink",
    )

asyncio.run(main())
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/758197374.gif' style="max-width:80%; max-height=80%;"></img></p>

32、[SwanLab](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SwanHubX/SwanLab)：AI Model Training Tracking and Observability Platform.This is a tracking, recording, analysis and collaboration tool specifically designed for AI model training, aiming to help researchers optimize the training process and improve team collaboration efficiency. It provides training visualization, automatic logging, hardware monitoring, experiment management and multi-person collaboration functions through a simple Python API and an intuitive interface. It has integrated more than 40 mainstream training frameworks and is suitable for large model training, computer vision, audio processing, AIGC and other task scenarios.Shared by [@Ze-Yi LIN](https://hellogithub.com/en/user/Oh5UaGjfrblg0yZ)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/722915433.png' style="max-width:80%; max-height=80%;"></img></p>

33、[WhisperLiveKit](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/QuentinFuxa/WhisperLiveKit)：Ready-to-use Local Speech Transcription Tool.This is an open-source tool that integrates real-time speech-to-text, translation, and speaker separation. It comes with a server-side and Web UI, and can be easily privately deployed with just one command. Based on the latest incremental streaming technology, it can achieve ultra-low latency in real-time meeting recording and cross-language communication without the need for network connection or writing front-end code.
```
# 使用 large-v3 模型，并将英语翻译为中文
whisperlivekit-server --model large-v3 --language en --target-language zh

# 说话人分离，服务器监听 80 端口
whisperlivekit-server --host 0.0.0.0 --port 80 --model medium --diarization --language zh
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/905697354.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
34、[balatro-gba](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GBALATRO/balatro-gba)：Annual Poker Masterpiece GBA Port.This is a project to port the game 'Balatro' to the GBA platform. To protect the game copyright, this project only provides a simplified version of 'Balatro' and will not fully restore the original content. Users need to build the ROM file by themselves.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/925448611.png' style="max-width:80%; max-height=80%;"></img></p>

35、[CookLikeHOC](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Gar-b-age/CookLikeHOC)：Laoxiang Chicken Recipe Open Source Version.This project is not produced by Laoxiang Chicken official. It is based on materials such as 'Laoxiang Chicken Dish Traceability Report', and has summarized and organized the formulas, production processes and cooking points of Laoxiang Chicken dishes.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

36、[flip-card](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Nicholas-L-Johnson/flip-card)：A 'Flowable' Electronic Business Card.This is an open-source project that presents real-time fluid simulation effects on a business card-sized hardware. It is based on Raspberry Pi RP2350 and uses Rust language to implement particle simulation. The overall hardware cost is about $12.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/1024724696.gif' style="max-width:80%; max-height=80%;"></img></p>

37、[podman-desktop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/podman-desktop/podman-desktop)：Fully Free Container Desktop Management Tool.This is a cross-platform, free and open-source container and K8s desktop management tool that provides an intuitive and easy-to-use desktop interface for the construction, management and deployment of containers and K8s, supporting mainstream containers such as Podman, Docker, Lima and kind.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/465844859.png' style="max-width:80%; max-height=80%;"></img></p>

38、[winboat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TibixDev/winboat)：Easily Run Windows Applications on Linux Systems.This is a tool that allows you to run Windows applications on Linux without complicated configurations. Through a graphical wizard, it automatically completes image pulling, container creation and RDP configuration. There is no need to manually enter commands throughout the process, and Windows applications can be seamlessly presented on the Linux desktop in independent windows.Shared by [@moyelx](https://hellogithub.com/en/user/e8vnBGS9XmjYLho)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/114/960420129.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
39、[ml-interviews-book](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chiphuyen/ml-interviews-book)：Machine Learning Interviews Book.This is a free and open-source e-book specifically designed for job interviews in the field of machine learning. It covers ML job types, the perspective of interviewer scoring, battle preparation routes, and more than 200 graded interview questions.



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub113.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub115.md">『Next』</a>
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
