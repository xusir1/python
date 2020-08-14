from sys import argv
# read the WYSS section for how to run this
script,frist,second,third = argv

print("The script is called:",script)
print("Your first variable is:",frist)
print("Your second variable is:",second)
print("Your third variable is:",third)
print("How old are you:",end="")
old = input()
print(f"you are {frist} years old")