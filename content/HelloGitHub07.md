# 《HelloGitHub》第 07 期
> 兴趣是最好的老师，**HelloGitHub** 让你对编程感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/07) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号更新

### C 项目
1、[BaiduPCS](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/GangZhuo/BaiduPCS)：C 写的百度网盘命令行工具，[在线文档](https://github.com/GangZhuo/BaiduPCS/wiki/BaiduPCS-基本使用)


### C# 项目
2、[MongoCola](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/magicdict/MongoCola)：MongoCola 是一个开源的 MongoDB 管理工具。持续开发、维护已经有**五年**了，[开发历程](http://www.cnblogs.com/TextEditor/p/5473190.html)，效果图如下：



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/2518082.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
3、[cpr](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/libcpr/cpr)：C++ 版 `Request for human`，[在线文档](https://whoshuu.github.io/cpr/)，示例代码：
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


### CSS 项目
4、[cssicon](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wentin/cssicon)：纯 CSS 实现的 icon


### Go 项目
5、[beego](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/beego/beego)：一个使用 Go 的思维来帮助您构建并开发 Go 应用程序的开源框架，齐全的文档（中文），丰富的使用案例。[官网地址](https://beego.me)


### JavaScript 项目
6、[clipboard.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/zenorocha/clipboard.js)：实现了点击文本内容的 JavaScript 插件，优点：最新、极小、无任依赖、使用简单方便。[在线文档](https://clipboardjs.com)



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/42751014.png' style="max-width:80%; max-height=80%;"></img></p>

7、[nodeclub](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cnodejs/nodeclub)：Nodeclub 是使用 Node.js 和 MongoDB 开发的社区系统，[社区地址](https://cnodejs.org/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/3447593.png' style="max-width:80%; max-height=80%;"></img></p>

### Objective-C 项目
8、[PYPhotoBrowser](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ko1o/PYPhotoBrowser)：高仿 QQ、微信效果的图片浏览器（支持原图和缩略图、多种手势、CocoaPods）


### Python 项目
9、[cli](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/httpie/cli)：非常好用的命令行 HTTP 客户端，cURL 的替代者，返回的结果支持**高亮**，提高了可读性。用于调试接口、查看服务器返回的 HTTP 协议的信息。[在线文档](https://httpie.org/docs#examples)，下面的是 cURL 和 httpie 的返回结果对比图：



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/07/3544424.gif' style="max-width:80%; max-height=80%;"></img></p>

10、[fake-useragent](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fake-useragent/fake-useragent)：伪装浏览器身份，常用于爬虫。这个项目的代码很少，可以阅读一下，看看 `ua.random` 是如何返回随机的浏览器身份的😁，示例代码：
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


11、[langid.py](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/saffsd/langid.py)：用于识别输入文本数据所属的语种，目前支持 97 种语言识别。示例代码：
```python
import langid
text1 = "I am a coder and love data mining"
text2 = "请注明作者和出处并保留声明和联系方式"

print langid.classify(text1)
print langid.classify(text2)

# ('en', 0.9999957874458753)
# ('zh', 1.0)
```


### 其它
12、[coding-interview-university](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/jwasham/coding-interview-university)：一套完整的学习手册帮助自己准备 Google 的面试，[中文翻译版](https://github.com/jwasham/coding-interview-university/blob/master/translations/README-cn.md)


13、[How-to-Make-a-Computer-Operating-System](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System)：（英文）如何做一个操作系统[在线阅读](https://www.gitbook.com/book/samypesse/how-to-create-an-operating-system/details)


14、[learning-react](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/yiminghe/learning-react)：[yiminghe](https://github.com/yiminghe) 的 react 中文教程，包含[入门](http://yiminghe.me/learning-react/tutorial/zh-cn/intro.html#/)和[进阶](http://yiminghe.me/learning-react/tutorial/zh-cn/advanced.html#/)


15、[static](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/staticfile/static)：这个项目是一个仓库，它尽可能全面收录优秀的开源库，并免费为之提供 CDN 加速服务，使之有更好的访问速度和稳定的环境。同时，它也提供开源库源接入的入口，让所有人都可以提交开源库，包括 JavaScript、CSS、image 和 swf 等静态文件。[访问 Staticfile CDN](https://www.staticfile.org/about.html)


16、[WebFundamentals](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/WebFundamentals)：（英文）Google 的 Web 开发者最佳练习教程


### 开源书籍
17、[build-web-application-with-golang](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/astaxie/build-web-application-with-golang)：《Go Web 编程》中文




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub06.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub08.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/07'>这里</a>。
</p>

## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
