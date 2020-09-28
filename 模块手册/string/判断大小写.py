import string
def check(value):
    for letter in value:
        if letter not in string.ascii_lowercase:
            return False
    return True
myval = input("请输入小写字母： ")
print(check(myval))
if check(myval) == False:
    print("请输入小写！")