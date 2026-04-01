# HelloGitHub Vol.111
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
1、[mimikatz](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gentilkiwi/mimikatz)：Tools for Exploring Windows Security Mechanisms.This is a tool written in C language for researching Windows security mechanisms. It can extract sensitive information such as plaintext passwords, hash values, PIN codes, Kerberos tickets, etc. from memory, and supports advanced operations such as pass-the-hash, Golden Ticket, DCSync, etc. It is widely used in security research, penetration testing and system security analysis scenarios.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/18496166.png' style="max-width:80%; max-height=80%;"></img></p>

### C#
2、[AutoUpdater.NET](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ravibpatel/AutoUpdater.NET)：WPF Desktop Application Auto-upgrade Component.This is an auto-update library specifically designed for WinForms and WPF desktop applications. With just a few lines of code, you can easily integrate functions such as automatically detecting new versions, prompting pop-ups, and downloading and installing packages into desktop applications.

3、[ExplorerTabUtility](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/w4po/ExplorerTabUtility)：Windows File Management Multi-tab Extension Tool.This is a file explorer enhancement tool specifically designed for Windows 11. It can automatically merge multiple windows into a single-window multi-tab mode. It supports path deduplication, tab search, batch opening/closing/restoring, etc., easily bidding farewell to the trouble of messy desktop windows.Shared by [@iKineticate](https://hellogithub.com/en/user/JCrYzT28cH9twxQ)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/722973124.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++
4、[defendnot](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/es3n1n/defendnot)：One-click Tool to Shut Down Windows Defender.This is a tool for disabling Windows Defender. It supports one-click installation and persistent effectiveness. It realizes the complete disabling of the system's built-in Defender real-time protection service by directly calling the Windows Security Center (WSC) interface and registering a virtual antivirus software. At the same time, it supports booting self-start to ensure that the disabled state still takes effect after restart.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/979241345.png' style="max-width:80%; max-height=80%;"></img></p>

5、[OpenSpeedy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/game1024/OpenSpeedy)：Ready-to-use Game Shifter.This is a completely free and open-source Windows game acceleration tool. It achieves flexible adjustment of game speed by hooking the system time function and provides a simple and easy-to-use interface, compatible with multiple single-player games. Do not use it in online games to avoid account suspension!Shared by [@game1024](https://hellogithub.com/en/user/kmUCncHJr9SpNV7)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/984862298.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[USearch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/unum-cloud/USearch)：Faster and Compact Vector Retrieval and Clustering Engine.This is a high-performance and lightweight similarity search and clustering engine with a single header file design. It can be embedded in mainstream databases and supports vector and multimodal data (text, images, geographic coordinates). It implements efficient approximate nearest neighbor search based on the HNSW algorithm and is compatible with multiple programming languages and precision types. It is suitable for scenarios such as recommendation systems, vector databases, intelligent retrieval, and geospatial analysis.
```c++
#include <usearch/index.hpp>
#include <usearch/index_dense.hpp>

using namespace unum::usearch;

int main(int argc, char **argv) {
    metric_punned_t metric(3, metric_kind_t::l2sq_k, scalar_kind_t::f32_k);

    // If you plan to store more than 4 Billion entries - use `index_dense_big_t`.
    // Or directly instantiate the template variant you need - `index_dense_gt<vector_key_t, internal_id_t>`.
    index_dense_t index = index_dense_t::make(metric);
    float vec[3] = {0.1, 0.3, 0.2};

    index.reserve(10); // Pre-allocate memory for 10 vectors
    index.add(42, &vec[0]); // Pass a key and a vector
    auto results = index.search(&vec[0], 5); // Pass a query and limit number of results

    for (std::size_t i = 0; i != results.size(); ++i)
        // You can access the following properties of every match:
        // results[i].element.key, results[i].element.vector, results[i].distance;
        std::printf("Found matching key: %zu", results[i].member.key);
    return 0;
}
```

### Go
7、[f2](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ayoisaiah/f2)：Cross-platform Batch Rename Tool.This is a command-line batch renaming tool written entirely in Go language, supporting regular expressions, automatically resolving conflicts, undoing, and other functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/259488212.png' style="max-width:80%; max-height=80%;"></img></p>

8、[logdy-core](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/logdyhq/logdy-core)：Real-time Log Viewing Tool with Built-in Web Interface.This is a lightweight real-time log viewing tool that requires no installation and is ready to use out of the box. It has a built-in Web interface, allowing you to view and filter logs in real-time like tail -f through a browser. It supports multiple input modes and custom parsers.Shared by [@刘睿华](https://hellogithub.com/en/user/TJ65FfbQU09PLHM)
```
# Use with any shell command
$ tail -f file.log | logdy
WebUI started, visit http://localhost:8080

# Read log files
$ logdy follow app-out.log --full-read
WebUI started, visit http://localhost:8080
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/747929369.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[OpenList](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/OpenListTeam/OpenList)：File List Program Supporting Multiple Storages.This is a file list program based on Gin and SolidJS, supporting multiple storage methods such as local storage, Aliyun Disk, OneDrive, and Google Drive. It is completely open source (forked from AList) and maintained by the community.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/1000524955.png' style="max-width:80%; max-height=80%;"></img></p>

10、[tldx](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/brandonyoungdev/tldx)：Tool for Finding Available Domains with One Click.This is a command-line tool for quickly querying available domains. It can intelligently generate domain combinations based on keywords, prefixes, suffixes and various top-level domains, and quickly detect their availability.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/791194177.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java
11、[booklore](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/booklore-app/booklore)：Personal Digital Library for Java Development.This is an open-source, self-hosted e-book management web application that supports PDF and ePub e-book formats. It is developed with Java (Spring Boot) + Angular and supports functions such as automatic acquisition of book information, sharing of books, synchronization of reading progress, and multi-user management.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/903039267.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[forge](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Card-Forge/forge)：Open Source Strategy Card Game.This is an open source rule engine and simulator designed for Magic: The Gathering players. It is a card game similar to Hearthstone with single-player adventures, tasks, multiple AI battle modes. It supports online battles, custom card and expansion features and is compatible with Windows, macOS, Linux and Android platforms.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/479890272.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
13、[eslint-plugin-unicorn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sindresorhus/eslint-plugin-unicorn)：ESLint Plugin to Improve JavaScript Code Quality.This is an ESLint plugin integrated with more than 100 high-quality JavaScript code inspection rules, comprehensively covering multiple aspects such as code style, performance, security and readability.

14、[heynote](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/heyman/heynote)：Notepad Designed Specifically for Programmers.This is a sticky note application specifically for developers, whose strength lies in the ability to easily store different content in chunks, be it snippets of code or Markdown text! It supports automatic syntax highlighting, automatic formatting, calculator mode, multi-cursor editing, global hotkeys and other features, suitable for Windows, macOS, and Linux.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/582974355.png' style="max-width:80%; max-height=80%;"></img></p>

15、[remotion](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/remotion-dev/remotion)：Making Dynamic Videos with React.This is a platform that can generate videos through code. Developers can dynamically generate video content using web technologies (such as CSS, Canvas, SVG, WebGL), React components, variables and functions, supporting complex animations and effects.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/274495425.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[TypeWords](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zyronon/TypeWords)：Minimalist Typing Word Memorization Website.This is a web-based word memorization software that helps users remember words through keyboard input. It has a simple interface, smooth interaction, and supports functions such as word pronunciation, error statistics, and a new word list.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/674186516.png' style="max-width:80%; max-height=80%;"></img></p>

17、[workout-cool](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Snouzy/workout-cool)：Open Source Fitness Guidance Platform.This is a free and open-source fitness guidance platform that provides rich fitness actions and video demonstrations. It is built with Next.js + TailwindCSS and supports creating fitness plans, progress tracking and multi-language functionality.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/1000235209.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
18、[flashdim](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cyb3rko/flashdim)：Professional Android Torch Application.This is a free, ad-free, and offline usable torch application that is compatible with Android 13 and above systems. It realizes multi-level brightness adjustment through hardware interfaces and supports modes such as SOS, Morse code signals, BMP, and timed blinking. It is very suitable for use in hiking, camping, night running and other scenarios.Shared by [@ewiro](https://hellogithub.com/en/user/iItGgWoJjnLsr0Y)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/555295333.png' style="max-width:80%; max-height=80%;"></img></p>

19、[Trail-Sense](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kylecorry31/Trail-Sense)：Essential Android Apps for Wilderness Survival.This is an open-source Android app specifically designed for hiking, camping, and wilderness survival scenarios. It utilizes the phone's sensors to provide practical functions such as offline navigation, sunset reminders, photo mapping, and path tracking. All functions can be used in a no-network environment.Shared by [@ewiro](https://hellogithub.com/en/user/iItGgWoJjnLsr0Y)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/215154276.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C
20、[mac-mouse-fix](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/noah-nuebling/mac-mouse-fix)：macOS Mouse Enhancement Tool.This is a mouse enhancement tool specifically designed for macOS, which makes up for the lack of support for non-Apple mice in the system. Users can customize various behaviors of third-party mice on Mac, including smooth scrolling, direction reversal, mouse gestures and button mapping functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/201134801.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python
21、[borg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/borgbackup/borg)：Efficient Data Duplication and Backup Tool.This is a highly efficient and secure duplication and backup tool that can accurately identify duplicate data even if the file structure or location changes. It uses content-defined chunking deduplication algorithm to significantly save storage space. It has multiple compression options such as lz4, zstd, zlib, and lzma built-in, and supports SSH remote backup.

22、[bunkerweb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bunkerity/bunkerweb)：Open Source Web Application Firewall.This project is an open source Web Application Firewall developed in Python, which can be seamlessly integrated into existing environments (Linux, Docker, K8s, etc.). It is built on Nginx, with a secure default configuration, a simple and user-friendly web interface, supports automatic HTTPS A+ rating configuration, security headers, and a rich plugin system. It can detect common attack patterns, restrict access, prevent malicious visits from bots and crawlers, protecting your website, API, and web applications.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/203456148.png' style="max-width:80%; max-height=80%;"></img></p>

23、[ebook2audiobook](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/DrewThomasson/ebook2audiobook)：Tool for Converting E-books to Audiobooks.This open-source tool can effortlessly convert e-books into audiobooks, supporting various common formats such as EPUB, MOBI, PDF, and more. It extracts e-book text through calibre and utilizes Text-to-Speech technology to generate audiobooks that include chapters and metadata, supporting over 1000 languages, including Chinese.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/746935181.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[isd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kainctl/isd)：Terminal Interactive systemd Management Tool.This is a systemd management tool with a terminal user interface (TUI) that supports fuzzy searching, automatic preview, smart sudo, shortcut keys, etc., simplifying the management experience of systemd units such as services and timers.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/917864037.png' style="max-width:80%; max-height=80%;"></img></p>

25、[romm](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rommapp/romm)：Must-have ROM Manager for Emulator Game Players.This is a ROM management and emulator platform developed based on Python, supporting the direct running of games in the browser. Users can easily scan local games, automatically grab game covers, and uniformly manage multi-platform ROM resources through a concise web interface, compatible with more than 400 game platforms.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/611338935.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust
26、[microbin](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/szabodanika/microbin)：Minimal File Sharing and Short Link Platform.This is a lightweight web application written in Rust that integrates file sharing, online clipboard, and URL shortening. It is secure, reliable, and easy to deploy, supporting features such as automatic expiration, setting passwords, and protection levels.Shared by [@xici](https://hellogithub.com/en/user/OzQPpgo5Hw1W9lk)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/480154226.png' style="max-width:80%; max-height=80%;"></img></p>

27、[mise](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jdx/mise)：One-stop Multilingual Development Environment Management Tool.This is a development environment management tool written in Rust. It integrates multi-language toolchain switching, environment variable management and task automation. It easily solves problems such as multi-version programming languages, environment isolation and automated construction. It can replace multiple tools such as asdf, nvm, pyenv, direnv and make.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/586920414.gif' style="max-width:80%; max-height=80%;"></img></p>

28、[somo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/theopfr/somo)：More User-Friendly Port Viewing Tool.This is a humanized and user-friendly command-line tool designed specifically for Linux. It is used to monitor sockets and local ports. It displays port and process network connection information in a beautiful and compact table in real time. It supports filtering, sorting, and formatted output and can be used as a replacement for netstat.Shared by [@kero990](https://hellogithub.com/en/user/c3Y4NR1rq6neVoD)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/641143821.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
29、[container](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/apple/container)：Apple Open-Sourced Lightweight Virtual Machine.This is an officially open-sourced lightweight virtualization container tool by Apple, used to create and run Linux containers on Mac. It is developed in Swift and optimized for Apple chips (such as M1, M2 chips). It aims to provide efficient and native container experiences for macOS users, supports OCI standard container images, and can be seamlessly connected to mainstream mirror repositories such as Docker Hub.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/993475914.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[FlashSpace](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wojciech-kulik/FlashSpace)：Instant Workspace Switching on macOS.This is a virtual workspace manager designed specifically for macOS, enabling ultra-fast and seamless switching between multiple tasks without animations. It provides an immediate workspace switching experience by eliminating the waiting animations when switching applications on macOS. It supports multiple monitors, picture-in-picture, focus/cursor management, and other functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/919165314.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
31、[claude-code](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/anthropics/claude-code)：Claude Coding Assistant in Terminal.This project is an AI coding assistant open-sourced by Claude officially. Integrated into the terminal, it can understand the entire codebase and help developers complete various coding tasks more efficiently through simple natural language commands.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/937253475.gif' style="max-width:80%; max-height=80%;"></img></p>

32、[gemini-cli](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google-gemini/gemini-cli)：Google Gemini Command Line Tool.This project is the official open-source command line tool of Gemini, integrating the powerful capabilities of Google Gemini into the terminal environment. It is based on a million-level context and can understand the architecture and logic of large codebases. It supports multimodal input and output, Google search, and MCP and other functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/968197216.png' style="max-width:80%; max-height=80%;"></img></p>

33、[happy-llm](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/datawhalechina/happy-llm)：LLM Principles and Practice Tutorial from Scratch.This project is a tutorial to help beginners systematically learn the principles and practices of large language models (LLMs). Through detailed tutorials and practical cases, it gradually leads readers to deeply understand the basics of natural language processing (NLP), the Transformer architecture, and the basic principles of pre-trained language models, and enables them to implement and train their own large language models hands-on.Shared by [@大痴小乙](https://hellogithub.com/en/user/aDd1NUpVvKHAJmE)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/806854629.jpg' style="max-width:80%; max-height=80%;"></img></p>

34、[nano-vllm](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GeeeekExplorer/nano-vllm)：Lightweight vLLM Built from Scratch.This project is a lightweight vLLM (large language model inference engine) implemented in Python. The core code is only over 1000 lines. It has a clear structure and is easy to read. The inference speed is comparable to the original vLLM and integrates inference optimization techniques such as prefix caching, tensor parallelism, and Torch compilation.
```python
from nanovllm import LLM, SamplingParams
llm = LLM("/YOUR/MODEL/PATH", enforce_eager=True, tensor_parallel_size=1)
sampling_params = SamplingParams(temperature=0.6, max_tokens=256)
prompts = ["Hello, Nano-vLLM."]
outputs = llm.generate(prompts, sampling_params)
outputs[0]["text"]
```

35、[prompt-optimizer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/linshenkx/prompt-optimizer)：Tool for Optimizing AI Prompts.This is a pure front-end implemented prompt optimizer that helps users quickly write higher-quality prompts. It supports multiple mainstream AI models and custom API addresses, and can compare the effects before and after optimization in real time.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/931352845.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
36、[daily-arXiv-ai-enhanced](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dw-dengwei/daily-arXiv-ai-enhanced)：Tool for Automatically Generating arXiv Paper Summaries Daily.This project can automatically obtain papers on arxiv and use large language models to summarize them, generating Chinese summaries.Shared by [@WeiTFw0B](https://hellogithub.com/en/user/lbNO5oE0sy1KGYW)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/951746200.png' style="max-width:80%; max-height=80%;"></img></p>

37、[ESP32-BlueJammer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/EmenstaNougat/ESP32-BlueJammer)：DIY Wireless Signal Jammer.This is a 2.4GHz communication jammer based on ESP32 and nRF24 module. The code is open source and can be DIY or developed further. It interferes with the communication of Bluetooth, BLE, WiFi and RC devices by generating noise and sending invalid data packets, making them unable to work properly.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/825347997.jpg' style="max-width:80%; max-height=80%;"></img></p>

38、[hoverzoom](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/extesy/hoverzoom)：Browser Plugin for Zooming Images on Hover.This is a browser plugin that automatically zooms videos and images on a webpage when the mouse hovers over them. It supports Chrome, Firefox, and Edge browsers.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/16063480.png' style="max-width:80%; max-height=80%;"></img></p>

39、[kubernetes-the-hard-way](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kelseyhightower/kubernetes-the-hard-way)：Tutorial on Building Kubernetes Cluster the Hard Way.This project aims to help beginners deeply understand the core components and working principles of K8s by manually building a Kubernetes cluster from scratch. It provides a detailed guide on installing, configuring and running a highly available K8s cluster completely manually without using automated tools.

40、[LeetCUDA](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xlite-dev/LeetCUDA)：CUDA Tutorial for Beginners in High-performance Computing.This is a CUDA tutorial and question bank prepared specifically for beginners in high-performance computing (HPC), including 200 CUDA-implemented operators, study notes, and hands-on practice of self-written performance benchmarking against official HGEMM and FlashAttention-2. It is suitable for interview preparation related to model inference optimization and operator optimization.Shared by [@DefTruth](https://hellogithub.com/en/user/ofSCbzTmdeQk3FD)

41、[obs-backgroundremoval](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/royshil/obs-backgroundremoval)：OBS Background Removal Plugin.This is an open-source OBS Studio plugin that can automatically recognize human figures and remove backgrounds during recording or live streaming, enabling users to easily change video backgrounds and supports platforms such as Windows, macOS and Ubuntu.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/111/358081783.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub110.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub112.md">『Next』</a>
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
