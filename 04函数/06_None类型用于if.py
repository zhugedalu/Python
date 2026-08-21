""""
None类型的应用场景：
None作为一个·特殊的字面量，用于表示：空、无意义。其有很多应用场景。
1. 用在函数返回值上
2. 用在if判断上：
   在if判断中，None等同于False
   一般用于函数主动返回None，配合if判断做相关处理。
3. 用于声明无内容的变量上：
   定义变量，但暂时不需要变量有具体值，可以用None来代替
   # 暂不赋予变量具体值
   name = None
"""

# None的第二个应用场景
# def check_age(age):
#     if age >= 18:
#         return "SUCCESS"
#     return None
# result = check_age(5)
# if not result:
#     print("未成年，不能进入！")

def check_age(age):
    if age < 18:
        return None
    return "SUCCESS"        # 在if中，有内容的的字符串算作True
if check_age(10):
    print("成年人")
else:
    print("未成年人")
# 只要不是0、False、None,""(空字符串也算)
# 其余都是True

if "":
    print("hello")