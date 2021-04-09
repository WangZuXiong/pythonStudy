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

    aTuple = (1, 2, 3)
    print(aTuple)  # (1, 2, 3)
    aList = list(aTuple)
    print(aList)  # [1, 2, 3]
