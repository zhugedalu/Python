# 思考：`testB`函数需要修改变量num的值为200，如何修改程序呢？
num = 100
def testA():
    print("A:",num)
def testB():
    # 想要在函数内部定义全局变量，需要做声明global
    global num          # 在此函数内部使用的num是全局变量
    num = 200           # 若没有声明global，这个num是一个和全局num同名的局部变量，相当于在函数内部声明了一个新局部变量num
                        # 声明了global num  这个num就是访问全局变量，修改它的值
    print("B:",num)     # 此时访问的num是局部变量num（未声明），声明后访问的就是全局变量num
testA()
testB()
print(f"全局变量num的值为：{num}")

# ```使用global关键字，可以在函数内部声明变量为全局变量```

# 总结：
#  1. 局部变量：作用范围在函数内部，在函数外部无法使用。
#  2.全局变量：在函数内外部都可使用
#  3.如何将函数内定义的变量声明为全局变量：使用global关键字，global变量