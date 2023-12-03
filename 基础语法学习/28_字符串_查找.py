# find():检测某个子串是否包含在这个字符串中，如果在，返回这个子串开始的位置下标，否则返回-1
# 字符串序列.find(子串，开始位置下标，结束位置下标)
# index():检测某个子串是否包含在这个字符串中，如果在，返回这个子串的开始位置下标，否则报异常
# 字符串.index(子串，开始位置下标，结束位置下标)
# 注意：开始位置和结束位置可以省略
# count():返回某个子串在字符串中出现的次数
# rfind() = find(),但是查找方向从右侧开始
# rindex() = index(),但是查找方向从右侧开始
mystr = "hello world and itcast and itheima and Python"
print(mystr.find('and'))  # 空格也占字符
print(mystr.find('and', 15, 30))
print(mystr.find('ands'))  # 空格也占字符

print(mystr.index('and'))
print(mystr.index('and', 15, 30))
# print(mystr.index('ands'))

print(mystr.count('and', 15, 30))
print(mystr.count('and'))
print(mystr.count('ands'))

print(len(mystr)) #统计长度