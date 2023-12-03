name_list = ['Tom', 'Lily', 'Rose', 'Lily']
# del 可以删除指定下标的数据,也可以删除整个列表
# del name_list
del name_list[0]
print(name_list)
print()

name_list = ['Tom', 'Lily', 'Rose', 'Lily']
# .pop() 删除指定下标，如果不指定下标，默认删除最后一个数据
# 无论是按照下标还是默认删除最后一个数据，pop函数都会返回这个被删除的数据
del_name = name_list.pop(1)
print(del_name)
print(name_list)
print()

# .remove(数据) 删除数据
name_list = ['Tom', 'Lily', 'Rose', 'Lily']
name_list.remove('Rose')
print(name_list)
print()

# .clear() 清空数据
name_list = ['Tom', 'Lily', 'Rose', 'Lily']
name_list.clear()
print(name_list)
