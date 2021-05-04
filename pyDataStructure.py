from collections import deque


# 将列表当作堆栈使用
def stack_test():
    stack = [1, 2, 3]
    stack.append(4)
    stack.append(5)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())


# 将列表当作队列使用
def queue_test():
    queue = deque([1, 2, 3])
    queue.append(4)
    queue.append(5)
    print(queue)
    print(queue.popleft())
    print(queue)
    print(queue.popleft())


def sorted_test():
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

    for f in sorted(set(basket)):  # 会排序
        print(f, end=",")
    print("\n")
    for f in set(basket):
        print(f, end=",")


def del_test():
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    print(len(a))  # 6
    del a[0]
    print(len(a))  # 5
    print(a)  # [1, 66.25, 333, 333, 1234.5]
    del a[0:2]
    print(a)  # [333, 333, 1234.5]
    del a[:]
    print(a)  # []
    del a
    # print(a) # UnboundLocalError: local variable 'a' referenced before assignment
