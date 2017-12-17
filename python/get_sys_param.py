#!/usr/bin/env python
import sys
import os


def usage():
    print("文件接收2个参数，请重新输入")
    print("eg. python get_sys_param.py sam 1")

if __name__ == "__main__":
    param = sys.argv
    if len(param) != 3:
        usage()
        quit()
    print("{}: {}'s age is {}".format(param[0], param[1], param[2]))
    home_dir = os.getcwd()
    false_dir = r"F:\bbbb"
    print(os.path.isdir(home_dir))
    print(os.path.isdir(false_dir))
    print(sys.path)
    print("=" * 20)
    tmp_file = r"F:\GitHub\FlaskyBlog\migrations\env.py"
    tmp_file2 = r"F:\GitHub\FlaskyBlog\xxxxx\env.py"
    print(os.path.dirname(tmp_file))
    print(os.path.basename(tmp_file))
    print(os.path.exists(tmp_file))