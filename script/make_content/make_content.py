#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/10/21 下午1:41
#   Desc    :   HelloGitHub项目——生成月刊脚本
"""
该脚本主要用于：生成月刊

《HelloGitHub》月刊每期内容都遵循统一格式，如果需要对通用部分的内容进行修改，需要手动修改每一
期的内容，这是不优雅的。

所以，我打算写个脚本，用于生成月刊，这样如果修改了通用内容部分，就只需要重新生成月刊，而不需要
手动修改已发布的所有期的内容。
"""
import sys
import os

CONTENT_FLAG = '{{ hello_github_content }}'
NUM_FLAG = '{{ hello_github_num }}'


class InputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


def check_path(input_path):
    """
    检查输入的路径是否存在
    """
    for fi_input in input_path[:-1]:
        if not os.path.exists(fi_input):
            error_message = 'Path: ' + fi_input + ', not exists.'
            raise InputError(error_message)


def get_args():
    """
    检查输入的参数是否合法
    """
    input_list = sys.argv

    if len(input_list) < 2:
        raise InputError('Input error: need args')
    elif len(input_list) != 4:
        raise InputError('Input error: just need 3 args')
    else:
        check_path(input_list)
    return input_list[1:]


def read_file(input_path):
    with open(input_path, 'r') as fb:
        return fb.read()


def write_file(output_path, output_data):
    with open(output_path, 'w') as fb:
        fb.write(output_data)


def make_content(input_args):
    temple_path = input_args[0]
    content_path = input_args[1]
    num = input_args[2]
    if len(num) == 1:
        num = '0' + num

    temple_data = read_file(temple_path).replace(NUM_FLAG, num)
    content_path = read_file(content_path)

    output_data = temple_data.replace(CONTENT_FLAG, content_path)

    write_file(os.path.join(os.path.abspath(os.curdir), 'HelloGitHub{num}.md'.format(num=num)), output_data)

if __name__ == '__main__':
    args = get_args()
    make_content(args)
    print os.path.abspath(os.curdir)
