# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import pyCoding
import pyDataStructure
import pyDictionary
import pyFunction
import pyIter
import pyList
import pyLoop

import pyNumber
import pySet
import pyString
import pyTuple


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。
    print("打印字符串： %s " % name)
    print("打印字符串： {} ".format(name))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pass
    # pyNumber.foo()
    # pyString.foo()
    # print_hi('PyCharm')
    # pyList.foo()
    # pyTuple.foo()
    # pyDictionary.foo()
    # pySet.foo()
    # pyCoding.foo()
    # pyLoop.foo()
    # pyIter.foo()
    # print(pyLoop.__a)
    # 查看py预定义的变量
    # import builtins
    # print(dir(builtins))

    # a = 100
    # print(id(a))  # 140716032267008
    # pyFunction.change(a)
    # tempList = [2, 3, 4]
    # pyFunction.changeMutable(tempList)  # 传递可变对象
    # print(tempList)  # [2, 3, 4, 1]
    # pyFunction.printVector2(1, 2)  # x=1,y=2
    # pyFunction.printVector2(y=2, x=1)  # x=1,y=2
    # pyFunction.printInfo(1, 2, 3, 4)
    # pyFunction.printInfo2(arg1=100, arg2=200.0) # {'arg1': 100, 'arg2': 200.0}
    # pyFunction.lambdaFunction()

    # pyDataStructure.stack_test()
    # pyDataStructure.queue_test()
    # pyDataStructure.sorted_test()
    # pyDataStructure.del_test()

    # import pyModule
    # pyModule.foo()
    from pyModule import *

    print(vara)  # 100
    # print(_varb)  # NameError: name '_varb' is not defined    这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例
    name_test()  # 我来自另一个模块

    name_test_inside()  # 我来自另一个模块

    print(__name__ == "__main__")  # True

    print(dir(sys))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
