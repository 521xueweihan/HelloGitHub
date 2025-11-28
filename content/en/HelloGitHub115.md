# HelloGitHub Vol.115
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
1、[iotop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Tomas-M/iotop)：IO Resource Monitoring Tool in Terminal.This is a command-line tool for monitoring I/O in Linux systems. It has an interactive interface and operation mode similar to the 'top' command, and supports real-time sorting and display of processes according to I/O usage rate.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/23103328.png' style="max-width:80%; max-height=80%;"></img></p>

2、[libsodium](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jedisct1/libsodium)：Out-of-the-box C Language Encryption Library.This is a modern, easy-to-use, cross-platform C language encryption library that provides comprehensive encryption operation APIs for developers. It integrates multiple encryption, signing and hash algorithms and is suitable for security communication, data protection and other scenarios.Shared by [@沐怡旸](https://hellogithub.com/en/user/76dhrs54nQGLuge)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/7710647.png' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[DepotDownloader](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SteamRE/DepotDownloader)：Steam Game Resource Command-line Download Tool.This is a command-line tool used to batch download specified contents from the Steam platform without installing the Steam client. Users can directly download files of specified games or applications through the command line, supporting parameters such as depot and manifest, and easily obtain game files of any version.

4、[PKHeX](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kwsch/PKHeX)：Pokémon Save Editing Tool.This is an open-source Pokémon save editor that supports reading and editing multiple Pokémon game save files. Users can freely modify Pokémon attributes, skills, items, Pokédex completion status, etc. It also has built-in save file validity verification functionality to ensure the safety and usability of modified saves.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/21311240.png' style="max-width:80%; max-height=80%;"></img></p>

5、[SlideSCI](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Achuan-2/SlideSCI)：Open Source PPT Editing Plugin.This is a plugin specifically designed to enhance PPT editing efficiency. It supports one-click adding of picture titles, automatic alignment, copying/pasting picture positions, and inserting Markdown text and LaTeX mathematical formulas.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/914468340.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++
6、[chrome_plus](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Bush2021/chrome_plus)：Out-of-the-box Chrome Enhancement Tool.This is a Chrome browser enhancement tool based on DLL hijacking technology. It supports double-click or right-click to close tabs, scrolling to switch tabs when hovering over the tab bar, forcibly keeping the last tab to prevent accidental browser closure, and customizing the boss key to quickly hide the window. It is compatible with all Chromium-based browsers and can be used by simply placing the DLL file in the browser directory.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

7、[quill](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/odygrd/quill)：Low-latency Asynchronous C++ Logging Library.This is a high-performance asynchronous C++ logging library designed specifically for low-latency and performance-sensitive applications. It reduces the performance impact on the main thread by handling log formatting and I/O operations in background threads, and is suitable for scenarios such as high-frequency trading and game engines.Shared by [@沐怡旸](https://hellogithub.com/en/user/76dhrs54nQGLuge)
```c++
int main()
{
  quill::Backend::start();

  quill::Logger* logger = quill::Frontend::create_or_get_logger(
    "root", quill::Frontend::create_or_get_sink<quill::ConsoleSink>("sink_id_1"));

  LOG_INFO(logger, "Hello from {}!", std::string_view{"Quill"});
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/234192998.gif' style="max-width:80%; max-height=80%;"></img></p>

8、[Vita3K](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Vita3K/Vita3K)：Open Source PSV Game Emulator.This is an experimental PS Vita emulator that supports Windows, Linux, macOS and Android platforms. It can run most PSV games and homebrew programs. It has successfully run popular games such as 'Persona 4: Golden Edition' and provides a detailed game compatibility list. The project is in an active development stage. Although there may be problems such as crashes or stutters, the overall experience is quite excellent.Shared by [@天涯孤雁](https://hellogithub.com/en/user/gf67BzSc528eYP9)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/119111364.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
9、[Ech0](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lin-snow/Ech0)：Fresh Lightweight Content Sharing Platform.This is an open-source and self-hosted lightweight content publishing platform focusing on the flow of ideas and quick sharing. It has a simple and intuitive operation interface and supports the publication and sharing of ideas, text, pictures and links. At the same time, it supports ActivityPub-like federation protocols to achieve interconnection between different instances (sites), so that content is no longer limited to a single isolated website.Shared by [@L1nSn0w](https://hellogithub.com/en/user/fdQ7xwPoCGy2UKD)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/952272279.png' style="max-width:80%; max-height=80%;"></img></p>

10、[eget](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zyedidia/eget)：One-click to Get GitHub Release Installation Package.This is a command-line tool written in Go that can automatically retrieve, download and install the published binary files (Releases) of open-source projects from GitHub without the need to manually find and download the installation package.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/397091905.gif' style="max-width:80%; max-height=80%;"></img></p>

11、[HAMi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Project-HAMi/HAMi)：Heterogeneous AI Computing Virtualization Middleware for K8s.This is a GPU sharing and scheduling management platform specifically designed for heterogeneous computing environments, aiming to maximize GPU utilization. It provides flexible, reliable, on-demand and elastic multi-heterogeneous GPU virtualization, scheduling and management capabilities, supporting various hardware and virtualization technologies from mainstream manufacturers such as NVIDIA and Ascend, and is suitable for high-performance computing scenarios such as deep learning, data processing and scientific computing.Shared by [@ysq](https://hellogithub.com/en/user/JaYG07AHXmhzIQn)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/406346103.gif' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[allure2](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/allure-framework/allure2)：Flexible Test Report Generation Tool.This is a Java-developed test report tool that supports multiple programming languages and testing frameworks. It can generate unified and detailed test reports, covering test result details, test case execution status, test coverage, etc.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/59838788.jpg' style="max-width:80%; max-height=80%;"></img></p>

13、[strimzi-kafka-operator](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/strimzi/strimzi-kafka-operator)：Easy Deployment of Kafka Cluster on K8s.This project enables developers to easily deploy and manage Apache Kafka clusters on K8s or OpenShift, simplifying the processes of installing, configuring, upgrading, expanding and monitoring Kafka clusters.

### JavaScript
14、[chronoframe](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/HoshinoSuzumi/chronoframe)：Minimal Personal Cloud Photo Album Platform.This is a powerful self-hosted personal photo album application designed specifically for displaying and sharing personal photography works. It provides a simple and easy-to-use web interface, allowing you to easily manage and browse photos. It supports Live Photo and Motion Photo formats and has functions such as EXIF information parsing, geographical location recognition and map exploration.Shared by [@星野鈴美](https://hellogithub.com/en/user/kLVoiAFPJaBtr1D)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1042231422.png' style="max-width:80%; max-height=80%;"></img></p>

15、[OpenStock](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Open-Dev-Society/OpenStock)：Free and Cool Stock Market App.This is a stock market platform built with Next.js, TailwindCSS and MongoDB, providing real-time quotes, charts (candlestick charts, heat maps), news and personalized monitoring. It focuses on data display and analysis and does not support trading.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1065936302.png' style="max-width:80%; max-height=80%;"></img></p>

16、[pages-cms](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pages-cms/pages-cms)：CMS Designed Specifically for Static Websites.This is a content management system (CMS) designed specifically for static website generators, supporting Jekyll, Next.js, VuePress, and Hugo, etc. It provides a friendly user interface, allowing non-technical personnel to easily edit and update website content. All changes will be automatically converted into commits on GitHub.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/732374797.png' style="max-width:80%; max-height=80%;"></img></p>

17、[twake-drive-legacy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/linagora/twake-drive-legacy)：Free and Open Source Google Drive Alternative.This is a cloud storage platform built with Node.js and MongoDB, providing file management and storage functions similar to Google Drive. It supports one-click deployment with Docker.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/617880579.png' style="max-width:80%; max-height=80%;"></img></p>

18、[zustand](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pmndrs/zustand)：Making React State Management Easier.This is a lightweight, fast, and easy-to-extend React state management library that provides developers with a concise and efficient state management experience. It has a simple API, supports directly defining and using states, and manages states through custom Hooks, helping you stay away from the complexity and pitfalls of traditional state management solutions.
```typescript
import { create } from 'zustand'

type Store = {
  count: number
  inc: () => void
}

const useStore = create<Store>()((set) => ({
  count: 1,
  inc: () => set((state) => ({ count: state.count + 1 })),
}))

function Counter() {
  const { count, inc } = useStore()
  return (
    <div>
      <span>{count}</span>
      <button onClick={inc}>one up</button>
    </div>
  )
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/180328715.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
19、[local-dream](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xororz/local-dream)：Running Stable Diffusion on Android Devices.This is a local Stable Diffusion AI painting app designed specifically for Android users. It runs completely offline and is compatible with Qualcomm Snapdragon NPU, CPU and GPU. It supports text-to-image, image-to-image and image repair functions.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/922050275.jpg' style="max-width:80%; max-height=80%;"></img></p>

20、[Voice-Recorder](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/FossifyOrg/Voice-Recorder)：Minimal Android Voice Recording App.This is a super easy-to-use Android voice recording app that supports offline recording, has no ads, and has a clean interface. It is suitable for scenarios such as meeting minutes, classroom notes, interviews, and daily memos.Shared by [@ewiro](https://hellogithub.com/en/user/iItGgWoJjnLsr0Y)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/595828370.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python
21、[checkov](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bridgecrewio/checkov)：Open Source IaC Static Code Analysis Tool.This is a static code analysis tool for Infrastructure as Code (IaC), aiming to help developers detect and prevent cloud infrastructure configuration errors and security vulnerabilities during the construction phase. It supports static detection of IaC files for multiple cloud platforms such as AWS, Azure, GCP, and Kubernetes (such as Terraform, CloudFormation, Kubernetes YAML, etc.), and can also analyze security risks in container images and open source dependency packages.Shared by [@刘睿华](https://hellogithub.com/en/user/TJ65FfbQU09PLHM)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/224386599.gif' style="max-width:80%; max-height=80%;"></img></p>

22、[docling](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/docling-project/docling)：Multi-format Document Parsing and Export Tool.This is a Python tool open-sourced by IBM, specifically designed to convert various documents into formats suitable for generative AI. It can export multiple popular document formats such as PDF, DOCX, PPTX, images, HTML, and Markdown into Markdown and JSON formats. It supports multiple OCR engines (for PDF) and a unified document object (DoclingDocument), and can be easily integrated into retrieval-augmented generation (RAG) and question-answering applications. It is suitable for scenarios where documents need to be used as input for generative AI models.
```python
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # PDF path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "### Docling Technical Report[...]"
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/826168160.png' style="max-width:80%; max-height=80%;"></img></p>

23、[gpu-hot](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/psalias2006/gpu-hot)：Real-time NVIDIA GPU Web Monitoring Panel.This is a real-time NVIDIA GPU monitoring dashboard developed based on FastAPI, supporting multiple GPU indicators such as utilization, memory, temperature, power consumption, and fan speed. It pushes data in real-time through WebSocket and supports multi-GPU, single-machine, and GPU cluster environments. It can be deployed with one click through Docker.Shared by [@wanzij](https://hellogithub.com/en/user/QkXB6ugmwMTqteF)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1070160746.png' style="max-width:80%; max-height=80%;"></img></p>

24、[PyQt-Frameless-Window](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zhiyiYo/PyQt-Frameless-Window)：Cross-platform Borderless Window Based on PyQt5.This project is a cross-platform borderless window component based on PyQt/PySide. While achieving the borderless window effect, it retains the basic functions of the window and is compatible with Windows, Linux, and macOS. It also supports window effects such as Acrylic and Mica.
```python
import sys

from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow


class Window(FramelessWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("PyQt-Frameless-Window")
        self.titleBar.raise_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/347549476.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[quark-auto-save](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Cp0204/quark-auto-save)：Quark Netdisk Auto Saving Tool.This is a Python-developed Quark Netdisk automation tool that supports functions such as netdisk sign-in, automatic saving, file naming and organizing, push reminders, and automatic refreshing of Emby media libraries.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/735799919.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust
26、[touchHLE](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/touchHLE/touchHLE)：Bring Classic iPhone Games Back to Life on Modern Devices.This project is an iOS game simulator developed with Rust, capable of running early versions of iOS games such as iPhone OS 2.x and 3.x. It uses high-level emulation (HLE) technology to run applications by implementing native frameworks like UIKit and OpenGL ES instead of directly simulating the underlying hardware, and supports Windows, macOS, and Android platforms.Shared by [@kero990](https://hellogithub.com/en/user/c3Y4NR1rq6neVoD)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/573107980.png' style="max-width:80%; max-height=80%;"></img></p>

27、[yaak](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mountain-loop/yaak)：Offline-first Desktop API Client.This is a fast, offline-first desktop API client that supports REST, GraphQL, SSE, WebSocket and gRPC protocols. It is built with Rust, Tauri and React, with a friendly interface, cross-platform availability, no telemetry and cloud locking, providing a simple and pure, distraction-free usage experience.Shared by [@刘睿华](https://hellogithub.com/en/user/TJ65FfbQU09PLHM)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/602379707.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
28、[bitchat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/permissionlesstech/bitchat)：Bluetooth-based Instant Communication Application.This is a server-less Bluetooth instant communication application designed specifically for non-network environments. By combining Bluetooth Mesh and Nostr protocols, it achieves end-to-end encrypted point-to-point communication and supports features such as message retry, offline forwarding, multi-user, and automatic discovery. It is suitable for small-scale instant communication scenarios such as disaster relief volunteers and field exploration teams.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1013830656.jpg' style="max-width:80%; max-height=80%;"></img></p>

29、[Dayflow](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/JerryZLiu/Dayflow)：macOS App for Automatically Generating Daily Timeline.This is a macOS app developed with Swift. It automatically generates a daily timeline by recording screen activities and combining with AI. It records the screen at a rate of 1 frame per second and uses AI to analyze the recorded content every 15 minutes to generate a concise activity summary. At the same time, it automatically deletes recorded files that are more than 3 days old to save storage space.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1062234789.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
30、[BrowserOS](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/browseros-ai/BrowserOS)：Open-source AI Browser.This project is an open-source AI browser based on Chromium, which can run AI Agents in the local browser and serve as an open-source alternative to ChatGPT Atlas, Perplexity Comet and Dia. While retaining the familiar interface and extension compatibility of Chrome, it helps users achieve AI-driven browser automation and intelligent question-answering tasks, and supports custom LLM services or local large models.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/985839104.gif' style="max-width:80%; max-height=80%;"></img></p>

31、[cache-dit](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vipshop/cache-dit)：Train-free DiT Model Caching Acceleration Framework.This project is a framework that provides unified caching acceleration for Diffusers. It supports almost all DiT diffusion models, including Qwen-Image-Lightning, Qwen-Image, HunyuanImage, Wan, FLUX, etc. It can achieve efficient caching acceleration through simple code and significantly improve the inference speed without retraining the model.Shared by [@DefTruth](https://hellogithub.com/en/user/ofSCbzTmdeQk3FD)
```python
import cache_dit
from diffusers import DiffusionPipeline
pipe = DiffusionPipeline.from_pretrained("Qwen/Qwen-Image") # Can be any diffusion pipeline
cache_dit.enable_cache(pipe) # One-line code with default cache options.
output = pipe(...) # Just call the pipe as normal.
stats = cache_dit.summary(pipe) # Then, get the summary of cache acceleration stats.
cache_dit.disable_cache(pipe) # Disable cache and run original pipe.
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1000711946.png' style="max-width:80%; max-height=80%;"></img></p>

32、[graphiti](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/getzep/graphiti)：Building Real-time Knowledge Graphs for AI Agents.This is a framework designed specifically for AI agents to build and query real-time, time-aware knowledge graphs. It can continuously integrate dynamic data such as user interactions, structured or unstructured data to form a coherent and queryable knowledge graph. It supports incremental data updates, efficient retrieval and historical queries, and is suitable for developing interactive, context-aware AI applications.Shared by [@塔咖](https://hellogithub.com/en/user/bzJpGyu0IanC6L7)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/840056306.gif' style="max-width:80%; max-height=80%;"></img></p>

33、[LEANN](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yichuan-w/LEANN)：Ultra-low Storage Occupancy Vector Database.This is an open-source lightweight vector database that achieves extremely low storage occupancy by computing embedded vectors on demand. Users can build powerful and fully private retrieval-augmented generation (RAG) systems on personal devices (laptops) and support semantic search on various data sources such as local files, emails, browser history, chat records, etc.Shared by [@Yichuan Wang](https://hellogithub.com/en/user/Tj5AEF9BDNXpKnk)
```python
from leann import LeannBuilder, LeannSearcher, LeannChat
from pathlib import Path
INDEX_PATH = str(Path("./").resolve() / "demo.leann")

# Build an index
builder = LeannBuilder(backend_name="hnsw")
builder.add_text("LEANN saves 97% storage compared to traditional vector databases.")
builder.add_text("Tung Tung Tung Sahur called—they need their banana‑crocodile hybrid back")
builder.build_index(INDEX_PATH)

# Search
searcher = LeannSearcher(INDEX_PATH)
results = searcher.search("fantastical AI-generated creatures", top_k=1)

# Chat with your data
chat = LeannChat(INDEX_PATH, llm_config={"type": "hf", "model": "Qwen/Qwen3-0.6B"})
response = chat.ask("How much storage does LEANN save?", top_k=1)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/998732712.png' style="max-width:80%; max-height=80%;"></img></p>

34、[surf](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/deta/surf)：Cross-media Personal AI Note App.This is a local-first AI notebook tool that can integrate multiple media types (such as local files, webpages, videos, etc.) into a local database and quickly generate notes with the help of AI. It helps users avoid the cumbersome operations of switching, searching, and manually copying and pasting between multiple applications and media such as browsers, note applications, and PDF readers during the learning and research process, and at the same time supports flexible selection of AI models.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1079906817.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
35、[anki-jlpt-decks](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/5mdld/anki-jlpt-decks)：Japanese Card Deck with Full Voice-matching for Ten Thousand Words.This is a high-quality Japanese word card deck made for the learning software Anki, covering JLPT (Japanese Language Proficiency Test) N1 to N5 levels, with a total of ten thousand words. Each entry includes meanings, examples, part of speech, as well as related words and antonyms.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/902164245.png' style="max-width:80%; max-height=80%;"></img></p>

36、[Berkeley-Humanoid-Lite](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)：Open-source Humanoid Robot.This project is open-sourced by the Berkeley Hybrid Robotics team. It aims to provide low-cost, modular and customizable humanoid robot solutions. The robot uses 3D printing and common components, with a total cost of less than $5000. It is suitable for multiple fields such as robot research, algorithm development and teaching experiments.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/950286225.png' style="max-width:80%; max-height=80%;"></img></p>

37、[document](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ranuts/document)：Online Office File Editor.This is a local web document editor based on OnlyOffice and WebAssembly. It is implemented purely on the front end and does not require server-side processing. Users can directly open and edit DOCX, XLSX, PPTX and other format documents in the browser.

38、[leetgpu-challenges](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AlphaGPU/leetgpu-challenges)：GPU Programming Battle in Practice.This project provides a series of GPU programming exercises in the style of LeetCode, including answer keys, test cases, and template codes for various GPU programming frameworks.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1022920558.png' style="max-width:80%; max-height=80%;"></img></p>

39、[NCE](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/iChochy/NCE)：Online Reading of All Four Volumes of 'New Concept English'.This project provides a convenient online learning platform for 'New Concept English' learners. It combines American pronunciation audio with Chinese subtitles generated by Gemini AI and supports reading of texts and single-sentence point reading.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/115/1063065062.png' style="max-width:80%; max-height=80%;"></img></p>

40、[pandoc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jgm/pandoc)：General Markup Language Conversion Tool.This project can convert multiple document formats to each other, supporting formats such as Markdown, HTML, LaTeX, Word, PDF, EPUB, etc. It is widely used in writing, academic papers, publishing and other scenarios.Shared by [@Xuefeng Xu](https://hellogithub.com/en/user/k4oyT8wSU5Qfx6H)

### Book
41、[agentic-design-patterns-cn](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ginobefun/agentic-design-patterns-cn)：Agentic Design Patterns Chinese Translation Version.This project is a Chinese-English parallel version of the book 'Agentic Design Patterns'. This book systematically introduces practical methods and design patterns for building modern AI agents (Agents), including prompt chains, RAG, MCP, and multi-agent collaboration.



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub114.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub116.md">『Next』</a>
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
