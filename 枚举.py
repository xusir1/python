list1 = ("这","是","一个","列表")
for i in range (len(list1)):
    print(i,list1[i])
#a = len(list)
#print(a)

list2 = ("这","是","一个","列表")
for index,item in enumerate(list2,0):
    print(index,item)

dir1 = {'china': 'beijing', 'janpan': 'dongjing', 'usa': 'huashengdun'}
for state, abbrev in list(dir1.items()):
    print(f"{state} has city {abbrev}")