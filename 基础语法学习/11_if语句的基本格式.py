# if语句
age = int(input("请输入自己的年龄"))
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")

print("时间过得真快")

# if else语句
print("欢迎来到迪士尼乐园，儿童免费，成人收费。")
print("请输入您的年龄：")
age = int(input())
if age >= 18:
    print("您已成年，游玩需要补票10元")
else:
    print("您未成年，可以免费游玩")
print("祝您玩的愉快")

# if elif else
"""
if 条件1:
elif 条件2:
elif 条件3:
else:
"""
height = int(input("请输入您的身高(cm): "))
vip_lvl = int(input("请输入您的VIP等级(1-5): "))
day = int(input("请告诉我今天的日期："))
if height < 120:
    print("身高小于120cm，可以免费游玩")
elif vip_lvl > 3:
    print("您是高级用户，可以免费游玩")
elif day == 1:
    print("今天是1号，免费游玩")
else:
    print("抱歉，条件均不符合，需要买票进入")

# Python判断语句的嵌套

if int(input("你的身高是多少：")) > 120:
    print("身高超出限制，不可以免费")
    print("但是，如果vip级别大于3，可以免费游玩")

    if int(input("你的vip级别是多少：")) >3:
       print("恭喜你，vip级别达标，可以免费")
    else:
        print("对不起，你需要买票10元")
else:
    print("欢迎小朋友，免费游玩")
