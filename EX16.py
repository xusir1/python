from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C) .")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file....")
target = open(filename,'w')

print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3 : ")

print("I'm going to write these to file.")

#target.write(f"{line1}\n {line2}\n {line3}\n")
target.write("{line1}\n {line2}\n {line3}\n".format(line1=line1,line2=line2,line3=line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()

print("Type the filename again:")

file_name = input("filename:")
with open(file_name) as f:
    print(f.read()) 

# new_file = open(input("filename:"))
# print(new_file.read())
new_file.close()