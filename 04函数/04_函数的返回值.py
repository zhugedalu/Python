# 程序中的返回值
# def add(a,b):
#     result = a + b
#     return result
# r = add(1,19)           # add(1,19)运行结果是3，相当于把3赋值给r
# print(r)

"""
返回值：就是程序中函数完成后，最后给调用者的结果。
返回值的语法：
def 函数名（参数）：
    函数体
    return 返回值
变量 = 函数（参数 ）

# 变量接收函数的返回值，语法：通过return关键字，就能向调用者返回数据。
# 注意：函数体在遇到return后结束了，所以写在return后的代码不会被执行
"""
# 定义一个函数：完成两数相加的功能，并返回结果。
def add(b,k):
    result = b + k
    return result
    print("hahah")       # return后的代码不会被执行。若没有return 执行完输出None
# add(1,3)              # 产生了一个结果，既没有存变量也没有被打印出来
r = add(1,4)      # return向调用方提供结果，add(1,4)等于5
print(r)