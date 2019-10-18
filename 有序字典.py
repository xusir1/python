# 字典按照添加顺序排序
#import collections
#a = {"C":"c", "B": "b", "A":"a", "Z":"z"}
#b = collections.OrderedDict(a)

#print(b)

c = {'a':5, 'c':3,'b':4}
d = sorted(c.items(),key=lambda x:x[0])
print(d)
