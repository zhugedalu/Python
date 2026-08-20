"""
思考:如果函数没有使用return语句返回数据，那么函数有返回值吗？

实际上是：有的

Python中有一个特殊的字面量，None，其类型是：<class 'NoneType'>
无返回值的函数，实际上就是返回了：None这个字面量

None 表示：空的、无实际意义的意思。
函数返回的None，就表示，这个函数没有返回什么有意义的内容。
也就是返回了空的意思。
"""

# 演示
# def say_hello():
#     print("hello")
# result = say_hello()
# print(result)               # 结果None,表示什么都没有
# print(type(result))         # 类型NoneType，是一个数据类型仅有一个字面量None
#
# # None可以主动使用return返回，效果等同于不写return语句
# print("-"*100)
# def say_hello():
#     print("hello")
#     return None
# result = say_hello()
# print(result)
# print(type(result))

# 在if判断中，None等同于False
if None:
    print("晚安")
if not None:
    print("晚安2")