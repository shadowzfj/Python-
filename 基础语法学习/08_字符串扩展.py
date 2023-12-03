name = 'heima'
print(type(name))

name = "yyds"
print(type(name))

name = """
yyds
"""

print(type(name))

print("zengergou" + " yyds")

#课程：字符串格式化
# 测试1
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)
# 测试2
name = "yyds"
message = "曾二狗，%s" %name
print(message)
# 字符串格式化
name = "智传播客"
set_up_year = 2006
num_test = 1
stock_price = 19.9
message = "我是：%s, 我成立于：%d+%d年, 我今天的股价是：%f" % (name, set_up_year, num_test, stock_price)
print(message)

# 字符串格式化精度控制
name = "智传播客"
set_up_year = 2006
num_test = 1
stock_price = 19.8345
message = "我是：%s, 我成立于：%d+%d年, 我今天的股价是：%1.4f" % (name, set_up_year, num_test, stock_price)
print(message)
message = "我是：%s, 我成立于：%d+%d年, 我今天的股价是：%5f" % (name, set_up_year, num_test, stock_price)
print(message)
message = "我是：%s, 我成立于：%d+%d年, 我今天的股价是：%5.1f" % (name, set_up_year, num_test, stock_price)
print(message)

# 字符串格式化方式2
# test1
# 快速格式化
name = "智传播客"
set_up_year = 2006
num_test = 1
stock_price = 19.8345
message = f"我是：{name}, 我成立于：{set_up_year}年, 我今天的股价是：{stock_price}"
print(message)

# 对表达式进行格式化
