# 字符串的下标（索引）
# 和其它容器一样：列表、元组一样，字符串也可以通过下标进行访问。
# 从前向后，下标从0开始。
# 从后向前，下标从-1开始。
name = "asjkhuds"
print(name[4])          # 访问下标都是使用中括号[]

# 同元组一样，字符串是一个：无法修改的数据容器。

# 修改字符串：报错
# name[6] = "haha"         # TypeError: 'str' object does not support item assignment 这是修改字符串的值

# name = "jaskhck"  # 改的不是字符串，而是变量本身，这是重新赋值变量

# index 查找元素在容器内的下标，找到返回下标，找不到报错。
name  = "asdkj哈哈000"
print(name.index("000"))

# replace(old_str,new_str)
# 将字符串内的指定字符，替换为新的。(返回值是新的，可以用变量接收，属于重新赋值)
# 字符串本身无法修改，所以replace函数是```返回```一个新的修改后的字符串
# 并没有对原有字符串作出修改
s = "张三|李四|王麻子"
s2 = s.replace("|"," , ")
print(s)
print(s2)


# 字符串的分割 split(分隔符)
# 可以按指定分隔符，将字符串分隔出多份，存入一个新的 list内并返回
s = "张三|李四|王麻子"
lst = s.split("|")
print("字符串本身：",s)
print("分隔后：",lst,type(lst))

# strip() 取出字符串的前后空格和回车符
# 原有字符串不会被修改，返回新的
s = "      \najhahahha哈哈哈\n   "
s = s.strip()
print(s)

# strip(字符串)  去除字符串中前后指定的字符
s = "|||||kjdsabj|||"
# s  = s.strip("|")
s = s.replace("|","")       # 变成空的字符串
print(s)

