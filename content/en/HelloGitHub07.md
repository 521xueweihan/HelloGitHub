# HelloGitHub Vol.07
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
1、[BaiduPCS](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/GangZhuo/BaiduPCS)：C 写的百度网盘命令行工具，[在线文档](https://github.com/GangZhuo/BaiduPCS/wiki/BaiduPCS-基本使用)


### C#
2、[MongoCola](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/magicdict/MongoCola)：MongoCola 是一个开源的 MongoDB 管理工具。持续开发、维护已经有**五年**了，[开发历程](http://www.cnblogs.com/TextEditor/p/5473190.html)，效果图如下：



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/2518082.png' style="max-width:80%; max-height=80%;"></img></p>

### C++
3、[cpr](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/libcpr/cpr)：C++ 版 `Request for human`，[在线文档](https://whoshuu.github.io/cpr/)，示例代码：
```C++
#include <cpr/cpr.h>

int main(int argc, char** argv) {
    auto r = cpr::Get(cpr::Url{"https://api.github.com/repos/whoshuu/cpr/contributors"},
                      cpr::Authentication{"user", "pass"},
                      cpr::Parameters{{"anon", "true"}, {"key", "value"}});
    r.status_code;                  // 200
    r.header["content-type"];       // application/json; charset=utf-8
    r.text;                         // JSON text string
}
```


### CSS
4、[cssicon](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/wentin/cssicon)：纯 CSS 实现的 icon


### Go
5、[beego](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/beego/beego)：一个使用 Go 的思维来帮助您构建并开发 Go 应用程序的开源框架，齐全的文档（中文），丰富的使用案例。[官网地址](https://beego.me)


### JavaScript
6、[clipboard.js](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/zenorocha/clipboard.js)：实现了点击文本内容的 JavaScript 插件，优点：最新、极小、无任依赖、使用简单方便。[在线文档](https://clipboardjs.com)



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/42751014.png' style="max-width:80%; max-height=80%;"></img></p>

7、[nodeclub](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/cnodejs/nodeclub)：Nodeclub 是使用 Node.js 和 MongoDB 开发的社区系统，[社区地址](https://cnodejs.org/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/3447593.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C
8、[PYPhotoBrowser](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ko1o/PYPhotoBrowser)：高仿 QQ、微信效果的图片浏览器（支持原图和缩略图、多种手势、CocoaPods）


### Python
9、[cli](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/httpie/cli)：非常好用的命令行 HTTP 客户端，cURL 的替代者，返回的结果支持**高亮**，提高了可读性。用于调试接口、查看服务器返回的 HTTP 协议的信息。[在线文档](https://httpie.org/docs#examples)，下面的是 cURL 和 httpie 的返回结果对比图：



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/3544424.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[fake-useragent](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/fake-useragent/fake-useragent)：伪装浏览器身份，常用于爬虫。这个项目的代码很少，可以阅读一下，看看 `ua.random` 是如何返回随机的浏览器身份的😁，示例代码：
```python
from fake_useragent import UserAgent
ua = UserAgent()

ua.ie
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);
ua.msie
# Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)'
ua['Internet Explorer']
# Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)
ua.opera
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11
ua.chrome
# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
ua.google
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13
ua['google chrome']
# Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11
ua.firefox
# Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1
ua.ff
# Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1
ua.safari
# Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25

# and the best one, random via real world browser usage statistic
ua.random
```


11、[langid.py](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/saffsd/langid.py)：用于识别输入文本数据所属的语种，目前支持 97 种语言识别。示例代码：
```python
import langid
text1 = "I am a coder and love data mining"
text2 = "请注明作者和出处并保留声明和联系方式"

print langid.classify(text1)
print langid.classify(text2)

# ('en', 0.9999957874458753)
# ('zh', 1.0)
```


### Other
12、[coding-interview-university](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/jwasham/coding-interview-university)：一套完整的学习手册帮助自己准备 Google 的面试，[中文翻译版](https://github.com/jwasham/coding-interview-university/blob/master/translations/README-cn.md)


13、[How-to-Make-a-Computer-Operating-System](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System)：（英文）如何做一个操作系统[在线阅读](https://www.gitbook.com/book/samypesse/how-to-create-an-operating-system/details)


14、[learning-react](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/yiminghe/learning-react)：[yiminghe](https://github.com/yiminghe) 的 react 中文教程，包含[入门](http://yiminghe.me/learning-react/tutorial/zh-cn/intro.html#/)和[进阶](http://yiminghe.me/learning-react/tutorial/zh-cn/advanced.html#/)


15、[static](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/staticfile/static)：这个项目是一个仓库，它尽可能全面收录优秀的开源库，并免费为之提供 CDN 加速服务，使之有更好的访问速度和稳定的环境。同时，它也提供开源库源接入的入口，让所有人都可以提交开源库，包括 JavaScript、CSS、image 和 swf 等静态文件。[访问 Staticfile CDN](https://www.staticfile.org/about.html)


16、[WebFundamentals](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/google/WebFundamentals)：（英文）Google 的 Web 开发者最佳练习教程


### Book
17、[build-web-application-with-golang](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/astaxie/build-web-application-with-golang)：《Go Web 编程》中文




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub06.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub08.md">『Next』</a>
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
