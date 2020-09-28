import string
def tel(num):
    for i in num:
        if i not in string.digits:
            return False
    if len(num) != 11:
        return False
    if num[0] == '0':
        return False
    return True
while 1:
    myval=input("请输入手机号 ")
    print(tel(myval))