# HelloGitHub Vol.02
> Passion is the best teacher. **HelloGitHub** inspires your interest in open-source!
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## Table of Contents

Click the **「Table of Contents」** icon at the top-right corner to open the navigation and enjoy a better reading experience.

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

## Content
> **The content of this issue is as follows**｜Updated on the **28th** of each month

### CSS
1、[github-markdown-css](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/sindresorhus/github-markdown-css)：仿 GitHub 的 Markdown 的样式，就是使用了这个 CSS 后，Markdown 展示效果和 GitHub 的大致一样。[示例](https://sindresorhus.com/github-markdown-css/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/02/19544711.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript
2、[ant-motion](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/ant-design/ant-motion)：阿里开源的项目，一套 React 框架动效解决方案，可以帮助开发者，更容易的在项目中使用动效。同时可以方便快捷地制作一个公司的介绍页，[在线演示](https://motion.ant.design/)


3、[jquery-weui](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/lihongxun945/jquery-weui)：可能是最好用 WeUI 版本，展示效果如下：



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/02/48972492.png' style="max-width:80%; max-height=80%;"></img></p>

4、[listen1_desktop](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/listen1/listen1_desktop)：Listen 1 让你用一个网页就能听到多个网站的在线音乐，支持各种平台。如图：



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/02/59187489.png' style="max-width:80%; max-height=80%;"></img></p>

5、[ssbc](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/78/ssbc)：Python Django 写的种子搜索网站——手撕包菜，如图：



<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/02/35296157.png' style="max-width:80%; max-height=80%;"></img></p>

6、[waitForImages](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/alexanderdickson/waitForImages)：背景加载完事件，示例代码：
```html
<script type="text/javascript" src="http://catmull.uk/downloads/bg-loaded/bg-loaded.js"></script>
<script type="text/javascript">
   $('body').bgLoaded({
      afterLoaded : function() {
         alert('Background image done loading');
      }
   });
</script>
```


7、[wechat-h5-boilerplate](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/panteng/wechat-h5-boilerplate)：为腾讯微信优化的 HTML5 动效模板，帮助你快速构建全屏滚动型 HTML5 页面，[示例](https://panteng.github.io/wechat-h5-boilerplate/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/02/48837302.jpg' style="max-width:80%; max-height=80%;"></img></p>

### Python
8、[algorithm](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/qiwsir/algorithm)：老齐的 Python 算法教程


9、[mincss](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/peterbe/mincss)：Python 写的用来找到 CSS 中没有用到的代码片段，并删除。适用于：想要做一个页面，但是不会写 CSS 人。示例代码如下：
```python
#coding:utf-8
#!/usr/bin/env python
from __future__ import print_function
import sys, os
sys.path.insert(0, os.path.abspath('.'))
from mincss.processor import Processor

# 这里改成想要参考的页面
URL = 'http://localhost:9000/page.html'

def run():
    p = Processor()
    p.process(URL)

    # 输出INlink的css的简化前和简化后的css代码
    print("INLINES ".ljust(79, '-'))
    for each in p.inlines:
        print("On line %s" % each.line)
        print('- ' * 40)
        print("BEFORE")
        print(each.before)
        print('- ' * 40)
        print("AFTER:")
        print(each.after)

    # 输出link引用的css的简化前和简化后的css代码
    print("LINKS ".ljust(79, '-'))
    for each in p.links:
        print("On href %s" % each.href)
        print('- ' * 40)
        print("BEFORE")
        print(each.before)
        print('- ' * 40)
        print("AFTER:")
        print(each.after)

if __name__ == '__main__':
    run()
```


10、[python-gems](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/RealHacker/python-gems)：有趣的 Pyhton 代码片段集合


11、[python-goose](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/grangier/python-goose)：Goose 用于文章提取器，提取中文内容的示例代码：
```python
>>> from goose import Goose
>>> from goose.text import StopWordsChinese
>>> url  = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'
>>> g = Goose({'stopwords_class': StopWordsChinese})
>>> article = g.extract(url=url)
>>> print article.cleaned_text[:150]
香港行政长官梁振英在各方压力下就其大宅的违章建筑（僭建）问题到立法会接受质询，并向香港民众道歉。

梁振英在星期二（12月10日）的答问大会开始之际在其演说中道歉，但强调他在违章建筑问题上没有隐瞒的意图和动机。

一些亲北京阵营议员欢迎梁振英道歉，且认为应能获得香港民众接受，但这些议员也质问梁振英有
```


### Other
12、[leetcode-solutions](https://hellogithub.com/en/periodical/statistics/click?target=https://github.com/RealHacker/leetcode-solutions)：Leetcode OJ 的 Python 算法实现




<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub01.md">『Previous』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>Feedback</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/en/HelloGitHub03.md">『Next』</a>
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
