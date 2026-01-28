# HelloGitHub Vol.112
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
1、[AltSnap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/RamonUnch/AltSnap)：Windows Global Alt Key Window Manager.This is a tool that replicates the efficient window management method in Linux systems onto the Windows platform. You only need to hold the Alt key and you can easily drag, scale and dock windows with the mouse at any position. Say goodbye to the traditional cumbersome operations of searching and clicking on the title bar and border.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/315453540.png' style="max-width:80%; max-height=80%;"></img></p>

2、[libpostal](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/openvenues/libpostal)：Global Address Format Compatibility Parsing Library.This project is a global address parsing library written in C language, supporting address strings in multiple languages, formats and countries. It can convert address information into structured data.
```c
#include <stdio.h>
#include <stdlib.h>
#include <libpostal/libpostal.h>

int main(int argc, char **argv) {
    // Setup (only called once at the beginning of your program)
    if (!libpostal_setup() || !libpostal_setup_parser()) {
        exit(EXIT_FAILURE);
    }

    libpostal_address_parser_options_t options = libpostal_get_address_parser_default_options();
    libpostal_address_parser_response_t *parsed = libpostal_parse_address("781 Franklin Ave Crown Heights Brooklyn NYC NY 11216 USA", options);

    for (size_t i = 0; i < parsed->num_components; i++) {
        printf("%s: %s\n", parsed->labels[i], parsed->components[i]);
    }

    // Free parse result
    libpostal_address_parser_response_destroy(parsed);

    // Teardown (only called once at the end of your program)
    libpostal_teardown();
    libpostal_teardown_parser();
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/31570906.gif' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[dlss-swapper](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/beeradmoore/dlss-swapper)：Tool for Switching Game DLSS Versions without Update.This is a tool for managing and replacing DLSS, FSR and XeSS DLL files of games, supporting mainstream game platforms such as Steam, GOG and Epic Games. It can upgrade or downgrade the DLSS, FSR and XeSS versions of games without updating the games, thus optimizing the game graphics and performance.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/393538656.gif' style="max-width:80%; max-height=80%;"></img></p>

4、[Mate-Engine](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shinyflvre/Mate-Engine)：Open-source VRM Desktop Virtual Companion.This is an open-source desktop virtual companion application that can serve as an open-source alternative to Desktop Mate. It supports placing custom 3D virtual characters on the desktop and has built-in smooth idle animations, click interactions, dancing with music, and other functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/951665915.jpg' style="max-width:80%; max-height=80%;"></img></p>

### C++
5、[d2mcpp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mcpp-community/d2mcpp)：Hands-on Learning of Modern C++ Language Features.This is a completely open-source interactive tutorial on modern C++ language features. It breaks down the core language features of C++11 (such as type deduction, move semantics, etc.) into runnable mini-exercises. Through the self-developed xlings tool, it realizes functions such as one-click installation of dependencies and real-time judgment of questions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/964948225.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[LunaTranslator](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/HIllya51/LunaTranslator)：Open-source Visual Novel Translation Tool.This is a visual novel (Galgame) translator designed specifically for the Windows platform. It supports multiple text extraction methods such as HOOK, OCR, and clipboard, which can be switched flexibly. It also provides functions such as online translation, offline translation, and speech synthesis.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/542386106.png' style="max-width:80%; max-height=80%;"></img></p>

7、[WindowsAppSDK](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/WindowsAppSDK)：SDK to Infuse New Vitality into Old Desktop Applications.This project is an official open-source Windows desktop application development component and toolkit by Microsoft, aiming to assist traditional Win32, WPF, WinForms, etc. applications in easily integrating the latest Windows UI and platform features. Just by introducing a NuGet package, it can bring more beautiful UI and features such as push notifications and rounded windows to the original application.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/256049233.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
8、[evcc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/evcc-io/evcc)：Personal Electric Vehicle Charging Intelligent Management Platform.This is an open-source EV (Electric Vehicle) charger control platform that provides flexible and easy-to-install charging solutions for electric vehicle owners. It offers a visual and mobile-friendly web platform through which users can remotely start, stop and monitor the charging status of their vehicles. It supports multiple charging devices and vehicle models. The intelligent charging function can also intelligently schedule charging times according to electricity prices, solar energy storage and schedules, thereby saving electricity costs.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/226368338.png' style="max-width:80%; max-height=80%;"></img></p>

9、[genai-toolbox](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/googleapis/genai-toolbox)：Google Open-Sourced Database MCP Tool.This project is the MCP server open-sourced by Google, specifically designed to provide a unified, secure, and scalable data access layer between LLM applications and various databases. It integrates functions such as connection pooling, authentication, and monitoring, enabling AI agents to quickly acquire the ability to query databases and supports multiple databases such as PostgreSQL and MySQL.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/812044182.png' style="max-width:80%; max-height=80%;"></img></p>

10、[gpt-load](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tbphp/gpt-load)：Enterprise-level Multi-channel Large Model API Management Platform.This is an enterprise-level large model interface management platform developed with Go language, supporting multiple services such as OpenAI, Gemini, and Claude. It is ready-to-use, with a built-in web management interface and retention of the native API format. It supports automatic key polling, fault switching, and horizontal scaling, and is designed specifically for high-concurrency production environments.Shared by [@tbphp](https://hellogithub.com/en/user/Qlh8vzrWJ0HCneG)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/997490512.png' style="max-width:80%; max-height=80%;"></img></p>

11、[zenta](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/e6a5/zenta)：Quickly Recover Concentration Command Line Tool.This is a Go language-developed command line tool designed to help developers regain focus and inner peace quickly through simple breathing exercises when they are distracted or lack concentration.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1008849671.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[javacv](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bytedeco/javacv)：Versatile Computer Vision Java Library.This project enables developers to directly call commonly used computer vision libraries such as OpenCV, FFmpeg, and Tesseract on the Java Virtual Machine (JVM), quickly developing functional modules such as real-time image analysis, video encoding and decoding, streaming, and OCR.
```java
import org.bytedeco.opencv.opencv_core.*;
import org.bytedeco.opencv.opencv_imgproc.*;
import static org.bytedeco.opencv.global.opencv_core.*;
import static org.bytedeco.opencv.global.opencv_imgproc.*;
import static org.bytedeco.opencv.global.opencv_imgcodecs.*;

public class Smoother {
    public static void smooth(String filename) {
        Mat image = imread(filename);
        if (image != null) {
            GaussianBlur(image, image, new Size(3, 3), 0);
            imwrite(filename, image);
        }
    }
}
```

13、[JsonPath](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/json-path/JsonPath)：Easily Read and Write JSON like XML.This project provides Java developers with a path query-like approach, allowing them to easily extract data from complex JSON structures and locate target nodes without manual traversal.Shared by [@塔咖](https://hellogithub.com/en/user/bzJpGyu0IanC6L7)
```java
String json = "...";
Object document = Configuration.defaultConfiguration().jsonProvider().parse(json);

String author0 = JsonPath.read(document, "$.store.book[0].author");
String author1 = JsonPath.read(document, "$.store.book[1].author");
```

14、[nifi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/apache/nifi)：Visual Drag-and-Drop Data Flow Management Platform.This is a data flow management system based on the concept of process programming. It provides a visual web management interface and supports data lineage, breakpoint continuation, flexible expansion and rich processors. Users can design, control and monitor the data flow between systems like drawing a flowchart. It is suitable for scenarios such as data lakes, real-time risk control and AI data pipelines.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/27911088.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
15、[base-ui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mui/base-ui)：Easily Customizable Styleless React Component Library.This project provides a set of basic, styless React components that only contain necessary functional logic and do not come with any preset styles. It helps developers get rid of the style constraints of traditional UI libraries and does not need to spend a lot of effort to cover and modify default styles.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/762289766.png' style="max-width:80%; max-height=80%;"></img></p>

16、[cap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tiagozip/cap)：Lightweight CAPTCHA Alternative.This is a lightweight, open-source CAPTCHA solution suitable for preventing robot abuse and data scraping. It is based on SHA-256 Proof-of-Work technology, easy to integrate and plug-and-play, providing a self-hosted anti-abuse verification mechanism for websites.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/915378930.png' style="max-width:80%; max-height=80%;"></img></p>

17、[drawnix](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/plait-board/drawnix)：Minimalist Online Whiteboard Tool.This is a free and open-source online whiteboard tool. It provides an infinite canvas and supports free drawing, mind mapping, flowcharts, pens, image insertion, automatic saving and other functions, as well as mobile adaptation, Docker deployment and plugin mechanism and other features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/810364325.png' style="max-width:80%; max-height=80%;"></img></p>

18、[FossFLOW](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/stan-smith/FossFLOW)：Open Source Pseudo 3D Graph Drawing Tool.This is a drawing tool specifically designed for creating professional isometric infrastructure diagrams. It supports offline use. Isometric diagrams present 3D effects in a 2D form, enabling a more intuitive and accurate display of complex designs and system architectures.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1011253718.png' style="max-width:80%; max-height=80%;"></img></p>

19、[snapdom](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zumerlab/snapdom)：Precise Web Content Screenshot Library.This is an efficient JavaScript library for web screenshots. It can quickly and accurately convert any DOM element on a web page into a high-quality image and supports exporting in PNG, JPG, WebP or Canvas formats. It is suitable for web automation testing, generating preview images, content saving and other scenarios.Shared by [@Yee1014](https://hellogithub.com/en/user/1B5n92jVikAMPpc)
```javascript
const el = document.querySelector('#target');
const result = await snapdom(el, { scale: 2 });

const img = await result.toPng();
document.body.appendChild(img);

await result.download({ format: 'jpg', filename: 'my-capture' });
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/973606777.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
20、[Iconify](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Mahmud0808/Iconify)：Deeply Customize Your Android System Interface.This is a powerful Android system-level beautification tool designed specifically for Pixel or AOSP-like ROMs on Android 12 and above. It supports in-depth customization and modification of the device's user interface (UI), including but not limited to status bar icons (such as Wi-Fi, signal), system icons, icon shapes, lock screen clock styles, notification panel layout and colors.Shared by [@ewiro](https://hellogithub.com/en/user/iItGgWoJjnLsr0Y)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/529537665.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
21、[jupyterlite](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jupyterlite/jupyterlite)：JupyterLab Running in Browser.This is a JupyterLab that runs entirely in the browser without the need to install Python or configure a server. It provides an online interactive Python programming environment and can be deployed as static files to any static website hosting platform (such as GitHub Pages).

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/352160885.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[mediacms](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mediacms-io/mediacms)：Django-based Online Video Platform.This is a video content management platform built with Django and React, which can quickly set up medium and small-sized video websites. It has built-in transcoding, search, playlist, permission management and mobile adaptation functions, and supports multimedia formats such as video, audio, image and PDF.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/321785127.jpg' style="max-width:80%; max-height=80%;"></img></p>

23、[requests-futures](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ross/requests-futures)：Elegant Asynchronous Python HTTP Request Library.This is a lightweight wrapper library that provides asynchronous HTTP requests for the Python requests library. It combines the ease of use of the requests library with the concurrency capabilities of the standard library concurrent.futures. It supports sending single or multiple HTTP requests in a non-blocking manner, thereby significantly improving the performance of I/O-intensive applications.
```python
from concurrent.futures import as_completed
from pprint import pprint
from requests_futures.sessions import FuturesSession

session = FuturesSession()

futures=[session.get(f'http://httpbin.org/get?{i}') for i in range(3)]

for future in as_completed(futures):
    resp = future.result()
    pprint({
        'url': resp.request.url,
        'content': resp.json(),
    })
```

24、[UavNetSim-v1](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Zihao-Felix-Zhou/UavNetSim-v1)：Drone Communication Network Simulation Platform.This is a Python (SimPy)-based drone communication network simulation platform designed specifically for organizing drone cluster communication. It provides multiple levels of the drone network (such as network layer, MAC layer, physical layer), as well as comprehensive modeling of drone mobility and energy models, and is suitable for protocol design, performance evaluation and visual analysis of drone networks.Shared by [@凝望，划过星空](https://hellogithub.com/en/user/yc7sS80jimthluU)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/955363828.png' style="max-width:80%; max-height=80%;"></img></p>

25、[ZSim](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ZSim-Dev/ZSim)：Zero District Zero Battle Simulator.This is a damage simulation and combat simulation tool specifically designed for the game 'Zero District Zero'. It supports full-auto simulation, visual reports, custom API and other functions. Players can freely choose characters and equipment in the game and configure attribute parameters, and then calculate the expected damage under specific team combinations through the simulator.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1012686024.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust
26、[rustfs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rustfs/rustfs)：High-performance Distributed Storage System Based on Rust.This is a high-performance distributed object storage system built with Rust, aiming to be an open-source alternative to MinIO. It is easy to install and compatible with the S3 protocol. It adopts a more friendly open-source protocol and has a built-in web management background with a clean interface. At the same time, it supports domestic secure devices and systems and is suitable for scenarios such as massive data storage, big data, the Internet, industry, and secure storage.Shared by [@SR.李](https://hellogithub.com/en/user/vQ0IpLkHo3T9lO1)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/722597620.png' style="max-width:80%; max-height=80%;"></img></p>

27、[tabiew](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shshemi/tabiew)：Command Line Data File Visualization Browsing Tool.This is a command-line tool for browsing and querying tabular data files such as CSV, Parquet, Arrow, Excel, etc. It provides interactive interface experience, supports SQL queries, multi-table operations, fuzzy search and Vim-style shortcut keys and other functions.Shared by [@HBSpy](https://hellogithub.com/en/user/rIXCy0ZT2L49Ysj)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/792805133.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift
28、[KeyboardCowboy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zenangst/KeyboardCowboy)：Reshape Your macOS Shortcuts.This is a keyboard workflow tool that can reshape the macOS shortcut experience. It can create powerful and context-aware shortcuts for any application without manual triggering. It can not only simulate clicking buttons without native shortcuts and selecting menu items, but also string multiple steps into an efficient process that can be executed with one click, improving workflow efficiency.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/292346804.png' style="max-width:80%; max-height=80%;"></img></p>

29、[TrackWeight](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/KrishKrosh/TrackWeight)：MacBook Touchpad Transforms into an Electronic Scale.This is a fun macOS application that turns the MacBook touchpad into a digital electronic scale. It utilizes the built-in Force Touch pressure sensor of the touchpad. Simply place an object on the touchpad, and the application can display its weight in real time.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1023406764.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
30、[gitingest](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/coderamp-labs/gitingest)：Tool for Instantly Converting Codebase to AI-friendly Format.This project can quickly convert any GitHub repository into a plain text summary suitable for large language models. It is very easy to use. Just replace 'hub' in the GitHub project address with 'ingest' to get the text summary.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/895942941.png' style="max-width:80%; max-height=80%;"></img></p>

31、[ManimML](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/helblazer811/ManimML)：Dynamically Demonstrating Neural Networks with Python.This is a Python library based on Manim, used to create animations and visualizations of machine learning-related concepts. Just write simple Python code to easily generate animation effects such as neural network structures, convolutional operations, and Dropout processes, helping to understand and present complex machine learning principles.
```python
from manim_ml.neural_network import NeuralNetwork, FeedForwardLayer

nn = NeuralNetwork([
    FeedForwardLayer(num_nodes=3),
    FeedForwardLayer(num_nodes=5),
    FeedForwardLayer(num_nodes=3)
])
self.add(nn)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/454906591.gif' style="max-width:80%; max-height=80%;"></img></p>

32、[unsloth](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/unslothai/unsloth)：Beginner-Friendly LLM Fine-Tuning Toolkit.This project is a Python toolkit for fine-tuning and optimizing large language models (LLMs). It enhances the speed of model fine-tuning through dynamic quantization and memory optimization techniques, while reducing GPU memory usage by 70%-80%. It supports a variety of hardware configurations, LLMs, and ultra-long context tasks. In addition, it provides Jupyter Notebook examples that can be experienced online directly, lowering the barrier to entry for fine-tuning large models.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/725205304.png' style="max-width:80%; max-height=80%;"></img></p>

33、[uzu](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/trymirai/uzu)：High-performance AI Inference Engine Exclusive to MacBook.This is a high-performance and lightweight AI model inference engine specifically designed for Apple M series chips. It fully utilizes the characteristics of Apple hardware to enhance inference speed and provides a simple and easy-to-use API to help you deploy efficient local large model services with one click.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1007360921.png' style="max-width:80%; max-height=80%;"></img></p>

34、[VideoCaptioner](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/WEIFENG2333/VideoCaptioner)：Out-of-the-box Intelligent Caption Assistant.This is an intelligent video caption processing tool based on large language models. It has a simple interface and convenient operation, supporting functions such as speech recognition, intelligent proofreading and automatic generation of multilingual subtitles.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/881171866.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Other
35、[12-factor-agents](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/humanlayer/12-factor-agents)：Design Guidelines for Building Production-Level LLM Applications.This is a design guide written for building production-level large model applications. After communicating with many excellent founders in the AI field, the author has提炼出 (extracted) 12 systematic and practical design principles.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/957658915.png' style="max-width:80%; max-height=80%;"></img></p>

36、[60s](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vikiboss/60s)：Daily 60-second Information API Collection.This project gathers API services including daily news, real-time box office, exchange rates, hot search lists, random jokes and other various data.

37、[bitwise-challenge-2048](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/izabera/bitwise-challenge-2048)：2048 Game Based on Bitwise Operations.This is a classic 2048 game implemented through bitwise operations. It consists of only one file (.bash), with zero dependencies and less than 200 lines of code. Different from the common way of simulating the game board with a two-dimensional array, this project cleverly uses bitwise operations to manage the game state and logic. The entire 4x4 game board is compressed and stored in a 64-bit integer, and all movements, merges and generations are achieved through bit operations.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/1004964759.png' style="max-width:80%; max-height=80%;"></img></p>

38、[CSS-Minecraft](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/BenjaminAster/CSS-Minecraft)：This 'World' Only Has HTML and CSS.This project achieved an interface interaction similar to Minecraft using only CSS and HTML, without a single line of JavaScript code. It supports basic operations such as placing, removing, and switching perspectives of blocks.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/562157524.png' style="max-width:80%; max-height=80%;"></img></p>

39、[pomodoro](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Rukenshia/pomodoro)：Self-made Electronic Ink Display Pomodoro Clock.This is a physical pomodoro timer based on ESP32, equipped with a 4.26-inch black and white ePaper screen and a knob operation. The working and rest time can be quickly set by rotating the knob, and pressing the knob can start timing immediately.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/956984646.png' style="max-width:80%; max-height=80%;"></img></p>

40、[scriptcat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/scriptscat/scriptcat)：Browser Plugin for Executing User Scripts.This is an open-source browser plugin that allows users to install and run third-party JavaScript code snippets. It can be used in scenarios such as blocking ads, enhancing website functions, and automating web page operations.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/327265659.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
41、[book](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/crypto101/book)：Crypto 101: An Introduction to Cryptography.This is an introductory book on cryptography for programmers. It starts with XOR and one-time pads and gradually explains symmetric encryption, public-key encryption, hashes, MACs, signatures, key exchange, random numbers and other cryptography 'building blocks', and assembles them into real systems such as TLS, OpenPGP and OTR.

42、[ThinkStats](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AllenDowney/ThinkStats)：Think Stats.This is an e-book on statistics for programmers. All code examples and exercises are implemented in Python. The whole book focuses on real data sets and uses statistical thinking to solve practical problems through statistical methods such as exploratory data analysis, probability distribution, hypothesis testing, correlation and regression analysis.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/112/815214314.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub111.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub113.md">『Next』</a>
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
