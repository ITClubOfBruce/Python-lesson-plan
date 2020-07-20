'''
    实现计算两个数的求最大公约数和最小公倍数的函数
    最大公约数  8,12  4
    最小公倍数  8*12/最大公约数4 = 24

def gcd(x,y):
    # 保证小的数在前面
    # 设置临时变量
    # if x > y:
    #     temp = x
    #     x = y
    #     y = temp
    # print(x,y)
    # Python中特有的
    # if x>y:
    #     (x,y) = (y,x)
    # print(x,y)

    # 三目运算
    (x,y) = (y,x) if x>y else(x,y) 

    for i in range(x,1,-1):
        if x%i == 0 and y%i == 0:
            return i
result = gcd(12,8)

print(result)


def lcm(x,y):
    return x*y//gcd(x,y)

print(lcm(12,8))

'''



'''
    判断一个数是不是回文数
    29 + 92 = 121 
    121 + 121 = 242

    双端队列：回文字符串;  人人为我，我为人人   abcba  


def is_num(num):
    temp = num
    total = 0
    while temp > 0:
        total = total*10 + temp%10
        temp //= 10 
    
    return total == num

print(is_num(121))
print(is_num(2442))
print(is_num(1234))
'''


'''
    判断一个数是不是素数（只有1和它本身两个因数的数）
    3 7 11
'''
def is_num(num):
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
            return flag
    
    return flag if num != 1 else False


print(is_num(3))
print(is_num(7))
print(is_num(1))



'''
    LeetCode 866 回文素数
'''