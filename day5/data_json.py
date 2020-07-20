'''
    json模块提供了一种很简单的方式来编码和解码JSON数据。
    其中两个主要的函数式json.dumps() 和 json.loads()，相对于其他序列化函数库接口少了很多
'''
import json

data = {
    'name':'西瓜',
    'weight':10,
    'price':100
}

json_str = json.dumps(data)

# 把json_str转换成Python中的数据结构
data = json.loads(json_str)




# 如果处理的是文件而不是字符串中的数据，json.dump()   json.load()

# with open('data_json.json','r') as f:
#     data = json.load(f)
#     print(data)

# with open('data_json.json','at',encoding='utf8') as f:
#     json.dump(data,f)




# JSON编码支持的基本数据类型None，bool，int，float，str
# 和包含以上基本类型的 lists tuples dictionaries；
# 为了遵循JSON规范，只能编码Python中的lists和dictionnaries
# 在web应用程序中，顶层对象被编码成一个字典是标准
# User.objects.all()  object
# dict list
# json.dumps(False)


# from urllib.request import urlopen
# import json
# from pprint import pprint

# # 天津天气的接口，返回json格式的数据
# url = urlopen('http://t.weather.sojson.com/api/weather/city/101030100')
# data = url.read().decode('utf-8')
# # 把网络上的json数据转换成Python中的数据结构
# resp = json.loads(data)

# print(resp)
# pprint(resp)



# 默认JSON解码会根据提供的数据创建dicts或者lists
# 如果你想要创建其他类型的对象，可以给json.loads()传参：object_pairs_hook或者object_hook

# 比如，你想解码后的数据时OrderDict类型
# s = '{"name":"西瓜","price":100}'
# from collections import OrderedDict
# data = json.loads(s,object_pairs_hook=OrderedDict)
# print(data)

# JSON 数据解码后变成python中的class
# class JSONObject:
#     def __init__(self,d):
#         # 每个类的类变量。函数名都会放在自己的__dict__中
#         self.__dict__ = d
        
# data = json.loads(s,object_hook=JSONObject)
# print(data)
# print(data.name)
# print(data.price)


# json.dumps的indent参数,美化输出
# data = {
#     "name":"西瓜",
#     "price":100
# }

# print(json.dumps(data))

# print(json.dumps(data,indent=4))



#  能不能把Python中的对象编码成json？  不能直接转换
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

p = Point(2,3)
# json.dumps(p)
# TypeError: Object of type Point is not JSON serializable 


'''
    序列化
'''
# DRF 可以实现编码一个对象，原理？自己实现了一个函数serialize
def serialize_instance(obj):
    d = {
        '__classname__':type(obj).__name__
    }
    # vars 函数返回对象object的属性和属性值 
    d.update(vars(obj))
    return d

s = json.dumps(p,default=serialize_instance)
print(s)


'''
    反序列化   把json - > object
    解码
'''
classes = {
    'Point':Point
}
def unserialize_object(d):
    class_name = d.pop('__classname__',None)
    if class_name:
        cls = classes[class_name]
        obj = cls.__new__(cls)
        for key,value in d.items():
            setattr(obj,key,value)
        return obj
    else:
        return d


a = json.loads(s,object_hook=unserialize_object)
print(a)
print(a.x)
print(a.y)