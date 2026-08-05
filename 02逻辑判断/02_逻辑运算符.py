"""
运算符：逻辑运算
1. 与  AND
       多条件同时满足，则结果为 True，否则是False
2. 或  OR
       多条件满足任意1个，则结果为True，否则是False
3. 非  NOT
       取反结果，True变成False或False变成True
"""

age = 19
# print("5 < age < 18 ? = %s" % (5 < age < 18))    计算结果中不要写成5 < age < 18，要分开写。如下：
print("5 < age < 18 ? = %s" % (age > 5 and age < 18))
print("5 < age 或 age < 18 ?  = %s" % (age > 5 or age < 18 ))
print("age不是成年人 = %s " % ( not age > 18))