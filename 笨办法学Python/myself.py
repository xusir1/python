from sys import argv
filename = input("输入需要重新改写的文件名：")
target = open(filename,'w')
target.truncate()

line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

target.write(f"{line1}\n {line2}\n {line3}\n")
# target.close()
target = open(filename)
print(target.read())