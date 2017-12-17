#!/usr/bin/env python

# 代码作用域
c = "hello"  # 全局变量

# 定义一个函数
def print_some():
    """DocString 表明函数的目的或功能"""
    print("hello world")
    print("bye bye world")
    print("bye bye again")


# 强制规则：如果参数有默认值，必须在没有默认值后面
def say_hello(name, age=16):
    """接受一个参数，然后输出hello, name"""
    print("hello {}!, age is {}".format(name, age))
    return True


def get_sum(x, y):
    """c 是一个局部变量"""
    global c
    c = x + y
    return c


def print_var_params(var1, *var_args, **kw_args):
    """接受可变参数"""
    print(var1)
    for i in var_args:
        print(i)

    for i in kw_args.keys():
        print("{}'s value is {}".format(i, kw_args[i]))


# 建议每一个函数都有main，有且仅有一个。
# 用途：测试你的代码
if __name__ == "__main__":
    """入口函数，执行py文件的时候，python解释器会自动去寻找有没有main函数"""
    # 调用函数
    print(print_some())
    print(print_some())
    print(say_hello("张三", 18))
    print(say_hello("lisi"))
    print(get_sum(3, 5))
    print(c)
    print_var_params(10)
    print_var_params(10, 50, 60, 70, name="sam", age=16)