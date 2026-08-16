"""
无论是while循环还是for循环，都是重复性的执行特定操作。
在这个重复过程中，会出现一些其它情况让我们不得不：
1. 暂时跳过某次循环，直接进行下一次。
2. 提前退出循环，不再继续。

对于这种场景，python提供 continue 和 break 关键字用以对循环进行临时跳过和直接结束。
"""
# continue
# continue关键字用于：中断本次循环，直接进入下一轮循环。
# continue可以用于：for循环和while循环，效果一致。
# for i in range(1,100):
#     语句 1
#     continue
#     语句2
# 在循环内，遇到continue就结束本次循环，进行下一次。所以，语句2是不会执行的。
# 应用场景：在循环中，因某些原因，临时结束本次循环。
# for i in range(3):
#     print("have good luck!")
#     continue
#     print("see you soon")
# continue关键字只可以控制：它所在的循环临时中断。不能越级(只对所在循环有效，对上层循环没用)，涉及到嵌套。


# break
# break关键字用于：直接结束循环
# break可以用于：for循环和while循环，效果一致。
# for i in range(3):
#     print("good night!")                    # 语句1
#     break
#     print("see you soon")                   # 语句2
#     print(" i hate you")                    # 语句3
# 在循环内，遇到break就结束循环了
# 所以，执行了语句1后，直接执行语句3
# break关键字同样只可以控制：它所在的循环结束

# 有10碗饭，内容不一样，每吃一碗前都会问你，这个吃不吃，吃就吃掉，不吃就跳过。
for i in range(1,11):
    flag = int(input(f"这是第{i}碗饭，吃还是不吃？(吃输入1，不吃输入0)"))
    if flag == 0:
        continue            # continue尽管在if内，但是和if没有任何关联，continue仅对for或while有效
    print(f"正在吃第{i}碗饭，嗷呜嗷呜吃完啦.....")
