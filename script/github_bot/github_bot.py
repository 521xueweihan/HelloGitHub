#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/8/30 下午10:43
#   Desc    :   Github Bot
import os
import logging
import smtplib
import datetime
from operator import itemgetter
from email.mime.text import MIMEText
from email.header import Header

import requests

logging.basicConfig(
    level=logging.WARNING,
    filename=os.path.join(os.path.dirname(__file__), 'bot_log.txt'),
    filemode='a',
    format='%(name)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
)
logger = logging.getLogger('Bot')  # 设置log名称
# github帐号
ACCOUNT = {
    'username': '',
    'password': ''
}

API = {
    'events': 'https://api.github.com/users/{username}/received_events'.format(username=ACCOUNT['username'])
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

# 几天前
DAY = 1

# 项目stars临界值
STARS = 100

# qq邮件服务文档：http://service.mail.qq.com/cgi-bin/help?id=28


CONTENT_FORMAT = """
    <table border="2" align="center">
      <tr>
        <th>头像</th>
        <th>用户名</th>
        <th>项目名</th>
        <th>starred 日期</th>
        <th>项目 star 数量</th>
      </tr>
      {project_info_string}
    </table>
"""


def get_data(page=1):
    """
    从目标源获取数据
    https://developer.github.com/v3/activity/events/
    GitHub 规定：默认每页 30 条，最多 300 条目
    """

    args = '?page={page}'.format(page=page)

    response = requests.get(API['events']+args,
                            auth=(ACCOUNT['username'], ACCOUNT['password']))
    status_code = response.status_code
    if status_code == 200:
        resp_json = response.json()
        return resp_json
    else:
        logging.error('请求 event api 失败：', status_code)
        return []


def get_all_data():
    """
    获取全部 300 条的数据
    https://developer.github.com/v3/activity/events/
    GitHub 规定：默认每页 30 条，最多 300 条目
    """
    all_data_list = []
    for i in range(10):
        response_json = get_data(i+1)
        if response_json:
            all_data_list.extend(response_json)
    return all_data_list


def check_condition(data):
    """
    过滤条件
    """
    create_time = datetime.datetime.strptime(
        data['created_at'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=8)
    date_condition = create_time >= (datetime.datetime.now()
                                     - datetime.timedelta(days=DAY))
    if (data['type'] == 'WatchEvent') and date_condition:
        # 不统计自己项目的star事件
        if data['payload']['action'] == 'started' and \
           ACCOUNT['username'] not in data['repo']['name']:
            data['date_time'] = create_time.strftime("%Y-%m-%d %H:%M:%S")
            return True
    else:
        return False


def analyze(json_data):
    """
    分析获取的数据
    :return 符合过滤条件的数据
    """
    result_data = []
    for fi_data in json_data:
        if check_condition(fi_data):
            result_data.append(fi_data)
    return result_data


def get_stars(data):
    """
    获取stars数量，同时过滤掉stars数量少的项目
    """
    project_info_list = []
    for fi_data in data:
        project_info = dict()
        project_info['user'] = fi_data['actor']['login']
        project_info['user_url'] = 'https://github.com/' + project_info['user']
        project_info['avatar_url'] = fi_data['actor']['avatar_url']
        project_info['repo_name'] = fi_data['repo']['name']
        project_info['repo_url'] = 'https://github.com/' + project_info['repo_name']
        project_info['date_time'] = fi_data['date_time']
        try:
            repo_stars = requests.get(fi_data['repo']['url'], timeout=2).json()
            if repo_stars:
                project_info['repo_stars'] = int(repo_stars['stargazers_count'])
            else:
                project_info['repo_stars'] = -1
        except Exception as e:
            project_info['repo_stars'] = -1
            logger.warning(u'获取：{} 项目星数失败——{}'.format(
                project_info['repo_name'], e))
        finally:
            if project_info['repo_stars'] >= STARS or project_info['repo_stars'] == -1:
                # 过滤掉star数量低于临界值的项目
                project_info_list.append(project_info)
    project_info_list = sorted(project_info_list, key=itemgetter('repo_stars'), reverse=True)
    return project_info_list


def make_content():
    """
    生成发布邮件的内容
    """
    json_data = get_all_data()
    data = analyze(json_data)
    content = []
    project_info_list = get_stars(data)
    for project_info in project_info_list:
        project_info_string = """<tr>
                                <td><img src={avatar_url} width=32px></img></td>
                                <td><a href={user_url}>{user}</a></td>
                                <td><a href={repo_url}>{repo_name}</a></td>
                                <td>{date_time}</td>
                                <td>{repo_stars}</td>
                              </tr>
                           """.format(**project_info)
        content.append(project_info_string)
    return content


def send_email(receivers, email_content):
    """
    发送邮件
    """
    sender = MAIL['mail']  # 发送邮件的邮箱
    receivers = receivers   # 接收邮件的邮箱，可设置多个

    # 三个参数：第一个为文本内容，第二个 html 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(
        CONTENT_FORMAT.format(project_info_string=''.join(email_content)),
        'html', 'utf-8'
    )
    message['From'] = Header(u'GitHub 机器人', 'utf-8')
    message['To'] = Header(u'削微寒', 'utf-8')

    subject = u'今日 GitHub 热点'  # 设置邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtp_obj = smtplib.SMTP_SSL()  # qq邮箱要求是https连接，所以需要用SMTP_SSL
        smtp_obj.connect(MAIL['host'], MAIL['port'])    # 设置SMTP地址和端口号
        smtp_obj.login(MAIL['username'], MAIL['password'])
        smtp_obj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException as e:
        logger.error(u"无法发送邮件: {}".format(e))

if __name__ == '__main__':
    content = make_content()
    send_email(RECEIVERS, content)
