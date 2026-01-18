#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import re
import json
import requests

def get_issue_number(content):
    match = re.search(r'# 《HelloGitHub》第 (\d+) 期', content)
    if match:
        return match.group(1)
    return None

def send_feishu_notification(title, issue_num):
    webhook_url = os.environ.get('FEISHU_WEBHOOK_URL')
    if not webhook_url:
        print("Error: FEISHU_WEBHOOK_URL environment variable not set.")
        return

    # Construct the link
    link = "https://hellogithub.com/periodical/volume/{}".format(issue_num)
    
    # Feishu Post Message Content
    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": title,
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": "感兴趣是最好的老师，HelloGitHub 让你对开源感兴趣！\n\n"
                            },
                            {
                                "tag": "a",
                                "text": "点击查看本期内容",
                                "href": link
                            }
                        ]
                    ]
                }
            }
        }
    }

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        result = response.json()
        if result.get("code") == 0:
            print("Successfully sent notification to Feishu.")
        else:
            print("Failed to send notification: {}".format(result))
    except Exception as e:
        print("Error sending request: {}".format(e))

def main():
    if len(sys.argv) < 2:
        print("Usage: python notify_feishu.py <markdown_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("File not found: {}".format(file_path))
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    issue_num = get_issue_number(content)
    if not issue_num:
        print("Could not extract issue number from file.")
        # Fallback: try to guess from filename if content regex fails
        basename = os.path.basename(file_path)
        match = re.search(r'HelloGitHub(\d+).md', basename)
        if match:
            issue_num = match.group(1)
        else:
            print("Could not determine issue number. Exiting.")
            sys.exit(1)

    title = "HelloGitHub 第 {} 期发布".format(issue_num)
    send_feishu_notification(title, issue_num)

if __name__ == '__main__':
    main()
