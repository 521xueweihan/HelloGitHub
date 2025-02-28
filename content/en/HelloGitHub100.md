# HelloGitHub Vol.100
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
1、[darktable](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/darktable-org/darktable)：Open-Source Photography Post-Processing Tool. This is a free and professional post-processing software for photographic works. It acts as a virtual light table and darkroom, helping photographers store digital negatives, magnify and search through photos. The software can display information such as the focal length and exposure of the photos and supports features like edit history, map mode, and photo printing.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/3791835.jpg' style="max-width:80%; max-height=80%;"></img></p>

2、[gnucash](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Gnucash/gnucash)：Fully Open Source Accounting Software. This is an open-source financial software suitable for individuals and small businesses. It uses double-entry accounting, offers a simple operation interface, and supports features such as generating reports, reconciliation, multi-currency, and real-time stock price retrieval. It is available on Windows, Linux, and macOS platforms.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/7966650.png' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[git-credential-manager](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/git-ecosystem/git-credential-manager)：Universal Git Credential Manager. This is a Git credential storage and management tool developed based on .NET. It's out-of-the-box, requiring no additional operations. When using Git commands, the tool will automatically guide you through the login process, eliminating the need for re-login and easily solving issues such as the need for login and failed authentication when performing operations on remote Git repositories. It supports platforms like GitHub, Bitbucket, and GitLab.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/158405551.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Lean](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/QuantConnect/Lean)：C#-Based Quantitative Trading Engine. This is an open-source, battle-hardened quantitative trading engine written in C#. It supports algorithmic trading written in either Python3 or C#, compatible with Windows, Linux, and macOS platforms, suitable for the research of quantitative trading strategies, backtesting, and live trading scenarios.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/27251463.png' style="max-width:80%; max-height=80%;"></img></p>

5、[space-station-14](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/space-wizards/space-station-14)：Open Source Game 'Space Station 14'. This project is an open-source remake of the classic game 'Space Station 13'. In this turn-based multiplayer role-playing game, players can choose various roles such as engineers, captains, and traitors, and cooperate or compete with other players to survive in a limited resource environment.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/92001425.jpg' style="max-width:80%; max-height=80%;"></img></p>

6、[subtitleedit](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SubtitleEdit/subtitleedit)：Open Source Video Subtitle Editing Tool. This is a free video subtitle editor for Windows. It is powerful out of the box and supports creating, adjusting, syncing, and transcribing subtitles, also offering features like automatic translation, subtitle format conversion, and speech recognition.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/16473585.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
7、[diff-pdf](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vslavik/diff-pdf)：Tool for Intuitive Comparison of Two PDF Files. This is a PDF file comparison tool written in C++. It supports two viewing modes, allowing the differences in file content to be output to a new PDF file or viewed directly in the GUI.
```
// 输出差异
diff-pdf --output-diff=diff.pdf a.pdf b.pdf
// 直接查看
diff-pdf --view a.pdf b.pdf
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/353360.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
8、[buildg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ktock/buildg)：Interactive Dockerfile Debugging Tool. This tool is an interactive Dockerfile debugging utility based on BuildKit, supporting features such as setting breakpoints, step-by-step execution, and non-root mode, and it can be used within editors like VSCode.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/490156339.png' style="max-width:80%; max-height=80%;"></img></p>

9、[devzat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/quackduck/devzat)：SSH Chatroom Exclusive for Programmers. This is a chatroom connected via SSH, where users don't need to install any client; they can log in with just an SSH command. It supports private messages, multiple chat rooms, image sharing, and code highlighting, and also provides the capability to integrate third-party services and self-host an SSH chatroom.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/354515412.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[expr](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/expr-lang/expr)：Expression Library for Go Language. This project is specifically designed as an expression language and evaluator for the Go language, supporting a rich set of operators and advanced functions, characterized by safety, side-effect-free, and static type checking. An expression is a single line of code composed of variables, operators, and functions, which can simplify complex computational tasks and is often used in scenarios such as dynamic configuration and business rule engines.Shared by [@两双筷子sqldc](https://hellogithub.com/en/user/5dGtvaZ6H3L4QMY)
```go
func main() {
    // 表达式
	code := `all(Tweets, {.Len <= 240})`

	program, err := expr.Compile(code, expr.Env(Env{}))
	if err != nil {
		panic(err)
	}

	env := Env{
		Tweets: []Tweet{{42}, {98}, {69}},
	}
    // 计算表达式
	output, err := expr.Run(program, env)
	if err != nil {
		panic(err)
	}

	fmt.Println(output)
}
```

11、[gdu](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dundee/gdu)：Command-line Tool for Quickly Viewing Disk Usage. This is a disk usage analyzer written in Go language, which can quickly scan and display the disk space occupied by files and directories, supporting TUI (default), interactive, and export modes.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/122750502.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[cryptomator](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cryptomator/cryptomator)：A Tool to 'Lock' Your Cloud Files. This is an open-source cloud storage file encryption tool that supports mainstream cloud storage services such as Dropbox and OneDrive. It is simple and user-friendly, cross-platform, and does not require registration. It uses AES-256 encryption to upload files and directories to the cloud storage, suitable for scenarios where data backup to the cloud is necessary but there are concerns about data leakage.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/16446099.png' style="max-width:80%; max-height=80%;"></img></p>

13、[JarEditor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Liubsyy/JarEditor)：IDEA Plugin for Directly Editing JAR Files. This is an IntelliJ IDEA plugin that allows you to directly edit the class and resource files within JAR files without the need to unzip them. It supports adding, deleting, and renaming files and directories within the JAR package, and provides features such as searching and copying the contents of JAR packages. It is compatible with SpringBoot and Kotlin projects.Shared by [@鹰影](https://hellogithub.com/en/user/iEnYZr4sASMjWJb)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/799158803.png' style="max-width:80%; max-height=80%;"></img></p>

14、[PojavLauncher](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PojavLauncherTeam/PojavLauncher)：Minecraft Game Launcher for Android. This project allows you to play Minecraft (World of Mine) on Android, offering both offline and multiplayer modes. It supports almost all versions of Minecraft and can install mods and loaders such as Forge, Fabric, and OptiFine.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/246464565.jpg' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
15、[grapesjs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GrapesJS/grapesjs)：Free Visual Web Page Construction Platform. This project offers an intuitive visual interface, enabling users to design and construct web HTML templates quickly through a drag-and-drop method. It features what-you-see-is-what-you-get (WYSIWYG) capabilities and mobile adaptation, suitable for official websites, news, and CMS types of websites.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/50146229.jpg' style="max-width:80%; max-height=80%;"></img></p>

16、[react-content-loader](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/danilowoz/react-content-loader)：React Component for Easily Creating Skeleton Screens. This project is a React component designed for creating placeholder graphics when pages are loading. It is compact, customizable, and provides a variety of pre-set styles and example code, which is extremely easy to use, and supports mainstream frameworks such as React, Vue, and Angular.
```typescript
import { Code } from 'react-content-loader'

const MyCodeLoader = () => <Code />
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/79509385.gif' style="max-width:80%; max-height=80%;"></img></p>

17、[Sink](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ccbikai/Sink)：Cloudflare-based Short Link Platform with Access Statistics. This project is a short link service operating on Cloudflare, supporting features such as URL shortening, access analysis, and link expiration dates.Shared by [@面条](https://hellogithub.com/en/user/qi74Zp23wYKeAVB)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/796284842.png' style="max-width:80%; max-height=80%;"></img></p>

18、[typebot.io](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/baptisteArno/typebot.io)：Self-Hosted Chatbot Builder. This project enables users to easily create advanced chatbots through a visual drag-and-drop interface and embed them into websites. It offers over 30 chat building blocks, along with features like self-hosting, analytics tools, custom domain names, and branding customization, suitable for scenarios such as online customer service and sales support.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/429736266.png' style="max-width:80%; max-height=80%;"></img></p>

19、[typed.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mattboldt/typed.js)：User-Friendly JavaScript Typing Animation Library. This project is a JavaScript library specifically designed to create typing animation effects. It is easy to use and SEO-friendly, supporting features such as deletion effects, setting the typing speed, and the number of loops.
```javascript
var typed = new Typed('.element', {
  strings: ["First sentence.", "Second sentence."],
  typeSpeed: 30
});
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/10290605.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
20、[WiFiAnalyzer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/VREMSoftwareDevelopment/WiFiAnalyzer)：Android App for Analyzing WiFi Signals. This project is a WiFi analysis tool written in Kotlin, offering intuitive graphical representation of WiFi network conditions, supporting the identification of surrounding WiFi, measuring signal strength, and viewing channel congestion, among other features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/47726042.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
21、[buzz](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chidiwilliams/buzz)：Audio Transcription and Translation Tool. This project is a Whisper-based audio transcription and translation tool that is ready to use and easy to operate, supporting speech to text, audio translation, multiple languages, and offline use, suitable for macOS, Windows, and Linux platforms.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/540842713.jpg' style="max-width:80%; max-height=80%;"></img></p>

22、[helium](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mherrmann/helium)：A Python Library for Simplifying Browser Automation. This project is a lightweight Python library based on Selenium, which makes writing browser automation scripts in Python easier and more convenient by providing a higher-level and more user-friendly API, supporting Chrome and Firefox browsers.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/224234024.gif' style="max-width:80%; max-height=80%;"></img></p>

23、[jurigged](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/breuleux/jurigged)：Python Hot Reloading Tool. This is a library specifically designed to provide hot reloading functionality for Python, allowing modifications and updates to Python code during runtime without the need to restart the program.
```
# Loop over a function
jurigged --loop function_name script.py
jurigged --loop module_name:function_name script.py

# Only stop on exceptions
jurigged --xloop function_name script.py
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/334540343.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[python-sortedcontainers](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/grantjenks/python-sortedcontainers)：Enhanced Python Sorting Collection Library. This project offers three data structures: SortedList, SortedDict, and SortedSet, which are fully compatible with the APIs of the built-in List, Dict, and Set data types in Python. Despite being written purely in Python, their performance rivals that of Python libraries implemented with C extensions.
```python
from sortedcontainers import SortedList
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
# sl: SortedList(['a', 'b', 'c', 'd', 'e'])
sl *= 10_000_000
sl.count('c')  # 10000000
sl[-3:]  # ['e', 'e', 'e']

from sortedcontainers import SortedDict
sd = SortedDict({'c': -3, 'a': 1, 'b': 2})
# sd: SortedDict({'a': 1, 'b': 2, 'c': -3})
sd.popitem(index=-1)  # ('c', -3)

from sortedcontainers import SortedSet
ss = SortedSet('abracadabra')
# ss: SortedSet(['a', 'b', 'c', 'd', 'r'])
ss.bisect_left('c')  # 2
```

25、[radon](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/rubik/radon)：Python Code Quality Analysis Tool. This is a powerful Python code measurement tool that can calculate a variety of code metrics, including McCabe complexity, Halstead metrics, and maintainability index, suitable for Python code quality assessment and continuous integration scenarios.
```
$ radon cc sympy/solvers/solvers.py -a -nc
sympy/solvers/solvers.py
    F 346:0 solve - F
    F 1093:0 _solve - F
    F 1434:0 _solve_system - F
    F 2647:0 unrad - F
    F 110:0 checksol - F
    F 2238:0 _tsolve - F
    F 2482:0 _invert - F
    F 1862:0 solve_linear_system - E
    F 1781:0 minsolve_linear_system - D
    F 1636:0 solve_linear - D
    F 2382:0 nsolve - C

11 blocks (classes, functions, methods) analyzed.
Average complexity: F (61.0)
```

### Rust
26、[komorebi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LGUG2Z/komorebi)：Window Tiling Manager for Windows. This is a desktop window management tool specially designed for Windows, supporting automatic window tiling, management of multiple virtual desktops, and multi-monitor functionality, applicable to Windows 10 and higher versions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/390873100.png' style="max-width:80%; max-height=80%;"></img></p>

27、[min-sized-rust](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/johnthagen/min-sized-rust)：Methods to Optimize the Size of Rust Binaries. By default, Rust does not optimize the size of the binary files during compilation. This project introduces tools and techniques to reduce the volume of Rust binaries without compromising functionality, suitable for scenarios sensitive to program size, such as embedded systems and the Internet of Things.

28、[readyset](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/readysettech/readyset)：SQL Database Caching Engine Developed in Rust. This project is a caching layer for Postgres and MySQL databases developed in Rust, featuring automatic cache maintenance, support for caching the results of complex SQL queries, and real-time data synchronization. It integrates seamlessly between existing applications and databases without the need for code modifications, significantly improving query performance.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/495863734.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift
29、[ATV-Bilibili-demo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yichengchen/ATV-Bilibili-demo)：Open Source Bilibili Client for Apple TV. This project is a Bilibili client designed specifically for Apple TV (tvOS), allowing users to watch videos, live streams, and barrage on Bilibili. It supports login, casting, search, and history features, although installation can be a bit tricky.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/352088293.jpg' style="max-width:80%; max-height=80%;"></img></p>

30、[PlayCover](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PlayCover/PlayCover)：Tool for Running iOS Games and Apps on Mac. This project is a tool designed specifically for Apple Silicon Mac devices (M-series chips) to run iOS applications and games. It simulates an iPad environment and provides keyboard mapping functionality, allowing users to play iOS games on their Mac computers. Users need to download IPA files themselves, and it is compatible with macOS 12.0 or higher.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/511961615.png' style="max-width:80%; max-height=80%;"></img></p>

### AI
31、[mem0](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mem0ai/mem0)：Python Library for Enhancing Context Continuity in Large Language Models. This project provides a memory layer for various mainstream large language models, supporting the saving of user interactions and context during conversations with LLMs, and is capable of dynamic real-time updates and adjustments, thereby enhancing the personalization of AI. It is suitable for personalized LLM applications that require long-term memory, such as learning assistants, medical assistants, and virtual companions.
```python
from mem0 import Memory
m = Memory()
# Add
result = m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
# Search
related_memories = m.search(query="What are Alice's hobbies?", user_id="alice")
# Update
result = m.update(memory_id="m1", data="Likes to play tennis on weekends")
```

32、[Retrieval-based-Voice-Conversion-WebUI](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)：Plug-and-Play AI Voice Changer. This project is a voice conversion framework based on VITS, which requires only a small amount of voice data and a regular graphics card to quickly train a high-quality voice conversion model. It offers a simple and user-friendly web and GUI interface, supporting real-time voice change, voice and accompaniment separation, and other features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/619521008.png' style="max-width:80%; max-height=80%;"></img></p>

33、[Upsonic](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Upsonic/Upsonic)：Minimalist GPT-4o Client. This project is a client for GPT-4o that is compatible with Windows, macOS, and Ubuntu. It features a minimalist user interface and supports various tasks, including reading the screen, opening applications, system audio, and text input.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/806192576.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
34、[dart_simple_live](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xiaoyaocz/dart_simple_live)：Easy-to-Use Live Streaming Tool. This project allows you to watch various mainstream live broadcasting platforms within a single APP and provides clients for Android, iOS, macOS, and Android TV.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/607042713.jpg' style="max-width:80%; max-height=80%;"></img></p>

35、[github-readme-terminal](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/x0rzavi/github-readme-terminal)：Display GitHub Profile with Retro Terminal GIFs. This project generates retro-style computer startup GIF animations based on your GitHub personal data to showcase your GitHub profile.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/719900617.gif' style="max-width:80%; max-height=80%;"></img></p>

36、[hugo-book](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alex-shpak/hugo-book)：Book-style Hugo Theme. This is an open-source Hugo theme that helps users easily create documentation sites resembling a book. It features a clean design, mobile adaptation, and multilingual support, making it suitable for technical documentation, online tutorials, and books.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/147530276.png' style="max-width:80%; max-height=80%;"></img></p>

37、[OMOTE](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/CoretechR/OMOTE)：Open Source Universal Remote Controller. This project is a universal remote controller crafted with the ESP32 that features a 2.8-inch capacitive touch screen, a 2000 mAh battery, and physical buttons, supporting infrared, WiFi, and Bluetooth connectivity options, thus enabling control over a variety of household appliances.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/655304519.gif' style="max-width:80%; max-height=80%;"></img></p>

38、[pintree](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Pintree-io/pintree)：Transform Chrome Bookmarks into a Navigation Site. This project can turn the bookmarks of the Chrome browser into a beautiful and easy-to-use navigation page with a few simple steps. Since a static site is generated, it cannot automatically synchronize newly added bookmarks.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/815891082.png' style="max-width:80%; max-height=80%;"></img></p>

39、[Scoop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ScoopInstaller/Scoop)：A Powerful Tool for Installing Software on Windows Command Line. This project is a Windows command line installation tool similar to Homebrew. It can install applications from the command line, with features such as eliminating permission pop-ups, hiding GUI wizards, automatically handling dependencies, and preventing contamination of PATH environment variables.
```
scoop install sudo
sudo scoop install 7zip git openssh --global
scoop install aria2 curl grep sed less touch
scoop install python ruby go perl
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/9994688.gif' style="max-width:80%; max-height=80%;"></img></p>

### Book
40、[introduction-to-git-and-github-ebook](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bobbyiliev/introduction-to-git-and-github-ebook)：A Beginner's Guide to Git and GitHub. This is an open-source book that introduces the basics of Git and GitHub, covering practical knowledge such as installing Git, GitHub CLI, branch management, and workflow.

41、[machine-learning-for-trading](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/stefan-jansen/machine-learning-for-trading)：Companion Code for 'Machine Learning for Algorithmic Trading'. This is a book that explains how to apply machine learning to trading strategies, and this project is the accompanying code and resources for the book. It includes over 150 code examples, covering aspects such as data collection, model training, and strategy evaluation.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/100/132754148.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub99.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub101.md">『Next』</a>
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
        <a href="https://apifox.cn/a103hello">
          <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/apifox.png" width="60px"><br>
          <sub>Apifox</sub><br>
          <sub>比 Postman 更强大</sub>
        </a>
      </th>
    </tr>
  </thead>
</table>


## Disclaimer
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
