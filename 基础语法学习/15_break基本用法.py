# 吃五个苹果，吃到第三个，吃饱了，不吃了
i = 0
while i <= 5:
    if i == 4:
        print("吃饱了，不吃了")
        break
    print(f"吃了第{i}个苹果")
    i = i + 1
