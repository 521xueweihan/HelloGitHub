#### Python 项目
1、[reddit](https://github.com/reddit/reddit)：[reddit.com](https://www.reddit.com/) 网站的源码，通过这个项目，可以学习 Python 在构建大型项目中的使用、项目结构、代码风格、Python 技巧的使用方法等。[安装教程](https://github.com/reddit/reddit/wiki/Install-guide)

![](https://github.com/521xueweihan/HelloGitHub/blob/master/08/img/reddit-show-min.jpg)

2、[httpstat](https://github.com/reorx/httpstat)：httpstat 美化了 `curl` 的结果，使得结果更加可读。同时它无依赖、兼容 Python3、一共才 300 多行。还可以显示 HTTP 请求的每个过程中消耗的时间，如下图：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/08/img/httpstat-show-min.png)

3、[PyMySQL](https://github.com/PyMySQL/PyMySQL)：纯 Pyton 写的 MySQL 库，纯 Python 的好处就是可以运行在任何装有 Python 解释器（CPython、PyPy、IronPython）的平台上。相对于 [MySQLdb](https://github.com/farcepest/MySQLdb1) 性能几乎一样，使用方法也一样，但是 **PyMySQL 安装方法极其简单**——`pip install PyMySQL`，PyMySQL 使用示例代码：
```
# 下面为例子需要的数据库的建表语句
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
```

```python
# -*- coding: utf-8 -*-
import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 创建一个新的纪录（record）
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # 连接不会自动提交，所以你想下面要调用 commit 方法，存储对数据库的改动
    connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))

        # 获取一条的纪录（record）
        result = cursor.fetchone()
        print(result)  # 结果输出：{'password': 'very-secret', 'id': 1}
finally:
    connection.close()  # 操作完数据库一要记得调用 close 方法，关闭连接
```

#### Go 项目
4、[kcptun](https://github.com/xtaci/kcptun)：也许是世界上最快的 UDP 传输工具，支持 macOS/Linux/Windows/FreeBSD/ARM/Raspberry Pi/OpenWrt。

![](https://github.com/521xueweihan/HelloGitHub/blob/master/08/img/kcptun-show-min.png)

#### Ruby 项目
5、[discourse](https://github.com/discourse/discourse)：Ruby 语言写的论坛，百分之百开源、免费。

![](https://github.com/521xueweihan/HelloGitHub/blob/master/08/img/discourse-show-min.png)

#### JavaScript 项目
6、[WeFlow](https://github.com/weixin/WeFlow)：微信出品的一个高效、强大、跨平台的 Web 前端开发工作流工具，[官网](https://weflow.io/)：

![](https://github.com/521xueweihan/HelloGitHub/blob/master/08/img/weflow-show-min.jpeg)

7、[atrament.js](https://github.com/jakubfiala/atrament.js)：极小的 JavaScript 画板，[在线演示](http://fiala.uk/atrament.js/demo/)

#### C++ 项目
8、[libco](https://github.com/Tencent/libco)：腾讯的开源项目——libco 是微信后台大规模使用的 C/C++ 协程库，2013 年至今稳定运行在微信后台的数万台机器上。
- 无需侵入业务逻辑，把多进程、多线程服务改造成协程服务，并发能力得到百倍提升
- 支持 CGI 框架，轻松构建 Web 服务
- 支持 gethostbyname、mysqlclient、ssl 等常用第三方库
- 可选的共享栈模式，单机轻松接入千万连接
- 完善简洁的协程编程接口
    - 类 pthread 接口设计，通过 co_create、co_resume 等简单清晰接口即可完成协程的创建与恢复
    - \_\_thread 的协程私有变量、协程间通信的协程信号量 co_signal
    - 语言级别的 lambda 实现，结合协程原地编写并执行后台异步任务
    - 基于 epoll/kqueue 实现的小而轻的网络框架，基于时间轮盘实现的高性能定时器

#### C# 项目
9、[Newtonsoft.Json](https://github.com/JamesNK/Newtonsoft.Json)：Newtonsoft.Json 是一款 .NET 平台中开源的 JSON 序列化和反序列化类库，示例代码：
```C#
public class Account
{
    public string Email { get; set; }
    public bool Active { get; set; }
    public DateTime CreatedDate { get; set; }
    public IList<string> Roles { get; set; }
}

Account account = new Account
{
     Email = "james@example.com",
     Active = true,
     CreatedDate = new DateTime(2013, 1, 20, 0, 0, 0, ateTimeKind.Utc),
     Roles = new List<string>
     {
         "User",
         "Admin"
    }
};

string json = JsonConvert.SerializeObject(account, Formatting.Indented);
// {
//   "Email": "james@example.com",
//   "Active": true,
//   "CreatedDate": "2013-01-20T00:00:00Z",
//   "Roles": [
//     "User",
//     "Admin"
//   ]
// }

Console.WriteLine(json);
```

#### Objective-C 项目
10、[aria2gui](https://github.com/yangshun1029/aria2gui)：Aria2 的 Mac 客户端（下载工具），[介绍、使用方法](http://www.jianshu.com/p/1290f8e7b326)，特点：
- 集成了 aria2，运行后即完成配置工作
- 多线程下载
- 未完成任务退出可以自动保存
- 支持迅雷离线，百度、115、360 等网盘的 aria2 导出（需要浏览器插件支持）
- 支持 PT/BT，BT 速度跟种子热度有关，如果没有速度网盘离线后再下载
- 在 Badge 显示整体下载速度
- 任务完成通知

![](https://github.com/521xueweihan/HelloGitHub/blob/master/08/img/aria2gui-show-min.png)

#### Java 项目
11、[AndroidUtilCode](https://github.com/Blankj/AndroidUtilCode)：Android 开发人员不得不收集的代码，[中文介绍](https://github.com/Blankj/AndroidUtilCode/blob/master/README-CN.md)

12、[DanmakuFlameMaster](https://github.com/Bilibili/DanmakuFlameMaster)：Bilibili 开源的，Android 开源弹幕引擎·烈焰弹幕使，特性：
- 使用多种方式(View/SurfaceView/TextureView)实现高效绘制
- 该站 XML 弹幕格式解析
- 基础弹幕精确还原绘制
- 支持 mode7 特殊弹幕
- 多核机型优化，高效的预缓存机制
- 支持多种显示效果选项实时切换
- 实时弹幕显示支持
- 换行弹幕支持/运动弹幕支持
- 支持自定义字体
- 支持多种弹幕参数设置
- 支持多种方式的弹幕屏蔽

#### 其它
13、[How-To-Ask-Questions-The-Smart-Way](https://github.com/FredWe/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)：提问的智慧，提出一个好的问题是解决问题的关键

14、[jstraining](https://github.com/ruanyf/jstraining)：阮一峰写的全栈工程师培训材料

15、[PTVS](https://github.com/Microsoft/PTVS)：Visual Studio 下的 Python 开发插件

16、[the-swift-programming-language-in-chinese](https://github.com/numbbbbb/the-swift-programming-language-in-chinese)：中文版 Apple 官方 Swift 教程《The Swift Programming Language》

17、[styleguide](https://github.com/fex-team/styleguide)：百度前端研发团队的文档与源码编写风格

18、[weex](https://github.com/alibaba/weex)：移动端，跨平台前端框架，[详细的中文档](https://github.com/weexteam/article/wiki/Weex中文文档)

19、[macOS-Security-and-Privacy-Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide)：MacOS 的安全和隐私指南，[中文翻译版](https://github.com/xitu/macOS-Security-and-Privacy-Guide/blob/master/README-cn.md)
