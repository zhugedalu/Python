# 有10碗饭，挨个吃，每一碗饭吃之前问你饱没饱，吃饱了就不吃了
# for i in range(1,11):
#      print(f"正在吃第{i}碗饭,嗷呜嗷呜吃完了.....")
#      flag = int(input("吃饱了吗？（饱了输入1，没饱输入0）"))
#      if flag == 1:
#          break              # break会直接结束循环（同样和if没关系，仅对for和while有效）
#      print(f"吃了{i}碗饭，真香。")
i = 1
while i <= 10:
    print(f"正在吃第{i}碗饭,嗷呜嗷呜吃完了.....")
    flag = int(input("吃饱了吗？（饱了输入1，没饱输入0）"))
    if flag == 1:
        break
    print(f"吃了{i}碗饭，真香。")
    i += 1