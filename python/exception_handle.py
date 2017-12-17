#!/usr/bin/env python
import sys

try:# 试一试下面的代码，如果发生异常，就走异常处理程序
    f = open('myfile.txt')
    s = f.readline()
    print(s)
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except Exception:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    print("Goodbye")