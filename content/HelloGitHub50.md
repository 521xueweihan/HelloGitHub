# 《HelloGitHub》第 50 期
> 兴趣是最好的老师，**HelloGitHub** 让你对开源感兴趣！
<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/cover.jpg' style="max-width:100%;"></img>
</p>

## 目录

点击右上角的 **「目录」** 图标打开目录，获得更好的阅读体验。

![](https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/catalog.png)

**Tips**：如果遇到图片刷不出来的情况，[点击](https://hellogithub.com/periodical/volume/50) 换一种浏览方式。

<p align="center">
  <img src="https://raw.githubusercontent.com/521xueweihan/img_logo/master/logo/weixin.png" style="max-width:30%;"></img><br>
关注「HelloGitHub」公众号，第一时间收到推送
</p>

## 内容
> **以下为本期内容**｜每月 **28** 号更新

### C# 项目
1、[KSFramework](https://hellogithub.com/periodical/statistics/click?target=https://github.com/mr-kelly/KSFramework)：一个整合 KEngine、SLua/XLua 的 Unity 5 Asset Bundle 游戏开发框架。它为程序员、美术、策划、运营提供辅助工具集，很多大型游戏都在用的项目，快来学起来吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/59349909.png' style="max-width:80%; max-height=80%;"></img></p>

### C++ 项目
2、[FlowChar](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Gusabary/FlowChar)：一个用来把伪代码生成纯字符流程图的小工具。让使用者仅需要写一段简单的伪代码，便可以生成对应的流程图。该项目结构清晰、使用简单，代码量少适合使用和“把玩”。示例图如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/237180335.png' style="max-width:80%; max-height=80%;"></img></p>

3、[notepanda](https://hellogithub.com/periodical/statistics/click?target=https://github.com/ChungZH/notepanda)：这是一个用 C++ 和 Qt 开发的记事本项目。支持代码高亮、自定义字体样式，还可以命令行呼出：notepanda main.cpp，支持 Windows、Linux 和 MacOS 三大系统。可作为学习 Qt、如何做开源项目的实战


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/258935245.png' style="max-width:80%; max-height=80%;"></img></p>

### CSS 项目
4、[css.gg](https://hellogithub.com/periodical/statistics/click?target=https://github.com/astrit/css.gg)：开源图标 UI 库。支持 CSS、SVG、Figma、NPM 等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/212204036.png' style="max-width:80%; max-height=80%;"></img></p>

### Go 项目
5、[grpcui](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fullstorydev/grpcui)：gRPC 的 Web 页面调试工具。该项目提供交互式的调试界面，让你开发 gRPC 的时候如虎添翼


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/160253491.png' style="max-width:80%; max-height=80%;"></img></p>

6、[uptoc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/bonaysoft/uptoc)：一个基于 Go 的静态博客部署到云存储的工具。静态博客不论是部署在 GitHubPages 还是 Netlify 等平台都存在国内访问速度慢的问题，解决这个问题最好的办法就是部署在国内的云存储，如腾讯云 COS、阿里云 OSS、七牛云等。借助该工具可以快速上传到上述云存储平台，加快你的静态博客访问速度
```bash
# 安装
curl -sSf http://uptoc.saltbo.cn/install.sh | sh
# 使用
uptoc --driver oss --region cn-beijing --access_key xxx --access_secret xxx --bucket demo-bucket /opt/blog/public
```


7、[Yearning](https://hellogithub.com/periodical/statistics/click?target=https://github.com/cookieY/Yearning)：Go 写的高颜值、开源 SQL 审核平台


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/107417113.png' style="max-width:80%; max-height=80%;"></img></p>

### Java 项目
8、[jbake](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jbake-org/jbake)：基于 Java 的开源静态网站、博客生成器。常用命令如下：
```
# 快速开始
$ curl -s "https://get.sdkman.io" | bash
$ sdk install jbake
$ mkdir awesome-jbake && cd awesome-jbake
$ jbake -i
$ jbake -b -s

jbake -h  #查看帮助文档
jbake -i  #安装依赖
jbake -s #运行项目
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/8530120.png' style="max-width:80%; max-height=80%;"></img></p>

9、[kkFileView](https://hellogithub.com/periodical/statistics/click?target=https://github.com/kekingcn/kkFileView)：基于 Spring boot 打造的多类型文件在线预览项目。支持多种文件例如：doc、ppt、xls、mp4、txt 等，功能强大便于快速开发和二次开发


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/113983289.png' style="max-width:80%; max-height=80%;"></img></p>

10、[Schedulis](https://hellogithub.com/periodical/statistics/click?target=https://github.com/WeBankFinTech/Schedulis)：一个基于 Azkaban 开发的工作流任务调度系统。该调度系统具备高性能、高可用（去中心化多调度中心和多执行器）和多租户资源隔离等。特性：
- 常规的 Command Shell 和 Linkis（HadoopMR、Hive、Spark、Sqoop、Python）大数据任务
- 特色的数据检查和工作流之间的依赖任务
- 完善的告警和工作流执行策略
- 提供多种类型的参数设置，动态全局变量和简单易用的 UI


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/261970003.png' style="max-width:80%; max-height=80%;"></img></p>

11、[zfile](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zfile-dev/zfile)：免费开源的在线云盘项目。功能特性：
- 文件夹密码
- 支持在线浏览文本文件、视频、图片、音乐
- 文件/目录二维码
- 全局搜索
- 等等


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/203183673.png' style="max-width:80%; max-height=80%;"></img></p>

### JavaScript 项目
12、[avataaars-generator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fangpenlin/avataaars-generator)：基于 React 实现的卡通头像生成工具。[在线尝试](https://getavataaars.com/)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/111056609.png' style="max-width:80%; max-height=80%;"></img></p>

13、[ce](https://hellogithub.com/periodical/statistics/click?target=https://github.com/jspreadsheet/ce)：一个轻量级、功能强大的电子表格库。轻松实现复杂数据的表格管理，支持 JS 数组、JSON、CSV 等数据，并且可以实现 excel 文件的直接复制和粘贴。示例代码：
```javascript
var data = [
    ['Jazz', 'Honda', '2019-02-12', '', true, '$ 2.000,00', '#777700'],
    ['Civic', 'Honda', '2018-07-11', '', true, '$ 4.000,01', '#007777'],
];

jexcel(document.getElementById('spreadsheet'), {
    data:data,
    columns: [
        { type: 'text', title:'Car', width:120 },
        { type: 'dropdown', title:'Make', width:200, source:[ "Alfa Romeo", "Audi", "Bmw" ] },
        { type: 'calendar', title:'Available', width:200 },
        { type: 'image', title:'Photo', width:120 },
        { type: 'checkbox', title:'Stock', width:80 },
        { type: 'numeric', title:'Price', width:100, mask:'$ #.##,00', decimal:',' },
        { type: 'color', width:100, render:'square', }
     ]
});
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/82552157.gif' style="max-width:80%; max-height=80%;"></img></p>

14、[form-create](https://hellogithub.com/periodical/statistics/click?target=https://github.com/xaboy/form-create)：一个可以通过 JSON 自动生成具有动态渲染、数据收集、验证和提交功能的表单生成器。结合内置多种常用表单组件和自定义组件，轻松搞定复杂的表单，支持 iview、element-ui、and-design-vue


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/121079935.gif' style="max-width:80%; max-height=80%;"></img></p>

15、[HueJumper2k](https://hellogithub.com/periodical/statistics/click?target=https://github.com/KilledByAPixel/HueJumper2k)：用 JS 实现的 2KB 大小的 3D 赛车游戏。[在线试试](https://killedbyapixel.itch.io/hue-jumper)


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/242063902.jpg' style="max-width:80%; max-height=80%;"></img></p>

16、[typical](https://hellogithub.com/periodical/statistics/click?target=https://github.com/camwiegert/typical)：零依赖、仅 400 字节的输入动画库。示例代码：
```javascript
import {
    type,
    type as loop
};

const steps = [1000, 'Ready', 1000, 'Set', 1000, 'Go'];

type(element, ...steps, loop);
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/211405607.gif' style="max-width:80%; max-height=80%;"></img></p>

### Python 项目
17、[fastapi](https://hellogithub.com/periodical/statistics/click?target=https://github.com/fastapi/fastapi)：基于 Python 3.6+ 的高性能 Web 框架。“人如其名”用 FastAPI 写接口那叫一个快、调试方便，Python 在进步而它基于这些进步，让 Web 开发变得更快、更强。示例代码：
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 启动命令：uvicorn main:app --reload
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/160919119.png' style="max-width:80%; max-height=80%;"></img></p>

18、[geek_crawler](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zhengxiaotian/geek_crawler)：极客时间课程（目前仅支持图文、音频）下载到本地的 Python 脚本。需输入账号密码后，才能将指定极客时间专栏课程保存到本地，方便随时随地学习


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/259614563.jpeg' style="max-width:80%; max-height=80%;"></img></p>

19、[MrDoc](https://hellogithub.com/periodical/statistics/click?target=https://github.com/zmister2016/MrDoc)：一个基于 Python 开发的在线文档系统。支持 Markdown 语法、文集分类、科学公式、流程图、思维导图等内容。清爽的阅读界面，还可以把内容打包导出为 Markdown 文件、EPUB 文件、PDF 文件。适合作为个人和小型团队的私有文档服务


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/254536602.png' style="max-width:80%; max-height=80%;"></img></p>

### Swift 项目
20、[SwiftUI](https://hellogithub.com/periodical/statistics/click?target=https://github.com/Jinxiansen/SwiftUI)：该项目参考 SwiftUI 官方示例，记录代码和展示效果


21、[vimr](https://hellogithub.com/periodical/statistics/click?target=https://github.com/qvacua/vimr)：Neovim 的 macOS 版


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/17300388.png' style="max-width:80%; max-height=80%;"></img></p>

### 人工智能
22、[photo2cartoon](https://hellogithub.com/periodical/statistics/click?target=https://github.com/minivision-ai/photo2cartoon)：将真实照片转换为卡通风格的开源项目。效果如下：


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/256445099.jpg' style="max-width:80%; max-height=80%;"></img></p>

23、[pose-animator](https://hellogithub.com/periodical/statistics/click?target=https://github.com/yemount/pose-animator)：一个基于 PoseNet 和 FaceMesh 可将你的 Pose 变成 2D 动画的工具。生成的动画人物会根据你的表情和肢体动作做出相应动作，来试试制作你专属的 2D 镜像人吧


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/251262566.gif' style="max-width:80%; max-height=80%;"></img></p>

24、[Real-World-Masked-Face-Dataset](https://hellogithub.com/periodical/statistics/click?target=https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset)：口罩人脸数据集


25、[scikit-opt](https://hellogithub.com/periodical/statistics/click?target=https://github.com/guofei9987/scikit-opt)：一个封装了 7 种启发式算法的 Python 代码库。分别是：差分进化算法、遗传算法、粒子群算法、模拟退火算法、蚁群算法、鱼群算法、免疫优化算法，示例代码：
```python
from sko.GA import GA_TSP

ga_tsp = GA_TSP(func=cal_total_distance, n_dim=num_points, size_pop=50, max_iter=500, prob_mut=1)
best_points, best_distance = ga_tsp.run()
```


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/113166974.gif' style="max-width:80%; max-height=80%;"></img></p>

### 其它
26、[fullstackopen](https://hellogithub.com/periodical/statistics/click?target=https://github.com/villeheikkila/fullstackopen)：免费开源的 Web 全栈编程课程。一站式学习 React、Redux、Node.js、MongoDB、GraphQL 以及 TypeScript，这门课程会向你介绍基于 JavaScript 的现代 Web 编程技术。让你可以利用 ReactJS 搭配 Node.js 开发的 REST API，来搭建单页面应用程序


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/166814830.png' style="max-width:80%; max-height=80%;"></img></p>

27、[GitHub520](https://hellogithub.com/periodical/statistics/click?target=https://github.com/521xueweihan/GitHub520)：通过修改 hosts 解决 GitHub 访问慢、图裂问题的项目。基于 GitHub Action 定时访问 ipaddress 自动获取、输出 GitHub 相关域名对应的最新 IP 保证长期有效，用户不需要安装和运行代码，直接复制项目首页的内容便可生效


28、[vim](https://hellogithub.com/periodical/statistics/click?target=https://github.com/vim/vim)：Vim 官方仓库


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/40997482.png' style="max-width:80%; max-height=80%;"></img></p>

29、[winget-cli](https://hellogithub.com/periodical/statistics/click?target=https://github.com/microsoft/winget-cli)：微软开源的 Windows 程序包管理器，帮助开发者快速的安装工具（预览版）。 目前有搜索、显示和安装软件包等功能，命令简单 `winget install <tool>`


<p align="center"><img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/50/197275130.png' style="max-width:80%; max-height=80%;"></img></p>



<p align="center">
    <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub49.md">『上一期』</a> | <a href='https://github.com/521xueweihan/HelloGitHub/issues/899'>反馈和建议</a> | <a href="https://github.com/521xueweihan/HelloGitHub/blob/master/content/HelloGitHub51.md">『下一期』</a>
</p>

---
<p align="center">
    👉 <a href='https://hellogithub.com/periodical'>来！推荐开源项目</a> 👈<br>
    微信中搜：<strong>HelloGitHub</strong> 关注公众号<br>
    不仅能第一时间收到推送，还有回馈粉丝的活动<br>
    如果文中的图刷不出来，可以点击 <a href='https://hellogithub.com/periodical/volume/50'>这里</a>。
</p>

## 赞助


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


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
