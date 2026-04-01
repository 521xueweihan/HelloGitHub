# HelloGitHub Vol.106
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
1、[sshfs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/libfuse/sshfs)：A tool for mounting remote file systems via SSH. This is a file system tool based on the SFTP protocol, which allows you to mount remote file systems to the local machine via the SSH protocol. It is easy to operate and only requires a single command to manage remote files and directories as if accessing a local file system, compatible with Linux, BSD, and macOS systems.
```
挂载文件系统
sshfs [user@]hostname:[directory] mountpoint
卸载文件系统
fusermount -u mountpoint
```

### C#
2、[mRemoteNG](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mRemoteNG/mRemoteNG)：Multi-Protocol Integrated Remote Connection Management Tool. This is a powerful remote connection management tool that supports various mainstream protocols such as RDP, VNC, and SSH. It features a tabbed interface, allowing users to manage and switch between multiple remote connections simultaneously, while supporting systems like Windows 11 and 10.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/460848.png' style="max-width:80%; max-height=80%;"></img></p>

3、[msstyleEditor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nptr/msstyleEditor)：Out-of-the-box Windows Visual Style Editor. This is a tool for editing Windows visual styles (.msstyles files), compatible with Windows 7, 8, 10, and 11 systems. It is ready to use out of the box, supports quick viewing of all components and modification of their properties, and easily customizes theme styles.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/93086337.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
4、[Memento](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ripose-jp/Memento)：A Video Player for Learning Japanese While Watching Videos. This is an open-source video player based on mpv, specifically designed for learning Japanese. It assists users in learning Japanese while watching videos, supporting features such as pop-up dictionaries, subtitle browsing, and the generation and synchronization of vocabulary cards.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/302477133.png' style="max-width:80%; max-height=80%;"></img></p>

5、[mixxx](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mixxxdj/mixxx)：Free Open-Source DJ Mixing Software. This project is a professional-grade DJ software developed with C++, which is completely free. It offers a rich set of features and hardware compatibility, supports automatic BPM detection, real-time effect processing, recording, and streaming capabilities, and is applicable across Windows, macOS, and Linux platforms.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/10126031.png' style="max-width:80%; max-height=80%;"></img></p>

6、[parallel-hashmap](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/greg7mdp/parallel-hashmap)：High-performance HashMap Library. This project provides various high-performance, memory-friendly, and thread-safe hash table and B-tree container implementations. It is developed and optimized based on Google's Abseil library, supports the C++11 standard, and is available in header-only form, eliminating the need for compilation.
```c++
#include <iostream>
#include <string>
#include <parallel_hashmap/phmap.h>

using phmap::flat_hash_map;

int main()
{
    flat_hash_map<std::string, std::string> nickname =
    {
        { "tom",  "tomcat"},
        { "jim",  "jimoby"}
    };

    for (const auto& n : nickname)
        std::cout << n.first << "'s nickname is: " << n.second << "\n";

    email["bill"] = "hellogithub";
    std::cout << "bill's nickname is: " << nickname["bill"] << "\n";

    return 0;
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/173454206.png' style="max-width:80%; max-height=80%;"></img></p>

7、[upx](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/upx/upx)：Utility for Compressing Executable Files. This is an open-source tool for compressing executable files, supporting various executable file formats (Windows, Linux, macOS). It boasts an excellent compression ratio (50-70%), and the compressed files can be run directly, making it suitable for program distribution and large-scale storage scenarios.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/67031040.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
8、[bunster](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yassinebenaid/bunster)：A Tool to 'Compile' Shell Scripts in One Click. This project is a Shell-to-Go transpiler, which works by first converting shell scripts to Go code and then leveraging the Go toolchain to compile them into binary executable files, addressing the traditional performance, portability, and security deficiencies of shell scripts.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/831420946.gif' style="max-width:80%; max-height=80%;"></img></p>

9、[daytona](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/daytonaio/daytona)：A Tool for Simplifying Development Environment Setup. This project enables the quick creation of a configured development environment with a single command, supports seamless integration with mainstream IDEs, and integrates with various infrastructures such as local machines, remote servers, and cloud platforms.Shared by [@IZRINO](https://hellogithub.com/en/user/eK0Bv1dmJPxnrwy)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/753490180.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[gopher-lua](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yuin/gopher-lua)：Embed Lua Scripts into Go Programs. This is a Lua virtual machine and compiler implemented in Go language, fully compatible with Lua5.1 syntax. Developers can embed Lua scripts into Go applications through simple code, making it suitable for scenarios requiring script support such as game development, automation tools, and plugin systems.Shared by [@两双筷子sqldc](https://hellogithub.com/en/user/5dGtvaZ6H3L4QMY)
```go
L := lua.NewState()
defer L.Close()
if err := L.DoString(`print("hello")`); err != nil {
    panic(err)
}
```

11、[SamWaf](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/samwafgo/SamWaf)：Open source lightweight Web Application Firewall. This is a fully open-source lightweight Web Application Firewall that supports private deployment, offering Bot detection, URL whitelist, CC protection, custom protection rules, and other features, making it suitable for small businesses, studios, and personal websites.Shared by [@猎隼丶止戈reNo7](https://hellogithub.com/en/user/Ew59HqRWjPe0zZO)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/737285725.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Java
12、[mzt-biz-log](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mouzt/mzt-biz-log)：Out-of-the-box Spring Boot Operation Log Component. This is an operation log component designed for Spring Boot projects, supporting easy recording of business operation logs through annotations, including the operator, operation time, operation content, etc.Shared by [@FangPengbo](https://hellogithub.com/en/user/WtxAwC6DlVhTEJO)
```java
@LogRecord(
        fail = "创建订单失败，失败原因：「{{#_errorMsg}}」",
        success = "{{#order.purchaseName}}下了一个订单,购买商品「{{#order.productName}}」,测试变量「{{#innerOrder.productName}}」,下单结果:{{#_ret}}",
        type = LogRecordType.ORDER,
        bizNo = "{{#order.orderNo}}")
public boolean createOrder(Order order) {
    log.info("【创建订单】orderNo={}", order.getOrderNo());

    // db insert order
    Order order1 = new Order();
    order1.setProductName("内部变量测试");

    LogRecordContext.putVariable("innerOrder", order1);

    return true;
}
```

13、[poi-tl](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Sayi/poi-tl)：Java-based Word Template Engine. This project is a Word template engine based on Apache POI, capable of dynamically generating Word documents. It provides a user-friendly API, supporting the rendering of various content types such as text, images, tables, conditional rendering, and charts, suitable for mass generation of contracts, reports, notices, certificates, and other scenarios.
```java
XWPFTemplate template = XWPFTemplate.compile("template.docx").render(
  new HashMap<String, Object>(){{
    put("title", "HelloGitHub");
}});  
template.writeAndClose(new FileOutputStream("output.docx")); 
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/32567673.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
14、[openmtp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ganeshrvel/openmtp)：Android File Transfer Tool for Mac. This is an open-source Android file transfer tool designed specifically for macOS. It enables fast and stable file transfers between macOS and Android devices via USB connections, supporting macOS versions 11.0 and above.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/161636751.png' style="max-width:80%; max-height=80%;"></img></p>

15、[readest](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/readest/readest)：Immersive E-Book Reader. This is a reading software tailor-made for users who love reading, integrating minimalist design with powerful features to bring you a focused and immersive reading experience. It is developed based on Next.js and Tauri, supporting cross-platform operation and currently supporting macOS, Windows, Linux, and Web platforms. Future plans include the release of iOS and Android versions to achieve true all-platform coverage.Shared by [@Huang Xin](https://hellogithub.com/en/user/eRLUbPOy2qZtDgw)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/871781831.png' style="max-width:80%; max-height=80%;"></img></p>

16、[sharp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lovell/sharp)：High-performance Node.js Image Processing Library. This is a high-performance Node.js image processing library based on libvips, supporting operations such as resizing, format conversion, cropping, and rotation for image formats like JPEG, PNG, WebP, GIF, and SVG.
```javascript
const semiTransparentRedPng = await sharp({
  create: {
    width: 48,
    height: 48,
    channels: 4,
    background: { r: 255, g: 0, b: 0, alpha: 0.5 }
  }
})
  .png()
  .toBuffer();
```

17、[stretchly](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hovancik/stretchly)：Cross-Platform Break Reminder Assistant. This is a cross-platform Electron application designed to help users develop healthy work habits through regular break reminders. It supports multiple languages, including Chinese, and provides personalized settings such as custom break intervals, durations, and reminder sound effects.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/63014033.png' style="max-width:80%; max-height=80%;"></img></p>

18、[svgl](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pheralb/svgl)：Elegant Logo Resource Library. This project is an online Logo library built with SvelteKit and Tailwind CSS, containing over 400 kinds of logos and word trademarks, covering categories such as technology, programming languages, frameworks, and companies, supporting one-click downloads and copy code.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/448688478.png' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
19、[AndroidEasterEggs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hushenghao/AndroidEasterEggs)：A Comprehensive Collection of Android System Easter Eggs. This project gathers various Easter Eggs from Android systems, including complete code and experience features.Shared by [@p0ssword](https://hellogithub.com/en/user/GxAPw47k9KVOyhM)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/306645388.png' style="max-width:80%; max-height=80%;"></img></p>

20、[Maestro](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mobile-dev-inc/Maestro)：Mobile UI Automation Testing Framework. This is an open-source UI automation testing tool for mobile devices and web applications. It uses simple and understandable YAML syntax to write test scripts, has built-in fault tolerance and operation delay tolerance, and supports Android, iOS, Flutter, and desktop browsers.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/476427476.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python
21、[chonkie](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/chonkie-inc/chonkie)：Lightweight Text Chunking Python Library. This is a lightweight text chunking library designed specifically for RAG applications. It is easy to use and fast, capable of splitting text into fixed sizes, supporting various tokenizers, vector models, and flexible chunking strategies, suitable for long text processing and constructing RAG applications.
```python
from chonkie import TokenChunker
from tokenizers import Tokenizer

tokenizer = Tokenizer.from_pretrained("gpt2")
chunker = TokenChunker(tokenizer)

chunks = chunker("HelloGitHub! Chonkie, the chunking library is so cool! I love the tiny hippo hehe.")

for chunk in chunks:
    print(f"Chunk: {chunk.text}")
    print(f"Tokens: {chunk.token_count}")
```

22、[fonttools](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fonttools/fonttools)：Python Library for Manipulating Font Files. This is a Python library for editing and converting font files, supporting the interconversion between TrueType and OpenType fonts and XML format (TTX), compatible with a variety of font formats, suitable for scenarios such as font editing, debugging, and optimization.
```python
from fontTools.afmLib import AFM

f = AFM("Tests/afmLib/data/TestAFM.afm")
print(f["A"])
# (65, 668, (8, -25, 660, 666))

f.FontName = "TestFont HelloGitHub"
f.write("testfont-hellogithub.afm")
```

23、[httpdbg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cle-b/httpdbg)：A Tool for Easily Capturing HTTP(S) Requests in Python Programs. This project is a tool designed to assist developers in debugging HTTP(S) requests within Python programs. By running the program with the pyhttpdbg command, one can view the outgoing HTTP requests in a browser, supporting various operation modes including script execution, interactive console, and unit testing.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/273906263.png' style="max-width:80%; max-height=80%;"></img></p>

24、[pwndbg](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/pwndbg/pwndbg)：GDB/LLDB Plugin Specifically for Reverse Engineering. This is a plugin designed specifically for GDB and LLDB debuggers, supporting features such as register state display, memory search, memory leak detection, and more. It is suitable for scenarios like low-level software development, hardware debugging, and reverse engineering.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/31181767.png' style="max-width:80%; max-height=80%;"></img></p>

25、[PyPSA](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PyPSA/PyPSA)：Power System Analysis Python Library. This is a Python library for power system analysis, focusing on modeling and optimization of electric and multi-energy systems. It is based on libraries such as Pandas, NumPy, GLPK, Cbc, and can efficiently calculate optimal power flow (OPF), linear and non-linear electric power flows, and supports simulation of various electric and energy system components.
```python
import pypsa

# create a new network
n = pypsa.Network()
n.add("Bus", "mybus")
n.add("Load", "myload", bus="mybus", p_set=100)
n.add("Generator", "mygen", bus="mybus", p_nom=100, marginal_cost=20)

# load an example network
n = pypsa.examples.ac_dc_meshed()

# run the optimisation
n.optimize()

# plot results
n.generators_t.p.plot()
n.plot()

# get statistics
n.statistics()
n.statistics.energy_balance()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/49414256.png' style="max-width:80%; max-height=80%;"></img></p>

### Rust
26、[aquascope](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cognitive-engineering-lab/aquascope)：Tool for Visualizing the Execution Process of Rust Code. This is a tool for visualizing Rust code, providing an intuitive demonstration of the details of code compilation and execution, assisting developers in understanding the operation mechanisms of the Rust language.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/537217688.png' style="max-width:80%; max-height=80%;"></img></p>

27、[code2prompt](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mufeedvh/code2prompt)：Toolkit for Converting Codebases to LLM Prompts. This is a Rust-written command-line tool capable of quickly transforming code repositories into prompts suitable for LLM (in Markdown files). It automatically traverses directories, generates a code structure tree, and integrates it into the prompt, while also supporting features like prompt templates, Token calculation, generating Git commit messages, file filtering, etc.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/769564277.png' style="max-width:80%; max-height=80%;"></img></p>

28、[rpg-cli](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/facundoolano/rpg-cli)：Turn Your File System into a Dungeon Game. This is a command-line RPG game written in Rust that simulates facing enemies and initiating turn-based combat (automatic) every time the cd command is executed. The game supports features such as character leveling, items, professions, and treasure chests.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/361019889.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
29、[boring.notch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TheBoredTeam/boring.notch)：Turn MacBook's Notch into a Music Control Center. This is an application designed specifically for macOS that can transform the originally monotonous notch area into a cool music control center, supporting features like calendar, AirDrop, and music controls.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/837073921.gif' style="max-width:80%; max-height=80%;"></img></p>

30、[SwiftUI-Shimmer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/markiv/SwiftUI-Shimmer)：SwiftUI Flash Animation Library. This is a lightweight SwiftUI animation library that can easily add flashing effects to any SwiftUI view. It supports custom animations, gradient styles, flashing speed, and more, suitable for loading states, placeholders, skeleton screens, and other scenarios.
```swift
Text("Custom Gradient Mode").bold()
    .font(.largeTitle)
    .shimmering(
        gradient: Gradient(colors: [.clear, .orange, .white, .green, .clear]),
        bandSize: 0.5,
        mode: .overlay()
    )
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/350812836.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
31、[AI-on-the-edge-device](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jomjol/AI-on-the-edge-device)：Integrating 'Old' Devices into the Digital World. This project utilizes inexpensive hardware like ESP32 (less than 10 euros) and the TensorFlow Lite framework to achieve automatic recognition of meter readings and data transmission, making it easy to retrofit traditional devices (water meters, gas meters, electric meters) into smart devices.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/283280154.jpg' style="max-width:80%; max-height=80%;"></img></p>

32、[instructor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/567-labs/instructor)：Python Library for Structuring LLM Outputs. This project is a Python library designed for handling structured outputs from Large Language Models (LLMs). It leverages Pydantic for data validation and type annotation, enabling the conversion of LLM results (natural language) into structured data. It supports multiple LLM services, as well as features like automatic retries and streaming responses.
```python
import instructor
from pydantic import BaseModel
from openai import OpenAI


# Define your desired output structure
class UserInfo(BaseModel):
    name: str
    age: int


# Patch the OpenAI client
client = instructor.from_openai(OpenAI())

# Extract structured data from natural language
user_info = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=UserInfo,
    messages=[{"role": "user", "content": "John Doe is 30 years old."}],
)

print(user_info.name)
#> John Doe
print(user_info.age)
#> 30
```

33、[lite.ai.toolkit](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/xlite-dev/lite.ai.toolkit)：Lightweight C++ AI Toolkit. This is an AI toolkit written in C++, which includes more than 100 AI models, covering areas such as object detection, facial recognition, segmentation, and background removal. It supports mainstream inference engines like ONNXRuntime, MNN, NCNN, TNN, and TensorRT, helping developers quickly deploy and utilize AI models.Shared by [@wangzijian](https://hellogithub.com/en/user/1NZpMjQFDvCfaEK)
```c++
#include "lite/lite.h"

int main(int argc, char *argv[]) {
  std::string onnx_path = "yolov5s.onnx";
  std::string test_img_path = "test_yolov5.jpg";
  std::string save_img_path = "test_results.jpg";

  auto *yolov5 = new lite::cv::detection::YoloV5(onnx_path); 
  std::vector<lite::types::Boxf> detected_boxes;
  cv::Mat img_bgr = cv::imread(test_img_path);
  yolov5->detect(img_bgr, detected_boxes);
  
  lite::utils::draw_boxes_inplace(img_bgr, detected_boxes);
  cv::imwrite(save_img_path, img_bgr);  
  delete yolov5;
  return 0;
}
```

34、[minimind](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jingyaogong/minimind)：Train a Small Language Model from Scratch. This is not only an implementation of a mini-language model, but also an introductory tutorial for LLMs, aimed at lowering the barrier to learning and getting started with LLMs. It provides the full process code and tutorials from data preprocessing to model training, fine-tuning, and inference. The smallest model has a parameter count of only 0.02B, which can be easily run on a regular GPU.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/834369920.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
35、[flutter_slidable](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/letsar/flutter_slidable)：Flutter's Sliding Action Component. This is an open-source library for Flutter, which can quickly implement sliding operations on list items, supports multi-direction, sliding animations, and auto-closing features.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/141008724.gif' style="max-width:80%; max-height=80%;"></img></p>

36、[inky-dashboard](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jaeheonshim/inky-dashboard)：E-Ink Todo List and Calendar Management Tool. This is a low-power E-Ink todo list and calendar management tool, using Raspberry Pi Pico W and Inky Frame 7.3-inch color E-Ink display for hardware, along with LVGL for interface layout, supporting multiple color displays, to-do lists, calendar synchronization, and more.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/900200373.jpg' style="max-width:80%; max-height=80%;"></img></p>

37、[nginx-proxy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nginx-proxy/nginx-proxy)：Automatic Nginx Reverse Proxy Configuration for Docker Containers. This project provides an automatic Nginx reverse proxy service for Docker containers. It can monitor the start and stop events of Docker containers in real-time, automatically configure Nginx reverse proxy for each Docker container without manual intervention, greatly simplifying the Nginx configuration process in the container environment.
```
# 第一步启动 nginx-proxy
docker run --detach \
    --name nginx-proxy \
    --publish 80:80 \
    --volume /var/run/docker.sock:/tmp/docker.sock:ro \
    nginxproxy/nginx-proxy:1.6

# 第二步启动应用
docker run --detach \
    --name your-proxied-app \
    --env VIRTUAL_HOST=hellogithub.com \
    nginx
```

38、[reference](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Fechin/reference)：Cheat Sheets for Developers. This is a collection of quick reference manuals (cheat sheets) prepared specifically for developers, aiming to provide developers with concise and intuitive quick reference guides, covering a variety of programming languages, frameworks, Linux commands, and databases.Shared by [@databook](https://hellogithub.com/en/user/1qC4w2Ey6bu0fgR)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/322855089.png' style="max-width:80%; max-height=80%;"></img></p>

39、[VoxelSpace](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/s-macke/VoxelSpace)：Terrain Rendering Algorithm in Less Than 20 Lines. This is an algorithm for terrain rendering, with the core code consisting of less than 20 lines. It recreates the rendering technique used in the classic game Comanche (Voxel Space), providing developers with an example for learning and reference.
```python
def Render(p, height, horizon, scale_height, distance, screen_width, screen_height):
    # Draw from back to the front (high z coordinate to low z coordinate)
    for z in range(distance, 1, -1):
        # Find line on map. This calculation corresponds to a field of view of 90°
        pleft  = Point(-z + p.x, -z + p.y)
        pright = Point( z + p.x, -z + p.y)
        # segment the line
        dx = (pright.x - pleft.x) / screen_width
        # Raster line and draw a vertical line for each segment
        for i in range(0, screen_width):
            height_on_screen = (height - heightmap[pleft.x, pleft.y]) / z * scale_height. + horizon
            DrawVerticalLine(i, height_on_screen, screen_height, colormap[pleft.x, pleft.y])
            pleft.x += dx

# Call the render function with the camera parameters:
# position, height, horizon line position,
# scaling factor for the height, the largest distance, 
# screen width and the screen height parameter
Render( Point(0, 0), 50, 120, 120, 300, 800, 600 )
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/104589662.gif' style="max-width:80%; max-height=80%;"></img></p>

40、[zh-style-guide](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yikeke/zh-style-guide)：Chinese Technical Documentation Writing Style Guide. This is an open-source guide for writing Chinese technical documentation, providing reference standards for aspects such as language style, structural style, content elements, punctuation, and formatting of Chinese technical documents.

### Book
41、[Foundations-of-LLMs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ZJU-LLMs/Foundations-of-LLMs)：Fundamentals of Large Models. This book is an open-source textbook on large language models by the DAILY Lab at Zhejiang University. It covers topics including traditional language models, the evolution of large language model architectures, Prompt engineering, efficient fine-tuning of parameters, model editing, and retrieval-augmented generation.Shared by [@无间之钟](https://hellogithub.com/en/user/rnlYFdQcyhRm50p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/822044840.png' style="max-width:80%; max-height=80%;"></img></p>

42、[pytorch-deep-learning](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mrdbourke/pytorch-deep-learning)：Learn PyTorch for Deep Learning: From Zero to Mastery. This project offers a wealth of illustrated tutorials, code examples, video explanations, and practical projects, aimed at helping beginners master the PyTorch framework and deep learning techniques through practical application.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/106/418718534.jpg' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub105.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub107.md">『Next』</a>
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
