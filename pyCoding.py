import random


def foo():
    # input_function()
    guess_game()


def guess_game():
    target_num = random.randint(0, 1000)
    temp_num = -1
    while temp_num != target_num:
        temp_num = int(input("pls input number"))
        if target_num == temp_num:
            print("yes")
            break
        elif target_num > temp_num:
            print("小了")
        else:
            print("大了")


def input_function():
    var = int(input("age?"))
    print("age = " + str(var))


def end_key_word():
    i = 0
    while i < 10:
        i = i + 1
        print(i, end=' ')
