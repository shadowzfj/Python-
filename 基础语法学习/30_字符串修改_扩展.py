mystr = "hello world and itcast and itheima and Python"

mystr0 = mystr.capitalize() #字符串首字母大写
mystr1 = mystr.title() #字符串每个单词的首字母大写
mystr2 = mystr.upper() #小写转换大写
mystr3 = mystr2.lower() #大写转换小写
print(mystr)
print(mystr0)
print(mystr1)
print(mystr2)
print(mystr3)
print()


mystr = "   hello world and itcast and itheima and Python   " #删除空白字符
mystr0 = mystr.lstrip() # 左侧
mystr1 = mystr.rstrip() # 右侧
mystr2 = mystr.strip() # 所有
print(mystr)
print(mystr0)
print(mystr1)
print(mystr2)
print()


mystr = "hello" #对齐
mystr0 = mystr.ljust(10, '.')
mystr1 = mystr.rjust(10, '.')
mystr2 = mystr.center(11, '.')
mystr3 = mystr.center(10, '.')
print(mystr)
print(mystr0)
print(mystr1)
print(mystr2)
print(mystr3)
print()

mystr = "hello world and itcast and itheima and Python"
mystr1 = "helloworldanditcastanditheimaandPython"
mystr2 = "1234"
mystr3 = "1sdfsdf234"
mystr4 = " "
print(mystr.isalpha())   # 字母，返回true
print(mystr1.isalpha())
print(mystr.isdigit())   # 数字，返回true
print(mystr2.isdigit())
print(mystr1.isalnum())   # 数字，字母，或者数字字母组合，返回true
print(mystr.isalnum())
print(mystr3.isalnum())
print(mystr.isspace())   # 都是空白，返回true
print(mystr4.isspace())





