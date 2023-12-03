import random
num = random.randint(1,10)
guess_num = int(input("请输入你猜测的数字"))

if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("请第二次输入你猜测的数字"))
    if guess_num == num:
        print("恭喜，第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("请第三次输入你猜测的数字"))
        if guess_num == num:
            print("恭喜，第三次就猜中了")
        else:
            if guess_num > num:
                print("你猜测的数字大了")
            else:
                print("你猜测的数字小了")