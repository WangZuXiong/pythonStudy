# 格式如下所示 d = {key1 : value1, key2 : value2, key3 : value3 }
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}


def foo():
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])
    # 如果用字典里没有的键访问数据，会输出错误如下：
    # print("dict['Alice']: ", dict['Alice']) # KeyError: 'Alice'
    del dict['Name']  # 删除键 'Name'
    print(dict)  # {'Age': 7, 'Class': 'First'}
    dict.clear()  # 清空字典
    # del dict  # 删除字典

    print(len(dict1))  # 1
    print(str(dict1))  # {'abc': 456}
    print(type(dict1))  # <class 'dict'>

    dict11 = {"a": 1}
    dict22 = dict11.copy()  # 深拷贝
    dict33 = dict11  # 浅拷贝
    print(dict22)  # {'a': 1}
    dict11["a"] = 100

    print(dict11)  # {'a': 100}
    print(dict22)  # {'a': 1}
    print(dict33)  # {'a': 100}

    # 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
    print(dict.fromkeys(["name", "sex", "age"]))  # {'name': None, 'sex': None, 'age': None}
    print(dict.fromkeys(["name", "sex", "age"], 100))  # {'name': 100, 'sex': 100, 'age': 100}

    print(dict1.get("abc", 100))  # 456
    print(dict1.get("AAAA", 100))  # 100
    print("AAAA" in dict1)  # False

    tempDict = {"a": 1, "b": 2}
    # 以列表返回可遍历的(键, 值) 元组数组
    items = tempDict.items()
    print(items)  # dict_items([('a', 1), ('b', 2)])
    print(type(items))  # <class 'dict_items'>
    for i, j in items:
        print("key:" + i + " value:" + str(j))  # key:a value:1 key:b value:2

    keys = tempDict.keys()
    print(type(keys))  # <class 'dict_keys'>
    print(keys)  # dict_keys(['a', 'b'])

    values = tempDict.values()
    print(type(values))  # <class 'dict_values'>
    print(values)  # dict_values([1, 2])

    tempDict.setdefault("c", 3)  # 相当于Dict Add
    print(tempDict["c"])  # 3
    print(tempDict)  # {'a': 1, 'b': 2, 'c': 3}

    tempDict2 = {"a": 100, "f": 9999}
    tempDict.update(tempDict2)  # 把字典dict2的键/值对更新到dict里
    print(tempDict)  # {'a': 100, 'b': 2, 'c': 3, 'f': 9999}

    t3 = tempDict.pop("f", -1)
    print(t3)  # 9999
    print(tempDict)  # {'a': 100, 'b': 2, 'c': 3}
    # 	pop(key[,default])
    # 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    t4 = tempDict.pop("g", -1)
    print(t4)  # -1
    print(tempDict)  # {'a': 100, 'b': 2, 'c': 3}

    site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
    pop_obj = site.popitem()
    print(pop_obj)
    print(site)