# ------------------------------ 列表 List案例 3  --------------------------------------
# 1.生成一个1-20的平方列表
# 定义列表
num_list = []
# 方式一：传统方式：range(1,21)
for i in range(1,21):
    num_list.append(i ** 2)
print(num_list)

# .利用while循环输出元素并添加到列表（自己写的）
# i = 1
# while i <= 20:
#     num = i * i
#     num_list.append(num)
#     i += 1
# print(num_list)

# 方式二 ```列表推导式```   ------> 就是按照一定的规则快速生成一个列表的方法 -----> 语法格式 1(不带条件)：[要插入的值 for i in 序列/列表]
num_list2 = [i**2 for i in range(1,21)]
print(num_list2)



# 2.从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表。-----> 判断偶数 num % 2 == 0
# num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]

# num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
# new_list = []
# for i in num_list:
#     if i % 2 == 0:
#         i = i * i
#         new_list.append(i)
# print(new_list)
# 方式二 ```列表推导式```   ------> 就是按照一定的规则快速生成一个列表的方法 -----> 语法格式 2（带条件）：[要插入的值 for i in 序列/列表 if 条件]
num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
new_list = [ i**2 for i in num_list if i % 2 == 0]
print(new_list)
