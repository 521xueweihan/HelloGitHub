# GitHub Bot
>兴趣是最好的老师，[HelloGitHub](https://github.com/521xueweihan/HelloGitHub) 就是帮你找到兴趣！

<p align="center">
    <img src='https://raw.githubusercontent.com/521xueweihan/img/master/hellogithub/01/img/hello-github.jpg' style="max-width:100%;"></img>
</p>

## 运行步骤
这个脚本主要使用收集 GitHub 上优秀的项目，用于编写[《HelloGitHub 月刊》](https://github.com/521xueweihan/HelloGitHub)，后面还会持续开发～

1. 安装依赖：`pip install -r requirements.txt`
2. 配置脚本中相关参数：
	```
	# github帐号
	ACCOUNT = {
	    'username': '',
	    'password': ''
	}

	# 发送邮件，邮箱的信息
	MAIL = {
	    'mail': '',  # 发送邮件的邮箱地址
	    'username': '',
	    'password': '',
	    'host': 'smtp.qq.com',
	    'port': 465
	}

	# 接收邮件的邮箱地址
	RECEIVERS = []
	# qq邮件服务文档：http://service.mail.qq.com/cgi-bin/help?id=28
	```

**最后**：`python github_bot.py`

## 开发日志
#### 2017-4-6
1. GitHub Api 更新，event 最多获取 300 条
2. 新注册帐号 521hellogithub 用于获取每天的数据

#### 2017-3-28
增加收集项目 star 临界值

#### 2016-9-29
- GitHub 今日热点项目不统计自己的项目
- 错误日志放到脚本的同目录下

#### 2016-9-24
实现根据 star 数量，从高到低展示。

#### 2016-9-5
实现请求 GitHub Api 获取关注的用户 star 的项目、过滤内容、定时发邮件

## Todo
1. 获取 explore 页的数据
2. 异步请求获取 star 数
3. 自己项目的数据统计
