import sys


def foo():
    # test_function()
    test_function2()
    return
    list1 = [1, 2, 3]
    for item in list1:
        print(item)

    iter1 = iter(list1)  # 创建迭代器
    print(next(iter1))  # 输出迭代器的下一个对象   1
    # for item in iter1:
    #     print(item)
    print(type(list1))  # <class 'list'>
    print(type(iter1))  # <class 'list_iterator'>

    while True:
        try:
            print(next(iter1))  # 2  3
        except StopIteration:
            sys.exit()


# 创建一个迭代器
class MyNumber:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        self.a = 1
        return self.a

    def __next__(self):
        if self.a < 10:
            self.a = self.a + 1
            return self.a
        else:
            raise StopIteration  # 防止出现无限循环的情况


def test_function():
    myNumber: MyNumber = MyNumber()
    while True:
        try:
            print(next(myNumber))
        except StopIteration:
            sys.exit()


# 创建一个生成器
def fibonacci(n):
    a, b, count = 0, 1, 0
    while True:
        if count > n:
            return
        yield a
        a, b = b, a + b
        count += 1


def test_function2():
    f = fibonacci(10)  # f是一个迭代器 是由生成器返回生成的
    while True:
        try:
            print(next(f))
        except StopIteration:
            sys.exit()
