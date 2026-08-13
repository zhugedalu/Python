"""
练习案例：数一数有几个 a
定义字符串变量 name ，内容为 “ajsuKMSKAaakknaikak”
通过for循环，遍历此字符串，统计有多少个英文字母：“a”
"""
counter = 0
name = "ajsuKMSKAaakknaikak"
for c in name:
    if c == "a":
        counter += 1
print(f"name变量中一共有{counter}个字母a")