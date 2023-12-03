name_list = ['Tom', 'Lily', 'Rose', 'Lily']
# 列表是可变数据类型

# extend 追加数据是一个序列，将数据序列中的数据拆开，逐一添加进列表的结尾
name_list.extend('xiaoming')
print(name_list)

name_list.extend(['xiaoming', 'xiaohong'])
print(name_list)

# append 列表结尾追加数据，如果数据是序列，将序列嵌套进入列表结尾
name_list.append('二狗')
print(name_list)
name_list.append(['zyx', 'zfj'])
print(name_list)

# insert(位置下标，数据) 指定位置增加
name_list.insert(1, '哈哈哈0')
print(name_list)
name_list.insert(1, ['哈哈哈1', '哈哈哈2'])
print(name_list)
