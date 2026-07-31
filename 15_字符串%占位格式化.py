"""
演示使用%占位的方式对字符串进行格式化（拼接）
"""
name = "项羽"
age = 5000
height = 190.55

# 传统拼接
info = "我是" + name + "，今年" + str(age) + "岁，身高为" + str(height) + "厘米"
print(info)

# 用%占位符  语法: "%占位符" % 变量或者变量的计算
# %s  %表示占位，s表示字符串，合上就是此处占位一个字符串，字符串由后边的变量提供。有几个%占位符就提供几个变量，要求一一对应。
print("-" * 100)
# 将name、age、height的值填入 %s所占的位置，括号里面有顺序
# %s占位提供数字类型，会自动转化为字符串。
# age是以"5000"的类型填充，height也是以"190.55"的类型填充。
info1 = "我是%s，今年%s岁，身高为%s厘米" % (name,age,height)
print(info1)

# 常用三个占位符
# %s占位是字符串 任何数据都可以用%s占位
# %d占位是数字 作精细的控制
# %f占位是浮点数 作精细的控制

print("-" * 100)
info2 = "我是%s，今年%d岁，身高为%f厘米" % (name,age,height)
print(info2)
print("-" * 100)
info3 = "我是%s，今年%d岁，身高为%.1f厘米" % (name,age,height)
print(info3)

