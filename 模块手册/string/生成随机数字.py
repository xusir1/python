import string,random
chars = string.ascii_letters
init = string.digits
sum = chars + init
print(chars)
print(init)
print(sum)


#随机密码 数字 大小写英文
passwords = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
print(passwords)