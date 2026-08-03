""""
股价计算小程序
定义如下变量：
 name 公司名
 stock_price 当前股价
 stock_code  股票代码
 stock_price_daily_growth_factor 股票每日增长系数 浮点数类型
 growth_days 增长天数
计算，经过growth_days的增长后，股价达到了多少钱
使用字符串格式化进行输出，如果是浮点数，要求小数点精确到2位数
"""
# 注意：最终股价计算公式为：当前股价 * 系数 ** 增长天数
name = "花为"
stock_price = 19.99
stock_code = "006789"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (
                                                            stock_price_daily_growth_factor,
                                                            growth_days,
                                                            stock_price *  stock_price_daily_growth_factor
                                                            **growth_days
                                                            ))