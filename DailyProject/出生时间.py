#   1. 写一个程序,输入您的出生日期(年月日)
#      1) 算出你已经出生多少天?
#      2) 算出你出生那天是星期几?

import time

y = int(input("请输入出生的年: "))
m = int(input("请输入出生的月: "))
d = int(input("请输入出生的日: "))

# 第一步算出出生时的计算机元年的秒数
birth_tuple = (y, m, d, 0, 0, 0, 0, 0, 0)
birth_second = time.mktime(birth_tuple)
# 得到当前时间的秒数
cur_second = time.time()
# 算出出生的秒数
life_scond = cur_second - birth_second
life_days = life_scond / 60 / 60 // 24  # 地板除取整
print("您已出生:", life_days, '天')

# 2. 得到出生那天的时间元组,根据元组来获取数据
t = time.localtime(birth_second)
weeks = {
    0:'星期一',
    1:'星期二',
    2:'星期三',
    3:'星期四',
    4:'星期五',
    5:'星期六',
    6:'星期日',
}

print("您出生那里是:", weeks[t[6]])