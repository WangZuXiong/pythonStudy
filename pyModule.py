import sys

vara = 100
_varb = 999


def foo():
    for i in sys.argv:
        print(i)

    print(sys.path)


def name_test():
    print(__name__)  # pyModule

    if __name__ == "__main__":
        print("程序自身在运行")
    else:
        print("我来自另一个模块")


def name_test_inside():
    name_test()
