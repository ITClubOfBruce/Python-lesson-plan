'''
   分支结构 if else elif，
   循环结构 for while
'''
'''
    1. 用户身份验证
    输入用户名admin，密码123456，打印出登出成功，否则登录失败
'''
# username = input('请输入用户名:')
# password = input('请输入密码:')

# if username == 'admin' and password == '123456':
#     print('success')
# else:
#     print('fail')

'''
    2. 百分制成绩转换成等级成绩，均不包含上边界
    > 90      A
    80-90     B
    70-80     C
    60-70     D
    < 60      E
'''
# score = float(input('请输入成绩:'))
# if score >= 90:
#     degree = 'A'
# elif score >= 80:
#     degree = 'B'
# elif score >= 70:
#     degree = 'C'
# elif score >= 60:
#     degree = 'D'
# else:
#     degree = 'E'

# print('对应的等级是:',degree)




'''
    3.输入三条边长，如果能构成三角形就计算其面积和周长
    # 任何两条边相加大于第三条边，就可以构成一个三角形
    海伦公式求面积：
    (a+b+c)/2  *  (a+b+c)/2-a  *  (a+b+c)/2-b  * (a+b+c)/2-c  之后开平方
'''

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a+b>c and a+c>b and b+c>a:
    print('周长:%f'%(a+b+c))
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print('面积:%f'%area)
else:
    print('不能构成三角形')

