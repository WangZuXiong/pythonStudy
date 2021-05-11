def foo():
    while True:
        try:
            print("执行代码")
            x = int(input("请输入一个数字"))
            # break
        except RuntimeError:
            print("RuntimeError")
        except ValueError:
            print("ValueError")
        except OSError as osError:
            print(osError)
        except:
            print("发生异常的时候执行的代码")
            print("输入的不是数字 再次重新输入")
        else:
            print("没有异常的时候执行的代码")
        finally:
            print("不论有没有异常都会执行的代码")


def Raise_Test():
    if True:
        raise Exception("抛出异常")