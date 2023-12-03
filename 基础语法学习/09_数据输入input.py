# test1
print("请告诉我你是谁？")
name = input()
print(f"我知道了，你是{name}。")
print("%s是个二傻子。"% name)
# test2
name = input("请告诉我你是谁")
print(f"我知道了，你是{name}。")
print("%s是个二傻子。"% name)
# test3, input默认输入是字符串，如需要其他类型，请自行转换
num = input("请告诉我你的银行卡密码")
print("你的银行卡密码的类型是：", type(num))
