import random,string
a=''.join(random.sample(string.hexdigits[:-6],3))
print(a)