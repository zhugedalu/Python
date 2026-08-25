print("---------------主菜单----------------")
option = int(input("你好，欢迎来到heaven银行ATM，请选择操作:\n查询余额 [输入1]\n存款\t\t[输入2]"
                   "\n取款\t\t[输入3]\n退出\t\t[输入4]\n请输入您的选择:"))
def balance():
    money = 500
    return money
if option == 1:
    print(f"您好，您的余额还剩：{balance()}元")
if option == 2:
    deposit = int(input("请输入您要存款的金额:"))
    print(f"您好，您存款的{deposit}元成功")
    print(f"您好，您的余额还剩：{deposit + balance()}元")
if option == 3:
    withdraw = int(input("请输入您要取款的金额："))
    if withdraw > balance():
        print("对不起，您的余额不足")
    else:
        print(f"您好，{withdraw}元已取出，您的余额还剩：{balance() - withdraw}元")


