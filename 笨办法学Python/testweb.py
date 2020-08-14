class Person(object):
    def __init__(self, luck):
        self.luck = luck
        #self.name = name
        #self.website = website
#
    def monkey(self):
        for myself in self.luck:
            print(myself)

xulei = Person(["Happy birthday","I love you","I hate you"])
#print(xulei.luck)
xulei.monkey()