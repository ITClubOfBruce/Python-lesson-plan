前言：

​	Python中的内容：Python中的数据结构与算法，字符串和文本操作，函数，文件与IO操作；

​	程序是由  数据结构 + 算法

​	第三方库：re库，re.sub(); 

​						os模块 open()    exists 



## 一、文件与IO操作

**一**、学生管理系统中，输入输出的是：文本；输入输出格式中还可以是二进制文件，windows上的换行符是\r\n，Unix上的换行符是\n，Python可以识别普通换行符，并且转换成单个\n字符，如果你不希望这种默认的处理方式，可以给open()函数传入参数 newline=''

1. 读写文本数据

   open(path)，打开文件，如果文件中有中文，需要将文件格式设置为gbk才可以

2. rt，wt，at

   rt 读取文本文件

   wt 写入一个文本文件，如果之前文件内容存在则清除并且覆盖掉

   at 在已经存在的文件中添加内容

3. 文件的读写操作默认使用的系统编码，使用sys.getdefaultencoding()可以得到

4. encoding='utf8'  errors = 'ignore'  忽略错误，errors = 'replace'  替换错误的字符串，



**二**、打印输出到文件中

1. 使用print()  函数的输出重定向到一个文件中去，必须是文本模式



**三、**使用分隔符或行终止符打印

1. 使用print()函数输出数据，但是想改变默认的分割符或者行尾符

   print('a',50,30,10)

   print('a',100,99,1000,sep=',',end='!!')

   

**四、**读写字节数据 img，视频，音频（编解码）这些都是二进制文件  播放器（编解码软件）

使用模式为rb  wb的open()函数来读取或写入二进制数据

二进制文件后缀名是：.bin

```python
byte1 = b"ABCDEFGHIJKLMNOP"
for c in byte1:
    print(c)
```

 

从二进制模式的文件中读取或写入文本数据，必须要进行编码和解码操作

```python
with open('./students.bin','wb') as f:
    text = '1903C'
    text = text.encode('utf-8')
    f.write(text)

with open('./students.bin','rb') as f:
    data = f.read()
    data = data.decode('utf-8')
    print(data)
```





**五、**run.log 不确定是不是之前有人写过这个run.log的文件，不能覆盖掉之前的run.log文件

```python
with open('./students.txt','xt') as f:
    f.write('Hello\n')
    
    
替换  os.path.exists()
```





**六、**使用操作类文件对象的程序来操作文本或二进制字符串

io.StringIO()

io.BytesIO()

```python
import io

# s = io.StringIO('193okfdojfie')
# # s.write('hello1903C')
# # print(s.getvalue())
# print(s.read(4))

s1 = io.BytesIO()
s1.write(b'binary data')
print(s1.getvalue())
```



在单元测试中，可以使用StringIO来创建一个包含测试数据的类文件对象，这个对象可以被传给某个参数为普通文件对象的函数



**七、**读写压缩文件

第三方模块：shutil

读写一个gzip或者bz2，使用Python中自带的gzip和bz2

1. 以文本的方式读取压缩文件

   ```python
   with gzip.open('./students.gz','rt',encoding='utf8') as f:
       text = f.read()
       print(text)
   
   with bz2.open('./students.bz2','rt',encoding='utf8') as f:
       text = f.read()
       print(text)
   ```

   

2. 以文本的方式写入压缩文件

   ```python
   
   with gzip.open('./students.gz','wt',encoding='utf8') as f:
       f.write('Hello')
   
   with gzip.open('./students.gz','rt',encoding='utf8') as f:
       text = f.read()
       print(text)
   
   # with bz2.open('./students.bz2','wt',encoding='utf8') as f:
   #     f.write('Hello')
   ```





## 二、函数

1. 可接受任意数量参数的函数

   

2. 只接受关键字参数的函数(只接受dict类型参数的函数)

   

3. 给函数参数增加元信息

   给自己写的函数增加一些额外信息，比如：这个函数的作用，参数等等

   增加注解

4. 返回多个值的函数

   return一个元组

5. 定义有默认参数的函数

   

6. 定义匿名或内联函数

   lambda：当你的函数很简单，仅仅是计算一个表达式的值得时候，就可以用lambda来代替

   def add(x,y):

   ​	return x+y

   add = lambda x,y :x+y

   

7. 匿名函数捕获变量值

   

8. 减少可调用对象的参数个

   

9. 将单方法的类转换为函数

   

10. 带额外状态信息的回调函数

11. 内联回调函数

12. 访问闭包中定义的变量





















