class Parent(object):
    def override(self):
        print("PARRENT override()")
    
    def implicit(self,a):
        print(f"PARENT imlicit() {a} ")

    def altered(self):
        print("PARENT altered")

class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()
#隐式继承
dad.implicit(2)
son.implicit(2)


#显示覆盖
dad.override()
son.override()

#运行前后替换
dad.altered()
son.altered()