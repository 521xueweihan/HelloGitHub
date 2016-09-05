# Github Bot
>兴趣是最好的老师，[《HelloGithub》](https://github.com/521xueweihan/HelloGithub)就是帮你找到兴趣！

![](https://github.com/521xueweihan/HelloGithub/blob/master/01/img/hello-github.jpg)

这个脚本主要使用收集Github上优秀的项目，用于编写[《HelloGithub月刊》](https://github.com/521xueweihan/HelloGithub)，后面还会持续开发～

## 运行步骤
1. 安装依赖：`pip install -r requirements.txt`
2. 配置脚本中相关参数：
	```
	API = {
	    'events': 'https://api.github.com/users/你的github用户名/received_events/public'
	}

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

**最后：**`python github_bot.py`

## 开发日志

#### 2016-9-5
实现请求Github api获取关注的用户star的项目、过滤内容、定时发邮件

Todo：

1. 获取explore页的数据
2. 异步请求获取star数
