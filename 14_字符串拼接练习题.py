"""
定义变量：
money : 记录余额（数字）
name  : 记录姓名（字符串）
salary ： 薪资（数字，2位小数点）

通过python语句输出：
我是XXX，钱包有XXX元，但是今天发放了工资XXXX元，目前钱包有XXX元。
上述4个XXX请以变量代替，并拼接为字符串后通过print输出
"""
money = 100000
salary = 15000
name =  '虞姬'
info = "我是" + name + ",钱包有" + str(money) + "元，但是今天发放了工资" + str(salary) +"元，目前钱包有" + str(salary + money) + "元。"
print(info)