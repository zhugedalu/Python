# ------------------------------ 列表 List案例 2  --------------------------------------
# 合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
lst1 = [1,2,3,56,8,58,4,34,4]
lst2 = [3,78,9,3,56,4,23,567,567]
# lst3 = list(set(lst1 + lst2))
lst3 = lst1 + lst2

# 1.用循环去重
lst4 = []
for i in lst3:
    if i not in lst4:
        lst4.append(i)
print(lst4)
# 2.用set()去重
lst5 =list(set(lst1 + lst2))
print(lst5)

# 判断一个元素是否存在于列表之中？ ---->  语法：元素 in 列表  ----->  结果返回布尔值（True表示存在）
print(4 in lst4)
