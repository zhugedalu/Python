"""
 通过input语句获取键盘输入身高
 判断身高是否超过120cm，并通过print给出提示信息。
 欢迎来到FUN动物园
 请输入你的身高（cm）：130
 您的身高超出120cm，游玩需要购票10元。  您的身高未超出120cm，可以免费游玩。
 祝您游玩愉快。
"""
print("Welcome to FUN ZOO!" )
height = float(input("please input your height(cm):"))
if height >= 120:
    print("your height is more than 120cm,please pay the 10 yuan for ticket.")
else:
    print("you can play for free!")
print("have a good time!")