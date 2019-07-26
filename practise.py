def right_justify(s):
    ab = " " * 69 + s
    return ab
b = input("please edit a number: ")
new = right_justify(b)
print(new) 
print(len(new))