"""
for 临时变量 in 待处理数据集(序列)：
    循环满足条件应做的事情 1
    循环满足条件应做的事情 2
    循环满足条件应做的事情 3
    .......
    for 临时变量 in 待处理数据集(序列)：
        循环满足条件应做的事情 1
        循环满足条件应做的事情 2
        循环满足条件应做的事情 3
        .......
while和for循环可以相互嵌套
注意事项：注意缩进
"""
# 需求：每天都去表白，共100天
# 每次：表白送10个花，说1句我喜欢你
# for day in range(1,101):
#     print(f"今天是第{day}天，表白准备开始.......")
#     for rose in range(1,11):
#         print(f"这是表白第{day}天，我给小美送的第{rose}支玫瑰花。")
#     print("小美，我喜欢你。")
# print(f"坚持到第{day}天，表白成功！")


# 外层for，内层while
# for day in range(1,101):
#     print(f"今天是第{day}天，表白准备开始.......")
#     rose = 1
#     while rose <= 10:
#         print(f"这是表白第{day}天，我给小美送的第{rose}支玫瑰花")
#         rose += 1
#     print("小美，我喜欢你。")
# print(f"坚持到第{day}天，表白成功！")


# 外层while，内层for
day = 1
while day < 101:
    print(f"今天是第{day}天，表白准备开始.......")
    for rose in range(1, 11):
        print(f"这是表白第{day}天，我给小美送的第{rose}支玫瑰花。")
    print("小美，我喜欢你。")
    day += 1
print(f"坚持到第{day}天，表白成功！")