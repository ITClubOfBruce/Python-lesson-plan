import os
import sys

file_path = './students.txt'

# file = open(file_path)
# file.close()

# print(sys.getdefaultencoding())

# with open(file_path,'rt') as f:
#     print(f.read())

# with open(file_path,'wt',encoding='utf8') as f:
#     print('Hello,World',file=f)

# print('a',100,99,1000,sep=',',end='!!')


# byte1 = b"ABCDEFGHIJKLMNOP"
# for c in byte1:
#     print(c)\


# with open('./students.bin','wb') as f:
#     text = '1903C'
#     text = text.encode('utf-8')
#     f.write(text)

# with open('./students.bin','rb') as f:
#     data = f.read()
#     data = data.decode('utf-8')
#     print(data)



# with open('./students.txt','xt') as f:
#     f.write('Hello\n')

# import io

# s = io.StringIO('193okfdojfie')
# # s.write('hello1903C')
# # print(s.getvalue())
# print(s.read(4))

# s1 = io.BytesIO()
# s1.write(b'binary data')
# print(s1.getvalue())


import gzip, bz2

# with gzip.open('./students.gz','rt',encoding='utf8') as f:
#     text = f.read()
#     print(text)

# with bz2.open('./students.bz2','rt',encoding='utf8') as f:
#     text = f.read()
#     print(text)


with gzip.open('./students.gz', 'wt', encoding='utf8') as f:
    f.write('Hello')

with gzip.open('./students.gz', 'rt', encoding='utf8') as f:
    text = f.read()
    print(text)

# with bz2.open('./students.bz2','wt',encoding='utf8') as f:
#     f.write('Hello')

