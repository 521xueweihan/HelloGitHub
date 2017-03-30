# 《HelloGitHub》第 07 期
>兴趣是最好的老师，[HelloGitHub](https://github.com/521xueweihan/HelloGitHub) 就是帮你找到兴趣！

![](https://github.com/521xueweihan/HelloGitHub/blob/master/01/img/hello-github.jpg)

## 简介
最开始我只是想把自己在浏览 [GitHub](https://github.com/) 过程中，发现的有意思、高质量、容易上手的项目收集起来，这样便于以后查找和学习。后来一想，如果给这些 GitHub 项目都加上简单的效果图和一些通俗易懂的中文介绍。应该能够帮助到我这样的新手激发兴趣去参与、学习这些优秀、好玩的开源项目。

所以，我就做了一个面向**编程新手**、**热爱编程**、**对开源社区感兴趣** 的人群的月刊，月刊的内容包括：**各种编程语言的项目**、**各种让生活变得更美好的工具**、**书籍、学习笔记、教程等**。这些项目都是非常容易上手，而且非常 Cool，主要是希望大家能动手用起来，加入到**开源社区**中。会编程的可以贡献代码，不会编程的可以反馈使用这些工具中的 Bug、帮着宣传你觉得优秀的项目、Star 项目⭐️。同时你将学习到更多编程知识、提高自己的编程技巧、发现自己的**兴趣**。

🎉 最后 [HelloGitHub](https://github.com/521xueweihan/HelloGitHub) 这个项目就诞生了 🎉

---
｜**以下为本期内容**｜每个月 28 号发布最新一期，首发在我的 [GitHub](https://github.com/521xueweihan) 上｜[点击查看往期内容](https://github.com/521xueweihan/HelloGitHub#往期回顾)｜

#### Python 项目
1、[httpie](https://github.com/jkbrzt/httpie)：非常好用的命令行 HTTP 客户端，cURL 的替代者，返回的结果支持**高亮**，提高了可读性。用于调试接口、查看服务器返回的 HTTP 协议的信息。[在线文档](https://httpie.org/docs#examples)，下面的是 cURL 和 httpie 的返回结果对比图：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/07/img/httpie-show-min.png)

2、[langid](https://github.com/saffsd/langid.py)：用于识别输入文本数据所属的语种，目前支持 97 种语言识别。*感谢推荐人：[zhbzz2007](https://github.com/zhbzz2007)*。示例代码：
```python
import langid
text1 = "I am a coder and love data mining"
text2 = "请注明作者和出处并保留声明和联系方式"

print langid.classify(text1)
print langid.classify(text2)

# ('en', 0.9999957874458753)
# ('zh', 1.0)
```

3、[fake-useragent](https://github.com/hellysmile/fake-useragent)：伪装浏览器身份，常用于爬虫。这个项目的代码很少，可以阅读一下，看看 `ua.random` 是如何返回随机的浏览器身份的😁，示例代码：
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

#### Go 项目
4、[beego](https://github.com/astaxie/beego)：一个使用 Go 的思维来帮助您构建并开发 Go 应用程序的开源框架，齐全的文档（中文），丰富的使用案例。[官网地址](https://beego.me)

#### JavaScript 项目
5、[nodeclub](https://github.com/cnodejs/nodeclub)：Nodeclub 是使用 Node.js 和 MongoDB 开发的社区系统，[社区地址](http://cnodejs.org)：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/07/img/nodeclub-show-min.png)

6、[clipboard](https://github.com/zenorocha/clipboard.js)：实现了点击文本内容的 JavaScript 插件，优点：最新、极小、无任依赖、使用简单方便。[在线文档](https://clipboardjs.com)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/07/img/clipboard-show-min.png)

#### C 项目
7、[BaiduPCS](https://github.com/GangZhuo/BaiduPCS)：C 写的百度网盘命令行工具，[在线文档](https://github.com/GangZhuo/BaiduPCS/wiki/BaiduPCS-基本使用)

#### C++ 项目
8、[cpr](https://github.com/whoshuu/cpr)：C++ 版 `Request for human`，[在线文档](https://whoshuu.github.io/cpr/)，示例代码：
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

#### C# 项目
9、[MongoCola](https://github.com/magicdict/MongoCola)：MongoCola 是一个开源的 MongoDB 管理工具。持续开发、维护已经有**五年**了，[开发历程](http://www.cnblogs.com/TextEditor/p/5473190.html)，效果图如下：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/07/img/mongocola-show-min.png)

#### Objective-C 项目
10、[PYPhotoBrowser](https://github.com/iphone5solo/PYPhotoBrowser)：高仿 QQ、微信效果的图片浏览器（支持原图和缩略图、多种手势、CocoaPods），*感谢推荐人：[CoderKo1o](https://github.com/iphone5solo)*

#### CSS 项目
11、[cssicon](https://github.com/wentin/cssicon)：纯 CSS 实现的 icon

#### 开源书籍
12、[build-web-application-with-golang](https://github.com/astaxie/build-web-application-with-golang/blob/master/zh/preface.md)：《Go Web 编程》中文

#### 其它
13、[google-interview-university](https://github.com/jwasham/google-interview-university)：一套完整的学习手册帮助自己准备 Google 的面试，[中文翻译版](https://github.com/jwasham/coding-interview-university/blob/master/translations/README-cn.md)

14、[learning-react](https://github.com/yiminghe/learning-react)：[yiminghe](https://github.com/yiminghe) 的 react 中文教程，包含[入门](http://yiminghe.me/learning-react/tutorial/zh-cn/intro.html#/)和[进阶](http://yiminghe.me/learning-react/tutorial/zh-cn/advanced.html#/)

15、[static](https://github.com/staticfile/static)：这个项目是一个仓库，它尽可能全面收录优秀的开源库，并免费为之提供 CDN 加速服务，使之有更好的访问速度和稳定的环境。同时，它也提供开源库源接入的入口，让所有人都可以提交开源库，包括 JavaScript、CSS、image 和 swf 等静态文件。[访问 Staticfile CDN](http://staticfile.org)

16、[WebFundamentals](https://github.com/google/WebFundamentals)：（英文）Google 的 Web 开发者最佳练习教程

17、[How-to-Make-a-Computer-Operating-System](https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System)：（英文）如何做一个操作系统[在线阅读](https://www.gitbook.com/book/samypesse/how-to-create-an-operating-system/details)


---

## 声明
如果你发现了好玩、有意义的开源项目，[点击这里](https://github.com/521xueweihan/HelloGitHub/issues/new) 分享你觉得有意思的项目。

- 分享项目格式：`项目名称——项目地址：项目描述(中文)，追求完美👉项目上手 demo、截图`

或许你分享的项目会让别人由衷的感慨：“原来还有这么有意思的项目！编程可以这么酷！”

**欢迎转载，请注明出处和作者，同时保留声明和联系方式。**

## 联系方式
- [削微寒](https://github.com/521xueweihan)

- [博客园](http://www.cnblogs.com/xueweihan/)

- [知乎专栏](https://zhuanlan.zhihu.com/hellogithub)
