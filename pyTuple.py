tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 不需要括号也可以


def foo():
    print(type(tup1))
    print(type(tup3))
    # 访问
    print(tup1[0])  # Google
    print(tup1[0:1])  # ('Google',)
    print(tup1[0:2])  # ('Google', 'Runoob')
    # 创建一个新的元组
    tempTup = tup1 + tup2
    print(tempTup)  # ('Google', 'Runoob', 1997, 2000, 1, 2, 3, 4, 5)

    tup = ('Google', 'Runoob', 1997, 2000)
    del tup  # 删除数组
    print("删除后的元组 tup : ")
    # print(tup)  # UnboundLocalError: local variable 'tup' referenced before assignment
    # 运算符
    # 计算元素个数
    print(len((1, 2, 3)))  # 3
    # 连接
    print((1, 2, 3) + (4, 5, 6))  # (1, 2, 3, 4, 5, 6)
    # 复制
    print(("hi",) * 4)
    # 元素是否存在
    print(3 in (1, 2, 3))
    # 迭代
    for x in (1, 2, 3):
        print(x)
    # 元素的索引
    print(tup2[1])
    print(tup2[-1])  # 反向读取，读取倒数第二个元素
    print(tup2[1:])  # 截取元素，从第二个开始后的所有元素
    print(tup2[1:4])  # 截取元素，从第二个开始到第四个元素（索引为 3）。
    # 内置函数
    print(len(tup2))
    print(max(tup2))
    print(min(tup2))
    print(tuple(["1", "b", 2]))  # ('1', 'b', 2) 将可迭代系列转换为元组。

    # 不支持修改元素    关于元组是不可变的   所谓元组的不可变指的是元组所指向的内存中的内容不可变。
    # tup2[1] = 100  # TypeError: 'tuple' object does not support item assignment
