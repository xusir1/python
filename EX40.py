class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song([ "Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

class Person:
    def __init__(self, luck, name, website):
        self.luck = luck
        self.name = name
        self.website = website
#
#    def monkey(self):
#        for myself in self.luck:
#            print(myself)

xulei = Person("Happy birthday","I love you","I hate you")
print(xulei.luck)
print(xulei.name)
print(xulei.website)
#xulei.monkey()
#info.luck
#info.name
#info.website