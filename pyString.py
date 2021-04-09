def foo():
    #  python三引号允许一个字符串跨多行
    print("""
    string1
        string 2
    """)
    StringFunction()


def StringFunction():
    # 首字母转为大写
    print("aa".capitalize())
    # 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
    print("A".center(11, '>'))
    # 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    print("ABa".count("A"))  # 1
    print("ABa".count("A", 1, 10))  # 0
    print("ABa".count("A", 1, 2))  # 0
    # decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
    print("----")
    # 编码
    str_utf8 = "a汉字123".encode('UTF-8')
    str_gbk = "a汉字123".encode('GBK');
    print(str_utf8)  # b'a\xe6\xb1\x89\xe5\xad\x97123'
    print(str_gbk)  # b'a\xba\xba\xd7\xd6123'
    # 解码
    print(str_utf8.decode("UTF-8"))  # a汉字123
    print(str_gbk.decode("GBK"))  # a汉字123
    print("----")
    print("123".endswith("3"))  # True
    print("123".endswith("2"))  # False
    print("123".endswith("2", 0, 2))  # True
    print("----")
    print("123\t12".expandtabs(3))  # tab符号\t   转化为 3个空格
    print("----")
    tempStr: str = "abca"
    print(tempStr.find("a"))  # 0
    print(tempStr.find("d"))  # -1 查找不到的话返回-1
    print(tempStr.find("a", 1))  # 3  从下标1开始查找
    print("----")
    print(tempStr.index("a"))  # 0
    # print(tempStr.index("d"))  # -1 查找不到的话 抛出异常
    print(tempStr.index("a", 1))  # 3  从下标1开始查找
    print("----")
    # 方法检测字符串是否由字母和数字组成。
    print("aaa".isalnum())  # True
    print("aaa".isalnum())
    # 字符串是否标题化
    print("This Is Title".istitle())
    print("this is Title".istitle())
    # 字符串的拼接
    seq = ("a", "b", "c")
    print("+".join(seq))
    # 字符串的长度
    print(len("123"))

    print("**".ljust(5, "-"))
    print("**".rjust(5, "-"))
    print("**".zfill(5))  # 用0来填充

    print("   abc".lstrip())  # abc
    print("QQQabc".lstrip("Q"))  # abc

    # 两个字符串的长度必须相同，为一一对应的关系。
    intab = "abc"
    outtab = "123"
    trantab = str.maketrans(intab, outtab)
    rawStr = "abcde"
    print(rawStr.translate(trantab))  # 123de

    print(max("abcABC"))  # c
    print(min("abcABC"))  # A

    print("aaabbb".replace("a", "A"))  # AAAbbb
    print("aaabbb".replace("a", "A", 1))  # Aaabbb

    # TODO
    print("this is really a string example....wow!!!".rfind("is"))  # 5
    print("aaa is a".rfind("aaa"))  # 0

    # 截取字符串 num：截取的次数
    print("a b c".split(" "))  # ['a', 'b', 'c']
    print("a b c".split(" ", 1))  # ['a', 'b c']
    print("a b c".split(" ", 2))  # ['a', 'b', 'c']

    str1 = """123
    456 789"""

    print(str1.splitlines())  # ['123', '    456 789']
    print(str1.splitlines(True))  # ['123\n', '    456 789']
    print(str1.startswith("1"))  # True
    print("aaa  bbb ccc".title())  # Aaa  Bbb Ccc
