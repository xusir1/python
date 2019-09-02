# -*- coding: utf-8 -*- 
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line,how?
#in_file = open(from_file)
#indata = in_file.read()
with open(from_file) as f:
    indata = f.read()


print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist ? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to about.")
print(f"{indata}")
input()

with open(to_file, 'w+') as out_file:
    out_file.write(indata)
#out_file = open(to_file, 'w+')
#out_file.write(indata)
#out_file.close()
#out_file = open(to_file, 'r')

print("Alright, all done .")

#out_file.close()
#in_file.close()
out_file = open(to_file, 'r+')
print(out_file.read())