# 《HelloGitHub》第 32 期
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
- [C 项目](#C-项目)
- [C# 项目](#C-项目-1)
- [C++ 项目](#C-项目-2)
- [Go 项目](#Go-项目)
- [Java 项目](#Java-项目)
- [JavaScript 项目](#JavaScript-项目)
- [Objective-C 项目](#Objective-C-项目)
- [Python 项目](#Python-项目)
- [其它](#其它)
- [开源书籍](#开源书籍)
- [机器学习](#机器学习)


**Tips**：如果文中的图刷不出来，可以向我们反馈。也可以访问 [官网](https://hellogithub.com/) 获取更好的阅读体验。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/logo/weixin.png" style="max-width:30%;"></img><br>
欢迎关注 HelloGitHub 公众号
</p>

## 内容
> **以下为本期内容**｜每个月 **28** 号发布最新一期

### C 项目
1、[os-tutorial](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/cfenollosa/os-tutorial)：（英文）如何从头开始创建操作系统

2、[nvtop](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/Syllo/nvtop)：NVIDIA GPU 类 (h)top 的任务监控工具，它可以监控多个 GPU 并以熟悉的方式（类 htop 方式）打印有关它们的信息

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/nvtop.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C# 项目
3、[QuickLook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/QL-Win/QuickLook)：它允许 Windows 用户只需按空格键即可以快速地查看文件内容（类 macOS 的 Quick Look）

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/QuickLook.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### C++ 项目
4、[oatpp](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/oatpp/oatpp)：轻量、高性能、零依赖，纯 C++ 实现的 Web 框架。示例代码片段：
```c++
ENDPOINT("GET", "demo/api/json", getJson) {
  auto dto = MyDto::createShared();
  dto->statusCode = 200;
  dto->message = "Hello json";
  return createDtoResponse(Status::CODE_200, dto);
}

Output:
{"message": "Hello json", "statusCode": 200}
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Go 项目
5、[go-sniffer](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/40t/go-sniffer)：该工具通过抓包截取项目中的数据库、redis 请求解析成相应的语句。便于调试，不要修改代码，直接嗅探项目中的数据请求。使用说明如下：
```
=======================================================================
[使用说明]

    go-sniffer [设备名] [插件名] [插件参数(可选)]

    [例子]
          go-sniffer en0 redis          抓取redis数据包
          go-sniffer en0 mysql -p 3306  抓取mysql数据包,端口3306

    go-sniffer --[命令]
               --help 帮助信息
               --env  环境变量
               --list 插件列表
               --ver  版本信息
               --dev  设备列表
    [例子]
          go-sniffer --list 查看可抓取的协议

=======================================================================
[设备名] : lo0 :   127.0.0.1
[设备名] : en0 : x:x:x:x:x5:x  192.168.1.3
[设备名] : utun2 :   1.1.11.1
=======================================================================
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/go-sniffer.gif' style="max-width:80%; max-height=80%;"></img></p>

6、[dive](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/wagoodman/dive)：用来探索 docker 镜像每一层文件系统，以及发现缩小镜像体积方法的命令行工具。启动命令：`dive 镜像名`

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/dive.gif' style="max-width:80%; max-height=80%;"></img></p>

7、[soar](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/XiaoMi/soar)：SQL 自动优化和改写的工具。可以自动优化 MySQL 语法族，并且给出为什么要这样优化的理由。功能特点：
- 跨平台支持
- 目前只支持 MySQL 语法族协议的 SQL 优化
- 支持基于启发式算法的语句优化
- 支持复杂查询的多列索引优化（UPDATE、INSERT、DELETE、SELECT）
- 等等

```
echo "select title from sakila.film" | ./soar 
# Query: 25807E6B94BEA72C
★ ★ ★ ★ ☆ 80分
SELECT
  title
FROM
  sakila. film
##  最外层SELECT未指定WHERE条件
* **Item:**  CLA.001
* **Severity:**  L4
* **Content:**  SELECT语句没有WHERE子句，可能检查比预期更多的行(全表扫描)。对于SELECT COUNT(\*)类型的请求如果不要求精度，建议使用SHOW TABLE STATUS或EXPLAIN替代。
```

8、[websocketd](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/joewalnes/websocketd)：把命令行的输出 stdout 和 stderr 重定向为一个 websocket 服务的工具。运行步骤如下：
1. 安装命令：`brew install websocketd`
2. 创建 count.sh 内容如下
3. 运行 count.sh，命令：`./count.sh`
4. 启动一个 websocket server，命令：`websocketd --port=8080 ./count.sh`
5. 创建 html 文件，代码如下
6. 点击打开 count.html 文件，查看效果
```
count.sh 文件内容如下

#!/bin/bash
for ((COUNT = 1; COUNT <= 3; COUNT++)); do
  echo $COUNT
  sleep 1
done

count.html 文件内容如下

<!DOCTYPE html>
<pre id="log"></pre>
<script>
  // helper function: log message to screen
  function log(msg) {
    document.getElementById('log').textContent += msg + '\n';
  }

  // setup websocket with callbacks
  var ws = new WebSocket('ws://localhost:8080/');
  ws.onopen = function() {
    log('CONNECT');
  };
  ws.onclose = function() {
    log('DISCONNECT');
  };
  ws.onmessage = function(event) {
    log('MESSAGE: ' + event.data);
  };
</script>
```

9、[athens](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/gomods/athens)：Go Modules 下载代理服务，解决国内 Go 装包的痛。妈妈再也不用担心我因为装不上依赖库而不吃饭，使用步骤：
```
$ export GO111MODULE=on
$ export GOPROXY=http://127.0.0.1:3000
$ git clone https://github.com/athens-artifacts/walkthrough.git
$ cd walkthrough
$ go run .
go: downloading github.com/athens-artifacts/samplelib v1.0.0
The 🦁 says rawr!
```

10、[archiver](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mholt/archiver)：命令行压缩和解压缩工具。终于不用再记 `tar -czvf` 了，使用命令：
```
# Syntax: arc archive [archive name] [input files...] 压缩

$ arc archive test.tar.gz file1.txt images/file2.jpg folder/subfolder

# Syntax: arc unarchive [archive name] [destination] 解压缩

$ arc unarchive test.tar.gz
```

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Java 项目
11、[ratel](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ainilili/ratel)：命令行可联网的斗地主游戏。Ratel 分客户端和服务端，你可以让小伙伴们的客户端都连接你的服务器进行游戏，也可以直接连接作者的公网服务器进行游戏

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/ratel.gif' style="max-width:80%; max-height=80%;"></img></p>

12、[SpiderMan](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/simplepeng/SpiderMan)：手机端显示 Android 崩溃日志，示例代码如下：
```java
SpiderMan.init(this)
//设置回调异常信息，友盟等第三方崩溃信息收集平台会用到,
.setOnCrashListener(new SpiderMan.OnCrashListener() {
    /**
      *
      * @param t
      * @param ex
      * @param model 崩溃信息记录，包含设备信息
      */
    @Override
    public void onCrash(Thread t, Throwable ex, CrashModel model) {
      
    }
});
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/SpiderMan.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### JavaScript 项目
13、[three.js](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/mrdoob/three.js)：一个知名的 JavaScript 3D 库。随着数据可视化以及 Web AR 的流行，会越来越多使用到 three.js ，尤其是和 Vue/React 前端框架结合使用。官方网站包含丰富的[示例](https://threejs.org/examples/)和全面的[中文文档](https://threejs.org/docs/)，赶快去写几个 demo 熟悉下该库吧

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/three-js.png' style="max-width:80%; max-height=80%;"></img></p>

14、[storybook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/storybookjs/storybook)：UI 组件开发测试的环境。你可以使用 React、React Native、Vue、Angular、Ember 开发你的组件，并且可以使用 storybook 提供的众多插件进行测试以及开发。[在线示例](https://storybook.js.org/examples/)

15、[hexo](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/hexojs/hexo)：基于 Node.js 快速、简洁且高效的静态博客生成框架。可以使用 hexo 快速生成静态博客，它拥有丰富的[插件库](https://hexo.io/plugins/)、[主题库](https://hexo.io/themes/)。在使用 hexo 的时候也可以自己创建、定制属于自己的主题

16、[picojs](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/tehnokv/picojs)：200 行实现的面部识别库，[在线示例](https://tkv.io/posts/picojs-intro/demo/)

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Objective-C 项目
17、[MacPass](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/MacPass/MacPass)：一款 macOS 平台的免费、开源、实用的密码管理工具

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/MacPass.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### Python 项目
18、[himawaripy](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/boramalper/himawaripy)：一个 Python3 脚本，它会定时（需设置定时任务）抓取由日本 Himawari 8 气象卫星拍摄的接近实时的地球照片，并将它设置成你的桌面背景

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/himawaripy.gif' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 其它
19、[search-engine-optimization](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/marcobiedermann/search-engine-optimization)：（英文）这个项目收集了很多 SEO 优化的建议

20、[lemonade-stand](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/nayafia/lemonade-stand)：《开源项目挣钱实用手册》[中文版](https://github.com/wizicer/FinancialSupportForOpenSource)

21、[ProgrammingFonts](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/ProgrammingFonts/ProgrammingFonts)：适合程序员的编程字体的集合，现在有 30 多种奇妙的字体

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/ProgrammingFonts.png' style="max-width:80%; max-height=80%;"></img></p>

22、[Linux-Tutorial](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/judasn/Linux-Tutorial)：Java 程序员眼中的 Linux

23、[Best-websites-a-programmer-should-visit](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sdmg15/Best-websites-a-programmer-should-visit)：（英文）一些对程序员有用的网站，网站类别包含：新闻、查问题、学习、教程等

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 开源书籍
24、[sdn-handbook](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/feiskyer/sdn-handbook)：有关 SDN 的资料和书籍非常丰富，但入门和学习 SDN 依然是非常困难。该项目整理了 SDN 实践中的一些基本理论和实践案例心得，希望大家看完后有所收获

25、[write-you-a-haskell](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/sdiehl/write-you-a-haskell)：（英文）《Write You a Haskell》

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>

### 机器学习
26、[awesome-machine-learning](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/josephmisiti/awesome-machine-learning)：一个精选的机器学习框架、库、软件的集合项目

27、[fastai](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/fastai/fastai)：利用当前最好的深度学习算法简化训练神经网络的过程。包含了很多“开箱即用”的工具，支持 Vision、Collab 等模型。示例代码：
```python
# here's how to train an MNIST model using resnet18
untar_data(MNIST_PATH)
data = image_data_from_folder(MNIST_PATH)
learn = create_cnn(data, tvm.resnet18, metrics=accuracy)
learn.fit(1)
```

28、[deepvariant](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google/deepvariant)：一个数据分析工作流。能够使用深度神经网络从下一代 DNA 序列数据中调用遗传变异体，联想到了最近的基因编辑人类事件。关于如何工作的技术细节，如下图：

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/deepvariant.png' style="max-width:80%; max-height=80%;"></img></p>

29、[AIAlpha](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/VivekPa/AIAlpha)：使用无监督学习和监督学习来预测股票，有趣的项目。运行步骤如下：
```
git clone https://github.com/VivekPa/AlphaAI.git
cd AlphaAI
pip install -r requirements.txt
python run.py
```

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/AlphaAI.png' style="max-width:80%; max-height=80%;"></img></p>

30、[bert](https://hellogithub.com/periodical/statistics/click/?target=https://github.com/google-research/bert)：一种新的语言表征模型，来自 Transformer 的双向编码器表征。目前最强 NLP 预训练模型，横扫 11 项 NLP 任务记录

<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/32/img/bert.png' style="max-width:80%; max-height=80%;"></img></p>

<p align="center"><a href="#目录">🔙 返回目录 🔙</a></p><br>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/31/HelloGitHub31.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/33/HelloGitHub33.md">『下一期』</a>
</p>

---
<p align="center">
    看完了，还不够？<a href='https://github.com/ruanyf/weekly'><科技爱好者周刊></a>。还不过瘾，那就看看 <a href='https://github.com/521xueweihan/HelloGitHub#%E5%86%85%E5%AE%B9'><往期内容></a>吧。<br>
    <a href='https://github.com/521xueweihan/HelloGitHub/issues/new'>点击分享发现的有趣项目</a>
</p>


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
