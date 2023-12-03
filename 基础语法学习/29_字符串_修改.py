# replace(旧子串，新子串，替换次数):替换 替换次数可以不写，即都替换
# split(分割字符，num):分割，num表示分割字符出现的次数，所以返回的数据个数是num+1,同时丢失分割字符
# 字符或字符串.join(多字符串组成的序列):合并列表李的字符串数据为一个大字符串

mystr = "hello world and itcast and itheima and Python"
print('replace测试')
new_mystr = mystr.replace('and', 'he', 1) #replace有返回值，但是不会修改原有的字符串
# 说明字符串是不可变类型
# 数据可以分为两种类型：1.可变类型；2.不可变类型
print(mystr)
print(new_mystr)
print()

print('split测试')
new_mystr1 = mystr.split('and') # 返回一个列表数据
new_mystr2 = mystr.split('and', 2)
print(new_mystr1)
print(new_mystr2)
print()

print('join测试')
mylist = ['aa', 'bb', 'cc']
new_mylist0 = '...'.join(mylist)
print(new_mylist0)
print(mylist)
