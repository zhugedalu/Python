"""
练习案例：有几个偶数
定义一个数字变量num,内容随意。
并使用range语句，获取从1到num的序列，使用for循环变量它。
在遍历的过程中，统计有多少偶数出现。
"""
num = int(input("请输入一个数字："))
counter = 0
for i in range(1,num):
    if i % 2 == 0:
        counter += 1
print(f"[1,{num}]这个数列一共有{counter}个偶数出现")
