"""
通过特性来分析：
    列表（混装、有序下标、支持元素重复、可以修改）可以修改、支持重复元素且有序
    元组（混装、有序、支持重复、不可修改）、字符串(单一存储、有序、可以重复、不可修改)不可修改，支持重复元素且有序
如果场景需要对内容去做重处理，列表、元组，字符串就不太方便了。
而集合的主要特点：不支持元素的重复（自带去重功能），并且内容无序。

"""
# 集合的定义
# 符号：{}  类型名：set
# 定义集合字面量
{1,2,5,8,3}
# 定义集合变量
nums1 = {1,4,6,"haha",4,6,True}         # 去重 True为1
print(nums1,type(nums1))
# 定义空集合
nums2 = set()        # 注意空集合是set()   空列表[]  空元组() 空字符串""  空集合set() 空字典{}
print(nums2,type(nums2))

# 去重且无序
# 因为要对元素做去重处理，所以无法保证顺序和创建时一致
set1 = {"bbb","bbb","aaa","cccc"}
print(set1)

# 下标访问,无法使用
# print(set1[2])

my_set = {"c","a","b","c"}
# 集合和列表一样，允许修改
# 1.add,向集合添加一个元素
my_set.add("d")
print(my_set)

# remove(元素)，移除指定元素
my_set.remove("d")
print(my_set)

# pop() 随机取出一个元素返回，此元素在集合内被删除
print(my_set.pop())     # 是随机取出一个元素，而不是给出指定元素
print(my_set)

# 清空集合 clear()
my_set.clear()
# 方式 2 ：my_set = set()
print(my_set)

# 2个集合的差集
set1 = {1,2,3}
set2 = {1,4,5}
# 集合1.difference(集合2)  取差集，集合1有而集合2没有的
# 结果是组成一个新集合返回，原有的集合1和集合2不变
set3 = set1.difference(set2)
print("差集结果：",set3)
print("原有集合：set1：",set1)
print("原有集合：set2：",set2)

set4 = set2.difference(set1)
print(set4)