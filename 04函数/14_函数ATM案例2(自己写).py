print("欢迎来到HEAVEN ATM 取款机！")
name = input("请输入您的姓名：")
money = 5000000
def menu():
    """
    显示主菜单，输出用户的选择
    :return: 用户的选择
    """
    print("-"*20 + "主菜单" + "-"*20)
    print(f"{name},您好。欢迎来到HEAVEN ATM取款机。请选择操作：")
    print("查询余额 [输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入您的选择："))
def check_balance(title):
    """
    查询账户余额并显示余额
    :return: None
    """
    if title:
        print("-"*20 + "查询余额" + "-"*20)
    print(f"{name},您的余额账户还剩：{money}元")
def save_money():
    """
    向账户存钱并显示余额
    :return: None
    """
    global money
    print("-" * 20 + "存款" + "-" * 20)
    num = int(input(f"{name},您要存款多少元："))
    print(f"{name},{num}元存款成功！")
    money += num
    check_balance(False)
def take_money():
    """
    向账户取钱并显示余额
    :return:
    """
    global money
    print("-" * 20 + "取款" + "-" * 20)
    num = int(input(f"{name},您要取款多少元："))
    if num > money:
        print("对不起，您的账户余额不足。")
        check_balance(False)
    else:
        money -= num
        print(f"{name},取款{money}成功")
        check_balance(False)
while True:
    option_num = menu()
    if option_num == 1:
        check_balance(True)
    elif option_num == 2:
        save_money()
    elif option_num == 3:
        take_money()
    else:
        print("欢迎下次光临HEAVEN ATM 取款机。再见！")
        break
