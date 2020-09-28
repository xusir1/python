import random,string
def IDstr(num1):
    f = open('模块手册/string/激活码.txt','w')
    for i in range(num1):
        chars = string.ascii_letters + string.digits
        s = [random.choice(chars) for i in range(8)]
        f.write('{0}\n'.format(''.join(s)))
    f.close

IDstr(2)