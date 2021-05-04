def change(a):
    print(id(a))  # 140716032267008 和实参其实指向的是同一个对象
    a = 0
    print(id(a))  # 140716032263808 一个新的对象


# 可更改(mutable)与不可更改(immutable)对象

def changeMutable(list1):
    list1.append(1)


def printVector2(x, y):
    print("x={0},y={1}".format(x, y))


# 不定长参数
def printInfo(*vartuple):
    for var in vartuple:
        print(var)


# 加两个*  参数会以字典的形式导入
def printInfo2(**kwargs):
    print(kwargs)


# 匿名函数
def lambdaFunction():
    sum = lambda a, b: a + b
    print(sum(1, 3))
