#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import re
import time
import requests

def get_issue_number(content):
    match = re.search(r'# 《HelloGitHub》第 (\d+) 期', content)
    if match:
        return match.group(1)
    return None

def parse_markdown(content):
    """
    Parses the markdown content into a structured format.
    Returns a list of categories, where each category has a title and a list of items.
    Structure: [{'title': 'C 项目', 'items': [{'name': '...', 'url': '...', 'desc': '...'}]}]
    """
    lines = content.split('\n')
    categories = []
    current_category = None
    
    # Regex for project items: "1、[Name](Url)：Description" or "1、[Name](Url): Description"
    # Handles potential slight variations in punctuation
    item_pattern = re.compile(r'^\d+、\[(.*?)\]\((.*?)\)(?:：|:)(.*)')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('### '):
            # Save previous category if exists
            if current_category:
                categories.append(current_category)
            
            # Start new category
            category_title = line.replace('###', '').strip()
            current_category = {'title': category_title, 'items': []}
        
        elif current_category is not None:
            # Check if line is a project item
            match = item_pattern.match(line)
            if match:
                name, url, desc = match.groups()
                current_category['items'].append({
                    'name': name.strip(),
                    'url': url.strip(),
                    'desc': desc.strip()
                })
            # Note: We ignore other text (like images or long descriptions) for simplicity 
            # to keep the notification clean and within size limits.

    # Append the last category
    if current_category:
        categories.append(current_category)
        
    return categories

def send_feishu_msg(title, content_lines):
    webhook_url = os.environ.get('FEISHU_WEBHOOK_URL')
    if not webhook_url:
        print("Error: FEISHU_WEBHOOK_URL environment variable not set.")
        return False

    # Construct the post content
    # Feishu Post structure: [[{tag: text, text: ...}, {tag: a, ...}]]
    post_content = []
    
    for line_data in content_lines:
        if line_data['type'] == 'text':
             post_content.append([{
                 'tag': 'text',
                 'text': line_data['text']
             }])
        elif line_data['type'] == 'link_item':
            # Format: [Name](Url): Desc
            # We want it to look like: "Name: Desc" where Name is a link
            post_content.append([
                {
                    'tag': 'text',
                    'text': "• "
                },
                {
                    'tag': 'a',
                    'text': line_data['name'],
                    'href': line_data['url']
                },
                {
                    'tag': 'text',
                    'text': "：{}".format(line_data['desc'])
                }
            ])

    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": title,
                    "content": post_content
                }
            }
        }
    }

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        result = response.json()
        if result.get("code") == 0:
            print("Successfully sent chunk: {}".format(title))
            return True
        else:
            print("Failed to send chunk {}: {}".format(title, result))
            return False
    except Exception as e:
        print("Error sending request for {}: {}".format(title, e))
        return False

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
        # Fallback to filename
        basename = os.path.basename(file_path)
        match = re.search(r'HelloGitHub(\d+).md', basename)
        if match:
            issue_num = match.group(1)
        else:
            issue_num = "Update"

    categories = parse_markdown(content)
    
    if not categories:
        print("No categories found to notify.")
        return

    # Send Intro Message
    intro_title = "HelloGitHub 第 {} 期发布".format(issue_num)
    intro_lines = [{'type': 'text', 'text': "本期内容如下："}]
    send_feishu_msg(intro_title, intro_lines)
    
    # Send Each Category as a separate message
    for cat in categories:
        cat_title = "HG Vol.{} - {}".format(issue_num, cat['title'])
        cat_lines = []
        for item in cat['items']:
            cat_lines.append({
                'type': 'link_item',
                'name': item['name'],
                'url': item['url'],
                'desc': item['desc']
            })
        
        if cat_lines:
            send_feishu_msg(cat_title, cat_lines)
            # Sleep briefly to avoid rate limits
            time.sleep(1)

if __name__ == '__main__':
    main()
