#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   num_date.py
@Time    :   2020/07/15 13:18:24
@Author  :   Bruce  
@Version :   1.0
@Contact :   wangzuozheng712@aliyun.com
@License :   (C)Copyright 2020-2021, Bruce
@Desc    :   demo
'''
# here put the import lib

'''
    数字、时间日期
'''


'''
    数字的四舍五入
    round  如果一个值刚好在两个边界的中间的时候，round函数返回离它最近的  偶数 

result = round(1.2325, 3)
print(result)
print(round(1.5))
print(round(2.5))


print(round(16754, -1))  # 十位
print(round(16754, -2))  # 百位
print(round(16754, -3))  # 千位

'''

'''
    金融行业，不允许，decimal 定位数, 牺牲性能
    对浮点数执行精确的计算操作，并且不能出现任何误差
    1. 现实生活中，很少能要求超过普通浮点数的17位精度
    2. 原生浮点数计算要快的多

a = 2.1
b = 4.2
c = a+b
print(c)  # 6.300000000000001 金融 
print(c == 6.3)

# 使用decimal
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
c = a + b

print(c)



print(1.3/1.7)
# 输出28位
from decimal import Decimal
a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)

# 小数点后50位，需要创建一个本地上下文并改变它的设置
from decimal import localcontext
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)


'''


'''
    数字格式化输出，控制数字的：位数、对齐、千位分隔符和其他

a = 1234.56789
print(a)
print(format(a,'0.2f'))
# 右对齐
print(format(a,'>10.1f'))
# 左对齐
print(format(a,'<10.1f'))
# 中间 center
print(format(a,'^10.1f'))

# 千位分隔符
print(format(a,','))

# 控制小数点后1位，同时加上千位分隔符
print(format(a,',.1f'))

# 1234 = 1.234*10^3 科学计数法
print(format(a,'e'))

# 1.23*10^3
print(format(a,'0.2E'))

'''

'''
    % 和 format 的区别
    % 不支持千位符这样的东西的
'''


'''
    字节字符串  ->   大整数
    大整数      ->   字节字符串

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))  # 16位

# python中有专门的方法去转换  int.to_bytes()  int.from_bytes()

print(int.from_bytes(data,'little'))
print(int.from_bytes(data,'big'))

a = 94522842520747284487117727783387188
print(a.to_bytes(16,'big'))
print(a.to_bytes(16,'little'))
'''


'''
    IPV6 网络地址使用一个128位的整数表示   
'''




'''
    正无穷，负无穷和 NaN（非数字）

a = float('inf')
b = float('-inf')
c = float('nan')

print(a)
print(b)
print(c)


# 判断这几个值的存在，使用math.isinf()  math.isnan()
# 这几个值做四则运算，产生的值都是inf，-inf，nan
# nan == nan  判断结果为False
import math
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))


d = float('nan')
e = float('nan')

print(d==e)
print(d is e)

'''



'''
    随机数：想从一个序列中随机抽取若干元素，或者想生成几个随机数
    random 模块
    

import random

values = [1,2,3,4,5,6]

# 每次只产生一个随机数  random.choice(values)
print(random.choice(values))

# 提取n个随机数  random.sample(values,n)
print(random.sample(values,4))
print(random.sample(values,2))

# 打乱原序列中的元素顺序
random.shuffle(values)
print(values)

# 生成随机整数 random.randint()

# 生成从0-1之间均匀分布的浮点数 random.random()

# 获取N为随机位（二进制）的整数，random.getrandbits(位数)
# 1个bytes(字节) = 8个bit(位)
print(random.getrandbits(100))

# rand.seed()  rand.seed(12345)  rand.seed(b'bytedata')
# 均匀分布随机数  random.uniform()    
# 高斯分布   random.gauss()


'''