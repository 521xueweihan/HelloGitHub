# HelloGitHub Vol.99
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
1、[HandBrake](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/HandBrake/HandBrake)：Free Open Source Video Transcoding Tool. This is a powerful, community-driven open source video transcoding tool that supports the conversion of various video file formats into common formats such as MP4 and MKV.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/41215835.png' style="max-width:80%; max-height=80%;"></img></p>

### C#
2、[SwashbucklerDiary](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Yu-Core/SwashbucklerDiary)：The Diary of a Wandering Knight that Records Life's Moments. The author of this project developed this offline-first journal app because of a fondness for writing diaries. It features a clean and simple interface, allowing users to record the weather, mood, and location when writing a diary entry. Besides supporting online use on the Web, it also offers clients for Android, Windows, iOS, and macOS.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/581626532.png' style="max-width:80%; max-height=80%;"></img></p>

3、[SyncClipboard](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Jeric-X/SyncClipboard)：Cross-Platform Clipboard Synchronization Tool. This project allows for seamless synchronization of clipboard content across various devices, supporting text, images, and files. Users can choose to deploy their own server or use a cloud storage service that supports the WebDAV protocol.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/91249910.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
4、[ladybird](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/LadybirdBrowser/ladybird)：Truly Independent Open Source Browser. The author of this project aims to build a completely independent open-source web browser from scratch, so he has separated the browser engine part from his own SerenityOS operating system, planning to create a completely new, cross-platform open-source browser based on this, which does not contain code from other browsers. Currently, no downloadable installation package is available, and the first Alpha version is planned to be released in the summer of 2026.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/808045485.png' style="max-width:80%; max-height=80%;"></img></p>

5、[mosh](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mobile-shell/mosh)：Remote Terminal Tool for Mobile Devices. This is a remote terminal tool specifically designed for mobile and unstable network environments. It can maintain stable remote sessions and faster responses even during network switches, high latency, and IP changes, suitable for systems such as Android, iOS, Linux, and macOS.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/1234783.png' style="max-width:80%; max-height=80%;"></img></p>

6、[OpenArk](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/BlackINT3/OpenArk)：Professional Windows Malware Analysis and Cleaning Tool. This is a tool designed for combating and cleaning up Rootkits (malicious software) on the Windows platform. It helps programmers to identify hidden malware within the system and supports functions such as viewing processes, process injection, kernel driver mode, and scanning.Shared by [@SHOWTA](https://hellogithub.com/en/user/GAeFLr6oWyYcnbp)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/183564981.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
7、[dblab](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/danvergara/dblab)：Interactive Database Command-line Client. This is a lightweight, interactive TUI (Text-based User Interface) database client written in Go. It is easy to use and comes with out-of-the-box convenience, supporting PostgreSQL, MySQL, SQLite3, and Oracle databases. It is not about affordability for desktop applications, but rather about the cost-effectiveness of command-line interfaces.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/352879222.gif' style="max-width:80%; max-height=80%;"></img></p>

8、[go-size-analyzer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Zxilly/go-size-analyzer)：Tool for Analyzing the Size of Compiled Go Files. This project utilizes reverse engineering and disassembly to collect addresses from binary files, combines them, and calculates the size occupied by each dependency in the final binary file, showcasing the results in a visual manner. It can be used to analyze the file size after compilation of Go programs and supports both command-line and web usage methods.Shared by [@Zxilly](https://hellogithub.com/en/user/QksOfglJ0njwLKa)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/609147387.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[gws](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lxzan/gws)：Simple and Fast Go WebSocket Library. This project is a WebSocket library written in Go. It provides a clean and straightforward API, featuring high throughput, low latency, minimal memory usage, and stable reliability. It is suitable for high concurrency scenarios, supporting context takeover, customizable window size, and broadcasting functionality.Shared by [@道一](https://hellogithub.com/en/user/TeObZoJ8pgUvBWf)
```go
package main

import (
	"github.com/lxzan/gws"
	"net/http"
	"time"
)

const (
	PingInterval = 5 * time.Second
	PingWait     = 10 * time.Second
)

func main() {
	upgrader := gws.NewUpgrader(&Handler{}, &gws.ServerOption{
		ParallelEnabled:  true,                                 // Parallel message processing
		Recovery:          gws.Recovery,                         // Exception recovery
		PermessageDeflate: gws.PermessageDeflate{Enabled: true}, // Enable compression
	})
	http.HandleFunc("/connect", func(writer http.ResponseWriter, request *http.Request) {
		socket, err := upgrader.Upgrade(writer, request)
		if err != nil {
			return
		}
		go func() {
			socket.ReadLoop() // Blocking prevents the context from being GC.
		}()
	})
	http.ListenAndServe(":6666", nil)
}

type Handler struct{}

func (c *Handler) OnOpen(socket *gws.Conn) {
	_ = socket.SetDeadline(time.Now().Add(PingInterval + PingWait))
}

func (c *Handler) OnClose(socket *gws.Conn, err error) {}

func (c *Handler) OnPing(socket *gws.Conn, payload []byte) {
	_ = socket.SetDeadline(time.Now().Add(PingInterval + PingWait))
	_ = socket.WritePong(nil)
}

func (c *Handler) OnPong(socket *gws.Conn, payload []byte) {}

func (c *Handler) OnMessage(socket *gws.Conn, message *gws.Message) {
	defer message.Close()
	socket.WriteMessage(message.Opcode, message.Bytes())
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/534446803.png' style="max-width:80%; max-height=80%;"></img></p>

10、[river](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/riverqueue/river)：Postgres-Based Background Task Management Platform. This project is a task queue developed with Go and the Postgres database, featuring a built-in web management backend, supporting automatic retries, scheduled tasks, and priorities.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/716228772.png' style="max-width:80%; max-height=80%;"></img></p>

11、[watermill](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ThreeDotsLabs/watermill)：Go Library for Rapid Development of Event-Driven Applications. This is a Go library for efficiently handling streams of messages, i.e., publishing/receiving messages and reacting to them. It is easy to start with and supports message brokers such as Kafka, RabbitMQ, HTTP, and MySQL binlog, suitable for scenarios like real-time data stream processing, distributed transactions, and microservices communication.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)
```go
func main() {
	saramaSubscriberConfig := kafka.DefaultSaramaSubscriberConfig()
	// equivalent of auto.offset.reset: earliest
	saramaSubscriberConfig.Consumer.Offsets.Initial = sarama.OffsetOldest

	subscriber, err := kafka.NewSubscriber(
		kafka.SubscriberConfig{
			Brokers:               []string{"kafka:9092"},
			Unmarshaler:           kafka.DefaultMarshaler{},
			OverwriteSaramaConfig: saramaSubscriberConfig,
			ConsumerGroup:         "test_consumer_group",
		},
		watermill.NewStdLogger(false, false),
	)
	if err != nil {
		panic(err)
	}

	messages, err := subscriber.Subscribe(context.Background(), "example.topic")
	if err != nil {
		panic(err)
	}

	go process(messages)
// ...
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/156768326.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[spring-reading](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xuchengsheng/spring-reading)：Spring Source Code Reading. This is a tutorial with illustrations and text explaining the Spring source code. The content covers the core concepts and key features of the Spring framework, and it also thoughtfully marks the difficulty level, making it more convenient for learning.Shared by [@Lex](https://hellogithub.com/en/user/AVv4KeNnZs2Ig3a)

13、[xpipe](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xpipe-io/xpipe)：Tool for One-Click Remote Login to Docker Instances. This project is a desktop tool for managing remote servers, which automatically detects the server environment and shell type after establishing an SSH connection. It achieves one-click login to various container instances (Docker, LXC, WSL) and supports features like remote file management and tool integration.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/593867048.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
14、[earthworm](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cuixueshe/earthworm)：English Learning Website That Makes You Addicted. This is an open-source online English learning website that supports self-hosting and local operation. It uses a method of forming sentences by connecting words and gradually advancing to help you learn English. By continuously repeating to form muscle memory, combined with game rewards and point rankings, it makes memorizing vocabulary fun and efficient.Shared by [@Immerse](https://hellogithub.com/en/user/249cPWvjfNmU7dp)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/741759862.png' style="max-width:80%; max-height=80%;"></img></p>

15、[million](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/aidenybai/million)：Tool for Optimizing React Component Performance. This project is an optimization compiler designed for React applications, which enhances React component performance by optimizing the virtual DOM and directly updating DOM nodes to reduce the time required for page updates, with the largest improvement being up to 70%. It supports usage through VSCode plugins and command line interfaces.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/372046384.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[pouchdb](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pouchdb/pouchdb)：Open Source JavaScript Database. This project is a browser-based NoSQL database written in JavaScript. It can store data locally in an offline state and automatically synchronize the data to keep it in sync with the server once the network is restored.
```javascript
var db = new PouchDB('dbname');

db.put({
  _id: 'hellogithub-1',
  name: 'HelloGitHub',
  age: 69
});

db.changes().on('change', function() {
  console.log('Ch-Ch-Changes');
});

db.replicate.to('远程数据库地址');
```

17、[stf](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/DeviceFarmer/stf)：Control Multiple Android Devices Through the Browser. This is an Android device testing tool developed using Node.js, providing a web platform that can remotely debug multiple Android devices, supporting devices such as Android phones and smartwatches.Shared by [@wang-qa](https://hellogithub.com/en/user/sPm5nXvGN2VlWCr)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/246332156.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[ua-parser-js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/faisalman/ua-parser-js)：User-Agent Parsing JS Library. This is a library for parsing User-Agent strings, which can turn the User-Agent string into a UAParser object, facilitating the detection and viewing of the user's browser, operating system, CPU, and device model information.
```javascript
const parser = new UAParser(ua);

console.log(parser.getResult());
/*
{
    ua: "Mozilla/5.0 (Linux; Android 10; STK-LX1 Build/HONORSTK-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 musical_ly_2022803040 JsSdk/1.0 NetType/WIFI Channel/huaweiadsglobal_int AppName/musical_ly app_version/28.3.4 ByteLocale/en ByteFullLocale/en Region/IQ Spark/1.2.7-alpha.8 AppVersion/28.3.4 PIA/1.5.11 BytedanceWebview/d8a21c6",
    browser: {
        name: "TikTok",
        version: "28.3.4",
        major: "28"
    },
    cpu: {},
    device: {
        type: "mobile",
        model: "STK-LX1",
        vendor: "Huawei"
    },
    engine: {
        name: "Blink",
        version: "110.0.5481.153"
    },
    os: {
        name: "Android",
        version: "10"
    }
}
*/
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/3320710.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP
19、[openemr](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/openemr/openemr)：Open Source Hospital Management System for Free. This project is the most popular open source hospital management system currently available. It integrates all the functionalities required for the daily operations of a hospital, such as appointments, patient profiles, electronic billing, and medical records, while also supporting more than 30 languages, including Chinese.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/679584.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
20、[CleanMyWechat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/blackboxo/CleanMyWechat)：Tool for Automatically Deleting WeChat Cache Data on PC. This project is a Windows utility written with PyQt5, designed to clean up useless data that the WeChat PC client automatically downloads. It supports automatic recognition of accounts, multi-account management, selection of file types for cleanup, and setting the duration for file cleanup.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/240239451.jpg' style="max-width:80%; max-height=80%;"></img></p>

21、[searxng](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/searxng/searxng)：A Python-based Metasearch Engine that Respects Individual Privacy. This project is a metasearch engine built on Flask that can aggregate search results from more than 70 search engines. It is easy to install, does not track user behavior, and supports features such as selecting search engines, safe search, and multi-language capabilities.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/357241735.png' style="max-width:80%; max-height=80%;"></img></p>

22、[vulture](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jendrikseipp/vulture)：Python's 'Dead' Code Detective. This is a static code analysis tool for Python. It can identify unused code in a Python project, and with a single command, it can clean up useless and invalid Python functions, variables, and code snippets.

23、[warp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NVIDIA/warp)：Python Framework for Writing High-Performance Simulation Programs. This project is an open-source Python framework from NVIDIA that uses just-in-time compilation to convert Python code into efficient kernel code that can run on CPUs or GPUs. It can be used to write programs for simulating physical environments, collision detection, and graphics processing.
```python
import warp as wp
import numpy as np

num_points = 1024

@wp.kernel
def length(points: wp.array(dtype=wp.vec3),
           lengths: wp.array(dtype=float)):

    # thread index
    tid = wp.tid()
    
    # compute distance of each point from origin
    lengths[tid] = wp.length(points[tid])


# allocate an array of 3d points
points = wp.array(np.random.rand(num_points, 3), dtype=wp.vec3)
lengths = wp.zeros(num_points, dtype=float)

# launch kernel
wp.launch(kernel=length,
          dim=len(points),
          inputs=[points, lengths])

print(lengths)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/471527576.jpg' style="max-width:80%; max-height=80%;"></img></p>

24、[wsgidav](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mar10/wsgidav)：WSGI-Based WebDAV Server. WebDAV is a communication protocol that allows direct editing and management of files on the network, commonly used in scenarios such as document sharing, cloud storage, and file synchronization. This project is a WebDAV server written in Python that can run independently, comes with a simple web interface, supports online editing of MS Office documents, and features authentication capabilities.
```
$ pip install wsgidav cheroot
$ wsgidav --host=0.0.0.0 --port=80 --root=/tmp --auth=anonymous
Running without configuration file.
10:54:16.597 - INFO    : WsgiDAV/4.0.0-a1 Python/3.9.1 macOS-12.0.1-x86_64-i386-64bit
10:54:16.598 - INFO    : Registered DAV providers by route:
10:54:16.598 - INFO    :   - '/:dir_browser': FilesystemProvider for path '/Users/martin/prj/git/wsgidav/wsgidav/dir_browser/htdocs' (Read-Only) (anonymous)
10:54:16.599 - INFO    :   - '/': FilesystemProvider for path '/tmp' (Read-Write) (anonymous)
10:54:16.599 - WARNING : Basic authentication is enabled: It is highly recommended to enable SSL.
10:54:16.599 - WARNING : Share '/' will allow anonymous write access.
10:54:16.813 - INFO    : Running WsgiDAV/4.0.0-a1 Cheroot/8.5.2 Python 3.9.1
10:54:16.813 - INFO    : Serving on http://0.0.0.0:80 ...
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/15376784.png' style="max-width:80%; max-height=80%;"></img></p>

### Ruby
25、[lolcommits](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lolcommits/lolcommits)：Selfie for Programmers Based on Git. This project automatically takes a photo with the webcam each time a code is committed using git, marking the commit ID on the photo. This not only records life but also allows you to quickly identify the author of the code.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/2499845.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust
26、[100-exercises-to-learn-rust](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mainmatter/100-exercises-to-learn-rust)：100 Exercises to Learn Rust. This tutorial adheres to the principle of learning by doing, containing approximately 100 exercises and their answers, guiding you to learn the Rust programming language from scratch.

27、[crossbeam](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/crossbeam-rs/crossbeam)：Rust Concurrency Programming Toolkit. In the world of Rust concurrency programming, it serves as a Swiss Army knife, providing a rich and powerful set of lock-free concurrent data structures and tools, which greatly enhance the efficiency of Rust concurrency programming.Shared by [@DeShuiYu](https://hellogithub.com/en/user/ZWJkOqsvYbPgD8p)

28、[zellij](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zellij-org/zellij)：Easier Terminal Multiplexer for Beginners. This project is a terminal multiplexer written in Rust, which supports features like single window multiple tabs, split windows, and automatic reconnection. It offers a ready-to-use default configuration along with a powerful plugin system, making it popular among both beginners and advanced users.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/292014229.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift
29、[Loop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/MrKai77/Loop)：Elegant macOS Window Management Tool. This is a minimalist window management application for macOS that requires no complex configuration. With simple key combinations, you can easily move the window position, adjust the window size, and arrange the windows. The interaction is very elegant, and the user experience is excellent.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/592882602.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[noTunes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tombonez/noTunes)：Tool to Disable iTunes. This is a macOS application that can prevent iTunes or Apple Music from automatically launching and popping up. It also supports setting up an alternative to iTunes.

### AI
31、[gateway](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Portkey-AI/gateway)：Large Language Model API Aggregation Gateway. This project provides a unified and fast API, allowing developers to easily access over 200 LLMs, and also supports multi-modality, automatic retry, and load balancing features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/682080300.gif' style="max-width:80%; max-height=80%;"></img></p>

32、[MoneyPrinterTurbo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/harry0703/MoneyPrinterTurbo)：One-Click AI Tool for Generating Short Videos. This project is an AI video generation tool based on large-scale model services. It can automatically generate high-definition short videos just by providing a topic or keyword. It features an easy-to-use web interface that supports batch generation, setting video duration, and screen orientation (portrait/landscape) among other functionalities.Shared by [@jolahua](https://hellogithub.com/en/user/8zvgylhiA5ds49u)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/770153867.jpg' style="max-width:80%; max-height=80%;"></img></p>

33、[Omost](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lllyasviel/Omost)：Minimalist Prompt-word Mind-mapping Tool. This project leverages the programming capabilities of Large Language Models (LLM) to help users automatically complete the prompt words for mind mapping. It can generate high-quality images based on brief user-provided prompt words and supports features like localized image modification, such as turning a dragon into a dinosaur within an image, significantly reducing the barrier to creating satisfying images without the need for complex prompt words.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/807619678.png' style="max-width:80%; max-height=80%;"></img></p>

34、[Scrapegraph-ai](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ScrapeGraphAI/Scrapegraph-ai)：AI-based Python Web Scraper. This is a Python web scraping library powered by AI. Leveraging the capabilities of Large Language Models (LLM), it can automatically capture data from target websites based on prompt words.
```python
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the projects with their descriptions",
    source="目标网站",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
```

### Other
35、[anx-reader](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Anxcye/anx-reader)：Free Android Ebook Reader. This is an ebook reading software written with Flutter. It is free and ad-free, supports WebDAV for syncing ebooks, notes, and reading progress, and is suitable for Android smartphones and tablets.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/778774319.jpg' style="max-width:80%; max-height=80%;"></img></p>

36、[etcher](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/balena-io/etcher)：Easy-to-Use USB/SD Bootable Disk Creation Tool. This project enables the burning of the OS image into an SD card or USB device, which can be used to create a bootable and portable operating system. It features a user-friendly interface, allowing the creation of a USB bootable disk in just 3 steps, suitable for Linux, macOS, and Windows 10 and above.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/45055693.png' style="max-width:80%; max-height=80%;"></img></p>

37、[GmsCore](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microg/GmsCore)：Open Source Alternative to Google Services Framework. This project is an open-source solution as an alternative to Google Play Services, allowing users who cannot or do not wish to use Google services to run Android applications dependent on Google services.

38、[OpenGlass](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/BasedHardware/OpenGlass)：Low-Cost AI Smart Glasses. This project offers a budget solution for upgrading regular glasses to AI smart glasses for just $25. It supports video recording, object recognition, and text translation functions. However, it requires cooperation with a computer and does not support displaying content on the lens.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/799645136.jpg' style="max-width:80%; max-height=80%;"></img></p>

39、[scribe](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/stephband/scribe)：Display Sheet Music in HTML Style. This project implements the display of musical symbols and sheet music on a webpage using CSS+SVG+HTML code.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/99/14271569.png' style="max-width:80%; max-height=80%;"></img></p>

40、[WTF-zk](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/WTFAcademy/WTF-zk)：An Introduction to Zero-Knowledge Proofs. This is a beginner-level tutorial on zero-knowledge proofs, a technology that allows one party to prove something is true to another party without revealing any specific information, commonly used in cryptography, privacy computation, and Web3 areas.

### Book
41、[introduction-to-bash-scripting](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bobbyiliev/introduction-to-bash-scripting)：Introduction to Bash Scripting Guide. This is an open-source book that teaches you how to write excellent Bash scripts.

42、[PyTorch-Tutorial-2nd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TingsongYu/PyTorch-Tutorial-2nd)：A Practical Guide to PyTorch. This book comprehensively introduces the basic knowledge of PyTorch, including a wealth of PyTorch practical cases and large-scale language model deployment examples, enabling you to quickly get started with PyTorch and possess excellent development capabilities.Shared by [@TingsongYu](https://hellogithub.com/en/user/vYkuK6UpxDah9mL)



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub98.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub100.md">『Next』</a>
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
