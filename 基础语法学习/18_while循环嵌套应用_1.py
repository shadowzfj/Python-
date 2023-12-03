# 打印星号 三角形
j = 0
while j < 5:
    i = 0
    while i <= j:
        print("*", end="")
        # print("*", end="\n") 换行打*
        i += 1
    print()  # print()默认有一个换行符
    j += 1
