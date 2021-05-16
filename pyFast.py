from collections import Counter
from copy import deepcopy
import re


# 字符元素组成判定  检查两个字符串的组成元素是不是一样的
def anagram(first, second):
    print(Counter(first))
    print(Counter(second))
    return Counter(first) == Counter(second)


from math import ceil


# 分块 给定具体的大小，定义一个函数以按照这个大小切割列表。
def chunk(lst, size):
    return list(map(lambda x: lst[x * size:x * size + size], list(range(0, ceil(len(lst) / size)))))


def split_list(raw_list, count):
    # t = raw_list[0]
    # for i in range(21):
    #     raw_list.append(t)
    result = []
    group_index = -1
    length = len(raw_list)
    for index in range(length):
        data = raw_list[index]
        if index % count == 0:
            group = []
            result.append(group)
            group_index += 1
        result[group_index].append(data)
    return result


def zip_test():
    lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]  # [[1, "a"], [2, "b"], [3, "c"]]
    transposed = zip(*lst)

    for item in transposed:  # 是一个迭代器对象
        print(item)

    print(list(transposed))  # [('a', 'c', 'e'), ('b', 'd', 'f')]

    print(range(3))  # range(0, 3)
    print(range(4))
    print(list(zip(range(3), range(4))))  # [(0, 0), (1, 1), (2, 2)]
    # 将n序列

    key = ["x", "y"]
    value = [100, 300]
    temp_dict = dict(zip(key, value))
    print(temp_dict)


def str_combin():
    int_lst = [1, 2, 3, 4]
    # print(",".join(int_lst))#TypeError: sequence item 0: expected str instance, int found

    str_lst = ["1", "2", "3"]
    print(",".join(str_lst))  # 1,2,3


def re_find_all():
    t = re.findall(r'[abc]', "1A2a1啊2abc", re.IGNORECASE)  # 没有区分大小写
    print(t)  # ['A', 'a', 'a', 'b', 'c']


def max_test():
    lst = [1, 1, 1, 2, 3, 4]
    # list 里面出现频率最多的元素
    t = max(set(lst), key=lst.count)
    print(t)  # 1


def deepcopy_test():
    lst = [1, 2, 3]
    lst1 = lst
    lst2 = deepcopy(lst)

    lst[0] = 100
    print(lst1)  # [100, 2, 3]
    print(lst2)  # [1, 2, 3]

    lst = [9, 9, 9]
    print(lst1)  # [100, 2, 3]
    print(lst2)  # [1, 2, 3]

    lst1 = [6, 6, 6]
    print(lst)  # [9, 9, 9]
    print(lst2)  # [1, 2, 3]


def isinstance_test():
    lst = [(1, 2, 3), [4, 5, 6]]
    result = []
    for t in lst:
        if isinstance(t, list):
            result.extend(t)

    print(result)  # [4, 5, 6]  tuple is not list instance
