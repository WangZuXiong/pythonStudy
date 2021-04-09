list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']


def foo():
    count = 4
    for i in range(count):
        print("index = {0}, value = {1}".format(i, list1[i]))
        print("index = {0}, value = {1}".format(i - count, list1[i - count]))
        print("------")
    # print(list1[4]) # IndexError: list index out of range

    print(len(list1))  # 4
    # print(max(list1))  # TypeError: '>' not supported between instances of 'int' and 'str'
    print(max(list2))  # 5
    print(min(list2))  # 5

    # 序列转List
    aTuple = (1, 2, 3)
    print(aTuple)  # (1, 2, 3)
    aList = list(aTuple)
    print(aList)  # [1, 2, 3]

    # list追加   追加一个object  占一个位置
    print(list1)  # ['Google', 'Runoob', 1997, 2000]
    list1.append(1)
    print(list1)  # ['Google', 'Runoob', 1997, 2000, 1]
    list1.append(aTuple)
    print(list1)  # ['Google', 'Runoob', 1997, 2000, 1, (1, 2, 3)]
    list1.append(aList)
    print(list1)  # ['Google', 'Runoob', 1997, 2000, 1, (1, 2, 3), [1, 2, 3]]

    list2.append(aList)  # [1, 2, 3, 4, 5, [1, 2, 3]]
    print(list2)

    # 在list末尾一次性追加序列中的多个值
    aList.extend(aList)
    print(aList)  # [1, 2, 3, 1, 2, 3]

    # 统计某个元素在列表中出现的次数
    count = list3.count("a")
    print(count)  # 1

    index = list3.index("a")
    print(index)  # 0
    # index = list3.index("f")    # ValueError: 'f' is not in list 找不到的话抛出异常
    # print(index)

    # 插入对象
    print(list3)  # ['a', 'b', 'c', 'd']
    list3.insert(0, "0")
    print(list3)  # ['0', 'a', 'b', 'c', 'd']

    # 弹出指定index元素，默认弹出最后一个元素
    print(list3.pop())  # d
    print(list3)  # ['0', 'a', 'b', 'c']
    print(list3.pop(0))  # 0
    print(list3)  # ['a', 'b', 'c']

    # 移除指定的元素 参数为value 不是value的index
    print(list3)  # ['a', 'b', 'c']
    list3.remove("a")
    print(list3)  # ['b', 'c']

    # 反向列表中的元素
    list3.reverse()
    print(list3)  # ['c', 'b']

    aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
    aList.sort()
    print(aList)  # ['Facebook', 'Google', 'Runoob', 'Taobao']

    vowels = ['e', 'a', 'u', 'o', 'i']
    vowels.sort(reverse=True)  # 降序
    print(vowels)  # ['u', 'o', 'i', 'e', 'a']

    random = [(2, 2), (3, 4), (4, 1), (1, 3)]

    # 获取列表的第二个元素
    def takeSecond(elem):
        return elem[1]

    random.sort(key=takeSecond)
    print(random)  # [(4, 1), (2, 2), (1, 3), (3, 4)]

    random.clear()
    print(random)  # []

    list11 = [1, 2, 3]
    list22 = list11.copy()
    print(list22)
    list22[0] = 100
    print("list 22 :")
    print(list22)  # [100, 2, 3]
    print("list 11 :")
    print(list11)  # [1, 2, 3]
    # 修改list22 不会导致 list11被修改  应该是深拷贝
    # 浅拷贝只复制指向某个对象的指针，而不复制对象本身，新旧对象还是共享同一块内存。但深拷贝会另外创造一个一模一样的对象，新对象跟原对象不共享内存，修改新对象不会改到原对象。
