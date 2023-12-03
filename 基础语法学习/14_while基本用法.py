# 需求：1-100 偶数累计相加

# 方法1：
# i = 1
# result = 0
#
# while i < 101:
#     if i % 2 == 0:
#         result = result + i
#     i = i + 1
#
# print(result)

# 方法2：
i = 0
result = 0
while i < 101:
    result = result + i
    i = i + 2
print(result)
