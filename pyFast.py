from collections import Counter


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
