from typing import Generator


def foo():
    # 列表
    lst = [x * x for x in (range(0, 10))]
    print(lst)
    print(type(lst))  # <class 'list'>

    # 创建生成器，方法1
    g: Generator = (x * x for x in (range(0, 10)))
    print(type(g))  # <class 'generator'>

    # 调用方式1
    print(next(g))  # 0
    # 调用方式2
    print(g.__next__())  # 1
    # 调用方式3
    for elem in g:
        print(elem, end=" ")

    print()
    print("------------------")

    # 创建生成器，方法2
    g3 = make_generator()  # 函数中用到了yield，该函数会变为生成器
    print(type(g3))  # <class 'generator'>

    for elem in g3:
        print(elem)

    print("------------------")

    g4 = fib(10)
    for elem in g4:
        print(elem, end=" ")

    print()
    print("------------------")
    # send 的

    def fun():
        r = 1
        while True:
            r += 1

            temp = yield r
            print(f"r = {r}")
            print(f"r = {temp}")

    g5 = fun()

    print(next(g5))
    print(g5.send(100))
    # print(next(g5))
    # print(next(g5))




def make_generator():
    """如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator"""
    print("执行到1")
    yield 1
    print("执行到2")
    yield 2
    print("执行到3")
    yield


"""
    generator 和函数的执行流程不一样，
    函数是顺序执行，遇到return语句或者最后一行函数语句就返回
    变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
