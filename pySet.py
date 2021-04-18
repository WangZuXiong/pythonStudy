set1 = {'a', 'b'}
set2 = {'a', 'D'}
set3 = {'b', 'D'}


def foo():
    set1.add('c')  # 不是追加到末尾
    set1.add('d')  # 不是追加到末尾
    print(set1)  # {'c', 'd', 'b', 'a'} {'d', 'c', 'b', 'a'}

    t = set1.difference(set2)
    print(t)  # {'b', 'd', 'c'} set1里面有 但是 set2里面没有的元素

    t = set2.difference(set3)
    print(t)

    # y是否包含了x的元素 不包含返回True 包含的话返回True
    x = {1, 2, 3}
    y = {1}
    print(x.isdisjoint(y))

    # x 是否为 y 的子集
    print(x.issubset(y))  # False
    print(y.issubset(x))  # True

    set1.update(set2)  # 合并两个集合，重复元素只会出现一次
    set1.update(set3)
    print(set1)  # {'c', 'a', 'D', 'd', 'b'} 去重了
