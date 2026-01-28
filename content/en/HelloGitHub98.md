# HelloGitHub Vol.98
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
1、[cmus](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cmus/cmus)：Compact Command Line Music Player. This is a lightweight command line music player designed for Unix-like systems that can play local music files. It is simple to use, resource-efficient, and starts up quickly, supporting multiple audio formats.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/7365136.png' style="max-width:80%; max-height=80%;"></img></p>

2、[Remotery](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Celtoys/Remotery)：Lightweight Remote Real-Time CPU/GPU Profiler. This project is a tool for monitoring multi-thread activities on CPUs and GPUs. It provides a C file that can be easily integrated into projects and comes with a real-time monitoring web interface, allowing remote observation and analysis of program performance through a browser. Suitable for scenarios such as monitoring real-time operational performance of games and analyzing performance of mobile applications.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/17664381.gif' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[RunCat365](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Kyome22/RunCat365)：A 'Kitten' Running on the Windows Taskbar. This is a small utility written in C# that displays an animated kitten running on the Windows taskbar, which runs faster with the higher the CPU usage.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/285618804.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++
4、[caesium-image-compressor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Lymphatus/caesium-image-compressor)：Free Image Compression Software. This is an image compression tool written in C++ with a simple Chinese interface. It supports lossless compression of JPG, PNG, and WebP formats, and is equipped with real-time preview and batch processing capabilities. In addition, it also provides clients for Windows, Linux, and macOS, as well as a web version that does not require installation.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/48986680.png' style="max-width:80%; max-height=80%;"></img></p>

5、[concurrentqueue](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cameron314/concurrentqueue)：High-Performance Lock-Free Concurrent Queue in C++. This project is a fast, lock-free, concurrent queue written in C++11, supporting multiple threads to perform producer and consumer operations simultaneously. It features the absence of locks and only requires a single header file, making it suitable for various scenarios that require high-performance concurrency processing.
```c++
#include "concurrentqueue.h"

moodycamel::ConcurrentQueue<int> q;
q.enqueue(25);

int item;
bool found = q.try_dequeue(item);
assert(found && item == 25);
```

6、[input-overlay](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/univrsal/input-overlay)：OBS Streaming Plugin to Display User Input Operations. This project is a plugin for live streaming that displays keyboard presses, mouse movements, and game controller button actions, suitable for OBS streaming software on Windows and Linux. It can be used in scenarios such as gaming live streams and educational demonstrations.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/99977220.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
7、[fscan](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/shadow1ng/fscan)：Open Source Internal Network Security Scanning Tool. This project is an internal network scanning tool developed using the Go language, offering one-click automated comprehensive vulnerability scanning. It is user-friendly and comprehensive, supporting functions such as port scanning, common server brute force attacks, web application vulnerability scanning, and NetBIOS sniffing.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/312629343.png' style="max-width:80%; max-height=80%;"></img></p>

8、[go-humanize](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dustin/go-humanize)：A Go Language Library for Making Numbers and Time Easier to Understand. This is a Go language library that provides humanized numbers and time. By offering formatting functions, it helps developers convert figures such as size and time into a form that is more easily understandable by humans, such as file sizes, relative times, comma-separated numbers, and ordinals.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)
```go
fmt.Printf("That file is %s.", humanize.Bytes(82854982)) // That file is 83 MB.
fmt.Printf("This was touched %s.", humanize.Time(someTimeInstance)) // This was touched 7 hours ago.
```

9、[mactop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/context-labs/mactop)：Mac Performance Monitoring Tool Tailored for Apple Silicon. This project implements a tool similar to the top command with less than 1k lines of Go code. It can display real-time performance metrics of Apple M-series chips, including CPU and GPU usage, memory, network, and disk information.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/789247155.png' style="max-width:80%; max-height=80%;"></img></p>

10、[micro](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/micro-editor/micro)：Modern Terminal Text Editor. This project is a terminal-based text editor written in Go, which serves as an alternative to Nano. It is ready to use upon download, requires no configuration, and is cross-platform with support for multi-cursor editing, syntax highlighting, mouse operations, plugin extensions, and more, making it especially suitable for text editing tasks when remotely accessing servers via SSH.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/53632140.png' style="max-width:80%; max-height=80%;"></img></p>

11、[superfile](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yorukot/superfile)：Very Beautiful Terminal File Manager. This is a modern terminal file manager that provides an intuitive and beautiful interface for command-line file operations. It defaults to Vim-style shortcut operations and also supports plugin and theme customization.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/774468912.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[Acode](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Acode-Foundation/Acode)：Code Editor for Android Devices. This is a code editing tool specifically designed for Android devices. It is a lightweight web-based IDE with features such as instant preview, console, and a rich set of plugins, supporting a variety of programming languages like HTML, Python, Java, JavaScript, and more.Shared by [@虾华](https://hellogithub.com/en/user/ckl6eKxwCuRyVJI)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/217150613.png' style="max-width:80%; max-height=80%;"></img></p>

13、[blossom](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/blossom-editor/blossom)：Private Cloud-based Bi-directional Linking Note Software. This is a cloud storage note software that supports private deployment. It allows you to save all your notes, images, and personal plans on your private server and achieve real-time synchronization across devices. The software provides features such as Markdown editing, bidirectional linking, full backup, web page conversion, multi-account permissions, and statistics, and is compatible with Windows, macOS, and web-based clients.Shared by [@猎隼丶止戈reNo7](https://hellogithub.com/en/user/Ew59HqRWjPe0zZO)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/675481198.png' style="max-width:80%; max-height=80%;"></img></p>

14、[JSqlParser](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/JSQLParser/JSqlParser)：Java Library for Parsing SQL Statements. This project can read SQL statements and break them down into structured Java objects, enabling the parsing or dynamic generation of SQL statements with Java code, and supports SQL standards and mainstream relational databases.
```java
String sqlStr = "select 1 from dual where a=b";

PlainSelect select = (PlainSelect) CCJSqlParserUtil.parse(sqlStr);

SelectItem selectItem =
        select.getSelectItems().get(0);
Assertions.assertEquals(
        new LongValue(1)
        , selectItem.getExpression());

Table table = (Table) select.getFromItem();
Assertions.assertEquals("dual", table.getName());

EqualsTo equalsTo = (EqualsTo) select.getWhere();
Column a = (Column) equalsTo.getLeftExpression();
Column b = (Column) equalsTo.getRightExpression();
Assertions.assertEquals("a", a.getColumnName());
Assertions.assertEquals("b", b.getColumnName());
```

15、[odc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/oceanbase/odc)：Enterprise-Level Database Collaborative Development Platform. This project is a platform designed for collaborative database development and data management, specifically to enhance the efficiency of SQL development. It is built on Spring Boot and Electron, providing both web and desktop clients, with features such as SQL specification checking, change rollback, data lifecycle management, data desensitization, and operational auditing, compatible with various data sources including OceanBase, Oracle, MySQL, and Doris.Shared by [@XiaoYangGzeyP](https://hellogithub.com/en/user/QfYG9d5Kt2nqWPJ)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/675901913.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
16、[papermark](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mfts/papermark)：Open-Source File Sharing Platform. This project serves as an open-source alternative to the DocSend service, providing self-hosted and easy-to-use document sharing capabilities. It is built with Next.js and Tailwind CSS, allowing users to upload documents and receive an online accessible address for file content. It supports custom domain names and features like access tracking.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/646985602.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[plane](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/makeplane/plane)：Open Source Project Management and Issue Tracking Platform. This project is an open-source system for managing projects, designed to streamline the project management process for teams. It is user-friendly and self-hostable, supporting issue tracking, cycle management, project breakdown, and analytical statistics, and can be used as an alternative to JIRA.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/568098118.png' style="max-width:80%; max-height=80%;"></img></p>

18、[swr](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vercel/swr)：React Hooks Library for Data Fetching. This project is a React library designed to simplify the data fetching logic for developers. It supports automatic handling of data caching, revalidation, error retry, and more. For instance, it automatically requests the latest data when a user re-clicks or returns to a page.
```javascript
import useSWR from 'swr'
 
function Profile() {
  const { data, error, isLoading } = useSWR('/api/user', fetcher)
 
  if (error) return <div>failed to load</div>
  if (isLoading) return <div>loading...</div>
  return <div>hello {data.name}!</div>
}
```

19、[undraw-ui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/readpage/undraw-ui)：Vue 3-based Comment Component. This is a UI component based on Vue 3, providing functionalities such as commenting, content collapsing, replying to comments, and using emoticons, as well as components for catalog and search.Shared by [@Mr.King](https://hellogithub.com/en/user/fUDKIpV5ohlc3qb)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/479253212.png' style="max-width:80%; max-height=80%;"></img></p>

20、[uppy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/transloadit/uppy)：Easy-to-Integrate JavaScript File Upload Component. This is a lightweight JavaScript file upload component that provides a visually appealing user interface, supports the import of files from multiple sources, resumable file uploads, internationalization, as well as functionalities for previewing, editing, and multi-file uploading.
```javascript
import React, { useEffect } from 'react'
import Uppy from '@uppy/core'
import Webcam from '@uppy/webcam'
import { Dashboard } from '@uppy/react'

const uppy = new Uppy().use(Webcam)

function Component () {
  return <Dashboard uppy={uppy} plugins={['Webcam']} />
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/46273445.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
21、[Lemuroid](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Swordfish90/Lemuroid)：All-in-One Game Emulator on Android Devices. This multi-emulator, based on Libretro, enables you to play various retro games on Android devices. It offers features such as instant save states, local multiplayer, customizable buttons, and supports emulation of various gaming consoles including NES, GBA, 3DS, and PSP.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/226883777.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python
22、[buku](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jarun/buku)：Browser Bookmark Management Tool with Built-in API Service. This is an open-source bookmark command-line management tool, which is lightweight, privacy-safe, and easy to use, supporting the import of bookmarks from mainstream browsers, automatic acquisition of bookmark information, cross-platform synchronization, and a powerful search function.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/45355064.png' style="max-width:80%; max-height=80%;"></img></p>

23、[flagsmith](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Flagsmith/flagsmith)：A Platform for Easy Management of Feature Switches and Configurations. This is an open-source, feature-rich feature flag and remote configuration platform designed for small and medium-sized teams. It is a web application built on Django REST framework for managing the enablement and remote configuration of application features, supporting A/B testing, multivariate testing, and organizational management. It is suitable for scenarios such as gradually rolling out new features, conducting market tests, and managing various environments.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/136163130.png' style="max-width:80%; max-height=80%;"></img></p>

24、[marimo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/marimo-team/marimo)：Innovative Responsive Python Notebook. This project is a responsive notebook tailored specifically for Python, designed to automatically execute and update the dependent code cells upon interaction with the user interface, ensuring the consistency of code and output. It is stored as a pure Python file, facilitating management and execution, and supports being run as a script or deployed as an interactive web application.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/678526156.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[umap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lmcinnes/umap)：Python library for high-dimensional data dimensionality reduction. This project is a Python library used to map high-dimensional data to low-dimensional spaces, aiding researchers in understanding complex datasets. Compared with t-SNE, it excels in preserving the global structure of the data, capable of efficiently performing high-dimensional to low-dimensional mapping, suitable for a variety of scenarios such as data visualization, feature extraction, and cluster analysis.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)
```python
import umap
from sklearn.datasets import load_digits

digits = load_digits()

mapper = umap.UMAP().fit(digits.data)
umap.plot(mapper, labels=digits.target)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/95995403.png' style="max-width:80%; max-height=80%;"></img></p>

26、[Windrecorder](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yuka-friends/Windrecorder)：Your Personal Screen Memory Search Tool. This project is a screen recording tool designed specifically for Windows, offering search and replay functionalities. It records the screen content continuously while ensuring data security (no uploads, no internet connection), utilizing OCR and image recognition technologies, allowing users to easily search for and review the history of screen activities.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/672537073.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Rust
27、[bacon](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Canop/bacon)：Background Rust Code Linter Tool. This is a code linting tool specially designed for the Rust language. It operates in the background and provides developers with real-time feedback on warnings, errors, and test failures in their Rust code, allowing developers to focus on writing code instead of frequently running check commands manually.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/308327979.png' style="max-width:80%; max-height=80%;"></img></p>

28、[bandwhich](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/imsnif/bandwhich)：Command-line Tool for Viewing Bandwidth Usage. This is an open-source command-line network bandwidth monitoring tool that can display the status of network usage in real-time, including information such as processes, connections, and remote addresses.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/206874323.png' style="max-width:80%; max-height=80%;"></img></p>

29、[rust-by-practice](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sunface/rust-by-practice)：Practical Rust Language Exercises. This project provides a multitude of practical Rust exercises to help newcomers learn and get started with the Rust language. In addition to a vast collection of exercise problems and solutions, it also supports online editing and execution of Rust code.

### Swift
30、[MacSymbolicator](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/inket/MacSymbolicator)：Tool for Symbolizing macOS/iOS Crash Reports. This is a simple Mac application that can convert hexadecimal addresses from macOS/iOS crash reports to functions and line numbers in the source code, assisting developers in analyzing the cause of application crashes and supporting crash and ips format crash reports.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/31854735.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
31、[facefusion](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/facefusion/facefusion)：Open-Source AI Face Swapping and Enhancement Tool. A robust tool for face swapping and enhancement, capable of replacing faces in images or videos with another person's face, improving the clarity of faces and backgrounds, and also providing a user-friendly web interface (WebUI) as well as low-barrier CPU processing options.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/679869950.png' style="max-width:80%; max-height=80%;"></img></p>

32、[litellm](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/BerriAI/litellm)：Tool for Simplified API Calls of Large Models. This project enables the unification of various AI large model and service interfaces into the OpenAI format, thereby simplifying the management and switching tasks between different AI services or large models. Additionally, it supports functions such as setting budgets, restricting request frequencies, managing API Keys, and configuring OpenAI proxy servers.
```python
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["COHERE_API_KEY"] = "your-cohere-key"

messages = [{ "content": "Hello, how are you?","role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion(model="command-nightly", messages=messages)
print(response)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/671269505.gif' style="max-width:80%; max-height=80%;"></img></p>

33、[llama3-from-scratch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/naklecha/llama3-from-scratch)：Tutorial on Implementing Llama 3 from Scratch. This project helps people deeply understand how Large Language Models (LLMs) work by building Llama 3 layer by layer. The author uses the PyTorch framework to implement loading model weights, text tokenization, model configuration, and step-by-step implementation of key components in the Transformer model.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/802916901.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
34、[cloudflare_temp_email](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dreamhunter2333/cloudflare_temp_email)：Free Temporary Email Service Setup. This project utilizes CloudFlare's free services to provide a fully functional temporary email service, supporting features such as receiving and sending emails, access passwords, automatic replies, and viewing attachments.Shared by [@Dream Hunter](https://hellogithub.com/en/user/FxNypXK7UQ9OECT)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/678900558.png' style="max-width:80%; max-height=80%;"></img></p>

35、[docs-linux-kernel-labs-zh-cn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/linux-kernel-labs-zh/docs-linux-kernel-labs-zh-cn)：Linux Kernel Experiments. This project is the Chinese translation of the 'Linux Kernel Teaching' course from the University of Bucharest, suitable for programmers interested in Linux kernels. The course content is divided into two parts: lectures and experiments. The experiments are conducted in a virtual machine based on QEMU, allowing participants to experience the development, compilation, deployment, and execution process of the Linux kernel firsthand.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/720977650.png' style="max-width:80%; max-height=80%;"></img></p>

36、[LapisCV](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/BingyanStudio/LapisCV)：Out-of-the-box Resume Templates. This project provides resume templates for Obsidian and Typora, which are based on the Markdown format, easy to edit, and offer a WYSIWYG (What You See Is What You Get) experience. The design is minimalist yet formal, and with the help of the editors, you can directly export resumes in PDF format.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/767730706.png' style="max-width:80%; max-height=80%;"></img></p>

37、[OV-Watch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/No-Chicken/OV-Watch)：Low-Cost Open Source Smartwatch. This is a smartwatch project with a manufacturing cost of only 80 yuan. It not only provides basic watch functions but also supports sleep mode, Bluetooth, step counting, card holder, compass, and heart rate monitoring, among other features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/637258361.jpg' style="max-width:80%; max-height=80%;"></img></p>

38、[phonedata](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xluohome/phonedata)：Mobile Number Geographic Information Library. This project compiles over 400,000+ Chinese mobile number segments and geographic information, all sourced from public data available online.

### Book
39、[LLMBook-zh.github.io](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LLMBook-zh/LLMBook-zh.github.io)：The Large Language Models. This is an open-source book prepared for programmers and students who want to get started with large model technology. The content covers not only the basic principles and key technologies of large models but also provides a code tool library and large models to help readers quickly get started and practice.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/786642156.jpg' style="max-width:80%; max-height=80%;"></img></p>

40、[raytracing.github.io](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/RayTracing/raytracing.github.io)：The 'Ray Tracing in One Weekend' Book Series. This is a set of introductory books on ray tracing technology, teaching you to implement a ray tracer in C++. Ray tracing is a rendering technique in computer graphics that produces photorealistic images by simulating the behavior of light within a virtual scene.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/98/197663980.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub97.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub99.md">『Next』</a>
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
