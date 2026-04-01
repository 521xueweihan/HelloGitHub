# HelloGitHub Vol.60
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
1、[rtty](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zhaojh329/rtty)：能够通过 Web 登录 Linux 终端的开源项目。采用 C 语言实现，算上依赖库体积不到 100KB，可用于嵌入式 Linux 设备。拥有 Web 管理界面，用此项目可以方便地远程维护 Linux 设备


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/92715023.gif' style="max-width:80%; max-height=80%;"></img></p>

2、[si78c](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/loadzero/si78c)：用 C 语言实现的《太空侵略者》命令行游戏


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/225607507.gif' style="max-width:80%; max-height=80%;"></img></p>

### C#
3、[nopCommerce](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nopSolutions/nopCommerce)：免费开源的 ASP.NET 电子商城平台。该项目始于 2008 年，由专业团队开发和维护，大而全的商城项目。支持 Windows、Linux、macOS 平台，还有支持开箱即用的 Docker 部署方式


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/18586705.png' style="max-width:80%; max-height=80%;"></img></p>

4、[osu](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ppy/osu)：支持多平台的同人节奏免费开源游戏。游戏中玩家随着音乐的节奏，点击界面上圈圈、随着轨迹拖拽和旋转。从最初（07 年）仅支持 Windows 平台，到目前已经扩展到支持 Linux、macOS、iOS、Android 等平台，并且还在持续维护和开发，我试玩了下感觉很有意思，快[下载](https://github.com/ppy/osu/releases)下来玩玩吧！


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/22456440.gif' style="max-width:80%; max-height=80%;"></img></p>

### C++
5、[jwEngine](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jwcpp/jwEngine)：一个跨平台、轻量级、支持 C++ 和 Lua 的 Web 框架。支持 TCP、KCP、WebSocket、HTTP 等协议，底层采用 libuv 异步 IO 提高并发，避免多线程上下文切换开销和破坏代码美感，网络部分和逻辑部分使用一个主事件循环驱动。支持 Lua 提高开发效率，适用于小型游戏开发，示例代码：
```lua
event_init()

server = NetServer:new()
server.on_accept = function(conn)
end

server.on_close = function(conn)
end

server.on_msg = function(conn, msgtype, pack)
end

server:listen("127.0.0.1", 3001, false)

event_run()
```


6、[Serial-Studio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Serial-Studio/Serial-Studio)：一款 C++ 写的数据可视化桌面工具。支持多平台，效果和操作步骤如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/305089628.gif' style="max-width:80%; max-height=80%;"></img></p>

### Go
7、[act](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nektos/act)：该项目可以让你在本地调试 GitHub Actions 脚本。GitHub Actions 是 GitHub 提供的仓库自动工作流程功能，用户可以利用 GitHub 提供的免费计算机资源轻松实现 CI/CD，还可以用来做很多有意思的事情。但是在编写 actions 脚本时，想调试脚本或得到运行结果，只能 push 到远程仓库等待运行结束，没有办法在本地调试和查看结果。有了 act 这个项目，就可以在本地轻松调试 actions 啦，是不是很棒


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/163883279.gif' style="max-width:80%; max-height=80%;"></img></p>

8、[dns](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/miekg/dns)：简单易用高性能的 Go DNS 库。示例代码：
```go
package main

import (
    "github.com/miekg/dns"
    "net"
    "os"
    "log"
    "fmt"
)

func main() {
    config, _ := dns.ClientConfigFromFile("/etc/resolv.conf")
    c := new(dns.Client)

    m := new(dns.Msg)
    m.SetQuestion(dns.Fqdn(os.Args[1]), dns.TypeMX)
    m.RecursionDesired = true

    r, _, err := c.Exchange(m, net.JoinHostPort(config.Servers[0], config.Port))
    if r == nil {
        log.Fatalf("*** error: %s\n", err.Error())
    }

    if r.Rcode != dns.RcodeSuccess {
            log.Fatalf(" *** invalid answer name %s after MX query for %s\n", os.Args[1], os.Args[1])
    }
    // Stuff must be in the answer section
    for _, a := range r.Answer {
            fmt.Printf("%v\n", a)
    }
}
```


9、[pretty](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/kr/pretty)：漂亮的 Go Printf 开源三方库。示例代码：
```go
package main

import (
	"fmt"

	"github.com/kr/pretty"
)

func main() {
	type myType struct {
		a, b int
	}
	var x = []myType{{1, 2}, {3, 4}, {5, 6}}
	fmt.Printf("%# v", pretty.Formatter(x))
}

Output:
[]pretty_test.myType{
    {a:1, b:2},
    {a:3, b:4},
    {a:5, b:6},
}
```


### Java
10、[QNotified](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ferredoxin/QNotified)：让运行在安卓系统上的 QQ 变得更好用的开源 Xposed 模块。Xposed 是一个运行于 Android 操作系统的 Hook 框架，可以理解为安卓操作系统的外挂！安装本工具后，可在 QQ 自带的设置中点击 QNotified 即可开启“超级”模式。支持：
- 防撤回
- 被删除好友通知
- 屏蔽 @全体成员 或者 群红包 的通知
- 批量撤回消息
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/177373545.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
11、[ChatUI](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alibaba/ChatUI)：专注于对话领域的 UI 开源项目。可以帮助用户快速搭建体验友好的机器人对话界面，特性：
- 最佳实践：基于阿里小蜜业务积累和打磨的对话式交互最佳实践
- TypeScript：使用 TypeScript 开发，提供完整的类型定义文件
- 响应式：响应式布局，在无线和 PC 端都可以友好展现
- 主题：支持灵活的样式定制，以满足业务和品牌上多样化的视觉需求
- 国际化：支持多语言和本土化特性
```javascript
import Chat, { Bubble, useMessages } from '@chatui/core';
import '@chatui/core/dist/index.css';

const App = () => {
  const { messages, appendMsg, setTyping } = useMessages([]);

  function handleSend(type, val) {
    if (type === 'text' && val.trim()) {
      appendMsg({
        type: 'text',
        content: { text: val },
        position: 'right',
      });

      setTyping(true);

      setTimeout(() => {
        appendMsg({
          type: 'text',
          content: { text: 'Bala bala' },
        });
      }, 1000);
    }
  }

  function renderMessageContent(msg) {
    const { content } = msg;
    return <Bubble content={content.text} ></Bubble>;
  }

  return (
    <Chat
      navbar={{ title: '智能助理' }}
      messages={messages}
      renderMessageContent={renderMessageContent}
      onSend={handleSend}
    ></Chat>
  );
};
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/284864176.jpeg' style="max-width:80%; max-height=80%;"></img></p>

12、[cool-admin-midway](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cool-team-official/cool-admin-midway)：一款基于 Node.js+midway.js 的后台权限管理系统。它开源免费不仅能够快速开发增删改查的需求，还支持 Serverless、Docker 等多种方便的部署方式，不管是用来学习如何开发管理后台，还是快速开发都是不错的选择


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/342884320.jpg' style="max-width:80%; max-height=80%;"></img></p>

13、[edex-ui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GitSquared/edex-ui)：一款跨平台基于 Electron 的炫酷终端工具。好莱坞级别的终端使用体验，拥有漂亮的启动动画、浮夸的音效，还能够直观地展示文件目录、系统资源、网络等信息


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/80276391.png' style="max-width:80%; max-height=80%;"></img></p>

14、[joplin](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/laurent22/joplin)：Markdown 友好的开源笔记软件。这是一款免费的开源笔记软件，能够方便地管理待办事项和处理大量笔记。可以直接导入印象笔记（Evernote）的笔记和 Markdown 文件，提供了 Windows、macOS、Linux、Android 和 iOS 等主流操作系统客户端。它不仅支持离线使用，同时也支持自定义网盘同步笔记，从而实现多端无缝创作。


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/79162682.png' style="max-width:80%; max-height=80%;"></img></p>

15、[MarioHTML](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/nbarkhina/MarioHTML)：用 TypeScript 写的马里奥网页游戏。[在线试玩](https://www.neilb.net/MarioHTML/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/203693850.png' style="max-width:80%; max-height=80%;"></img></p>

16、[semaphore](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/semaphoreui/semaphore)：好看的 Ansible UI 项目。受够了 Ansible 老气的界面了吗？那就试试这个项目吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/23267883.png' style="max-width:80%; max-height=80%;"></img></p>

### PHP
17、[dompdf](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/dompdf/dompdf)：一个 HTML 转 PDF 的 PHP 库。示例代码：
```php
// reference the Dompdf namespace
use Dompdf\Dompdf;

// instantiate and use the dompdf class
$dompdf = new Dompdf();
$dompdf->loadHtml('hello world');

// (Optional) Setup the paper size and orientation
$dompdf->setPaper('A4', 'landscape');

// Render the HTML as PDF
$dompdf->render();

// Output the generated PDF to Browser
$dompdf->stream();
```


18、[PHPMailer](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PHPMailer/PHPMailer)：应该是最流行的 PHP 发邮件的开源库。很多知名 PHP 开源项目中都有它的身影，比如：WordPress、Yii 等，支持你对发邮件的所有开发需求。看看示例代码，就知道使用起来有多简单啦：
```php
<?php
//Import PHPMailer classes into the global namespace
//These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

//Load Composer's autoloader
require 'vendor/autoload.php';

//Instantiation and passing `true` enables exceptions
$mail = new PHPMailer(true);

try {
    //Server settings
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      //Enable verbose debug output
    $mail->isSMTP();                                            //Send using SMTP
    $mail->Host       = 'smtp.example.com';                     //Set the SMTP server to send through
    $mail->SMTPAuth   = true;                                   //Enable SMTP authentication
    $mail->Username   = 'user@example.com';                     //SMTP username
    $mail->Password   = 'secret';                               //SMTP password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;         //Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` encouraged
    $mail->Port       = 587;                                    //TCP port to connect to, use 465 for `PHPMailer::ENCRYPTION_SMTPS` above

    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('joe@example.net', 'Joe User');     //Add a recipient
    $mail->addAddress('ellen@example.com');               //Name is optional
    $mail->addReplyTo('info@example.com', 'Information');
    $mail->addCC('cc@example.com');
    $mail->addBCC('bcc@example.com');

    //Attachments
    $mail->addAttachment('/var/tmp/file.tar.gz');         //Add attachments
    $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    //Optional name

    //Content
    $mail->isHTML(true);                                  //Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
    $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
```


19、[video_spider](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/5ime/video_spider)：视频去水印工具。原理很简单就是根据输入的视频的地址，返回原平台无水印的视频源地址。目前支持 15 个视频平台，[在线尝试](https://lab.5ime.cn/video/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/281640234.png' style="max-width:80%; max-height=80%;"></img></p>

### Python
20、[Airtest](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/AirtestProject/Airtest)：适用于移动端应用的跨平台 UI 自动化框架。基于图像识别定位元素，可能都不需要一行代码就可以很方便地用它来测试 APP 或刷游戏


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/118709540.gif' style="max-width:80%; max-height=80%;"></img></p>

21、[ArchiveBox](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ArchiveBox/ArchiveBox)：Self-hosted Web Archiving Platform. This is a Python-based web archiving tool designed to help users save and archive internet content. It is free, open-source, and self-hosted, supporting the downloading of web pages from URLs, browser bookmarks, RSS feeds, open-source projects, and social media, generating local snapshots for offline reading and archiving, and offering various archiving formats including HTML, PDF, images, and text. The well-known Internet Archive (Wayback Machine) is built on this project.

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/90356372.png' style="max-width:80%; max-height=80%;"></img></p>

22、[lux](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lux-org/lux)：一个用于数据科学方面的 Python 开源库。这个库适用于实验室分析数据的场景，基于 Jupyter 的数据可视化和操作界面，再加上 pandas 丰富的数据接入方式以及强大的数据处理能力，让数据的分析变得简单从而可以更加直观地找到数据背后藏着的“真理”


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/232480726.gif' style="max-width:80%; max-height=80%;"></img></p>

23、[qutebrowser](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/qutebrowser/qutebrowser)：基于 PyQt5 编写的 Vim 操作方式的浏览器。支持 Linux，Windows 和 macOS 操作系统，可以先[安装](https://github.com/qutebrowser/qutebrowser/releases)体验下。然后再看看源码学习如何用 Python 写浏览器


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/21244505.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift
24、[flappy-fly-bird](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/eleev/flappy-fly-bird)：用 Swift 写的 Flappy Bird 游戏


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/131873713.gif' style="max-width:80%; max-height=80%;"></img></p>

25、[Hue](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zenangst/Hue)：一个集合多功能于一体的着色工具。在 iOS 开发中非常好用，可以快速简单的进行 UI 的颜色设置、透明度修改、设置渐变颜色、修改图片的颜色等。相比于使用 Swift 原生繁重复杂的 RGBA 颜色 API，Hue 仅需要一行代码，简洁易用。示例代码：
```swift
// 设置 16 进制颜色
let white = UIColor(hex: "#ffffff")
let black = UIColor(hex: "#000000")

// 设置 alpha
let colorWithAlpha = myColor.alpha(0.75)

// 设置渐变
let gradient = [UIColor.blackColor(), UIColor.orangeColor()].gradient()

let secondGradient = [UIColor.blackColor(), UIColor.orangeColor()].gradient { gradient in
  gradient.locations = [0.25, 1.0]
  return gradient
}
```


### AI
26、[best-of-ml-python](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lukasmasuch/best-of-ml-python)：优秀的 Python 机器学习相关开源库集合。该项目会根据收录的开源项目各项指标计算得出一个评分，并定期更新


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/317029148.png' style="max-width:80%; max-height=80%;"></img></p>

27、[fawkes](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/Shawn-Shan/fawkes)：通过 AI 技术保护个人照片隐私的开源项目。芝加哥大学 Sand Lab 团队发起的项目，通过 AI 技术对图片的像素进行一些微调，人眼很难看出修改前后的区别，但对于人脸识别系统来说微调前后是天壤之别的，从而达到保护你照片隐私的效果


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/264782257.png' style="max-width:80%; max-height=80%;"></img></p>

28、[Paddle](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/PaddlePaddle/Paddle)：百度开源的深度学习框架。开发便捷的产业级深度学习框架，支持千亿特征、万亿参数、数百节点的大规模训练。官方还为用户提供了免费的算力可用于学习和训练，社区活跃教程齐全对新手友好


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/65711522.png' style="max-width:80%; max-height=80%;"></img></p>

29、[tinygrad](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/tinygrad/tinygrad)：一款小型的开源深度学习框架。它代码不足 1k 行足够简单，支持深度模型推理与训练。示例代码：
```python
from tinygrad.tensor import Tensor
import tinygrad.optim as optim

class TinyBobNet:
  def __init__(self):
    self.l1 = Tensor.uniform(784, 128)
    self.l2 = Tensor.uniform(128, 10)

  def forward(self, x):
    return x.dot(self.l1).relu().dot(self.l2).logsoftmax()

model = TinyBobNet()
optim = optim.SGD([model.l1, model.l2], lr=0.001)

# ... and complete like pytorch, with (x,y) data

out = model.forward(x)
loss = out.mul(y).mean()
optim.zero_grad()
loss.backward()
optim.step()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/305144746.png' style="max-width:80%; max-height=80%;"></img></p>

### Other
30、[azuredatastudio](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/microsoft/azuredatastudio)：微软开源的数据库桌面管理工具。该工具支持 SQL Server、Azure SQL DB 和 SQL DW 数据库，Windows 下的安装包仅不到 100 MB，还支持另外两大操作系统 macOS 和 Linux。如果开发中用到了上面的几种数据库，就试试这款免费的数据库桌面管理工具吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/109200851.jpeg' style="max-width:80%; max-height=80%;"></img></p>

31、[cats-of-jasnah](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/countable/cats-of-jasnah)：专为 3 岁左右孩子做的网页游戏。游戏很简单就是看图中有几只符合条件的猫，比如：有几只蓝色的猫？问题是通过语音提问，选择正确后会进入下一关。通过该项目不仅可以提高小孩的颜色辨识和识数的能力，还可以锻炼英语听力。[在线试玩](https://countable.github.io/cats-of-jasnah/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/229992640.png' style="max-width:80%; max-height=80%;"></img></p>

32、[Docker-OSX](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sickcodes/Docker-OSX)：让你用 Docker 跑 macOS 操作系统的项目。仅需 2 条命令分分钟让你起来一个 macOS 操作系统，听着刺激吧！搞起来：
```
# 拉镜像
docker pull sickcodes/docker-osx:latest

# 运行
docker run -it \
    --device /dev/kvm \
    -p 50922:10022 \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e "DISPLAY=${DISPLAY:-:0.0}" \
    sickcodes/docker-osx:latest
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img2/master/hellogithub/60/269336148.png' style="max-width:80%; max-height=80%;"></img></p>

33、[what-happens-when](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alex/what-happens-when)：该项目详细地解释了当你在浏览器中输入 google.com 按下回车后发生了什么。[中文](https://github.com/skyline75489/what-happens-when-zh_CN)




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub59.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub61.md">『Next』</a>
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
