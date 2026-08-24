"""
全局变量，指的是在函数体内、外都能生效的变量(不定义在函数内部的变量)
思考：如果有一个数据，在函数A和函数B中都要使用，该怎么办？
将这个数据存储在一个全局变量里面
"""
# 定义全局变量
num = 100
def test1():
    print("test1输出：",num)
def test2():
    print("test2输出：",num)
test1()
test2()
print(f"外部：{num}")