# 函数：是组织好的、可重复使用的，用来实现特定功能的代码段。

# 统计字符串长度函数len

# 写法1
# name = "hianksdjk"
# length = len(name)
# print(length)

# 写法2
# name = "hasjsdkmlnhhhhhhhhhhhhhhhhhhhhhhhhhhhhajsdjdd"
# print(f"{name}的长度是：{len(name)}")

# 为什么随时都可以使用len()统计长度呢？
# 因为，len()是Python内置的函数：
# 1.是提前写好的
# 2.可以重复使用
# 3. 实现统计长度这一特定功能的代码段
# 我们使用的：input()、print()、str()、int()等都是Python的内置函数。 该叫print函数、input函数，不说成语句了。

# 不使用内置函数len()、完成字符串长度的计算。
name = "ahjhujsdkjasn"
counter = 0
for i in name:                  # 重复的代码片段
    counter += 1
print(f"‘{name}’的长度为：{counter}")

info = "我爱学习学习使我快乐"
length = 0
for i in info:                  # 重复的代码片段
    length += 1
print(f"'{info}'的长度是：{length}")

# 把重复的代码片段打包起来，打包成一个函数：将功能封装在函数内，可供随时随地重复利用。
# 提前写好的
# 重复使用
# 特定需求
def my_len(data):
    length = 0
    for i in data:
        length += 1
    return length
name = "jkakindhoPMSHBUJSDND"
print(f"{name}的长度为：{my_len(name)}")

# 为什么要学习、使用函数呢？
# 为了得到一个针对特定需求，可供重复利用的代码段，提高程度的复用性、减少重复性代码，提高开发效率。





