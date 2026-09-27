# 邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），如果输入正确，输出“ 邮箱格式正确 ”，否则输出“ 邮箱格式错误 "

# 方式一：
# 1.接收用户输入的邮箱
email = str(input("请输入您的邮箱："))

# 2.判断邮箱的格式
if email.count("@") == 1 and email.count(".") >= 1:
    print(f"{email}是合法的邮箱")
else:
    print(f"{email}是非法的邮箱")

# 正常的邮箱校验需要用到正则表达式，后续学习。

# 方式二：
# 运用的知识点：in 运算符（返回 bool值）-----> 判断子串是否在在字符串中，存在返回True；否则返回False
# 1.接收用户输入的邮箱
email = str(input("请输入您的邮箱："))

# 2.判断邮箱的格式
if email.count("@") == 1 and "." in email:
    print(f"{email}是合法的邮箱")
else:
    print(f"{email}是非法的邮箱")