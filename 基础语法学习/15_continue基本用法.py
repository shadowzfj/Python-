# continue: 条件成立时，退出当前一次循环，开始下一次循环
# 吃五个苹果，吃到第3个时吃到虫子，继续吃第四五个
i = 0
while i < 5:
    i = i+1
    if i == 3:
        print(f"吃出一个大虫子，这个第{i}个苹果不吃了")
        continue
    print(f"吃了第{i}个苹果")
