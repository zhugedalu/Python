"""
print(内容，内容，内容.....,end = ?)
end是print的一个形式参数，它决定了输出内容的最后是什么(在内容最后加上符合，只不过默认是换行)
默认我们没有使用end参数，则它的值默认是：\n  换行  默认end = “\n”
如果不需要自带带有\n效果，可以用end=？修改，比如end=“”  最后什么都不加

"""

# 默认print语句输出内容会自动换行 这是print语句的默认效果
print("hello")
print("world")
print("hello",end="\n")
print("world",end="\n")
# 想要hello和world在一行，要求不换行
print("hello", end = "k")
print("hello", end = "k")
print("world", end = " ")
print("world", end = " ")
print()

# \t制表符：相当于键盘按tab键，默认按补四个宽度补齐空格
print("-"*50)
print("abc\t\t你好")
print("a\t\t你好")
print("abcde\t你好")   # \t前面超过四个，补到八个宽度，四个作为一组 补三个空格


# i = 1
# while i < 10:
#     print(f"1 * {i} = {1 * i}")
#     i += 1
