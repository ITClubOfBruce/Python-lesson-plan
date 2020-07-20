'''
    csv 约等于 excel
    JSON  轻量级的数据格式，key-value，体积小，传输速度快 
    XML   <book>哈利波特</book>   体积大，传输速度稍慢 
    base64   压缩图片   5M
    txt
    html
'''


'''
    读取 csv
    涉及：去除分隔符 -> 逗号 ,去除数据的引号
'''
import csv

# list 列表
# with open('goods.csv',encoding='utf8') as f:
#     f_csv = csv.reader(f)
#     header = next(f_csv)
#     # row 是列表 row[0]  row.name
#     for row in f_csv:
#         print(row)


# namedtuple 命名元组
# from collections import namedtuple

# with open('goods.csv',encoding='utf8') as f:
#     f_csv = csv.reader(f)
#     # 获取csv 表头
#     headings = next(f_csv)
#     print(headings)
#     # 映射名称到序列元素
#     Row = namedtuple('Row', headings)
#     for r in f_csv:
#         row = Row(*r)
#         print(row.name)
#         print(row.price)



# dict 字典
# with open('goods.csv',encoding='utf8') as f:
#     f_csv = csv.DictReader(f)
#     for row in f_csv:
#         print(row['name'])
#         print(row['price'])




'''
    写入CSV
'''
# 设置表头
# headers = ['name','price']
# rows = [
#     ('橘子',400),
#     ('西瓜',500)
# ]

# with open('goods.csv','at',encoding='utf-8') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)


# 写入的数据时dict序列
# headers = ['name','price']
# rows = [
#     {
#         'name':'橘子',
#         'price':400
#     },
#     {
#         'name':'西瓜',
#         'price':500
#     }
# ]

# with open('goods.csv','wt',encoding='utf8') as f:
#     f_csv = csv.DictWriter(f,headers)
#     f_csv.writeheader()
#     f_csv.writerows(rows)


# csv文件中列数据分隔符不一定是 逗号，还可以是 \t（制表符）
with open('goods.csv','rt',encoding='utf8') as f:
    f_csv = csv.reader(f,delimiter='\t')
    for row in f_csv:
        print(row)