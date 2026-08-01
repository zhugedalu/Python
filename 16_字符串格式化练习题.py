"""
定义变量：
money : 记录余额（数字）
name  : 记录姓名（字符串）
salary ： 薪资（数字，2位小数点）

通过python语句输出：
我是XXX，钱包有XXX元，但是今天发放了工资XXXX元，目前钱包有XXX元。
上述4个XXX请以变量代替，并字符串格式化的形式完成print输出
"""
name = "虞姬"
money = 100000
salary = 15000.72
# %.1f代表小数后一位，%.2f代表小数后2位，四舍五入的  在python种，浮点数默认小数点后六位
info = "我是%s，钱包有%d元，但是今天发放了工资%.2f元，目前钱包有%.2f元" % (name,money,salary,money + salary)
print(info)