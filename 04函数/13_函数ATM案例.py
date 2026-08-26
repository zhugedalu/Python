name = input("请输入您的姓名:")
money = 5000000
def cunkuan():
    money = int(input("请输入您要存款的余额："))
def qukuan():
    result = int(input("请输入您要取款的余额："))
    return result
def balance():
    print(f"您的余额还剩：{money + cunkuan - qukuan}元")
def menu():
    print("---------------主菜单----------------")
    global option
    option = int(input("你好，欢迎来到heaven银行ATM，请选择操作:\n查询余额 [输入1]\n存款\t\t[输入2]"
                       "\n取款\t\t[输入3]\n退出\t\t[输入4]\n请输入您的选择:"))
while True:
    menu()
    if option == 1:
        balance()







