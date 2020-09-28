import string,random
s=string.hexdigits[0:10] + string.hexdigits[16:22]
def randomcolor():
    colorArr = [c for c in s]
    color = ''
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color
for i in range(10):
    print(randomcolor())