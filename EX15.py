from sys import argv  #import mudule

script, filename = argv   # transmit variable

txt = open(filename)    #obtain file name transmit to txt variable

print(f"Here's your file {filename}:")
print(txt.read())       #print txt content

print("Type the filename again:")   #obtain the name content again
file_again = input(">")             #user designated the filename

txt_again = open(file_again)    #obtain new file content to txt_again

print(txt_again.read())     #print txt_again