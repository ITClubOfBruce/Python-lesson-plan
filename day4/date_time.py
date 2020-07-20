#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   date_time.py
@Time    :   2020/07/15 14:24:10
@Author  :   Bruce 
@Version :   1.0
@Contact :   wangzuozheng712@aliyun.com
@License :   (C)Copyright 2020-2021, Bruce
@Desc    :   demo
'''

# here put the import lib
''' 
    表示一段时间：2天6小时
    datetime中timedelta
'''
# from datetime import timedelta

# a = timedelta(days=2,hours=6)
# b = timedelta(hours=4.5)

# c = a+b

# print(c.days)
# print(c.seconds)
# print(c.seconds/3600)
# print(c.total_seconds())
# print(c.total_seconds()/3600)


'''
    表示指定日期和时间  2020年2月24号
'''
# from datetime import datetime
# a = datetime(2020,2,24)
# # 自动处理闰年
# print(a+timedelta(days=5))

# # 到今天2020年7月15日，经过了多长时间的网络教学
# b = datetime(2020,7,15)

# c = b - a
# print(c.days)

# now = datetime.today()
# print(now)

# print(now+timedelta(minutes=8))




'''
    基本的时间和日期处理，用datetime
    处理时区的问题，模糊时间范围，节假日计算
    安装 pip install dateutil模块，dateutil.relativedelta()函数代替
'''
# from datetime import datetime
# from datetime import timedelta

# a = datetime(2020,7,15)
# 报错
# print(a+timedelta(months=1))

# 模糊时间范围：整月的间隙，需要使用
# from dateutil.relativedelta import relativedelta

# print(a + relativedelta(months=1))
# print(a + relativedelta(months=+4))
# print(a + relativedelta(months=-1))

# b = a + relativedelta(months=1)
# c = a + relativedelta(months=+4)

# d = c - b
# print(d.days)


'''
    计算距离今天最近的上一个周几出现的日期
    第一步：星期几转换成日期，输入Monday  -> 2020年7月13号
'''
# from datetime import datetime
# from datetime import timedelta

# weekdays = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

# def get_previous_byday(dayname,start_date=None):
#     if start_date is None:
#         start_date = datetime.today()
#     # 得到今天是星期几
#     day_num = start_date.weekday()
#     day_num_target = weekdays.index(dayname)

#     days_ago = 7 + day_num - day_num_target

#     target_date = start_date - timedelta(days=days_ago)

#     return target_date

# result = get_previous_byday('星期一',datetime.today())

# print(result)




'''
    求当前月份的日期范围
    第一步：得到当前月份的第一天  
'''
# from datetime import datetime,date,timedelta
# import calendar

# 计算出当前月份的第一天和最后一天，并返回
# def get_month_range(start_date=None):
#     if start_date is None:
#         # 计算当前月份第一天
#         start_date = date.today().replace(day=1)
#     _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
#     end_date = start_date + timedelta(days=days_in_month)
#     return (start_date, end_date)

# one_day = timedelta(days=1)
# first_day,last_day = get_month_range()

# while first_day < last_day:
#     print(first_day)
#     first_day += one_day




'''
    假设全世界都要高考，计划于7月7号和7月8号早上9:30在北京举行，
    要求全世界参加高考的同学同一时间参加，计算出在美国纽约参加考试的时间

    结合时区
    所有涉及到时区相关的问题, 都使用pytz 模块，这个包提供了Olson时区数据库，
    这个数据库是时区信息事实上的标准
'''
from datetime import datetime,timedelta
from pytz import timezone
import pytz

date1 = datetime(2020,3,8,1,45,0)

print(date1)

new_york = timezone('America/New_York')
new_york_local = new_york.localize(date1)
new_york_later = new_york.normalize(new_york_local+timedelta(minutes=30))
print(new_york_local)
print(new_york_later)  # 并没有考虑到夏令时的问题


# 使用UTC，一旦转换成了UTC，就不用考虑夏令时的问题了
utc_date = new_york_local.astimezone(pytz.utc)
later_utc = utc_date + timedelta(minutes=30)
print(utc_date)
print(later_utc)

'''
    时区，去ISO 3166国家代码 去查询pytz.county_timezones
'''

print(pytz.country_timezones('CN'))