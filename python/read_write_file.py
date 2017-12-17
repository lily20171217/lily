#!/usr/bin/env python
"""
文件读、写，的步骤：
    1.打开文件
    2.读/写
    3.关闭文件
UTF-8编码：
建议，文件在磁盘上保存时统一使用UTF-8编码
在内存中，统一使用Unicode编码
"""
import pickle

def 从文件中读数据():
    fp = open("names.txt", "rb")
    #print(fp.read())
    content = fp.readlines()
    print(content)
    for i in content:
        print(i.decode("utf-8").strip())
    fp.close()


def 把数据写入到文件():
    fp = open("地址.txt", "wb")
    address = ["中国", "非洲", "朝鲜"]
    for i in address:
        #fp.write(i.encode("utf-8")+ b'\n')
        fp.write("{}\n".format(i).encode("utf-8"))
    fp.close()


def write_pickle():
    dict1 = {"name": "sam", "age": 16}
    # fp = open("tmp_pickle", 'wb')
    # pickle.dump(dict1, fp)
    # fp.close()

    # 优势：with上下文管理器，自动关闭已经打开的问题
    with open("tmp_pickle", 'wb') as fp:
        pickle.dump(dict1, fp)


def read_pickle():
    fp = open("tmp_pickle", 'rb')
    dict1 = pickle.load(fp)
    print(dict1)
    fp.close()


if __name__ == "__main__":
    #从文件中读数据()
    #把数据写入到文件()
    write_pickle()
    #read_pickle()