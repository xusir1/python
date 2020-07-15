class A:
    def add(self,x):
        y = x+1
        print(y)

class B(A):
    def add(self,x):
        super().add(x)

b = B()
b.add(2)




#spuer()和__init__搭配使用
class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        spuer(Child,self).__init__()