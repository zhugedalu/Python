# 1.字符串的下标（索引）
# 和其它容器一样：列表、元组一样，字符串也可以通过下标进行访问。
# 从前向后，下标从0开始。
# 从后向前，下标从-1开始。
name = "asjkhuds"
print(name[4])          # 访问下标都是使用中括号[]

# 同元组一样，字符串是一个：无法修改的数据容器。

# 修改字符串：报错
# name[6] = "haha"         # TypeError: 'str' object does not support item assignment 这是修改字符串的值

# name = "jaskhck"  # 改的不是字符串，而是变量本身，这是重新赋值变量

# 2.index 查找元素在容器内的下标，找到返回下标，找不到报错。
name  = "asdkj哈哈000"
print(name.index("000"))

# 3.replace(old_str,new_str)
# 将字符串内的指定字符，替换为新的。(返回值是新的，可以用变量接收，属于重新赋值)
# 字符串本身无法修改，所以replace函数是```返回```一个新的修改后的字符串
# 并没有对原有字符串作出修改
s = "张三|李四|王麻子"
s2 = s.replace("|"," , ")
print(s)
print(s2)


# 4.字符串的分割 split(分隔符)
# 可以按指定分隔符，将字符串分隔出多份，存入一个新的 list内并返回
s = "张三|李四|王麻子"
lst = s.split("|")
print("字符串本身：",s)
print("分隔后：",lst,type(lst))

# 5.strip() 取出字符串的前后空格和回车符
# 原有字符串不会被修改，返回新的
s = "      \najhahahha哈哈哈\n   "
s = s.strip()
print(s)

# 6.strip(字符串)  去除字符串中前后指定的字符
s = "|||||kjdsabj|||"
# s  = s.strip("|")
s = s.replace("|","")       # 变成空的字符串
print(s)

# 统计字符串有多少个a
# 7.count(字符串) 统计字符串内有多少个指定的子串
s = "wdksjnfcgsDNLKVGASBJDSDBGVKJNHDAVGDSFBLKSVAHJSJD"
print(s.count("J"))
# 用循环统计字符串中指定的字串
counter = 0
for i in s:
    if i == "J":
        counter += 1
print(f"s字符串中有：{counter}个'J'")

# 8.统计字符串长度(不管是字符、字母、中文都算作一个长度)
# len(字符串)
s = "wdksjnfcgsDNLKVGASBJDSDBGVKJNHDAVGDSFBLKSVAHJSJD"
length = len(s)
print(length)


# 9.字符串的遍历
# 同列表、元组一样，字符串也支持while、for循环
my_str = "你好呀小可爱"
index = 0
while index < len(my_str):
    print(my_str[index])
    index  += 1

for i in my_str:
    print(i)

'''
字符串的特点：
作为数据容器，有如下特点：
1. ```只存储字符串```
2. 长度任意（取决于内存大小）
3. 支持下标索引
4. 允许重复字符串存在
5. ```不可以修改（增加或删除元素等)```
6. 支持for循环
'''