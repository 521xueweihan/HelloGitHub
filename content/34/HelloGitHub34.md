# 《HelloGitHub》第 34 期
>兴趣是最好的老师，**HelloGitHub** 就是帮你找到兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 简介
分享 GitHub 上有趣、入门级的开源项目。

这是一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 人群的月刊，月刊的内容包括：**各种编程语言的项目**、**让生活变得更美好的工具**、**书籍、学习笔记、教程等**，这些开源项目大多都是非常容易上手，而且非常 Cool。主要是希望大家能动手用起来，加入到**开源社区**中。
- 会编程的可以贡献代码
- 不会编程的可以反馈使用这些工具中的 Bug
- 帮着宣传你觉得优秀的项目
- Star 项目⭐️

在浏览、参与这些项目的过程中，你将学习到**更多编程知识**、**提高编程技巧**、**找到编程的乐趣**。

🎉 最后 HelloGitHub 这个项目就诞生了 🎉

## 目录
- [C++ 项目](#C-项目)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [PHP 项目](#PHP-项目)
- [Python 项目](#Python-项目)
- [Swift 项目](#Swift-项目)
- [其它](#其它)
- [机器学习](#机器学习)


- [返回首页](https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9)

**Tips**：如果文中的图刷不出来，可以向我们[反馈](https://github.com/521xueweihan/HelloGitHub/issues/899)。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C++ 项目
1、[playerdemo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/itisyang/playerdemo)：开源、入门级视频播放器跨平台视频播放器。该播放器拥有视频播放器基本功能，适合学习播放器开发技术，音频、视频技术

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/playerdemo.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
2、[sqler](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/alash3al/sqler)：根据 SQL 和配置文件生成接口的工具。与传统的 SQL 生成 RESETful API 的工具不同，这个工具允许你自定义一些 API 的前、后处理，Auth 之类的行为。启动命令 `sqler -config=path to config file`，配置示例：
```
adduser {
// 参数校验
    validators {
        user_name_is_empty = "$input.user_name && $input.user_name.trim().length > 0"
        user_email_is_empty = "$input.user_email && $input.user_email.trim(' ').length > 0"
        user_password_is_not_ok = "$input.user_password && $input.user_password.trim(' ').length > 5"
    }

    bind {
        name = "$input.user_name"
        email = "$input.user_email"
        password = "$input.user_password"
    }

    methods = ["POST"]
// 权限校验
    authorizer = <<JS
        (function(){
            log("use this for debugging")
            token = $input.http_authorization
            response = fetch("http://requestbin.fullcontact.com/zxpjigzx", {
                headers: {
                    "Authorization": token
                }
            })
            if ( response.statusCode != 200 ) {
                return false
            }
            return true
        })()
    JS

    exec = <<SQL
        INSERT INTO users(name, email, password, time) VALUES(:name, :email, :password, UNIX_TIMESTAMP());
        SELECT * FROM users WHERE id = LAST_INSERT_ID();
    SQL
}
```

3、[color](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gookit/color)：Golang 的命令行色彩使用库。拥有丰富的色彩渲染输出、通用的 API 方法、兼容 Windows 系统

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/color.png' style="max-width:80%; max-height=80%;"></img></p>

4、[Modlishka](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/drk1wi/Modlishka)：钓鱼网站生成工具。该工具会根据给定的模版生成一个钓鱼网站，然后在该网站输入的用户名密码等敏感信息会被记录

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/Modlishka.jpeg' style="max-width:80%; max-height=80%;"></img></p>

5、[txqr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/divan/txqr)：通过动态二维码传输数据，如：传输文件等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/txqr.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[gitbatch](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/isacikgoz/gitbatch)：批量管理 Git 仓库的命令行工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/gitbatch.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
7、[hutool](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/looly/hutool)：功能丰富的 Java 工具包。它帮助我们实现了常用的工具方法，从而减少代码的体积，提高开发效率。该项目最初是作者工作项目中的`util`模块，后来慢慢积累并加入更多非业务相关工具类方法。经过整理修改，最终形成丰富的开源工具集。示例代码：
```java
int a = 1;
//aStr为"1"
String aStr = Convert.toStr(a);
```

8、[VIABUS-Architecture](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/KunMinX/VIABUS-Architecture)：一款响应式架构。借助总线转发数据的请求和响应，实现 UI、业务的完全解耦

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/android-viabus-architecture.png' style="max-width:80%; max-height=80%;"></img></p>

9、[DevUtils](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/afkT/DevUtils)：Android 工具库，注释规范、API文档清晰明了、工具类种类多。根据不同功能模块封装，方便使用。帮助开发人员，便捷、快速地开发安全、可靠的项目。内置部分常用的资源文件，如 color.xml、layout.xml 等

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
10、[vConsole](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/vConsole)：腾讯开源的移动 H5 的控制台开发调试工具，支持查看 console 日志、网络请求、自定义插件等。示例代码：
```javascript
<script src="path/to/vconsole.min.js"></script>
<script>
  // init vConsole
  var vConsole = new VConsole();
  console.log('Hello world');
</script>

```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/vConsole.png' style="max-width:80%; max-height=80%;"></img></p>

11、[omi](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Tencent/omi)：腾讯开源的通用 Web 组件化框架。特点：
- 拥有官方 UI 组件库
- 使用 omio 可以兼容到 IE8
- 设计精巧、兼容性好
- 基于 Web Components 标准
- 等等

```javascript
import { render, WeElement, define } from 'omi'

define('my-counter', class extends WeElement {
    static observe = true
    
    data = {
      count: 1
    }

    sub = () => {
      this.data.count--
    }

    add = () => {
      this.data.count++
    }

    render() {
      return (
        <div>
          <button onClick={this.sub}>-</button>
          <span>{this.data.count}</span>
          <button onClick={this.add}>+</button>
        </div>
      )
    }
  })

render(<my-counter />, 'body')
```

12、[RSSHub](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/DIYgod/RSSHub)：轻量、易于扩展的 RSS 生成器，可以给任何奇奇怪怪的内容生成 RSS 订阅源。现已支持丰富的源，详情见[文档](https://docs.rsshub.app/)

13、[gridea](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/getgridea/gridea)：静态博客写作客户端，你可以用它来记录你的生活、心情、知识、笔记、创意。使用了 electron 技术，对于学习 Javascript 桌面端开发是一个很好的项目

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/hve-notes.png' style="max-width:80%; max-height=80%;"></img></p>

14、[weapp-library](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/imageslr/weapp-library)：提供在线借书功能的开源小程序项目。连接读者与图书馆，实现图书借阅线上化。界面风格良好，功能完整。具有注册登录、图书搜索、书单系统、订单管理等功能。这是一个完整的小程序项目，包括了前后端的开发，并且撰写了完善的文档，适合初学者学习。可以扫描下面的小程序码体验：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/weapp-library.png' style="max-width:80%; max-height=80%;"></img></p>

15、[axial3d](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/bestvist/axial3d)：实现了类似 GitHub 404 页面的动画效果。效果有趣，使用场景较多，并且实现了组件化，示例代码：
```javascript
<html>
<head>
    <title>Demo - Axial3d</title>
</head>
<body>
    <script src="https://unpkg.com/axial3d"></script>
    <div id="axial3d"></div>
    <script>
        (function () {
            var options = {
                selector: '#axial3d',
                imgs: [
                    {src: 'https://bestvist.github.io/axial3d/public/demo1/bg.png', left: '50px', top: '10px'},
                    {src: 'https://bestvist.github.io/axial3d/public/demo1/2.png', left: '150px', top: '10px'},
                    {src: 'https://bestvist.github.io/axial3d/public/demo1/3.png', left: '50px', top: '300px'},
                    {src: 'https://bestvist.github.io/axial3d/public/demo1/4.png', left: '300px', top: '300px'}
                ]
            }
            var effect = new Axial3d(options);
        })()
    </script>
</body>
</html>
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/axial3d.gif' style="max-width:80%; max-height=80%;"></img></p>

16、[giojs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/syt123450/giojs)：基于 Three.js 的 Web 3D 地球数据可视化的开源组件库。使用 Gio.js 的网页应用开发者，可以快速地以申明的方式创建自定义的 Web3D 数据可视化模型，添加数据，并且将其作为一个组件整合到自己的应用中。支持静态 Dom、React和微信小程序。具有一下特点：
- 易用性 -- 仅使用 4 行 Javascript 即可创建 3D 地球数据可视化模型
- 定制化 -- 使用 Gio.js 提供的丰富的 API 来创建自定义样式的 3D 地球
- 现代化 -- 基于 Gio.js 构建高交互、跨平台、自适应的现代化 3D 前端应用

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/giojs.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
17、[keycastr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/keycastr/keycastr)：在屏幕上实时显示当前按键的工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/keycastr.gif' style="max-width:80%; max-height=80%;"></img></p>

18、[Karabiner-Elements](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pqrs-org/Karabiner-Elements)：一款 macOS 的强大的修键软件

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### PHP 项目
19、[laravel-s](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hhxsv5/laravel-s)：用于快速集成 [Swoole](https://www.swoole.com/) 到 [Laravel](https://laravel.com/)，开箱即用。特点：
- 集成 LaravelS 之后无需使用 PHP FPM，直接基于 Swoole 开启 HTTP Server
- 代码常驻内存之中，性能提升非常明显
- 可快速开发 WebSocket/TCP/UDP 服务
- 支持异步任务队列、自定义进程、定时任务，支持更多的业务场景
- 可直接使用 Swoole 的很多特性
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/laravel-s.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
20、[sherlock](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sherlock-project/sherlock)：（英文）在主流社交网站，例如：GitHub、Facebook 等网站上查找指定的用户名是否存在。你想取一个独一无二的名字吗？快试试吧

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/sherlock.png' style="max-width:80%; max-height=80%;"></img></p>

21、[click](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/pallets/click)：Python 的第三方库，用于快速创建命令行。支持装饰器方式调用、多种参数类型、自动生成帮助信息等。示例代码如下：
```python
import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)

if __name__ == '__main__':
    hello()

# 下面为运行效果
$ python hello.py --count=3
Your name: Click
Hello, Click!
Hello, Click!
Hello, Click!
```

22、[PSpider](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/xianhu/PSpider)：代码量极少，功能却很完备的 Python 爬虫框架。特点：
- 功能完备：包含抓取、解析、存储等
- 代码量少：方便阅读源码、动手修改、二次开发
- 等等

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/PSpider.png' style="max-width:80%; max-height=80%;"></img></p>

23、[awesome-python-applications](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mahmoud/awesome-python-applications)：（英文）介绍 Python 有趣、神奇的开源项目。目前涵盖多个领域、项目丰富

24、[ranger](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ranger/ranger)：以类似 VIM 操作，方便、快捷地管理文件的工具

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Swift 项目
25、[iOS-Developer-Roadmap](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/BohdanOrlov/iOS-Developer-Roadmap)：（英文） iOS 开发者学习路线图

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
26、[Visual-Studio-Code-Keymap-CN](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/OrwillT/Visual-Studio-Code-Keymap-CN)：VS Code 编辑器官方快捷键查图汉化版

27、[algorithm-visualizer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/algorithm-visualizer/algorithm-visualizer)：算法可视化工具。你可以自由选择自己想学习的算法，每个算法它都清晰描绘了其原理和运作过程

28、[html](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/whatwg/html)：《HTML 标准》[中文版](https://whatwg-cn.github.io/html/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
29、[spinningup](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/openai/spinningup)：（英文）OpenAI 制作的教育资源，可以更容易地学习深层强化学习。官方项目，浅显易懂，提供练手的例子，方便初学者或对深层强化学习感兴趣的人群学习和入门

30、[the-gan-zoo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hindupuravinash/the-gan-zoo)：生成对抗网络（Generative Adversarial Networks，简称GAN）的一个大集合，作者列举了生成对抗网络领域各式各样的应用集合，大部分为论文，包含少数的 GitHub 项目。该项目对于 GAN 领域覆盖面全面，论文列表整理清晰，GAN 方向的研究者可以从这个项目中查询到想看的经典的论文或者扩充自己的知识储备

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/the-gan-zoo.png' style="max-width:80%; max-height=80%;"></img></p>

31、[transformers](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/huggingface/transformers)：Google 神级语言表示模型的 PyTorch 预训练模型和 PyTorch 框架结合，使得更加容易上手。PyTorch 版本更方便小白上手实验。示例代码：
```python
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenized input
text = "Who was Jim Henson ? Jim Henson was a puppeteer"
tokenized_text = tokenizer.tokenize(text)

# Mask a token that we will try to predict back with `BertForMaskedLM`
masked_index = 6
tokenized_text[masked_index] = '[MASK]'
assert tokenized_text == ['who', 'was', 'jim', 'henson', '?', 'jim', '[MASK]', 'was', 'a', 'puppet', '##eer']

# Convert token to vocabulary indices
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
# Define sentence A and B indices associated to 1st and 2nd sentences (see paper)
segments_ids = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Convert inputs to PyTorch tensors
tokens_tensor = torch.tensor([indexed_tokens])
segments_tensors = torch.tensor([segments_ids])
```

32、[RecommenderSystem-Paper](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/daicoolb/RecommenderSystem-Paper)：推荐系统论文整理列表，包括了行业顶尖会议 AAAI、NIPS 等发表的论文，以及 KDD 一些获奖论文。方便推荐系统方向以及文本表示方向等研究人员，跟踪阅读行业内经典论文和最新研究方向

33、[Semantic-Segmentation-Suite](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/GeorgeSeif/Semantic-Segmentation-Suite)：图像语义分割模型组件整理，包含了模型、数据增广、准确率评价等模块。方便研究者快速搭建和试验一个图像语义分割模型，同时集成了一些 state-of-the-art 的模型

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/34/img/Semantic-Segmentation-Suite.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/33/HelloGitHub33.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/35/HelloGitHub35.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://afdian.net/@HelloGitHub'>点击赞助</a> ｜ <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击推荐项目</a> 👈<br>
    关注公众号：<strong>HelloGitHub</strong><br>
    "第一时间收到推送及更多内容"<br>

</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
