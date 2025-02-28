# HelloGitHub Vol.103
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
1、[rawdrawandroid](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cnlohr/rawdrawandroid)：Develop Android Apps with Only C Language. This is an Android application development framework that allows developers to develop Android apps using only C and Make without Java. It is lightweight and cross-platform, supporting OpenGL ES, gyroscope, multi-touch, and Android keyboard, and can directly access USB devices.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/212012440.png' style="max-width:80%; max-height=80%;"></img></p>

2、[taisei](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/taisei-project/taisei)：Free and Open Source Touhou Project Series Shooter Game. This project is a bullet-hell shoot 'em up game based on the Touhou Project universe, featuring an original independent storyline, music, and game mechanics. Named 'Taixi', the game is developed using C11, SDL2, and OpenGL, and is completely free and open source, supporting operation on Windows, Linux, macOS, and Chrome browsers.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/977986.gif' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[Bulk-Crap-Uninstaller](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Klocman/Bulk-Crap-Uninstaller)：Free Windows App Uninstaller. This is a Windows software uninstallation tool developed with C# that can quickly delete a large number of unwanted applications. It is completely free, ready to use out of the box, and supports batch and forced uninstallation, cleanup residual files, and detection of hidden or protected registered applications. Although designed for IT professionals, its simple default settings make it easy for anyone to get started.Shared by [@猎隼丶止戈reNo7](https://hellogithub.com/en/user/Ew59HqRWjPe0zZO)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/64677873.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Macro-Deck](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Macro-Deck-App/Macro-Deck)：Tool to Turn Phones into a Stream Deck. This project turns phones, tablets, and other devices with a browser into a remote customizable keypad similar to Stream Deck, enabling one-touch execution of single or multi-step operations, suitable for live streaming and simplifying daily tasks.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/166713531.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
5、[aria2](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/aria2/aria2)：Super Fast Command-Line Download Tool. This cross-platform command-line download tool is developed in C++ and supports various protocols such as HTTP(S), FTP, SFTP, and BitTorrent. It features easy operation, small size, fast download speeds, and offers functionality like running in the background, speed limiting, segmented downloading, and BitTorrent extensions.Shared by [@刘睿华](https://hellogithub.com/en/user/TJ65FfbQU09PLHM)

6、[fast_float](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fastfloat/fast_float)：A C++ Numeric Parsing Library That Is Both Fast and Accurate. This project is a C++ library for quickly parsing numeric strings, implementing functionality similar to a from_chars function. It is an extremely fast, header-only library that is several times faster than the standard library. It supports parsing strings of float, double, and integer types and has been widely used in well-known projects such as Chromium, Redis, and LLVM.
```c++
#include "fast_float/fast_float.h"
#include <iostream>

int main() {
    const std::string input =  "3.1416 xyz ";
    double result;
    auto answer = fast_float::from_chars(input.data(), input.data()+input.size(), result);
    if(answer.ec != std::errc()) { std::cerr << "parsing failure\n"; return EXIT_FAILURE; }
    std::cout << "parsed the number " << result << std::endl;
    return EXIT_SUCCESS;
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/305438763.png' style="max-width:80%; max-height=80%;"></img></p>

7、[mame](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mamedev/mame)：Open Source Arcade Emulator. This is an emulator that supports a vast array of arcade games. By simulating various hardware platforms, it achieves the capability to run various retro software on computers. It not only supports arcade games but also old computers and gaming consoles.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/14303048.png' style="max-width:80%; max-height=80%;"></img></p>

### Go
8、[beszel](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/henrygd/beszel)：Lightweight and Stylish Docker Monitoring Platform. This is a lightweight server monitoring platform that includes Docker statistics, historical data, and alerting functionalities. It features a user-friendly web interface, simple configuration, out-of-the-box usability, and supports automatic backup, multi-user, OAuth authentication, and API access.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/825470378.png' style="max-width:80%; max-height=80%;"></img></p>

9、[envd](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tensorchord/envd)：Efficient AI Development Environment Setup Tool. This command-line tool provides reproducible development environments for AI/ML projects. With simple configuration languages and commands, you can quickly create container-based development environments, supporting remote building, dependency caching, and importing remote repositories.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/480303698.png' style="max-width:80%; max-height=80%;"></img></p>

10、[gophish](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/gophish/gophish)：Open Source Phishing Platform. This project offers a ready-to-use phishing platform for simulating phishing attacks. It features a user-friendly web management backend, supports email templates, bulk email sending, website cloning, and data visualization, suitable for scenarios such as enterprise security training and penetration testing.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/14508450.png' style="max-width:80%; max-height=80%;"></img></p>

11、[opentofu](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/opentofu/opentofu)：Open Source Solution for Infrastructure as Code. This project is an open source Infrastructure as Code tool that focuses on the automated creation, management, and deployment of local and cloud service infrastructures. As a spin-off of Terraform, it is community-driven and supports describing infrastructure using advanced configuration syntax, generating execution plans, and building resource dependency diagrams, thereby reducing human operation errors and automating complex changes.Shared by [@刘睿华](https://hellogithub.com/en/user/TJ65FfbQU09PLHM)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/679421146.png' style="max-width:80%; max-height=80%;"></img></p>

12、[photoview](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/photoview/photoview)：Minimalist Photo Management Platform. This is a Web application designed for self-hosted cloud photo albums. It features an intuitive user interface and a wealth of capabilities, such as automatic photo organization, thumbnail generation, shared albums, EXIF data parsing, and multi-user management. An iOS app is also provided for convenient access on mobile devices.Shared by [@刘睿华](https://hellogithub.com/en/user/TJ65FfbQU09PLHM)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/195657294.png' style="max-width:80%; max-height=80%;"></img></p>

### Java
13、[GoGoGo](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ZCShou/GoGoGo)：Open Source Android Virtual Location App. This project is a virtual positioning tool based on Android debugging APIs and Baidu Maps, capable of modifying geographic locations without ROOT permissions. It supports location search and manual input of coordinates, and provides a freely movable joystick to simulate movement.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/434497397.jpg' style="max-width:80%; max-height=80%;"></img></p>

14、[karate](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/karatelabs/karate)：Open Source API Automated Testing Framework. This is an API testing framework based on Java, which can seamlessly integrate with Java ecosystems like Spring Boot and Maven. It integrates API test automation, simulation, performance testing, and UI automation, supports writing test cases with a syntax similar to Cucumber, and provides a cross-platform executable file that can be easily used even without familiarity with Java.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/81226206.jpg' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
15、[icones](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/antfu-collective/icones)：Minimal Icon Search Website. This is a website for quickly searching various icons, supporting category filtering and multi-selection mode. Users can package the selected icons as fonts or directly download them in SVG format.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/278862095.png' style="max-width:80%; max-height=80%;"></img></p>

16、[media-chrome](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/muxinc/media-chrome)：A Component Library for Crafting Modern Web Player Interfaces. This library is designed for customizing web audio and video player interfaces compatible with various JavaScript frameworks. It is highly customizable, allowing developers to easily adjust the appearance and functionality of components, supporting features such as subtitles, screen casting, shortcut keys, playback speed, preview thumbnails, mobile compatibility, and a mute button.
```html
<media-controller audio>
  <audio
    slot="media"
    src="xxxxxx"
  ></audio>
  <media-control-bar>
    <media-play-button></media-play-button>
    <media-time-display showduration></media-time-display>
    <media-time-range></media-time-range>
    <media-playback-rate-button></media-playback-rate-button>
    <media-mute-button></media-mute-button>
    <media-volume-range></media-volume-range>
  </media-control-bar>
</media-controller>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/208394975.jpg' style="max-width:80%; max-height=80%;"></img></p>

17、[Moe-Counter](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/journey-ad/Moe-Counter)：Adorable Website Counter. This project is a visitor counter designed for tracking the number of visits to a webpage. It is not only simple and easy to use but also offers a variety of cute and stylish themes for users to choose from according to their personal preferences.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/284698414.png' style="max-width:80%; max-height=80%;"></img></p>

18、[piscina](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/piscinajs/piscina)：Flexible and efficient Node.js thread pool. This project is a high-performance Node Worker thread pool written in TypeScript, aimed at simplifying multi-threaded programming in Node.js. It provides a simple and easy-to-use API, supporting inter-thread communication, dynamic adjustment of thread pool size, task cancellation, setting memory limits, and asynchronous task tracking.
```javascript
const path = require('path');
const Piscina = require('piscina');

const piscina = new Piscina({
  filename: path.resolve(__dirname, 'worker.js')
});

(async function() {
  const result = await piscina.run({ a: 4, b: 6 });
  console.log(result);  // Prints 10
})();
```

19、[swapy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/TahaSh/swapy)：A Library to Easily Implement Draggable Layouts. This project allows any layout to be converted into a draggable and swappable form with just a few lines of code. It supports the configuration of interactive animations and can be used in frameworks such as React, Vue, Svelte, applicable to various scenarios requiring interactive layouts.
```typescript
import { createSwapy } from 'swapy'

const container = document.querySelector('.container')

const swapy = createSwapy(container, {
  animation: 'dynamic' // or spring or none
})

// You can disable and enable it anytime you want
swapy.enable(true)
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/829042475.gif' style="max-width:80%; max-height=80%;"></img></p>

### Kotlin
20、[etchdroid](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/etchdroid/etchdroid)：A tool for creating bootable USB drives on mobile phones. This is an open-source Android application designed specifically for creating bootable USB drives for operating systems directly on your phone. It does not require ROOT permissions to write operating system images to USB devices, supporting multiple systems like Ubuntu and Raspberry Pi. It is suitable for creating bootable USB drives when you cannot use a computer.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/147043230.png' style="max-width:80%; max-height=80%;"></img></p>

21、[KeyMapper](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/keymapperorg/KeyMapper)：Android Key Remapping App. This is a free and open-source Android application that allows users to customize keys, fingerprints, and gestures on Android devices. It works without the need for ROOT permissions and supports both Bluetooth and wired keyboards, providing a flexible key remapping experience.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/141129812.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
22、[backtrader](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mementum/backtrader)：Python Quantitative Trading Backtest Framework. This project is a backtesting library written in Python, designed specifically for the development and testing of trading strategies. It can extract data from CSV files, online data sources, and pandas, supporting the synchronous operation of multiple strategies, and generating visualizations for trading strategies. It includes over 100 indicators, including trend, volume, and volatility indicators.
```python
from datetime import datetime
import backtrader as bt

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

data0 = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime(2011, 1, 1),
                                  todate=datetime(2012, 12, 31))
cerebro.adddata(data0)

cerebro.run()
cerebro.plot()
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/29050338.png' style="max-width:80%; max-height=80%;"></img></p>

23、[core](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/home-assistant/core)：Open-source Smart Home Platform. This is an open-source smart home platform written in Python, which aims to integrate various smart devices from different brands to provide a personalized home automation experience. It addresses the poor interoperability problems of traditional systems, allowing users to freely control and link devices like Apple HomeKit, Mi Home, Aqara, TuYa, and more on the same platform, greatly enhancing the flexibility and convenience of smart homes. It is suitable for users who want to break the single-platform limitations, especially DIY smart home enthusiasts who pursue high cost-performance.Shared by [@无间之钟](https://hellogithub.com/en/user/rnlYFdQcyhRm50p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/12888993.png' style="max-width:80%; max-height=80%;"></img></p>

24、[paperless-ngx](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/paperless-ngx/paperless-ngx)：Paper Document Digitalization Archive Tool. This is a document management system based on Django that can convert paper documents into searchable online archives. Unlike ordinary scanners that turn physical books into images or PDF formats that are difficult to retrieve, it achieves digitization through document scanners and is transformed into a format that is easy to search.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/458648791.png' style="max-width:80%; max-height=80%;"></img></p>

25、[pipreqs](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/bndr/pipreqs)：A Tool for Rapidly Generating Python Project Dependency Files. This project can generate a requirements.txt file based on the import statements within a Python project. It is capable of automatically identifying libraries used in the project and generating a list of dependencies without needing any installation.

26、[pokeapi](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PokeAPI/pokeapi)：Pokémon Data API Service. This is a Pokémon data RESTful API service built based on Django, providing developers with a comprehensive Pokémon database, including detailed information such as the actions, attributes, skills, and evolution of the little creatures.

### Rust
27、[insta](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mitsuhiko/insta)：A Snapshot Testing Library for Rust. This is a snapshot testing library for Rust projects, particularly suitable for scenarios where reference values are very large or change frequently. It provides VSCode plugins and command-line tools. When a test fails due to changes in reference values, you can review the issue with the review command and update the snapshot (reference values) with one click, making it easy to pass unit tests quickly.
```rust
fn split_words(s: &str) -> Vec<&str> {
    s.split_whitespace().collect()
}

#[test]
fn test_split_words() {
    let words = split_words("hello from the other side");
    insta::assert_yaml_snapshot!(words);
}
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/165561258.gif' style="max-width:80%; max-height=80%;"></img></p>

28、[oha](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hatoo/oha)：HTTP Stress Testing Tool Powered by Rust. This is an HTTP stress testing tool developed in Rust. It's easy to operate, comes with a TUI animation interface, supports generating reports for metrics such as request delays and throughput, and offers capabilities like dynamic URLs and more flexible request intervals (burst-delay).

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/244377430.gif' style="max-width:80%; max-height=80%;"></img></p>

29、[steel](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/mattwparas/steel)：Rust-based Embedded Scheme Interpreter. This is an embedded Scheme interpreter written in Rust, aimed at providing lightweight and fast scripting language support. It addresses the need for a highly efficient, flexible script engine in embedded environments or small applications.Shared by [@无间之钟](https://hellogithub.com/en/user/rnlYFdQcyhRm50p)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/241949362.gif' style="max-width:80%; max-height=80%;"></img></p>

### Swift
30、[aural-player](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kartik-venugopal/aural-player)：macOS Music Player Inspired by Winamp. This project is a music player for macOS inspired by the classic Winamp player, developed in Swift programming language. It features built-in sound effects and equalizers, supports a variety of audio formats, playback, lyric display, customizable interfaces, and more.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/96710143.gif' style="max-width:80%; max-height=80%;"></img></p>

31、[DockDoor](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ejbills/DockDoor)：Window Preview Tool for macOS. This project is a Dock window preview tool developed with Swift and SwiftUI. By simply hovering the mouse cursor over an application icon in the Dock, one can preview the open windows and it also supports Alt+Tab-like switching and custom shortcuts functionalities, similar to Windows.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/809906907.gif' style="max-width:80%; max-height=80%;"></img></p>

### AI
32、[moondream](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/vikhyat/moondream)：Compact Vision-Language Model. This is a compact vision-language model designed to operate on resource-constrained devices. It can understand and generate natural language descriptions related to images, supporting image recognition, description generation, and question-answering features.
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

image = Image.open('<IMAGE_PATH>')
enc_image = model.encode_image(image)
print(model.answer_question(enc_image, "Describe this image.", tokenizer))
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/736812439.png' style="max-width:80%; max-height=80%;"></img></p>

33、[Prompt_Engineering](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NirDiamant/Prompt_Engineering)：Comprehensive Prompt Engineering Guide for Practical Applications. This tutorial is dedicated to helping users master the skills of communicating with Large Language Models (LLM). It covers prompt engineering techniques from basic to advanced levels, with detailed implementation guides and sample code.

34、[spaCy](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/explosion/spaCy)：Powerful Natural Language Processing Python Library. This is an industrial-grade Natural Language Processing (NLP) library that supports tokenization and training in more than 70 languages. Written in Python, it enables functions such as annotation, parsing, and text classification, and supports model packaging and deployment.
```python
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
```

35、[ultralytics](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ultralytics/ultralytics)：Advanced Object Detection and Tracking Model. This project is based on previous YOLO versions, with added features and improvements to the model, showing excellent performance in tasks such as object detection, tracking, instance segmentation, and image classification.
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data="coco8.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("path/to/image.jpg")
results[0].show()

# Export the model to ONNX format
path = model.export(format="onnx")  # return path to exported model
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/535360445.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
36、[BilibiliSponsorBlock](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/hanydd/BilibiliSponsorBlock)：Bilibili Video Skipping Assistant. This is a browser extension that can automatically skip sponsorship clips and opening and ending animations in Bilibili videos. All marked data is contributed by netizens and supports Chrome, Edge, and FireFox browsers.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/744617272.png' style="max-width:80%; max-height=80%;"></img></p>

37、[cognitive-load](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zakirullin/cognitive-load)：Suggestions to Reduce Cognitive Load for Developers. This is an article about how to reduce cognitive load in the software development process. That is, to simplify the code and improve its readability, to alleviate the burden on developers when reading and understanding the code.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/642858415.png' style="max-width:80%; max-height=80%;"></img></p>

38、[dockerc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/NilsIrl/dockerc)：Tool to Compile Docker Image into a Standalone Executable File. This project can transform a Docker image into a binary executable file, eliminating the need to configure a Docker environment or install dependencies, which simplifies the process of software distribution and execution.Shared by [@kero990](https://hellogithub.com/en/user/c3Y4NR1rq6neVoD)

39、[kubernetes-goat](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/madhuakula/kubernetes-goat)：Kubernetes Security Attack and Defense Drill Platform. This project is for constructing a vulnerable and easily attackable cluster environment, allowing developers to learn K8s attack and defense techniques in a real-world scenario.

40、[pilipala](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/guozhigq/pilipala)：Open-source Bilibili Third-party Client. This project is a third-party Bilibili client developed using Flutter and supports both Android and iOS platforms. It provides features such as a list of recommended videos, popular live broadcasts, anime series, offline caching, replying to comments, bullet chats, and search functionality.Shared by [@Micro·J](https://hellogithub.com/en/user/L2Xx0OfvPzpYt4u)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/629282922.png' style="max-width:80%; max-height=80%;"></img></p>

41、[Sensor-Watch](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/joeycastillo/Sensor-Watch)：Open-Source PCB for Casio F-91W Watch. This project is a homemade circuit board for the classic Casio F-91W watch, using an ARM Cortex-M0+ microcontroller (SAM L22). Equipped with a ten-digit segment LCD display, five indicator segments, LED backlighting, and three buttons, it supports USB programming and allows users to run custom programs on the watch.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/356689400.jpg' style="max-width:80%; max-height=80%;"></img></p>

42、[themostdangerouswritingapp](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/maebert/themostdangerouswritingapp)：Tool to Push Writing Efficiency to the Extremes. This is a web application designed to help users enter a writing 'flow' state. If you stop typing for more than 5 seconds, the text on the screen will gradually become blurry and eventually disappear completely.Shared by [@孤胆枪手](https://hellogithub.com/en/user/i1wAIyo6P3NXkxm)

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/52758523.gif' style="max-width:80%; max-height=80%;"></img></p>

### Book
43、[udlbook](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/udlbook/udlbook)：Understanding Deep Learning. This book, written by Simon J.D. Prince, is a professional book about deep learning, covering topics such as the theoretical foundations of deep learning, performance evaluation, convolutional networks, Transformers, graph neural networks, Generative Adversarial Networks (GANs), diffusion models, and reinforcement learning, accompanied by a multitude of exercises.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img4/master/hellogithub/103/520128820.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub102.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub104.md">『Next』</a>
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
