age = None
# r如果不存在，print(f"最后一个同学的年龄是:{age}")会标黄，无法访问for循环里面的age
# 当使用变量时，初始化的值没有任何要求，可以用None代替
for i in range(3):
    age = int(input("请输入你的年龄："))
    print(f"你的年龄是：{age}")
print(f"最后一个同学的年龄是:{age}")