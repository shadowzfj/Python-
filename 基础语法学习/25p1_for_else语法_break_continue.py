# for 临时变量 in 序列：
#     重复执行代码
#     *****
print('测试break')
str1 = "itheima"
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
else:
    print("循环正常结束后执行的代码")

print()

print('测试continue')
str1 = "itheima"
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
else:
    print("循环正常结束后执行的代码")