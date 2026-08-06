"""
if 要判断的条件（表达式） ：    # 表达式一定是产出bool类型True或者False，冒号不要忘记。
    条件成立时，要做的事。      # 条件成立的代码和if语句在缩进上不是一个层级的，要求是四个空格。
"""
# age = int(input("今年你多少岁？"))
# print( f"我知道啦！今年您{age}岁啦！")
# if age >= 18:
#     # 前方四个空格缩进，归属于if判断的代码语句块。python通过缩进判断代码块的归属关系。
#     print("恭喜您进入大学生活，请领取NPC任务！")  # 当if判断条件结果为True时，if内的代码会被执行。为False时，if内的代码不会执行。
# print("请继续努力！")

age = int(input("请输入您的年龄："))
height = int(input("请输入您的身高："))
if age <= 18 and height <= 120:
    print("您可以免票！")
print("欢迎游玩！")

