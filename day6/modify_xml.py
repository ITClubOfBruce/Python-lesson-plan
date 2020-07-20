#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   modify_xml.py
@Time    :   2020/07/17 15:52:34
@Author  :   Bruce 
@Version :   1.0
@Contact :   wangzuozheng712@aliyun.com
@License :   (C)Copyright 2020-2021, Bruce
@Desc    :   demo
'''

# here put the import lib

'''
    读取xml文档，修改后将结果写回XML文档
'''
from xml.etree.ElementTree import parse,Element

# 根节点
doc = parse('./myxml.xml')
# 得到根节点名称
root = doc.getroot()
print(root.find('h1'))
root.remove(root.find('h1'))

# 删除 remove(element)   insert(位置，element) 插入
for item in doc.iterfind('units/unit/title'):
    item.text = 'lalalalal'

doc.write('new.xml',xml_declaration=True)