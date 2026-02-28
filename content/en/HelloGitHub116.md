# HelloGitHub Vol.116
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
1、[sj.h](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rxi/sj.h)：Minimal C Language JSON Parsing Library.This is a lightweight C language JSON parsing library that provides reliable JSON traversal and basic parsing functions. It has only 150 lines of code and has no external dependencies. It adopts a zero-memory allocation strategy and parses directly on the original data. It is fast and has no risk of memory leaks. It is suitable for scenarios such as embedded, Internet of Things, and game development.
```c
char *json_text = "{ \"x\": 10, \"y\": 20, \"w\": 30, \"h\": 40 }";

typedef struct { int x, y, w, h; } Rect;

bool eq(sj_Value val, char *s) {
    size_t len = val.end - val.start;
    return strlen(s) == len && !memcmp(s, val.start, len);
}

int main(void) {
    Rect rect = {0};

    sj_Reader r = sj_reader(json_text, strlen(json_text));
    sj_Value obj = sj_read(&r);

    sj_Value key, val;
    while (sj_iter_object(&r, obj, &key, &val)) {
        if (eq(key, "x")) { rect.x = atoi(val.start); }
        if (eq(key, "y")) { rect.y = atoi(val.start); }
        if (eq(key, "w")) { rect.w = atoi(val.start); }
        if (eq(key, "h")) { rect.h = atoi(val.start); }
    }

    printf("rect: { %d, %d, %d, %d }\n", rect.x, rect.y, rect.w, rect.h);
    return 0;
}
```

### C#
2、[CPUSetSetter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SimonvBez/CPUSetSetter)：Manually Specify CPU Cores for Running Games.This project is a performance optimization tool specifically designed for Windows 11. Using CPU Sets technology, it allows users to freely control the CPU cores used when running games and applications without the need to restart the program throughout the process.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1029765448.png' style="max-width:80%; max-height=80%;"></img></p>

3、[PicView](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Ruben2776/PicView)：A Better Picture Viewing Tool than System-built.This is a fast and free picture viewing tool suitable for Windows and macOS platforms. It uses.NET NativeAOT compilation technology, with a small volume and fast startup speed. It supports functions such as browsing long pictures, editing pictures, format conversion, and batch processing.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/79786795.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
4、[crossdesk](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kunkundi/crossdesk)：Web-Supported Remote Desktop Tool.This is an open-source and lightweight cross-platform remote desktop tool that supports remote desktop control and audio-video transmission between different devices (Windows, Linux and macOS). The characteristic is that it can directly control remote devices through the browser without the need to install any additional applications.Shared by [@Junkun Di](https://hellogithub.com/en/user/cb0OpZRrBuGVAfL)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/720999514.png' style="max-width:80%; max-height=80%;"></img></p>

5、[MouseClick](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SeaEpoch/MouseClick)：Open-source Mouse Clicker Tool.This is a mouse clicker built with Qt6 and is only available for Windows systems. It is ready-to-use and easy to operate, supporting custom mouse click intervals and shortcut key functions.Shared by [@SeaYJ](https://hellogithub.com/en/user/6aHSOczLEVNxDF7)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/383007660.png' style="max-width:80%; max-height=80%;"></img></p>

6、[objcurses](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/admtrv/objcurses)：Command-line Tool for Viewing 3D Models.This is a minimalist 3D model viewer that can render and display 3D model files in ASCII characters within the terminal. It supports real-time preview, rotation, and interactive operations of 3D objects.Shared by [@CN1998Ft](https://hellogithub.com/en/user/QwmfN9cuvYja4b3)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/887103582.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[seekdb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/oceanbase/seekdb)：Out-of-the-box Lightweight Vector Database.This project is a lightweight AI-native search database open-sourced by the OceanBase team, supporting unified storage and retrieval of relational, vector, and text data. It provides both embedded and server modes and can run with as low as 1C1G. It is compatible with the MySQL protocol.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1080442728.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
8、[filebrowser](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gtsteffaniak/filebrowser)：Fully Open Source and Self-Hostable Private Cloud Disk.This project is an online file management tool built based on Go+Vue.js. It has more features than the original FileBrowser, supporting multi-file sources (local or cloud), directory-level access control, setting shared expiration time, file search, and thumbnail functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/652319769.png' style="max-width:80%; max-height=80%;"></img></p>

9、[kite](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kite-org/kite)：Open Source Lightweight K8s Management Panel.This is a lightweight and modern Kubernetes visual management platform suitable for managing and monitoring K8s clusters. It has an intuitive and easy-to-use interface and supports functions such as viewing Pod logs, executing container commands, editing YAML configurations, and managing user permissions.Shared by [@Zzde](https://hellogithub.com/en/user/w5uk718RFhDzdCX)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1003614809.png' style="max-width:80%; max-height=80%;"></img></p>

10、[term.everything](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mmulet/term.everything)：Running Any GUI Application in the Terminal.This project breaks the limitation that traditional terminals can only run command-line programs. It enables users to run any GUI application in the terminal. It brings the graphical interface operation experience into the terminal environment. Through its self-developed Wayland compositor, it renders the original GUI window output to the monitor into characters or pictures that can be displayed in the terminal in real time, realizing the ability to run graphical applications in the terminal. It is compatible with mainstream terminal emulators such as iTerm2, Alacritty, and Kitty.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1051928239.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[tuios](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Gaurav-Gosain/tuios)：Achieving Desktop-level Window Management within the Terminal.This is a terminal multi-window management tool written in Go, supporting floating windows, mouse dragging, automatic tiling, multi-workspace switching, etc. Windows can be freely overlapped and moved. Just like a desktop operating system, it is suitable for developers who find tmux shortcut keys difficult to remember.Shared by [@天涯孤雁](https://hellogithub.com/en/user/gf67BzSc528eYP9)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1051789550.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[CordysCRM](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/1Panel-dev/CordysCRM)：New-generation Customer Relationship Management System.This is a CRM (Customer Relationship Management) platform built based on Spring Boot and Vue.js. It supports functions such as lead acquisition, business opportunity follow-up, and contract signing. It can also achieve AI enhancement by integrating SQLBot and MaxKB.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1043515641.png' style="max-width:80%; max-height=80%;"></img></p>

13、[reitti](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dedicatedcode/reitti)：Personal Footprint Analysis Platform for Java Development.This is a personal location tracking and analysis platform built based on Spring Boot and PostGIS, suitable for recording personal travel routes and geographical location information. It supports automatically identifying stay locations, analyzing travel routes, determining transportation methods, and presenting them in a time-axis + map mode.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/989939173.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
14、[cesium](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/CesiumGS/cesium)：JavaScript Library for 3D Geospatial Visualization.This project is a JavaScript library for creating interactive 3D globes and 2D maps on web pages, leveraging WebGL technology to accelerate graphics processing, offering a good rendering speed, capable of handling massive and dynamic data visualizations, supporting various data formats such as terrain and 3D Tiles, suitable for building Web applications for Geographic Information Systems (GIS).
```javascript
import { Viewer } from "cesium";
import "cesium/Build/Cesium/Widgets/widgets.css";

const viewer = new Viewer("cesiumContainer");
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/3606738.png' style="max-width:80%; max-height=80%;"></img></p>

15、[jsonrepair](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/josdejong/jsonrepair)：JavaScript Library for Automatically Compatible with Error JSON Format.This is a JavaScript library for fixing/parsing various error JSON formats. Unlike JSON.parse() which directly throws an exception when encountering format errors, it can automatically handle common JSON format issues such as missing quotes in key names, single quotes instead of double quotes, trailing commas, missing commas, and irregular line breaks.
```javascript
import { jsonrepair } from 'jsonrepair'

try {
  // The following is invalid JSON: is consists of JSON contents copied from 
  // a JavaScript code base, where the keys are missing double quotes, 
  // and strings are using single quotes:
  const json = "{name: 'John'}"
  
  const repaired = jsonrepair(json)
  
  console.log(repaired) // '{"name": "John"}'
} catch (err) {
  console.error(err)
}
```

16、[log-lottery](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LOG1997/log-lottery)：Cool 3D Sphere Annual Meeting Lottery Application.This is an annual meeting lottery tool built based on Three.js and Vue.js, supporting functions such as importing personnel lists, setting prizes/awards, playing background music, and temporary lottery.Shared by [@1：](https://hellogithub.com/en/user/EQPvVCA9NTGfnoR)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/738128540.png' style="max-width:80%; max-height=80%;"></img></p>

17、[openscreen](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/siddharthvaddem/openscreen)：Free and Open-source Screen Recording Tool.This is a free and open-source screen recording tool that can serve as a lightweight alternative to Screen Studio. It supports application recording, background modification, custom scaling duration, etc. and is suitable for Windows and macOS systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1073433866.png' style="max-width:80%; max-height=80%;"></img></p>

18、[stylex](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/facebook/stylex)：Easy-to-expand CSS-in-JS Solution.This project is a CSS-in-JS library open-sourced by Meta. It supports defining styles in JavaScript and automatically optimizes and extracts them into independent CSS files during compilation. This not only eliminates runtime performance overhead but also completely avoids style conflicts.Shared by [@IZRINO](https://hellogithub.com/en/user/eK0Bv1dmJPxnrwy)
```javascript
import * as stylex from '@stylexjs/stylex';

const styles = stylex.create({
  root: {
    padding: 10,
  },
  element: {
    backgroundColor: 'red',
  },
});

const styleProps = stylex.props(styles.root, styles.element);
```

### Kotlin
19、[librepods](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kavishdevar/librepods)：Bring AirPods Back to Life on Android Devices.This project enables users to use the advanced features of AirPods Pro/Max on Android devices, including active noise cancellation switching, ear detection, head pose control, and conversation awareness. However, it requires root permission and cooperation with Xposed.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/863717537.png' style="max-width:80%; max-height=80%;"></img></p>

20、[XMSLEEP](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Tosencen/XMSLEEP)：Open-source Android White Noise App.This is an Android app focused on playing white noise, providing various natural sounds such as rain, bonfire, thunder, cat purring, bird chirping, and night insects to help you relax, meditate and fall asleep.Shared by [@Tosencen](https://hellogithub.com/en/user/Gxvd2eIyHm54S9p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1089198514.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP
21、[Wallos](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ellite/Wallos)：Open Source Personal Subscription Management Platform.This is a self-hosted personal subscription management platform developed with PHP. It can intuitively display all subscribed service names, prices, payment cycles (month/year/week, etc.) and the remaining days until the next payment. It supports multiple notification methods and statistical analysis.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/701017456.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
22、[fastapi-best-practices](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zhanymkanov/fastapi-best-practices)：Best Practice Guide of FastAPI.This is a summary of the author's practical experience in developing applications with FastAPI in start-up companies for many years. The content covers project structure, asynchronous, Pydantic, Depends, data migration and other aspects.

23、[FindMy.py](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/malmeloo/FindMy.py)：Playing with Python Library of Find My Network.This is a Python library for querying Apple Find My Network, enabling developers to obtain real-time location information of official devices such as AirTag, iPhone, iPad, and self-made AirTag using Python code.

24、[localstack](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/localstack/localstack)：Local Simulation of AWS Cloud Services.This is a full-featured local AWS cloud service simulation framework that supports services such as Lambda, S3, DynamoDB, Kinesis, SQS, SNS, and API Gateway. With just one command, you can start a complete AWS service environment locally, solving the pain points of relying on AWS accounts and services during the development and debugging process.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/71948498.png' style="max-width:80%; max-height=80%;"></img></p>

25、[PythonRobotics](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AtsushiSakai/PythonRobotics)：Robot Algorithm Python Implementation Collection.This project brings together Python implementations of algorithms in the robotics field, covering technologies such as localization, SLAM, path planning, aerial navigation, robotic arms, bipedal robots, etc., and provides example code and visual demonstrations.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/54376220.gif' style="max-width:80%; max-height=80%;"></img></p>

26、[tiny8](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sql-hkr/tiny8)：Pure Python Implemented CPU Simulator.This project is a lightweight 8-bit CPU simulator written in Python. It can transform the abstract assembly language execution process into a visual and interactive learning experience. It also supports exporting the code execution process as GIF or MP4, which is suitable for teaching and learning in courses such as 'Computer Organization Principles' or 'Assembly Language'.
```python
from tiny8 import CPU, assemble_file

asm = assemble_file("fibonacci.asm")
cpu = CPU()
cpu.load_program(asm)
cpu.run(max_steps=1000)

print(f"Result: R17 = {cpu.read_reg(17)}")  # Final Fibonacci number
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1079950805.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust
27、[gitlogue](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/unhappychoice/gitlogue)：Replay Your Git Commit History.This is a command-line tool that can convert Git commit history into animations, vividly showing each change in the terminal through typing animations and code highlighting.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1092562478.gif' style="max-width:80%; max-height=80%;"></img></p>

28、[xan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/medialab/xan)：CSV Data Magician in the Terminal.This is a command-line tool capable of handling GB-sized CSV files. It supports operations such as previewing, filtering, slicing, aggregating, and sorting. Data visualization can be achieved in the terminal through histograms and heatmaps.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/140488417.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
29、[Petrichor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kushalpandya/Petrichor)：Elegant macOS Local Music Player.This is a carefully designed macOS local music player developed with Swift, supporting mainstream and lossless audio formats such as MP3, FLAC, and DSD. It focuses on offline scenarios with a clean interface, providing you with a pure music playing experience.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/969355437.png' style="max-width:80%; max-height=80%;"></img></p>

30、[ScrollSnap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Brkgng/ScrollSnap)：Mac Scroll Screenshot Tool.This is a tool designed to solve the problem that the native screenshot function of macOS does not support scrolling screenshots. You only need to select the specified area and then scroll the page to easily obtain a complete long screenshot.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/983779325.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
31、[char](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fastrepl/char)：Local-first AI Note and Meeting Assistant.This is a locally runnable AI intelligent note and meeting recording application. By integrating Ollama, it can complete voice transcription to summary generation locally. It supports functions such as meeting recording, real-time transcription, note organization and intelligent summary.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/900550981.png' style="max-width:80%; max-height=80%;"></img></p>

32、[cognee](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/topoteretes/cognee)：Out-of-the-box Intelligent Agent Memory Engine.This is a Python project specifically designed to provide memory functionality for AI agents. It integrates technologies such as graph databases, knowledge graphs, and vector databases. With just 5 lines of code, it can easily provide persistent and multimodal memory for AI agents, supporting the connection and retrieval of past conversations, documents, image and audio transcripts, etc.
```python
import cognee
import asyncio


async def main():
    # Add text to cognee
    await cognee.add("Natural language processing (NLP) is an interdisciplinary subfield of computer science and information retrieval.")

    # Generate the knowledge graph
    await cognee.cognify()

    # Query the knowledge graph
    results = await cognee.search("Tell me about NLP")

    # Display the results
    for result in results:
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/679343504.png' style="max-width:80%; max-height=80%;"></img></p>

33、[droidrun](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/droidrun/droidrun)：Control Your Phone with Natural Language.This is a mobile automation framework based on LLM Agents. It allows you to control Android devices or emulators through natural language. It supports mainstream large models such as DeepSeek, OpenAI, and Gemini. When using it, you need to install DroidRun Portal on your phone to collect UI information and execute operation commands. Then, the information is passed to the DroidRun framework on the computer through ADB. The framework interacts with the LLM and gives execution instructions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/965313467.gif' style="max-width:80%; max-height=80%;"></img></p>

34、[Everywhere](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/DearVa/Everywhere)：Handy AI Desktop Assistant.This is a context-aware desktop AI assistant that can automatically obtain and understand the content on the current screen without the need for screenshotting, copying content or switching applications. Just one click can summon the AI to perform tasks such as answering questions, translation and providing answers to doubts.Shared by [@Dear.Va](https://hellogithub.com/en/user/LNYEf6O9Qv5JeR2)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/971243074.png' style="max-width:80%; max-height=80%;"></img></p>

35、[next-ai-draw-io](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/DayuanJiang/next-ai-draw-io)：Let AI Draw Architecture Diagrams for You.This is a Web application built based on Next.js that integrates AI and draw.io chart drawing capabilities. Now you can directly generate, edit, and optimize flowcharts and architecture diagrams through conversations. It supports flowing effect connections, screenshot replication, and historical version functions.Shared by [@喜BFoCE](https://hellogithub.com/en/user/Fzr3vHc5AxqYUVj)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/953521037.gif' style="max-width:80%; max-height=80%;"></img></p>

### Other
36、[bash-screensavers](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/attogram/bash-screensavers)：Hacker-style Terminal Screen Saver Collection.This project provides 12 interesting command-line ASCII animations, including classic matrix code rain, infinite pipe maze, fireworks, etc.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1036073889.gif' style="max-width:80%; max-height=80%;"></img></p>

37、[espectre](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/francescopace/espectre)：Wi-Fi Signal-based Motion Monitoring System.This is a motion detection system based on Wi-Fi spectrum analysis (CSI), developed with an ESP32-S3 development board and costing around 10 euros. It realizes motion detection without cameras or microphones by analyzing the interference changes of the human body on Wi-Fi signals. It supports Home Assistant integration and is suitable for smart home automation scenarios such as turning on lights when people come and home security.Shared by [@LaoZ](https://hellogithub.com/en/user/LT1VF8UXAHRoheE)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1083590674.png' style="max-width:80%; max-height=80%;"></img></p>

38、[GreenWall](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zmrlft/GreenWall)：Customize GitHub Green Grid like Painting.This is a tool for customizing GitHub contribution wall (green wall). It allows you to easily create text, logos or any patterns through an intuitive drag-and-drop interface.Shared by [@ShiYi](https://hellogithub.com/en/user/ucwD1E5BxrhWt4J)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/1080902977.png' style="max-width:80%; max-height=80%;"></img></p>

39、[SO-ARM100](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TheRobotStudio/SO-ARM100)：Open Source and Low-Cost Manipulator.This project is an open-source low-cost manipulator jointly developed by TheRobotStudio and Hugging Face, including all the materials of the self-made SO-100 and SO-101 manipulators.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/798981945.png' style="max-width:80%; max-height=80%;"></img></p>

40、[vscode-pets](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tonybaloney/vscode-pets)：Raise a Pet in VSCode.This project allows you to raise one or more interactive electronic pets in the VSCode editor, with built-in cute cats, dogs, rubber ducks and other pets.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/116/341041243.gif' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub115.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub117.md">『Next』</a>
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
