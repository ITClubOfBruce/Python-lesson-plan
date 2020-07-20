'''
    写代码要符合PEP8规范
    用小写字母拼写，多个单词使用_（下划线）连接
    受到保护的实例属性用单个下划线开头
    私有的属性实例用两个下划线开头
'''

'''
   练习一：华氏温度转摄氏温度
   用户输入华氏温度，需要我们写程序输出摄氏温度  c = (f-32)/1.8
  Version:1.0
  Author:Bruce 
'''

'''
f = float(input('请输入华氏温度:'))
c = (f-32)/1.8
print('%.1f华氏温度=%.1f摄氏度'%(f,c))
'''




'''
    练习二：计算圆的周长和面积，输入r（半径）的情况下
    Version:1.0
    Author:Bruce 
'''
'''
PI = 3.14
r = float(input('请输入圆的半径:'))
per = 2*PI*r
area = PI*r*r
a = PI*r**2

print('周长:%.2f'%per)
print('面积:%2.f'%area)
print(a)
'''

'''
     练习三：用户输入自己出生年份，判断用户的生肖
     Version:1.0
    Author:Bruce

'''
'''
2020年  鼠
1989%12 = 9   蛇
2020%12 = 4

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input('请输入您的出生年份:'))

index = year%12

print('您的生肖为:%s'%chinese_zodiac[index])
'''

'''
     练习四：用户输入自己出生月日，判断用户的星座
    Version:1.0
    Author:Bruce
'''
zodiac_name=('摩羯','水瓶','双鱼','白羊','金牛','双子','巨蟹','狮子','处女','天秤','天蝎','射手')
zodiac_days=((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

#  接收用户的输入
int_month = int(input('请输入月份:'))
int_day = int(input('请输入日期:'))

(int_month,int_day)

'''
for x in zodiac_days:
	if x > (int_month,int_day):
		print(x)
		break
'''
# 但是我们需要的是（7,23）的脚标
'''
for zd_num in range(len(zodiac_days)):
	if zodiac_days[zd_num] > (int_month,int_day):
		print(zodiac_name[zd_num])
		break
	elif int_month==12 and int_day>22:
		print(zodiac_name[0])
		break
'''
num = 0

while zodiac_days[num] < (int_month,int_day):
	if int_month==12 and int_day>22:
		break
	num += 1

print(zodiac_name[num])

#  元组之间的比较
# (month,day) = (7,12)
#  lambada 表达式（表示条件的函数）
'''
for x in zodiac_days:
	if x < (month,day):
		print(x)
'''
# filter函数，python3中内置的过滤函数，返回一个迭代器
#  两个参数：第一个参数是函数，第二个参数为序列
'''
f_list = filter(lambda x:x<(month,day),zodiac_days)
new_list = list(f_list)
print(new_list)
'''








'''
     练习五：用户输入自己出生年月日，判断用户的星座和生肖
    Version:1.0
    Author:Bruce
'''


















