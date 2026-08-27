print("欢迎来到heaven ATM 取款机")
name = input("请输入你的姓名：")
money = 5000000
def menu():
    """
    这是ATM取款机主菜单函数，提示用户输入选择：查询余额、取款、存款、退出。并返回得到的结果
    :return:返回用户输入的数字
    """
    print("-"*15 + "主菜单" + "-"*15)
    print("请输入操作：")
    print("查询余额 [输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入你的选择："))
def check_balance(title):
    """
    查询用户余额
    :return:None
    """
    global money
    if title:       # 传入True打印下面的内容
        print("-" * 15 + "查询余额" + "-" * 15)
    print(f"{name},你好，您的余额剩余：{money}元")
def save_money():
    """
    向用户余额存钱并显示余额
    :return:None
    """
    global money
    print("-" * 15 + "存款" + "-" * 15)
    num = int(input(f"{name},你要存款多少元："))
    money += num        # 修改全局变量money值，用global声明
    print(f"{name},你好，你存款{num}元成功！")
    # print(f"{name},你好，你的余额还剩：{money}元。")
    check_balance(False)     # 调用check_balance函数查询余额
def take_money():
    """
    用户向银行取钱并显示余额
    :return:None
    """
    global money
    print("-" * 15 + "取钱" + "-" * 15)
    num = int(input(f"{name},你要取钱多少元："))
    if num > money:
        print("对不起，您的余额不足！")
        check_balance(False)
    else:
        money -= num
        print(f"{name},你好，你取款{num}元成功！")
        # print(f"{name},你好，你的余额还剩：{money}元。")
        check_balance(False)  # 调用check_balance函数查询余额



while True:
    # 输入用户姓名后，显示主菜单，得到用户输入的数字
    input_num = menu()
    # 基于用户输入数字来决定要做什么
    if input_num == 1:
        check_balance(True)
    elif input_num == 2:
        save_money()
    elif input_num == 3:
        take_money()
    else:
        print("欢迎下次光临heaven ATM 取款机！")
        break








