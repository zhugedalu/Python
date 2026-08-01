"""
使用f_format方式格式化字符串（格式化就是字符串拼接   ）
语法: f"内容{变量}"
好处：不理会类型（全部作为字符串用）、不做精度控制。
     做精度控制的话 f"内容{变量：精度}"
"""
name = "蔡小葵"
age = 19
height = 190.66
# 字符串之前写f标记，如f""
# 变量用{}括起来
info =  f"我叫{name},今年{age}岁，身高为{height}cm"
print( f"我叫{name},今年{age}岁，身高为{height}cm")
print( f"我叫{name},今年{age}岁，身高为{height:8.1f}cm")