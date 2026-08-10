# 案例需求
# 定义一个数字（1-10随机产生），通过3次判断来猜出数字。
# 案例要求：
# 1. 数字随机产生，范围1-10
# 2. 有3次机会猜测数字，通过3层嵌套判断实现。
# 3. 每次猜不中，会提示大了或小了。
# 提示，通过如下代码，可以定义一个变量num，变量内存储随机数字。
# import random
# num = random.randint(1,10)

# 第一次写
import random
num = random.randint(1,10)
# guess1 = int(input("请输入第一次猜想的数字："))
# if guess1 != num:
#     if guess1 > num:
#         print("猜大了")
#         guess2 = int(input("请输入第二次猜想的数字："))
#         if guess2 != num:
#             if guess2 > num:
#                 print("猜大了")
#                 guess3 = int(input("请输入第三次猜想的数字："))
#                 if guess3 != num:
#                     if guess3 > num:
#                         print("猜大了")
#                     else:
#                         print("猜小了")
#                 else:
#                     print("恭喜您第三次猜对了")
#             else:
#                 print("猜小了")
#                 guess3 = int(input("请输入第三次猜想的数字："))
#                 if guess3 != num:
#                     if guess3 > num:
#                         print("猜大了")
#                     else:
#                         print("猜小了")
#                 else:
#                     print("恭喜您第三次猜对了")
#         else:
#             print("恭喜您！第二次猜对了！")
#     else:
#         print("猜小了")
#         guess2 = int(input("请输入第二次猜想的数字："))
#         if guess2 != num:
#             if guess2 > num:
#                 print("猜大了")
#                 guess3 = int(input("请输入第三次猜想的数字："))
#                 if guess3 != num:
#                     if guess3 > num:
#                         print("猜大了")
#                     else:
#                         print("猜小了")
#                 else:
#                     print("恭喜您第三次猜对了")
#             else:
#                 print("猜小了")
#                 guess3 = int(input("请输入第三次猜想的数字："))
#                 if guess3 != num:
#                     if guess3 > num:
#                         print("猜大了")
#                     else:
#                         print("猜小了")
#                 else:
#                     print("恭喜您第三次猜对了")
#         else:
#             print("恭喜您！第二次猜对了！")
# else:
#     print("恭喜你！第一次就猜对了！")
# print(f"这个随机数是{num}")

# 第二次写
guess = int(input("第一次猜想的数字："))
if guess == num:
    print("恭喜您！第一次就猜对！")
else:
    if guess > num:
        print("猜大了")
    else:
        print("猜小了")
    guess = int(input("第二次猜想的数字："))
    if guess == num:
        print("恭喜你！第二次就猜对了")
    else:
        if guess > num:
            print("猜大了")
        else:
            print("猜小了")
        guess = int(input("第三次猜想的数字："))
        if guess == num:
            print("恭喜你第三次猜对了")
        else:
            print("机会用完，全部猜错")
print("这个随机数是%s" % num)




