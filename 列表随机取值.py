import random
list1 = ['佛山', '南宁', '北海', '杭州', '南昌', '厦门', '温州']
a = random.choice(list1) 
d = random.choice(list1)
print(a)
print(d)
b = random.sample(list1, 1)
c = random.sample(list1, 3)
print(b)
print(c)