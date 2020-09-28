import string
f = open('模块手册\string\过滤数字.txt','r')
s=f.read()
for c in string.digits:
    print(c)
    s=s.replace(c,'')
print(s)