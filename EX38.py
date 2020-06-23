import random
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix taht.")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Gril","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Addning: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:  ",stuff)

print("Let's do some things with stuff.")
random = random.choice(stuff)
print(random)
print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool
print('#'.join(stuff[3:5])) #super stellar 注意 这里是取值索引为3到4 不包括5 等同于rang(3,5)
    