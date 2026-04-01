# HelloGitHub Vol.96
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
1、[cosmopolitan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jart/cosmopolitan)：Making C a Language that Builds Once and Runs Anywhere. This tool allows programs written in the C language to be compiled into executables that can seamlessly run on various operating systems. It uses a self-contained binary file design to package all program dependencies into the executable, achieving true cross-platform operation. It supports mainstream operating systems such as Windows, macOS, and Linux.
```
// 编译
cosmocc -o hello hello.c
// 运行
./hello
// 调试
./hello --strace
./hello --ftrace
```

2、[linenoise](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/antirez/linenoise)：C Language Command Line Editing Library. This project is a single-file library written by the Redis author in C language to enhance the command-line interaction experience. The overall code is about 800 lines, lightweight and easy to grasp, providing single/multi-line editing modes, cursor movement left and right, up and down history roll, and command completion features.Shared by [@9Ajiang](https://hellogithub.com/en/user/SMTnPZI9BxYvVXr)

3、[xxHash](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Cyan4973/xxHash)：Ultra-Fast Non-Cryptographic Hash Algorithm. A hash algorithm is a method that converts input data of arbitrary length into a fixed-length hash value. xxHash is a non-cryptographic hash algorithm designed specifically for quick calculation of hash values for large datasets. It features excellent speed, zero dependencies, and superior distribution characteristics, supporting a streaming computation model and implementations in various programming languages. It is suitable for scenarios that require high computational performance for data integrity checks, data stream analysis, and key-value pair retrieval.
```c
#include <string.h>
#include "xxhash.h"
 
// Example for a function which hashes a null terminated string with XXH32().
XXH32_hash_t hash_string(const char* string, XXH32_hash_t seed)
{
    // NULL pointers are only valid if the length is zero
    size_t length = (string == NULL) ? 0 : strlen(string);
    return XXH32(string, length, seed);
}
```

### C#
4、[Snap.Hutao](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/DGP-Studio/Snap.Hutao)：Practical Multifunctional Genshin Impact Toolbox. This is a Genshin Impact toolbox specifically designed for the Windows platform, supporting multi-account switching, custom frame rate limits, wish records, achievement management, sign-in rewards, character data queries, and training calculators. It does not make any destructive modifications to the game client, only aiming to enhance the gaming experience for Genshin Impact players on the desktop platform.Shared by [@Masterain](https://hellogithub.com/en/user/0xVspWlUv3kdeX5)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/482734649.png' style="max-width:80%; max-height=80%;"></img></p>

5、[yarp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dotnet/yarp)：Microsoft's Open Source Reverse Proxy Toolkit. This project is a toolkit developed by the Microsoft team using C#, which provides core proxy functionality and can be used as a library and project template for creating reverse proxy servers, including a simple example of a reverse proxy server.

### C++
6、[ada](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ada-url/ada)：Blazing Fast URL Parsing Tool. This project is a C++ written URL parser that complies with the WHATWG specification, with parsing speed several times faster than curl. It has become the default URL parser for Node.js (versions 18.16.0 and above), note that it is for URL parsing only, not for making requests.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/579485798.png' style="max-width:80%; max-height=80%;"></img></p>

7、[keepassxc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/keepassxreboot/keepassxc)：An Open Source, Secure, Cross-Platform Password Manager. This project is a free, offline, ad-free password management tool developed with C++. It provides a simple and intuitive user interface that makes it easy to manage the account passwords for various applications/websites, and supports multi-platform, browser plugins, automatic filling, password generation, and other features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/52729242.png' style="max-width:80%; max-height=80%;"></img></p>

8、[TranslucentTB](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TranslucentTB/TranslucentTB)：Custom Transparency Tool for Windows Taskbar. This project is a tool developed in C++ to adjust the transparency of the Windows taskbar. It is compact, free, simple to use, supports 5 taskbar states, 6 dynamic modes, and is compatible with both Windows 10 and 11 operating systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/78483432.png' style="max-width:80%; max-height=80%;"></img></p>

9、[tugraph-db](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TuGraph-family/tugraph-db)：The Distributed Graph Database Behind Alipay. This project is a high-performance distributed graph database jointly developed by Ant Group and Tsinghua University, supporting transaction processing, terabyte-level large capacity, low latency search, and rapid graph analysis capabilities.

### CSS
10、[easings.net](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ai/easings.net)：CSS Easing Functions Cheat Sheet. Easing functions are used to control the speed of CSS animations. This project provides a series of elegant examples of easing functions, along with their effects.
```css
.block {
	transition: transform 0.6s cubic-bezier(0.7, 0, 0.84, 0);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/3796591.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
11、[codapi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nalgeon/codapi)：Go Service for Running Online Code Snippets. This project offers an API service capable of running code snippets for 30 programming languages online, including Python, TypeScript, C, and Go. It is used for showcasing interactive code examples in documentation and tutorials.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/723189658.png' style="max-width:80%; max-height=80%;"></img></p>

12、[focalboard](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mattermost-community/focalboard)：Open Source Project Management and Team Collaboration Tool. This is an open-source, multilingual, self-hosted project management tool that integrates features from Trello and Notion. It supports task management through Kanban boards, tables, and calendars, and offers features such as comment synchronization, file sharing, and user permissions. The tool also provides clients suitable for Windows, macOS, and Linux systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/301793434.jpg' style="max-width:80%; max-height=80%;"></img></p>

13、[go-pretty](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jedib0t/go-pretty)：Go Library for Beautifying Console Outputs. This is a library for enhancing the visual appeal of console outputs such as tables, lists, progress bars, and text. You can utilize it to display beautifully formatted tables, multi-level lists, and multi-task progress bars, among other content.

14、[gopeed](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GopeedLab/gopeed)：A High-Speed Downloader Developed with Go+Flutter. This downloader utilizes the Go language for its backend, which supports various protocols such as HTTP, BitTorrent, and Magnet, and implements high-speed concurrent downloads using coroutines. The frontend is developed using Flutter, providing clients that are compatible with platforms including Windows, macOS, Linux, Android, iOS, and Web.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/182502850.png' style="max-width:80%; max-height=80%;"></img></p>

15、[teleport](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gravitational/teleport)：A Go-written Enterprise-Level Open Source Bastion Host. This is a platform specifically designed to provide connection, authentication, access control, and secure auditing for infrastructure. It supports secure access to internal Linux servers, Kubernetes clusters, web applications, and PostgreSQL and MySQL databases. The platform employs an automatic certificate delivery method for authentication, eliminating the need to manage passwords and SSH keys on target machines. Moreover, users can easily use remote connection tools such as ssh, mysql, and kubectl to seamlessly access managed resources.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/31558937.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
16、[javers](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/javers/javers)：Java Library for Tracking Data History and Auditing. This project is a Java library that applies version control concepts to the management of data (Java objects) changes. It supports viewing the differences in complex object structures, preserving the history of modified data, and tracking object changes.Shared by [@猎隼丶止戈reNo7](https://hellogithub.com/en/user/Ew59HqRWjPe0zZO)

17、[source-code-hunter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/doocs/source-code-hunter)：Source Code Analysis of Commonly Used Frameworks in Internet Companies. This project offers a series of source code explanations for mainstream frameworks and middleware on the Internet, including the Spring Suite, Mybatis, Netty, Dubbo, and more.

### JavaScript
18、[aspoem](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/meetqy/aspoem)：Modernized Ancient Poetry Learning Website. This is a poetry website that prioritizes reading experience and UI, built with TypeScript, Next.js, and Tailwind CSS. It boasts a clean and refreshing interface along with attractive fonts, offering features such as pinyin, annotations, translations of ancient poems, and functions like mobile adaptation, search, and one-click sharing.Shared by [@meetqyhvkXU](https://hellogithub.com/en/user/5Flg6I2oHsSUdEk)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/733312562.png' style="max-width:80%; max-height=80%;"></img></p>

19、[MyIP](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jason5ng32/MyIP)：A Handy IP Toolkit. The author of this project is a product manager. This is his first Vue.js project completed with the help of ChatGPT. Through this project, you can view your own IP information (from multiple sources) online and perform tests for website availability, internet speed, MTR, DNS leaks, WebRTC, and more.Shared by [@Jason Ng](https://hellogithub.com/en/user/9CU82obLc56qzAg)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/722152303.png' style="max-width:80%; max-height=80%;"></img></p>

20、[nutui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jd-opensource/nutui)：JD Style Mobile Vue Component Library. This project is a mobile Vue component library open-sourced by JD.com, designed specifically for mobile H5 and mini-program development scenarios. It includes over 80 high-quality components, supporting features such as on-demand reference, TypeScript, and internationalization.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/118392397.png' style="max-width:80%; max-height=80%;"></img></p>

21、[pikachu-volleyball](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gorisanson/pikachu-volleyball)：Pikachu Volleyball Game implemented with JavaScript. This project reverse-engineers the original Pikachu volleyball game and reconstructs it using JavaScript, including the physics engine and AI opponents.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/243930206.png' style="max-width:80%; max-height=80%;"></img></p>

22、[wasp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wasp-lang/wasp)：A Rails-like Full-stack Web Framework with React and Node.js. This project is a full-stack web framework aimed at web developers, where developers only need to write a simple .wasp configuration file to automatically generate a web application built on React and Node.js, and it comes with built-in features such as database, authentication, and routing.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/237222619.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
23、[marker](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/datalab-to/marker)：Project for Converting PDF to Markdown File. This is a Python project capable of converting PDF, EPUB, and MOBI formatted files into Markdown files. Compared to Nougat, it offers faster speed and higher accuracy, providing optimal results when handling English content, though the processing of Chinese can be less effective.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/712111618.png' style="max-width:80%; max-height=80%;"></img></p>

24、[Paper-Piano](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Mayuresh1611/Paper-Piano)：Play Piano on Paper. This project utilizes Python and OpenCV for image processing and recognition. It captures finger movements and the shadows beneath them through a camera, allowing users to play the piano by touching paper.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/768431034.png' style="max-width:80%; max-height=80%;"></img></p>

25、[pelican](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/getpelican/pelican)：A Static Site Generator for the Python Language. This is a static site generator written in Python, allowing you to create websites by writing text files in formats such as Markdown or reStructuredText. It supports features like RSS generation, syntax highlighting for code, and plugin extensions.

26、[posthog](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PostHog/posthog)：Open Source Product Analytics Platform. This is a product analytics and user tracking platform built with Django. It offers a suite of features, including event tracking, funnel analysis, cohort analysis, A/B testing, and more, suitable for understanding user behavior and improving product experience scenarios.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/235901813.png' style="max-width:80%; max-height=80%;"></img></p>

27、[taipy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Avaiga/taipy)：Quickly Build Data-Driven Web Applications. This project, based on Python and Flask, leverages front-end technologies like React to provide developers with a concise and efficient development framework. It simplifies the development processes of data handling, API development, and user interface construction. Whether you are a data scientist, machine learning engineer, or web developer, you can utilize Taipy to quickly complete the entire cycle from prototype to web application.Shared by [@刘三非](https://hellogithub.com/en/user/VhrXCAs7cMxL08W)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/460914281.gif' style="max-width:80%; max-height=80%;"></img></p>

### Rust
28、[genact](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/svenstaro/genact)：Busy Pretense Idler. This project simulates a busy facade on the terminal, such as compiling, scanning, downloading, etc. These actions are all fake and effectively no operation is performed, so they will not impact your computer, and it is compatible with Windows, Linux, and macOS operating systems.Shared by [@39499740](https://hellogithub.com/en/user/7eRBdwFSrtPxipV)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/1345495.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[rnote](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/flxzt/rnote)：Cross-Platform Handwriting Notes and Drawing Application. This is a drawing application written in Rust and GTK4, which can be used for sketching, handwriting notes, and annotating documents. It supports the import/export of PDF and image files, as well as unlimited canvas, drag and drop, and auto-saving features. It is suitable for Windows, Linux, and macOS systems and should be used with a drawing tablet.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/393045142.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
30、[Applite](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/milanvarady/Applite)：Desktop Application for Homebrew Cask. This is a free macOS application developed with Swift, providing a graphical user interface for Homebrew Cask, enabling one-click installation, updates, and uninstallation of applications.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/674388699.png' style="max-width:80%; max-height=80%;"></img></p>

31、[BLEUnlock](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ts1/BLEUnlock)：Unlock Your Mac Using a Bluetooth Device. This tool enables the unlocking and locking of a Mac computer via Bluetooth devices on macOS. No applications need to be installed on the Bluetooth device for it to work. When the Bluetooth device is in proximity to the Mac, it can unlock the screen and wake up the computer; whereas, when the device is out of range, it automatically locks the screen and pauses video or music playback. It supports devices like iPhone, Apple Watch, and Bluetooth earphones.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/183878515.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
32、[FastChat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lm-sys/FastChat)：Open Platform for Training and Evaluating Large Language Models. This platform is designed for training, deploying, and evaluating large language models, allowing you to deploy and assess various large models locally. In addition, it offers an online platform for evaluating large models, where users can ask the same question to two different large models and then choose the one they believe is better to use based on the responses. During this process, you can use dialogue bots like Claude and ChatGPT for free.Shared by [@浮生若夢](https://hellogithub.com/en/user/hKmH64UjOdwgCEi)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/615882673.png' style="max-width:80%; max-height=80%;"></img></p>

33、[generative-ai-for-beginners](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/generative-ai-for-beginners)：Generative AI Tutorial for Beginners. This is a free course on generative AI for beginners, open-sourced by Microsoft. The course is divided into 18 sections, covering everything you need to know to create a generative AI application, including an introduction to generative AI and Large Language Models (LLMs), prompt crafting, building text generation applications, chat applications, image generation applications, and vector database topics.

34、[jan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/janhq/jan)：All-in-One Desktop App for LLMs Experience. This is an AI dialogue desktop application that supports running open-source LLMs locally and connecting to ChatGPT services. It is ready to use out of the box, features a clean interface, and is not hardware specific. It supports proxy settings, accessing ChatGPT, one-click download/connection of models adapted to the current system configuration, offline operation, and is compatible with Windows, Linux, and macOS operating systems.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/679506386.png' style="max-width:80%; max-height=80%;"></img></p>

35、[open-interpreter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/openinterpreter/open-interpreter)：Run Code on Your Computer with LLM. This project allows large language models to run code locally, supporting programming languages such as Python, JavaScript, and Shell. It acts as a natural language interpreter, converting spoken or written instructions into the corresponding code scripts and executing them. After installation, users can operate their computer through terminal chat, for example, creating and editing images, videos, and files, or controlling the Chrome browser to perform searches.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/666299222.gif' style="max-width:80%; max-height=80%;"></img></p>

### Other
36、[candle](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mitxela/candle)：DIY 3D Electronic Candle. The project author has created a miniature electronic candle using a simple LED board and a small circuit board, and simulated a 3D candlelight effect by using a rotating base and fluid simulation algorithms.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/726135770.gif' style="max-width:80%; max-height=80%;"></img></p>

37、[docker-android](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/budtmo/docker-android)：Android in Docker Containers. This is a Docker image of an Android emulator that supports versions 9 to 14, VNC (Remote Desktop), ADB (Android Debug Bridge), and log viewing capabilities, suitable for scenarios such as Android client testing and debugging.
```
docker run -d -p 6080:6080 \
-e EMULATOR_DEVICE="Samsung Galaxy S10" \
-e WEB_VNC=true \
--device /dev/kvm \
--name android-container \
budtmo/docker-android:emulator_11.0
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/77145066.png' style="max-width:80%; max-height=80%;"></img></p>

38、[excelCPU](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/InkboxSoftware/excelCPU)：Building a CPU with Only Excel. This project is a 16-bit CPU processor running in an Excel file, featuring a 3Hz clock speed, 128KB RAM, and a 128x128 pixel display screen. For this, the author also developed an assembly language.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/748991484.png' style="max-width:80%; max-height=80%;"></img></p>

39、[Mr.-Ranedeer-AI-Tutor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)：Craft Your Personalized AI Tutor. This project enables an AI chatbot to act as a teacher and study assistant by using prompt words to generate study plans, teach complex concepts, create exercises, and more. You can also select different teaching styles and depths. It is compatible with any large model, with the author recommending GPT-4 for the best results.
```
===
Author: JushBJJ
Name: "Mr. Ranedeer 提示词"
Version: 2.7
===

[Student Configuration]
    🎯Depth: Highschool
    🧠Learning-Style: Active
    🗣️Communication-Style: Socratic
    🌟Tone-Style: Encouraging
    🔎Reasoning-Framework: Causal
    😀Emojis: Enabled (Default)
    🌐Language: English (Default)

    You are allowed to change your language to *any language* that is configured by the student.

[Overall Rules to follow]
    1. Use emojis to make the content engaging
    2. Use bolded text to emphasize important points
    3. Do not compress your responses
    4. You can talk in any language
...
```

40、[ugly-avatar](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/txstc55/ugly-avatar)：Ugly Avatar Generator. This project can be used to randomly generate an extremely unattractive hand-drawn avatar. Don't doubt it, it really is very ugly and abstract, purely for entertainment.Shared by [@puz_zle](https://hellogithub.com/en/user/hpUacD34bC7zAgw)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/777080032.png' style="max-width:80%; max-height=80%;"></img></p>

### Book
41、[Real-Time-Rendering-4th-CN](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Morakito/Real-Time-Rendering-4th-CN)：Chinese Translation of 'Real-Time Rendering 4th'. This project is the Chinese translation of the fourth edition of 'Real-Time Rendering', a classic in the field of real-time rendering, which is ideal for developers engaged in game development, 3D graphics, VR/AR, and related fields for learning.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img3/master/hellogithub/96/721135559.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub95.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub97.md">『Next』</a>
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


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
