"""
通过type语句查看字面量和变量的数据类型是什么
通过type(变量)可以输出类型，这是查看的是变量的类型还是数据的类型？ 变量看出一个容器，里面存放数据。
查看的是：变量存储的数据的类型。
因为，变量无类型，但存储的数据有类型。
字符串变量，是指这个变量存储了字符串，而不是这个变量是字符串类型。
"""

# 语法： type(被查看的)  被查看的可以是：字面量、变量
# 执行顺序： 1.先执行type(666)得到结果 2.将结果通过print显示在屏幕上
print(type(666))
print(type(123.45))
print(type("我不会放弃的")) # str是string的缩写
print("---------------------------------------------------")

# 将类型信息记录到变量中
int_type = type(123) # type()语句会给出结果（返回值）
float_type = type(12.3)
str_type = type("hahaha")
print(int_type)
print(float_type)
print(str_type)
print("----------------------------------")

# type也可以查看变量的类型
name = "诸葛大璐"
age = 23
height = 158.5
print(type(name))
print(type(age))
print(type(height))