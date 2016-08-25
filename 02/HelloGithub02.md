#《HelloGithub》第二期
>兴趣是最好的老师，[《HelloGithub》](https://github.com/521xueweihan/HelloGithub)就是帮你找到兴趣！

![](https://github.com/521xueweihan/HelloGithub/blob/master/01/img/hello-github.jpg)

欢迎各路人士加入本项目，丰富月刊的内容，也可以直接在[Issue](https://github.com/521xueweihan/HelloGithub/issues/new)（需要登录github账号）分享你觉得好的项目。

## 简介
最开始只是我自己浏览github过程中收集的一些有中文介绍，通俗易懂，简单容易上手的项目。后来一想，如果每个github都有个简单的效果图和一些通俗易懂的中文介绍。这样应该更容易让我这样的新手接受。

所以，我就想做一个月刊的形式，面向新手的github月刊，月刊的内容主要包括：中文项目、少许英文项目、翻译的书籍以及教程。项目越容易上手越好，看起来越cool越好！主要是能动手用起来，我觉得这样会有助于编程能力的提高。然后[《HelloGithub月刊》](https://github.com/521xueweihan/HelloGithub)
这个项目就诞生了！😄

---
>**以下为本期内容**｜[点击查看往期内容](https://github.com/521xueweihan/HelloGithub)

#### Python项目
1、[螺壳网](https://github.com/alvan/luokr.com)：python Tornado写的开源网站，[访问](http://luokr.com/)，如图：
![](https://github.com/521xueweihan/HelloGithub/blob/master/02/img/%E8%9E%BA%E5%A3%B3%E7%BD%91-min.png)

2、[手撕包菜网站](https://github.com/78/ssbc)：python Django写的种子搜索网站，[访问](http://www.cilibaba.com/)，如图：
![](https://github.com/521xueweihan/HelloGithub/blob/master/02/img/%E6%89%8B%E6%92%95%E5%8C%85%E8%8F%9C%E7%BD%91-min.png)

3、[Listen 1](https://github.com/listen1)：Listen 1 让你用一个网页就能听到多个网站的在线音乐，支持各种平台。如图：
![](https://github.com/521xueweihan/HelloGithub/blob/master/02/img/listen1-min.png)

4、[pyhton代码片段](https://github.com/RealHacker/python-gems) or [leetcode答案](https://github.com/RealHacker/leetcode-solutions)

5、[老齐的python算法实现](https://github.com/qiwsir/algorithm)

6、[python-goose](https://github.com/grangier/python-goose)：python内容，文章提取器

Goose提取中文内容，示例代码

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

7、[mincss](https://github.com/peterbe/mincss)：python写的用来找到css中没有用到的代码片段，并删除。适用于：想要做一个页面，但是不会写css人。示例代码如下：

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
        print("\n")

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
        print("\n")


if __name__ == '__main__':
    run()
```

#### 其他项目（UI，CSS，JS等）
6、[ant-motion](https://github.com/ant-motion/ant-motion)：[在线演示](http://motion.ant.design/#/cases/help?_k=8bdppr)

7、[jQuery WeUI](https://github.com/lihongxun945/jquery-weui)：可能是最好用 WeUI 版本，如图：
![](https://github.com/521xueweihan/HelloGithub/blob/master/02/img/jquery-weui-min.png)

8 、[wechat-h5-boilerplate](https://github.com/panteng/wechat-h5-boilerplate)：为腾讯微信优化的H5动效模板，帮助你快速构建全屏滚动型H5页面，[示例](http://panteng.me/demos/whb/)

9、[github-markdown-css](https://github.com/sindresorhus/github-markdown-css)：github的markdown的css，就是使用了这个css后，markdown展示效果和github的大致一样。[示例](https://sindresorhus.com/github-markdown-css/)

10、 [waitForImages](https://github.com/alexanderdickson/waitForImages)：背景加载完事件，示例代码：
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

---
## 声明
不管你是大神，还是菜鸟，只要你发现了好玩的开源项目，都可以直接在[Issue](https://github.com/521xueweihan/HelloGithub/issues/new)（需要登录github账号），分享你觉得有意思的项目。同时有可能会被收录到下一期的月刊中，让更多人知道。

- 分享项目格式：项目名称——项目地址：项目描述(中文)，追求完美👉项目上手demo、有图有真相～

或许你分享的项目会让别人由衷的感慨：“原来还有这么有意思的项目！编程可以这么酷！”

欢迎转载，请注明出处和作者，同时保留声明和联系方式。

## 联系方式
- Github：[削微寒](https://github.com/521xueweihan)

- 博客园：[削微寒](http://www.cnblogs.com/xueweihan/)

- 邮箱：595666367@qq.com
