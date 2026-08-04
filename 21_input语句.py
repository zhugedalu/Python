# input语句
# print语句，可以将内容（字面量、变量等）输出到屏幕上
# 而input语句用来获取键盘输入
# 数据输出：print
# 数据输入：input
# 使用input()语句可以从键盘上获取输入
# 使用一个变量接收（存储）input语句获取的键盘输入数据即可

# # Process finished with exit code 0  代表程序正常退出，没有则说明程序还在运行中。
# print("陌生人，请问你是谁呐？")
#
# #input语句还会阻塞程序运行，知道得到输入信息为止
# name = input()  # 右侧是一个表达式，会产生一个明确的结果
# print("Get!你叫%s，你可以叫我小鹿！以后请多多关照！" % name)
# print("-"*100)
#
# # 但其实  print("陌生人，请问你是谁呐？") 这段代码是多余的
# # input()语句可以在要求使用者输入内容前，直接在input括号里面填入输出提示内容。
# name = input("请告诉我您是谁")
# print("Get!你叫%s，你可以叫我小鹿！以后请多多关照！" % name)

# print("-"*100)
# # input语句有个特征：无论输入什么，都是字符串
# var = input("请输入信息")
# print(f"您输入的信息是：{var}，类型是：{type(var)}")

# 输入年龄
age = int(input("您的年龄是："))  # 想要输入数字类型，要自行 进行类型转换
age += 10
print(age)