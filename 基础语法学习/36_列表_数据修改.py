name_list = ['Tom', 'Lily', 'Rose', 'Lily']

# 1.修改指定下标的数据
name_list[0] = '小麦'
print(name_list)
print()

# 2.逆序 reverse()
name_list.reverse()
print(name_list)
print()

# 3. sort() 排序：升序或者降序
list1 = [1, 4, 5, 14, 10]
list1.sort(reverse=False)
print(list1)

list1.sort(reverse=True)
print(list1)