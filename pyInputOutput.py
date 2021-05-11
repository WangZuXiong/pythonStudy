import math
import pickle
import sys


def str_and_repr():
    print(str("1\n23"))
    '''
    1
    23
    '''
    print(repr("1\n23"))
    '''
    '1\n23'
    '''


def output_format_test():
    '''

    这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。

    还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。

    另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：
    '''
    for i in range(1, 10):
        print(repr(i).rjust(2), repr(i * i).rjust(3), repr(i * i * i).rjust(4))

    for i in range(1, 10):
        print("{0:2d} {1:3d} {2:4d}".format(i, i * i, i * i * i))

    print(math.pi)  # 3.141592653589793
    print("{0:.3f}".format(math.pi))  # 3.142


def inoput_test():
    str = input("请输入：")
    print(str)


def write_file():
    print(sys.path)
    # 将字符串写入本地文本·
    file = sys.path[0] + "/file.txt"
    mode = "w"
    f = open(file, mode)
    num = f.write("py input test")
    print("写入的字符数：{NUM}".format(NUM=num))
    f.close()  # 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。

    # 从本地文本中读取文本
    mode = "r"
    f = open(file, mode)
    temp = f.read()
    f.close()
    print(temp)


def pickle_test():
    # 序列化
    obj = {"x": 100, "name": "wzx"}
    file = sys.path[0] + "/file.txt"
    mode = "wb"
    f = open(file, mode)
    pickle.dump(obj, f, -1)
    f.close()
    # 反序列化
    mode = "rb"
    f = open(file, mode)
    data = pickle.load(f)
    print(data)
    f.close()
