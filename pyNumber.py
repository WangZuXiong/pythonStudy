import random


def foo():
    randomFunction()


# 随机数函数
def randomFunction():
    # 从序列中随机一个函数
    t = random.choice(range(10))
    print(t)
    t1 = random.choice([1, 2, 3])
    print(t1)

    #
    print("-----")
    print(random.randrange(1, 10, 2))  # 7 7 9 3 3 1 3 7 9 1 9 9 每次变化都是2  n = 1 + x * 2
    print(random.randrange(1, 10, 1))

    # 随机生成下一个实数，它在[0,1)范围内。
    print(random.random())

    # 用随机种子生成随机数
    print("-----")
    print(random.random())  # 0.8903395469432293    0.042077788452625664    0.4026985325184388
    random.seed(10, 1)  # 指定随机种子
    print(random.random())  # 0.5714025946899135    0.5714025946899135  0.5714025946899135  重启IDE之后也是一样的
    random.seed(10, 1)  # 指定随机种子
    print(random.random())  # 0.5714025946899135    0.5714025946899135  0.5714025946899135
    random.seed(10, 2)  # 指定随机种子 版本2
    print(random.random())  # 0.5714025946899135    0.5714025946899135  0.5714025946899135
    random.seed(10, 2)  # 指定随机种子 版本2
    print(random.random())  # 0.5714025946899135    0.5714025946899135  0.5714025946899135

    # 将序列的所有元素随机排序
    print("-----")
    l1 = [1, 2, 3]
    random.shuffle(l1)
    print(l1)  # [1, 3, 2]
    random.shuffle(l1)
    print(l1)  # [3, 1, 2]

# 三角函数
# 数学常量
