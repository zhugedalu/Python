"""
待处理数据集，严格来时，称之为：可迭代类型。
可迭代类型指，其内容可一个个依次取出的一种类型，包括:
字符串、列表、元组等。
range语句可以生成可迭代对象。
for循环语句，本质上是遍历：可迭代对象。
range语句功能，获得一个简单的数字序列（可迭代类型的一种）
语法：
range(num1[num2[,step]])
- []在描述语法中，表示：可选
"""
# 语法1：
# range(num)
# 获取一个从0开始，到num结束的数字序列（不含num本身）
# range（5）获取的数据是：[0,1,2,3,4]
for c in range(7):
    print(c)
print("-"*50)
# 可以快速得到100次的循环，可以用for a in range(100),比用字符串方便

# 语法2：
# range(num1,num2)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身) 包头不包尾
for a in range(1,10):
    print(a)
print("-"*50)
# 语法3：
# range(numq,num2,step)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身)
# 数字之间的步长，以step（步进）为准（默认为1）
for b in range(1,9,2):
    print(b)


