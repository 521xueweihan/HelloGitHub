"""
该脚本主要用于：生成月刊

《HelloGitHub》月刊每期内容都遵循统一格式，如果需要对通用部分的内容进行修改，需要手动修改每一
期的内容，这是不优雅的。

所以，我打算写个脚本，用于生成月刊，这样如果修改了通用内容部分，就只需要重新生成月刊，而不需要
手动修改已发布的所有期的内容。
"""
from __future__ import print_function
import sys
import os
CONTENT_FLAG = '{{ hello_github_content }}'
NUM_FLAG = '{{ hello_github_num }}'

class InputError(Exception):

    def __init__(self, message):
        """Process data using __init__ with arguments message."""
        self.message = message

    def __str__(self):
        """Implement the __str__ operation on provided input: no arguments."""
        return repr(self.message)

def check_path(path):
    """
    检查路径是否存在
    """
    if not os.path.exists(path):
        print('not exist: {path}'.format(path=path))
        return False
    else:
        return True

def read_file(input_path):
    """Implement the read_file operation on provided input: input_path."""
    with open(input_path, 'r') as fb:
        return fb.read()

def write_file(output_path, output_data):
    """Process data using write_file with arguments output_path, output_data."""
    with open(output_path, 'w') as fb:
        fb.write(output_data)

def make_content(num):
    """Calculate and return the output of make_content based on num."""
    template_path = os.path.join(os.path.abspath(os.curdir), 'template.md')
    output_path = os.path.join(os.path.abspath(os.curdir), num)
    content_path = os.path.join(output_path, 'content' + num + '.md')
    if not (check_path(content_path) and check_path(template_path)):
        return None
    temple_data = read_file(template_path).replace(NUM_FLAG, num)
    content_data = read_file(content_path)
    output_data = temple_data.replace(CONTENT_FLAG, content_data)
    write_file(os.path.join(output_path, 'HelloGitHub{num}.md'.format(num=num)), output_data)
    print('Make 《GitHub月刊{num}》 successful！'.format(num=num))

def make_all_content():
    """Implement the make_all_content operation on provided input: no arguments."""
    dir_list = os.listdir(os.path.abspath(os.curdir))
    for fi_dir in dir_list:
        if os.path.isdir(fi_dir) and 'script' not in fi_dir:
            make_content(fi_dir)

def main():
    """
    入口方法
    """
    input_list = sys.argv
    if len(input_list) != 2:
        raise InputError('Input error: Need a param')
    else:
        try:
            input_arg = input_list[1]
        except Exception:
            raise InputError('Input error: Must be number')
    if len(input_arg) == 1:
        make_content('0' + input_arg)
    elif input_arg == 'all':
        make_all_content()
    else:
        make_content(input_arg)
if __name__ == '__main__':
    main()