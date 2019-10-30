class Person:
    def __init__(self, name, lang, website):
        self.name = name
        self.lang = lang
        self.website = website

info = Person("hiekay","python","hiekay.github.io")     #实例化Person
print(info.name)
print(info.lang)
print(info.website)