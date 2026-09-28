# 练习 1
# 输入一个字符串，判断该字符串是否是回文（两边对称）。
# str1 = input("请输入一个字符串：")
# if str1 == str1[::-1]:
#     print(f"{str1}是回文")
# else:
#     print(f"{str1}不是回文")


# 练习 2
# 将用户输入的10个字符串，反转后全部转换成大写，然后记录在列表中，最后将列表内容，遍历输出出来。
list1 = []
for i in range(10):
    str2 = input("请输入一个字符串:")
    new_str = str2[::-1].upper()
    list1.append(new_str)
print(list1)

# 注意：反转是反转输入的字符串，而不是列表位置 字符串.upper() ----> 改成大写字母


