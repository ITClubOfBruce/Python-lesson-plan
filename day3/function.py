'''
    可接收任意数量参数的函数
    1. 使用  * 参数,接收任意数量的位置参数，type(rest) 元组类型
    2. **  接收任意数量的关键字参数，它的数据类型是字典dict
'''
'''
def avg(a,*rest):
    sum_num = a+sum(rest)

    avg_num = sum_num/(1+len(rest))

    return avg_num

print(avg(1,2))
print(avg(1,2,3,4))
'''

# HttpResponse 
# import html
# def index(request):
#     return HttpResponse('<p class="box" id>这是一个p元素</p>')

# def make_element(name,value,**attrs):
#     keyvals = [' %s="%s"'% item for item in attrs.items()]
#     attr_str = ' '.join(keyvals)

#     element = '<{name}{attrs}>{value}</{name}>'.format(name=name,attrs=attr_str,value=html.escape(value))

#     return element

# print(make_element('item','Albatross',size='large',quantity=6))


# 一个 * 参数只能出现在函数定义中最后一个位置参数后面; **参数只能出现在最后一个参数
# 思考：如果 * 参数后面又出现了其他参数，会怎么样？

def fun1(a,*args,b):  # b就是dict
    pass
def fun2(x,*args,y,**kwargs):
    pass


def recv(maxsize,*,block):
    pass
# TypeError: recv() takes 1 positional argument but 2 were given
# recv(1024,True)

# recv(1024,block=True)

# 强制关键字参数，增加程序的可读性
# def min_num(*values,clip=None):
#     m = min(values)
#     if clip is not None:
#         m = clip if clip > m else m
#     return m

# print(min_num(1,2,3,4,5))
# print(min_num(1,2,3,4,5,clip=0))


'''
    给函数增加注解

def add(x:int, y:int) -> int:
    return x+y

print(add(2,3))

# 如何查看注解？ 函数注解只存储在函数的__annotations__属性中
print(add.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}  通常使用类或者字符串来给函数添加注解
'''


'''
    返回多个值得函数（返回一个元组）,元组是通过逗号生成的，而不是小括号

def myfun():
    return 1,2,3

a,b,c = myfun()
print(a)
print(b)
print(c)
print(type(myfun()))

x = myfun()
print(x)

a = (1,2)
b = 1,2
print(a)
print(b)
'''

'''
    带有默认参数的函数，


def spam(a,b=42):
    print(a,b)

spam(1)
spam(1,2)

# 默认参数是一个可以修改的容器，比如列表，集合或者字典，可以使用None作为默认值
# 如果你不想提供默认值，而只是想测试一下某个默认参数是不是有传递进来
_no_value = object()

def spam(a,b=_no_value):
    if b is _no_value:
        print('没有提供b的值')
spam(1)



x = 42
def spam(a, b=x):
    print(a, b)

spam(1)

x = 12
spam(1)
# 默认参数的值仅在函数定义的时候赋值一次，默认值在函数定义的时候就已经确定了
# 默认参数的值应该是一个不可变的对象，None，True，False，数字或者字符串

def spam(a,b=[]):  !!!千万不要
    print(b)

    return b

x = spam(1)
print(x)

x.append(99)
x.append('abcd')
print(x)

print(spam(1))


# 为了避免默认值被设置成[],可以用如下方案代替，
def spam(a,b=None):
    if b is None:
        b = []

'''


'''
    匿名函数或内联函数

# lambda：当你的函数很简单，仅仅是计算一个表达式的值得时候，就可以用lambda来代替

# def add(x,y):
# ​	return x+y

add = lambda x, y: x+y

print(add(2, 3))
'''
# 写一个lambda表达式，把name变量中所有的字母小写，比方说 Bruce -> bruce
# def change_lower(name):
#     return name.lower()

# change_lower = lambda name:name.lower()
# print(change_lower('Bruce'))


# names = ['Danny Smith','Bruce Weier','Lily Hettings','Janny Beazley'] 使用sort排序
names = ['Danny Smith','Bruce Weier','Lily Hettings','Janny Beazley']
# 根据姓名中的姓来排序（也就是第二个单词）
# def get_lastname(names):
#     new_names = []
#     for name in names:
#         name = name.split()[-1].lower()
#         new_names.append(name)
#     return new_names

result = sorted(names,key=lambda name: name.split()[-1].lower())
print(result)

# 排序或者数据reduce是lambda的常用的地方



'''
    lambda 匿名函数捕获变量值


x = 10
fun1 = lambda y: x+y

x = 20
fun2 = lambda y: x+y


print(fun1(10)) # 30  lambda中的x是一个自由变量，在运行时绑定值

print(fun2(10))


#  可以设置成默认参数，这样就在函数定义的时候被邦定值

x = 10
fun1 = lambda y, x=x: x+y

x = 20
fun2 = lambda y, x=x: x+y

print(fun1(10))
print(fun2(10))


funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))

#  循环完后再去赋值   n = 4 
# 当做默认参数
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))

'''



'''
    将单方法的类转换为函数(除了__init__方法外只定义一个方法的类)，
    为了简化代码，可以把它转换成一个函数

from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template
    
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

xiaozhu = UrlTemplate('http://bj.xiaozhu.com/search-duanzufang-p{pages}-0/?startDate=2020-07-14&endDate=2020-07-15')
for line in xiaozhu.open(pages='10,11,12'):
    print(line.decode('utf-8'))


'''
# 这个简单的类就可以简化成函数来代替
from urllib.request import urlopen

# 闭包：函数里面套函数
def urltemplate(tempalte):
    def opener(**kwargs):
        return urlopen(tempalte.format_map(kwargs))
    return opener

xiaozhu = urltemplate('http://bj.xiaozhu.com/search-duanzufang-p{pages}-0/?startDate=2020-07-14&endDate=2020-07-15')
for line in xiaozhu(pages='10,11,12'):
    print(line.decode('utf-8'))
